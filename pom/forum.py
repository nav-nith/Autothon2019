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
    def __init__(self, driver, is_mobile):
        self.driver = driver
        self.video_title_elem = ""
        self.is_mobile = is_mobile

    def goto_youtube(self):
        log.debug(f"Going to open YouTube")
        self.driver.get("https://www.youtube.com")

    def goto_channel(self, channel_name):
        log.debug(f"navigate to youtube channel page")
        if self.is_mobile:
            self.driver.find_element_by_id("[aria-label=‘Search YouTube’]").click()
            search_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.CSS_SELECTOR, '.searchbox-input')))
            search_elem.send_keys(channel_name)
            self.driver.find_element_by_id("[aria-label=‘Search YouTube’]").click()
            channel_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.XPATH, '//h4[text()="STep-IN Forum"')))
            channel_elem.click()

        else:
            search_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.NAME, 'search_query')))
            search_elem.send_keys(channel_name)
            self.driver.find_element_by_id("search-icon-legacy").click()
            channel_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.ID, 'channel-title')))
            channel_elem.click()

    def goto_video_tab(self):
        video_tab_locator = '//a[text()="Videos"]' if self.is_mobile else "//div[@id='tabsContent']/paper-tab[2]/div"
        videos_tab_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.XPATH, video_tab_locator)))
        videos_tab_elem.click()

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
        youtube_video_title_locator = '.slim-video-metadata-title' if self.is_mobile else '#info-contents .title'
        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.CSS_SELECTOR, youtube_video_title_locator)))

    def sign_in(self):
        quality_value_elem = self.driver.switch_to.active_element
        while "Sign in to like videos" not in quality_value_elem.text:
            quality_value_elem = self.driver.switch_to.active_element
        keyboard.press_and_release('esc')

    def change_video_quality(self, quality_value: str):
        def pause_play():
            player_css = "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button"
            player_elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.CSS_SELECTOR, player_css)))
            player_elem.click()

        def elem_operation_css(css_sel, click=False):
            elem = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.CSS_SELECTOR, css_sel)))
            asd = f"{elem.get_attribute('innerHTML')}"
            if click:
                elem.click()
            else:
                return asd

        self.driver.get("https://www.youtube.com/watch?v=ffUnNaQTfZE")
        self.sign_in()

        pause_play()

        settings_css = "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-button.ytp-settings-button"
        elem_operation_css(settings_css, True)

        quality_css = "#ytp-id-18 > div > div > div:nth-child(5) > div.ytp-menuitem-content"
        elem_operation_css(quality_css, True)

        is_required_quality = False
        for i in range(6):
            keyboard.press_and_release('up')
            time.sleep(0.5)
            quality_value_elem = self.driver.switch_to.active_element
            if quality_value == quality_value_elem.text:
                is_required_quality = True
                break
        if is_required_quality:
            keyboard.press_and_release('enter')
            pause_play()
            time.sleep(2)

        elem_operation_css(settings_css, True)
        return quality_value in elem_operation_css(quality_css)

    def get_up_next(self, video_title):
        """Return a dict of next videos"""
        d = {
            "team": "sony-team",
            "video": video_title,
            "upcoming-videos": []
        }

        up_next_video_elems = '.item .compact-media-item-headline' if self.is_mobile else "#items #video-title"
        video_list = self.driver.find_elements_by_css_selector(up_next_video_elems)
        for video in video_list:
            if video.text:
                d["upcoming-videos"].append(video.text)

        return d
