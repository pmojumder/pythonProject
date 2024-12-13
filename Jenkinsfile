pipeline {
    agent any
    parameters {
        string(name: 'ARTIFACT_VERSION', defaultValue: '', description: 'Artifact version to deploy')
        string(name: 'DEPLOY_ENVIRONMENT', defaultValue: '', description: 'Deployment environment')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/pmojumder/pythonProject.git'
            }
        }
        stage('Print Parameters') {
            steps {
                script {
                    echo "Artifact Version: ${params.ARTIFACT_VERSION}"
                    echo "Deployment Environment: ${params.DEPLOY_ENVIRONMENT}"
                }
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    bat '''
                        "C:\\Users\\Plabani\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv
                        venv\\Scripts\\activate.bat
                        "C:\\Users\\Plabani\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install --upgrade pip
                        "C:\\Users\\Plabani\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat '''
                        venv\\Scripts\\activate.bat
                        "C:\\Users\\Plabani\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest
                    '''
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up'
            bat 'call venv\\Scripts\\deactivate.bat || echo "Already deactivated"'
        }
    }
}
