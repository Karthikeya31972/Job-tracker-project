#!/usr/bin/env python3
"""
Enhanced Markdown to PowerPoint Converter
Features: Gradients, visual diagrams, section dividers, two-column layouts
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import nsmap
from pptx.oxml import parse_xml

# Color scheme
PRIMARY_DARK = RGBColor(15, 23, 42)      # Dark blue-black
PRIMARY = RGBColor(37, 99, 235)           # Bright blue
PRIMARY_LIGHT = RGBColor(96, 165, 250)      # Light blue
ACCENT = RGBColor(245, 158, 11)           # Amber/orange accent
WHITE = RGBColor(255, 255, 255)
LIGHT_GRAY = RGBColor(248, 250, 252)
DARK_TEXT = RGBColor(30, 41, 59)
MUTED_TEXT = RGBColor(100, 116, 139)

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_gradient_background(slide, prs, color1, color2):
    """Add gradient background using multiple shapes"""
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = color1
    bg.line.fill.background()
    bg.z_order = 0
    return bg

def add_title_slide(prs, title, subtitle, date="April 2026"):
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Gradient background effect (solid for now - pptx doesn't support true gradients easily)
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = PRIMARY_DARK
    bg.line.fill.background()
    
    # Decorative accent bar at top
    accent_bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.15)
    )
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = ACCENT
    accent_bar.line.fill.background()
    
    # Small decorative circles
    for x, y, size in [(Inches(11), Inches(1), Inches(1.5)), 
                       (Inches(12), Inches(5), Inches(2)),
                       (Inches(0.5), Inches(6), Inches(1))]:
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, size, size)
        circle.fill.solid()
        circle.fill.fore_color.rgb = PRIMARY
        circle.fill.fore_color.brightness = 0.3
        circle.line.fill.background()
    
    # Main title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(11.7), Inches(1.2))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(60)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = "Calibri Light"
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(28)
        p2.font.color.rgb = PRIMARY_LIGHT
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(12)
    
    # Tech stack badge
    badge = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.5), Inches(4.5), Inches(6.333), Inches(0.6)
    )
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 41, 59)
    badge.line.color.rgb = PRIMARY
    badge.line.width = Pt(2)
    
    badge_text = slide.shapes.add_textbox(Inches(3.5), Inches(4.55), Inches(6.333), Inches(0.5))
    tf = badge_text.text_frame
    p = tf.paragraphs[0]
    p.text = "⚡ React 19 • Node.js • Express • MongoDB Atlas"
    p.font.size = Pt(18)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Date
    date_box = slide.shapes.add_textbox(Inches(0.5), Inches(6.8), Inches(12.333), Inches(0.4))
    tf = date_box.text_frame
    p = tf.paragraphs[0]
    p.text = f"Presented by: [Your Name]  •  {date}"
    p.font.size = Pt(14)
    p.font.color.rgb = MUTED_TEXT
    p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_section_divider(prs, section_number, section_title):
    """Add a section divider slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Background
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = PRIMARY
    bg.line.fill.background()
    
    # Large section number
    num_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(3), Inches(2))
    tf = num_box.text_frame
    p = tf.paragraphs[0]
    p.text = f"0{section_number}" if section_number < 10 else str(section_number)
    p.font.size = Pt(120)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.font.color.brightness = -0.2
    
    # Section title
    title_box = slide.shapes.add_textbox(Inches(4), Inches(2.8), Inches(8.5), Inches(1))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = section_title
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    return slide

