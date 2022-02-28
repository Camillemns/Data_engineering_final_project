pipeline {
    agent { docker { image 'python:3.6' } }
    stages {
        stage('ls') { 
            steps {
                bat 'dir'
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
        stage('Test front') { 
            steps {
                echo "test front"
            }
        }
        stage('Test back') { 
            steps {
                echo "test back"
                bat 'python --version'
            }
        }
    }
}
