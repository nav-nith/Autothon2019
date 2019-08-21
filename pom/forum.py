import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


log = logging.getLogger("FORUM")
log.setLevel(logging.DEBUG)
delay = 5


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
        channel_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.ID, 'channel-title')))
        channel_elem.click()
        pass

    def goto_video_tab(self):
        videos_tab_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.XPATH, "//div[@id='tabsContent']/paper-tab[2]/div")))
        videos_tab_elem.click()
        pass

    def scroll_to_view(self, video_title):
        print(f"Title: {video_title}")
        assert video_title, "Video title is empty!"
        y = 0
        end = 30
        for index in range(end):
            try:
                self.video_title_elem = WebDriverWait(self.driver, 1).until(ec.presence_of_element_located((By.XPATH, "//a[text()='"+video_title+"']/..")))
            except Exception:
                print("Scrolling..")
                y += 500
                self.driver.execute_script(f"window.scrollTo(0, {y})")
                if index == (end - 1):
                    raise
            else:
                break

        ActionChains(self.driver).move_to_element(self.video_title_elem).perform()

    def play_video(self):
        self.video_title_elem.click()
        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.CSS_SELECTOR, '#info-contents .title')))

    def change_video_quality(self):
        pass

    def get_up_next(self):
        """Return a dict of next videos"""
        video_list = self.driver.find_elements_by_id("video-title")
        for video in video_list:
            print(video.text)
