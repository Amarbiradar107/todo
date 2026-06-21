pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
        steps {
                sh 'docker build -t todo-app:${BUILD_NUMBER} .'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    docker stop todo_app_container || true
                    docker rm todo_app_container || true

                    docker run -d \
                      --name todo_app_container \
                      -p 8000:8000 \
                      todo-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}