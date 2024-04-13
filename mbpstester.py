import argparse
from modules.downloader import Downloader
from modules.uploader import Uploader
from modules.result_formatter import format_result
from modules.write_log import write_log
from modules.network_info import get_network_info
from config import DOWNLOAD_URL, UPLOAD_URL, SIZE

VERSION = '0.1.0'

def parse_arguments():
    parser = argparse.ArgumentParser(description='Measure download and upload speeds and optionally log the results.')
    parser.add_argument('--log', action='store_true', help='Enable logging of speed test results')
    parser.add_argument('--log-file', type=str, default='mbpstester.log', help='Specify the path to the log file (default: mbpstester.log)')
    parser.add_argument('--version', '-v', action='version', version=f'version {VERSION}', help='Show the version of the program and exit')
    parser.add_argument('--no-download', action='store_true', help='Skip the download test and only perform the upload test')
    parser.add_argument('--no-upload', action='store_true', help='Skip the upload test and only perform the download test')
    parser.add_argument('--network-info', action='store_true', help='Display network information')
    return parser.parse_args()

def main():
    args = parse_arguments()
    
    if args.no_download and args.no_upload:
        print("Error: Cannot skip both download and upload tests.")
        return

    network_info = {}
    if args.network_info:
        network_info = get_network_info()
        if 'error' in network_info:
            print(f"Error getting network information: {network_info['error']}")
        else:
            print("Network Information:")
            print(f"  Hostname:  {network_info.get('hostname', 'N/A')}")
            print(f"  Global IP: {network_info.get('global_ip', 'N/A')}")
            print(f"  Provider:  {network_info.get('provider', 'N/A')}")
            print("-" * 40)

    print("Speed Test Results:")
    try:
        if not args.no_download:
            print("Download Test:")
            downloader = Downloader(DOWNLOAD_URL, SIZE)
            download_speed = downloader.measure_speed()
        else:
            download_speed = None
            
        if not args.no_upload:
            print("Upload Test:")
            uploader = Uploader(UPLOAD_URL, SIZE)
            upload_speed = uploader.measure_speed()
        else:
            upload_speed = None
            
        result = format_result(download_speed, upload_speed)
        print(result)
        
        if args.log:
            write_log(args.log_file, result, network_info)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
if __name__ == "__main__":
    main()