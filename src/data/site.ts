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
  bullets: string[];
};

export const profile = {
  name: "Charlie Mai",
  shortName: "Charlie",
  title: "IT DevOps Support Engineer",
  descriptor: "AWS, automation, and AI-assisted troubleshooting",
  location: "Dublin, Ireland",
  email: "me@cmai.ai",
  image: "/profile.JPG",
  cv: "/cv.pdf",
  links: {
    github: "https://github.com/charliemai",
    linkedin: "https://www.linkedin.com/in/charlie-mai/",
  },
  summary:
    "I turn production problems into clearer systems: investigating incidents, improving operational workflows, and building practical tools across AWS, backend services, and AI-assisted troubleshooting.",
  availability:
    "Open to engineering, DevOps, cloud support, and technical operations roles where reliability and useful automation matter.",
};

export const metrics = [
  { value: "16", label: "years across cloud, backend, DevOps, and technical leadership" },
  { value: "440k+", label: "civic reports handled by a public-facing mobile platform" },
  { value: "AWS #1", label: "customer satisfaction recognition in Cloud Support" },
  { value: "457", label: "resolves with Top 2 case-performance recognition" },
];

export const focusAreas = [
  {
    title: "Production support",
    description:
      "Incident investigation, root-cause analysis, change workflows, integration support, and calm communication during high-impact issues.",
    tags: ["AWS", "CDN", "Observability"],
  },
  {
    title: "Operational automation",
    description:
      "Small scripts, visualisation tools, and repeatable workflows that reduce recurring work and make systems easier to operate.",
    tags: ["Python", "FastAPI", "CI/CD"],
  },
  {
    title: "Useful AI systems",
    description:
      "RAG and assistant experiments grounded in real troubleshooting needs, with attention to evidence, retrieval quality, and human trust.",
    tags: ["RAG", "Machine learning", "Product thinking"],
  },
];

export const experience: ExperienceEntry[] = [
  {
    company: "National Broadband Ireland",
    position: "IT DevOps Support Engineer",
    period: "Feb 2025 - Present",
    location: "Dublin, Ireland",
    summary:
      "Support production systems built on AWS serverless and commercial platforms, with a focus on reliable operations and actionable diagnostics.",
    bullets: [
      "Investigate incidents, integration failures, and recurring issues across backend and internal systems.",
      "Build and improve operational automation to reduce manual work and improve system reliability.",
      "Deploy fixes, support maintenance, and create scripts and visualisation tools for better troubleshooting visibility.",
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
      "Managed parallel workstreams across engineering, R&D, and business stakeholders.",
      "Aligned scope, requirements, and delivery plans for complex enterprise initiatives.",
      "Connected technical teams and business owners so decisions moved from ambiguity to delivery.",
    ],
  },
  {
    company: "Amazon Web Services (AWS)",
    position: "Cloud Support Engineer II / Cloud Support Engineer",
    period: "Jan 2022 - Mar 2024",
    location: "Dublin, Ireland",
    summary:
      "Resolved complex distributed-cloud issues and progressed to Cloud Support Engineer II within 21 months, specialising in CloudFront and adjacent AWS services.",
    bullets: [
      "Worked across CloudFront, S3, Route 53, API Gateway, Lambda, IAM, WAF, SES, and media services.",
      "Recognised as Top 1 in customer satisfaction and Top 2 in case performance within the support team.",
      "Accredited as a CloudFront Subject Matter Expert and contributed to mentoring, enablement, documentation, and hiring.",
    ],
  },
  {
    company: "Verizon Media Platform",
    position: "Solutions Engineer / Delivery Customer Support Engineer",
    period: "Apr 2019 - Aug 2021",
    location: "Taiwan",
    summary:
      "Delivered customer-facing CDN solutions, implementation support, and incident coordination for enterprise media customers.",
    bullets: [
      "Analysed traffic logs and CDN performance to support production troubleshooting and service optimisation.",
      "Managed incident, problem, and change workflows with regional teams during onboarding and production issues.",
      "Supported enterprise implementations, PoCs, and cross-regional delivery with engineering and commercial stakeholders.",
    ],
  },
  {
    company: "CATCHPLAY",
    position: "Technical Lead",
    period: "May 2017 - Apr 2019",
    location: "Taipei / Jakarta",
    summary:
      "Led Android TV and set-top-box delivery, partner integrations, and cross-platform technical alignment across Android, iOS, and web teams.",
    bullets: [
      "Built CI practices and helped improve application architecture, performance, and user experience.",
      "Supported streaming SDK integration and multi-region product delivery across Taiwan and Indonesia.",
    ],
  },
  {
    company: "Mobile and early engineering roles",
    position: "Team Lead, Mobile / Android Developer / IT Lead",
    period: "2009 - 2017",
    location: "Taiwan",
    summary:
      "Built software products and led mobile, backend, and application delivery across several technology companies.",
    bullets: [
      "Led native Android and iOS development, CI setup, technical capability building, and application architecture improvements.",
      "Worked across web, hybrid, Java enterprise, mobile, and internal systems development.",
    ],
  },
];

