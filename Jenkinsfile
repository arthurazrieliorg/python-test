pipeline {
    agent {
        docker {
            image 'python:alpine3.7'
        }
    }

    stages {
        stage('Build') {
            steps {
                pip install -r requirements.txt
            }
        }
        stage('Test') {
            steps {
                python test.py
            }
        }
        stage('Deploy') {
            steps {
                python app.py
            }
        }
    }
}
