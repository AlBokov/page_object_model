import pytest
from selenium import webdriver
from pages.pages import LoginPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

