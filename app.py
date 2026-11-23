"""Public portfolio website. No AWS credentials or private APIs are exposed."""

from datetime import datetime, timezone

from flask import Flask, abort, jsonify, render_template, Response

app = Flask(__name__)

PROJECTS = {
    "cloudops": {
        "number": "01", "type": "Independent infrastructure project",
        "name": "CloudOps", "subtitle": "From a simple Python service to a real AWS deployment.",
        "summary": "I built and operate a Python web application on AWS EC2, using Linux, Nginx, Gunicorn, Terraform, CloudWatch, and automated deployments through GitHub Actions and Systems Manager.",
        "tags": ["AWS EC2", "Terraform", "Python / Flask", "GitHub Actions", "IAM / OIDC", "Linux", "CloudWatch"],
        "role": "Infrastructure, application development & deployment automation",
        "context": "An independent project to learn how real applications are hosted, secured, observed, and updated in the cloud.",
        "challenges": [
            {"title": "Operating an application", "text": "Configured Ubuntu, systemd, Gunicorn, Nginx and Let's Encrypt to serve a Python application over HTTPS."},
            {"title": "Delivering changes safely", "text": "Used GitHub Actions to test code and deploy a specific commit through AWS Systems Manager, with post-deployment health verification."},
            {"title": "Adopting infrastructure as code", "text": "Imported the existing EC2 instance, security group and five firewall rules into Terraform. Added S3 remote state with locking and a private state backup."},
        ],
        "outcomes": [
            "Live application hosted on AWS EC2 with HTTPS and a /health endpoint.",
            "Automated app.py deployment after CI tests on the main branch; manual deployment supported.",
            "Existing EC2 and firewall resources managed through Terraform; VPC and subnet referenced read-only.",
            "CloudWatch infrastructure monitoring and controlled, isolated application-recovery tests.",
        ],
        "note": "This project began as manually provisioned infrastructure. Terraform adoption is partial, not a claim of reproducible end-to-end provisioning. The production deployment script currently manages app.py only and requires an upgrade before deploying this multi-file portfolio.",
        "github": "https://github.com/NyxxOhhNyxx/aws-cloudops-portfolio",
        "live": "https://cloudops-portfolio.duckdns.org/health",
        "live_label": "Live health endpoint",
        "architecture": True,
    },
    "banking": {
        "number": "02", "type": "Academic software project",
        "name": "Online banking simulation", "subtitle": "A complete banking workflow, built as a software project.",
        "summary": "Developed a full-stack banking simulation with authentication, account management and transaction processing as part of technical education.",
        "tags": ["Full-stack development", "Authentication", "Database design", "Transactions"],
        "role": "Application and database development",
        "context": "An educational project to connect application logic, data models, and everyday user workflows.",
        "challenges": [
            {"title": "Authentication", "text": "Designed the user-facing flow for signing in and accessing banking features."},
            {"title": "Account management", "text": "Implemented account-related functionality and connected it to application state."},
            {"title": "Transaction processing", "text": "Developed simulated transactions and account updates within an educational application."},
        ],
        "outcomes": ["Full-stack educational application with authentication, account management and simulated transactions.", "Practical experience connecting software architecture, business logic and database operations."],
        "note": "A classroom simulation, not a real banking product. Public source code and screenshots have not yet been added.",
        "github": None, "live": None, "architecture": False,
    },
    "windows-server": {
        "number": "03", "type": "Academic infrastructure lab",
        "name": "Windows Server network", "subtitle": "Learning infrastructure from the network layer up.",
        "summary": "Built a virtualized Windows Server client–server environment with DNS, DHCP, and network resource management.",
        "tags": ["Windows Server", "Virtualization", "DNS", "DHCP", "Networking"],
        "role": "Virtualization, network configuration and administration",
        "context": "A technical education project focused on how enterprise networks and client–server systems work together.",
        "challenges": [
            {"title": "Virtual infrastructure", "text": "Configured a Windows Server environment using virtualization."},
            {"title": "Network services", "text": "Set up DNS and DHCP services to support the lab network."},
            {"title": "Resource management", "text": "Practiced configuring and managing resources within a client–server setup."},
        ],
        "outcomes": ["Working educational Windows Server lab combining virtualization and core network services.", "Hands-on understanding of DNS, DHCP and client–server administration."],
        "note": "Educational lab; network diagrams and configuration screenshots can be added later.",
        "github": None, "live": None, "architecture": False,
    },
    "calculator": {
        "number": "04", "type": "Academic C# project",
        "name": "C# calculator", "subtitle": "Small scope. Solid fundamentals.",
        "summary": "Built a console calculator application in C#, practicing program structure, user input, calculations and error handling.",
        "tags": ["C#", "Console application", "Error handling", "Programming fundamentals"],
        "role": "Software development",
        "context": "An educational application used to strengthen core C# programming concepts.",
        "challenges": [
            {"title": "Application logic", "text": "Organized calculations and user interaction into a console workflow."},
            {"title": "Input handling", "text": "Handled user input and common invalid-entry cases."},
            {"title": "Reliability", "text": "Practiced implementing validation and error-handling behavior."},
        ],
        "outcomes": ["Functional educational C# console application with calculation features and error handling."],
        "note": "An early learning project. Source code and screenshots are not currently linked.",
        "github": None, "live": None, "architecture": False,
    },
}


@app.context_processor
def common_context():
    return {"year": datetime.now(timezone.utc).year}


@app.get("/")
def home():
    return render_template("index.html", projects=PROJECTS)


@app.get("/projects/<slug>")
def project_detail(slug):
    project = PROJECTS.get(slug)
    if project is None:
        abort(404)
    return render_template("project.html", project=project, slug=slug)


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy", "service": "cloudops",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.get("/robots.txt")
def robots():
    return Response("User-agent: *\nAllow: /\n", mimetype="text/plain")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.after_request
def security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("X-Frame-Options", "DENY")
    return response


if __name__ == "__main__":
    app.run(debug=False)
