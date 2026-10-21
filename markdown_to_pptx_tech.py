#!/usr/bin/env python3
"""
Technical Architecture Focused PPT
Highlights: Frontend, Backend, Database with detailed diagrams
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Colors
REACT_BLUE = RGBColor(97, 218, 251)
NODE_GREEN = RGBColor(83, 158, 67)
MONGO_GREEN = RGBColor(71, 162, 72)
DARK_BG = RGBColor(15, 23, 42)
WHITE = RGBColor(255, 255, 255)
GRAY = RGBColor(100, 116, 139)
LIGHT_GRAY = RGBColor(241, 245, 249)
ACCENT = RGBColor(245, 158, 11)

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_title_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Dark background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_BG
    bg.line.fill.background()
    
    # Accent bars for each layer
    colors = [REACT_BLUE, NODE_GREEN, MONGO_GREEN]
    y_pos = [Inches(0.1), Inches(0.25), Inches(0.4)]
    for color, y in zip(colors, y_pos):
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4), y, Inches(5.333), Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()
    
    # Title
    title = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(12.333), Inches(1.2))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Job Tracking System"
    p.font.size = Pt(56)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle with three icons
    p2 = tf.add_paragraph()
    p2.text = "⚛️ React 19  •  🟢 Node.js + Express  •  🍃 MongoDB Atlas"
    p2.font.size = Pt(28)
    p2.font.color.rgb = REACT_BLUE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(20)
    
    # Description
    desc = slide.shapes.add_textbox(Inches(2), Inches(4.5), Inches(9.333), Inches(1))
    tf = desc.text_frame
    p = tf.paragraphs[0]
    p.text = "Full-Stack Technical Architecture Deep Dive"
    p.font.size = Pt(20)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER
    
    # Date
    date = slide.shapes.add_textbox(Inches(0.5), Inches(6.8), Inches(12.333), Inches(0.4))
    tf = date.text_frame
    p = tf.paragraphs[0]
    p.text = "Technical Interview Presentation • April 2026"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_three_pillar_slide(prs):
    """Overview of the three layers"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # White background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background()
    
    # Header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.2))
    header.fill.solid()
    header.fill.fore_color.rgb = DARK_BG
    header.line.fill.background()
    
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.7))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "3-Tier Architecture Overview"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Three pillars
    pillars = [
        ("⚛️", "FRONTEND", "React 19", REACT_BLUE, [
            "22 Components",
            "React Router",
            "Chart.js + Recharts",
            "Axios HTTP"
        ]),
        ("🟢", "BACKEND", "Node + Express", NODE_GREEN, [
            "30+ REST APIs",
            "Middleware Layer",
            "Auth Controllers",
            "Error Handling"
        ]),
        ("🍃", "DATABASE", "MongoDB Atlas", MONGO_GREEN, [
            "6 Collections",
            "Indexed Schema",
            "Cloud Hosted",
            "BSON Storage"
        ])
    ]
    
    x_positions = [Inches(0.8), Inches(4.8), Inches(8.8)]
    
    for i, (emoji, layer, tech, color, points) in enumerate(pillars):
        x = x_positions[i]
        
        # Card background
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.6), Inches(3.7), Inches(5.5))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_GRAY
        card.line.color.rgb = color
        card.line.width = Pt(3)
        
        # Emoji
        emoji_box = slide.shapes.add_textbox(x, Inches(1.9), Inches(3.7), Inches(0.8))
        tf = emoji_box.text_frame
        p = tf.paragraphs[0]
        p.text = emoji
        p.font.size = Pt(48)
        p.alignment = PP_ALIGN.CENTER
        
        # Layer name
        layer_text = slide.shapes.add_textbox(x + Inches(0.2), Inches(2.7), Inches(3.3), Inches(0.5))
        tf = layer_text.text_frame
        p = tf.paragraphs[0]
        p.text = layer
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = color
        p.alignment = PP_ALIGN.CENTER
        
        # Tech
        tech_text = slide.shapes.add_textbox(x + Inches(0.2), Inches(3.2), Inches(3.3), Inches(0.4))
        tf = tech_text.text_frame
        p = tf.paragraphs[0]
        p.text = tech
        p.font.size = Pt(14)
        p.font.color.rgb = DARK_BG
        p.alignment = PP_ALIGN.CENTER
        
        # Points
        points_box = slide.shapes.add_textbox(x + Inches(0.3), Inches(3.8), Inches(3.1), Inches(3))
        tf = points_box.text_frame
        tf.word_wrap = True
        
        for j, point in enumerate(points):
            if j == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = f"• {point}"
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_BG
            p.space_after = Pt(8)
    
    return slide

