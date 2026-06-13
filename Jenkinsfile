pipeline {
    agent any

    stages {

        stage('Pull Latest Code') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Build Containers') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down'
                sh 'docker compose up -d'
            }
        }
    }
}