pipeline {
    agent any

    tools {
        // Use Jenkins-installed SonarScanner here
        sonarRunner 'SonarScanner' // sonarRunner is the correct keyword
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/UmerGulzar223/JenkinsWithSonarQube.git'
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
