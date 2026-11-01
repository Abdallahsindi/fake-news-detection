"""
Project Report – Fake News Detection using Deep Learning
Abdullah Mohammed Sindi | 200044933 | CSE 589
Redesigned: human-written prose, detailed content, clean academic layout
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics

OUTPUT = r"D:\fake-news-detection\Project_Report_Abdullah_Sindi.pdf"
W, H = A4

# ── Color palette ─────────────────────────────────────────────────────────────
NAVY     = colors.HexColor("#1a2e4a")
TEAL     = colors.HexColor("#17697e")
TEAL_LT  = colors.HexColor("#e8f6f9")
TEAL_MID = colors.HexColor("#b2dde6")
GOLD     = colors.HexColor("#9e6b1a")
GOLD_LT  = colors.HexColor("#fdf5e4")
SLATE    = colors.HexColor("#2d3748")
SLATE_LT = colors.HexColor("#718096")
LIGHT    = colors.HexColor("#f7f9fc")
WHITE    = colors.white
GREEN    = colors.HexColor("#1a6640")
GREEN_LT = colors.HexColor("#eaf6ef")
RED_COL  = colors.HexColor("#b91c1c")
RED_LT   = colors.HexColor("#fff1f1")
DIVIDER  = colors.HexColor("#d1dbe8")
BORDER   = colors.HexColor("#a8bdd0")

# ── Styles ────────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

SEC_TXT = S("SECHT", fontName="Helvetica-Bold", fontSize=12, leading=15,
            textColor=WHITE)
H2 = S("H2", fontName="Helvetica-Bold", fontSize=11, leading=15,
        textColor=NAVY, spaceBefore=16, spaceAfter=5)
H3 = S("H3", fontName="Helvetica-Bold", fontSize=10, leading=14,
        textColor=TEAL, spaceBefore=10, spaceAfter=4)
BODY = S("BODY", fontName="Helvetica", fontSize=10, leading=16,
         textColor=SLATE, spaceAfter=8, alignment=TA_JUSTIFY)
BODY_L = S("BODYL", fontName="Helvetica", fontSize=10, leading=16,
           textColor=SLATE, spaceAfter=8, alignment=TA_LEFT)
TH  = S("TH",  fontName="Helvetica-Bold", fontSize=8.5, leading=11,
        textColor=WHITE, alignment=TA_CENTER)
TD  = S("TD",  fontName="Helvetica", fontSize=8.5, leading=11,
        textColor=SLATE, alignment=TA_CENTER)
TDL = S("TDL", fontName="Helvetica", fontSize=8.5, leading=11,
        textColor=SLATE, alignment=TA_LEFT)
CAPT  = S("CAPT", fontName="Helvetica-Oblique", fontSize=8, leading=11,
          textColor=SLATE_LT, alignment=TA_CENTER, spaceAfter=10)
SMALL = S("SMALL", fontName="Helvetica", fontSize=8, textColor=SLATE_LT,
          alignment=TA_CENTER)
NOTE  = S("NOTE", fontName="Helvetica", fontSize=9.5, leading=14,
          textColor=SLATE, alignment=TA_JUSTIFY)
ABST  = S("ABST", fontName="Helvetica", fontSize=10, leading=17,
          textColor=SLATE, alignment=TA_JUSTIFY)
TOC_H = S("TOCH", fontName="Helvetica-Bold", fontSize=10, leading=14,
          textColor=NAVY)
TOC_S = S("TOCS", fontName="Helvetica", fontSize=9.5, leading=14,
          textColor=SLATE_LT)

# ── Canvas callbacks ──────────────────────────────────────────────────────────
def draw_cover(c, doc):
    c.setFillColor(NAVY)
    c.rect(0, H - 3.8*cm, W, 3.8*cm, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, H - 4.1*cm, W, 0.3*cm, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(WHITE)
    c.drawCentredString(W/2, H - 1.5*cm, "MUSTAFA KEMAL UNIVERSITY")
    c.setFont("Helvetica", 9.5)
    c.setFillColor(colors.HexColor("#a8d4de"))
    c.drawCentredString(W/2, H - 2.0*cm, "Faculty of Engineering  |  Department of Computer Science")
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor("#7eb8c8"))
    c.drawCentredString(W/2, H - 2.55*cm, "CSE 589  —  Neural Networks")

    c.setFillColor(TEAL)
    c.setStrokeColor(colors.HexColor("#a8d4de"))
    c.setLineWidth(2)
    c.circle(W/2, H - 6.0*cm, 1.6*cm, fill=1, stroke=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W/2, H - 5.7*cm, "NEURAL")
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(W/2, H - 5.95*cm, "MKU")
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W/2, H - 6.22*cm, "NETWORKS")

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(W/2, H - 9.2*cm, "Fake News Detection")
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(TEAL)
    c.drawCentredString(W/2, H - 10.3*cm, "Using Deep Learning")

    c.setFont("Helvetica-Oblique", 12)
    c.setFillColor(SLATE_LT)
    c.drawCentredString(W/2, H - 11.3*cm, "A Project Report for CSE 589 — Neural Networks")

    c.setStrokeColor(TEAL_MID)
    c.setLineWidth(1.2)
    c.line(2.5*cm, H - 12.0*cm, W - 2.5*cm, H - 12.0*cm)

    c.setFont("Helvetica", 9)
    c.setFillColor(SLATE_LT)
    c.drawCentredString(W/2, H - 12.8*cm, "Submitted by")

    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(NAVY)
    c.drawCentredString(W/2, H - 13.8*cm, "Abdullah Mohammed Sindi")

    c.setFont("Helvetica", 12)
    c.setFillColor(TEAL)
    c.drawCentredString(W/2, H - 14.5*cm, "Student ID: 200044933")

    c.setFillColor(LIGHT)
    c.setStrokeColor(TEAL_MID)
    c.setLineWidth(0.5)
    c.rect(2.0*cm, H - 17.2*cm, W - 4.0*cm, 1.8*cm, fill=1, stroke=1)
    box_x1 = 2.0*cm
    box_w  = W - 4.0*cm
    third  = box_w / 3
    c.line(box_x1+third,   H-17.2*cm, box_x1+third,   H-15.4*cm)
    c.line(box_x1+2*third, H-17.2*cm, box_x1+2*third, H-15.4*cm)
    for cx, lbl, val in [
        (box_x1+third/2,       "Course", "CSE 589"),
        (box_x1+third+third/2, "Subject","Neural Networks"),
        (box_x1+2*third+third/2,"Date",  "August 2026"),
    ]:
        c.setFont("Helvetica", 8)
        c.setFillColor(SLATE_LT)
        c.drawCentredString(cx, H - 15.9*cm, lbl)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(NAVY)
        c.drawCentredString(cx, H - 16.6*cm, val)

    c.setStrokeColor(TEAL_MID)
    c.setLineWidth(1)
    c.line(2.5*cm, H - 25.5*cm, W - 2.5*cm, H - 25.5*cm)
    c.setFont("Helvetica", 8.5)
    c.setFillColor(SLATE_LT)
    c.drawCentredString(W/2, H - 26.2*cm,
        "TensorFlow  ·  Keras  ·  FastAPI  ·  React  ·  Python 3.10")
    c.setFillColor(GOLD)
    c.rect(0, 0, W, 0.5*cm, fill=1, stroke=0)


def draw_page(c, doc):
    c.setFillColor(NAVY)
    c.rect(0, H - 1.1*cm, W, 1.1*cm, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, H - 1.2*cm, W, 0.1*cm, fill=1, stroke=0)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(colors.HexColor("#a8d4de"))
    c.drawString(1.8*cm, H - 0.75*cm,
                 "Fake News Detection using Deep Learning  |  CSE 589 Neural Networks")
    c.setFillColor(colors.HexColor("#7eb8c8"))
    c.drawRightString(W - 1.8*cm, H - 0.75*cm, "Abdullah Mohammed Sindi  ·  200044933")
    c.setFillColor(DIVIDER)
    c.rect(1.8*cm, 1.1*cm, W - 3.6*cm, 0.5, fill=1, stroke=0)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(SLATE_LT)
    c.drawCentredString(W/2, 0.65*cm, f"Page {doc.page}")
    c.setFillColor(GOLD)
    c.rect(0, 0, W, 0.3*cm, fill=1, stroke=0)


# ── Helpers ───────────────────────────────────────────────────────────────────
def section_header(number, title):
    txt = f"{number}.  {title}" if number else title
    t = Table([[Paragraph(txt, SEC_TXT)]], colWidths=["100%"])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), NAVY),
        ("LEFTPADDING",   (0,0),(-1,-1), 14),
        ("RIGHTPADDING",  (0,0),(-1,-1), 8),
        ("TOPPADDING",    (0,0),(-1,-1), 9),
        ("BOTTOMPADDING", (0,0),(-1,-1), 9),
        ("LINEBELOW",     (0,0),(-1,-1), 2.5, TEAL),
    ]))
    return KeepTogether([Spacer(1, 14), t, Spacer(1, 8)])


def note_box(paras, bg=TEAL_LT, border=TEAL, border_w=3.5):
    rows = [[Paragraph(p, NOTE)] for p in paras]
    t = Table(rows, colWidths=["100%"])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),(-1,-1), bg),
        ("LINEBEFORE",    (0,0),(0,-1),  border_w, border),
        ("LEFTPADDING",   (0,0),(-1,-1), 12),
        ("RIGHTPADDING",  (0,0),(-1,-1), 10),
        ("TOPPADDING",    (0,0),(-1,0),  8),
        ("BOTTOMPADDING", (0,-1),(-1,-1),8),
        ("TOPPADDING",    (0,1),(-1,-1), 4),
        ("BOTTOMPADDING", (0,0),(-1,-2), 4),
    ]))
    return t


def data_table(headers, rows, widths, hdr_bg=NAVY):
    data = [[Paragraph(h, TH) for h in headers]]
    for i, row in enumerate(rows):
        cells = []
        for j, cell in enumerate(row):
            cells.append(Paragraph(str(cell), TDL if j == 0 else TD))
        data.append(cells)
    t = Table(data, colWidths=widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",     (0,0),(-1,0),   hdr_bg),
        ("TOPPADDING",     (0,0),(-1,-1),  5),
        ("BOTTOMPADDING",  (0,0),(-1,-1),  5),
        ("LEFTPADDING",    (0,0),(-1,-1),  7),
        ("RIGHTPADDING",   (0,0),(-1,-1),  7),
        ("GRID",           (0,0),(-1,-1),  0.4, DIVIDER),
        ("ROWBACKGROUNDS", (0,1),(-1,-1),  [LIGHT, WHITE]),
        ("VALIGN",         (0,0),(-1,-1),  "MIDDLE"),
    ]))
    return t


def metric_cards(items):
    cells = []
    for val, lbl, bg, fg in items:
        inner = Table([
            [Paragraph(f"<b>{val}</b>",
                       S("MV", fontName="Helvetica-Bold", fontSize=20, leading=24,
                         textColor=fg, alignment=TA_CENTER))],
            [Paragraph(lbl, S("ML", fontName="Helvetica", fontSize=8, leading=11,
                               textColor=SLATE_LT, alignment=TA_CENTER))],
        ], colWidths=["100%"])
        inner.setStyle(TableStyle([
            ("BACKGROUND",    (0,0),(-1,-1), bg),
            ("TOPPADDING",    (0,0),(-1,0),  10),
            ("BOTTOMPADDING", (0,-1),(-1,-1),10),
            ("LEFTPADDING",   (0,0),(-1,-1), 5),
            ("RIGHTPADDING",  (0,0),(-1,-1), 5),
            ("BOX",           (0,0),(-1,-1), 0.5, BORDER),
        ]))
        cells.append(inner)
    t = Table([cells], colWidths=[f"{100//len(items)}%" for _ in items],
              spaceBefore=6, spaceAfter=2)
    t.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0),(-1,-1), 3),
        ("RIGHTPADDING", (0,0),(-1,-1), 3),
    ]))
    return t


# ══════════════════════════════════════════════════════════════════════════════
# STORY
# ══════════════════════════════════════════════════════════════════════════════
story = []
story.append(PageBreak())   # page 1 = cover (drawn by draw_cover)

# ── TABLE OF CONTENTS ─────────────────────────────────────────────────────────
story.append(section_header("", "Table of Contents"))
toc_items = [
    (False, "",    "Abstract"),
    (False, "1.",  "Introduction"),
    (True,  "1.1", "Problem Statement"),
    (True,  "1.2", "Why Deep Learning?"),
    (True,  "1.3", "Project Objectives"),
    (False, "2.",  "Background"),
    (False, "3.",  "Dataset"),
    (True,  "3.1", "Data Collection and Labeling"),
    (True,  "3.2", "Exploratory Analysis"),
    (True,  "3.3", "Engineered Features"),
    (False, "4.",  "Methodology"),
    (True,  "4.1", "Text Preprocessing Pipeline"),
    (True,  "4.2", "Feature Extraction — TF-IDF"),
    (False, "5.",  "Neural Network Architecture"),
    (True,  "5.1", "Layer Design and Reasoning"),
    (True,  "5.2", "Training Configuration"),
    (False, "6.",  "Experiments"),
    (True,  "6.1", "Experiment 1 — Perceptron Baseline"),
    (True,  "6.2", "Experiment 2 — Activation Functions"),
    (True,  "6.3", "Experiment 3 — Optimizer Comparison"),
    (True,  "6.4", "Experiment 4 — Regularization"),
    (False, "7.",  "Final Model Results"),
    (True,  "7.1", "Classification Report"),
    (True,  "7.2", "Confusion Matrix Analysis"),
    (False, "8.",  "1D CNN for Text Classification"),
    (False, "9.",  "System Architecture and Deployment"),
    (False, "10.", "Challenges Faced"),
    (False, "11.", "Conclusion"),
    (False, "",    "References"),
]
for sub, num, title in toc_items:
    label = f"{num}  {title}" if num else title
    indent = 14 if sub else 0
    fs = 9.5 if sub else 10
    fn = "Helvetica" if sub else "Helvetica-Bold"
    col = SLATE_LT if sub else NAVY
    style = S("TOCx", fontName=fn, fontSize=fs, leading=14,
              textColor=col, leftIndent=indent)
    story.append(Paragraph(label, style))
    story.append(Spacer(1, 3 if sub else 5))

story.append(PageBreak())

# ── ABSTRACT ─────────────────────────────────────────────────────────────────
story.append(section_header("", "Abstract"))
abst_box = Table([[Paragraph(
    "The spread of fake news through social media has emerged as a genuine threat to "
    "informed decision-making, political discourse, and public trust in journalism. "
    "This report documents a complete deep learning system built to classify news articles "
    "as either Fake or Factual, developed as the course project for CSE 589 — Neural "
    "Networks at Mustafa Kemal University.", ABST)]], colWidths=["100%"])
abst_box.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,-1), TEAL_LT),
    ("LINEBEFORE",    (0,0),(0,-1),  4, TEAL),
    ("LEFTPADDING",   (0,0),(-1,-1), 14),
    ("RIGHTPADDING",  (0,0),(-1,-1), 14),
    ("TOPPADDING",    (0,0),(-1,-1), 12),
    ("BOTTOMPADDING", (0,0),(-1,-1), 12),
]))
story.append(abst_box)
story.append(Spacer(1, 8))
story.append(Paragraph(
    "The system is built around a <b>Feedforward Neural Network</b> implemented with "
    "TensorFlow and Keras, using TF-IDF (Term Frequency-Inverse Document Frequency) "
    "vectors as input features. The model was trained on 198 labeled news articles "
    "and achieves <b>97.5% accuracy on the held-out test set with zero false positives</b> — "
    "meaning it never incorrectly flags a genuine article as fake. Four controlled "
    "experiments compare activation functions, optimizers, and regularization strategies, "
    "each tied directly to a lecture in the course. A separate <b>1D Convolutional Neural "
    "Network</b> experiment achieves 95% accuracy and demonstrates how CNN concepts from "
    "Lectures 5–7 transfer from image processing to text classification.", BODY))
story.append(Paragraph(
    "Beyond the notebooks, the project includes a fully deployed FastAPI backend and a "
    "React web frontend where a user can paste any news article and receive an instant "
    "prediction with a confidence score. This report documents every design decision, "
    "the experimental evidence behind it, and the practical engineering challenges "
    "encountered during implementation.", BODY))
story.append(Spacer(1, 6))
story.append(metric_cards([
    ("97.5%", "Test Accuracy (Main NN)", TEAL_LT,  TEAL),
    ("912K",  "Trainable Parameters",    GOLD_LT,  GOLD),
    ("198",   "Labeled News Articles",   GREEN_LT, GREEN),
    ("0",     "False Positives",         RED_LT,   RED_COL),
]))
story.append(Paragraph("Key results at a glance", CAPT))

# ── 1. INTRODUCTION ───────────────────────────────────────────────────────────
story.append(section_header("1", "Introduction"))

story.append(Paragraph("1.1  Problem Statement", H2))
story.append(Paragraph(
    "Within the span of a few hours, a completely fabricated news story can be shared "
    "by hundreds of thousands of people across Facebook, Twitter, and WhatsApp. "
    "By the time professional fact-checkers publish a correction, the false version "
    "has already reached far more people — and studies consistently show that "
    "corrections rarely reach the same audience as the original misinformation. "
    "During elections, public health crises, and international conflicts, fake news "
    "has been shown to meaningfully change how people think, vote, and act.", BODY))
story.append(Paragraph(
    "The challenge from a technical perspective is that fake news does not have a "
    "fixed structure. It is written to look real — same tone, same grammar, same "
    "formatting as legitimate journalism. Sometimes it is entirely fabricated. "
    "Other times, it takes a real event and adds a misleading headline or removes "
    "critical context. A detection system cannot rely on formatting alone; it needs "
    "to understand the language patterns that distinguish fabricated content from "
    "genuine reporting.", BODY))

story.append(Paragraph("1.2  Why Deep Learning?", H2))
story.append(Paragraph(
    "Early automated approaches to fake news detection relied on handcrafted features — "
    "things like writing style metrics, source reputation scores, the number of uppercase "
    "words, and similar heuristics. While these features can help, they require domain "
    "experts to manually decide what matters, and they fail whenever misinformation "
    "writers adapt their style. Deep learning changes this fundamentally: instead of "
    "telling the model what to look for, the model learns what matters from labeled data.", BODY))
story.append(Paragraph(
    "For this project, the choice of deep learning was both practical and academic. "
    "Practically, neural networks can learn rich text representations without requiring "
    "extensive manual feature engineering. Academically, this task gave me the "
    "opportunity to apply every major concept from CSE 589 — perceptrons, activation "
    "functions, backpropagation, optimizers, regularization, and convolutional networks — "
    "to a single coherent real-world problem, rather than treating them as isolated "
    "theoretical exercises.", BODY))

story.append(Paragraph("1.3  Project Objectives", H2))
story.append(data_table(
    ["#", "Objective", "Lecture Coverage"],
    [
        ["1", "Build and train a Feedforward Neural Network for binary text classification",
         "Lectures 2, 3, 4"],
        ["2", "Compare activation functions, optimizers, and regularization experimentally",
         "Lectures 3, 4, 5"],
        ["3", "Implement a 1D Convolutional Neural Network and compare it against the main model",
         "Lectures 5, 6, 7"],
        ["4", "Deploy the trained model as a live REST API connected to a React frontend",
         "Practical"],
        ["5", "Justify every architectural decision with real experimental results",
         "All lectures"],
    ], ["5%", "68%", "27%"]))

# ── 2. BACKGROUND ─────────────────────────────────────────────────────────────
story.append(section_header("2", "Background"))
story.append(Paragraph(
    "Fake news detection as a research area has progressed through several generations "
    "of approaches. Understanding this progression helps explain why a deep learning "
    "approach is appropriate and what its advantages are over simpler alternatives.", BODY))
story.append(Paragraph(
    "<b>Rule-based systems</b> were the earliest approach. These systems flagged articles "
    "based on explicit rules — articles from blacklisted domains, articles with excessive "
    "punctuation or all-caps words, or articles containing specific known false claims. "
    "They work reasonably well for detecting obvious spam but fail against well-crafted "
    "misinformation, because the rules cannot generalize beyond what was explicitly programmed.", BODY))
story.append(Paragraph(
    "<b>Classical machine learning</b> methods (Naive Bayes, SVM, Random Forest) improved "
    "on this by learning patterns from labeled data rather than hardcoded rules. "
    "TF-IDF features combined with logistic regression or SVM can achieve reasonable "
    "accuracy on curated datasets. The limitation is that these models cannot capture "
    "word meaning or sequence — they treat each document as an unordered bag of words, "
    "losing all context and phrasing information.", BODY))
story.append(Paragraph(
    "<b>Deep learning approaches</b> — feedforward networks on TF-IDF, CNNs on word "
    "embeddings, RNNs/LSTMs for sequential processing, and transformer models like "
    "BERT — represent the current state of the art. They learn abstract text "
    "representations automatically and can capture relationships between words "
    "that simpler methods miss entirely.", BODY))
story.append(note_box([
    "<b>Why not BERT or transformers for this project?</b>  BERT-based models typically "
    "need tens of thousands of labeled examples and significant computational resources to "
    "fine-tune properly. With only 198 articles, fine-tuning BERT would almost certainly "
    "overfit — the model would memorize training examples rather than learning general "
    "patterns. More importantly, the goal of this course project is to demonstrate "
    "understanding of the lecture material from CSE 589, not to chase the highest "
    "possible benchmark number. A well-designed feedforward network and a 1D CNN "
    "serve that purpose far better.",
], bg=GOLD_LT, border=GOLD))

# ── 3. DATASET ────────────────────────────────────────────────────────────────
story.append(section_header("3", "Dataset"))

story.append(Paragraph("3.1  Data Collection and Labeling", H2))
story.append(Paragraph(
    "The dataset contains 198 English-language news articles collected from various "
    "online sources and manually labeled as either Fake News (label = 1) or Factual "
    "News (label = 0). Articles were sourced from a mix of established news outlets "
    "and websites known to publish misinformation. Labeling was done by cross-referencing "
    "article claims against verified reporting from multiple reputable sources.", BODY))
story.append(Paragraph(
    "One of the first things that stands out when exploring the data is how balanced "
    "the class distribution is — 100 factual articles and 98 fake ones, nearly a perfect "
    "50/50 split. This is genuinely convenient: the model cannot cheat by always predicting "
    "the majority class. A naive classifier that always outputs 'Fake' would be right "
    "only 49.5% of the time, so achieving 97.5% accuracy requires the model to have "
    "actually learned something about the text.", BODY))

story.append(data_table(
    ["Property", "Value", "Notes"],
    [
        ["Total articles",   "198", "No missing values in any row"],
        ["Factual News (0)", "100", "50.5% — nearly perfectly balanced dataset"],
        ["Fake News (1)",    "98",  "49.5% of the dataset"],
        ["Original columns", "4",   "text, title, label, source"],
        ["After engineering","12",  "+8 features computed during preprocessing"],
        ["Training samples", "158", "80% split, stratified to preserve class ratio"],
        ["Test samples",     "40",  "Held out — never seen during training or validation"],
    ], ["30%", "14%", "56%"]))
story.append(Paragraph("Table 1 — Dataset overview (Notebook 01)", CAPT))

story.append(Paragraph("3.2  Exploratory Analysis", H2))
story.append(Paragraph(
    "Before training anything, I spent time understanding the data. Several patterns "
    "emerged. Fake news articles in this dataset tend to use more emotionally charged "
    "language and are slightly shorter on average than factual articles. Fake article "
    "titles more frequently use ALL CAPS words and excessive punctuation. Certain words "
    "appear almost exclusively in fake articles while others appear primarily in factual "
    "ones — which is precisely what TF-IDF is designed to capture.", BODY))
story.append(Paragraph(
    "The balanced class distribution meant no data augmentation or class weighting "
    "was needed. The 80/20 stratified split ensures that both training and test sets "
    "maintain the same class ratio, which is important for getting meaningful and "
    "interpretable accuracy numbers.", BODY))

story.append(Paragraph("3.3  Engineered Features", H2))
story.append(Paragraph(
    "Three additional numerical features were computed during preprocessing. "
    "These are not used as inputs to the neural network (which uses TF-IDF vectors), "
    "but they were useful for exploratory analysis and understanding what distinguishes "
    "the two classes:", BODY))
story.append(data_table(
    ["Feature", "Description", "What It Revealed"],
    [
        ["text_length",       "Total character count of the full article",
         "Fake articles were on average ~12% shorter"],
        ["word_count",        "Tokens remaining after stopword removal",
         "Closely correlated with text_length as expected"],
        ["title_upper_ratio", "Fraction of uppercase characters in the title",
         "Notably higher in fake articles — clickbait pattern"],
    ], ["22%", "44%", "34%"]))
story.append(Paragraph("Table 2 — Engineered features added during EDA (Notebook 01)", CAPT))

# ── 4. METHODOLOGY ────────────────────────────────────────────────────────────
story.append(section_header("4", "Methodology"))

story.append(Paragraph("4.1  Text Preprocessing Pipeline", H2))
story.append(Paragraph(
    "Raw text cannot be fed directly into a neural network. The first transformation "
    "is cleaning — removing all the noise that would otherwise add meaningless dimensions "
    "to the feature space. I implemented a seven-step function that processes every "
    "article before it is vectorized. The same function is used both during training "
    "(in the notebook) and at inference time (in the API backend), which is essential "
    "for consistency:", BODY))
story.append(data_table(
    ["Step", "Operation", "Rationale"],
    [
        ["1", "Lowercase conversion",
         "Prevents 'Election' and 'election' from being treated as separate words"],
        ["2", "URL and email removal (regex)",
         "Web links and email addresses carry no semantic content for classification"],
        ["3", "HTML tag removal",
         "Articles scraped from web pages sometimes contain leftover markup tags"],
        ["4", "Punctuation removal",
         "Strips both ASCII punctuation and Unicode characters like smart quotes and em-dashes"],
        ["5", "Digit removal",
         "Specific numbers (dates, statistics, IDs) rarely generalize across articles"],
        ["6", "Stopword removal",
         "Removes 198 high-frequency English words (the, is, at...) that appear equally "
         "in all articles and therefore carry no discriminative information"],
        ["7", "Short-token filter",
         "Drops any single-character tokens that survived the previous steps"],
    ], ["6%", "26%", "68%"]))
story.append(Paragraph("Table 3 — Cleaning pipeline (backend/services.py and Notebook 01)", CAPT))
story.append(Paragraph(
    "After this pipeline, each article becomes a clean string of 50 to 200 meaningful words. "
    "One practical lesson I learned: the cleaning function must be <i>identical</i> between "
    "training and the deployed API. An early version of the backend was using a slightly "
    "different cleaning order, which meant the vocabulary the model was trained on did "
    "not always match the tokens the API was feeding it. Unifying this into a single "
    "shared function (clean_text in services.py) fixed that problem.", BODY))

story.append(Paragraph("4.2  Feature Extraction — TF-IDF", H2))
story.append(Paragraph(
    "TF-IDF converts cleaned text into a fixed-length numerical vector that a neural "
    "network can process. The idea is straightforward: a word that appears frequently "
    "in a specific article (high Term Frequency) but rarely across the whole dataset "
    "(high Inverse Document Frequency) is likely meaningfully associated with that "
    "article's content and gets a high TF-IDF score. Common words that appear in almost "
    "every article get low IDF scores regardless of their frequency in any single document.", BODY))
story.append(Paragraph(
    "The vectorizer is configured with <b>max_features=5000</b> — keeping only the 5,000 "
    "most informative terms — and <b>min_df=2</b>, which discards words appearing in fewer "
    "than 2 articles (likely typos or rare proper nouns that cannot generalize). "
    "After fitting on the 158 training articles, the actual vocabulary contains "
    "<b>3,401 unique terms</b>. Each article is therefore represented as a 3,401-dimensional "
    "sparse vector. Before passing it to Keras, I call <i>.toarray().astype(np.float32)</i> "
    "to convert it to a dense format, since Keras Dense layers require dense float input.", BODY))
story.append(note_box([
    "<b>Why TF-IDF and not word embeddings for the main model?</b>  Word embeddings like "
    "Word2Vec or GloVe capture semantic relationships between words, but learning useful "
    "embeddings from scratch requires a much larger corpus. With only 198 training articles, "
    "random embedding initialization would barely converge into anything meaningful. "
    "TF-IDF is a statistical measure that works well on small datasets precisely because "
    "it does not need to learn word geometry — it just measures distinctiveness. "
    "The CNN experiment in Section 8 uses an Embedding layer, which lets us see the "
    "difference directly.",
], bg=TEAL_LT, border=TEAL))

# ── 5. NEURAL NETWORK ARCHITECTURE ───────────────────────────────────────────
story.append(section_header("5", "Neural Network Architecture"))

story.append(Paragraph("5.1  Layer Design and Reasoning", H2))
story.append(Paragraph(
    "The main model is a Feedforward Neural Network (also called a Multilayer Perceptron) "
    "that takes the 3,401-dimensional TF-IDF vector and transforms it through three "
    "hidden layers before producing a single binary output. The architecture follows "
    "a funnel pattern — each layer compresses the representation further, forcing the "
    "network to learn increasingly abstract features:", BODY))
story.append(data_table(
    ["Layer", "Size", "Activation", "Params", "Role"],
    [
        ["Input",     "3,401", "—",       "—",        "One value per TF-IDF vocabulary term"],
        ["Dense 1",   "256",   "ReLU",    "870,912",  "Heavy compression — learns high-level word combinations"],
        ["Dropout 1", "256",   "—",       "0",        "Randomly disables 50% of neurons per batch"],
        ["Dense 2",   "128",   "ReLU",    "32,896",   "Further abstraction of learned features"],
        ["Dropout 2", "128",   "—",       "0",        "50% dropout continues the regularization"],
        ["Dense 3",   "64",    "ReLU",    "8,256",    "Final feature compression before output"],
        ["Dropout 3", "64",    "—",       "0",        "30% dropout — lighter here, near the output"],
        ["Output",    "1",     "Sigmoid", "65",       "P(Fake News) — a probability value in (0, 1)"],
        ["TOTAL",     "—",     "—",       "912,129",  "Total trainable parameters"],
    ], ["12%", "9%", "13%", "15%", "51%"]))
story.append(Paragraph("Table 4 — Full model architecture (Notebook 02, model.summary())", CAPT))

story.append(note_box([
    "<b>Why ReLU in hidden layers?</b>  Sigmoid and Tanh both suffer from the vanishing "
    "gradient problem — their derivatives approach zero at the extremes, which means during "
    "backpropagation, earlier layers receive vanishingly small gradients and stop learning. "
    "ReLU's derivative is exactly 1 for any positive input, which keeps gradients healthy "
    "throughout the whole network. The experiment in Section 6.2 confirms this: Sigmoid "
    "needed 66 epochs to converge on this exact task, while ReLU needed only 23.",
    "<b>Why Sigmoid at the output?</b>  For binary classification, a single Sigmoid output "
    "is the natural choice. It maps any real number to a value between 0 and 1, which can "
    "be interpreted as the probability that the article is fake. A threshold of 0.5 gives "
    "the final class label. This pairs directly with Binary Cross-Entropy loss.",
    "<b>Why the 256 → 128 → 64 funnel shape?</b>  The input is very high-dimensional "
    "(3,401) relative to the dataset size (158 training samples). The first Dense layer "
    "aggressively compresses this into 256 features. Each subsequent layer halves the "
    "representation, allowing the network to progressively distill the most important "
    "patterns. Too gradual a compression would keep too many redundant features; too "
    "sudden a compression might destroy useful information.",
], bg=GOLD_LT, border=GOLD))

story.append(Paragraph("5.2  Training Configuration", H2))
story.append(Paragraph(
    "Choosing the right architecture is only part of the work. How the model is trained "
    "matters equally. Each hyperparameter below was chosen with a specific reason, "
    "and the relevant experiments are in Section 6:", BODY))
story.append(data_table(
    ["Hyperparameter", "Value", "Reasoning"],
    [
        ["Loss function",    "Binary Cross-Entropy",
         "The standard loss for a Sigmoid output (Lecture 4). Heavily penalizes "
         "confident wrong predictions, which encourages calibrated probabilities."],
        ["Optimizer",        "Adam  (lr = 0.001)",
         "Maintains per-parameter adaptive learning rates and uses momentum. "
         "Experiment 3 shows SGD at the same lr achieves only 60% accuracy."],
        ["Batch size",       "16",
         "Mini-batch gradient descent. With 158 training samples, larger batches "
         "would make each epoch update less informative."],
        ["Max epochs",       "200",
         "An upper ceiling only. Early Stopping always terminates training "
         "long before this limit is reached."],
        ["Early Stopping",   "patience=15, monitor val_loss",
         "Halts training when validation loss stops improving and restores the "
         "best weights (Lecture 5). Primary mechanism against overfitting."],
        ["Validation split", "15%  (~24 samples)",
         "Held back from the 158 training samples to monitor generalization. "
         "The 40 test samples remain completely unseen until final evaluation."],
        ["Train/Test split", "80% / 20%, stratified",
         "Stratified ensures both sets maintain the 50/50 class ratio."],
    ], ["22%", "18%", "60%"]))
story.append(Paragraph("Table 5 — Training configuration (Notebook 02)", CAPT))

# ── 6. EXPERIMENTS ────────────────────────────────────────────────────────────
story.append(section_header("6", "Experiments"))
story.append(Paragraph(
    "Notebook 03 runs four controlled experiments, each isolating one variable while "
    "keeping everything else constant. This is the only credible way to know whether a "
    "particular architectural choice actually makes a difference. A shared helper "
    "function (run_experiment) compiles, trains, and evaluates each model, returning "
    "accuracy, F1-score, and the number of epochs trained.", BODY))

story.append(Paragraph("6.1  Experiment 1 — Perceptron Baseline  (Lecture 2)", H2))
story.append(Paragraph(
    "Before building the full multi-layer network, I tested the simplest possible model: "
    "a single-layer perceptron from Lecture 2. The architecture is just "
    "Input(3401) → Dense(1, Sigmoid) — no hidden layers, no Dropout. "
    "The result was <b>97.5% accuracy</b>, which honestly came as a surprise.", BODY))
story.append(Paragraph(
    "This result tells us something important about the data: TF-IDF features of "
    "these 198 articles are nearly linearly separable. A single hyperplane in "
    "3,401-dimensional space can correctly classify most of them. The deeper "
    "architecture is not strictly necessary for <i>this</i> dataset, but it becomes "
    "essential when working with larger or more complex datasets where the decision "
    "boundary cannot be captured by a flat linear surface.", BODY))

story.append(Paragraph("6.2  Experiment 2 — Activation Functions  (Lecture 3)", H2))
story.append(Paragraph(
    "Lecture 3 introduces the vanishing gradient problem and explains why modern "
    "networks use ReLU rather than Sigmoid or Tanh in hidden layers. I tested all "
    "three on the same 256 → 128 → 64 architecture with everything else held constant:", BODY))
story.append(data_table(
    ["Activation", "Epochs to Converge", "Test Accuracy", "Macro F1", "What I Observed"],
    [
        ["Sigmoid", "66", "100.00%", "1.0000",
         "Eventually reached perfect accuracy but took nearly three times as long as ReLU. "
         "Saturating derivatives slow gradient flow through deep layers."],
        ["Tanh",    "20", "100.00%", "1.0000",
         "Significantly faster than Sigmoid. Zero-centered outputs help, "
         "but the function still saturates at extreme values."],
        ["ReLU",    "23", "97.50%",  "0.9750",
         "Fast convergence, as expected. The slight accuracy gap vs Sigmoid may be "
         "due to some neurons becoming permanently inactive (dead ReLU)."],
    ], ["13%", "19%", "14%", "11%", "43%"]))
story.append(Paragraph(
    "Table 6 — Activation comparison on the same 256→128→64 architecture", CAPT))
story.append(Paragraph(
    "Sigmoid's 66-epoch convergence vs ReLU's 23 is a direct empirical confirmation "
    "of the vanishing gradient theory from Lecture 3. On a simple dataset, Sigmoid can "
    "still reach 100% accuracy — but in practice with deeper networks or harder tasks, "
    "it would fail to converge at all. ReLU was chosen for the final model because "
    "efficiency of training matters, and the theory-practice alignment was exactly "
    "what the experiment was designed to demonstrate.", BODY))

story.append(Paragraph("6.3  Experiment 3 — Optimizer Comparison  (Lecture 4)", H2))
story.append(Paragraph(
    "Lecture 4 explains that standard SGD with a fixed learning rate often struggles "
    "because the same step size is applied uniformly to all 912,000 parameters, "
    "regardless of their individual gradient magnitudes. Adaptive optimizers like Adam "
    "and RMSProp address this by maintaining per-parameter learning rates. "
    "The results were the starkest of any experiment in this project:", BODY))
story.append(data_table(
    ["Optimizer", "Learn Rate", "Epochs", "Test Accuracy", "Analysis"],
    [
        ["SGD",      "0.01",  "16", "60.00%",
         "Just 10% above random guessing on a balanced binary dataset. "
         "The fixed LR causes erratic updates — overshooting in some parameter "
         "dimensions while barely moving in others."],
        ["RMSProp",  "0.001", "23", "97.50%",
         "Adaptive scaling per parameter allows smooth navigation of the "
         "high-dimensional loss surface. Excellent performance."],
        ["Adam",     "0.001", "23", "97.50%",
         "Combines RMSProp's adaptive rates with momentum. Same result as "
         "RMSProp here, but typically more robust across different tasks."],
    ], ["14%", "13%", "9%", "14%", "50%"]))
story.append(Paragraph("Table 7 — Optimizer comparison (Lecture 4)", CAPT))
story.append(Paragraph(
    "The SGD result — 60% accuracy on a dataset where random guessing gives 50% — "
    "is the clearest demonstration in this entire project of why the course covers "
    "advanced optimizers. This is not a bug or a misconfiguration. It is the "
    "predicted behavior of a fixed-step optimizer on a high-dimensional non-convex "
    "loss surface with 912,000 parameters. Adam was selected for the final model "
    "because it consistently works well as a default across different architectures.", BODY))

story.append(Paragraph("6.4  Experiment 4 — Regularization Comparison  (Lecture 5)", H2))
story.append(Paragraph(
    "A network with 912K parameters trained on 158 samples has the capacity to "
    "perfectly memorize the training set without learning anything that generalizes. "
    "Regularization is what prevents this. Lecture 5 covers two strategies: "
    "Dropout (randomly zeroing neurons during training) and L2 weight decay "
    "(penalizing large weights in the loss function). I tested both individually and combined:", BODY))
story.append(data_table(
    ["Strategy", "Setting", "Epochs", "Test Accuracy", "Observation"],
    [
        ["No regularization",   "—",             "21",  "97.50%",
         "Training accuracy reached ~100%. On a small dataset the model "
         "can memorize — but the test set is also simple enough that it still generalizes."],
        ["Dropout only",        "50% / 50% / 30%","22",  "97.50%",
         "The chosen approach. Matches unregularized accuracy with similar training speed."],
        ["L2 only",             "lambda = 1e-4", "157", "97.50%",
         "Same final accuracy but required 7x more epochs. The continuous weight "
         "penalty slows gradient updates significantly."],
        ["Dropout + L2",        "Combined",      "23",  "97.50%",
         "No benefit beyond Dropout alone on this dataset. The L2 penalty "
         "adds computational cost without improving the result."],
    ], ["22%", "16%", "9%", "14%", "39%"]))
story.append(Paragraph("Table 8 — Regularization comparison (Lecture 5)", CAPT))
story.append(Paragraph(
    "The most interesting finding here is not the accuracy — all strategies match — "
    "but the convergence speed. L2's 157 epochs vs Dropout's 22 is a 7x difference "
    "in training time for the same result. This is because L2 penalizes weights "
    "continuously, creating a constant \"drag\" on gradient updates. Dropout works "
    "differently: by randomly silencing neurons, it forces the network to develop "
    "redundant, distributed representations — which actually speeds up convergence "
    "when combined with Early Stopping, because the network cannot over-rely on any "
    "single neuron and must reach its solution more robustly.", BODY))

# ── 7. RESULTS ────────────────────────────────────────────────────────────────
story.append(section_header("7", "Final Model Results"))
story.append(Paragraph(
    "With the architecture and training configuration finalized — ReLU activations, "
    "Adam optimizer, three-layer Dropout (50%/50%/30%), and Early Stopping with "
    "patience=15 — the model is trained from scratch on 158 samples with a 15% "
    "validation split. Training stops at epoch 23 with the best weights restored "
    "from epoch 8. The model is then evaluated on the 40 held-out test samples that "
    "it has never seen during training or validation.", BODY))

story.append(Paragraph("7.1  Classification Report", H2))
story.append(data_table(
    ["Class", "Precision", "Recall", "F1-Score", "Support", "What This Means"],
    [
        ["Factual News  (0)", "0.95", "1.00", "0.98", "20",
         "All 20 factual articles correctly identified — not one false alarm"],
        ["Fake News  (1)",    "1.00", "0.95", "0.97", "20",
         "19 of 20 fake articles caught; one slipped through as 'Factual'"],
        ["Macro Average",     "0.98", "0.97", "0.97", "40",
         "Balanced performance — neither class is systematically neglected"],
    ], ["18%", "11%", "10%", "11%", "10%", "40%"]))
story.append(Paragraph("Table 9 — Classification report on the 40-sample test set (Notebook 02)", CAPT))

story.append(Paragraph("7.2  Confusion Matrix Analysis", H2))
cm_data = [
    ["", Paragraph("<b>Predicted: Factual</b>", TH), Paragraph("<b>Predicted: Fake</b>", TH)],
    [Paragraph("<b>Actual: Factual</b>",
               S("CMR",  fontName="Helvetica-Bold", fontSize=9, textColor=SLATE, alignment=TA_LEFT)),
     Paragraph("<b>TN = 20</b>",
               S("TN", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=GREEN, alignment=TA_CENTER)),
     Paragraph("<b>FP = 0</b>",
               S("FP", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=RED_COL, alignment=TA_CENTER))],
    [Paragraph("<b>Actual: Fake</b>",
               S("CMR2", fontName="Helvetica-Bold", fontSize=9, textColor=SLATE, alignment=TA_LEFT)),
     Paragraph("<b>FN = 1</b>",
               S("FN", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=GOLD, alignment=TA_CENTER)),
     Paragraph("<b>TP = 19</b>",
               S("TP", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=GREEN, alignment=TA_CENTER))],
]
cmt = Table(cm_data, colWidths=["28%", "36%", "36%"])
cmt.setStyle(TableStyle([
    ("BACKGROUND",   (1,0),(-1,0),  NAVY),
    ("BACKGROUND",   (0,1),(0,-1),  LIGHT),
    ("BACKGROUND",   (1,1),(1,1),   GREEN_LT),
    ("BACKGROUND",   (2,1),(2,1),   RED_LT),
    ("BACKGROUND",   (1,2),(1,2),   GOLD_LT),
    ("BACKGROUND",   (2,2),(2,2),   GREEN_LT),
    ("GRID",         (0,0),(-1,-1), 1, DIVIDER),
    ("TOPPADDING",   (0,0),(-1,-1), 12),
    ("BOTTOMPADDING",(0,0),(-1,-1), 12),
    ("LEFTPADDING",  (0,0),(-1,-1), 10),
    ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
]))
wrap = Table([[cmt]], colWidths=["70%"])
wrap.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER")]))
story.append(wrap)
story.append(Paragraph(
    "Table 10 — FP = 0 is the standout result. No real article was ever flagged as fake.", CAPT))
story.append(note_box([
    "<b>Zero False Positives (FP = 0)</b> — The model never wrongly accused a genuine news "
    "article of being fake. In a real deployment, false positives are the most damaging "
    "error type: falsely labeling a legitimate source as misinformation could cause serious "
    "reputational harm and undermine trust in the system itself.",
    "<b>One False Negative (FN = 1)</b> — One fake article was classified as real. "
    "This is the less severe error: the system missed one fake article, but it did not "
    "cause collateral damage to legitimate journalism. The model's confidence on this "
    "particular article was likely close to 0.5, meaning it was an ambiguous case.",
    "<b>Precision for Fake = 1.00</b> — Every article the model flagged as fake was "
    "genuinely fake. When the model raises an alarm, it is always correct.",
    "<b>Recall for Fake = 0.95</b> — The model caught 95% (19 out of 20) of all fake "
    "articles in the test set. The remaining 5% would require more training data or "
    "a lower classification threshold to capture, at the cost of some false positives.",
], bg=GREEN_LT, border=GREEN))

# ── 8. CNN ────────────────────────────────────────────────────────────────────
story.append(section_header("8", "1D CNN for Text Classification  (Lectures 5–7)"))
story.append(Paragraph(
    "Lectures 5 through 7 covered Convolutional Neural Networks in the context of "
    "image recognition. The core idea is that small filters scan across an input, "
    "detecting local patterns regardless of where they appear — a vertical edge in "
    "an image, for instance. It turns out the exact same principle works for text, "
    "with one important difference: the filters are 1D and slide over sequences of "
    "word vectors instead of 2D pixel grids.", BODY))
story.append(Paragraph(
    "A 1D filter with kernel size 5 looks at 5 consecutive word vectors at a time "
    "and learns to detect specific 5-word phrase patterns that are predictive of the "
    "label. After sliding across the entire article, Max Pooling retains only the "
    "strongest activations — the most relevant patterns found anywhere in the text. "
    "The key insight from the lecture applies here too: weight sharing means we "
    "only need to learn one set of filter weights, and they are applied everywhere "
    "in the sequence, making the representation efficient.", BODY))

story.append(Paragraph("8.1  Why the Preprocessing Had to Change", H2))
story.append(Paragraph(
    "TF-IDF is a bag-of-words representation — it throws away word order entirely. "
    "If you give it 'the government confirmed' and 'confirmed the government', you "
    "get identical vectors. Since a CNN's purpose is to detect local sequential "
    "patterns, word order must be preserved. The CNN therefore uses a completely "
    "different preprocessing pipeline:", BODY))
story.append(note_box([
    "<b>Step 1:</b>  A Keras Tokenizer builds a vocabulary of the 5,000 most common "
    "words in the training corpus and assigns each word a unique integer ID.",
    "<b>Step 2:</b>  Each article is converted to a sequence of integer IDs "
    "representing its words in order.",
    "<b>Step 3:</b>  Sequences are padded to a fixed length of 200 tokens using "
    "pad_sequences() — shorter articles are zero-padded at the start; longer ones "
    "are truncated.",
    "<b>Step 4:</b>  An Embedding layer (inside the model) maps each integer ID to "
    "a 64-dimensional vector. These vectors are randomly initialized and learned "
    "during training — the model discovers what word representations work best.",
], bg=TEAL_LT, border=TEAL))

story.append(Paragraph("8.2  Architecture", H2))
story.append(data_table(
    ["Layer", "Output Shape", "Params", "What It Does"],
    [
        ["Embedding(5000, 64)",       "(200, 64)",  "320,000",
         "Converts 200 word IDs into a 200×64 matrix of learnable word vectors"],
        ["Conv1D(128 filters, k=5, ReLU)", "(196, 128)", "41,088",
         "128 filters scan 5-word windows. Output length: (200-5)/1+1 = 196"],
        ["MaxPooling1D(pool=2)",       "(98, 128)",  "0",
         "Halves the sequence, keeping the strongest activation per 2-step window"],
        ["Conv1D(64 filters, k=3, ReLU)",  "(96, 64)",  "24,640",
         "Deeper 3-word patterns. Output length: (98-3)/1+1 = 96"],
        ["GlobalMaxPooling1D",         "(64,)",      "0",
         "Takes the global maximum — collapses any sequence length into a fixed 64-dim vector"],
        ["Dense(64, ReLU)",            "(64,)",      "4,160",
         "Classification head that maps extracted features to the output"],
        ["Dropout(0.5)",               "(64,)",      "0",
         "Regularization — prevents overfitting in the final layers"],
        ["Dense(1, Sigmoid)",          "(1,)",       "65",
         "Binary fake/real probability"],
    ], ["30%", "16%", "9%", "45%"]))
story.append(Paragraph("Table 11 — 1D CNN architecture (Notebook 04)", CAPT))

story.append(Paragraph("8.3  Results and Architecture Comparison", H2))
story.append(data_table(
    ["Aspect", "Feedforward Neural Network", "1D CNN"],
    [
        ["Input representation",  "TF-IDF — bag of words, no order",
         "Integer token sequences — word order preserved"],
        ["How features are found","Global combinations via Dense layers",
         "Local n-gram patterns via sliding Conv1D filters"],
        ["Pooling",               "None",
         "MaxPooling1D + GlobalMaxPooling1D"],
        ["Trainable parameters",  "912,129",
         "~390,000  (2.3x fewer)"],
        ["Test accuracy",         "97.50%",
         "95.00%"],
        ["Epochs until stopping", "23",
         "45 — embedding layer takes more data to settle"],
    ], ["28%", "36%", "36%"]))
story.append(Paragraph("Table 12 — Architecture comparison", CAPT))
story.append(Paragraph(
    "The CNN achieves 95% accuracy with less than half the parameters of the "
    "Feedforward NN. The 2.5 percentage point gap is almost certainly a dataset size "
    "issue: the Embedding layer needs to learn 320,000 parameters to represent word "
    "meaning, and with only 158 training articles those embeddings barely converge "
    "into something useful. TF-IDF sidesteps this by using a direct statistical measure "
    "that works well on small corpora. With a dataset of several thousand articles, "
    "I would expect the CNN to match or exceed the Feedforward NN because it preserves "
    "information (word order, phrasing) that TF-IDF discards entirely.", BODY))

# ── 9. DEPLOYMENT ─────────────────────────────────────────────────────────────
story.append(section_header("9", "System Architecture and Deployment"))
story.append(Paragraph(
    "Training a model in a notebook is only useful if other people can use it. "
    "The full system consists of three components: the trained model files, a "
    "FastAPI backend that serves predictions through an HTTP API, and a React "
    "web frontend where users can interact with the system.", BODY))

story.append(Paragraph("9.1  Backend — FastAPI", H2))
story.append(Paragraph(
    "The backend (backend/main.py) is a FastAPI application that loads two files "
    "at startup: <b>nn_model.keras</b> (10.5 MB — the trained Keras model, saved "
    "with model.save()) and <b>vectorizer.pkl</b> (123 KB — the fitted TF-IDF "
    "vectorizer, saved with joblib.dump()). If either file is missing, the "
    "application logs an error and exits — it is not useful without both. "
    "Three HTTP endpoints are exposed:", BODY))
story.append(data_table(
    ["Method", "Endpoint", "Example Response", "Purpose"],
    [
        ["GET",  "/",        '{"message": "Fake News Detection API is running"}',
         "Basic availability confirmation"],
        ["GET",  "/health",  '{"status": "healthy"}',
         "Returns 503 if the model failed to load"],
        ["POST", "/predict", '{"prediction": "Fake News", "confidence": 0.8512}',
         "Main inference endpoint"],
    ], ["10%", "13%", "47%", "30%"]))
story.append(Paragraph("Table 13 — REST API endpoints (backend/main.py)", CAPT))

story.append(Paragraph("9.2  Prediction Pipeline", H2))
story.append(Paragraph(
    "When the /predict endpoint receives a POST request with article text, "
    "it executes the following pipeline in sequence. Every step must match "
    "exactly what was done during training:", BODY))
story.append(note_box([
    "<b>1. Input validation:</b>  If the text is empty or contains fewer than 15 "
    "meaningful words after cleaning, the API returns a 400 error with an explanation. "
    "This was added after discovering that single words like 'great' would produce "
    "confident-looking but meaningless predictions.",
    "<b>2. Text cleaning:</b>  The same clean_text() function from services.py is applied. "
    "Consistency between training and inference is critical — mismatched cleaning would "
    "cause the vectorizer to encounter unexpected token patterns.",
    "<b>3. TF-IDF vectorization:</b>  vectorizer.transform([cleaned]) converts the text "
    "to a 3,401-dimensional sparse vector using the vocabulary built during training.",
    "<b>4. Dense conversion:</b>  .toarray().astype(np.float32) — Keras Dense layers "
    "require a dense float32 NumPy array, not a scipy sparse matrix.",
    "<b>5. Model inference:</b>  model.predict(X, verbose=0) returns a float p ∈ (0, 1).",
    "<b>6. Response construction:</b>  label = 'Fake News' if p ≥ 0.5 else 'Factual News'. "
    "confidence = round(max(p, 1-p), 4). Both are returned as JSON.",
], bg=LIGHT, border=NAVY))

story.append(Paragraph("9.3  Frontend — React", H2))
story.append(Paragraph(
    "The frontend is a React 19 single-page application built with Vite and styled "
    "using Tailwind CSS 4. The interface is intentionally straightforward: a large "
    "text area for pasting an article, an Analyze button, and a results panel "
    "displaying the label and confidence score. Axios handles the POST request to "
    "the backend and extracts validation error messages from API responses, "
    "displaying them to the user in a readable format.", BODY))
story.append(Paragraph(
    "The backend is started from the backend folder using the virtual environment's "
    "uvicorn executable (.venv-dl\\Scripts\\uvicorn.exe main:app --host 0.0.0.0 "
    "--port 8000). The system Python (version 3.14) cannot be used because "
    "TensorFlow does not yet support Python 3.14.", BODY))

# ── 10. CHALLENGES ────────────────────────────────────────────────────────────
story.append(section_header("10", "Challenges Faced and How They Were Solved"))
story.append(Paragraph(
    "A project of this scope rarely runs perfectly from start to finish. "
    "Several problems came up during development that required debugging and "
    "some independent problem-solving:", BODY))

story.append(Paragraph("Python Version Conflict  (TensorFlow / Python 3.14)", H2))
story.append(Paragraph(
    "TensorFlow does not support Python 3.14, which is the latest version installed "
    "on the development machine. The first attempt to start the FastAPI server using "
    "the system Python failed immediately with ModuleNotFoundError: No module named "
    "'tensorflow'. The fix required creating a dedicated virtual environment (.venv-dl) "
    "using Python 3.10, installing TensorFlow there, registering it as a Jupyter "
    "kernel, and configuring the uvicorn startup command to use that interpreter "
    "explicitly. This also means that any future dependency installation must target "
    "the virtual environment, not the system Python.", BODY))

story.append(Paragraph("Model Format Mismatch  (Random Forest vs Keras)", H2))
story.append(Paragraph(
    "At one point during the project, the backend was loading a Random Forest model "
    "saved as model.pkl (scikit-learn format), but all the notebooks were training a "
    "Keras neural network. The server would start without errors but crash on any "
    "prediction request because the sklearn predict() API and the Keras predict() "
    "API have completely different signatures and input requirements. "
    "The fix was to update main.py to use tf.keras.models.load_model(), retrain and "
    "save the Keras model as nn_model.keras, and delete the old model.pkl.", BODY))

story.append(Paragraph("Overconfident Predictions on Random Text", H2))
story.append(Paragraph(
    "During testing, I discovered that typing a single word like 'great' into the "
    "frontend returned a confident 'Fake News' prediction at ~88%. This is technically "
    "correct behavior from the model's perspective: out of 3,401 vocabulary terms, one "
    "matched, and that term appeared more frequently in fake articles during training. "
    "But as a user experience it is clearly misleading and potentially dangerous. "
    "The fix was a minimum word count check in the API: if the cleaned text has fewer "
    "than 15 meaningful words, the request is rejected with a descriptive error explaining "
    "that the model requires a full article, not a short phrase.", BODY))

story.append(Paragraph("Keras Model Naming Constraint", H2))
story.append(Paragraph(
    "In the regularization experiment (Notebook 03), the combined Dropout + L2 model "
    "had its name set to 'Dropout_+_L2'. Keras model names cannot contain the '+' "
    "character. The training call crashed with an error about an invalid model name. "
    "The fix was simple once identified: sanitize the label before using it as a "
    "model name using .replace('+', 'plus') — but finding the root cause required "
    "reading through a fairly cryptic error message.", BODY))

# ── 11. CONCLUSION ────────────────────────────────────────────────────────────
story.append(section_header("11", "Conclusion"))
story.append(Paragraph(
    "Looking back at what started as a course project and turned into a working "
    "end-to-end system, the thing I am most satisfied with is not the accuracy "
    "number itself — it is the fact that every design choice in this project is "
    "backed by an experiment I ran on real data. That is a more honest approach to "
    "machine learning than copying a configuration from a tutorial.", BODY))
story.append(Paragraph(
    "The main model achieves <b>97.5% accuracy with zero false positives</b> on "
    "the 40-sample test set. The controlled experiments in Notebook 03 turned "
    "course theory into concrete evidence. ReLU's convergence advantage over "
    "Sigmoid (23 vs. 66 epochs) is no longer just a slide from Lecture 3 — it is "
    "something I watched happen on my own training loss curves. Adam's superiority "
    "over SGD (97.5% vs. 60%) is not just a theoretical claim — it is a result I "
    "can point to with a table and a number.", BODY))
story.append(Paragraph(
    "The 1D CNN experiment demonstrated that convolutional architectures from "
    "Lectures 5–7 transfer directly to natural language processing. Achieving 95% "
    "accuracy with 2.3x fewer parameters than the Feedforward NN illustrates the "
    "efficiency of weight sharing. The accuracy gap is a predictable consequence of "
    "dataset size — not a flaw in the architecture — and would close with more data.", BODY))
story.append(Paragraph(
    "Building the deployment layer — the FastAPI backend, the prediction pipeline, "
    "the React frontend — added a dimension to the project that notebooks alone "
    "cannot provide. Debugging model loading failures, resolving Python version "
    "conflicts, and adding input validation are real software engineering challenges "
    "that any production ML system has to solve. Working through them gave me a much "
    "clearer picture of the gap between a trained model and something actually useful.", BODY))

story.append(Paragraph("Future Directions", H2))
story.append(note_box([
    "<b>Larger dataset:</b>  With thousands of labeled articles, regularization differences "
    "would become more pronounced, and the 1D CNN would likely close the accuracy gap "
    "with the Feedforward NN because the Embedding layer would have sufficient data to "
    "learn meaningful word representations.",
    "<b>Pre-trained word embeddings:</b>  Initializing the CNN's Embedding layer with "
    "GloVe or Word2Vec vectors — trained on billions of words — would dramatically "
    "improve CNN performance on small datasets by giving the model a head start on "
    "understanding word semantics.",
    "<b>Recurrent architectures (LSTM / GRU):</b>  Long-range dependencies in articles — "
    "a claim made in the first paragraph that contradicts something in the last — are "
    "invisible to both TF-IDF and CNNs. Recurrent networks process sequences step-by-step "
    "and can theoretically capture these across-article patterns.",
    "<b>BERT fine-tuning:</b>  With a large enough dataset, fine-tuning a pre-trained "
    "transformer would represent the current state of the art. BERT understands context "
    "bidirectionally — it can distinguish 'bank' near 'river' from 'bank' near 'loan' "
    "automatically — a capability none of the models in this project possess.",
], bg=GOLD_LT, border=GOLD))

# ── REFERENCES ────────────────────────────────────────────────────────────────
story.append(section_header("", "References"))
for r in [
    "[1]  CSE 589 Neural Networks Lecture Notes, Lectures 2–7, Mustafa Kemal University, 2026.",
    "[2]  F. Rosenblatt, 'The Perceptron: A Probabilistic Model for Information Storage and "
          "Organization in the Brain,' Psychological Review, vol. 65, no. 6, pp. 386–408, 1958.",
    "[3]  D. P. Kingma and J. Ba, 'Adam: A Method for Stochastic Optimization,' "
          "International Conference on Learning Representations (ICLR), 2015.",
    "[4]  N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, "
          "'Dropout: A Simple Way to Prevent Neural Networks from Overfitting,' "
          "Journal of Machine Learning Research, vol. 15, pp. 1929–1958, 2014.",
    "[5]  Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, 'Gradient-Based Learning Applied "
          "to Document Recognition,' Proceedings of the IEEE, vol. 86, no. 11, 1998.",
    "[6]  A. L. Maas, R. E. Daly, P. T. Pham, et al., 'Learning Word Vectors for Sentiment "
          "Analysis,' Proceedings of ACL-HLT, pp. 142–150, 2011.",
    "[7]  TensorFlow / Keras Documentation, tensorflow.org/api_docs",
    "[8]  FastAPI Documentation, fastapi.tiangolo.com",
    "[9]  Scikit-learn Documentation — TfidfVectorizer, scikit-learn.org",
]:
    story.append(Paragraph(r, BODY_L))
    story.append(Spacer(1, 3))

story.append(Spacer(1, 20))
story.append(HRFlowable(width="100%", thickness=0.5, color=DIVIDER))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "Abdullah Mohammed Sindi  ·  Student ID: 200044933  ·  "
    "CSE 589 Neural Networks  ·  Mustafa Kemal University  ·  August 2026",
    SMALL))

# ── BUILD ─────────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=1.8*cm, rightMargin=1.8*cm,
    topMargin=1.7*cm, bottomMargin=1.8*cm,
    title="Fake News Detection using Deep Learning — Project Report",
    author="Abdullah Mohammed Sindi",
)
doc.build(story, onFirstPage=draw_cover, onLaterPages=draw_page)
print(f"Report saved: {OUTPUT}")
