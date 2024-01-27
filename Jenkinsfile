pipeline {
    agent {
            label 'linux'
          }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install Flask Flask-MongoEngine'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }
    }
}

