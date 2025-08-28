pipeline {
    agent any

    environment {
        REPOSITORIO = 'https://github.com/BI-PARVI/Backup_Relatorios.git'
        JIRA_CREDS = credentials('jira_credentials')
        JIRA_URL = 'https://parvibi.atlassian.net/rest/api/3'
        JIRA_PROJECT_KEY = 'SCRUM'
    }

    triggers {
        cron('H/10 0-19 * * *')
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup & Run') {
            steps {
                bat """
                  "C:\\Program Files\\Python313\\python.exe" -m venv .venv
                  call .venv\\Scripts\\activate.bat
                  python -m pip install --upgrade pip
                  pip install -r requirements.txt
                  python main.py
                """
            }
        }
    }
}
