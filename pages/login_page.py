from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, 'username')
        self.password_input = (By.NAME, 'password')
        self.login_button = (By.XPATH, '//button[@type="submit"]')

    def open_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def input_text(self, locator, text):
        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def login(self, username, password):
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def get_error_message(self):
        error_message_locator = (By.XPATH, '//p[contains(@class, "oxd-alert-content-text")]')
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(error_message_locator)
        ).text