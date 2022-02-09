from pages import MailLanding

from collections import namedtuple
import json

import allure
from selenium import webdriver
import pytest

Credentials = namedtuple('Credentials', ['login', 'password'])

class TestCases:
    @pytest.fixture
    def account_credentials(self):
        """Считывает данные для входа в аккаунт из конфига"""
        with open('config.json') as f:
            config = json.load(f)
        return Credentials(
            login=config['yandex_account']['login'],
            password=config['yandex_account']['password']
        )

    @pytest.fixture
    def driver(self):
        """Инициализирует WebDriver"""
        USE_REMOTE = True

        if USE_REMOTE:
            options = webdriver.FirefoxOptions()
            options.set_capability('javascriptEnabled', 'true')
            driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                options=options
            )
        else:
            driver = webdriver.Firefox(executable_path='.\\resources\\geckodriver.exe')
        
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(MailLanding.URL)
        yield driver
        # driver.close()
        driver.quit()

    @allure.title("Main test")
    @allure.description("""
    This test:
    - Logs user in Yandex Mail;
    - Reads the amount of mail with specific title;
    - Sends a new mail with the amount found.
    """)
    def test_mailing(self, driver, account_credentials):
        SEARCH_QUERY = 'папка:Входящие Simbirsoft Тестовое задание'

        NEW_MAIL_TO = account_credentials.login + '@yandex.ru'
        NEW_MAIL_SUBJECT = 'Simbirsoft Тестовое задание. Давыдов'
        NEW_MAIL_TEMPLATE = '{answer}'

        SCREENSHOT_PATH = '.\\screenshot.png'

        mail_landing = MailLanding(driver)
        login_page = mail_landing.clickLoginButton()
        mail_app_page = (
            login_page
            .inputLogin(account_credentials.login)
            .clickNextButton()
            .inputPassword(account_credentials.password)
            .clickSigninButton()
        )
        answer = (
            mail_app_page
            .clickSeachBar()
            .inputSearchQuery(SEARCH_QUERY)
            .sendEnterToSearchQuery()
            .screenshot(SCREENSHOT_PATH)
            .getSearchResultAmount()
        )

        # присоединяем скриншот к отчёту
        allure.attach.file(SCREENSHOT_PATH, name='Search result screenshot', attachment_type=allure.attachment_type.PNG)

        (
            mail_app_page
            .clickComposeButton()
            .inputMailRecipientTo(NEW_MAIL_TO)
            .inputMailSubject(NEW_MAIL_SUBJECT)
            .inputMailContent(NEW_MAIL_TEMPLATE.format(answer=answer))
            .clickSendButton()
        )