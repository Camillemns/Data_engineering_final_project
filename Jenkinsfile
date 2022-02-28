pipeline {
    agent any
    stages {
        stage('Git pull') { 
            steps {
                bat  'dir'
            }
        }
        stage('Launch Docker Build') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('Launch Docker Build') { 
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
