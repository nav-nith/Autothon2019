import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import keyboard


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

    def sign_in(self):
        time.sleep(3)
        quality_value_elem = self.driver.switch_to.active_element
        if "Sign in to like videos" in quality_value_elem.text:
            keyboard.press_and_release('esc')

    def change_video_quality(self, quality_value: str):
        settings_xpath = "//*[@id='movie_player']/div[21]/div[2]/div[2]/button[3]"
        settings_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.XPATH, settings_xpath)))
        settings_elem.click()

        quality_xpath = "//*[@id='ytp-id-18']/div/div/div[3]/div[1]"
        quality_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.XPATH, quality_xpath)))
        quality_elem.click()

        is_required_quality = False
        for i in range(6):
            keyboard.press_and_release('up')
            quality_value_elem = self.driver.switch_to.active_element
            if quality_value == quality_value_elem.text:
                is_required_quality = True
                break
        if is_required_quality:
            keyboard.press_and_release('enter')
            return True

    def get_up_next(self, video_title):
        """Return a dict of next videos"""
        d = {
            "team": "sony-team",
            "video": video_title,
            "upcoming-videos": []
        }

        video_list = self.driver.find_elements_by_css_selector("#items #video-title")
        for video in video_list:
            if video.text:
                d["upcoming-videos"].append(video.text)

        return d
