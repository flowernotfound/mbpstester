import http.client
import time
from modules.progress_bar import ProgressBar
from urllib.parse import urlparse

class Uploader:
    def __init__(self, url, size):
        self.url = url
        self.size = size

    def upload(self):
        start_time = time.time()
        with ProgressBar(self.size) as progress_bar:
            parsed_url = urlparse(self.url)
            conn = http.client.HTTPSConnection(parsed_url.netloc)
            conn.request("POST", parsed_url.path, b"0" * self.size)
            response = conn.getresponse()
            progress_bar.update(self.size)
            conn.close()
        end_time = time.time()
        return end_time - start_time

    def measure_speed(self, num_measurements=3):
        total_time = 0
        for _ in range(num_measurements):
            total_time += self.upload()
        average_time = total_time / num_measurements
        speed = self.size / average_time
        return speed