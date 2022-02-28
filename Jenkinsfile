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
        stage('Test back') { 
            steps {
                bat 'docker-compose run back bash -c "ls -a && sleep 500 && python app_test.py"'
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
    }
}
