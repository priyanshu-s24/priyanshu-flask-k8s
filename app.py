from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Priyanshu Singh -Updated CI/CD Pipeline</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
            max-width: 500px;
            width: 90%;
        }
        h1 {
            font-size: 2.2rem;
            margin-bottom: 10px;
            color: #4ade80;
        }
        h2 {
            font-size: 1.4rem;
            font-weight: 400;
            margin-top: 0;
            color: #e2e8f0;
        }
        .badge {
            display: inline-block;
            background-color: #22c55e;
            color: white;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
            margin: 15px 0;
        }
        .details {
            text-align: left;
            background: rgba(0, 0, 0, 0.2);
            padding: 15px 20px;
            border-radius: 8px;
            margin-top: 20px;
            font-size: 0.95rem;
        }
        .details p {
            margin: 6px 0;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Priyanshu Singh</h1>
        <h2>Updated CI/CD Pipeline Application</h2>
        <div class="badge">Status: Live on Kubernetes (Minikube) - Version 1.0</div>
        <p>This is a fully automated CI/CD pipeline built and deployed automatically via Jenkins.</p>
        <div class="details">
            <p><strong>Developer:</strong> Priyanshu Singh</p>
            <p><strong>Environment:</strong> Local Kubernetes (Minikube)</p>
            <p><strong>Pipeline Status:</strong> Completed Successfully</p>
            <p><strong>Version:</strong> v1.0 (Ready for Live Source Update)</p>
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
    return {"status": "healthy", "developer": "Priyanshu Singh", "version": "1.0"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

