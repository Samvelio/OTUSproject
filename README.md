# OTUS

## Как запустить
1. Установка зависимостей: `pip install -r requirements.txt`
2. Запуск API Тестов: `pytest api/tests -v --alluredir=allure-results`
3. Запуск UI Тестов: `pytest ui/tests -v --alluredir=allure-results`
4. Генерация отчета: `allure serve allure-results`

## CI/CD
- Тесты запускаются при пуше
- Allure-отчёт сохраняется как артефакт


- Некоторые тесты оставил зафейленными, так как об этом говорили на созвоне по проектной работе
- Ссылка на запись экрана с запуском тестов: https://disk.yandex.ru/i/T1RCxsoDVbgvKw