def add_two_column_slide(prs, title, left_title, left_items, right_title, right_items):
    """Add a slide with two columns"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Light background
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = LIGHT_GRAY
    bg.line.fill.background()
    
    # Modern header
    header = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1)
    )
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY_DARK
    header.line.fill.background()
    
    # Accent line
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(1.08), prs.slide_width, Inches(0.05)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.3), Inches(12), Inches(0.6))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Left column title
    left_title_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.4), Inches(6), Inches(0.5))
    tf = left_title_box.text_frame
    p = tf.paragraphs[0]
    p.text = f"● {left_title}"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    
    # Left column content
    left_box = slide.shapes.add_textbox(Inches(0.6), Inches(1.95), Inches(5.8), Inches(5))
    tf = left_box.text_frame
    tf.word_wrap = True
    
    first = True
    for item in left_items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        
        if item.startswith('- '):
            p.text = "▸ " + item[2:]
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(8)
        else:
            p.text = item
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_TEXT
    
    # Divider line
    divider = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(6.5), Inches(1.5), Pt(2), Inches(5.5)
    )
    divider.fill.solid()
    divider.fill.fore_color.rgb = RGBColor(203, 213, 225)
    divider.line.fill.background()
    
    # Right column title
    right_title_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.4), Inches(6), Inches(0.5))
    tf = right_title_box.text_frame
    p = tf.paragraphs[0]
    p.text = f"● {right_title}"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    
    # Right column content
    right_box = slide.shapes.add_textbox(Inches(6.8), Inches(1.95), Inches(5.8), Inches(5))
    tf = right_box.text_frame
    tf.word_wrap = True
    
    first = True
    for item in right_items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        
        if item.startswith('- '):
            p.text = "▸ " + item[2:]
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(8)
        else:
            p.text = item
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_TEXT
    
    return slide

def add_content_slide_v2(prs, title, content_items, subtitle="", has_subtitle=False):
    """Enhanced content slide with better styling"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Light background
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background()
    
    # Header with gradient effect (simulated with shape)
    header = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.3)
    )
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY_DARK
    header.line.fill.background()
    
    # Accent line
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(1.28), Inches(3), Inches(0.06)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.35), Inches(12), Inches(0.7))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    if subtitle and has_subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(16)
        p2.font.color.rgb = PRIMARY_LIGHT
    
    # Content area with subtle background
    content_bg = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.4), Inches(1.5), Inches(12.5), Inches(5.7)
    )
    content_bg.fill.solid()
    content_bg.fill.fore_color.rgb = LIGHT_GRAY
    content_bg.line.fill.background()
    
    # Content
    content_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.7), Inches(12), Inches(5.3))
    tf = content_box.text_frame
    tf.word_wrap = True
    
    first = True
    for item in content_items:
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        
        # Check if it's a heading
        if item.startswith('### '):
            p.text = item[4:]
            p.font.size = Pt(20)
            p.font.bold = True
            p.font.color.rgb = PRIMARY
            p.space_before = Pt(14)
            p.space_after = Pt(6)
        elif item.startswith('## '):
            p.text = item[3:]
            p.font.size = Pt(22)
            p.font.bold = True
            p.font.color.rgb = PRIMARY_DARK
            p.space_before = Pt(16)
        elif item.startswith('**') and item.endswith('**'):
            p.text = "▸ " + item.strip('*')
            p.font.size = Pt(17)
            p.font.bold = True
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(4)
        elif item.startswith('> '):
            p.text = '"' + item[2:].strip('"') + '"'
            p.font.size = Pt(15)
            p.font.italic = True
            p.font.color.rgb = MUTED_TEXT
            p.space_before = Pt(10)
            p.space_after = Pt(10)
        elif item.startswith('- '):
            p.text = "• " + item[2:]
            p.font.size = Pt(16)
            p.level = 0
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(4)
        elif item.startswith('  - '):
            p.text = "   ◦ " + item[4:]
            p.font.size = Pt(14)
            p.level = 1
            p.font.color.rgb = MUTED_TEXT
        elif item.startswith(('1. ', '2. ', '3. ', '4. ', '5. ', '6. ')):
            p.text = item
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(4)
        elif item.strip() == "":
            p.text = ""
            p.space_after = Pt(6)
        else:
            p.text = item
            p.font.size = Pt(16)
            p.font.color.rgb = DARK_TEXT
    
    return slide