def add_frontend_detail_slide(prs):
    """Detailed frontend slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # React blue gradient header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.3))
    header.fill.solid()
    header.fill.fore_color.rgb = REACT_BLUE
    header.line.fill.background()
    
    # Dark accent
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.25), prs.slide_width, Inches(0.08))
    accent.fill.solid()
    accent.fill.fore_color.rgb = DARK_BG
    accent.line.fill.background()
    
    # Title
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(12.333), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "⚛️ FRONTEND: React 19 Architecture"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = DARK_BG
    
    # Two columns
    # Left - Architecture
    left_title = slide.shapes.add_textbox(Inches(0.5), Inches(1.6), Inches(6), Inches(0.5))
    tf = left_title.text_frame
    p = tf.paragraphs[0]
    p.text = "Architecture"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = REACT_BLUE
    
    left_content = slide.shapes.add_textbox(Inches(0.5), Inches(2.1), Inches(5.8), Inches(4.8))
    tf = left_content.text_frame
    tf.word_wrap = True
    
    points = [
        "• Component-based architecture (22 reusable components)",
        "• Functional components with React Hooks",
        "• React Router v6 for client-side navigation",
        "• Protected routes with role-based access",
        "• Axios for HTTP API calls with interceptors",
        "",
        "State Management:",
        "• React Context API for global auth state",
        "• useState for local component state",
        "• Props drilling minimized"
    ]
    
    for i, point in enumerate(points):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(14)
        p.font.color.rgb = DARK_BG if point.startswith("•") else GRAY
        p.space_after = Pt(4)
    
    # Divider
    divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.5), Inches(1.6), Pt(2), Inches(5.5))
    divider.fill.solid()
    divider.fill.fore_color.rgb = RGBColor(203, 213, 225)
    divider.line.fill.background()
    
    # Right - Key Features
    right_title = slide.shapes.add_textbox(Inches(6.8), Inches(1.6), Inches(6), Inches(0.5))
    tf = right_title.text_frame
    p = tf.paragraphs[0]
    p.text = "Key Features"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = REACT_BLUE
    
    right_content = slide.shapes.add_textbox(Inches(6.8), Inches(2.1), Inches(5.8), Inches(4.8))
    tf = right_content.text_frame
    tf.word_wrap = True
    
    features = [
        "• Dynamic forms for Resume Builder",
        "  - Add/remove work experiences",
        "  - Controlled components pattern",
        "",
        "• Role-based UI rendering",
        "  - Same app, different dashboards",
        "  - Conditional route rendering",
        "",
        "• Data Visualization",
        "  - Chart.js + Recharts",
        "  - Dashboard analytics",
        "",
        "• Session Management",
        "  - localStorage persistence",
        "  - JWT-ready structure"
    ]
    
    for i, point in enumerate(features):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_BG if point.startswith("•") else GRAY
        p.space_after = Pt(3)
    
    return slide

def add_backend_detail_slide(prs):
    """Detailed backend slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Node green header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.3))
    header.fill.solid()
    header.fill.fore_color.rgb = NODE_GREEN
    header.line.fill.background()
    
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.25), prs.slide_width, Inches(0.08))
    accent.fill.solid()
    accent.fill.fore_color.rgb = DARK_BG
    accent.line.fill.background()
    
    # Title
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(12.333), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "🟢 BACKEND: Node.js + Express"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Three sections
    sections = [
        ("Architecture", Inches(0.5), [
            "• Express.js framework",
            "• 30+ REST API endpoints",
            "• MVC pattern (no View)",
            "• Controller separation",
            "• Business logic isolated"
        ]),
        ("Middleware", Inches(4.5), [
            "• CORS handling",
            "• Auth validation",
            "• Role checking",
            "• Error handling",
            "• Request logging"
        ]),
        ("File Handling", Inches(8.5), [
            "• Base64 encoding",
            "• In-memory storage",
            "• 10MB validation",
            "• No Multer needed",
            "• Direct DB storage"
        ])
    ]
    
    for title_text, x, points in sections:
        # Section title
        sec_title = slide.shapes.add_textbox(x, Inches(1.6), Inches(4), Inches(0.5))
        tf = sec_title.text_frame
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = NODE_GREEN
        
        # Content box
        content = slide.shapes.add_textbox(x, Inches(2.2), Inches(3.8), Inches(4.5))
        tf = content.text_frame
        tf.word_wrap = True
        
        for i, point in enumerate(points):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_BG
            p.space_after = Pt(6)
    
    # API Endpoints box at bottom
    api_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(5.2), Inches(12.333), Inches(1.8))
    api_box.fill.solid()
    api_box.fill.fore_color.rgb = LIGHT_GRAY
    api_box.line.color.rgb = NODE_GREEN
    api_box.line.width = Pt(2)
    
    api_title = slide.shapes.add_textbox(Inches(0.7), Inches(5.35), Inches(12), Inches(0.4))
    tf = api_title.text_frame
    p = tf.paragraphs[0]
    p.text = "REST API Endpoints"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = NODE_GREEN
    
    api_content = slide.shapes.add_textbox(Inches(0.7), Inches(5.8), Inches(12), Inches(1.1))
    tf = api_content.text_frame
    tf.word_wrap = True
    
    endpoints = [
        "Auth: POST /signup, POST /login",
        "Jobs: POST /jobs, GET /jobs, PUT /jobs/:id, DELETE /jobs/:id",
        "Portal: POST /create-job-posting, POST /apply-job, PATCH /job-applications/:id/status"
    ]
    
    for i, ep in enumerate(endpoints):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = f"• {ep}"
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_BG
        p.font.name = "Consolas"
    
    return slide

