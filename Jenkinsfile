pipeline {
    agent {
        node {
         // label 'slaveslave'
	    label 'margarita'
        }
    }
/*
    agent {
        docker {
            image 'python:alpine3.7'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
*/

//    agent any

    stages {
	    stage('Version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Build') {
            steps {
                sh 'apt-get update && apt-get install -y \
                        php5-mcrypt \
                        python-pip'
                sh 'pip --no-cache-dir install -r requirements.txt'
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
