#!/usr/bin/env python3
"""
Enhanced Original PPT - 14 slides with Frontend/Backend/Database focus
Keeps original structure but adds technical depth and better visuals
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Tech Colors
REACT_BLUE = RGBColor(97, 218, 251)
NODE_GREEN = RGBColor(83, 158, 67)
MONGO_GREEN = RGBColor(71, 162, 72)
DARK_BG = RGBColor(15, 23, 42)
WHITE = RGBColor(255, 255, 255)
GRAY = RGBColor(100, 116, 139)
LIGHT_GRAY = RGBColor(241, 245, 249)
ACCENT = RGBColor(245, 158, 11)
DARK_TEXT = RGBColor(30, 41, 59)

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_header(slide, prs, title, subtitle="", accent_color=ACCENT):
    """Add modern header with accent line"""
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.2))
    header.fill.solid()
    header.fill.fore_color.rgb = DARK_BG
    header.line.fill.background()
    
    # Accent line
    accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.15), Inches(3), Inches(0.06))
    accent.fill.solid()
    accent.fill.fore_color.rgb = accent_color
    accent.line.fill.background()
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(12.333), Inches(0.6))
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
        p2.font.color.rgb = GRAY
    
    return Inches(1.4)  # Return content start Y

def add_title_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Dark gradient background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_BG
    bg.line.fill.background()
    
    # Tech stack badges at top
    badges = [
        ("⚛️ React 19", REACT_BLUE, Inches(2)),
        ("🟢 Node.js", NODE_GREEN, Inches(5)),
        ("🍃 MongoDB", MONGO_GREEN, Inches(8))
    ]
    
    for text, color, x in badges:
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(0.4), Inches(2.8), Inches(0.5))
        badge.fill.solid()
        badge.fill.fore_color.rgb = RGBColor(30, 41, 59)
        badge.line.color.rgb = color
        badge.line.width = Pt(2)
        
        badge_text = slide.shapes.add_textbox(x, Inches(0.45), Inches(2.8), Inches(0.4))
        tf = badge_text.text_frame
        p = tf.paragraphs[0]
        p.text = text
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color
        p.alignment = PP_ALIGN.CENTER
    
    # Main title
    title = slide.shapes.add_textbox(Inches(0.5), Inches(2.8), Inches(12.333), Inches(1))
    tf = title.text_frame
    p = tf.paragraphs[0]
    p.text = "Job Tracking System"
    p.font.size = Pt(56)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Subtitle
    p2 = tf.add_paragraph()
    p2.text = "Full Stack Web Application"
    p2.font.size = Pt(28)
    p2.font.color.rgb = GRAY
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(12)
    
    # Description
    desc = slide.shapes.add_textbox(Inches(0.5), Inches(4.5), Inches(12.333), Inches(1))
    tf = desc.text_frame
    p = tf.paragraphs[0]
    p.text = "React 19 • Node.js • Express • MongoDB Atlas"
    p.font.size = Pt(22)
    p.font.color.rgb = REACT_BLUE
    p.alignment = PP_ALIGN.CENTER
    
    # Date
    date = slide.shapes.add_textbox(Inches(0.5), Inches(6.5), Inches(12.333), Inches(0.4))
    tf = date.text_frame
    p = tf.paragraphs[0]
    p.text = "Presented by: [Your Name] • April 2026"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_problem_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "The Challenge", "Problem Statement")
    
    # Two columns
    # Left - Job Seekers
    left_title = slide.shapes.add_textbox(Inches(0.5), y_start + Inches(0.2), Inches(6), Inches(0.5))
    tf = left_title.text_frame
    p = tf.paragraphs[0]
    p.text = "For Job Seekers"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = REACT_BLUE
    
    left_content = slide.shapes.add_textbox(Inches(0.5), y_start + Inches(0.8), Inches(5.8), Inches(4))
    tf = left_content.text_frame
    tf.word_wrap = True
    
    for point in ["• Managing 50+ applications across companies", "• Missing deadlines and follow-up dates", "• Scattered notes and spreadsheets", "• No visibility into application progress"]:
        p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(16)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(8)
    
    # Divider
    divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.5), y_start + Inches(0.3), Pt(2), Inches(4.5))
    divider.fill.solid()
    divider.fill.fore_color.rgb = RGBColor(203, 213, 225)
    divider.line.fill.background()
    
    # Right - Recruiters
    right_title = slide.shapes.add_textbox(Inches(6.8), y_start + Inches(0.2), Inches(6), Inches(0.5))
    tf = right_title.text_frame
    p = tf.paragraphs[0]
    p.text = "For Recruiters"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    
    right_content = slide.shapes.add_textbox(Inches(6.8), y_start + Inches(0.8), Inches(5.8), Inches(4))
    tf = right_content.text_frame
    tf.word_wrap = True
    
    for point in ["• Overwhelmed by application volume", "• Disorganized candidate tracking", "• No analytics on hiring pipeline", "• Manual document management"]:
        p = tf.add_paragraph()
        p.text = point
        p.font.size = Pt(16)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(8)
    
    # Quote box at bottom
    quote_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), y_start + Inches(5), Inches(11.333), Inches(0.8))
    quote_box.fill.solid()
    quote_box.fill.fore_color.rgb = LIGHT_GRAY
    quote_box.line.color.rgb = REACT_BLUE
    quote_box.line.width = Pt(2)
    
    quote = slide.shapes.add_textbox(Inches(1.2), y_start + Inches(5.15), Inches(10.9), Inches(0.5))
    tf = quote.text_frame
    p = tf.paragraphs[0]
    p.text = '"The average job seeker applies to 50+ jobs but loses track within a week"'
    p.font.size = Pt(16)
    p.font.italic = True
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER
    
    return slide

def add_solution_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "Our Solution", "Job Tracking System", REACT_BLUE)
    
    # Main description
    main_desc = slide.shapes.add_textbox(Inches(0.5), y_start + Inches(0.2), Inches(12.333), Inches(0.6))
    tf = main_desc.text_frame
    p = tf.paragraphs[0]
    p.text = "A unified platform connecting job seekers, recruiters, and admins"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_TEXT
    
    # Capabilities
    caps_title = slide.shapes.add_textbox(Inches(0.5), y_start + Inches(0.9), Inches(6), Inches(0.4))
    tf = caps_title.text_frame
    p = tf.paragraphs[0]
    p.text = "Key Capabilities"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = REACT_BLUE
    
    caps = ["Track job applications with status updates", "Build professional resumes with structured sections", "Apply to jobs through integrated portal", "Analyze hiring metrics with visual dashboards", "Extract skills from job descriptions"]
    
    caps_content = slide.shapes.add_textbox(Inches(0.5), y_start + Inches(1.4), Inches(6), Inches(3))
    tf = caps_content.text_frame
    tf.word_wrap = True
    
    for cap in caps:
        p = tf.add_paragraph()
        p.text = f"✓ {cap}"
        p.font.size = Pt(14)
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(6)
    
    # User Roles card
    roles_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7), y_start + Inches(0.5), Inches(5.8), Inches(4.5))
    roles_card.fill.solid()
    roles_card.fill.fore_color.rgb = LIGHT_GRAY
    roles_card.line.color.rgb = NODE_GREEN
    roles_card.line.width = Pt(2)
    
    roles_title = slide.shapes.add_textbox(Inches(7.2), y_start + Inches(0.7), Inches(5.4), Inches(0.4))
    tf = roles_title.text_frame
    p = tf.paragraphs[0]
    p.text = "User Roles"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = NODE_GREEN
    
    roles = [
        ("Job Seeker", "Track apps, build resumes, apply for jobs"),
        ("Recruiter", "Post jobs, review candidates, analytics"),
        ("Admin", "Manage users, oversee platform")
    ]
    
    roles_content = slide.shapes.add_textbox(Inches(7.2), y_start + Inches(1.2), Inches(5.4), Inches(3.5))
    tf = roles_content.text_frame
    tf.word_wrap = True
    
    for role, desc in roles:
        p = tf.add_paragraph()
        p.text = f"● {role}"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(4)
        
        p2 = tf.add_paragraph()
        p2.text = f"  → {desc}"
        p2.font.size = Pt(12)
        p2.font.color.rgb = GRAY
        p2.space_after = Pt(10)
    
    return slide

def add_tech_stack_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "Technology Stack", accent_color=REACT_BLUE)
    
    # Three columns for Frontend, Backend, Database
    sections = [
        ("⚛️ Frontend", REACT_BLUE, ["React 19 - Component-based UI library", "React Router - Client-side navigation", "Chart.js & Recharts - Data visualization", "Axios - HTTP client for API calls"]),
        ("🟢 Backend", NODE_GREEN, ["Node.js - JavaScript runtime", "Express.js - Web framework for REST APIs", "MongoDB Driver - Database connectivity", "Middleware - CORS, Auth, Error handling"]),
        ("🍃 Database", MONGO_GREEN, ["MongoDB Atlas - Cloud-hosted NoSQL", "6 collections with optimized indexing", "BSON format for complex data", "Automatic scaling & backups"])
    ]
    
    x_positions = [Inches(0.5), Inches(4.6), Inches(8.7)]
    
    for i, (title, color, points) in enumerate(sections):
        x = x_positions[i]
        
        # Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y_start + Inches(0.3), Inches(3.9), Inches(5))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_GRAY
        card.line.color.rgb = color
        card.line.width = Pt(3)
        
        # Title
        title_box = slide.shapes.add_textbox(x + Inches(0.2), y_start + Inches(0.5), Inches(3.5), Inches(0.5))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = color
        
        # Points
        points_box = slide.shapes.add_textbox(x + Inches(0.2), y_start + Inches(1.1), Inches(3.5), Inches(4))
        tf = points_box.text_frame
        tf.word_wrap = True
        
        for point in points:
            p = tf.add_paragraph()
            p.text = f"• {point}"
            p.font.size = Pt(13)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(6)
    
    return slide

def add_architecture_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "System Architecture", "3-Tier Design", ACCENT)
    
    # Three stacked boxes
    layers = [
        ("📱 Presentation Layer", "React Frontend (Port 3000)", REACT_BLUE, [
            "Dashboard Components",
            "Resume Builder Forms",
            "Job Portal Interface"
        ]),
        ("⚙️ Application Layer", "Express Server (Port 5000)", NODE_GREEN, [
            "30+ REST API Endpoints",
            "Middleware (CORS, Auth)",
            "Business Logic Handlers"
        ]),
        ("🗄️ Data Layer", "MongoDB Atlas (Cloud)", MONGO_GREEN, [
            "users, jobs, resumes",
            "job_postings, applications",
            "Indexed Collections"
        ])
    ]
    
    y_positions = [y_start + Inches(0.3), y_start + Inches(2.3), y_start + Inches(4.3)]
    
    for i, ((title, subtitle, color, points), y) in enumerate(zip(layers, y_positions)):
        # Layer box
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2), y, Inches(9.333), Inches(1.6))
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(248, 250, 252)
        box.line.color.rgb = color
        box.line.width = Pt(3)
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(2.3), y + Inches(0.15), Inches(8.7), Inches(0.4))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = color
        
        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(2.3), y + Inches(0.55), Inches(4), Inches(0.35))
        tf = sub_box.text_frame
        p = tf.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(13)
        p.font.color.rgb = DARK_TEXT
        
        # Points on right
        points_box = slide.shapes.add_textbox(Inches(6), y + Inches(0.2), Inches(5), Inches(1.2))
        tf = points_box.text_frame
        tf.word_wrap = True
        
        for point in points:
            p = tf.add_paragraph()
            p.text = f"• {point}"
            p.font.size = Pt(12)
            p.font.color.rgb = GRAY
            p.space_after = Pt(2)
        
        # Arrow (except last)
        if i < len(layers) - 1:
            arrow = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(5.5), y + Inches(1.65), Inches(2), Inches(0.5))
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = ACCENT
            arrow.line.fill.background()
    
    return slide

def add_module_slide(prs, title, subtitle, left_items, right_items, accent_color=ACCENT):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, title, subtitle, accent_color)
    
    # Left column
    left_box = slide.shapes.add_textbox(Inches(0.5), y_start + Inches(0.3), Inches(6), Inches(5.5))
    tf = left_box.text_frame
    tf.word_wrap = True
    
    for item in left_items:
        p = tf.add_paragraph()
        if item.startswith("###"):
            p.text = item[4:]
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = accent_color
            p.space_before = Pt(10)
        elif item.startswith("-"):
            p.text = f"• {item[2:]}"
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(4)
        elif item.startswith("**"):
            p.text = item.strip("*")
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = DARK_TEXT
        else:
            p.text = item
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(4)
    
    # Divider
    divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.5), y_start + Inches(0.3), Pt(2), Inches(5.5))
    divider.fill.solid()
    divider.fill.fore_color.rgb = RGBColor(203, 213, 225)
    divider.line.fill.background()
    
    # Right column
    right_box = slide.shapes.add_textbox(Inches(6.8), y_start + Inches(0.3), Inches(6), Inches(5.5))
    tf = right_box.text_frame
    tf.word_wrap = True
    
    for item in right_items:
        p = tf.add_paragraph()
        if item.startswith("###"):
            p.text = item[4:]
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = accent_color
            p.space_before = Pt(10)
        elif item.startswith("-"):
            p.text = f"• {item[2:]}"
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(4)
        elif item.startswith("**"):
            p.text = item.strip("*")
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = DARK_TEXT
        else:
            p.text = item
            p.font.size = Pt(14)
            p.font.color.rgb = DARK_TEXT
        p.space_after = Pt(4)
    
    return slide

def add_api_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "API Design", "REST Endpoints", NODE_GREEN)
    
    # Three sections
    sections = [
        ("Authentication", NODE_GREEN, ["POST /signup", "POST /login"]),
        ("Job Management", ACCENT, ["POST /jobs", "GET /jobs", "PUT /jobs/:id", "DELETE /jobs/:id"]),
        ("Job Portal", REACT_BLUE, ["POST /create-job-posting", "POST /apply-job", "PATCH /job-applications/:id/status"])
    ]
    
    x_positions = [Inches(0.5), Inches(4.6), Inches(8.7)]
    
    for (title, color, endpoints), x in zip(sections, x_positions):
        # Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y_start + Inches(0.3), Inches(3.9), Inches(5))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_GRAY
        card.line.color.rgb = color
        card.line.width = Pt(2)
        
        # Title
        title_box = slide.shapes.add_textbox(x + Inches(0.2), y_start + Inches(0.5), Inches(3.5), Inches(0.5))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = color
        
        # Endpoints
        ep_box = slide.shapes.add_textbox(x + Inches(0.2), y_start + Inches(1.1), Inches(3.5), Inches(4))
        tf = ep_box.text_frame
        tf.word_wrap = True
        
        for ep in endpoints:
            p = tf.add_paragraph()
            p.text = f"→ {ep}"
            p.font.size = Pt(14)
            p.font.name = "Consolas"
            p.font.color.rgb = DARK_TEXT
            p.space_after = Pt(8)
    
    return slide

def add_database_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "Database Design", "MongoDB Collections", MONGO_GREEN)
    
    # Table
    collections = [
        ["users", "Authentication", "username, password, role"],
        ["jobs", "Personal job apps", "user_id, company, role, status, deadline"],
        ["resumes", "Resume builder data", "user_id, personalInfo, experience[], skills[]"],
        ["job_postings", "Recruiter listings", "recruiter_id, position, company, requirements[]"],
        ["job_applications", "Portal applications", "user_id, job_id, resume_attachment, status"],
        ["job_seeker_resumes", "Uploaded files", "user_id, name, file_content (base64)"]
    ]
    
    # Table
    table = slide.shapes.add_table(7, 3, Inches(0.5), y_start + Inches(0.3), Inches(12.333), Inches(4.2)).table
    table.columns[0].width = Inches(2.5)
    table.columns[1].width = Inches(3)
    table.columns[2].width = Inches(6.5)
    
    # Header
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
    
    # Rows
    for row_idx, row_data in enumerate(collections, 1):
        for col_idx, cell_text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = cell_text
            if row_idx % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GRAY
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(11)
                p.font.color.rgb = DARK_TEXT
    
    # Indexing note
    note = slide.shapes.add_textbox(Inches(0.5), y_start + Inches(4.7), Inches(12.333), Inches(0.6))
    tf = note.text_frame
    p = tf.paragraphs[0]
    p.text = "Indexing: users.username (unique), jobs.user_id (query opt), job_applications (compound)"
    p.font.size = Pt(12)
    p.font.color.rgb = GRAY
    p.font.italic = True
    
    return slide

def add_features_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "Key Features", accent_color=ACCENT)
    
    features = [
        ("📊 Visual Dashboard", "Charts showing application status, deadline calendar, statistics cards"),
        ("📄 Resume Builder", "Multiple versions, dynamic sections, professional structure"),
        ("🔗 Job Portal", "Direct seeker-recruiter connection, document review, real-time updates"),
        ("📈 Analytics", "Hiring metrics, conversion rates, pipeline visualization"),
        ("🤖 Smart Features", "Skill extraction, deadline reminders, company search")
    ]
    
    for i, (icon_title, desc) in enumerate(features):
        y = y_start + Inches(0.3 + i * 0.95)
        
        # Icon box
        icon_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), y, Inches(0.7), Inches(0.7))
        icon_box.fill.solid()
        icon_box.fill.fore_color.rgb = ACCENT
        icon_box.line.fill.background()
        
        # Title
        title_box = slide.shapes.add_textbox(Inches(1.4), y + Inches(0.1), Inches(4), Inches(0.5))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = icon_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = DARK_TEXT
        
        # Description
        desc_box = slide.shapes.add_textbox(Inches(1.4), y + Inches(0.45), Inches(11), Inches(0.4))
        tf = desc_box.text_frame
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(12)
        p.font.color.rgb = GRAY
    
    return slide

def add_demo_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "Demo Walkthrough", "System in Action", REACT_BLUE)
    
    # Two journeys
    journeys = [
        ("Job Seeker Journey", REACT_BLUE, [
            ("1", "Sign up", "Create account as job seeker"),
            ("2", "Build resume", "Fill 6 sections with experience"),
            ("3", "Add job", "Track Google application with deadline"),
            ("4", "Browse portal", "Find matching positions"),
            ("5", "Apply", "Upload resume + cover letter"),
            ("6", "Track progress", "View status in dashboard")
        ]),
        ("Recruiter Journey", ACCENT, [
            ("1", "Post job", "Create Full Stack Developer listing"),
            ("2", "Review applicants", "View 20+ applications"),
            ("3", "Access documents", "Download resumes"),
            ("4", "Make decisions", "Accept/reject candidates"),
            ("5", "View analytics", "Check conversion rates"),
            ("", "", "")
        ])
    ]
    
    x_positions = [Inches(0.5), Inches(6.8)]
    
    for (title, color, steps), x in zip(journeys, x_positions):
        # Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y_start + Inches(0.3), Inches(6), Inches(5.3))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_GRAY
        card.line.color.rgb = color
        card.line.width = Pt(3)
        
        # Title
        title_box = slide.shapes.add_textbox(x + Inches(0.2), y_start + Inches(0.5), Inches(5.6), Inches(0.5))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = color
        
        # Steps
        for i, (num, step_title, desc) in enumerate(steps[:6]):
            step_y = y_start + Inches(1.1 + i * 0.7)
            
            if num:
                # Number circle
                circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.3), step_y, Inches(0.4), Inches(0.4))
                circle.fill.solid()
                circle.fill.fore_color.rgb = color
                circle.line.fill.background()
                
                num_text = slide.shapes.add_textbox(x + Inches(0.3), step_y + Inches(0.05), Inches(0.4), Inches(0.3))
                tf = num_text.text_frame
                p = tf.paragraphs[0]
                p.text = num
                p.font.size = Pt(12)
                p.font.bold = True
                p.font.color.rgb = WHITE
                p.alignment = PP_ALIGN.CENTER
            
            # Step title
            step_title_box = slide.shapes.add_textbox(x + Inches(0.85), step_y, Inches(5), Inches(0.35))
            tf = step_title_box.text_frame
            p = tf.paragraphs[0]
            p.text = f"● {step_title}" if num else ""
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = DARK_TEXT
            
            # Description
            if desc:
                desc_box = slide.shapes.add_textbox(x + Inches(0.85), step_y + Inches(0.3), Inches(5), Inches(0.35))
                tf = desc_box.text_frame
                p = tf.paragraphs[0]
                p.text = f"  → {desc}"
                p.font.size = Pt(11)
                p.font.color.rgb = GRAY
    
    return slide

def add_conclusion_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    y_start = add_header(slide, prs, "Summary & Future Scope", accent_color=MONGO_GREEN)
    
    # Three columns
    sections = [
        ("✅ Achievements", MONGO_GREEN, [
            "Full-stack MERN implementation",
            "Multi-role architecture (3 types)",
            "30+ REST APIs with validation",
            "6 MongoDB collections + indexing",
            "File handling & analytics",
            "3,500+ lines of code"
        ]),
        ("⚠️ Limitations", ACCENT, [
            "Plaintext passwords",
            "No email notifications",
            "No real-time WebSocket",
            "Base64 storage (MVP scale)",
            "",
            ""
        ]),
        ("🚀 Future", REACT_BLUE, [
            "JWT + bcrypt security",
            "Email/SMS notifications",
            "AI job matching",
            "LinkedIn integration",
            "React Native mobile app",
            "PDF resume export"
        ])
    ]
    
    x_positions = [Inches(0.5), Inches(4.6), Inches(8.7)]
    
    for (title, color, items), x in zip(sections, x_positions):
        # Card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y_start + Inches(0.3), Inches(3.9), Inches(5.3))
        card.fill.solid()
        card.fill.fore_color.rgb = LIGHT_GRAY
        card.line.color.rgb = color
        card.line.width = Pt(2)
        
        # Title
        title_box = slide.shapes.add_textbox(x, y_start + Inches(0.5), Inches(3.9), Inches(0.5))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = color
        p.alignment = PP_ALIGN.CENTER
        
        # Items
        items_box = slide.shapes.add_textbox(x + Inches(0.2), y_start + Inches(1.1), Inches(3.5), Inches(4.5))
        tf = items_box.text_frame
        tf.word_wrap = True
        
        for item in items:
            p = tf.add_paragraph()
            p.text = f"• {item}" if item else ""
            p.font.size = Pt(13)
            p.font.color.rgb = DARK_TEXT if item else WHITE
            p.space_after = Pt(6)
    
    return slide

def add_thank_you_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    
    # Dark background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = DARK_BG
    bg.line.fill.background()
    
    # Three tech bars
    colors = [REACT_BLUE, NODE_GREEN, MONGO_GREEN]
    y_pos = [Inches(2.8), Inches(3.15), Inches(3.5)]
    for color, y in zip(colors, y_pos):
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4), y, Inches(5.333), Inches(0.12))
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
    p2.text = "React 19 • Node.js • Express • MongoDB Atlas"
    p2.font.size = Pt(24)
    p2.font.color.rgb = REACT_BLUE
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(30)
    
    # Questions
    p3 = tf.add_paragraph()
    p3.text = "Questions?"
    p3.font.size = Pt(32)
    p3.font.color.rgb = GRAY
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(25)
    
    # Links
    links = slide.shapes.add_textbox(Inches(0.5), Inches(5.8), Inches(12.333), Inches(0.8))
    tf = links.text_frame
    p = tf.paragraphs[0]
    p.text = "GitHub: [Repository URL] • Demo: http://localhost:3000"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER
    
    return slide

def main():
    prs = create_presentation()
    
    # Original 14 slides with enhanced styling
    add_title_slide(prs)
    add_problem_slide(prs)
    add_solution_slide(prs)
    add_tech_stack_slide(prs)  # Enhanced with 3 columns
    add_architecture_slide(prs)  # Visual 3-tier
    
    # Core Modules (3 slides)
    add_module_slide(prs, "Core Modules", "Authentication & Job Tracking",
        ["### Authentication Module", "- User registration with role selection", "- Login with credential validation", "- Session management via localStorage", "- Role-based access control (client/recruiter/admin)", "", "### Job Tracking Module", "- **POST** /jobs → Add application", "- **GET** /jobs → View all applications", "- **PUT** /jobs/:id → Update status", "- **DELETE** /jobs/:id → Remove application", "", "Fields: Company, Role, Status, Deadline, Follow-up, Notes, URL"],
        ["### Resume Builder", "- Personal Information", "- Professional Summary", "- Work Experience (multiple entries)", "- Education History", "- Skills (tag-based)", "- Projects Portfolio", "", "### Job Portal", "**For Recruiters:**", "- Create job postings with requirements", "- Review applicants with documents", "- Update application status", "- View hiring analytics", "", "**For Job Seekers:**", "- Browse available positions", "- Apply with resume + cover letter", "- Track application status"],
        ACCENT)
    
    add_module_slide(prs, "Core Modules (Continued)", "Admin, File Upload & Skill Analysis",
        ["### Admin Module", "- View all users and job postings", "- Delete users (cascades to their data)", "- Manage platform content", "- View system-wide statistics", "", "### File Upload Module", "- Base64 encoding for storage", "- Resume and cover letter attachments", "- 10MB size limit", "- Retrieval for recruiter review"],
        ["### Skill Analysis Module", "- Keyword-based skill extraction", "- 40+ predefined skills database", "- Contextual analysis (remote → Remote Collaboration)", "- Gap identification for job seekers", "", "### Technical Highlights", "- **Frontend:** React Hooks, Context API", "- **Backend:** Express middleware pattern", "- **Database:** MongoDB aggregation queries", "- **Security:** Role validation per endpoint"],
        REACT_BLUE)
    
    add_api_slide(prs)  # Enhanced API slide
    add_database_slide(prs)  # Enhanced table
    add_features_slide(prs)
    add_demo_slide(prs)
    add_conclusion_slide(prs)
    add_thank_you_slide(prs)
    
    output = r"c:\Users\arebu\Desktop\job-tracker-project\Job_Tracking_System_Enhanced_Final.pptx"
    prs.save(output)
    print(f"✅ Enhanced Original PPT saved: {output}")
    print(f"📊 14 slides with Frontend-Backend-Database focus")
    print(f"🎨 Modern styling with React Blue, Node Green, Mongo Green accents")

if __name__ == "__main__":
    main()
