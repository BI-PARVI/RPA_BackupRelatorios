pipeline {
  agent any

  environment {
        REPOSITORIO = 'https://github.com/BI-PARVI/Backup_Relatorios.git'
        JIRA_CREDS = credentials('jira_credentials')
        JIRA_URL = 'https://parvibi.atlassian.net/rest/api/3'
        JIRA_PROJECT_KEY = 'SCRUM'
        JIRA_USERS={
        "joao.mendes":"712020:142fa7a7-5676-4a87-8dc8-18e31a0164c0", 
        "allyf.silva":"712020:ced71a53-5125-4244-b88b-0a484a9c998f", 
        "luiz.vinicius":"712020:ab1f2aff-ad2a-4ff3-9488-1e85d70c0202", 
        "gabriel.freitas":"5d828ef68db4330c3b12851c", 
        "yury.souza":"712020:8f406a09-8c1a-4b89-b104-a2e9dc74fcec", 
        "lucas.silva":"712020:34700eb1-c1ab-49eb-8a51-b9713df07c9a"}
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
