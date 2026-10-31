# Automated CI/CD Pipeline - Priyanshu Singh

**Student:** Priyanshu Singh  
**Course:** TYCSE: Cloud Computing and DevOps  
**Assignment:** CCA 2 – CI/CD Pipeline Implementation and Deployment  

---

## 📌 Project Overview
This project contains an automated CI/CD pipeline built for **Priyanshu Singh**. It demonstrates continuous integration and continuous deployment of a containerized Python Flask web application to a Kubernetes cluster managed locally via Minikube.

Whenever changes are committed to the GitHub repository, Jenkins pulls the repository, executes automated test suites, creates a new Docker container image, pushes it to Docker Hub, and rolls out the deployment to Minikube with zero downtime.

---

## 🚀 Pipeline Stages
1. **Source Code:** Hosted on GitHub with complete source code, Dockerfile, Jenkinsfile, and Kubernetes configurations.
2. **Checkout:** Jenkins automatically pulls changes from GitHub upon trigger/webhook.
3. **Build & Test:** Virtual environment setup, dependency installation (`requirements.txt`), and automated unit tests (`test_app.py`).
4. **Docker Build:** Builds Docker image tagged with both the Jenkins build ID (`${BUILD_NUMBER}`) and `:latest`.
5. **Push Image:** Authenticates securely to Docker Hub via Jenkins Credentials (`dockerhub-credentials`) and pushes the newly created image.
6. **Minikube Deployment:** Applies `k8s/deployment.yaml` and `k8s/service.yaml`, updating the container image tag and tracking rollout completion.
7. **Verification:** Inspects running pods, deployments, and services via `kubectl`.

---

## 🛠 Repository Structure
```text
├── app.py                  # Main Flask web application (Priyanshu Singh CI/CD UI)
├── test_app.py             # Unit test suite verifying HTTP responses and app data
├── requirements.txt        # Python dependencies (Flask, Werkzeug)
├── Dockerfile              # Containerization definition
├── Jenkinsfile             # Declarative multi-stage Jenkins pipeline
├── k8s/
│   ├── deployment.yaml     # Kubernetes Deployment manifest (2 replicas, resource limits)
│   └── service.yaml        # NodePort Service manifest (port 30080)
└── README.md               # Pipeline documentation and deployment instructions
```

---

## 💻 Commands for Local Execution & Verification

### 1. Start Minikube
```bash
minikube start --driver=docker
```

### 2. Manual Build & Test
```bash
python test_app.py
```

### 3. Deploy to Minikube manually
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
```

### 4. Access the App
```bash
minikube service priyanshu-flask-service --url
```

