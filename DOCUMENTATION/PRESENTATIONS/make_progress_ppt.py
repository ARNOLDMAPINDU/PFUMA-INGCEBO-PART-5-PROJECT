# -*- coding: utf-8 -*-
"""
make_progress_ppt.py - generates PFUMA/INGCEBO's Part 5 progress/defense
presentation in the "gmoyo style": plain, short bullet text (one clause
per line) plus a small infographic panel on each content slide - coloured
rounded-rectangle boxes, connecting lines, a native (vector, not an
image) Gantt chart, and a colour-coded implementation-status panel.

Follows the exact slide sequence and 15-minute defense format of the
reference exemplar "G.Moyo NT018481Z Telecommunication SOS System for
captised boats.pptx" (see PART5\\PROJECT WRITE UPPS and SCHOOL GUIDELINES
FOR PART 5 PROJECTS\\), and reuses the builder pattern already proven for
Arnold's sibling Fault-Injection Testbed project
(PART5\\FAULT INJECTION PROJECT\\THE PROJECT\\make_gmoyo_style_ppt.py).

Edit the CONTENT section near the bottom (bullets, Gantt tasks, status
rows, student/supervisor details) and rerun - no shape needs to be
hand-placed again.

Run: python make_progress_ppt.py
"""
import os

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Emu, Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(HERE, "PFUMA_INGCEBO_Progress_Presentation.pptx")

# ---------------------------------------------------------------------------
# Design system - matched to the sibling project's reference file
# ---------------------------------------------------------------------------
BLUE = RGBColor(0x52, 0x99, 0xD6)       # platform / primary
BLUE_BG = RGBColor(0xE6, 0xED, 0xF5)    # title-slide value cells
ORANGE = RGBColor(0xE5, 0x82, 0x26)     # pending / attention
RED = RGBColor(0xBE, 0x41, 0x41)        # rejected / risk
GREEN = RGBColor(0x2F, 0xA0, 0x5A)      # done / cleared
GREY = RGBColor(0x7D, 0x7D, 0x7D)       # admin / captions
PURPLE = RGBColor(0x91, 0x41, 0xB4)     # write-up
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK = RGBColor(0x14, 0x14, 0x14)
LINE_GREY = RGBColor(0xD9, 0xD9, 0xD9)
CONNECTOR_BLUE = RGBColor(0x37, 0xAA, 0xCD)

FONT_SERIF = "Times New Roman"
FONT_TITLE = "Arial Narrow"
FONT_BODY = "Arial"

# NOTE: registration number and supervisor are genuinely not known yet
# (see CLAUDE.md section 3/8) - keep these bracketed placeholders, never
# invent values. Update here once Arnold has them.
STUDENT = "Arnold T. Mapindu"
REG = "[Registration Number]"
SUPERVISOR = "[Supervisor's Name and Title]"
TITLE = ("Role-Based Digital Platform Connecting Cattle and Goat Farmers, "
         "Veterinarians, Suppliers, Buyers, Police and Financial Institutions "
         "Around a Verified Livestock Registry, Marketplace and "
         "Sale-Clearance System (PFUMA/INGCEBO)")


# ---------------------------------------------------------------------------
# low-level helpers
# ---------------------------------------------------------------------------
def add_bg(slide, prs):
    """Full-slide plain white rectangle - no shadow, no border."""
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    rect.fill.solid()
    rect.fill.fore_color.rgb = WHITE
    rect.line.fill.background()
    rect.shadow.inherit = False
    return rect


def _style_text(tf, size, color, bold=False, italic=False, align=PP_ALIGN.LEFT,
                 font=FONT_BODY, space_after=None):
    for para in tf.paragraphs:
        para.alignment = align
        if space_after is not None:
            para.space_after = Pt(space_after)
        for run in para.runs:
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.italic = italic
            run.font.color.rgb = color
            run.font.name = font


def add_textbox(slide, text, left, top, width, height, size=17, color=DARK,
                 bold=False, italic=False, align=PP_ALIGN.LEFT, font=FONT_BODY):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    tf.text = text
    _style_text(tf, size, color, bold, italic, align, font)
    return box


