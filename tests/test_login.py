import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_valid_login(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(driver)

    # Wait for the username input to be visible
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )

    login_page.login("Admin", "admin123")

    # Assert login success (implement based on your application behavior)


def test_invalid_login(setup):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(driver)

    # Wait for the username input to be visible
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )

    login_page.login("Admin", "invalid_password")

    # Wait for the error message to be visible
    error_message = login_page.get_error_message()
    assert "Invalid credentials" in error_message