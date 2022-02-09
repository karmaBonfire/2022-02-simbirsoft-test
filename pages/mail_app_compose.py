import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MailAppCompose:
    def __init__(self, driver) -> None:
        self.driver = driver
    
    @property
    def mailToInput(self):
        """Поле для ввода адресата письма (To:)"""
        return self.driver.find_element(By.CSS_SELECTOR, ".ComposeRecipients-ToField .composeYabbles")
    
    @property
    def mailSubjectInput(self):
        """Поле для ввода темы письма (Subject:)"""
        return self.driver.find_element(By.CSS_SELECTOR, ".ComposeSubject input.ComposeSubject-TextField")
    
    @property
    def mailContentInput(self):
        """Поле для ввода тела письма (WYSIWYG-редактор)"""
        return self.driver.find_element(By.CSS_SELECTOR, ".mail-Editor .cke_wysiwyg_div")
    
    @property
    def mailSendButton(self):
        """Кнопка отправки письма"""
        return self.driver.find_element(By.CSS_SELECTOR, ".ComposeSendButton")

    @allure.step('Filled "To:" field')
    def inputMailRecipientTo(self, string):
        self.mailToInput.send_keys(string)
        return self
    
    @allure.step('Filled "Subject:" field')
    def inputMailSubject(self, string):
        self.mailSubjectInput.click()
        self.mailSubjectInput.send_keys(string)
        return self

    @allure.step('Filled mail contents')
    def inputMailContent(self, string):
        self.mailContentInput.send_keys(string)
        return self
    
    @allure.step('Clicked "Send" button')
    def clickSendButton(self):
        self.mailSendButton.click()
        return self