def add_database_detail_slide(prs):
    """Detailed database slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Mongo green header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.3))
    header.fill.solid()
    header.fill.fore_color.rgb = MONGO_GREEN
    header.line.fill.background()
    
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.25), prs.slide_width, Inches(0.08))
    accent.fill.solid()
    accent.fill.fore_color.rgb = DARK_BG
    accent.line.fill.background()
    
    # Title
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.35), Inches(12.333), Inches(0.8))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "🍃 DATABASE: MongoDB Atlas"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Collections table
    collections = [
        ["users", "Auth + Roles", "username, password, role"],
        ["jobs", "Job Tracking", "user_id, company, status, deadline"],
        ["resumes", "Resume Data", "user_id, experience[], skills[]"],
        ["job_postings", "Recruiter Jobs", "recruiter_id, position, requirements[]"],
        ["job_applications", "Applications", "user_id, job_id, status, files"],
        ["seeker_resumes", "File Storage", "user_id, name, base64_content"]
    ]
    
    # Table header
    table = slide.shapes.add_table(7, 3, Inches(0.5), Inches(1.6), Inches(8), Inches(4.2)).table
    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(2.5)
    table.columns[2].width = Inches(3)
    
    # Header row
    headers = ["Collection", "Purpose", "Key Fields"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = MONGO_GREEN
        for p in cell.text_frame.paragraphs:
            p.font.color.rgb = WHITE
            p.font.bold = True
            p.font.size = Pt(12)
    
    # Data rows
    for row_idx, row_data in enumerate(collections, 1):
        for col_idx, cell_text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = cell_text
            if row_idx % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GRAY
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11)
                p.font.color.rgb = DARK_BG
    
    # Right side - Indexing Strategy
    idx_title = slide.shapes.add_textbox(Inches(8.8), Inches(1.6), Inches(4), Inches(0.5))
    tf = idx_title.text_frame
    p = tf.paragraphs[0]
    p.text = "Indexing Strategy"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = MONGO_GREEN
    
    idx_content = slide.shapes.add_textbox(Inches(8.8), Inches(2.1), Inches(4), Inches(4))
    tf = idx_content.text_frame
    tf.word_wrap = True
    
    indexes = [
        "• users.username",
        "  → Unique index",
        "  → Fast login lookup",
        "",
        "• jobs.user_id",
        "  → Single field index",
        "  → 'My applications' query",
        "",
        "• job_applications",
        "  → Compound: user_id + job_id",
        "  → Quick status checks",
        "",
        "Why MongoDB?",
        "• Flexible schema",
        "• Cloud-hosted (Atlas)",
        "• Scales horizontally",
        "• BSON handles nested data"
    ]
    
    for i, point in enumerate(indexes):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_BG if point.startswith("•") else GRAY
        p.space_after = Pt(2)
    
    return slide

def add_data_flow_slide(prs):
    """Data flow diagram"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background()
    
    # Header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.2))
    header.fill.solid()
    header.fill.fore_color.rgb = DARK_BG
    header.line.fill.background()
    
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.7))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Data Flow: Frontend → Backend → Database"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Frontend box
    fe_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.8), Inches(3.5), Inches(4.8))
    fe_box.fill.solid()
    fe_box.fill.fore_color.rgb = RGBColor(224, 242, 254)
    fe_box.line.color.rgb = REACT_BLUE
    fe_box.line.width = Pt(3)
    
    fe_title = slide.shapes.add_textbox(Inches(0.7), Inches(2), Inches(3.1), Inches(0.5))
    tf = fe_title.text_frame
    p = tf.paragraphs[0]
    p.text = "⚛️ FRONTEND"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = REACT_BLUE
    
    fe_content = slide.shapes.add_textbox(Inches(0.7), Inches(2.6), Inches(3.1), Inches(3.8))
    tf = fe_content.text_frame
    tf.word_wrap = True
    
    fe_points = [
        "User Action:",
        "• Form submission",
        "• Button click",
        "• API request",
        "",
        "Axios call:",
        "POST /jobs",
        "Headers: Auth",
        "Body: Job data"
    ]
    
    for i, point in enumerate(fe_points):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_BG if not point.endswith(":") else GRAY
        p.font.bold = point.endswith(":")
    
    # Arrow 1
    arrow1 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(4.1), Inches(3.5), Inches(1.2), Inches(0.8))
    arrow1.fill.solid()
    arrow1.fill.fore_color.rgb = ACCENT
    arrow1.line.fill.background()
    
    # HTTP label
    http_label = slide.shapes.add_textbox(Inches(4.2), Inches(4.4), Inches(1), Inches(0.3))
    tf = http_label.text_frame
    p = tf.paragraphs[0]
    p.text = "HTTP"
    p.font.size = Pt(10)
    p.font.color.rgb = GRAY
    
    # Backend box
    be_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.4), Inches(1.8), Inches(3.5), Inches(4.8))
    be_box.fill.solid()
    be_box.fill.fore_color.rgb = RGBColor(220, 252, 231)
    be_box.line.color.rgb = NODE_GREEN
    be_box.line.width = Pt(3)
    
    be_title = slide.shapes.add_textbox(Inches(5.6), Inches(2), Inches(3.1), Inches(0.5))
    tf = be_title.text_frame
    p = tf.paragraphs[0]
    p.text = "🟢 BACKEND"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NODE_GREEN
    
    be_content = slide.shapes.add_textbox(Inches(5.6), Inches(2.6), Inches(3.1), Inches(3.8))
    tf = be_content.text_frame
    tf.word_wrap = True
    
    be_points = [
        "Express handles:",
        "• Route matching",
        "• Middleware auth",
        "• Controller logic",
        "",
        "Business logic:",
        "• Validate input",
        "• Process data",
        "• DB query prep"
    ]
    
    for i, point in enumerate(be_points):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_BG if not point.endswith(":") else GRAY
        p.font.bold = point.endswith(":")
    
    # Arrow 2
    arrow2 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(9), Inches(3.5), Inches(1.2), Inches(0.8))
    arrow2.fill.solid()
    arrow2.fill.fore_color.rgb = ACCENT
    arrow2.line.fill.background()
    
    # Mongo label
    mongo_label = slide.shapes.add_textbox(Inches(9.1), Inches(4.4), Inches(1), Inches(0.3))
    tf = mongo_label.text_frame
    p = tf.paragraphs[0]
    p.text = "BSON"
    p.font.size = Pt(10)
    p.font.color.rgb = GRAY
    
    # Database box
    db_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.3), Inches(1.8), Inches(2.5), Inches(4.8))
    db_box.fill.solid()
    db_box.fill.fore_color.rgb = RGBColor(220, 252, 254)
    db_box.line.color.rgb = MONGO_GREEN
    db_box.line.width = Pt(3)
    
    db_title = slide.shapes.add_textbox(Inches(10.5), Inches(2), Inches(2.1), Inches(0.5))
    tf = db_title.text_frame
    p = tf.paragraphs[0]
    p.text = "🍃 DB"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = MONGO_GREEN
    
    db_content = slide.shapes.add_textbox(Inches(10.5), Inches(2.6), Inches(2.1), Inches(3.8))
    tf = db_content.text_frame
    tf.word_wrap = True
    
    db_points = [
        "MongoDB:",
        "• Insert/Update",
        "• Indexed query",
        "• Return result",
        "",
        "Response:",
        "Success + ID"
    ]
    
    for i, point in enumerate(db_points):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(12)
        p.font.color.rgb = DARK_BG if not point.endswith(":") else GRAY
        p.font.bold = point.endswith(":")
    
    # Response arrow (bottom)
    resp_arrow = slide.shapes.add_shape(MSO_SHAPE.LEFT_ARROW, Inches(4.1), Inches(6), Inches(7.7), Inches(0.5))
    resp_arrow.fill.solid()
    resp_arrow.fill.fore_color.rgb = RGBColor(148, 163, 184)
    resp_arrow.line.fill.background()
    
    resp_label = slide.shapes.add_textbox(Inches(6), Inches(6.6), Inches(3), Inches(0.3))
    tf = resp_label.text_frame
    p = tf.paragraphs[0]
    p.text = "← JSON Response (200 OK + data)"
    p.font.size = Pt(11)
    p.font.color.rgb = GRAY
    
    return slide

