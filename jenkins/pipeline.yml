pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-login' // ID des identifiants créés dans Jenkins
        IMAGE_NAME = "ton_user_dockerhub/tonnom-flask-app"
    }

    stages {
        stage('Clonage') {
            steps {
                // Jenkins clone automatiquement si le fichier est dans le dépôt
                checkout scm
            }
        }
        
        stage('Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }
        
        stage('Publication') {
            steps {
                script {
                    docker.withRegistry('', DOCKERHUB_CREDENTIALS) {
                        sh "docker push ${IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}