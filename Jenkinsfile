pipeline {
    agent none

    stages {
        stage('Clone Repository') {
             steps {
                 // Use your actual repository URL
                 git branch: 'main', url: 'https://github.com/nzlefko/python_automation_tests.git'
             }
        }

        stage('Install and Test') {
            // Run this entire stage inside the Python Docker container
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root'
                }
            }
            steps {
                // Streamlined installation within the Docker container
                sh 'pip install -r requirements.txt'
                sh 'pip install allure-pytest'

                // Run tests
                sh 'pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // Runs on the Jenkins agent to ensure file path access
            node(label: 'any') {
                // Publish Allure Report using the required list syntax for results
                allure results: [[path: 'allure-results']], commandline: 'Allure'
            }
        }
    }
}