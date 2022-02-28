pipeline {
    agent any
    stages {
        stage('ls') { 
            steps {
                bat 'dir'
                bat 'cd back && dir'
            }
        }
        stage('Git') { 
            steps {
                bat 'git status'
            }
        }
        stage('Launch Docker Build') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('Launch Docker Compose') {
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage('Test back') {
            steps {
                bat 'SET PATH = pythonpath'
                bat 'python app_test.py"'
            }
        }
    }
}
