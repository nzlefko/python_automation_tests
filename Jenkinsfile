pipeline {
    // 1. Set the top-level agent to 'none'
    agent none

    stages {
        stage('Clone Repository') {
             // Optional: You can keep a simple git step here if you want to ensure the clone runs immediately
             steps {
                 git branch: 'main', url: 'YOUR_GITHUB_REPO_URL'
             }
        }

        stage('Install and Test') {
            // 2. Define the Docker agent within the stage
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root'
                }
            }
            steps {
                // 3. The streamlined installation and test steps (no apt-get or venv source needed)
                sh 'pip install -r requirements.txt'
                sh 'pip install allure-pytest'
                sh 'pytest --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // 4. Wrap the allure step in a node block to restore file access
            node {
                // Use the simplest, most compatible allure syntax
                allure 'allure-results'

                // OR: If the simplest form fails, use this (but try the simpler first):
                // allure results: 'allure-results', commandline: 'Allure', history: 20
            }
        }
    }
}