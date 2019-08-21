import pytest
import logging

class TestAutothon():
    def test_a(self, chrome_driver):
        chrome_driver.get("https://www.youtube.com")
        # mobile_driver.get("https://www.youtube.com")
        # print(dir(browzer_driver))