export const education = [
  {
    institution: "University College Dublin",
    programme: "MSc in Computer Science (Negotiated Learning), Artificial Intelligence",
    period: "Sep 2025 - Aug 2027",
    note: "Part-time programme; current study focus includes AI and applied computing.",
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
    slug: "vouchgether",
    title: "Vouchgether",
    eyebrow: "Mobile product",
    problem: "Make voucher discovery and sharing easier to act on in a mobile-first experience.",
    summary:
      "A mobile product for discovering, sharing, and claiming discount vouchers with a serverless AWS foundation.",
    evidence: "User-facing product case study",
    role: "Product builder / engineer",
    stack: ["React Native", "AWS Lambda", "Cognito", "S3", "DynamoDB"],
    image: "/projects/vouchgether.svg",
    status: "Product case study",
    featured: true,
    href: "https://lkk.dev",
    bullets: [
      "Designed the core voucher discovery, sharing, and claim experience.",
      "Connected a React Native client to authentication, media, and serverless backend services.",
      "Balanced product iteration with the reliability and trust boundaries of user-generated content.",
    ],
  },
  {
    slug: "parking-reporter",
    title: "Parking Violation Reporter",
    eyebrow: "Civic technology",
    problem: "Give citizens a faster, more visible way to report traffic and environmental violations.",
    summary:
      "A citizen reporting platform built to make traffic-environment feedback faster, more visible, and more actionable.",
    evidence: "440k+ civic reports handled",
    role: "Founder / mobile engineer",
    stack: ["Android", "Firebase", "Push notifications", "Product delivery"],
    image: "/projects/parking-reporter.svg",
    status: "Public impact",
    featured: true,
    bullets: [
      "Built and shipped the reporting workflow for citizens in Taiwan.",
      "Handled more than 440,000 reports through the platform.",
      "The related social-enterprise concept received a U-START competition Silver Medal.",
    ],
  },
  {
    slug: "rag-troubleshooting-assistant",
    title: "RAG Troubleshooting Assistant",
    eyebrow: "AI systems",
    problem: "Turn technical documents and incident evidence into troubleshooting context people can inspect.",
    summary:
      "A retrieval-augmented assistant experiment for turning technical documents and incident evidence into useful troubleshooting context.",
    evidence: "Evidence-first AI for operational work",
    role: "Architect / builder",
    stack: ["Python", "FastAPI", "Embeddings", "Vector search"],
    image: "/projects/rag-assistant.svg",
    status: "Active lab",
    featured: true,
    bullets: [
      "Built document ingestion, semantic retrieval, and conversational Q&A flows.",
      "Explored how an assistant can expose evidence and reasoning instead of returning opaque answers.",
      "Used production-support experience to shape the questions, failure modes, and useful output format.",
    ],
  },
  {
    slug: "videotranslate",
    title: "VideoTranslate",
    eyebrow: "Workflow automation",
    problem: "Make a multi-stage video translation workflow easier to operate, inspect, and iterate.",
    summary:
      "An experiment in making video translation workflows easier to operate, inspect, and iterate.",
    evidence: "Applied automation to a media workflow",
    role: "Builder",
    stack: ["Python", "Media processing", "Automation", "Web UI"],
    image: "/projects/video-translate.svg",
    status: "Exploration",
    bullets: [
      "Prototyped a workflow for turning source video into translated, reviewable output.",
      "Focused on clear stages, useful failure feedback, and reducing repeated manual steps.",
    ],
  },
  {
    slug: "argumentlab",
    title: "ArgumentLab",
    eyebrow: "Learning lab",
    problem: "Make reasoning exercises easier to compare, inspect, and discuss.",
    summary:
      "A structured-reasoning playground for testing how people and AI systems make, inspect, and improve arguments.",
    evidence: "Learning through small, inspectable experiments",
    role: "Researcher / builder",
    stack: ["TypeScript", "AI experiments", "Evaluation", "UX"],
    image: "/projects/argument-lab.svg",
    status: "Learning project",
    bullets: [
      "Turns reasoning exercises into small interfaces that are easier to compare and discuss.",
      "Keeps the experiment surface explicit so the quality of an answer can be inspected.",
    ],
  },
  {
    slug: "ucd-sport-auto-booker",
    title: "UCD Sport Auto Booker",
    eyebrow: "Automation utility",
    problem: "Reduce friction in a recurring sports-booking workflow while keeping timing and failure behaviour visible.",
    summary:
      "A focused automation experiment for reducing friction in recurring sports-booking tasks while studying at UCD.",
    evidence: "Small automation with a clear user job",
    role: "Builder",
    stack: ["Browser automation", "Scheduling", "Reliability", "UX"],
    image: "/projects/sport-auto-booker.svg",
    status: "Personal utility",
    bullets: [
      "Mapped a repetitive booking workflow into a small, observable automation.",
      "Used the project to explore reliability, timing, and safe failure behaviour.",
    ],
  },
];

