import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome_driver(url):
    print("initiating chrome driver")
    # driver = webdriver.Chrome("chrome driver path")
    driver.get(url)
    driver.maximize_window()

    yield driver
    driver.close()

@pytest.fixture(scope="class")
def firefox_driver(url):
    print("initiating firefox driver")
    # driver = webdriver.Firefox("firefox driver path")
    driver.get(url)
    driver.maximize_window()

    yield driver
    driver.close()