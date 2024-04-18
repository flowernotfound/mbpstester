import http.client
import time
from modules.progress_bar import ProgressBar
from urllib.parse import urlparse
from colorama import Fore

class Uploader:
    def __init__(self, url, size, timeout=30, chunk_size=1024, bar_style=None):
        self.url = url
        self.size = size
        self.timeout = timeout
        self.chunk_size = chunk_size
        self.bar_style = bar_style or {'color': Fore.GREEN}

    def upload(self):
        start_time = time.time()
        with ProgressBar(self.size, "Uploading", bar_style=self.bar_style) as progress_bar:
            parsed_url = urlparse(self.url)
            conn = http.client.HTTPSConnection(parsed_url.netloc, timeout=self.timeout)
            conn.putrequest("POST", parsed_url.path)
            conn.putheader("Content-Length", str(self.size))
            conn.endheaders()

            uploaded_size = 0
            while uploaded_size < self.size:
                chunk = b"0" * min(self.chunk_size, self.size - uploaded_size)
                conn.send(chunk)
                uploaded_size += len(chunk)
                progress_bar.update(len(chunk))

            response = conn.getresponse()
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