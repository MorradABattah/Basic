pipeline {
    agent any

    stages {
        stage('Pull from Repository') {
            steps {
                git url: 'https://github.com/MorradABattah/Basic.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
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
                sh 'source venv/bin/activate && python app.py'
            }
        }
    }
}
