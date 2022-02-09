
import allure
from selenium.webdriver.common.by import By
from .login_page import LoginPage

class MailLanding:
    """Модель страницы-лендинга до входа в аккаунт"""

    URL = 'https://mail.yandex.ru'

    def __init__(self, driver):
        self.driver = driver
    
    @property
    def login_button(self):
        """Кнопка 'Войти'"""
        return self.driver.find_element(By.CSS_SELECTOR, ".HeadBanner-Button-Enter")

    @allure.step('Clicked Login button')
    def clickLoginButton(self):
        self.login_button.click()
        return LoginPage(self.driver)
