import argparse
from modules.downloader import Downloader
from modules.uploader import Uploader
from modules.result_formatter import format_result
from modules.write_log import write_log
from config import DOWNLOAD_URL, UPLOAD_URL, SIZE

VERSION = '0.1.0'

def parse_arguments():
    parser = argparse.ArgumentParser(description='Measure download and upload speeds and optionally log the results.')
    parser.add_argument('--log', action='store_true', help='Enable logging of speed test results')
    parser.add_argument('--log-file', type=str, default='mbpstester.log', help='Specify the path to the log file (default: mbpstester.log)')
    parser.add_argument('--version', '-v', action='version', version=f'mbpstester version {VERSION}', help='Show the version of the program and exit')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.log:
        write_log(args.log_file, result)

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