pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m venv venv'
                    bat 'venv\\Scripts\\activate && pip install Flask Flask-MongoEngine'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat 'venv\\Scripts\\activate && python -m unittest discover tests'
                }
            }
        }
    }
}

