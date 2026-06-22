pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "todo"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Cleanup') {
            steps {
                dir('todo') {
                    sh '''
                        docker compose -p ${COMPOSE_PROJECT_NAME} down --remove-orphans || true

                        docker stop todo-nginx-1 || true
                        docker rm -f todo-nginx-1 || true

                        docker image prune -f
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                dir('todo') {
                    sh '''
                        docker compose -p ${COMPOSE_PROJECT_NAME} build
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('todo') {
                    sh '''
                        docker compose -p ${COMPOSE_PROJECT_NAME} up -d
                    '''
                }
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    docker ps
                '''
            }
        }
    }
}