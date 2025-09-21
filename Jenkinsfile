pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // This step is often handled automatically by Jenkins if you configure the job with SCM
                git branch: 'main', url: 'https://github.com/nzlefko/python_automation_tests.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python and pip first if they are not present
                // Example for a Debian/Ubuntu-based Jenkins image
                sh 'apt-get update'
                sh 'apt-get install -y python3 python3-pip'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'pip install allure-pytest'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate'
                sh 'pytest --alluredir=allure-results'
            }
        }
    }
    post {
        always {
            // This step publishes the Allure report in Jenkins
            allure report: 'allure-results', commandline: 'Allure', results: [
                [type: 'directory', source: 'allure-results', results: [retention: [ history: 20]]]
            ]
        }
    }
}