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
                bat 'docker-compose up -d front back'
            }
        }
        stage('Stress test back') {
            steps {
                bat 'docker-compose run tester /bin/sh ./wait-for-it.sh back:8000 --timeout=0 -- python app_test.py'
            }
        }
    }
}
