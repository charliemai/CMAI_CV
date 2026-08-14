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
        fontSize=9.0,
        leading=11.4,
        textColor=INK_SOFT,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfSmall",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.8,
        leading=9.6,
        textColor=INK_SOFT,
        spaceAfter=1.5,
    )
)
styles.add(
    ParagraphStyle(
        name="PdfSmallMuted",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.6,
        leading=9.3,
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
styles.add(
    ParagraphStyle(
        name="PdfMetricRow",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.4,
        leading=10.2,
        textColor=INK_SOFT,
        spaceAfter=0,
    )
)


def p(text: str, style: str = "PdfBody") -> Paragraph:
    return Paragraph(text, styles[style])


def bullet(text: str) -> Paragraph:
    return Paragraph("- " + esc(text), styles["PdfSmall"])


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
    group_title: bool = False,
) -> list[object]:
    if group_title:
        heading = p(f"<b>{esc(company)}</b>", "PdfRole")
        role_line = p(esc(role), "PdfSmallMuted")
    else:
        heading = p(
            f"<b>{esc(role)}</b> <font color=\"{MUTED.hexval()}\">at {esc(company)}</font>",
            "PdfRole",
        )
        role_line = None
    meta = p(f"{esc(period)} - {esc(location)}", "PdfSmallMuted")
    story: list[object] = [heading]
    if role_line is not None:
        story.append(role_line)
    story.extend([meta, p(esc(summary), "PdfSmall")])
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
        [p('<font color="#075B61"><b>15+</b></font> - years across engineering and operations', "PdfMetricRow")],
        [p('<font color="#075B61"><b>440k+</b></font> - civic reports handled by a public platform', "PdfMetricRow")],
        [p('<font color="#075B61"><b>#1</b></font> - customer satisfaction ranking within an AWS support team', "PdfMetricRow")],
        [p('<font color="#075B61"><b>457</b></font> - AWS support cases resolved; Top 2 case-performance ranking', "PdfMetricRow")],
    ]
    metric_table = Table(metrics, colWidths=[A4[0] - 34 * mm], hAlign="LEFT")
    metric_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
                ("BACKGROUND", (0, 0), (-1, -1), PANEL),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
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
                "Support production releases, maintenance activities and cross-system workflows involving cloud services, internal platforms and third-party applications.",
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
            [
                "Managed parallel workstreams across engineering, R&D and business stakeholders; aligned scope, requirements and delivery plans.",
                "Connected technical teams and business owners so decisions moved from ambiguity to delivery.",
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
                "Ranked #1 for customer satisfaction and Top 2 for case performance within an AWS cloud support team.",
                "Accredited as a CloudFront SME; contributed to mentoring, enablement, documentation and hiring.",
                "Worked with customers, architects and TAMs to reproduce issues, provide root-cause analysis and support critical incident communications.",
            ],
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
            "Earlier Engineering & Technical Leadership",
            "Team Lead, Mobile / Android Developer / IT Lead",
            "2009 - 2017",
            "Taiwan",
            "Built software products and led mobile, backend and application delivery across several technology companies.",
            [
                "Led native mobile development, CI setup, technical capability building and application architecture improvements.",
                "Worked across Android, iOS, web, hybrid applications, Java enterprise systems and internal business platforms.",
            ],
            group_title=True,
        )
    )

    story.extend(section("Selected projects"))
    story.extend(project_line("RAG Troubleshooting Assistant", "Active lab", "Python service prototype for document ingestion, semantic retrieval, source visibility and human review; evaluation contract covers missing context, ambiguity, abstention and grounded next actions. No production adoption claim."))
    story.extend(project_line("Parking Violation Reporter", "Public impact case study", "Mobile workflow: capture violation details, attach evidence, submit a civic report and receive status or feedback; the platform handled more than 440,000 reports and the related concept received a U-START Silver Medal."))
    story.extend(project_line("Vouchgether", "Historical case study", "Documented flow using React Native, Cognito, Lambda, S3 and DynamoDB across voucher discovery, sharing and claiming; historical version only, with no current live architecture claim."))

    story.extend(section("Operating principles"))
    story.extend(
        [
            bullet("Make failure behaviour visible and the next engineering action explicit."),
            bullet("Keep measured evidence, historical context and current status separate."),
            bullet("Use human review when an automated answer could change a high-consequence decision."),
            bullet("Prefer reproducible checks and small automation before adding platform complexity."),
        ]
    )

    story.extend(section("Education"))
    story.extend(
        [
            p("<b>MSc in Computer Science (Negotiated Learning)</b><br/>University College Dublin - Sep 2025 - Aug 2027; part-time study with an AI-focused pathway; expected 2027.", "PdfSmall"),
            p("<b>Certificate in Artificial Intelligence</b><br/>University of Limerick - Sep 2025 - Jan 2026; First Class Honours.", "PdfSmall"),
            p("<b>Master of Information Technology</b><br/>Queensland University of Technology - 2007 - 2008; GPA 6.5 / 7.0; Dean's List and scholarship recognition.", "PdfSmall"),
            p("<b>Bachelor of Civil Engineering</b><br/>National Chiao Tung University - 2003 - 2006.", "PdfSmall"),
        ]
    )

    story.extend(section("Certifications and recognition"))
    story.extend(
        [
            bullet("AWS Certified Solutions Architect - Associate"),
            bullet("U-START Social Enterprise competition - Silver Medal"),
            bullet("Earlier Java, Java EE and Android certifications"),
            bullet("Languages: English (Full professional); Mandarin (Native or bilingual)"),
        ]
    )

    doc.build(story)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build()
