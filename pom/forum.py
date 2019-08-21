import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


log = logging.getLogger("FORUM")
log.setLevel(logging.DEBUG)
delay = 10


class Forum:
    def __init__(self, driver):
        self.driver = driver
        self.video_title_elem = ""

    def goto_youtube(self):
        log.debug(f"Going to open YouTube")
        self.driver.get("https://www.youtube.com")
        pass

    def goto_channel(self, channel_name):
        log.debug(f"navigate to youtube channel page")
        search_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.NAME, 'search_query')))
        search_elem.send_keys(channel_name)
        self.driver.find_element_by_id("search-icon-legacy").click()
        channel_elem = WebDriverWait(self.chrome_driver, delay).until(ec.presence_of_element_located((By.ID, 'channel-title')))
        channel_elem.click()
        pass

    def goto_video_tab(self):
        videos_tab_elem = WebDriverWait(self.chrome_driver, delay).until(ec.presence_of_element_located((By.XPATH, "//div[@id='tabsContent']/paper-tab[2]/div")))
        videos_tab_elem.click()
        pass

    def search_for(self, video_title):
        pass

    def scroll_to_view(self, video_title):
        self.video_title_elem = WebDriverWait(self.chrome_driver, delay).until(ec.presence_of_element_located((By.XPATH, "//a[text()='"+video_title+"']")))
        ActionChains(self.driver).move_to_element(self.video_title_elem).perform()
        pass

    def play_video(self):
        self.video_title_elem.click()
        WebDriverWait(self.chrome_driver, delay).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#info-contents .title')))
        pass

    def change_video_quality(self):
        pass

    def get_up_next(self):
        """Return a dict of next videos"""
        pass
