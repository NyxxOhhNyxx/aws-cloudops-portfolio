/* Small, dependency-free enhancements. Every page remains usable without JS. */
document.documentElement.classList.add('js');

const menu = document.querySelector('.menu-button');
const mobileNav = document.getElementById('mobile-nav');
if (menu && mobileNav) {
  const closeMenu = () => { menu.setAttribute('aria-expanded', 'false'); mobileNav.hidden = true; };
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    mobileNav.hidden = !open;
  });
  mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
  window.matchMedia('(min-width: 651px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
}

const motionReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealItems = document.querySelectorAll('[data-reveal]');
if ('IntersectionObserver' in window && !motionReduced) {
  const observer = new IntersectionObserver((entries, watcher) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('revealed'); watcher.unobserve(entry.target); }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
  revealItems.forEach(item => observer.observe(item));
} else {
  revealItems.forEach(item => item.classList.add('revealed'));
}

const architectureDetails = {
  github: ['GitHub · Source control', 'Application code, automated tests and workflow definitions live in GitHub.'],
  terraform: ['Terraform · Infrastructure as Code', 'EC2 and firewall rules are managed through Terraform with locked S3 remote state.'],
  oidc: ['OIDC / IAM · Temporary access', 'GitHub Actions assumes a restricted AWS IAM role without permanent AWS keys.'],
  ec2: ['EC2 · Application server', 'Ubuntu, Nginx, Gunicorn and Flask run the application.'],
  monitor: ['CloudWatch · Monitoring', 'AWS CloudWatch tracks EC2 CPU, network traffic, credits and instance health.'],
  web: ['HTTPS · Secure delivery', 'Nginx serves the Flask app over HTTPS using a Let\'s Encrypt certificate.']
};
const nodes = document.querySelectorAll('[data-node]');
const nodeTitle = document.getElementById('node-title');
const nodeDescription = document.getElementById('node-description');
if (nodes.length && nodeTitle && nodeDescription) {
  nodes.forEach(node => node.addEventListener('click', () => {
    nodes.forEach(item => { item.classList.remove('active'); item.setAttribute('aria-pressed', 'false'); });
    node.classList.add('active'); node.setAttribute('aria-pressed', 'true');
    const detail = architectureDetails[node.dataset.node];
    if (detail) { nodeTitle.textContent = detail[0]; nodeDescription.textContent = detail[1]; }
  }));
}

const filters = document.querySelectorAll('[data-filter]');
const skillGroups = document.querySelectorAll('[data-category]');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(item => { item.classList.remove('active'); item.setAttribute('aria-pressed', 'false'); });
  button.classList.add('active'); button.setAttribute('aria-pressed', 'true');
  skillGroups.forEach(group => { group.hidden = button.dataset.filter !== 'all' && group.dataset.category !== button.dataset.filter; });
}));

const copyEmail = document.querySelector('[data-copy]');
if (copyEmail) {
  copyEmail.addEventListener('click', async () => {
    if (!navigator.clipboard || !window.isSecureContext) {
      copyEmail.textContent = 'Use the email link above ↗'; return;
    }
    try { await navigator.clipboard.writeText(copyEmail.dataset.copy); copyEmail.textContent = 'Email copied ✓'; }
    catch { copyEmail.textContent = 'Use the email link above ↗'; }
  });
}
