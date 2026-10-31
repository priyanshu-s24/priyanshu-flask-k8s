from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Priyanshu Singh - CI/CD Pipeline</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(12px);
            border-radius: 18px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 12px 35px 0 rgba(0, 0, 0, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.25);
            max-width: 520px;
            width: 90%;
            animation: fadeIn 0.8s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            font-size: 2.4rem;
            margin-bottom: 8px;
            color: #38bdf8;
            letter-spacing: 0.5px;
        }
        h2 {
            font-size: 1.35rem;
            font-weight: 500;
            margin-top: 0;
            color: #f1f5f9;
        }
        .badge {
            display: inline-block;
            background: linear-gradient(90deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 8px 20px;
            border-radius: 24px;
            font-size: 0.95rem;
            font-weight: 700;
            margin: 18px 0;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
        }
        .description {
            font-size: 1.05rem;
            color: #cbd5e1;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        .details {
            text-align: left;
            background: rgba(15, 23, 42, 0.6);
            padding: 18px 24px;
            border-radius: 12px;
            margin-top: 15px;
            font-size: 0.95rem;
            border-left: 4px solid #10b981;
        }
        .details p {
            margin: 8px 0;
            display: flex;
            justify-content: space-between;
        }
        .label {
            color: #94a3b8;
            font-weight: 600;
        }
        .val {
            color: #ffffff;
            font-weight: bold;
        }
        .val-highlight {
            color: #38bdf8;
            font-weight: bold;
        }
        .val-success {
            color: #4ade80;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Priyanshu Singh</h1>
        <h2>Automated CI/CD Pipeline Application</h2>
        <div class="badge">🚀 Live on Kubernetes (Minikube) - Version 2.0 [UPDATED]</div>
        <p class="description">This is an automated CI/CD pipeline built from GitHub and re-deployed dynamically on Kubernetes with zero downtime.</p>
        <div class="details">
            <p><span class="label">Developer:</span> <span class="val">Priyanshu Singh</span></p>
            <p><span class="label">Environment:</span> <span class="val">Local Kubernetes (Minikube)</span></p>
            <p><span class="label">Pipeline Status:</span> <span class="val-success">✅ Successfully Re-deployed</span></p>
            <p><span class="label">Version:</span> <span class="val-highlight">v2.0 (Live Code Change Verified)</span></p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    return {"status": "healthy", "developer": "Priyanshu Singh", "version": "2.0"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
