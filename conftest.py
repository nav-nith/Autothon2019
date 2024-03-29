import pytest
import logging
from appium import webdriver as appium_webdriver
from selenium import webdriver as selenium_webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.chrome.options import Options
import os

MOBILE_CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chromedrivers", "chromedriver_mobile_74.exe")
DESKTOP_CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chromedrivers", "chromedriver_desktop_76.exe")

log = logging.getLogger("CONFTEST")
log.setLevel(logging.DEBUG)


APPIUM_HOST = "localhost"
APPIUM_PORT = 4723


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Add for headless browser")
    parser.addoption("--mobile", action="store_true", default=False, help="Run on mobile. Default: run on desktop")


# @pytest.fixture(scope="class")
# def appium():
#     appium = AppiumService()

#     log.debug(f"Starting Appium Server")
#     appium.start(args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)])

#     yield

#     log.debug(f"Stopping Appium Server")
#     appium.stop()


def get_chrome_driver(is_headless):
    log.info("initiating chrome driver in web browzer")

    chrome_options = Options()
    if is_headless:
        chrome_options.add_argument("--headless")

    chrome_driver = selenium_webdriver.Chrome(DESKTOP_CHROMEDRIVER_PATH, options=chrome_options)
    chrome_driver.maximize_window()

    return chrome_driver


def get_mobile_driver():
    log.info("initiating chrome driver in mobile browzer")
    
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'emulator-5554 (10)'
    desired_caps['autoGrantPermissions'] = 'True'
    desired_caps['autoDismissAlerts'] = 'True'
    desired_caps['noReset'] = 'True'
    desired_caps['chromedriverExecutable'] = MOBILE_CHROMEDRIVER_PATH
    desired_caps['browserName'] = 'Chrome'
    desired_caps['nativeWebScreenshot'] = 'True'

    mobile_driver = appium_webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub', desired_caps)

    return mobile_driver


@pytest.fixture(scope="class")
def driver(request):
    is_mobile = request.config.getoption("--mobile")
    is_headless = request.config.getoption("--headless")

    request.cls.is_mobile = is_mobile

    if is_mobile:
        mobile_driver = get_mobile_driver()
        yield mobile_driver
        mobile_driver.close()
    else:
        chrome_driver = get_chrome_driver(is_headless)
        yield chrome_driver
        chrome_driver.close()
