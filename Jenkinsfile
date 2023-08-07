pipeline {
    agent any

    environment {
        DATABASE_URL = 'postgresql://username:password@localhost:5433/mydatabase'
        SECRET_KEY = 'your_secret_key'  // Ideally, this should be stored securely
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up virtual environment and installing requirements...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Setup PostgreSQL') {
            steps {
                echo 'Setting up PostgreSQL...'
                withCredentials([string(credentialsId: 'jenkins', variable: 'password')]) {
                    sh '''
                        which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                        brew update
                        brew install postgresql@15
                        brew services start postgresql@15
                        /usr/local/Cellar/postgresql@15/15.3_2/bin/dropdb --if-exists mydatabase
                        /usr/local/Cellar/postgresql@15/15.3_2/bin/createdb mydatabase
                    '''
                }
            }
        }

        stage('Reinstall psycopg2') {
            steps {
                echo 'Reinstalling psycopg2...'
                sh '''
                    . venv/bin/activate
                    pip uninstall -y psycopg2
                    export PATH=$PATH:/usr/local/Cellar/postgresql@15/15.3_2/bin
                    pip install psycopg2
                '''
            }
        }

        stage('Load schema') {
            steps {
                echo 'Loading database schema using Python script...'
                sh '''
                    . venv/bin/activate
                    python load_schema.py
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
                echo 'Running deployment script...'
                sh '''
                    . venv/bin/activate
                    python runner.py
                '''
            }
        }
    }
}
