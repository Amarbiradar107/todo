pipeline {
    agent any

    stages {

        stage('Deploy') {
            steps {
                    sh '''
                    pwd
                    cd /home/ubuntu/todoproject
                    git pull origin main
                    docker compose down
                    docker compose up -d --build
                    '''
            }
        }
    }
}