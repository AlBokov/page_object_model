from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_message = (By.CLASS_NAME, "error-message-container")
        self.title = (By.CLASS_NAME, "title")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def get_pass_login(self):
        return self.driver.find_element(*self.title).text