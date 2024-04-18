import urllib.request
import time
from modules.progress_bar import ProgressBar
from colorama import Fore

class Downloader:
    def __init__(self, url, size, timeout=30, chunk_size=1024, bar_style=None):
        self.url = url
        self.size = size
        self.timeout = timeout
        self.chunk_size = chunk_size
        self.bar_style = bar_style or {'color': Fore.BLUE}

    def download(self):
        start_time = time.time()
        with ProgressBar(self.size, "Downloading", bar_style=self.bar_style) as progress_bar:
            with urllib.request.urlopen(self.url, timeout=self.timeout) as response:
                downloaded_size = 0
                while True:
                    chunk = response.read(self.chunk_size)
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