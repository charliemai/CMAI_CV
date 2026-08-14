export type ExperienceEntry = {
  company: string;
  position: string;
  period: string;
  location: string;
  summary: string;
  bullets: string[];
};

export type ProjectEntry = {
  slug: string;
  title: string;
  eyebrow: string;
  problem: string;
  summary: string;
  evidence: string;
  role: string;
  stack: string[];
  image: string;
  status: string;
  featured?: boolean;
  href?: string;
  context: string;
  ownership: string;
  technicalShape: string;
  decisions: string[];
  trustBoundaries: string[];
  testing: string[];
  outcome: string;
  currentStatus: string;
  next: string;
};

export type WritingEntry = {
  slug: string;
  title: string;
  date: string;
  tag: string;
  summary: string;
  status: "Planned" | "In development";
};

export const profile = {
  name: "Charlie Mai",
  shortName: "Charlie",
  title: "Cloud, DevOps & Production Reliability Engineer",
  currentRole: "IT DevOps Support Engineer at National Broadband Ireland",
  descriptor: "Former AWS CloudFront SME",
  location: "Dublin, Ireland",
  email: "me@cmai.ai",
  image: "/profile.JPG",
  cv: "/cv.pdf",
  links: {
    github: "https://github.com/charliemai",
    linkedin: "https://www.linkedin.com/in/charlie-mai/",
    portfolio: "https://cv.cmai.ai/",
  },
  summary:
    "I operate AWS-based systems, investigate complex production failures, and build practical automation that makes incidents easier to diagnose and systems easier to run.",
  availability:
    "Interested in selected Cloud, DevOps, Production Reliability, Platform Engineering and SRE-aligned opportunities across Ireland and the EU.",
  targetRoles: [
    "Cloud Engineering",
    "DevOps",
    "Production Reliability",
    "Platform Engineering",
    "SRE-aligned operations",
  ],
};

export const metrics = [
  { value: "15+", label: "years across engineering, cloud operations and technical leadership" },
  { value: "440k+", label: "civic reports handled by a public-facing platform" },
  { value: "Top 1", label: "customer satisfaction recognition within an AWS support team" },
  { value: "457", label: "AWS support resolves with Top 2 case-performance recognition" },
];

export const focusAreas = [
  {
    title: "Production reliability and incident response",
    description:
      "Incident investigation, root-cause analysis, observability, change support and calm communication when systems are under pressure.",
    tags: ["Incident response", "RCA", "Observability"],
  },
  {
    title: "AWS, serverless and CDN systems",
    description:
      "Hands-on troubleshooting across AWS serverless services, CloudFront and the distributed-system boundaries around them.",
    tags: ["AWS", "CloudFront", "Distributed systems"],
  },
  {
    title: "DevOps and operational automation",
    description:
      "Repeatable test, deployment and diagnostic workflows that reduce recurring operational effort and make failure behaviour visible.",
    tags: ["Python", "CI/CD", "Automation"],
  },
  {
    title: "Integration and backend troubleshooting",
    description:
      "Evidence-driven work across APIs, event-driven workflows, PostgreSQL and commercial platforms without losing sight of the user job.",
    tags: ["APIs", "PostgreSQL", "Event-driven"],
  },
  {
    title: "Applied AI for operational evidence",
    description:
      "RAG and assistant experiments that expose sources, uncertainty and useful next actions rather than returning opaque answers.",
    tags: ["RAG", "Evaluation", "Human-in-the-loop"],
  },
];

export const skillGroups = [
  {
    title: "Production reliability",
    items: ["Incident response", "Root-cause analysis", "Observability", "Production troubleshooting", "Failure analysis"],
  },
  {
    title: "Cloud and distributed systems",
    items: ["AWS", "Lambda", "Step Functions", "EventBridge", "API Gateway", "S3", "CloudFront", "Route 53", "IAM", "WAF"],
  },
  {
    title: "DevOps and operational automation",
    items: ["Python", "CI/CD", "Infrastructure automation", "Test automation", "Change and release support"],
  },
  {
    title: "Integration and backend",
    items: ["REST APIs", "PostgreSQL", "Event-driven architecture", "Commercial platform integration", "Diagnostic tooling"],
  },
  {
    title: "Applied AI",
    items: ["RAG", "Retrieval evaluation", "Evidence-grounded assistants", "Human-in-the-loop design"],
  },
];

