import argparse
import datetime
from modules.downloader import Downloader
from modules.uploader import Uploader
from modules.result_formatter import format_result
from config import DOWNLOAD_URL, UPLOAD_URL, SIZE

def parse_arguments():
    parser = argparse.ArgumentParser(description='Measure download and upload speeds.')
    parser.add_argument('--log', action='store_true', help='Enable logging')
    parser.add_argument('--log-file', type=str, default='mbpstester.log', help='Log file path')
    return parser.parse_args()

def write_log(log_file, result):
    try:
        with open(log_file, 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{timestamp}\n")
            file.write(result)
            file.write("--------------------\n")
    except IOError as e:
        print(f"Error writing to log file: {str(e)}")

def main():
    args = parse_arguments()
    try:
        downloader = Downloader(DOWNLOAD_URL, SIZE)
        download_speed = downloader.measure_speed()
        uploader = Uploader(UPLOAD_URL, SIZE)
        upload_speed = uploader.measure_speed()
        result = format_result(download_speed, upload_speed)
        print(result)
        
        if args.log:
            write_log(args.log_file, result)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