def add_key_features_slide(prs):
    """Technical highlights"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = LIGHT_GRAY
    bg.line.fill.background()
    
    # Header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.2))
    header.fill.solid()
    header.fill.fore_color.rgb = DARK_BG
    header.line.fill.background()
    
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.7))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Technical Highlights & Decisions"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Three cards
    cards = [
        ("Frontend", REACT_BLUE, [
            "✓ Dynamic form arrays",
            "  (resume builder)",
            "✓ Role-based rendering",
            "  (3 dashboard types)",
            "✓ Chart integration",
            "  (analytics viz)",
            "",
            "Challenge:",
            "Multi-role UI state"
        ]),
        ("Backend", NODE_GREEN, [
            "✓ 30+ REST endpoints",
            "  (full CRUD)",
            "✓ Base64 file handling",
            "  (no external S3)",
            "✓ Middleware auth",
            "  (role validation)",
            "",
            "Challenge:",
            "File storage design"
        ]),
        ("Database", MONGO_GREEN, [
            "✓ 6 collections",
            "  (normalized)",
            "✓ Strategic indexing",
            "  (query optimization)",
            "✓ BSON nested data",
            "  (experience[])",
            "",
            "Challenge:",
            "Schema flexibility"
        ])
    ]
    
    x_pos = [Inches(0.5), Inches(4.6), Inches(8.7)]
    
    for i, (name, color, points) in enumerate(cards):
        x = x_pos[i]
        
        # Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.5), Inches(4), Inches(5.5))
        card.fill.solid()
        card.fill.fore_color.rgb = WHITE
        card.line.color.rgb = color
        card.line.width = Pt(3)
        
        # Title bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.5), Inches(4), Inches(0.6))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()
        
        # Card title
        card_title = slide.shapes.add_textbox(x, Inches(1.55), Inches(4), Inches(0.5))
        tf = card_title.text_frame
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER
        
        # Content
        content = slide.shapes.add_textbox(x + Inches(0.2), Inches(2.2), Inches(3.6), Inches(4.6))
        tf = content.text_frame
        tf.word_wrap = True
        
        for j, point in enumerate(points):
            if j == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = point
            p.font.size = Pt(13)
            p.font.color.rgb = DARK_BG if point.startswith("✓") else GRAY
            p.font.bold = point.startswith(("✓", "Challenge"))
            p.space_after = Pt(4)
    
    return slide

def add_metrics_slide(prs):
    """Project metrics"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = WHITE
    bg.line.fill.background()
    
    # Header
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.2))
    header.fill.solid()
    header.fill.fore_color.rgb = DARK_BG
    header.line.fill.background()
    
    title = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.7))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Project Metrics"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    
    # Large metrics
    metrics = [
        ("3,500+", "Lines of Code", REACT_BLUE),
        ("22", "React Components", REACT_BLUE),
        ("30+", "API Endpoints", NODE_GREEN),
        ("6", "DB Collections", MONGO_GREEN)
    ]
    
    positions = [
        (Inches(1), Inches(2)),
        (Inches(7), Inches(2)),
        (Inches(1), Inches(4.5)),
        (Inches(7), Inches(4.5))
    ]
    
    for (num, label, color), (x, y) in zip(metrics, positions):
        # Number
        num_box = slide.shapes.add_textbox(x, y, Inches(5), Inches(1.2))
        tf = num_box.text_frame
        p = tf.paragraphs[0]
        p.text = num
        p.font.size = Pt(72)
        p.font.bold = True
        p.font.color.rgb = color
        
        # Label
        label_box = slide.shapes.add_textbox(x, y + Inches(1.1), Inches(5), Inches(0.6))
        tf = label_box.text_frame
        p = tf.paragraphs[0]
        p.text = label
        p.font.size = Pt(20)
        p.font.color.rgb = DARK_BG
    
    return slide

