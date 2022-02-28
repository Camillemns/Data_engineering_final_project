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
                bat 'SET PATH=%PATH%;C:/Users/camil/AppData/Local/Programs/Python/Python39/'
                bat 'py --version'
                bat 'py -m pip install requests'
                bat 'py app_test.py'
            }
        }
    }
}