export const experience: ExperienceEntry[] = [
  {
    company: "National Broadband Ireland",
    position: "IT DevOps Support Engineer",
    period: "Feb 2025 - Present",
    location: "Dublin, Ireland",
    summary:
      "Operate and troubleshoot event-driven AWS systems and commercial platforms, with a focus on production reliability and actionable diagnostics.",
    bullets: [
      "Operate and troubleshoot event-driven AWS systems integrating Lambda, Step Functions, EventBridge, API integrations, PostgreSQL and commercial platforms.",
      "Investigate production incidents, integration failures and recurring defects using logs, data analysis and evidence-driven root-cause analysis.",
      "Build repeatable test, deployment and diagnostic workflows across multiple environments.",
      "Develop Python automation and observability tooling that reduces recurring operational effort and improves troubleshooting.",
      "Support production releases, maintenance activities and cross-system workflows involving cloud services, internal platforms and third-party applications.",
    ],
  },
  {
    company: "VIVERSE",
    position: "Business Programme Manager",
    period: "Apr 2024 - Feb 2025",
    location: "Dublin, Ireland",
    summary:
      "Led cross-functional delivery and customer-facing technical coordination for product and enterprise initiatives across EMEA.",
    bullets: [
      "Managed parallel workstreams across engineering, R&D and business stakeholders.",
      "Aligned scope, requirements and delivery plans for complex enterprise initiatives.",
      "Connected technical teams and business owners so decisions moved from ambiguity to delivery.",
    ],
  },
  {
    company: "Amazon Web Services (AWS)",
    position: "Cloud Support Engineer II / Cloud Support Engineer",
    period: "Jan 2022 - Mar 2024",
    location: "Dublin, Ireland",
    summary:
      "Progressed to Cloud Support Engineer II within 21 months and became a CloudFront Subject Matter Expert while resolving complex distributed-cloud issues.",
    bullets: [
      "Resolved 457 complex AWS support cases across CloudFront, S3, Route 53, API Gateway, Lambda, IAM, WAF, SES and media services.",
      "Recognised as Top 1 in customer satisfaction and Top 2 in case performance within the cloud support team.",
      "Accredited as a CloudFront Subject Matter Expert and contributed to mentoring, enablement, documentation and hiring.",
      "Worked with customers, architects and TAMs to reproduce issues, provide root-cause analysis and support critical incident communications.",
    ],
  },
  {
    company: "Verizon Media Platform",
    position: "Solutions Engineer / Delivery Customer Support Engineer",
    period: "Apr 2019 - Aug 2021",
    location: "Taiwan",
    summary:
      "Delivered customer-facing CDN solutions, implementation support and incident coordination for enterprise media customers.",
    bullets: [
      "Analysed traffic logs and CDN performance to support production troubleshooting and service optimisation.",
      "Managed incident, problem and change workflows with regional teams during onboarding and production issues.",
      "Supported enterprise implementations, PoCs and cross-regional delivery with engineering and commercial stakeholders.",
    ],
  },
  {
    company: "CATCHPLAY",
    position: "Technical Lead",
    period: "May 2017 - Apr 2019",
    location: "Taipei / Jakarta",
    summary:
      "Led Android TV and set-top-box delivery, partner integrations and cross-platform technical alignment across Android, iOS and web teams.",
    bullets: [
      "Built CI practices and helped improve application architecture, performance and user experience.",
      "Supported streaming SDK integration and multi-region product delivery across Taiwan and Indonesia.",
    ],
  },
  {
    company: "Earlier engineering and technical leadership",
    position: "Team Lead, Mobile / Android Developer / IT Lead",
    period: "2009 - 2017",
    location: "Taiwan",
    summary:
      "Built software products and led mobile, backend and application delivery across several technology companies.",
    bullets: [
      "Led native Android and iOS development, CI setup, technical capability building and application architecture improvements.",
      "Worked across web, hybrid, Java enterprise, mobile and internal systems development.",
    ],
  },
];

export const education = [
  {
    institution: "University College Dublin",
    programme: "MSc in Computer Science (Negotiated Learning), Artificial Intelligence",
    period: "Sep 2025 - Aug 2027",
    note: "Part-time study; expected 2027.",
  },
  {
    institution: "University of Limerick",
    programme: "Certificate in Artificial Intelligence",
    period: "Sep 2025 - Jan 2026",
    note: "First Class Honours.",
  },
  {
    institution: "Queensland University of Technology",
    programme: "Master of Information Technology",
    period: "2007 - 2008",
    note: "GPA 6.5 / 7.0; Dean's List and scholarship recognition.",
  },
  {
    institution: "National Chiao Tung University",
    programme: "Bachelor of Civil Engineering",
    period: "2003 - 2006",
    note: "",
  },
];