export const writing = [
  {
    slug: "production-support-to-ai-systems",
    title: "From production support to useful AI systems",
    date: "2026",
    tag: "Perspective",
    summary:
      "What incident work teaches us about evidence, failure modes, and the shape of a trustworthy assistant.",
  },
  {
    slug: "small-tools-earn-trust",
    title: "Small tools earn trust before big platforms do",
    date: "2026",
    tag: "Engineering",
    summary:
      "A practical case for focused automation: make the next decision clearer before trying to automate everything.",
  },
  {
    slug: "learning-in-public-without-noise",
    title: "Learning in public without turning a portfolio into a dashboard",
    date: "2026",
    tag: "Portfolio",
    summary:
      "Why a technical portfolio should show evidence and judgment, not every unfinished experiment.",
  },
];

export const learning = [
  {
    title: "UCD MSc in Computer Science",
    period: "2025 - 2027",
    description:
      "Part-time study in AI and negotiated learning, connected to applied engineering work and real systems.",
    tags: ["AI", "Computer science", "Applied learning"],
  },
  {
    title: "AI foundations",
    period: "2025 - 2026",
    description:
      "A completed University of Limerick certificate strengthened the foundations behind scientific computing and deep-learning systems.",
    tags: ["Machine learning", "Scientific computing"],
  },
  {
    title: "Cloud and distributed systems",
    period: "Ongoing",
    description:
      "Continuous practice across AWS, CDN delivery, incident response, automation, and the operational details that make systems dependable.",
    tags: ["AWS", "CDN", "DevOps"],
  },
];

export const lab = [
  {
    title: "Retrieval and evidence",
    status: "Active",
    description: "Testing how assistants expose sources, uncertainty, and useful next actions in troubleshooting contexts.",
  },
  {
    title: "Automation with guardrails",
    status: "Active",
    description: "Exploring small browser and workflow automations that fail visibly and remain easy to recover.",
  },
  {
    title: "Technical portfolio systems",
    status: "Shipping",
    description: "Building the website itself as a compact example of content modelling, static delivery, and careful information hierarchy.",
  },
];
