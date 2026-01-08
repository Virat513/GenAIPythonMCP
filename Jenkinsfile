pipeline {
    agent any

    tools {
        python 'Python310'   // Name of Python installation in Jenkins
        allure 'allure'
    }

    environment {
        ALLURE_RESULTS = "allure-results"
        GITHUB_TOKEN = credentials('github-pat-genai') // secure GitHub PAT
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/Virat513/GenAIPythonMCP.git',
                    credentialsId: 'github-pat-genai'
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
echo Creating virtual environment...
python -m venv venv
call venv\\Scripts\\activate
echo Upgrading pip...
python -m pip install --upgrade pip
"""
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
call venv\\Scripts\\activate
echo Installing requirements...
pip install -r requirements.txt
pip install allure-pytest pytest
"""
            }
        }

        stage('Run Pytest Tests') {
            steps {
                bat """
call venv\\Scripts\\activate
echo Running pytest...
pytest --alluredir=${ALLURE_RESULTS}
"""
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }

    post {
        always {
            echo "Archiving allure-results..."
            archiveArtifacts artifacts: "${ALLURE_RESULTS}/**", allowEmptyArchive: true
        }
    }
}
