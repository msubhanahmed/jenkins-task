pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the GitHub repository
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest on the test.py file
                sh 'pytest test.py'
            }
        }
    }

    post {
        always {
            // Cleanup steps if needed
        }
    }
}