export const certifications = [
  "AWS Certified Solutions Architect - Associate",
  "U-START Social Enterprise competition - Silver Medal",
  "Sun Certified Java Programmer (SCJP)",
  "Sun Certified Web Component Developer for Java EE 1.4",
  "Oracle Certified Professional, Java EE 5 Web Services Developer",
  "Android Certified Application Developer",
];

export const languages = [
  { name: "English", level: "Full professional" },
  { name: "Mandarin", level: "Native or bilingual" },
];

export const projects: ProjectEntry[] = [
  {
    slug: "rag-troubleshooting-assistant",
    title: "RAG Troubleshooting Assistant",
    eyebrow: "Applied operational AI",
    problem: "Turn technical documents and incident evidence into troubleshooting context people can inspect.",
    summary:
      "An evidence-grounded assistant experiment shaped by production-support work: retrieval, source visibility and useful next actions before conversational polish.",
    evidence: "Active lab; no production adoption claim",
    role: "Architect / builder",
    stack: ["Python", "FastAPI", "Embeddings", "Vector search", "Evaluation"],
    image: "/projects/rag-assistant.svg",
    status: "Active lab",
    featured: true,
    context:
      "Technical support teams often have the right material spread across runbooks, service notes and incident evidence. The useful question is not whether a chatbot can answer, but whether an engineer can inspect why an answer was produced and decide what to do next.",
    ownership:
      "I shaped the system around operational troubleshooting: document ingestion, retrieval, source visibility and a response format that keeps uncertainty visible.",
    technicalShape:
      "The experiment combines a Python service, document ingestion, semantic retrieval and a conversational interface. The architecture is intentionally described as a prototype rather than a deployed enterprise platform.",
    decisions: [
      "Treat retrieval quality and source visibility as first-class product behaviour.",
      "Keep evidence and uncertainty close to the suggested next action.",
      "Use production-support questions and failure modes to shape the evaluation surface.",
    ],
    trustBoundaries: [
      "Do not present an unsupported answer as an incident resolution.",
      "Keep the source material inspectable and make human review part of the workflow.",
      "Separate a useful prototype from any claim of production adoption.",
    ],
    testing: [
      "Compare retrieval results against known technical questions and expected source passages.",
      "Probe missing context, ambiguous terminology and low-confidence retrieval.",
      "Review answers for grounded evidence and actionable troubleshooting steps.",
    ],
    outcome:
      "The project demonstrates how cloud-support experience changes the design of applied AI: the result should help an engineer investigate, not merely generate fluent text.",
    currentStatus: "Active lab and research/engineering experiment.",
    next: "Add a stronger retrieval evaluation set, explicit abstention behaviour and repeatable evidence reports.",
  },
  {
    slug: "parking-reporter",
    title: "Parking Violation Reporter",
    eyebrow: "Civic technology",
    problem: "Give citizens a faster, more visible way to report traffic and environmental violations.",
    summary:
      "A citizen reporting platform that turned a real public frustration into a repeatable mobile workflow and handled more than 440,000 reports.",
    evidence: "More than 440,000 reports handled",
    role: "Founder / mobile engineer",
    stack: ["Android", "Firebase", "Push notifications", "Product delivery"],
    image: "/projects/parking-reporter.svg",
    status: "Public impact case study",
    featured: true,
    context:
      "The project addressed a concrete citizen problem: make reporting easier and make the result feel more visible and actionable. The public-facing platform ultimately handled more than 440,000 civic reports.",
    ownership:
      "I owned the reporting workflow and the product engineering needed to make it usable as a real mobile service, from the citizen interaction through delivery and feedback loops.",
    technicalShape:
      "The source-supported case study is a mobile reporting product using Android, Firebase, push notifications and product-delivery work. The public metric is scoped to reports handled by the platform, not a claim about government adoption, revenue or total users.",
    decisions: [
      "Keep the reporting journey focused on the citizen's immediate job.",
      "Use feedback and notifications to make a submitted report feel observable rather than disappearing into a form.",
      "Prioritise a simple workflow that could handle meaningful public volume.",
    ],
    trustBoundaries: [
      "Report the measured platform volume without inferring government outcomes.",
      "Keep the case study focused on product ownership and delivery rather than unsupported institutional claims.",
      "Treat public reporting as a trust-sensitive interaction that needs clear status and feedback.",
    ],
    testing: [
      "Validate the mobile reporting path and its feedback states.",
      "Test notification and submission behaviour across the supported workflow.",
      "Use real usage scale as evidence of a shipped product, not as a substitute for a reliability claim.",
    ],
    outcome:
      "More than 440,000 reports were handled through the platform. The related social-enterprise concept also received a U-START competition Silver Medal.",
    currentStatus: "Public impact case study; historical product evidence.",
    next: "Document the product's evolution and separate current public facts from historical implementation detail.",
  },
  {
    slug: "vouchgether",
    title: "Vouchgether",
    eyebrow: "Historical mobile product",
    problem: "Make voucher discovery and sharing easier to act on in a mobile-first experience.",
    summary:
      "An original product case study about discovering, sharing and claiming discount vouchers with a bounded serverless AWS foundation.",
    evidence: "Historical product case study",
    role: "Product builder / engineer",
    stack: ["React Native", "AWS Lambda", "Cognito", "S3", "DynamoDB"],
    image: "/projects/vouchgether.svg",
    status: "Historical case study",
    featured: true,
    context:
      "The available project evidence describes a mobile product for discovering, sharing and claiming discount vouchers. It is kept as an original product case study rather than presented as a claim about a current live architecture.",
    ownership:
      "I shaped the product experience and connected the mobile client to authentication, media and serverless backend services.",
    technicalShape:
      "The documented version used React Native with AWS Lambda, Cognito, S3 and DynamoDB. This description is intentionally bounded to that version; the current external product state is not asserted here.",
    decisions: [
      "Keep discovery, sharing and claiming as a single understandable user journey.",
      "Separate identity, media and application data responsibilities across the documented AWS services.",
      "Balance product iteration with the trust boundaries of user-generated voucher content.",
    ],
    trustBoundaries: [
      "Do not imply that the documented architecture is the current live product architecture.",
      "Do not infer payment, messaging or production-provider integrations without source evidence.",
      "Keep the product status explicitly historical.",
    ],
    testing: [
      "Exercise the discovery, sharing and claim flows as a mobile user journey.",
      "Check authentication, media and data boundaries independently.",
      "Review failure behaviour around user-generated content and network-dependent actions.",
    ],
    outcome:
      "The case study demonstrates product ownership, mobile delivery and practical serverless integration without overstating the current product state.",
    currentStatus: "Historical product case study; current live status not asserted.",
    next: "Refresh the case study only if a current canonical product source becomes available.",
  },
  {
    slug: "videotranslate",
    title: "VideoTranslate",
    eyebrow: "Workflow automation",
    problem: "Make a multi-stage video translation workflow easier to operate, inspect and iterate.",
    summary: "An experiment in making video translation workflows easier to operate, inspect and iterate.",
    evidence: "Applied automation to a media workflow",
    role: "Builder",
    stack: ["Python", "Media processing", "Automation", "Web UI"],
    image: "/projects/video-translate.svg",
    status: "Experiment",
    context: "A lab project for turning a repeated media workflow into clearer stages with useful failure feedback.",
    ownership: "I prototyped the workflow and focused on making each stage inspectable.",
    technicalShape: "Python-based media processing and a small web interface for reviewing output.",
    decisions: ["Prefer visible stages over opaque automation.", "Keep iteration cheap while the workflow is still experimental."],
    trustBoundaries: ["Treat output as experimental until reviewed.", "Do not claim production media delivery."],
    testing: ["Review each stage independently.", "Check failure feedback and translated output before accepting a run."],
    outcome: "A compact example of applying operational thinking to a media workflow.",
    currentStatus: "Exploration.",
    next: "Document input/output contracts and add repeatable quality checks.",
  },
  {
    slug: "argumentlab",
    title: "ArgumentLab",
    eyebrow: "Learning lab",
    problem: "Make reasoning exercises easier to compare, inspect and discuss.",
    summary: "A structured-reasoning playground for testing how people and AI systems inspect and improve arguments.",
    evidence: "Learning through small, inspectable experiments",
    role: "Researcher / builder",
    stack: ["TypeScript", "AI experiments", "Evaluation", "UX"],
    image: "/projects/argument-lab.svg",
    status: "Experiment",
    context: "A small interface for making reasoning exercises easier to compare and discuss.",
    ownership: "I designed the experiment surface and kept the evaluation questions explicit.",
    technicalShape: "A lightweight web interface with structured prompts and reviewable outputs.",
    decisions: ["Make the quality of an answer inspectable.", "Keep the experiment small enough to change quickly."],
    trustBoundaries: ["Do not treat an experiment as a benchmark claim.", "Keep human judgement in the loop."],
    testing: ["Compare outputs against explicit reasoning criteria.", "Review the interface with different argument shapes."],
    outcome: "A learning project about evaluation, UX and the limits of fluent answers.",
    currentStatus: "Learning project.",
    next: "Capture a small evaluation set and publish the method before expanding the interface.",
  },
  {
    slug: "ucd-sport-auto-booker",
    title: "UCD Sport Auto Booker",
    eyebrow: "Automation utility",
    problem: "Reduce friction in a recurring sports-booking workflow while keeping timing and failure behaviour visible.",
    summary: "A focused automation experiment for reducing friction in recurring sports-booking tasks while studying at UCD.",
    evidence: "Small automation with a clear user job",
    role: "Builder",
    stack: ["Browser automation", "Scheduling", "Reliability", "UX"],
    image: "/projects/sport-auto-booker.svg",
    status: "Personal utility",
    context: "A personal utility that maps a repetitive booking task into a small, observable automation.",
    ownership: "I mapped the workflow, timing constraints and safe failure behaviour.",
    technicalShape: "Browser automation and scheduling around a recurring booking flow.",
    decisions: ["Make timing assumptions explicit.", "Fail visibly rather than silently submitting an uncertain action."],
    trustBoundaries: ["Personal utility only.", "No claim of official UCD integration."],
    testing: ["Exercise timing and retry behaviour.", "Review the result before treating a booking attempt as successful."],
    outcome: "A small example of reliability thinking applied to everyday automation.",
    currentStatus: "Personal utility.",
    next: "Keep the workflow bounded and document recovery behaviour if it is maintained.",
  },
];

