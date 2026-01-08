pipeline {
    agent any

    tools {
        allure 'allure'
    }

    environment {
        ALLURE_RESULTS = "allure-results"
        // GITHUB_TOKEN = credentials('github-pat-genai') // optional if private repo
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/Virat513/GenAIPythonMCP.git'
                    // credentialsId: 'github-pat-genai' // uncomment if private repo
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
echo Upgrading pip...
python -m pip install --upgrade pip
echo Installing required Python packages...
pip install -r requirements.txt
pip install pytest allure-pytest
"""
            }
        }

        stage('Run Pytest Tests') {
            steps {
                bat """
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
