pipeline {
    agent any

    environment {
        REPOSITORIO = 'https://github.com/BI-PARVI/Backup_Relatorios.git'
        JIRA_CREDS = credentials('jira_credentials')
        JIRA_URL = 'https://parvibi.atlassian.net/rest/api/3'
        JIRA_PROJECT_KEY = 'SCRUM'
        PATH = "C:\\Program Files\\Python313;C:\\Program Files\\Python313\\Scripts;%PATH%"
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

        stage('Install venv & deps') {
            steps {
                bat """
                  python -m venv .venv
                  .venv\\Scripts\\activate
                  python -m pip install --upgrade pip
                  pip install -r requirements.txt
                """
            }
        }

        stage('Run') {
            steps {
                bat """
                  .venv\\Scripts\\activate
                  python main.py
                """
            }
        }
    }
}
