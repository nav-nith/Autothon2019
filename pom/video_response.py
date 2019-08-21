import logging
import requests
import json
import os

log = logging.getLogger("VIDEORESPONSE")
log.setLevel(logging.DEBUG)


class VideoReponse:
    def __init__(self, url: str="http://54.169.34.162:5252"):
        self.url = url

    def get_video_title(self):
        """This function fetches a video name from the url
        """
        get_url = f"{self.url}/video"
        log.info(f"HTTP GET: {get_url}")
        r = requests.get(get_url)
        log.info(f"GET RESP: {r.status_code}")
        video_title = r.content.decode()
        assert isinstance(video_title, str)
        log.info(f"Fetched Video: {video_title}")
        return video_title

    def upload_up_next(self, videos_up_next: dict):
        """This function uploads a jason file of the argued dictionary to the url
        """
        json_upnext = json.dumps(videos_up_next)
        with open ("results.json", "w") as f:
            log.info(f"Creating Json File")
            f.write(json_upnext)
        files = {'file': ('results.json', open('results.json', 'rb'), 'multipart/form-data')}
        post_url = f"{self.url}/upload"
        log.info(f"HTTP POST: {post_url}")
        r = requests.post(post_url, files=files)
        log.info(f"POST RESP: {r.status_code}")
        hash_key = r.content.decode()
        log.info(f"Hash Key: {hash_key}")
        return hash_key

    def get_result(self, hash_key: str):
        """This function fetches the result using the hash key
        """
        get_url = f"{self.url}/result/{hash_key}"
        log.info(f"HTTP GET: {get_url}")
        r = requests.get(get_url)
        log.info(f"GET RESP: {r.status_code}")
        response = r.content.decode()
        log.info(f"Result Response: {response}")
        return response
