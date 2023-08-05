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
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'No tests to run'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    echo "Deploying application..."
                    ssh user@host "uwsgi --ini uwsgi.ini"
                '''
            }
        }
    }
}