#!/usr/bin/env python3
"""
Convert PPTX Presentation and Markdown Documentation to PDF
"""

import subprocess
import sys
import os

def markdown_to_pdf(input_file, output_file):
    """Convert Markdown to PDF using pandoc"""
    try:
        # Try using pandoc first (best quality)
        cmd = [
            'pandoc',
            input_file,
            '-o', output_file,
            '--pdf-engine=xelatex',
            '-V', 'geometry:margin=1in',
            '-V', 'fontsize=11pt',
            '--toc'
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Created: {output_file}")
            return True
        else:
            print(f"Pandoc error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("Pandoc not found. Trying alternative method...")
        return markdown_to_pdf_alternative(input_file, output_file)

def markdown_to_pdf_alternative(input_file, output_file):
    """Alternative: Convert Markdown to HTML, then print to PDF"""
    try:
        import markdown
        from weasyprint import HTML, CSS
        
        # Read markdown
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert to HTML
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        
        # Add styling
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: 'Times New Roman', Times, serif;
                    font-size: 11pt;
                    line-height: 1.6;
                    margin: 1in;
                    color: #333;
                }}
                h1 {{
                    font-size: 24pt;
                    color: #1a1a1a;
                    border-bottom: 2px solid #333;
                    padding-bottom: 10px;
                }}
                h2 {{
                    font-size: 18pt;
                    color: #2a2a2a;
                    margin-top: 24pt;
                }}
                h3 {{
                    font-size: 14pt;
                    color: #3a3a3a;
                }}
                code {{
                    font-family: Consolas, Monaco, monospace;
                    background: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                }}
                pre {{
                    background: #f4f4f4;
                    padding: 12px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 15px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background: #f0f0f0;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Convert to PDF
        HTML(string=full_html).write_pdf(output_file)
        print(f"✅ Created: {output_file}")
        return True
        
    except ImportError:
        print("weasyprint not installed. Trying reportlab...")
        return markdown_to_pdf_reportlab(input_file, output_file)

def markdown_to_pdf_reportlab(input_file, output_file):
    """Last resort: Use reportlab for simple PDF generation"""
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib import colors
        import re
        
        # Read markdown
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create PDF
        doc = SimpleDocTemplate(output_file, pagesize=letter,
                                rightMargin=1*inch, leftMargin=1*inch,
                                topMargin=1*inch, bottomMargin=1*inch)
        
        styles = getSampleStyleSheet()
        story = []
        
        # Simple parsing (basic)
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                story.append(Paragraph(line[2:], styles['Title']))
                story.append(Spacer(1, 12))
            elif line.startswith('## '):
                story.append(Paragraph(line[3:], styles['Heading1']))
                story.append(Spacer(1, 6))
            elif line.startswith('### '):
                story.append(Paragraph(line[4:], styles['Heading2']))
                story.append(Spacer(1, 6))
            elif line.startswith('- '):
                story.append(Paragraph('• ' + line[2:], styles['BodyText']))
            elif line.strip():
                story.append(Paragraph(line, styles['BodyText']))
        
        doc.build(story)
        print(f"✅ Created: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to convert markdown: {e}")
        return False

def pptx_to_pdf_windows(input_file, output_file):
    """Convert PPTX to PDF using PowerPoint COM on Windows"""
    try:
        import win32com.client
        
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        powerpoint.Visible = False
        
        abs_input = os.path.abspath(input_file)
        abs_output = os.path.abspath(output_file)
        
        presentation = powerpoint.Presentations.Open(abs_input)
        presentation.SaveAs(abs_output, 32)  # 32 = PDF format
        presentation.Close()
        powerpoint.Quit()
        
        print(f"✅ Created: {output_file}")
        return True
        
    except ImportError:
        print("win32com not available. Trying LibreOffice...")
        return pptx_to_pdf_libreoffice(input_file, output_file)
    except Exception as e:
        print(f"PowerPoint COM error: {e}")
        return pptx_to_pdf_libreoffice(input_file, output_file)

def pptx_to_pdf_libreoffice(input_file, output_file):
    """Convert PPTX to PDF using LibreOffice"""
    try:
        cmd = [
            'soffice',
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', os.path.dirname(os.path.abspath(output_file)),
            os.path.abspath(input_file)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            # Rename to desired output name
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            generated_pdf = os.path.join(os.path.dirname(os.path.abspath(output_file)), base_name + '.pdf')
            if os.path.exists(generated_pdf):
                if generated_pdf != os.path.abspath(output_file):
                    os.rename(generated_pdf, output_file)
                print(f"✅ Created: {output_file}")
                return True
        print(f"LibreOffice error: {result.stderr}")
        return False
    except FileNotFoundError:
        print("LibreOffice not found (soffice command missing)")
        return False
    except Exception as e:
        print(f"LibreOffice error: {e}")
        return False

def main():
    print("=" * 60)
    print("CONVERTING PRESENTATION AND DOCUMENTATION TO PDF")
    print("=" * 60)
    
    # Define files
    pptx_file = "Job_Tracking_System_TimesRoman.pptx"  # Use the Times Roman version
    md_file = "PROJECT_DOCUMENTATION.md"
    
    # Check which files exist
    pptx_exists = os.path.exists(pptx_file)
    md_exists = os.path.exists(md_file)
    
    if not pptx_exists:
        # Try other PPTX files
        alternatives = [
            "Job_Tracking_System_Enhanced_Final.pptx",
            "Job_Tracking_System_Simple.pptx",
            "Job_Tracking_System_Presentation.pptx"
        ]
        for alt in alternatives:
            if os.path.exists(alt):
                pptx_file = alt
                pptx_exists = True
                print(f"Using alternative PPTX: {alt}")
                break
    
    # Convert PPTX to PDF
    if pptx_exists:
        print(f"\n📊 Converting presentation: {pptx_file}")
        pdf_output = os.path.splitext(pptx_file)[0] + ".pdf"
        if not pptx_to_pdf_windows(pptx_file, pdf_output):
            print("⚠️  PPTX to PDF conversion failed.")
            print("   Manual method: Open the PPTX in PowerPoint → File → Save As → PDF")
    else:
        print("\n⚠️  No PPTX file found for conversion")
    
    # Convert Markdown to PDF
    if md_exists:
        print(f"\n📄 Converting documentation: {md_file}")
        pdf_output = "Project_Documentation.pdf"
        markdown_to_pdf(md_file, pdf_output)
    else:
        print(f"\n⚠️  {md_file} not found")
    
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
    else:
        print("\n⚠️  No PDF files were generated")
        print("\nAlternative methods:")
        print("1. For PPTX: Open in PowerPoint → File → Save As → PDF")
        print("2. For Markdown: Use online converter like md2pdf.netlify.app")

if __name__ == "__main__":
    main()
