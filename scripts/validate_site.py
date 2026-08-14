"""Small, dependency-light regression checks for the public CV site."""

from __future__ import annotations

import base64
import json
import re
import sys
import zlib
from pathlib import Path

try:
    from pypdf import PdfReader
except ModuleNotFoundError:  # Keep the repository check runnable without a new dependency.
    PdfReader = None


ROOT = Path(__file__).resolve().parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def fallback_pdf_inspect(path: Path) -> tuple[int, str, str]:
    """Inspect the generated ReportLab PDF with only Python's stdlib available."""

    raw_pdf = path.read_bytes()
    page_count = len(re.findall(rb"/Type\s*/Page\b", raw_pdf))
    streams: list[bytes] = []
    for match in re.finditer(rb"stream\r?\n", raw_pdf):
        end = raw_pdf.find(b"endstream", match.end())
        if end < 0:
            continue
        encoded = raw_pdf[match.end() : end].strip()
        decoded: bytes | None = None
        for candidate in (encoded,):
            try:
                decoded = zlib.decompress(candidate)
                break
            except zlib.error:
                pass
            try:
                decoded = zlib.decompress(base64.a85decode(candidate, adobe=True))
                break
            except (ValueError, zlib.error):
                pass
        if decoded:
            streams.append(decoded)

    content = b"\n".join(streams)
    text_parts = []
    for match in re.finditer(rb"\(((?:\\.|[^\\)])*)\)\s*Tj", content):
        value = match.group(1)
        value = value.replace(b"\\(", b"(").replace(b"\\)", b")").replace(b"\\\\", b"\\")
        text_parts.append(value.decode("latin-1"))
    title_match = re.search(rb"/Title \((.*?)\)", raw_pdf)
    title = title_match.group(1).decode("latin-1") if title_match else ""
    return page_count, "\n".join(text_parts), title


