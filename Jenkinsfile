pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Program Files\\Python313\\python.exe"
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
                  "%PYTHON_PATH%" -m venv .venv
                  call .venv\\Scripts\\activate.bat
                  python -m pip install --upgrade pip
                  pip install -r requirements.txt
                  python main.py
                """
            }
        }
    }
}
