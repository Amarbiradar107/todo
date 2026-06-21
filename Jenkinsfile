pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('cleanup') {

            steps {}
                dir('todo') {
                    sh 'docker ps -a'
                    sh 'docker compose down'
                    sh 'docker container prune -f'
                }
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