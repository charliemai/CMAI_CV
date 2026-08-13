# cmai_cv

Personal portfolio and CV site for Charlie Mai, built with Astro and delivered as a static site.

The site is optimised for job search and technical credibility. The primary routes are:

- / - positioning, proof points, selected projects, and recent career signal
- /cv/ - web CV and formal PDF download
- /projects/ - selected work
- /projects/[slug]/ - project case studies
- /writing/, /lab/, /learning/ - secondary narrative

## Local development

Install dependencies with pnpm install, then start the development server with pnpm run dev.
The production build is generated with pnpm run build.

## Content and assets

- src/data/site.ts is the canonical web content model.
- public/cv.pdf is the latest LinkedIn-generated formal CV PDF.
- public/profile.JPG is the avatar used by the site.
- public/projects/ contains the project diagrams used by the portfolio cards and case studies.
- public/social-card.svg is the default social preview image.

When the formal CV changes, update public/cv.pdf and review the corresponding facts in
src/data/site.ts. UCD is the current MSc institution; old Trinity wording must not return.

## Deployment note

The working branch for this repository is main. Do not create feature branches for this personal
site. The production provider and repository webhook must be independently verified before the first
push of the rewrite; the current public response shows Vercel/CloudFront/Cloudflare headers, which
does not prove the remembered Render setup.
