pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('9de2552f-a42f-4ba8-babb-f4ef4a011a9b')
        DOCKER_IMAGE_NAME = 'abdullah1234123/ml-app'
        ADMIN_EMAIL = 'i222515@nu.edu.pk'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', 
                    url: 'https://github.com/Azmarffs/MLOps-Ass_1.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def image = docker.build("${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}")
                    docker.withRegistry('https://registry-1.docker.io', 'docker-hub-credentials') {
                        image.push()
                        image.push('latest')
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Application deployed successfully!'
            }
        }
    }
    
    post {
        success {
            emailext (
                subject: "✅ Jenkins Job Successful - Build #${BUILD_NUMBER}",
                body: """
                <h2>Jenkins Job Completed Successfully!</h2>
                <p><strong>Project:</strong> ${JOB_NAME}</p>
                <p><strong>Build Number:</strong> ${BUILD_NUMBER}</p>
                <p><strong>Docker Image:</strong> ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}</p>
                <p><strong>Status:</strong> SUCCESS</p>
                <p>The application has been containerized and pushed to Docker Hub.</p>
                """,
                to: "${ADMIN_EMAIL}",
                mimeType: 'text/html'
            )
        }
        failure {
            emailext (
                subject: "❌ Jenkins Job Failed - Build #${BUILD_NUMBER}",
                body: "Jenkins job failed. Please check the logs for details.",
                to: "${ADMIN_EMAIL}"
            )
        }
    }
}

