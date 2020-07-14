pipeline {
    withDockerContainer { image 'python:3.5.1', args:'-u root:root' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    sh 'python WebChecker.py'
                }
                sh "python3 --version"
            }
        }
        stage('test') {
            steps {
                sh 'python3 -m robot tests.robot'
            }
        }
    }
}