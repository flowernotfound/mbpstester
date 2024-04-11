import sys

class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.progress = 0

    def update(self, progress):
        self.progress += progress
        percent = self.progress / self.total * 100
        sys.stdout.write(f"\rProgress: [{int(percent)}%]")
        sys.stdout.flush()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write("\n")
        sys.stdout.flush()