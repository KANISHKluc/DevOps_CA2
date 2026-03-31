pipeline {
    agent any

    environment {
        // You can define paths or specific configurations here
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                // Get code from your version control system or workspace
                checkout scm
                echo 'Source code checked out.'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                // Check if python is in PATH
                bat 'python --version'
                // Use python -m pip to avoid pip PATH issues
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Selenium automated tests...'
                // Run the Python test script
                bat 'python test_form.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up workspace or archiving artifacts if needed.'
            // You can archive test results here, e.g. archiveArtifacts 'test-reports/*.xml'
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
