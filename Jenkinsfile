pipeline {
    agent any

    environment {
        REPOSITORIO = 'https://github.com/BI-PARVI/Backup_Relatorios.git'
        JIRA_CREDS = credentials('jira_credentials')
        JIRA_URL = 'https://parvibi.atlassian.net/rest/api/3'
        JIRA_PROJECT_KEY = 'SCRUM'
        JIRA_USER = "${JIRA_CREDS_USR}"
        JIRA_TOKEN = "${JIRA_CREDS_PSW}"
    }

    triggers {
        cron('H/10 7-19 * * *')
    }

    options {
        timestamps()
    }

    stage('Debug Variáveis') {
    steps {
        bat 'echo JIRA_USER=%JIRA_USER%'
        bat 'echo JIRA_TOKEN=%JIRA_TOKEN%'
    }
}

    stages {
        stage('Clonar o repositório') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/BI-PARVI/RPA_BackupRelatorios.git'
            }
        }

        stage('Instalar dependências') {
            steps {
                bat '"C:\\Users\\adm.luiz.vinicius\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe" install -r requirements.txt'
            }
        }

        stage('Executar script Python') {
            steps {
                bat '''
                C:\\Users\\adm.luiz.vinicius\\AppData\\Local\\Programs\\Python\\Python312\\python.exe main.py
                '''
            }
        }
    }
}
