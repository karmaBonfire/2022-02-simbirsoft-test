import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .mail_app_compose import MailAppCompose

class MailAppMain:
    """Модель главной страницы приложения"""

    def __init__(self, driver):
        self.driver = driver
    
    @property
    def search_bar(self):
        """Обёртка строки поиска (без фокуса)"""
        return self.driver.find_element(By.CSS_SELECTOR, ".search-input__form")
    
    @property
    def search_bar_input(self):
        """input строки поиска"""
        return self.driver.find_element(By.CSS_SELECTOR, ".search-input__form .textinput__control")
    
    @property
    def search_result_description(self):
        """Комментарий к результатам поиска с количеством результатов"""
        return self.driver.find_element(By.CSS_SELECTOR, ".mail-MessagesSearchInfo-Title_misc")
    
    @property
    def composeButton(self):
        """Кнопка 'Написать' для перехода в интерфейс создания письма"""
        return self.driver.find_element(By.CSS_SELECTOR, ".mail-ComposeButton.js-main-action-compose")
    
    @allure.step('Clicked search bar')
    def clickSeachBar(self):
        self.search_bar.click()
        return self
    
    @allure.step('Entered search query')
    def inputSearchQuery(self, query):
        self.search_bar_input.send_keys(query)
        return self
    
    @allure.step('Pressed Enter in search bar')
    def sendEnterToSearchQuery(self):
        self.search_bar_input.send_keys(Keys.ENTER)
        return self
    
    def getSearchResultAmount(self):
        return self.search_result_description.text
    
    @allure.step('Clicked "Compose" button')
    def clickComposeButton(self):
        self.composeButton.click()
        return MailAppCompose(self.driver)
    
    @allure.step('Created a screenshot')
    def screenshot(self, path='.\\screenshot.png'):
        self.driver.save_screenshot(path)
        return self