pipeline {
    agent any

    environment {
        PATH = "/opt/sonar-scanner/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/UmerGulzar223/JenkinsWithSonarQube.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner -Dsonar.projectKey=jenkins-sonar-project -Dsonar.sources=.'
                }
            }
        }
    }
}
