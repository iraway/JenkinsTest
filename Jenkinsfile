pipeline {
    agent { docker { image 'robotframework/rfdocker:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'pip3 install robotframework'
            }
        }
        stage('test') {
            steps {
                sh 'robot tests.robot'
            }
        }
    }
}