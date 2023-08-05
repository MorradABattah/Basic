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
                    ssh user@localhost "uwsgi --ini uwsgi.ini"
                '''
            }
        }
    }
}

#ssh 192.168.1.100 'uwsgi --ini uwsgi.ini'
