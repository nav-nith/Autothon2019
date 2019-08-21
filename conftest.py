import pytest
import logging
from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.chrome.options import Options

log = logging.getLogger("CONFTEST")
log.setLevel(logging.DEBUG)


APPIUM_HOST = "localhost"
APPIUM_PORT = 4723


@pytest.fixture(scope="class")
def appium():
    appium = AppiumService()

    log.debug(f"Starting Appium Server")
    appium.start(args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)])

    yield

    log.debug(f"Stopping Appium Server")
    appium.stop()


@pytest.fixture(scope="class")
def chrome_driver():
    log.info("initiating chrome driver in web browzer")

    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    chrome_driver = selenium_webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()

    yield chrome_driver

    chrome_driver.close()

@pytest.fixture(scope="class")
def mobile_driver():
    log.info("initiating chrome driver in mobile browzer")
    
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'emulator-5554 (10)'
    desired_caps['autoGrantPermissions'] = 'True'
    desired_caps['autoDismissAlerts'] = 'True'
    desired_caps['noReset'] = 'True'
    # desired_caps['chromedriverExecutable'] = 'chrome'
    desired_caps['browserName'] = 'Chrome'

    mobile_driver = appium_webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub', desired_caps)

    yield mobile_driver

    mobile_driver.close()
