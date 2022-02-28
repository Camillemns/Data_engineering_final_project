pipeline {
    agent any
    stages {
        stage('Git') { 
            steps {
                bat 'git pull'
                bat 'git checkout dev'
                bat 'git pull'
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
                echo "test front"
            }
        }
    }
}
