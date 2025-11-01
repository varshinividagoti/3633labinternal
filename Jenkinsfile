pipeline{
    agent any

    stages {
        stage('Build Docker Image') {
            steps('Build'){
                echo 'Building Docker Image...'
                bat 'docker build -t my-flask-app:latest .'
            }
        }
        stage('Run Docker Container') {
            steps {
                echo 'Running Docker Container...'
                bat 'docker run -d -p 5000:5000 --name flask-container my-flask-app:latest'
            }
        }
    }
}