def main() -> int:
    failures: list[str] = []
    source_paths = [
        *sorted((ROOT / "src").rglob("*.astro")),
        *sorted((ROOT / "src").rglob("*.ts")),
        *sorted((ROOT / "src").rglob("*.js")),
        ROOT / "vercel.json",
        ROOT / "scripts" / "build_cv_pdf.py",
    ]
    source = "\n".join(read_text(path) for path in source_paths if path.exists())

    required = {
        "recruiter-first title": "Cloud, DevOps & Production Reliability Engineer",
        "current role": "National Broadband Ireland",
        "former CloudFront expertise": "CloudFront SME",
        "UCD canonical title": "MSc in Computer Science (Negotiated Learning)",
        "UCD pathway wording": "AI-focused pathway",
        "experience proof": "15+",
        "public impact proof": "440k+",
        "AWS support proof": "457",
        "natural AWS ranking wording": "Ranked #1 for customer satisfaction",
        "natural AWS case wording": "Resolved 457 complex AWS support cases",
        "permanent redirect config": '"permanent": true',
    }
    for label, needle in required.items():
        if needle not in source:
            fail(f"missing {label}: {needle}", failures)

    forbidden = {
        "mobile number": "0874614368",
        "stale duration": "16 years",
        "encoding artefact": "-- IT professional",
        "old positioning": "living portfolio",
        "old positioning 2": "growth log",
        "incorrect UCD title": "MSc in Computer Science (Negotiated Learning), Artificial Intelligence",
        "unscoped AWS ranking": "AWS #1",
        "awkward Top 1 wording": "Top 1",
        "awkward support wording": "support resolves",
        "fake earlier employer": "at Earlier engineering and technical leadership",
        "old earlier-career heading": "Earlier engineering and technical leadership",
        "AI-first navigation": "Cloud / DevOps / AI",
        "placeholder link": 'href="#"',
    }
    source_lower = source.casefold()
    for label, needle in forbidden.items():
        if needle.casefold() in source_lower:
            fail(f"forbidden {label}: {needle}", failures)

    redirect_config = read_text(ROOT / "vercel.json")
    for source_path, destination in {
        "/insights": "/writing/",
        "/blog/": "/writing/",
        "/blog/tag/Learning": "/learning/",
        "/services/": "/projects/",
        "/projects/rag-troubleshooting-gpt-assistant": "/projects/rag-troubleshooting-assistant/",
        "/blog/self-evolving-ai-agents-my-vision-and-challenges": "/lab/",
        "/blog/ul-ai-certificate-what-i-learned-and-how-it-changed-my-builds": "/learning/",
    }.items():
        if f'"source": "{source_path}"' not in redirect_config or f'"destination": "{destination}"' not in redirect_config:
            fail(f"missing redirect {source_path} -> {destination}", failures)

    dist = ROOT / "dist"
    built_routes = [
        "index.html",
        "cv/index.html",
        "projects/index.html",
        "projects/rag-troubleshooting-assistant/index.html",
        "projects/parking-reporter/index.html",
        "projects/vouchgether/index.html",
        "writing/index.html",
        "lab/index.html",
        "learning/index.html",
        "404.html",
    ]
    for route in built_routes:
        if not (dist / route).exists():
            fail(f"missing built route: {route}", failures)

    if dist.exists():
        built_source = "\n".join(
            read_text(path)
            for path in sorted(dist.rglob("*.html"))
            if path.exists()
        )
        if "<h1" not in built_source:
            fail("built HTML has no h1", failures)
        if "0874614368" in built_source:
            fail("mobile number leaked into built HTML", failures)
        if "href=\"#\"" in built_source:
            fail("placeholder link leaked into built HTML", failures)
        for route in built_routes:
            route_html_path = dist / route
            route_html = read_text(route_html_path)
            if len(re.findall(r"<h1\b", route_html)) != 1:
                fail(f"{route} must have exactly one logical h1", failures)
        if re.search(r"<div[^>]*class=\"tag-list", built_source):
            fail("tag lists must use semantic ul elements", failures)
        if len(re.findall(r"<ul[^>]*class=\"tag-list", built_source)) < 10:
            fail("semantic tag-list coverage is incomplete", failures)
        if "technical-artefact" not in built_source or "flow-diagram" not in built_source:
            fail("flagship project artefacts are missing from built HTML", failures)
        if "MSc in Computer Science (Negotiated Learning), Artificial Intelligence" in built_source:
            fail("incorrect UCD title leaked into built HTML", failures)
        if "MSc in Computer Science (Negotiated Learning)" not in built_source:
            fail("canonical UCD title missing from built HTML", failures)
        if '<link rel="canonical" href="https://cv.cmai.ai/"' not in built_source:
            fail("homepage canonical URL is missing", failures)
        if not (dist / "sitemap-index.xml").exists():
            fail("generated sitemap is missing", failures)
        if not (dist / "robots.txt").exists():
            fail("robots.txt is missing from the built site", failures)
        for raw_json in re.findall(r'<script type="application/ld\+json">(.*?)</script>', built_source, flags=re.DOTALL):
            try:
                schema = json.loads(raw_json)
            except json.JSONDecodeError as error:
                fail(f"invalid JSON-LD: {error}", failures)
                continue
            if schema.get("@type") != "Person":
                fail("Person JSON-LD is missing", failures)
            if "0874614368" in raw_json:
                fail("phone number leaked into JSON-LD", failures)

        for asset in sorted(set(re.findall(r'(?:src|href)="(/[^"#?]+\.(?:svg|JPG|jpg|png|pdf))', built_source))):
            if not (ROOT / "public" / asset.lstrip("/")).exists():
                fail(f"broken local asset: {asset}", failures)

    pdf_path = ROOT / "public" / "cv.pdf"
    if not pdf_path.exists():
        fail("public/cv.pdf is missing", failures)
    else:
        if PdfReader is not None:
            reader = PdfReader(str(pdf_path))
            page_count = len(reader.pages)
            pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
            metadata_title = str((reader.metadata or {}).get("/Title", ""))
        else:
            page_count, pdf_text, metadata_title = fallback_pdf_inspect(pdf_path)
        pdf_text_normalized = re.sub(r"\s+", " ", pdf_text).strip()
        if page_count != 2:
            fail(f"CV PDF must have exactly 2 pages, got {page_count}", failures)
        for page in reader.pages if PdfReader is not None else []:
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            if abs(width - 595.2756) > 1 or abs(height - 841.8898) > 1:
                fail(f"CV PDF page is not A4: {width} x {height}", failures)
        for label, needle in {
            "mobile number in PDF": "0874614368",
            "stale duration in PDF": "16 years",
            "PDF separator artefact": "--",
            "incorrect UCD title in PDF": "MSc in Computer Science (Negotiated Learning), Artificial Intelligence",
            "awkward Top 1 wording in PDF": "Top 1",
            "awkward support wording in PDF": "support resolves",
            "fake earlier employer in PDF": "at Earlier engineering and technical leadership",
        }.items():
            if needle in pdf_text:
                fail(f"{label}: {needle}", failures)
        for label, needle in {
            "canonical UCD title in PDF": "MSc in Computer Science (Negotiated Learning)",
            "AI pathway wording in PDF": "AI-focused pathway",
            "natural ranking wording in PDF": "Ranked #1 for customer satisfaction",
            "natural case wording in PDF": "Resolved 457 complex AWS support cases",
            "earlier-career heading in PDF": "Earlier Engineering & Technical Leadership",
        }.items():
            if needle not in pdf_text:
                fail(f"missing {label}: {needle}", failures)
        for proof_row in [
            "15+ - years across engineering and operations",
            "440k+ - civic reports handled by a public platform",
            "#1 - customer satisfaction ranking within an AWS support team",
            "457 - AWS support cases resolved; Top 2 case-performance ranking",
        ]:
            if proof_row not in pdf_text_normalized:
                fail(f"PDF proof value and label are not adjacent: {proof_row}", failures)
        experience_order = [
            "National Broadband Ireland",
            "VIVERSE",
            "Amazon Web Services (AWS)",
            "Verizon Media Platform",
            "CATCHPLAY",
            "Earlier Engineering & Technical Leadership",
        ]
        positions = [pdf_text.find(item) for item in experience_order]
        if any(position < 0 for position in positions) or positions != sorted(positions):
            fail(f"PDF experience order is not reverse chronological: {positions}", failures)
        if len(pdf_text.strip()) < 3000:
            fail("CV PDF text extraction is unexpectedly sparse", failures)
        if "Cloud, DevOps & Production Reliability Engineer" not in metadata_title:
            fail("PDF metadata title is not recruiter-first", failures)

    if failures:
        print("VALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("VALIDATION PASSED")
    print(f"- source assertions: {len(required)} required / {len(forbidden)} forbidden")
    print(f"- built routes: {len(built_routes)}")
    print("- PDF: 2 pages, searchable text, metadata and public-safe content")
    return 0


if __name__ == "__main__":
    sys.exit(main())