export const writing: WritingEntry[] = [
  {
    slug: "production-support-to-ai-systems",
    title: "From production support to useful AI systems",
    date: "Planned",
    tag: "Perspective",
    status: "In development",
    summary: "A planned note on what incident work teaches us about evidence, failure modes and trustworthy assistants.",
  },
  {
    slug: "small-tools-earn-trust",
    title: "Small tools earn trust before big platforms do",
    date: "Planned",
    tag: "Engineering",
    status: "Planned",
    summary: "A planned note on focused automation: make the next decision clearer before trying to automate everything.",
  },
  {
    slug: "learning-in-public-without-noise",
    title: "Learning in public without turning a portfolio into a dashboard",
    date: "Planned",
    tag: "Portfolio",
    status: "Planned",
    summary: "A planned note on showing evidence and judgement without presenting unfinished experiments as published work.",
  },
];

export const learning = [
  {
    title: "UCD MSc in Computer Science (Negotiated Learning)",
    period: "2025 - 2027",
    description:
      "Part-time study at University College Dublin with an AI-focused pathway, connected to applied engineering work and real systems.",
    tags: ["UCD", "Computer science", "Applied learning"],
  },
  {
    title: "University of Limerick AI certificate",
    period: "2025 - 2026",
    description:
      "Completed with First Class Honours, strengthening the foundations behind scientific computing and applied AI work.",
    tags: ["AI foundations", "First Class Honours"],
  },
  {
    title: "Cloud and distributed systems",
    period: "Ongoing",
    description:
      "Continuous practice across AWS, CDN delivery, incident response, automation and the operational details that make systems dependable.",
    tags: ["AWS", "CDN", "DevOps"],
  },
];

export const lab = [
  {
    title: "Retrieval and evidence",
    status: "Active",
    description: "Testing how assistants expose sources, uncertainty and useful next actions in troubleshooting contexts.",
  },
  {
    title: "Automation with guardrails",
    status: "Experiment",
    description: "Exploring small browser and workflow automations that fail visibly and remain easy to recover.",
  },
  {
    title: "Technical portfolio systems",
    status: "Shipping",
    description: "Building the website itself as a compact example of content modelling, static delivery and careful information hierarchy.",
  },
];
