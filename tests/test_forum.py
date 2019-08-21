from pom.forum import Forum
from utils.video_response import VideoReponse
import logging
import threading
import time


log = logging.getLogger("TEST")
log.setLevel(logging.DEBUG)


class TestForum:
    def test_run(self, driver):
        f = Forum(driver, self.is_mobile)
        video_response = VideoReponse()

        f.goto_youtube()
        f.goto_channel("step-in forum")
        f.goto_video_tab()

        video_title = video_response.get_video_title()

        f.scroll_to_view(video_title)

        driver.get_screenshot_as_file(f"screenshot_{time.strftime('%Y%m%d-%H%M%S')}.png")

        f.play_video()

        f.change_video_quality('360p')
        videos_up_next = f.get_up_next(video_title)

        hash_key = video_response.upload_up_next(videos_up_next)
        res = video_response.get_result(hash_key)
        print(f"RESPONSE: {res}")
