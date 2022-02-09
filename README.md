# 2022-02-simbirsoft-test

## Установка

- Создайте виртуальное окружение (venv)
- `pip install -r requirements.txt`
- Измените значения в `config.json` (логин и пароль от почты)

## Использование

- Запустите Selenium Grid (сначала hub, затем node)
- Запустите тесты, указав папку для отчётов Allure: `python -m pytest main.py --alluredir=.\allure_results`
- Для просмотра отчётов `python -m allure serve .\allure_results`
