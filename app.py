from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Personal cloud engineering portfolio landing page."""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#090c14">
  <meta name="description" content="Nikolas Wasielewski — aspiring Cloud and DevOps Engineer. Explore real AWS infrastructure, Terraform, CI/CD, and Linux projects.">
  <title>Nikolas Wasielewski — Cloud & DevOps Engineering</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #090c14;
      --surface: #101522;
      --surface-2: #151b2a;
      --line: rgba(203, 213, 225, .12);
      --text: #f0f4ff;
      --muted: #9da9bc;
      --mint: #79e8c3;
      --violet: #b4a1ff;
      --wrap: 1160px;
    }
    *, *::before, *::after { box-sizing: border-box; }
    html { scroll-behavior: smooth; scroll-padding-top: 95px; }
    body {
      margin: 0;
      color: var(--text);
      background: var(--bg);
      font: 16px/1.65 Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont,
        "Segoe UI", sans-serif;
      -webkit-font-smoothing: antialiased;
    }
    a { color: inherit; text-decoration: none; }
    a:focus-visible, button:focus-visible { outline: 3px solid var(--mint); outline-offset: 4px; }
    ::selection { background: #5c83ab; color: #fff; }
    .skip {
      position: absolute; left: 16px; top: -100px; z-index: 10;
      padding: 12px 16px; background: var(--mint); color: #06130e;
    }
    .skip:focus { top: 16px; }
    .container { width: min(var(--wrap), calc(100% - 48px)); margin-inline: auto; }
    .accent { color: var(--mint); }
    .eyebrow {
      display: inline-flex; align-items: center; gap: 9px;
      font-size: 11px; font-weight: 750; letter-spacing: .17em; text-transform: uppercase;
      color: var(--mint);
    }
    .eyebrow::before { content: ""; height: 6px; width: 6px; border-radius: 50%; background: currentColor; }
    .site-header {
      position: sticky; top: 0; z-index: 5; border-bottom: 1px solid var(--line);
      background: rgba(9, 12, 20, .88); backdrop-filter: blur(18px);
    }
    .header-inner { min-height: 80px; display: flex; align-items: center; justify-content: space-between; gap: 24px; }
    .brand { display: inline-flex; align-items: center; gap: 12px; font-weight: 800; letter-spacing: -.04em; white-space: nowrap; }
    .brand-mark {
      width: 39px; height: 39px; display: grid; place-items: center;
      border: 1px solid rgba(121, 232, 195, .4); border-radius: 11px;
      color: var(--mint); background: rgba(121, 232, 195, .07); font-size: 14px; letter-spacing: -.04em;
    }
    .brand-dot { color: var(--mint); }
    .nav-links { display: flex; align-items: center; gap: 28px; }
    .nav-links a { color: #bdc6d7; font-size: 13px; font-weight: 600; transition: color .2s; }
    .nav-links a:hover, .nav-links a:focus-visible { color: var(--mint); }
    .nav-links .nav-contact {
      border: 1px solid rgba(121, 232, 195, .32);
      padding: 9px 14px; border-radius: 9px; color: var(--mint);
    }
    .hero-wrap {
      position: relative; overflow: hidden;
      background:
        radial-gradient(ellipse 40% 55% at 78% 23%, rgba(92, 80, 170, .17), transparent 85%),
        radial-gradient(ellipse 40% 55% at 8% 75%, rgba(28, 121, 116, .10), transparent 86%);
    }
    .hero { display: grid; grid-template-columns: 1.1fr .9fr; gap: 65px; align-items: center; padding-block: 105px 115px; }
    .availability {
      display: inline-flex; align-items: center; gap: 9px;
      border: 1px solid rgba(121, 232, 195, .23); padding: 8px 13px; border-radius: 100px;
      color: #b1dccc; background: rgba(121, 232, 195, .055);
      font-size: 12px; font-weight: 650;
    }
    .availability::before {
      content: ""; width: 7px; height: 7px; background: var(--mint);
      box-shadow: 0 0 12px rgba(121, 232, 195, .55); border-radius: 50%;
    }
    h1, h2, h3, p { margin-top: 0; }
    h1 {
      margin-block: 30px 22px; font-size: clamp(44px, 5.2vw, 78px);
      letter-spacing: -.071em; font-weight: 800; line-height: 1.08; max-width: 740px;
    }
    .gradient {
      background: linear-gradient(110deg, var(--mint), #a9d9ed 49%, var(--violet));
      background-clip: text; -webkit-background-clip: text; color: transparent;
    }
    .hero-lede { max-width: 550px; color: var(--muted); font-size: clamp(16px, 1.6vw, 18px); line-height: 1.75; }
    .hero-buttons { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 33px; }
    .button {
      display: inline-flex; align-items: center; justify-content: center; gap: 12px;
      min-height: 47px; padding: 11px 19px; border: 1px solid var(--line);
      border-radius: 10px; font-size: 13px; font-weight: 750;
      transition: transform .2s, background .2s, border-color .2s;
    }
    .button:hover { transform: translateY(-2px); }
    .button-primary { color: #06130e; background: var(--mint); border-color: var(--mint); }
    .button-primary:hover { background: #a7f3d8; }
    .button-quiet { background: rgba(255,255,255,.035); }
    .button-quiet:hover { border-color: rgba(255,255,255,.28); }
    .hero-meta { display: flex; flex-wrap: wrap; gap: 12px 24px; margin-top: 38px; color: #8492a8; font-size: 12px; }
    .hero-meta span::before { content: "✦"; color: var(--mint); margin-right: 8px; font-size: 10px; }
    .terminal {
      border: 1px solid rgba(205, 216, 234, .17); border-radius: 17px; overflow: hidden;
      background: linear-gradient(155deg, #171e2d, #0c101b);
      box-shadow: 0 25px 85px rgba(0,0,0,.45), 0 0 0 10px rgba(255,255,255,.015);
    }
    .terminal-top {
      display: flex; align-items: center; justify-content: space-between; gap: 12px;
      min-height: 50px; padding-inline: 18px; border-bottom: 1px solid var(--line);
      color: #97a7bd; font-size: 11px; font-weight: 650;
    }
    .dots { display: flex; gap: 6px; }
    .dots i { display: block; height: 8px; width: 8px; border-radius: 50%; background: #536075; }
    .dots i:first-child { background: #e98f97; }
    .dots i:nth-child(2) { background: #f0c876; }
    .dots i:last-child { background: #73d6ad; }
    .terminal-body { padding: 28px; font: 12px/1.9 ui-monospace, SFMono-Regular, Consolas, monospace; }
    .terminal-prompt { color: var(--mint); }
    .terminal-muted { color: #8998ae; }
    .terminal-title { color: #f1f5ff; font-weight: 700; font-size: 14px; margin-block: 12px 15px; }
    .terminal-line { margin: 0; overflow-wrap: anywhere; }
    .pipeline { display: flex; align-items: center; flex-wrap: wrap; gap: 8px; margin-block: 17px 20px; }
    .pipeline span {
      padding: 6px 10px; border: 1px solid rgba(121, 232, 195, .23);
      background: rgba(121, 232, 195, .065); border-radius: 6px; color: #a8e7d1;
    }
    .pipeline b { color: #77869d; font-weight: 500; }
    .terminal-status {
      margin-top: 19px; display: flex; align-items: center; justify-content: space-between; gap: 12px;
      padding: 12px; border: 1px solid rgba(121,232,195,.18); background: rgba(121,232,195,.045); border-radius: 8px;
    }
    .terminal-status strong { color: var(--mint); font-weight: 650; }
    .terminal-status span { color: #8393aa; }
    .section { padding-block: 90px; }
    .section-heading { display: flex; align-items: end; justify-content: space-between; gap: 28px; margin-bottom: 35px; }
    h2 { font-size: clamp(30px, 3.1vw, 45px); line-height: 1.16; letter-spacing: -.055em; margin-block: 12px 0; }
    .section-desc { color: var(--muted); max-width: 400px; font-size: 14px; margin-bottom: 3px; }
    .project-card {
      position: relative; overflow: hidden; border: 1px solid var(--line); border-radius: 20px;
      background: linear-gradient(128deg, #171d2d, #101520 60%, #121a25);
      display: grid; grid-template-columns: 1.07fr .93fr;
    }
    .project-copy { padding: clamp(28px, 4.8vw, 64px); display: flex; flex-direction: column; align-items: start; }
    .small-label { color: var(--mint); letter-spacing: .15em; font-size: 11px; font-weight: 750; text-transform: uppercase; }
    .project-copy h3 { font-size: clamp(29px, 3.5vw, 48px); letter-spacing: -.055em; line-height: 1.15; margin: 20px 0 14px; }
    .project-copy p { color: var(--muted); max-width: 480px; font-size: 15px; line-height: 1.75; }
    .tags { display: flex; flex-wrap: wrap; gap: 8px; margin: 9px 0 30px; }
    .tag { font-size: 11px; color: #bec9d9; padding: 5px 9px; border-radius: 6px; border: 1px solid var(--line); background: rgba(255,255,255,.025); }
    .project-link { color: var(--mint); font-weight: 750; font-size: 13px; margin-top: auto; }
    .project-link:hover { text-decoration: underline; text-underline-offset: 4px; }
    .architecture {
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      padding: 40px 32px; min-height: 385px;
      border-left: 1px solid var(--line);
      background: radial-gradient(circle at 50% 44%, rgba(90, 118, 175, .12), transparent 70%), rgba(3, 8, 17, .15);
    }
    .architecture .arch-box {
      min-width: 170px; padding: 12px 18px; text-align: center;
      border: 1px solid rgba(180, 161, 255, .35); border-radius: 9px; background: #1b2033;
      font: 700 12px/1.4 ui-monospace, Consolas, monospace; color: #d8d5ff;
    }
    .architecture .arch-box.primary { color: #b9f4df; background: #142821; border-color: rgba(121,232,195,.35); }
    .arch-arrow { color: #748199; font-size: 20px; height: 34px; line-height: 34px; }
    .arch-note { color: #8190aa; font: 11px/1.5 ui-monospace, Consolas, monospace; margin-top: 22px; text-align: center; }
    .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 18px; }
    .feature { padding: 26px; border: 1px solid var(--line); border-radius: 14px; background: rgba(255,255,255,.017); }
    .feature-icon { display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; border: 1px solid rgba(121,232,195,.19); border-radius: 9px; color: var(--mint); margin-bottom: 17px; }
    .feature h3 { letter-spacing: -.035em; font-size: 17px; margin: 0 0 7px; }
    .feature p { color: var(--muted); font-size: 13px; margin: 0; line-height: 1.75; }
    .about-section { border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); background: rgba(255,255,255,.013); }
    .about-grid { display: grid; grid-template-columns: .9fr 1.1fr; gap: 80px; align-items: start; }
    .about-copy { color: #b3bfd0; font-size: 16px; line-height: 1.9; }
    .about-copy p { margin-bottom: 18px; }
    .stack-label { color: #e1e7f4; font-size: 13px; font-weight: 750; margin-bottom: 16px; }
    .stack { display: flex; flex-wrap: wrap; gap: 9px; }
    .stack span { border: 1px solid var(--line); background: #151c29; padding: 7px 12px; border-radius: 8px; font-size: 12px; color: #c5d1e0; }
    .contact-panel {
      display: flex; align-items: center; justify-content: space-between; gap: 30px;
      padding: clamp(30px, 4vw, 56px); border: 1px solid rgba(121,232,195,.22); border-radius: 20px;
      background: radial-gradient(ellipse at 90% 0%, rgba(121, 232, 195, .095), transparent 60%), #111924;
    }
    .contact-panel h2 { max-width: 620px; margin-block: 13px 12px; }
    .contact-panel p { color: var(--muted); margin: 0; max-width: 490px; font-size: 14px; }
    footer { border-top: 1px solid var(--line); padding: 24px 0; color: #8c9aae; font-size: 12px; }
    .footer-row { display: flex; justify-content: space-between; gap: 18px; flex-wrap: wrap; }
    .footer-links { display: flex; gap: 20px; }
    .footer-links a:hover { color: var(--mint); }
    @media (max-width: 850px) {
      .hero { grid-template-columns: 1fr; gap: 55px; padding-block: 75px 85px; }
      .terminal { max-width: 600px; width: 100%; }
      .project-card { grid-template-columns: 1fr; }
      .architecture { border-left: 0; border-top: 1px solid var(--line); min-height: 315px; }
      .about-grid { grid-template-columns: 1fr; gap: 20px; }
      .features-grid { grid-template-columns: 1fr; }
    }
    @media (max-width: 580px) {
      .container { width: min(var(--wrap), calc(100% - 32px)); }
      .header-inner { min-height: 68px; gap: 14px; }
      .brand { font-size: 13px; gap: 8px; }
      .brand-mark { width: 31px; height: 31px; font-size: 11px; }
      .nav-links { gap: 12px; }
      .nav-links a { font-size: 12px; }
      .nav-links .nav-contact { padding: 7px 9px; }
      .nav-links .about-link { display: none; }
      .hero { padding-block: 64px 75px; }
      h1 { font-size: clamp(41px, 11vw, 60px); }
      .terminal-body { padding: 20px 16px; font-size: 11px; }
      .section { padding-block: 64px; }
      .section-heading { display: block; }
      .section-desc { margin-top: 15px; }
      .project-copy { padding: 28px 23px; }
      .architecture { padding: 33px 16px; }
      .contact-panel { display: block; }
      .contact-panel .button { margin-top: 24px; }
      .footer-row { flex-direction: column; }
    }
    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto; }
      *, *::before, *::after { transition: none !important; animation: none !important; }
    }
  </style>
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="#top" aria-label="Nikolas Wasielewski, home">
        <span class="brand-mark">NW</span><span>Nikolas<span class="brand-dot">.</span></span>
      </a>
      <nav class="nav-links" aria-label="Primary navigation">
        <a href="#work">Work</a>
        <a href="#about" class="about-link">About</a>
        <a href="#contact" class="nav-contact">Let's connect ↗</a>
      </nav>
    </div>
  </header>

  <main id="main">
    <div id="top" class="hero-wrap">
      <section class="container hero" aria-labelledby="hero-title">
        <div>
          <div class="availability">Open to cloud &amp; DevOps opportunities</div>
          <h1 id="hero-title">Building reliable systems.<br><span class="gradient">From code to cloud.</span></h1>
          <p class="hero-lede">
            I'm Nikolas, an aspiring Cloud &amp; DevOps Engineer focused on AWS,
            infrastructure automation, and the engineering that keeps applications running.
            I learn by building real systems.
          </p>
          <div class="hero-buttons">
            <a href="#work" class="button button-primary">Explore my work <span aria-hidden="true">↗</span></a>
            <a href="https://github.com/NyxxOhhNyxx" class="button button-quiet" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a>
          </div>
          <div class="hero-meta"><span>AWS infrastructure</span><span>Linux &amp; automation</span><span>CI/CD pipelines</span></div>
        </div>

        <div class="terminal" aria-label="Illustration of the CloudOps deployment process">
          <div class="terminal-top">
            <div class="dots" aria-hidden="true"><i></i><i></i><i></i></div>
            <span>cloudops / deployment-overview</span>
            <span>↗</span>
          </div>
          <div class="terminal-body">
            <p class="terminal-line"><span class="terminal-prompt">$</span> cloudops status --overview</p>
            <p class="terminal-line terminal-muted"># Architecture snapshot · conceptual</p>
            <p class="terminal-title">CloudOps / delivery pipeline</p>
            <div class="pipeline" aria-hidden="true"><span>GitHub</span><b>→</b><span>Actions</span><b>→</b><span>SSM</span><b>→</b><span>EC2</span></div>
            <p class="terminal-line"><span class="terminal-muted">infrastructure:</span> Terraform + AWS</p>
            <p class="terminal-line"><span class="terminal-muted">edge:</span> Nginx / HTTPS</p>
            <p class="terminal-line"><span class="terminal-muted">application:</span> Flask / Gunicorn</p>
            <p class="terminal-line"><span class="terminal-muted">observability:</span> CloudWatch</p>
            <div class="terminal-status"><span>Application health endpoint</span><strong>/health ↗</strong></div>
            <p class="terminal-line terminal-muted" style="margin-top:13px">Actual status: <a href="/health" style="color:var(--mint);text-decoration:underline;text-underline-offset:3px">view live JSON health check</a></p>
          </div>
        </div>
      </section>
    </div>

    <section class="section container" id="work" aria-labelledby="work-heading">
      <div class="section-heading">
        <div><span class="eyebrow">Selected work</span><h2 id="work-heading">Built, not just studied.</h2></div>
        <p class="section-desc">Hands-on projects with real infrastructure, real deployment constraints, and documented engineering decisions.</p>
      </div>

      <article class="project-card">
        <div class="project-copy">
          <span class="small-label">01 / Flagship project · AWS</span>
          <h3>CloudOps.<br>Infrastructure in action.</h3>
          <p>
            A self-hosted Flask application on AWS EC2 with HTTPS, automated
            GitHub Actions deployments, temporary OIDC credentials, Systems Manager,
            CloudWatch monitoring, and Terraform-managed infrastructure.
          </p>
          <div class="tags">
            <span class="tag">AWS EC2</span><span class="tag">Terraform</span>
            <span class="tag">GitHub Actions</span><span class="tag">Python / Flask</span>
            <span class="tag">Nginx</span><span class="tag">IAM / OIDC</span>
          </div>
          <a class="project-link" href="https://github.com/NyxxOhhNyxx/aws-cloudops-portfolio" target="_blank" rel="noopener noreferrer">Explore source code &amp; documentation ↗</a>
        </div>
        <div class="architecture" aria-label="CloudOps architecture: GitHub Actions through AWS Systems Manager to an EC2 application">
          <div class="arch-box">GitHub Actions</div>
          <div class="arch-arrow" aria-hidden="true">↓</div>
          <div class="arch-box">AWS Systems Manager</div>
          <div class="arch-arrow" aria-hidden="true">↓</div>
          <div class="arch-box primary">EC2 · Nginx · Flask</div>
          <div class="arch-note">Terraform manages EC2 and security rules.<br>CloudWatch monitors infrastructure.</div>
        </div>
      </article>

      <div class="features-grid" aria-label="CloudOps technical highlights">
        <article class="feature"><span class="feature-icon" aria-hidden="true">◇</span><h3>Infrastructure as Code</h3><p>Imported and tracked existing EC2 and firewall resources using Terraform, with private S3 state and locking.</p></article>
        <article class="feature"><span class="feature-icon" aria-hidden="true">↗</span><h3>Automated delivery</h3><p>Built a GitHub Actions pipeline that tests application changes and deploys through AWS Systems Manager.</p></article>
        <article class="feature"><span class="feature-icon" aria-hidden="true">◎</span><h3>Operations &amp; security</h3><p>Configured HTTPS, scoped IAM access, Linux services, health checks, and CloudWatch monitoring.</p></article>
      </div>
    </section>

    <section class="section about-section" id="about" aria-labelledby="about-heading">
      <div class="container about-grid">
        <div><span class="eyebrow">Behind the infrastructure</span><h2 id="about-heading">Curious by default.<br><span class="accent">Hands-on by choice.</span></h2></div>
        <div>
          <div class="about-copy">
            <p>I'm a technology-focused builder pursuing a career in cloud engineering, DevOps, and systems architecture. I enjoy understanding how applications, networks, operating systems, and automation fit together.</p>
            <p>My approach is practical: deploy something real, monitor it, break assumptions, fix problems, and document what I learn along the way.</p>
          </div>
          <p class="stack-label">Technologies I've worked with</p>
          <div class="stack" aria-label="Technical skills">
            <span>AWS EC2</span><span>IAM</span><span>Systems Manager</span><span>CloudWatch</span>
            <span>Terraform</span><span>Linux</span><span>Python</span><span>Flask</span>
            <span>Nginx</span><span>Gunicorn</span><span>Git / GitHub</span><span>GitHub Actions</span>
            <span>Networking</span><span>HTTPS / TLS</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section container" id="contact" aria-labelledby="contact-heading">
      <div class="contact-panel">
        <div>
          <span class="eyebrow">What's next?</span>
          <h2 id="contact-heading">Let's build something<br><span class="gradient">that matters.</span></h2>
          <p>Interested in cloud infrastructure, automation, and meaningful engineering challenges. Explore my work or connect through GitHub.</p>
        </div>
        <a href="https://github.com/NyxxOhhNyxx" class="button button-primary" target="_blank" rel="noopener noreferrer">Connect on GitHub ↗</a>
      </div>
    </section>
  </main>
  <footer>
    <div class="container footer-row">
      <span>© 2026 Nikolas Wasielewski · Built on AWS.</span>
      <div class="footer-links">
        <a href="#top">Back to top ↑</a>
        <a href="/health">Health API</a>
        <a href="https://github.com/NyxxOhhNyxx/aws-cloudops-portfolio" target="_blank" rel="noopener noreferrer">Source ↗</a>
      </div>
    </div>
  </footer>
</body>
</html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "cloudops",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })
