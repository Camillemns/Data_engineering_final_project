pipeline {
    agent any
    stages {
        stage('Launch Docker Build') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('Launch Docker Compose Front and back') {
            steps {
                bat 'docker-compose up -d front back'
            }
        }
        stage('Unit test front') {
            steps {
                bat 'cd front && npm install'
                bat 'ls'
                bat 'npm run test:unit'
            }
        }
        stage('Stress test back') {
            steps {
                bat 'cd ..'
                bat 'docker-compose up tester'
            }
        }
        stage('End to end test') {
            steps {
                bat 'ls'
                bat 'npm run test:e2e'
            }
        }
    }
}
