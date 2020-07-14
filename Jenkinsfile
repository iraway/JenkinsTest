pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.5.1'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r robotframework'
                    sh 'python3 --version'
                }
            }
        }
        stage('Test') {
        	steps {
                sh 'python3 -m robot tests.robot'
            }
        }
    }
}