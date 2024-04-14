import sys
import time
from colorama import Fore, Style

class ProgressBar:
    def __init__(self, total, process_name, bar_width=50, update_interval=0.1, bar_style=None):
        self.total = total
        self.process_name = process_name
        self.bar_width = bar_width
        self.update_interval = update_interval
        self.progress = 0
        self.last_update_time = time.time()
        self.bar_style = bar_style or {'filled': '█', 'empty': '-', 'color': Fore.GREEN}

    def update(self, progress):
        self.progress += progress
        current_time = time.time()
        if current_time - self.last_update_time >= self.update_interval:
            self.display_progress()
            self.last_update_time = current_time

    def display_progress(self):
        percent = self.progress / self.total
        filled_width = int(self.bar_width * percent)
        bar = self.bar_style['color'] + self.bar_style['filled'] * filled_width + Style.RESET_ALL + self.bar_style['empty'] * (self.bar_width - filled_width)
        sys.stdout.write(f"\r{self.process_name}: [{bar}] {percent:.1%}")
        sys.stdout.flush()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.display_progress()
        sys.stdout.write(Style.RESET_ALL + "\n")
        sys.stdout.flush()