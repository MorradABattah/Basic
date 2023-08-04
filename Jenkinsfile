pipeline {
    agent any

    stages {
        stage('Pull from Repository') {
            steps {
                git 'https://github.com/MorradABattah/Basic.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install flask flask_sqlalchemy'
            }
        }
        stage('Test') {
            steps {
                // Here you would typically run your tests. 
                // We have none to run in this case.
                echo 'No tests to run'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
