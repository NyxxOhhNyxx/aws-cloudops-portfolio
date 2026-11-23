# Personal Portfolio — Nikolas Wasielewski

A fully responsive, accessible Flask portfolio highlighting real cloud infrastructure, software development, enterprise IT internships and academic projects.

## Local development

In the repository root, with Python 3.12 installed:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt pytest
.\.venv\Scripts\python.exe -m flask --app app run --port 5000
```

Visit <http://127.0.0.1:5000>.

Tests: ` .\.venv\Scripts\python.exe -m pytest -q `.

## Pages

- `/`: Personal introduction, interactive cloud diagram, projects, experience, skills, portrait, contact.
- `/projects/cloudops`: CloudOps technical case study with working repo and public health links.
- `/projects/banking`, `/projects/windows-server`, `/projects/calculator`: Academic project case studies.
- `/health`: Existing API shape preserved for deployment verification.
- `/robots.txt`: Search indexing policy.

## Technologies

Flask + Jinja2, CSS, vanilla JavaScript. No frontend build pipeline, external UI libraries or AWS browser credentials. Web fonts load from Google Fonts when connected; local fallbacks work offline.

## Deployment warning — read before merging

**The currently deployed EC2 script `/usr/local/sbin/cloudops-deploy` only deploys `app.py`. This portfolio introduces the `templates/` and `static/` directories. DO NOT merge into `main` until the server-side deployment routine has been reviewed and upgraded to deploy those files atomically, with backups and rollback.** The existing GitHub Actions workflow may trigger on `app.py` changes to `main`. Merging prematurely could break the live homepage despite `/health` continuing to return `healthy`.

This bundle intentionally does not alter the production EC2 instance or deploy anything to AWS. Build, review and test on the feature branch; separately plan and install an updated server-side deployment script before production release.

## Content accuracy

- VS Direct experience is described conservatively.
- Projects without public repositories do not link to invented code or demos.
- No certifications or professional job titles are claimed.
- The portrait supplied by the owner has been cropped and resized to a bandwidth-friendly WebP; no facial changes were made.
- Contact phone number, email and location were provided by the site owner for public display.

**Portrait asset:** The provided photo is losslessly retained in appearance as optimized WebP pixels wrapped in a text-based SVG so it can be committed through the connected GitHub text-file workflow. No AI retouching was applied.
