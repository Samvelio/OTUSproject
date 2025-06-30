pipeline {
    agent any

    environment {
        PROJECT_DIR = "${WORKSPACE}"
        VENV_PATH = "${PROJECT_DIR}/venv"
        ALLURE_RESULTS = "${PROJECT_DIR}/allure-results"
        ALLURE_REPORT = "${PROJECT_DIR}/allure-report"
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    echo "Установка системных зависимостей..."
                    sudo apt update -qq
                    sudo apt install -y python3-venv python3-pip firefox

                    echo "Установка geckodriver..."
                    wget -q https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
                    tar -xvzf geckodriver-*.tar.gz
                    sudo mv geckodriver /usr/local/bin/
                    sudo chmod +x /usr/local/bin/geckodriver
                    rm geckodriver-*.tar.gz
                '''
            }
        }

        stage('Prepare Environment') {
            steps {
                sh '''
                    echo "Создание виртуального окружения..."
                    python3 -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Запуск тестов..."
                    . ${VENV_PATH}/bin/activate
                    pytest api/tests -v --alluredir=${ALLURE_RESULTS}
                    pytest ui/tests -v --browser=firefox --alluredir=${ALLURE_RESULTS}
                '''
            }
        }

        stage('Generate Report') {
            steps {
                sh '''
                    echo "Генерация Allure-отчета..."
                    . ${VENV_PATH}/bin/activate
                    allure generate ${ALLURE_RESULTS} -o ${ALLURE_REPORT} --clean
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                jdk: '',
                results: [[path: "${ALLURE_RESULTS}"]],
                reportBuildPolicy: 'ALWAYS'
            cleanWs()
        }
    }
}
