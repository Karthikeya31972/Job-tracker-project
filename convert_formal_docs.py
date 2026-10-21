#!/usr/bin/env python3
"""
Convert formal project documentation to PDF
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
import re

def markdown_to_pdf(input_file, output_file):
    """Convert Markdown to PDF using ReportLab"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=1*inch,
        leftMargin=1*inch,
        topMargin=1*inch,
        bottomMargin=1*inch
    )
    
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=12,
        textColor=colors.HexColor('#1a1a1a'),
        alignment=TA_CENTER,
        fontName='Times-Bold'
    )
    
    # Main heading style
    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontSize=14,
        spaceAfter=10,
        spaceBefore=16,
        textColor=colors.HexColor('#000080'),
        alignment=TA_CENTER,
        fontName='Times-Bold'
    )
    
    # Section heading style
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=8,
        spaceBefore=12,
        textColor=colors.HexColor('#000000'),
        fontName='Times-Bold'
    )
    
    # Subsection style
    h3_style = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading3'],
        fontSize=11,
        spaceAfter=6,
        spaceBefore=10,
        textColor=colors.HexColor('#000000'),
        fontName='Times-Bold'
    )
    
    # Body style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        spaceAfter=6,
        leading=14,
        fontName='Times-Roman',
        alignment=TA_JUSTIFY
    )
    
    # Code style
    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=8,
        fontName='Courier',
        textColor=colors.HexColor('#333'),
        backColor=colors.HexColor('#f5f5f5'),
        leftIndent=20,
        spaceAfter=6
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['BodyText'],
        fontSize=10,
        leftIndent=30,
        spaceAfter=4,
        bulletIndent=15,
        fontName='Times-Roman'
    )
    
    # Table cell style
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Times-Bold',
        alignment=TA_CENTER
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=9,
        fontName='Times-Roman',
        alignment=TA_LEFT
    )
    
    story = []
    lines = content.split('\n')
    
    in_code_block = False
    code_lines = []
    in_table = False
    table_data = []
    
    for line in lines:
        # Handle code blocks
        if line.startswith('```'):
            if in_code_block:
                code_text = '<br/>'.join(code_lines)
                story.append(Paragraph(code_text, code_style))
                story.append(Spacer(1, 6))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            continue
        
        if in_code_block:
            escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            code_lines.append(escaped if escaped else ' ')
            continue
        
        # Skip HTML-like content
        if line.strip().startswith('<') and line.strip().endswith('>'):
            continue
        
        # Page break marker
        if line.strip() == '---' and len(line.strip()) == 3:
            story.append(PageBreak())
            continue
        
        # Headers
        if line.startswith('# ') and not line.startswith('## '):
            text = line[2:].strip()
            story.append(Paragraph(text, title_style))
        elif line.startswith('## '):
            text = line[3:].strip()
            story.append(Paragraph(text, h2_style))
        elif line.startswith('### '):
            text = line[4:].strip()
            story.append(Paragraph(text, h3_style))
        elif line.startswith('#### '):
            text = line[5:].strip()
            story.append(Paragraph(text, h3_style))
        
        # Table rows
        elif line.startswith('|') and '|' in line[1:]:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells and not all(c.replace('-', '') == '' for c in cells):
                table_data.append(cells)
        
        # List items
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            text = process_inline(text)
            story.append(Paragraph(f'• {text}', bullet_style))
        
        # Numbered list
        elif re.match(r'^\d+\.', line.strip()):
            text = re.sub(r'^\d+\.', '', line.strip()).strip()
            text = process_inline(text)
            story.append(Paragraph(text, bullet_style))
        
        # Empty lines
        elif not line.strip():
            if table_data:
                # Create table
                if len(table_data) > 0:
                    table = Table(table_data, repeatRows=1)
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 9),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),
                        ('FONTSIZE', (0, 1), (-1, -1), 9),
                        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ]))
                    story.append(table)
                    story.append(Spacer(1, 10))
                table_data = []
            story.append(Spacer(1, 6))
        
        # Regular paragraphs
        else:
            if table_data:
                # Create table before paragraph
                if len(table_data) > 0:
                    table = Table(table_data, repeatRows=1)
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 9),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),
                        ('FONTSIZE', (0, 1), (-1, -1), 9),
                        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ]))
                    story.append(table)
                    story.append(Spacer(1, 10))
                table_data = []
            
            text = process_inline(line)
            story.append(Paragraph(text, body_style))
    
    # Handle remaining table
    if table_data:
        table = Table(table_data, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(table)
    
    doc.build(story)
    print(f"✅ Created PDF: {output_file}")

def process_inline(text):
    """Process inline formatting"""
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = re.sub(r'`(.*?)`', r'<font face="Courier" size="9">\1</font>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    return text

if __name__ == "__main__":
    markdown_to_pdf(
        'PROJECT_DOCUMENTATION_FORMAL.md',
        'Project_Documentation_Formal.pdf'
    )
    print("\n📄 Formal project documentation PDF created!")