def add_bullets(slide, bullets, left, top, width, height, size=17, color=DARK,
                 space_after=9, bullet_char="• "):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for i, line in enumerate(bullets):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.text = bullet_char + line
        para.alignment = PP_ALIGN.LEFT
        para.space_after = Pt(space_after)
        for run in para.runs:
            run.font.size = Pt(size)
            run.font.color.rgb = color
            run.font.name = FONT_BODY
    return box


def add_box(slide, text, left, top, width, height, color, text_color=WHITE,
            size=12, bold=True):
    """A shadowed, coloured rounded rectangle with centred label text - the
    basic infographic unit used throughout (roles, pipeline states, status
    pills)."""
    box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    box.fill.solid()
    box.fill.fore_color.rgb = color
    box.line.fill.background()
    tf = box.text_frame
    tf.word_wrap = True
    if "\n" in text:
        lines = text.split("\n")
        tf.text = lines[0]
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        for run in tf.paragraphs[0].runs:
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.color.rgb = text_color
            run.font.name = FONT_BODY
        for line in lines[1:]:
            para = tf.add_paragraph()
            para.text = line
            para.alignment = PP_ALIGN.CENTER
            for run in para.runs:
                run.font.size = Pt(size)
                run.font.bold = bold
                run.font.color.rgb = text_color
                run.font.name = FONT_BODY
    else:
        tf.text = text
        _style_text(tf, size, text_color, bold, False, PP_ALIGN.CENTER)
    return box


def add_line(slide, x1, y1, x2, y2, color=DARK, weight_pt=1.4):
    conn = slide.shapes.add_connector(
        MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2)
    )
    conn.line.color.rgb = color
    conn.line.width = Pt(weight_pt)
    return conn


def add_slide_title(slide, text, prs, top=0.3):
    add_textbox(
        slide, text, 0.7, top, prs.slide_width / Emu(1) / 914400 - 1.4, 0.65,
        size=28, color=DARK, align=PP_ALIGN.CENTER, font=FONT_TITLE,
    )


def new_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank
    add_bg(slide, prs)
    return slide


# ---------------------------------------------------------------------------
# composite blocks
# ---------------------------------------------------------------------------
def build_title_slide(prs, rows):
    slide = new_slide(prs)
    add_textbox(slide, "THE NATIONAL UNIVERSITY OF SCIENCE AND TECHNOLOGY",
                0.7, 0.55, 12.0, 0.50, size=17, color=DARK, bold=True,
                align=PP_ALIGN.CENTER, font=FONT_SERIF)
    add_textbox(slide, "FACULTY OF INDUSTRIAL TECHNOLOGY", 1.5, 1.02, 10.3, 0.38,
                size=14, color=DARK, bold=True, align=PP_ALIGN.CENTER, font=FONT_SERIF)
    add_textbox(slide, "DEPARTMENT OF TELECOMMUNICATIONS ENGINEERING", 1.5, 1.40, 10.3, 0.35,
                size=13, color=DARK, bold=True, align=PP_ALIGN.CENTER, font=FONT_SERIF)

    top = 2.05
    for label, value, tall in rows:
        h = 0.72 if tall else 0.48
        label_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                            Inches(0.55), Inches(top), Inches(3.0), Inches(h))
        label_box.fill.solid()
        label_box.fill.fore_color.rgb = BLUE
        label_box.line.fill.background()
        value_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                            Inches(3.55), Inches(top), Inches(9.2), Inches(h))
        value_box.fill.solid()
        value_box.fill.fore_color.rgb = BLUE_BG
        value_box.line.fill.background()
        add_textbox(slide, label, 0.65, top + 0.09, 2.8, h - 0.10, size=13, color=WHITE,
                    bold=True, align=PP_ALIGN.LEFT)
        add_textbox(slide, value, 3.65, top + 0.08, 8.95, h - 0.10, size=13, color=DARK,
                    align=PP_ALIGN.LEFT)
        top += h + 0.03
    return slide


