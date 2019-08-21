import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome_driver():
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.close()

@pytest.fixture(scope="class")
def firefox_driver():
    print("initiating firefox driver")
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
    driver.close()