def add_visual_architecture_slide(prs):
    """Create a visual 3-tier architecture diagram"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Background
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background()
    
    # Header
    header = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1)
    )
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY_DARK
    header.line.fill.background()
    
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(1.08), Inches(4), Inches(0.05)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()
    
    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.3), Inches(12), Inches(0.6))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = "3-Tier System Architecture"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Layer 1: Presentation (Top)
    layer1 = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2), Inches(1.6), Inches(9.333), Inches(1.5)
    )
    layer1.fill.solid()
    layer1.fill.fore_color.rgb = RGBColor(219, 234, 254)
    layer1.line.color.rgb = PRIMARY
    layer1.line.width = Pt(2)
    
    # Layer 1 content
    l1_text = slide.shapes.add_textbox(Inches(2.2), Inches(1.7), Inches(9), Inches(1.3))
    tf = l1_text.text_frame
    p = tf.paragraphs[0]
    p.text = "📱 PRESENTATION LAYER"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    
    p2 = tf.add_paragraph()
    p2.text = "React 19 Frontend (Port 3000) • Dashboard • Resume Builder • Job Portal"
    p2.font.size = Pt(14)
    p2.font.color.rgb = DARK_TEXT
    
    # Arrow 1
    arrow1 = slide.shapes.add_shape(
        MSO_SHAPE.DOWN_ARROW, Inches(5.5), Inches(3.15), Inches(2), Inches(0.5)
    )
    arrow1.fill.solid()
    arrow1.fill.fore_color.rgb = ACCENT
    arrow1.line.fill.background()
    
    # HTTP Label
    http_label = slide.shapes.add_textbox(Inches(7.8), Inches(3.15), Inches(2), Inches(0.4))
    tf = http_label.text_frame
    p = tf.paragraphs[0]
    p.text = "HTTP/JSON"
    p.font.size = Pt(11)
    p.font.color.rgb = MUTED_TEXT
    p.font.italic = True
    
    # Layer 2: Application (Middle)
    layer2 = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2), Inches(3.7), Inches(9.333), Inches(1.5)
    )
    layer2.fill.solid()
    layer2.fill.fore_color.rgb = RGBColor(254, 243, 199)
    layer2.line.color.rgb = ACCENT
    layer2.line.width = Pt(2)
    
    l2_text = slide.shapes.add_textbox(Inches(2.2), Inches(3.8), Inches(9), Inches(1.3))
    tf = l2_text.text_frame
    p = tf.paragraphs[0]
    p.text = "⚙️ APPLICATION LAYER"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = RGBColor(180, 83, 9)
    
    p2 = tf.add_paragraph()
    p2.text = "Express Server (Port 5000) • 30+ REST APIs • Middleware • Business Logic"
    p2.font.size = Pt(14)
    p2.font.color.rgb = DARK_TEXT
    
    # Arrow 2
    arrow2 = slide.shapes.add_shape(
        MSO_SHAPE.DOWN_ARROW, Inches(5.5), Inches(5.25), Inches(2), Inches(0.5)
    )
    arrow2.fill.solid()
    arrow2.fill.fore_color.rgb = ACCENT
    arrow2.line.fill.background()
    
    # MongoDB Protocol Label
    mongo_label = slide.shapes.add_textbox(Inches(7.8), Inches(5.25), Inches(2.5), Inches(0.4))
    tf = mongo_label.text_frame
    p = tf.paragraphs[0]
    p.text = "MongoDB Protocol"
    p.font.size = Pt(11)
    p.font.color.rgb = MUTED_TEXT
    p.font.italic = True
    
    # Layer 3: Data (Bottom)
    layer3 = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2), Inches(5.8), Inches(9.333), Inches(1.4)
    )
    layer3.fill.solid()
    layer3.fill.fore_color.rgb = RGBColor(220, 252, 231)
    layer3.line.color.rgb = RGBColor(22, 163, 74)
    layer3.line.width = Pt(2)
    
    l3_text = slide.shapes.add_textbox(Inches(2.2), Inches(5.9), Inches(9), Inches(1.2))
    tf = l3_text.text_frame
    p = tf.paragraphs[0]
    p.text = "🗄️ DATA LAYER"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = RGBColor(22, 101, 52)
    
    p2 = tf.add_paragraph()
    p2.text = "MongoDB Atlas (Cloud) • users • jobs • resumes • job_postings • applications"
    p2.font.size = Pt(14)
    p2.font.color.rgb = DARK_TEXT
    
    return slide

def add_enhanced_table_slide(prs, title, headers, rows):
    """Enhanced table with better styling"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Background
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background()
    
    # Header
    header = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1)
    )
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY_DARK
    header.line.fill.background()
    
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(1.08), Inches(4), Inches(0.05)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()
    
    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.3), Inches(12), Inches(0.6))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Table with better styling
    num_rows = len(rows) + 1
    num_cols = len(headers)
    
    table = slide.shapes.add_table(
        num_rows, num_cols, Inches(0.6), Inches(1.4), Inches(12), Inches(0.65 * num_rows)
    ).table
    
    # Set column widths
    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(3.5)
    table.columns[2].width = Inches(6)
    
    # Set header
    for i, header_text in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header_text
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        for paragraph in cell.text_frame.paragraphs:
            paragraph.font.color.rgb = WHITE
            paragraph.font.bold = True
            paragraph.font.size = Pt(13)
            paragraph.alignment = PP_ALIGN.CENTER
    
    # Set rows with alternating colors
    for row_idx, row_data in enumerate(rows, 1):
        for col_idx, cell_text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = str(cell_text)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            for paragraph in cell.text_frame.paragraphs:
                paragraph.font.size = Pt(12)
                paragraph.alignment = PP_ALIGN.LEFT if col_idx > 0 else PP_ALIGN.CENTER
            
            # Alternating row colors
            if row_idx % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(241, 245, 249)
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE
    
    return slide

