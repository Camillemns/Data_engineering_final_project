pipeline {
    agent any
    stages {
        stage('Git') {
            steps {
                bat 'git status'
                bat 'git branch'
            }
        }
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
        stage('Merge unto dev') {
            steps {
                bat 'echo "merge to dev"'
                bat 'dir'
                bat 'git config --global user.email "jenkins@localhost"'
                bat 'git config --global user.name "jenkins"'
                bat 'git status'
                bat 'git branch'
                bat 'git checkout dev'
                bat 'git merge %BRANCH%'
                withCredentials([string(credentialsId: 'personal_access_token', variable: 'token')]) {
                    bat 'git push https://%token%@github.com/Camillemns/Data_engineering_final_project.git'
                }
            }
        }
        stage('Launch monitoring') {
            steps {
                bat 'echo "launch monitoring"'
            }
        }
        stage('Stress test back') {
            steps {
                bat 'cd ..'
                bat 'docker-compose up tester'
            }
        }
        stage('Merge unto release') {
            steps {
                bat 'echo "merge to release"'
                bat 'dir'
                bat 'git config --global user.email "jenkins@localhost"'
                bat 'git config --global user.name "jenkins"'
                bat 'git status'
                bat 'git branch'
                bat 'git checkout release'
                bat 'git merge dev'
                withCredentials([string(credentialsId: 'personal_access_token', variable: 'token')]) {
                    bat 'git push https://%token%@github.com/Camillemns/Data_engineering_final_project.git'
                }
            }
        }
        stage('End to end test') {
            steps {
                bat 'cd front && npx vue-cli-service test:e2e --headless'
            }
        }
        stage('Merge unto master') {
            steps {
                bat 'echo "merge to master"'
                bat 'dir'
                bat 'git config --global user.email "jenkins@localhost"'
                bat 'git config --global user.name "jenkins"'
                bat 'git status'
                bat 'git branch'
                bat 'git checkout main'
                bat 'git merge release'
                withCredentials([string(credentialsId: 'personal_access_token', variable: 'token')]) {
                    bat 'git push https://%token%@github.com/Camillemns/Data_engineering_final_project.git'
                }
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo "Deploy"'
            }
        }
    }
}