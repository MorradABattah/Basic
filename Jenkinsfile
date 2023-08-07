pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Setting up virtual environment and installing requirements...'
                sh '''
                  python3 -m venv venv || exit 1
                  . venv/bin/activate
                  pip install -r requirements.txt || exit 1
                '''
            }
        }
        
        stage('Install SQLite') {
            steps {
                echo 'Installing SQLite...'
                withCredentials([string(credentialsId: 'jenkins', variable: 'password')]) {
                    sh '''
                        which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                        brew update
                        brew install sqlite || exit 1
                    '''
                }
            }
        }
        
        stage('Load schema') {
        steps {
           echo 'Loading database schema using Python script...'
    sh '''
        . venv/bin/activate
        python load_schema.py || exit 1
        mkdir uploads || exit 1
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
                  python runner.py || exit 1
                '''
            }
        }
    }
}
