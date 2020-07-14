pipeline {
    agent { docker { image 'python:3.5.1', args:'-u root:root' } }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('test') {
            steps {
                sh 'python3 -m robot tests.robot'
            }
        }
    }
}