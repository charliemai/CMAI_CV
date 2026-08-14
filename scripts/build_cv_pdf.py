from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "cv.pdf"

INK = colors.HexColor("#17242B")
INK_SOFT = colors.HexColor("#31434B")
MUTED = colors.HexColor("#65747A")
TEAL = colors.HexColor("#075B61")
LINE = colors.HexColor("#D4DFDE")
PANEL = colors.HexColor("#F4F6F3")


def esc(value: str) -> str:
    return escape(value)


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="PdfName",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=24,
        textColor=INK,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=13,
        textColor=TEAL,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfContact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.5,
        leading=9.5,
        textColor=MUTED,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfSection",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=10,
        textColor=TEAL,
        spaceBefore=5,
        spaceAfter=3,
        uppercase=True,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.4,
        leading=10.5,
        textColor=INK_SOFT,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfSmall",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.4,
        leading=9.1,
        textColor=INK_SOFT,
        spaceAfter=1.5,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfSmallMuted",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.2,
        leading=8.8,
        textColor=MUTED,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfRole",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=10.8,
        textColor=INK,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfMetricValue",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=14,
        textColor=TEAL,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfMetricLabel",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=6.8,
        leading=8,
        textColor=MUTED,
    )
)


def p(text: str, style: str = "PdfBody") -> Paragraph:
    return Paragraph(text, styles[style])


def bullet(text: str) -> Paragraph:
    return Paragraph("<bullet>&bull;</bullet>" + esc(text), styles["PdfSmall"])


def section(title: str) -> list[object]:
    return [
        p(esc(title.upper()), "PdfSection"),
        HRFlowable(width="100%", thickness=0.55, color=LINE, spaceBefore=0, spaceAfter=4),
    ]


def role_block(
    company: str,
    role: str,
    period: str,
    location: str,
    summary: str,
    bullets: list[str],
) -> list[object]:
    heading = p(
        f"<b>{esc(role)}</b> <font color=\"{MUTED.hexval()}\">at {esc(company)}</font>",
        "PdfRole",
    )
    meta = p(f"{esc(period)} - {esc(location)}", "PdfSmallMuted")
    story: list[object] = [heading, meta, p(esc(summary), "PdfSmall")]
    story.extend(bullet(item) for item in bullets)
    story.append(Spacer(1, 2.5))
    return [KeepTogether(story)]


def project_line(title: str, status: str, text: str) -> list[object]:
    return [
        p(f"<b>{esc(title)}</b> <font color=\"{TEAL.hexval()}\">- {esc(status)}</font>", "PdfSmall"),
        p(esc(text), "PdfSmallMuted"),
    ]


class ResumeDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs: object) -> None:
        super().__init__(filename, **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates([PageTemplate(id="resume", frames=[frame], onPage=draw_page)])


def draw_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.55)
    canvas.line(doc.leftMargin, 14 * mm, A4[0] - doc.rightMargin, 14 * mm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 9.5 * mm, "Charlie Mai - Cloud / DevOps / Production Reliability")
    canvas.drawRightString(A4[0] - doc.rightMargin, 9.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build() -> None:
    doc = ResumeDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=13 * mm,
        bottomMargin=19 * mm,
        title="Charlie Mai | Cloud, DevOps & Production Reliability Engineer",
        author="Charlie Mai",
        subject="Recruiter-first technical CV",
    )

    story: list[object] = []
    story.extend(
        [
            p("Charlie Mai", "PdfName"),
            p("Cloud, DevOps &amp; Production Reliability Engineer", "PdfTitle"),
            p(
                '<link href="mailto:me@cmai.ai" color="#075B61">me@cmai.ai</link>  |  Dublin, Ireland  |  '
                '<link href="https://www.linkedin.com/in/charlie-mai/" color="#075B61">linkedin.com/in/charlie-mai</link>  |  '
                '<link href="https://github.com/charliemai" color="#075B61">github.com/charliemai</link>  |  '
                '<link href="https://cv.cmai.ai/" color="#075B61">cv.cmai.ai</link>',
                "PdfContact",
            ),
        ]
    )

    story.extend(section("Profile"))
    story.append(
        p(
            "Cloud, DevOps and production-reliability engineer with 15+ years across software delivery, distributed systems, technical leadership and production operations. Former AWS Cloud Support Engineer II and CloudFront SME with deep experience in incident investigation, root-cause analysis and customer-facing technical resolution. Currently operating AWS-based systems and building practical automation for complex integration and support workflows. Applies AI selectively to evidence-grounded troubleshooting and operational decision support.",
            "PdfBody",
        )
    )

    story.extend(section("Core capabilities"))
    capabilities = [
        [
            p("<b>Production reliability</b><br/>Incident response, RCA, observability, failure analysis", "PdfSmall"),
            p("<b>Cloud and distributed systems</b><br/>AWS, Lambda, Step Functions, EventBridge, CloudFront, S3, Route 53, IAM, WAF", "PdfSmall"),
        ],
        [
            p("<b>DevOps and automation</b><br/>Python, CI/CD, test automation, release support, infrastructure automation", "PdfSmall"),
            p("<b>Integration and backend</b><br/>REST APIs, PostgreSQL, event-driven architecture, diagnostic tooling", "PdfSmall"),
        ],
        [
            p("<b>Applied AI</b><br/>RAG, retrieval evaluation, evidence-grounded assistants, human-in-the-loop design", "PdfSmall"),
            p("<b>Target opportunities</b><br/>Cloud, DevOps, Production Reliability, Platform Engineering and SRE-aligned roles in Ireland and the EU", "PdfSmall"),
        ],
    ]
    capability_table = Table(capabilities, colWidths=[(A4[0] - 34 * mm) / 2] * 2, hAlign="LEFT")
    capability_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PANEL),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(capability_table)

    story.extend(section("Selected proof"))
    metrics = [
        [p("15+", "PdfMetricValue"), p("440k+", "PdfMetricValue"), p("Top 1", "PdfMetricValue"), p("457", "PdfMetricValue")],
        [
            p("years across engineering and operations", "PdfMetricLabel"),
            p("civic reports handled by a public platform", "PdfMetricLabel"),
            p("customer satisfaction within AWS support team", "PdfMetricLabel"),
            p("support resolves; Top 2 case performance", "PdfMetricLabel"),
        ],
    ]
    metric_table = Table(metrics, colWidths=[(A4[0] - 34 * mm) / 4] * 4, hAlign="LEFT")
    metric_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    story.append(metric_table)

    story.extend(section("Experience"))
    story.extend(
        role_block(
            "National Broadband Ireland",
            "IT DevOps Support Engineer",
            "Feb 2025 - Present",
            "Dublin, Ireland",
            "Operate and troubleshoot event-driven AWS systems and commercial platforms, with a focus on production reliability and actionable diagnostics.",
            [
                "Operate event-driven AWS systems integrating Lambda, Step Functions, EventBridge, API integrations, PostgreSQL and commercial platforms.",
                "Investigate production incidents, integration failures and recurring defects using logs, data analysis and evidence-driven RCA.",
                "Build repeatable test, deployment and diagnostic workflows; develop Python automation and observability tooling.",
            ],
        )
    )
    story.extend(
        role_block(
            "Amazon Web Services (AWS)",
            "Cloud Support Engineer II / Cloud Support Engineer",
            "Jan 2022 - Mar 2024",
            "Dublin, Ireland",
            "Progressed to Cloud Support Engineer II within 21 months and became a CloudFront SME while resolving complex distributed-cloud issues.",
            [
                "Resolved 457 complex AWS support cases across CloudFront, S3, Route 53, API Gateway, Lambda, IAM, WAF, SES and media services.",
                "Recognised as Top 1 in customer satisfaction and Top 2 in case performance within the cloud support team.",
                "Accredited as a CloudFront SME; contributed to mentoring, enablement, documentation and hiring.",
            ],
        )
    )
    story.extend(
        role_block(
            "VIVERSE",
            "Business Programme Manager",
            "Apr 2024 - Feb 2025",
            "Dublin, Ireland",
            "Led cross-functional delivery and customer-facing technical coordination for product and enterprise initiatives across EMEA.",
            ["Managed parallel workstreams across engineering, R&D and business stakeholders; aligned scope, requirements and delivery plans."],
        )
    )

    story.append(PageBreak())
    story.extend(section("Experience continued"))
    story.extend(
        role_block(
            "Verizon Media Platform",
            "Solutions Engineer / Delivery Customer Support Engineer",
            "Apr 2019 - Aug 2021",
            "Taiwan",
            "Delivered customer-facing CDN solutions, implementation support and incident coordination for enterprise media customers.",
            [
                "Analysed traffic logs and CDN performance to support production troubleshooting and service optimisation.",
                "Managed incident, problem and change workflows with regional teams during onboarding and production issues.",
                "Supported enterprise implementations, PoCs and cross-regional delivery with engineering and commercial stakeholders.",
            ],
        )
    )
    story.extend(
        role_block(
            "CATCHPLAY",
            "Technical Lead",
            "May 2017 - Apr 2019",
            "Taipei / Jakarta",
            "Led Android TV and set-top-box delivery, partner integrations and cross-platform technical alignment across Android, iOS and web teams.",
            [
                "Built CI practices and helped improve application architecture, performance and user experience.",
                "Supported streaming SDK integration and multi-region product delivery across Taiwan and Indonesia.",
            ],
        )
    )
    story.extend(
        role_block(
            "Earlier engineering and technical leadership",
            "Team Lead, Mobile / Android Developer / IT Lead",
            "2009 - 2017",
            "Taiwan",
            "Built software products and led mobile, backend and application delivery across several technology companies.",
            ["Led mobile development, CI setup, technical capability building and application architecture improvements across web, Java enterprise and internal systems."],
        )
    )

    story.extend(section("Selected projects"))
    story.extend(project_line("RAG Troubleshooting Assistant", "Active lab", "Evidence-grounded operational AI prototype exploring ingestion, retrieval, source visibility, uncertainty and useful next actions. No production adoption claim."))
    story.extend(project_line("Parking Violation Reporter", "Public impact case study", "Citizen reporting platform that handled more than 440,000 reports; related social-enterprise concept received a U-START Silver Medal."))
    story.extend(project_line("Vouchgether", "Historical case study", "Original mobile product case study using the documented React Native and serverless AWS foundation; current live architecture is not asserted."))

    story.extend(section("Education"))
    education_rows = [
        [p("<b>MSc in Computer Science (Negotiated Learning), Artificial Intelligence</b><br/>University College Dublin - Sep 2025 - Aug 2027; part-time study, expected 2027.", "PdfSmall"), p("<b>Certificate in Artificial Intelligence</b><br/>University of Limerick - Sep 2025 - Jan 2026; First Class Honours.", "PdfSmall")],
        [p("<b>Master of Information Technology</b><br/>Queensland University of Technology - 2007 - 2008; GPA 6.5 / 7.0.", "PdfSmall"), p("<b>Bachelor of Civil Engineering</b><br/>National Chiao Tung University - 2003 - 2006.", "PdfSmall")],
    ]
    education_table = Table(education_rows, colWidths=[(A4[0] - 34 * mm) / 2] * 2, hAlign="LEFT")
    education_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(education_table)

    story.extend(section("Certifications and recognition"))
    story.append(p("AWS Certified Solutions Architect - Associate  |  U-START Social Enterprise competition - Silver Medal  |  Earlier Java, Java EE and Android certifications", "PdfSmall"))

    doc.build(story)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()
