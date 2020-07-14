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
                    sh 'pip3 install --user robotframework'
                    sh 'python3 --version'
                    sh 'python3 -m robot --version'
                }
            }
        }
        stage('Test') {
        	steps {
                sh 'robot tests.robot'
            }
        }
    }
}