def build_bullets_with_panel(prs, title, bullets, panel_fn, notes=None):
    """Standard content-slide shape: title, bullets on the left (~55% width),
    a small infographic panel on the right built by panel_fn(slide)."""
    slide = new_slide(prs)
    add_slide_title(slide, title, prs)
    add_bullets(slide, bullets, 1.0, 1.55, 6.7, 4.5)
    if panel_fn:
        panel_fn(slide)
    if notes:
        slide.notes_slide.notes_text_frame.text = notes
    return slide


def build_image_style_slide(prs, title, figure_label, caption, diagram_fn, notes=None):
    """Full-width diagram slide: title, small bold figure label, the
    diagram itself, and an italic caption underneath."""
    slide = new_slide(prs)
    add_slide_title(slide, title, prs)
    if figure_label:
        add_textbox(slide, figure_label, 0, 1.25, prs.slide_width / 914400, 0.3,
                    size=13, color=DARK, bold=True, align=PP_ALIGN.CENTER)
    diagram_fn(slide)
    if caption:
        add_textbox(slide, caption, 0.7, prs.slide_height / 914400 - 1.1,
                    prs.slide_width / 914400 - 1.4, 0.5, size=13, color=DARK,
                    italic=True, align=PP_ALIGN.CENTER)
    if notes:
        slide.notes_slide.notes_text_frame.text = notes
    return slide


def build_gantt_slide(prs, title, subtitle, tasks, total_weeks=16):
    """tasks: list of (name, start_week, duration_weeks, color). Row height
    and label font shrink automatically as the task list grows, so adding
    rows later (a new feature the schedule forgot) can't silently overflow
    the slide the way a fixed cell_h did before."""
    slide = new_slide(prs)
    add_slide_title(slide, title, prs)
    add_textbox(slide, subtitle, 3.2, 1.15, 7.0, 0.3, size=12, color=DARK,
                bold=True, align=PP_ALIGN.CENTER)

    grid_left, grid_top = 4.40, 1.65
    available_h = 7.5 - grid_top - 0.35
    cell_w = 0.52
    cell_h = min(0.335, available_h / len(tasks))
    label_font = 10.5 if cell_h >= 0.30 else max(8.0, 9.5 * (cell_h / 0.30))
    label_left, label_w = 0.85, 3.45

    for w in range(total_weeks):
        add_textbox(slide, str(w + 1), grid_left + w * cell_w, grid_top - 0.27, cell_w, 0.20,
                    size=8, color=GREY, bold=False, align=PP_ALIGN.CENTER)

    for r, (name, start, duration, color) in enumerate(tasks):
        row_top = grid_top + r * cell_h
        add_textbox(slide, name, label_left, row_top - 0.02, label_w, cell_h,
                    size=label_font, color=DARK, align=PP_ALIGN.LEFT)
        for w in range(total_weeks):
            cell = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE, Inches(grid_left + w * cell_w), Inches(row_top),
                Inches(cell_w), Inches(cell_h - 0.02),
            )
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE
            cell.line.color.rgb = LINE_GREY
            cell.line.width = Pt(0.5)
            cell.shadow.inherit = False
        bar = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            Inches(grid_left + (start - 1) * cell_w + 0.02), Inches(row_top + 0.02),
            Inches(duration * cell_w - 0.04), Inches(cell_h - 0.06),
        )
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()
    return slide


def build_status_slide(prs, title, bullets, header, rows, notes=None, footnote=None):
    """rows: list of (label, status_text, color). `footnote` renders on the
    slide itself, under the status panel — an asterisk explained only in
    the speaker notes is invisible to anyone just reading the slide."""
    slide = new_slide(prs)
    add_slide_title(slide, title, prs)
    add_bullets(slide, bullets, 0.85, 1.35, 7.1, 4.2)
    add_textbox(slide, header, 8.2, 1.45, 3.6, 0.35, size=15, color=DARK,
                bold=True, align=PP_ALIGN.LEFT)
    top = 2.00
    for label, status, color in rows:
        add_textbox(slide, label, 8.2, top, 2.0, 0.30, size=12.5, color=DARK)
        add_box(slide, status, 10.35, top - 0.03, 1.35, 0.35, color, size=9)
        top += 0.60
    if footnote:
        add_textbox(slide, footnote, 8.2, top + 0.10, 4.60, 1.00,
                     size=9.5, color=GREY, italic=True, align=PP_ALIGN.LEFT)
    if notes:
        slide.notes_slide.notes_text_frame.text = notes
    return slide


