#!/usr/bin/env python3
"""
Simple Markdown to PDF converter using ReportLab
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
import re
import os

def markdown_to_pdf(input_file, output_file):
    """Convert Markdown to PDF using ReportLab"""
    
    # Read markdown content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=1*inch,
        leftMargin=1*inch,
        topMargin=1*inch,
        bottomMargin=1*inch
    )
    
    # Create custom styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.HexColor('#1a1a1a'),
        alignment=TA_CENTER,
        fontName='Times-Bold'
    )
    
    # Heading 1 style
    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12,
        spaceBefore=20,
        textColor=colors.HexColor('#2a2a2a'),
        fontName='Times-Bold'
    )
    
    # Heading 2 style
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=10,
        spaceBefore=15,
        textColor=colors.HexColor('#3a3a3a'),
        fontName='Times-Bold'
    )
    
    # Heading 3 style
    h3_style = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=8,
        spaceBefore=12,
        textColor=colors.HexColor('#4a4a4a'),
        fontName='Times-Bold'
    )
    
    # Body style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        spaceAfter=8,
        leading=16,
        fontName='Times-Roman'
    )
    
    # Code style
    code_style = ParagraphStyle(
        'CustomCode',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        textColor=colors.HexColor('#333'),
        backColor=colors.HexColor('#f4f4f4'),
        leftIndent=20,
        spaceAfter=8
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['BodyText'],
        fontSize=11,
        leftIndent=30,
        spaceAfter=4,
        bulletIndent=15,
        fontName='Times-Roman'
    )
    
    # Process markdown
    story = []
    lines = content.split('\n')
    
    in_code_block = False
    code_lines = []
    
    for line in lines:
        # Check for code blocks
        if line.startswith('```'):
            if in_code_block:
                # End of code block
                code_text = '<br/>'.join(code_lines)
                story.append(Paragraph(code_text, code_style))
                story.append(Spacer(1, 8))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            continue
        
        if in_code_block:
            # Escape special HTML characters
            escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            code_lines.append(escaped if escaped else ' ')
            continue
        
        # Skip HTML tags
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
        
        # Horizontal rule
        elif line.strip() == '---' or line.strip() == '***':
            story.append(Spacer(1, 20))
        
        # List items
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            text = process_inline_formatting(text)
            story.append(Paragraph(f'• {text}', bullet_style))
        
        # Numbered list
        elif re.match(r'^\d+\.', line.strip()):
            text = re.sub(r'^\d+\.', '', line.strip()).strip()
            text = process_inline_formatting(text)
            story.append(Paragraph(text, bullet_style))
        
        # Empty lines
        elif not line.strip():
            story.append(Spacer(1, 8))
        
        # Regular paragraphs
        else:
            text = process_inline_formatting(line)
            story.append(Paragraph(text, body_style))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Created PDF: {output_file}")

def process_inline_formatting(text):
    """Process inline markdown formatting"""
    # First escape any existing HTML special chars
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    
    # Code: `text` - process first to avoid conflicts
    text = re.sub(r'`(.*?)`', r'<font face="Courier" size="9">\1</font>', text)
    
    # Bold: **text** or __text__
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.*?)__', r'<b>\1</b>', text)
    
    # Italic: *text* or _text_
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    
    # Links: [text](url) -> just show text
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    
    return text

def convert_presentation_notes():
    """Convert the presentation markdown to PDF"""
    md_file = "PRESENTATION_SLIDES.md"
    if os.path.exists(md_file):
        print(f"\n📊 Converting Presentation: {md_file}")
        markdown_to_pdf(md_file, "Job_Tracking_System_Presentation.pdf")
    else:
        print(f"⚠️  {md_file} not found")

def convert_documentation():
    """Convert project documentation to PDF"""
    md_file = "PROJECT_DOCUMENTATION.md"
    if os.path.exists(md_file):
        print(f"\n📄 Converting Documentation: {md_file}")
        markdown_to_pdf(md_file, "Project_Documentation.pdf")
    else:
        print(f"⚠️  {md_file} not found")

def convert_core_modules():
    """Convert core modules explanation to PDF"""
    md_file = "core_modules_explanation.md"
    if os.path.exists(md_file):
        print(f"\n📦 Converting Core Modules: {md_file}")
        markdown_to_pdf(md_file, "Core_Modules_Explanation.pdf")
    else:
        print(f"⚠️  {md_file} not found")

def main():
    print("=" * 60)
    print("CONVERTING MARKDOWN FILES TO PDF")
    print("=" * 60)
    
    convert_presentation_notes()
    convert_documentation()
    convert_core_modules()
    
    print("\n" + "=" * 60)
    print("CONVERSION COMPLETE")
    print("=" * 60)
    
    # List generated PDFs
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    if pdf_files:
        print("\n📁 Generated PDF files:")
        for pdf in pdf_files:
            size = os.path.getsize(pdf) / 1024
            print(f"   • {pdf} ({size:.1f} KB)")
    
    print("\n⚠️  Note: PPTX files need PowerPoint or LibreOffice to convert to PDF")
    print("   Open the PPTX file in PowerPoint → File → Save As → PDF")

if __name__ == "__main__":
    main()
