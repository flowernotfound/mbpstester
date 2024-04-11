import urllib.request
import time
from speedtest.progress_bar import ProgressBar

class Downloader:
    def __init__(self, url, size):
        self.url = url
        self.size = size

    def download(self):
        start_time = time.time()
        with ProgressBar(self.size) as progress_bar:
            with urllib.request.urlopen(self.url) as response:
                chunk_size = 1024
                downloaded_size = 0
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    downloaded_size += len(chunk)
                    progress_bar.update(len(chunk))
        end_time = time.time()
        return end_time - start_time

    def measure_speed(self, num_measurements=3):
        total_time = 0
        for _ in range(num_measurements):
            total_time += self.download()
        average_time = total_time / num_measurements
        speed = self.size / average_time
        return speed