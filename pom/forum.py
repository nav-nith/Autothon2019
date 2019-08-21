import logging


log = logging.getLogger("FORUM")
log.setLevel(logging.DEBUG)


class Forum:
    def __init__(self, driver):
        self.driver = driver

    def goto_youtube(self):
        log.debug(f"Going to open YouTube")
        pass

    def goto_channel(self, channel_name):
        pass

    def goto_video_tab(self):
        pass

    def search_for(self, video_title):
        pass

    def scroll_to_view(self, video_title):
        pass

    def play_video(self):
        pass

    def change_video_quality(self):
        pass

    def get_up_next(self):
        """Return a dict of next videos"""
        pass
