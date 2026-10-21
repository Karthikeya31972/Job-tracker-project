#!/usr/bin/env python3
"""
Convert Big Data exam notes to PDF
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
import re

def markdown_to_pdf(input_file, output_file):
    """Convert Markdown to PDF using ReportLab"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=0.8*inch,
        leftMargin=0.8*inch,
        topMargin=0.8*inch,
        bottomMargin=0.8*inch
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        textColor=colors.HexColor('#1a1a1a'),
        alignment=TA_CENTER,
        fontName='Times-Bold'
    )
    
    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontSize=14,
        spaceAfter=10,
        spaceBefore=15,
        textColor=colors.HexColor('#0d47a1'),
        fontName='Times-Bold'
    )
    
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=12,
        spaceAfter=8,
        spaceBefore=12,
        textColor=colors.HexColor('#1565c0'),
        fontName='Times-Bold'
    )
    
    h3_style = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading3'],
        fontSize=11,
        spaceAfter=6,
        spaceBefore=10,
        textColor=colors.HexColor('#1976d2'),
        fontName='Times-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=9,
        spaceAfter=4,
        leading=12,
        fontName='Times-Roman'
    )
    
    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=8,
        fontName='Courier',
        textColor=colors.HexColor('#333'),
        backColor=colors.HexColor('#f5f5f5'),
        leftIndent=15,
        spaceAfter=4
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['BodyText'],
        fontSize=9,
        leftIndent=20,
        spaceAfter=3,
        bulletIndent=10,
        fontName='Times-Roman'
    )
    
    story = []
    lines = content.split('\n')
    
    in_code_block = False
    code_lines = []
    
    for line in lines:
        if line.startswith('```'):
            if in_code_block:
                code_text = '<br/>'.join(code_lines)
                story.append(Paragraph(code_text, code_style))
                story.append(Spacer(1, 4))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            continue
        
        if in_code_block:
            escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            code_lines.append(escaped if escaped else ' ')
            continue
        
        if line.strip().startswith('<') and line.strip().endswith('>'):
            continue
        
        # Headers
        if line.startswith('# '):
            text = line[2:].strip()
            story.append(Paragraph(text, title_style))
        elif line.startswith('## '):
            text = line[3:].strip()
            story.append(Paragraph(text, h1_style))
        elif line.startswith('### '):
            text = line[4:].strip()
            story.append(Paragraph(text, h2_style))
        elif line.startswith('#### '):
            text = line[5:].strip()
            story.append(Paragraph(text, h3_style))
        elif line.strip() == '---' or line.strip() == '***':
            story.append(Spacer(1, 10))
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            text = process_inline(text)
            story.append(Paragraph(f'• {text}', bullet_style))
        elif re.match(r'^\d+\.', line.strip()):
            text = re.sub(r'^\d+\.', '', line.strip()).strip()
            text = process_inline(text)
            story.append(Paragraph(text, bullet_style))
        elif not line.strip():
            story.append(Spacer(1, 4))
        else:
            text = process_inline(line)
            story.append(Paragraph(text, body_style))
    
    doc.build(story)
    print(f"✅ Created PDF: {output_file}")

def process_inline(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = re.sub(r'`(.*?)`', r'<font face="Courier" size="8">\1</font>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<b>\1</b>', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    return text

if __name__ == "__main__":
    markdown_to_pdf(
        'Cassandra_Hive_Exam_Notes.md',
        'Cassandra_Hive_Exam_Notes.pdf'
    )
    print("\n📚 Exam notes PDF created successfully!")
