Jenkinsfile(Declarative Pipeline)
/* Requires the Docker Pipeline plugin * /
pipeline {
    agent {docker {image 'python:3.10.8-alpine'}}
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