def add_thank_you_slide(prs):
    """Final slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_BG
    bg.line.fill.background()
    
    # Three colored bars
    colors = [REACT_BLUE, NODE_GREEN, MONGO_GREEN]
    y_positions = [Inches(2.8), Inches(3.2), Inches(3.6)]
    
    for color, y in zip(colors, y_positions):
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4), y, Inches(5.333), Inches(0.15))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()
    
    # Title
    title = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(12.333), Inches(1))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "THANK YOU"
    p.font.size = Pt(72)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = "React • Node.js • Express • MongoDB Atlas"
    p2.font.size = Pt(24)
    p2.font.color.rgb = REACT_BLUE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(40)
    
    # Questions
    p3 = tf.add_paragraph()
    p3.text = "Questions?"
    p3.font.size = Pt(32)
    p3.font.color.rgb = GRAY
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(30)
    
    return slide

def main():
    prs = create_presentation()
    
    # 10 slides total
    add_title_slide(prs)
    add_three_pillar_slide(prs)
    add_frontend_detail_slide(prs)
    add_backend_detail_slide(prs)
    add_database_detail_slide(prs)
    add_data_flow_slide(prs)
    add_key_features_slide(prs)
    add_metrics_slide(prs)
    add_thank_you_slide(prs)
    
    output = r"c:\Users\arebu\Desktop\job-tracker-project\Job_Tracking_System_Technical.pptx"
    prs.save(output)
    print(f"✅ Technical PPT saved: {output}")
    print(f"📊 9 slides: Frontend-Backend-Database focus")

if __name__ == "__main__":
    main()
