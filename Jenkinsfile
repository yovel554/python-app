pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // cloning the project from GitHub
                git 'https://github.com/yovel554/python-app.git'
            }
        
        stage('Code Formatting'){
                // Format code using black
                sh 'black .'
            }
        }
    }
}