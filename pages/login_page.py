import allure
from selenium.webdriver.common.by import By
from .mail_app_main import MailAppMain

class LoginPage:
    """Модель страницы для входа в аккаунт Яндекс"""

    def __init__(self, driver):
        self.driver = driver
    
    @property
    def login_input(self):
        """Поле для ввода логина"""
        return self.driver.find_element(By.CSS_SELECTOR, "#passp-field-login")
    
    @property
    def signin_button(self):
        """Кнопка для входа"""
        return self.driver.find_element(By.ID, "passp:sign-in")
    
    @property
    def password_input(self):
        """Поле для ввода пароля"""
        return self.driver.find_element(By.CSS_SELECTOR, "#passp-field-passwd")

    @allure.step('Entered login')
    def inputLogin(self, string):
        self.login_input.send_keys(string)
        return self
    
    @allure.step('Entered password')
    def inputPassword(self, string):
        self.password_input.send_keys(string)
        return self
    
    @allure.step('Clicked "Continue" button')
    def clickNextButton(self):
        self.signin_button.click()
        return self

    @allure.step('Clicked "Sign in" button')
    def clickSigninButton(self):
        self.signin_button.click()
        return MailAppMain(self.driver)
