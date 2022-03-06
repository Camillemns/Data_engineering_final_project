pipeline {
    agent any
    stages {
        stage('See the repository') {
            steps {
                bat 'dir'
                bat 'cd front && dir'
            }
        }
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
                bat 'cd front && npm run test:unit'
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
                bat 'cd front && npx vue-cli-service test:e2e --headless'
            }
        }
    }
}
