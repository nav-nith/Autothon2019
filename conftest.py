import pytest
import logging
from appium import webdriver


@pytest.fixture(scope="class")
def chrome_driver():
    logging.info("initiating chrome driver in web browzer")

    desired_caps = dict()
    desired_caps['browserName'] = 'Chrome'

    chrome_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    chrome_driver.maximize_window()

    yield chrome_driver

    chrome_driver.close()

@pytest.fixture(scope="class")
def mobile_driver():
    logging.info("initiating chrome driver in mobile browzer")
    
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = 'Auto'
    desired_caps['deviceName'] = 'Auto'
    desired_caps['autoGrantPermissions'] = 'True'
    desired_caps['autoDismissAlerts'] = 'True'
    desired_caps['noReset'] = 'True'
    # desired_caps['chromedriverExecutable'] = 'chrome'
    desired_caps['browserName'] = 'Chrome'

    mobile_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield mobile_driver

    mobile_driver.close()