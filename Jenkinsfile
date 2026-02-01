pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest pytest-html pytest-cov
                '''
            }
        }

        stage('Build / Compile Check') {
            steps {
                echo 'Checking Python syntax...'
                bat '''
                call venv\\Scripts\\activate
                python -m py_compile app.py
                '''
            }
        }

        stage('Unit Test') {
            steps {
                echo 'Running unit tests with pytest...'
                bat '''
                call venv\\Scripts\\activate
                mkdir test-reports
                pytest test.py --junitxml=test-reports\\results.xml
                '''
            }
        }
    }

    post {
        success {
            echo 'Python CI Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs and test reports.'
        }
    }
}
