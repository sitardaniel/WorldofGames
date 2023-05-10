pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                sh 'docker exec myapp-container python e2e.py --url http://localhost:8777'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose build'
                sh 'docker tag myapp <your-dockerhub-username>/myapp:latest'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                    sh 'docker push <your-dockerhub-username>/myapp:latest'
                }
            }
        }
    }
}

