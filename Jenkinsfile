pipeline {
    agent {
        docker {
            image 'python:alpine3.7'
        }
    }

    stages {
	stage('Version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python test.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
