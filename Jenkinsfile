pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                dir('todo') {
                    sh 'docker compose build'
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('todo') {
                    sh '''
                        docker compose down
                        docker compose up -d
                    '''
                }
            }
        }
    }
}