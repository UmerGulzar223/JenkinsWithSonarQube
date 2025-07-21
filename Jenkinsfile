pipeline {
    agent any

    tools {
        sonarQubeScanner 'SonarScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/UmerGulzar223/JenkinsWithSonarQube.git'  // or use local
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonar') {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
