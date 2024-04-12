import sys
import time

class ProgressBar:
    def __init__(self, total, process_name, bar_width=50, update_interval=0.1):
        self.total = total
        self.process_name = process_name
        self.bar_width = bar_width
        self.update_interval = update_interval
        self.progress = 0
        self.last_update_time = time.time()

    def update(self, progress):
        self.progress += progress
        current_time = time.time()
        if current_time - self.last_update_time >= self.update_interval:
            self.display_progress()
            self.last_update_time = current_time

    def display_progress(self):
        percent = self.progress / self.total
        filled_width = int(self.bar_width * percent)
        bar = '█' * filled_width + '-' * (self.bar_width - filled_width)
        sys.stdout.write(f"\r{self.process_name}: [{bar}] {percent:.1%}")
        sys.stdout.flush()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.display_progress()
        sys.stdout.write("\n\n")
        sys.stdout.flush()