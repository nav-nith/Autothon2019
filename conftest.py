import pytest
import logging
from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver
from appium.webdriver.appium_service import AppiumService


log = logging.getLogger("CONFTEST")
log.setLevel(logging.DEBUG)


@pytest.fixture
def appium():
    appium = AppiumService()

    log.debug(f"Starting Appium Server")
    appium.start()

    yield

    log.debug(f"Stopping Appium Server")
    appium.stop()


@pytest.fixture(scope="class")
def chrome_driver():
    log.info("initiating chrome driver in web browzer")

    chrome_driver = selenium_webdriver.Chrome()
    chrome_driver.maximize_window()

    yield chrome_driver

    chrome_driver.close()

@pytest.fixture(scope="class")
def mobile_driver():
    log.info("initiating chrome driver in mobile browzer")
    
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = 'Auto'
    desired_caps['deviceName'] = 'Auto'
    desired_caps['autoGrantPermissions'] = 'True'
    desired_caps['autoDismissAlerts'] = 'True'
    desired_caps['noReset'] = 'True'
    # desired_caps['chromedriverExecutable'] = 'chrome'
    desired_caps['browserName'] = 'Chrome'

    mobile_driver = appium_webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield mobile_driver

    mobile_driver.close()
