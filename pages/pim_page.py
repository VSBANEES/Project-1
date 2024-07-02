from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_pim = (By.ID, "menu_pim_viewPimModule")
        self.add_employee_button = (By.ID, "btnAdd")
        self.first_name_field = (By.NAME, "firstName")
        self.last_name_field = (By.NAME, "lastName")
        self.save_button = (By.XPATH, '//button[contains(text(), "Save")]')

    def open_pim_module(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPimModule")

    def add_new_employee(self, first_name, last_name):
        self.open_pim_module()
        self.click_element(self.add_employee_button)
        self.find_element(self.first_name_field).send_keys(first_name)
        self.find_element(self.last_name_field).send_keys(last_name)
        self.click_element(self.save_button)

    def edit_employee(self, employee_id, new_first_name):
        # Implement editing functionality as needed
        pass

    def delete_employee(self, employee_id):
        # Implement deletion functionality as needed
        pass