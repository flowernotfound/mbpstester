import requests
import time
from modules.progress_bar import ProgressBar
from colorama import Fore

class Uploader:
    def __init__(self, url, size, timeout=60, chunk_size=1024, bar_style=None):
        self.url = url
        self.size = size
        self.timeout = timeout
        self.chunk_size = chunk_size
        self.bar_style = bar_style or {'color': Fore.GREEN, 'filled': '█', 'empty': '-'}

    def upload(self):
        start_time = time.time()
        with ProgressBar(self.size, "Uploading", bar_style=self.bar_style) as progress_bar:
            data = b"0" * self.size
            response = requests.post(self.url, data=data, timeout=self.timeout)
            progress_bar.update(self.size)
        end_time = time.time()
        return end_time - start_time

    def measure_speed(self, num_measurements=3):
        total_time = 0
        for _ in range(num_measurements):
            total_time += self.upload()
        average_time = total_time / num_measurements
        speed = self.size / average_time
        return speed