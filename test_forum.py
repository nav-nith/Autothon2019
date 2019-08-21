from pom.forum import Forum
from pom.video_response import VideoReponse
import logging


log = logging.getLogger("TEST")
log.setLevel(logging.DEBUG)


class TestForum:
    def test_one(self):
        f = Forum()
        video_response = VideoReponse()

        f.goto_youtube()
        f.goto_channel("step-in forum")
        f.goto_video_tab()

        video_title = video_response.get_video_title()

        f.search_for(video_title)
        f.scroll_to_view(video_title)

        # driver.get_screenshot_as_file("screenshot.png")

        f.play_video()

        f.change_video_quality()
        videos_up_next = f.get_up_next()

        video_response.upload_up_next(videos_up_next)
