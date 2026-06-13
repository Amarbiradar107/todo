pipeline {
    agent any

    stages {

        stage('Pull Latest Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/your-repo/todo.git'
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