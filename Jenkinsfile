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
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\python -m pip install -r requirements.txt
                venv\\Scripts\\python -m pip install pytest pytest-html pytest-cov
                '''
            }
        }

        stage('Build / Compile Check') {
            steps {
                echo 'Checking Python syntax...'
                bat '''
                venv\\Scripts\\python -m py_compile app.py
                '''
            }
        }

        stage('Unit Test') {
            steps {
                echo 'Running unit tests...'
                bat '''
                venv\\Scripts\\python -m pytest test.py ^
                --junitxml=results.xml ^
                --html=report.html ^
                --self-contained-html
                '''
            }
            post {
                always {
                    junit 'results.xml'
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report'
                    ])
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
