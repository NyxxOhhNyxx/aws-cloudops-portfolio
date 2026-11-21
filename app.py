from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1">
        <title>CloudOps | AWS Portfolio</title>

        <style>
            * { box-sizing: border-box; }
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #0f172a;
                color: #f8fafc;
                font-family: Arial, sans-serif;
                padding: 24px;
            }
            .card {
                max-width: 650px;
                padding: 48px;
                background: #1e293b;
                border: 1px solid #334155;
                border-radius: 20px;
                text-align: center;
            }
            h1 { font-size: 48px; }
            p { color: #cbd5e1; }
            a { color: #38bdf8; }
            .status { color: #4ade80; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CloudOps</h1>
            <h2>AWS Cloud Engineering Portfolio</h2>
            <p>Deployed on Amazon EC2 with Ubuntu Linux.</p>
            <p>Python | Flask | Gunicorn | Nginx</p>
            <p class="status">Application Online</p>
            <a href="/health">View API Health Check</a>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "cloudops",
        "timestamp": datetime.now(
            timezone.utc
        ).isoformat()
    })