def build_closing_slide(prs, timing_note):
    slide = new_slide(prs)
    add_textbox(slide, "Questions", 0.8, 2.30, 11.75, 0.70, size=40, color=DARK,
                align=PP_ALIGN.CENTER, font=FONT_TITLE)
    add_textbox(slide, "Thank you.", 1.5, 3.35, 10.3, 0.50, size=31, color=DARK,
                align=PP_ALIGN.CENTER, font=FONT_TITLE)
    add_textbox(slide, timing_note, 2.0, 4.10, 9.3, 0.55, size=16, color=GREY,
                align=PP_ALIGN.CENTER, italic=True)
    return slide


# ---------------------------------------------------------------------------
# content
# ---------------------------------------------------------------------------
def build():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # 1. Title
    build_title_slide(prs, [
        ("Project Title:", TITLE, True),
        ("FULL NAME:", STUDENT, False),
        ("STUDENT NUMBER:", REG, False),
        ("PROGRAMME:", "BACHELOR OF ENGINEERING HONOURS DEGREE IN\nTELECOMMUNICATIONS ENGINEERING", True),
        ("COURSE CODE:", "TCL 5000", False),
        ("SUPERVISOR:", SUPERVISOR, False),
        ("COHORT :", "BEng Final Year 2026", False),
    ])

    # 2. Purpose
    def purpose_panel(slide):
        add_box(slide, "FARMER / VET /\nSUPPLIER / BUYER", 8.35, 1.75, 2.55, 0.85, BLUE)
        add_line(slide, 9.62, 2.60, 9.62, 3.10, CONNECTOR_BLUE)
        add_box(slide, "VERIFIED\nRECORD", 8.55, 3.15, 2.15, 0.75, GREEN)
        add_line(slide, 9.62, 3.90, 9.62, 4.40, CONNECTOR_BLUE)
        add_box(slide, "MARKETPLACE, CLEARANCE,\nCERTIFICATION & MORE",
                8.05, 4.45, 3.15, 0.80, ORANGE, size=11)
        add_textbox(slide, "One shared, checkable record behind every function", 7.60, 5.55, 5.20, 0.35,
                    size=12.5, color=GREY, italic=True, align=PP_ALIGN.CENTER)

    build_bullets_with_panel(
        prs, "Purpose of the Project",
        ["Turns livestock ownership and health history into a verifiable "
         "digital record, instead of paper, memory, or a stranger's word.",
         "Connects the farmer, vet, supplier, buyer, police, and a bank or "
         "insurer into one shared system.",
         "Gives every role its own marketplace, certification, messaging, "
         "cooperative and outbreak-alert workflow, gated by verification "
         "wherever it matters — not just a single generic app."],
        purpose_panel,
        notes="Read this once, plainly. This is the one-sentence version of "
              "the whole project. State up front that this is a software "
              "platform — no hardware component in this submission.",
    )

    # 3. Background
    def background_panel(slide):
        add_box(slide, "PAPER\nRECORDS", 8.40, 1.85, 2.10, 0.75, GREY)
        add_line(slide, 10.50, 2.22, 11.00, 2.22, DARK, 1.0)
        add_box(slide, "LOST / FORGED /\nNEVER EXISTED", 11.00, 1.85, 1.90, 0.75, RED)
        add_box(slide, "NO EVIDENCE TRAIL\nFOR STOCK THEFT", 8.40, 3.10, 2.60, 0.80, RED)
        add_box(slide, "WEALTH THAT\nCAN'T BE BORROWED\nAGAINST", 8.40, 4.30, 2.60, 0.95, ORANGE)

    build_bullets_with_panel(
        prs, "Background",
        ["Livestock is frequently a rural family's largest store of wealth, "
         "and the least protected asset they own, in the Zimbabwean context.",
         "Ownership, health history, vaccinations and past sales are tracked "
         "on paper, by memory, or not at all.",
         "Disease outbreaks such as Theileriosis (“January Disease”) spread "
         "faster than paper record-keeping can respond to them.",
         "Stock theft and ownership disputes have no fast, credible evidence "
         "trail, and livestock wealth cannot easily be used as loan collateral "
         "without a verifiable record."],
        background_panel,
        notes="(2 minutes) This is a real problem, not a hypothetical one — "
              "ground it in the Stock Theft Prevention Act clearance process "
              "and the disease-surveillance angle if asked.",
    )

    # 4. Main elements of the problem
    def problem_panel(slide):
        add_box(slide, "UNVERIFIABLE\nRECORD", 8.30, 1.70, 2.70, 0.75, ORANGE)
        add_line(slide, 9.65, 2.45, 9.65, 3.00, DARK, 1.4)
        add_box(slide, "NO TRUST FOR BUYERS,\nBANKS, OR POLICE", 8.05, 3.05, 3.20, 0.85, RED)
        add_line(slide, 9.65, 3.90, 9.65, 4.45, DARK, 1.4)
        add_box(slide, "ROLE-BASED PLATFORM\nregistry, marketplace,\nclearance & more",
                8.05, 4.50, 3.20, 0.95, GREEN, size=11)

    build_bullets_with_panel(
        prs, "Main Elements of the Problem",
        ["What: livestock ownership and health records exist only on paper, "
         "or not at all.",
         "Why: this leaves buyers, banks, and police with nothing credible to "
         "check before a sale, a loan, or an investigation.",
         "How: build a role-based digital platform that records the history "
         "and gates resale behind verification."],
        problem_panel,
        notes="(2 minutes)",
    )

    # 5. Aim
    def aim_panel(slide):
        add_box(slide, "REGISTER", 1.30, 4.10, 1.90, 0.70, BLUE)
        add_line(slide, 3.20, 4.45, 4.60, 4.45, DARK, 1.4)
        add_box(slide, "VERIFY", 4.60, 4.10, 1.90, 0.70, ORANGE)
        add_line(slide, 6.50, 4.45, 7.90, 4.45, DARK, 1.4)
        add_box(slide, "CLEAR TO SELL", 7.90, 4.10, 2.10, 0.70, GREEN)
        add_line(slide, 10.00, 4.45, 11.20, 4.45, DARK, 1.4)
        add_box(slide, "BORROW\nAGAINST", 11.20, 4.10, 1.60, 0.70, PURPLE)

    slide5 = new_slide(prs)
    add_slide_title(slide5, "Aim", prs)
    add_textbox(slide5,
                "The aim of the project is to develop a role-based digital "
                "platform connecting farmers, veterinary practitioners, "
                "suppliers, buyers, police officers and financial "
                "institutions around a single verified livestock record, "
                "giving every role a shared registry, marketplace, "
                "messaging and clearance system in place of separate "
                "paper trails.",
                1.00, 1.55, 11.30, 2.00, size=19, color=DARK, align=PP_ALIGN.CENTER)
    aim_panel(slide5)

    # 6. Objectives - two columns; 15 objectives no longer fit one column
    # legibly, and the earlier single-column version under-represented how
    # much of the platform (compliance lifecycle, feed/trading, Jinda
    # assistant) actually exists.
    slide6 = new_slide(prs)
    add_slide_title(slide6, "Objectives", prs, top=0.20)
    add_bullets(slide6, [
        "1) To design a database schema and role-based access control "
        "serving seven platform roles.",
        "2) To develop a herd registry recording each animal's identity, "
        "health timeline, and ownership.",
        "3) To develop a health-and-compliance lifecycle with "
        "vaccination, weaning and gestation countdowns.",
        "4) To develop a marketplace workflow that gates a sale behind "
        "police clearance.",
        "5) To develop a valuation-certificate workflow, informed by "
        "logged vet health events, issuing a verifiable certificate.",
        "6) To create an institution ledger for certificate lookup and "
        "loan-collateral flagging.",
        "7) To develop an outbreak reporting and verification pipeline "
        "that broadcasts confirmed alerts.",
        "8) To develop a farmer cooperative function sharing a dip-tank "
        "schedule and group vet requests.",
    ], 0.55, 0.95, 6.10, 6.20, size=13, bullet_char="")
    add_bullets(slide6, [
        "9) To develop a farmer feed-budget function and a "
        "supplier/buyer trading-journal function.",
        "10) To calculate an animal's estimated market value from an "
        "automated market-rate scan.",
        "11) To develop a web-based application giving every role "
        "browser access.",
        "12) To develop a native mobile application giving every role "
        "mobile access.",
        "13) To develop a secure, end-to-end messenger linking every "
        "role.",
        "14) To develop a role-aware natural-language assistant "
        "answering health and compliance questions.",
        "15) To determine, by deploying the platform locally, whether "
        "these workflows operate correctly end to end.",
    ], 6.85, 0.95, 6.10, 6.20, size=13, bullet_char="")

    # 7. Tasks and resources
    slide7 = new_slide(prs)
    add_slide_title(slide7, "Tasks and Resources Required", prs)
    add_bullets(slide7, [
        "Design the shared database schema serving both the web and mobile "
        "clients.",
        "Build the role-based authentication and access-control layer.",
        "Build the health-and-compliance lifecycle and its countdowns.",
        "Build the marketplace listing and police sale-clearance workflow.",
        "Build the valuation-certificate and institution ledger flow.",
        "Build the outbreak reporting, verification, and broadcast pipeline.",
        "Build the farmer cooperative and secure cross-role messenger "
        "functions.",
        "Build the web app, the mobile app, the feed/trading tools, and "
        "the natural-language assistant.",
    ], 0.85, 1.20, 6.60, 4.60, size=13)
    add_textbox(slide7, "Resources", 7.70, 1.40, 3.50, 0.35, size=15, bold=True, color=DARK)
    add_bullets(slide7, [
        "Flask (Python) API", "MySQL database (XAMPP, local)",
        "React / Vite web app", "Expo / React Native mobile app",
        "A single development PC — no specialised hardware required",
    ], 7.70, 1.95, 4.00, 3.00, size=14)
    slide7.notes_slide.notes_text_frame.text = (
        "(2 minutes) Emphasise this is a purely software submission — no "
        "bench hardware, no procurement risk."
    )

    # 8. System diagram
    def system_diagram(slide):
        add_box(slide, "FARMER", 0.55, 1.55, 1.55, 0.60, BLUE)
        add_box(slide, "VET", 0.55, 2.30, 1.55, 0.60, BLUE)
        add_box(slide, "SUPPLIER", 0.55, 3.05, 1.55, 0.60, BLUE)
        add_box(slide, "BUYER", 0.55, 3.80, 1.55, 0.60, BLUE)
        add_box(slide, "POLICE", 0.55, 4.55, 1.55, 0.60, BLUE)
        add_box(slide, "INSTITUTION", 0.55, 5.30, 1.55, 0.60, BLUE)

        # One combined client box, not two role-segmented ones: no role is
        # web-only or mobile-only. Each role still gets its OWN tailored
        # dashboard (Farmer's registry/marketplace differs from Police's
        # clearance queue) - the parity is between web and mobile for a
        # given role, not sameness across roles.
        add_box(slide, "WEB APP  &  MOBILE APP\n(React/Vite + Expo/RN)\neach role's own tailored dashboard,\navailable on either client",
                2.55, 2.65, 2.35, 1.55, GREEN, size=10)

        # The API box is widened into a small module map instead of a bare
        # "143 routes" label - a single terse box was exactly what read as
        # "only a fraction" of the platform. These nine module names are
        # the actual cross-cutting features in DOCUMENTATION/FEATURES_
        # AND_ROLES.md, not a marketing gloss.
        add_box(slide,
                "FLASK API  —  143 ROUTES\n\n"
                "Registry & Compliance   |   Marketplace & Clearance\n"
                "Certification & Institution Ledger   |   Outbreak Pipeline\n"
                "Cooperatives   |   Feed & Trading Tools\n"
                "Messenger   |   Jinda AI Assistant",
                5.35, 1.90, 4.60, 2.30, ORANGE, size=10)

        add_box(slide, "MYSQL\nDATABASE", 10.35, 2.65, 1.85, 0.90, PURPLE)
        add_box(slide,
                "VERIFICATION GATES\nsignup  ·  sale clearance  ·  "
                "movement permits  ·  outbreak reports",
                5.55, 4.75, 4.20, 0.95, RED, size=10)

        for y in (1.85, 2.60, 3.35, 4.10, 4.85, 5.60):
            add_line(slide, 2.10, y, 2.55, 3.42, LINE_GREY, 1.0)
        add_line(slide, 4.90, 3.42, 5.35, 3.05, CONNECTOR_BLUE)
        add_line(slide, 9.95, 3.05, 10.35, 3.10, ORANGE)
        add_line(slide, 7.65, 4.20, 7.65, 4.75, RED)

    build_image_style_slide(
        prs, "System Diagram", "Figure 3.1: Overall Platform System Block Diagram",
        "Every role reaches its own tailored dashboard through either "
        "client; one Flask API holds nine distinct modules over one "
        "shared record, several of them gated behind their own "
        "verification step.",
        system_diagram,
        notes="(explain in 2 minutes) Point at the six roles on the left, "
              "the single combined client box (web and mobile are "
              "feature-equivalent for a given role - a Farmer's dashboard "
              "differs from a Police officer's, but each is the same on "
              "web and mobile), the widened API box listing all nine "
              "modules (this is the fix for 'it only shows a fraction'), "
              "and the "
              "verification-gates box — sale clearance is only one of "
              "four (signup, sale, movement, outbreak); this pattern is "
              "the piece unique to the problem being solved.",
    )

    # 9. Principle
    def principle_panel(slide):
        states = [
            ("LISTING\nCREATED", BLUE),
            ("PENDING\nCLEARANCE", ORANGE),
            ("POLICE\nREVIEW", ORANGE),
        ]
        x, y = 8.05, 1.75
        w, h = 2.45, 0.70
        for text, color in states:
            add_box(slide, text, x, y, w, h, color, size=11)
            if y < 3.6:
                add_line(slide, x + w / 2, y + h, x + w / 2, y + h + 0.28, DARK, 1.2)
            y += h + 0.28
        add_box(slide, "CLEARED — visible to buyers", 7.60, y, 2.35, 0.60, GREEN, size=10)
        add_box(slide, "REJECTED — stays hidden", 10.15, y, 2.35, 0.60, RED, size=10)
        add_line(slide, 9.28, y - 0.28, 8.75, y, DARK, 1.0)
        add_line(slide, 9.28, y - 0.28, 11.30, y, DARK, 1.0)

        # Visible on the slide, not buried in the notes: this pending ->
        # verified -> released pattern is not sale-clearance-only.
        y2 = y + 0.60 + 0.30
        add_box(slide,
                "SAME PATTERN ALSO GATES:\nnew-account signup   |   "
                "movement permits   |   outbreak-report broadcast",
                7.60, y2, 4.90, 0.75, PURPLE, size=10)

    build_bullets_with_panel(
        prs, "Principle: One Pattern, Four Workflows",
        ["A livestock listing tied to a registered animal starts hidden, in "
         "a pending-clearance state.",
         "It is invisible to buyers until police verify ownership and brand "
         "papers against the herd registry.",
         "A cross-district sale additionally requires a movement permit "
         "before it is released.",
         "The same pending → verified → released pattern also gates a "
         "new account at signup and an outbreak report before it is "
         "broadcast — one mechanism, reused four times, not a special "
         "case built just for sales.",
         "This mirrors the real Stock Theft Prevention Act clearance "
         "process, moved from a paper queue into a checkable workflow."],
        principle_panel,
        notes="(2 minutes) The right-hand panel now shows this explicitly "
              "- point at the purple box after the CLEARED/REJECTED split.",
    )

    # 10. Schedule of work
    build_gantt_slide(
        prs, "Schedule of Work", "Indicative 16-Week Execution Timeline",
        [
            ("Guidelines review / proposal", 1, 2, GREY),
            ("Database schema design", 2, 2, BLUE),
            ("Auth & role-based access", 3, 2, BLUE),
            ("Herd registry (web)", 4, 2, GREEN),
            ("Health-compliance lifecycle", 5, 1, GREEN),
            ("Marketplace + clearance gate", 5, 3, GREEN),
            ("Valuation certificate workflow", 6, 2, GREEN),
            ("Institution ledger", 7, 1, GREEN),
            ("Outbreak reporting pipeline", 8, 2, GREEN),
            ("Farmer cooperatives", 8, 1, GREEN),
            ("Feed & trading tools", 9, 1, GREEN),
            ("Mobile app (Expo/RN)", 8, 3, GREEN),
            ("Secure messenger", 10, 1, GREEN),
            ("Jinda AI assistant", 10, 2, GREEN),
            ("Local (XAMPP) deployment", 11, 1, ORANGE),
            ("Integration testing", 11, 2, RED),
            ("Chapters 1-3 write-up", 12, 2, PURPLE),
            ("Chapters 4-5 write-up", 14, 1, PURPLE),
            ("Final corrections", 15, 2, GREY),
        ],
    )

    # 11. Work carried out
    build_status_slide(
        prs, "Work Carried Out",
        ["The backend API and database schema are built and running, "
         "covering all seven roles.",
         "The web app is built and demoed live; the mobile app is built "
         "and reaches the same backend, but has not yet been exercised "
         "on a physical device.",
         "The marketplace, clearance, certification, outbreak-reporting, "
         "messenger, cooperative, health-compliance, feed/trading and "
         "assistant workflows are all implemented end to end.",
         "The platform was moved off external hosting and now runs "
         "entirely on the local development machine.",
         "Next: complete the dissertation write-up against the school's "
         "guidelines."],
        "Implementation Status",
        [
            ("Backend API / DB", "DONE", GREEN),
            ("Web app", "DONE", GREEN),
            ("Mobile app", "BUILT", ORANGE),
            ("Core workflows*", "DONE", GREEN),
            ("Local deployment", "DONE", GREEN),
            ("Dissertation", "IN PROGRESS", ORANGE),
        ],
        footnote="* marketplace, sale clearance, the valuation certificate, "
                 "institution ledger, outbreak reporting, the messenger, "
                 "farmer cooperatives, the health-compliance lifecycle, "
                 "feed/trading tools, and the Jinda assistant.",
        notes="(3 minutes) * Core workflows = marketplace, sale clearance, "
              "the valuation certificate, institution ledger, outbreak "
              "reporting, the messenger, farmer cooperatives, the "
              "health-compliance lifecycle, feed/trading tools, and the "
              "natural-language "
              "assistant - say this if asked what the pill covers. Be "
              "honest and confident: the platform itself is built and "
              "demoable locally; the remaining work is the academic "
              "write-up, not the software. On Jinda specifically, if "
              "asked how smart it is: it correctly handles a recognised "
              "request, including one typed in Shona, and actually "
              "navigates the app - shown live in testing. It does not "
              "reason through an open-ended question (tested: asked why "
              "a vaccine was overdue, it fell back to a generic keyword "
              "match instead of answering). Say this plainly if asked - "
              "it is a fixed rule set, not a language model, by design "
              "(see Table 3.1), and that tradeoff is the honest answer.",
    )

    # 12. Closing
    build_closing_slide(prs, "15 minutes total: 10 to present, 5 for questions.")

    prs.save(OUTPUT)
    print("Saved: %s" % OUTPUT)
    print("Slides: %d" % len(list(prs.slides)))


if __name__ == "__main__":
    build()
