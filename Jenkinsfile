pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // For Windows, use 'bat' instead of 'sh'
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate && pip install Flask Flask-MongoEngine'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // For Windows, use 'bat' instead of 'sh'
                    bat 'venv\\Scripts\\activate && python -m unittest discover tests'
                }
            }
        }
    }
}

