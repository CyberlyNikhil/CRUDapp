pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate && pip install Flask Flask-MongoEngine'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'source venv/bin/activate && python -m unittest discover tests'
                }
            }
        }
    }
}
