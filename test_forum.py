from pom.forum import Forum
from pom.video_response import VideoReponse
import logging
import threading
import time


log = logging.getLogger("TEST")
log.setLevel(logging.DEBUG)


class TestForum:
    def test_base(self, chrome_driver):
        # mobile_thread = threading.Thread(target=self.run, args=(mobile_driver,))
        browser_thread = threading.Thread(target=self.run, args=(chrome_driver,))

        log.debug(f"Starting mobile test...")
        # mobile_thread.start()
        log.debug(f"Starting chrome test...")
        browser_thread.start()

        log.debug("Joining mobile thread...")
        # mobile_thread.join()
        log.debug("Joining browser thread...")
        browser_thread.join()

    def run(self, driver):
        f = Forum(driver)
        video_response = VideoReponse()

        f.goto_youtube()
        f.goto_channel("step-in forum")
        f.goto_video_tab()

        video_title = video_response.get_video_title()

        f.scroll_to_view(video_title)

        driver.get_screenshot_as_file(f"screenshot_{time.strftime('%Y%m%d-%H%M%S')}.png")

        f.play_video()

        assert f.change_video_quality('360p')
        videos_up_next = f.get_up_next()

        video_response.upload_up_next(videos_up_next)
