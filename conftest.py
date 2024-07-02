import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()
