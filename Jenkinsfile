pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "priyanshu11/flask-cicd-app"
        DOCKER_CREDENTIALS_ID = "dockerhub-credentials"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                echo 'Running tests and linting...'
                sh '''
                    python3 -m venv venv || virtualenv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python3 test_app.py
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker Image...'
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                    docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Push Image') {
            steps {
                echo 'Pushing Docker Image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }

        stage('Minikube Deployment') {
            steps {
                echo 'Deploying to Kubernetes / Minikube...'
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl set image deployment/priyanshu-flask-deployment flask-container=${DOCKER_IMAGE}:${BUILD_NUMBER}
                    kubectl rollout status deployment/priyanshu-flask-deployment --timeout=120s
                '''
            }
        }

        stage('Verification') {
            steps {
                echo 'Verifying deployment status and running pods...'
                sh '''
                    kubectl get nodes
                    kubectl get deployments
                    kubectl get pods -l app=priyanshu-flask
                    kubectl get svc priyanshu-flask-service
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD Pipeline executed successfully for Priyanshu Singh!"
        }
        failure {
            echo "CI/CD Pipeline failed. Please check build console logs."
        }
    }
}