def add_timeline_slide(prs, title, steps, subtitle=""):
    """Add a timeline/process slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Background
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background()
    
    # Header
    header = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1)
    )
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY_DARK
    header.line.fill.background()
    
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(1.08), Inches(4), Inches(0.05)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()
    
    title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.3), Inches(12), Inches(0.6))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(14)
        p2.font.color.rgb = PRIMARY_LIGHT
    
    # Timeline steps
    y_start = Inches(1.8)
    x_positions = [Inches(1), Inches(4.5), Inches(8), Inches(11.5)]
    colors = [PRIMARY, ACCENT, RGBColor(34, 197, 94), RGBColor(168, 85, 247)]
    
    for i, (step_title, step_desc) in enumerate(steps[:4]):
        x = x_positions[i]
        color = colors[i % len(colors)]
        
        # Number circle
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y_start, Inches(0.6), Inches(0.6))
        circle.fill.solid()
        circle.fill.fore_color.rgb = color
        circle.line.fill.background()
        
        num_text = slide.shapes.add_textbox(x, y_start + Inches(0.1), Inches(0.6), Inches(0.4))
        tf = num_text.text_frame
        p = tf.paragraphs[0]
        p.text = str(i + 1)
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        
        # Connector line (except last)
        if i < len(steps) - 1 and i < 3:
            line = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE, x + Inches(0.65), y_start + Inches(0.25), 
                Inches(2.6), Pt(3)
            )
            line.fill.solid()
            line.fill.fore_color.rgb = RGBColor(203, 213, 225)
            line.line.fill.background()
        
        # Step title
        title_box = slide.shapes.add_textbox(x - Inches(0.2), y_start + Inches(0.8), Inches(2.5), Inches(0.5))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = step_title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = DARK_TEXT
        p.alignment = PP_ALIGN.CENTER
        
        # Step description
        desc_box = slide.shapes.add_textbox(x - Inches(0.2), y_start + Inches(1.3), Inches(2.5), Inches(2))
        tf = desc_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = step_desc
        p.font.size = Pt(12)
        p.font.color.rgb = MUTED_TEXT
        p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_end_slide_v2(prs, title="THANK YOU", subtitle="Questions?"):
    """Enhanced thank you slide"""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Dark gradient background
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = PRIMARY_DARK
    bg.line.fill.background()
    
    # Decorative elements
    for x, y, size, color in [
        (Inches(-1), Inches(-1), Inches(4), PRIMARY),
        (Inches(11), Inches(5), Inches(3), ACCENT),
        (Inches(10), Inches(-0.5), Inches(2), RGBColor(30, 41, 59))
    ]:
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, size, size)
        circle.fill.solid()
        circle.fill.fore_color.rgb = color
        circle.fill.fore_color.brightness = 0.2
        circle.line.fill.background()
    
    # Accent bar at bottom
    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, 0, Inches(7.35), prs.slide_width, Inches(0.15)
    )
    accent.fill.solid()
    accent.fill.fore_color.rgb = ACCENT
    accent.line.fill.background()
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(12.333), Inches(1.2))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(72)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(32)
    p2.font.color.rgb = PRIMARY_LIGHT
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(20)
    
    # Contact info box
    contact_box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3), Inches(5.2), Inches(7.333), Inches(1.2)
    )
    contact_box.fill.solid()
    contact_box.fill.fore_color.rgb = RGBColor(30, 41, 59)
    contact_box.line.color.rgb = PRIMARY
    contact_box.line.width = Pt(1)
    
    contact_text = slide.shapes.add_textbox(Inches(3), Inches(5.35), Inches(7.333), Inches(0.9))
    tf = contact_text.text_frame
    p = tf.paragraphs[0]
    p.text = "🔗 GitHub: [Repository URL]"
    p.font.size = Pt(14)
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    p2 = tf.add_paragraph()
    p2.text = "🌐 Demo: http://localhost:3000"
    p2.font.size = Pt(14)
    p2.font.color.rgb = PRIMARY_LIGHT
    p2.alignment = PP_ALIGN.CENTER
    
    return slide

def main():
    prs = create_presentation()
    
    # Slide 1: Title (Enhanced)
    add_title_slide(prs, "Job Tracking System", "Full Stack Web Application", "April 2026")
    
    # Slide 2: Section Divider - Overview
    add_section_divider(prs, 1, "Problem & Solution")
    
    # Slide 3: Problem Statement (Two Column)
    add_two_column_slide(prs, "The Challenge", 
        "For Job Seekers",
        [
            "- Managing 50+ applications across companies",
            "- Missing deadlines and follow-ups",
            "- Scattered notes and spreadsheets",
            "- No visibility into progress"
        ],
        "For Recruiters",
        [
            "- Overwhelmed by application volume",
            "- Disorganized candidate tracking",
            "- No analytics on hiring pipeline",
            "- Manual document management"
        ]
    )
    
    # Slide 4: Solution (Enhanced content)
    add_content_slide_v2(prs, "Our Solution", [
        "## A Unified Platform",
        "**Track** job applications with real-time status updates",
        "**Build** professional resumes with structured sections",
        "**Apply** to jobs through integrated portal",
        "**Analyze** hiring metrics with visual dashboards",
        "**Extract** skills from job descriptions automatically",
        "",
        "### User Roles",
        "- **Job Seeker** → Track apps, build resumes, apply for jobs",
        "- **Recruiter** → Post jobs, review candidates, analytics",
        "- **Admin** → Manage users, oversee platform"
    ])
    
    # Slide 5: Section Divider - Technical
    add_section_divider(prs, 2, "Technical Architecture")
    
    # Slide 6: Tech Stack (Enhanced)
    add_content_slide_v2(prs, "Technology Stack", [
        "### Frontend",
        "- **React 19** — Component-based UI library",
        "- **React Router** — Client-side navigation",
        "- **Chart.js & Recharts** — Data visualization",
        "- **Axios** — HTTP client for API calls",
        "",
        "### Backend",
        "- **Node.js** — JavaScript runtime environment",
        "- **Express.js** — Web framework for REST APIs",
        "- **MongoDB Driver** — Database connectivity",
        "",
        "### Database & Cloud",
        "- **MongoDB Atlas** — Cloud-hosted NoSQL database",
        "- **6 collections** with optimized indexing"
    ])
    
    # Slide 7: Visual Architecture Diagram
    add_visual_architecture_slide(prs)
    
    # Slide 8: Section Divider - Features
    add_section_divider(prs, 3, "Core Features")
    
    # Slide 9: Core Modules (Two Column)
    add_two_column_slide(prs, "Core Modules",
        "Authentication & Job Tracking",
        [
            "- User registration with role selection",
            "- Login with credential validation",
            "- Session management via localStorage",
            "- Role-based access control",
            "",
            "- POST /jobs → Add application",
            "- GET /jobs → View all applications",
            "- PUT /jobs/:id → Update status",
            "- DELETE /jobs/:id → Remove"
        ],
        "Resume Builder & Portal",
        [
            "- Personal Information section",
            "- Professional Summary",
            "- Work Experience (multiple)",
            "- Education History",
            "- Skills (tag-based)",
            "- Projects Portfolio",
            "",
            "Recruiters: Post jobs, review, decide",
            "Seekers: Browse, apply, track"
        ]
    )
    
    # Slide 10: More Modules
    add_content_slide_v2(prs, "Additional Modules", [
        "### Admin Module",
        "- View all users and job postings",
        "- Delete users with cascade data removal",
        "- Manage platform content",
        "- View system-wide statistics",
        "",
        "### File Upload Module",
        "- Base64 encoding for document storage",
        "- Resume and cover letter attachments",
        "- 10MB size limit per file",
        "- Retrieval for recruiter review",
        "",
        "### Skill Analysis Module",
        "- Keyword-based skill extraction",
        "- 40+ predefined skills database",
        "- Contextual analysis (remote → Remote Work)",
        "- Gap identification for job seekers"
    ])
    
    # Slide 11: Section Divider - Data
    add_section_divider(prs, 4, "Data & APIs")
    
    # Slide 12: API Endpoints
    add_content_slide_v2(prs, "REST API Endpoints", [
        "### Authentication",
        "- **POST** /signup — User registration with validation",
        "- **POST** /login — User authentication & session",
        "",
        "### Job Management (Personal Tracking)",
        "- **POST** /jobs — Create new job application",
        "- **GET** /jobs — Retrieve all applications",
        "- **PUT** /jobs/:id — Update application status",
        "- **DELETE** /jobs/:id — Remove application",
        "",
        "### Job Portal (Platform)",
        "- **POST** /create-job-posting — Recruiter creates listing",
        "- **POST** /apply-job — Seeker submits application",
        "- **PATCH** /job-applications/:id/status — Recruiter decision"
    ])
    
    # Slide 13: Database (Enhanced Table)
    add_enhanced_table_slide(prs, "MongoDB Collections",
        ["Collection", "Purpose", "Key Fields"],
        [
            ["users", "Authentication", "username, password_hash, role, created_at"],
            ["jobs", "Personal job apps", "user_id, company, role, status, deadline"],
            ["resumes", "Resume builder", "user_id, personal_info, experience[], skills[]"],
            ["job_postings", "Recruiter listings", "recruiter_id, position, company, requirements[]"],
            ["job_applications", "Portal apps", "user_id, job_id, resume_file, status"],
            ["seeker_resumes", "File storage", "user_id, filename, content (base64)"]
        ]
    )
    
    # Slide 14: Section Divider - Demo
    add_section_divider(prs, 5, "Demo & Results")
    
    # Slide 15: Key Features
    add_content_slide_v2(prs, "Key Features & Capabilities", [
        "### 📊 Visual Dashboard",
        "- Charts showing application status distribution",
        "- Deadline calendar with color coding",
        "- Statistics cards (total, interviews, offers)",
        "",
        "### 📄 Resume Builder",
        "- Multiple resume versions support",
        "- Dynamic section addition/removal",
        "- Professional structured layout",
        "",
        "### 🔗 Job Portal",
        "- Direct seeker-recruiter connection",
        "- Document upload and review system",
        "- Real-time application status updates"
    ])
    
    # Slide 16: User Journey (Timeline)
    add_timeline_slide(prs, "User Journey: Job Seeker", [
        ("Sign Up", "Create account as job seeker with profile"),
        ("Build Resume", "Fill all 6 sections with experience"),
        ("Find Jobs", "Browse portal for matching positions"),
        ("Apply", "Upload resume + cover letter")
    ], "From registration to application")
    
    # Slide 17: Achievements
    add_content_slide_v2(prs, "Achievements & Metrics", [
        "### ✅ Project Accomplishments",
        "- Full-stack implementation with modern MERN stack",
        "- Multi-role architecture serving 3 user types",
        "- 30+ REST APIs with input validation",
        "- 6 MongoDB collections with proper indexing",
        "- File handling, analytics, and skill extraction",
        "",
        "### 📊 System Stats",
        "- **3,500+** Lines of Code",
        "- **22** React Components",
        "- **30+** API Endpoints",
        "- **6** Database Collections",
        "- **4** User Roles Supported"
    ])
    
    # Slide 18: Future Scope
    add_content_slide_v2(prs, "Future Roadmap", [
        "### 🔒 Security Improvements",
        "- JWT authentication & bcrypt password hashing",
        "- Rate limiting and input sanitization",
        "",
        "### 📧 Communication",
        "- Email notifications for status updates",
        "- SMS alerts for deadline reminders",
        "",
        "### 🤖 AI & Integrations",
        "- AI-powered job matching algorithm",
        "- LinkedIn profile integration",
        "- Resume PDF export functionality",
        "",
        "### 📱 Platform Expansion",
        "- Mobile app (React Native)",
        "- Real-time updates with WebSocket"
    ])
    
    # Slide 19: Thank You (Enhanced)
    add_end_slide_v2(prs, "THANK YOU", "Questions?")
    
    # Save
    output_path = r"c:\Users\arebu\Desktop\job-tracker-project\Job_Tracking_System_Enhanced.pptx"
    prs.save(output_path)
    print(f"✅ Enhanced presentation saved to: {output_path}")
    print(f"📊 Total slides: 19")

if __name__ == "__main__":
    main()
