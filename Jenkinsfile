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
        stage('Install SQLite') {
            steps {
                sh '''
                    echo "Installing SQLite..."
                    sudo -u jenkins -i jenkins apt install sqlite3      '''
            }
        }
        stage('Load schema') {
            steps {
                sh '''
                    echo "Loading schema..."
                    sqlite3 db.sqlite3 < schema.sql
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
                  . venv/bin/activate
                  python runner.py
                '''
            }
        }
    }
}