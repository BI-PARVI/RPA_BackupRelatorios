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

    stage('Install venv & deps') {
      steps {
        sh '''
          python -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run') {
      steps {
        sh '''
          . .venv/bin/activate
          python main.py
        '''
      }
    }
  }
}
