pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy') {
            steps {
                dir('todo') {
                    sh '''
                        docker compose up -d --build
                    '''
                }
            }
        }
    }
}