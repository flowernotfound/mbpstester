from modules.downloader import Downloader
from modules.uploader import Uploader
from modules.result_formatter import format_result
from config import DOWNLOAD_URL, UPLOAD_URL, SIZE

def main():
    try:
        downloader = Downloader(DOWNLOAD_URL, SIZE)
        download_speed = downloader.measure_speed()
        uploader = Uploader(UPLOAD_URL, SIZE)
        upload_speed = uploader.measure_speed()
        result = format_result(download_speed, upload_speed)
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
