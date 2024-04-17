import argparse
import json
from colorama import Fore
from modules.downloader import Downloader
from modules.uploader import Uploader
from modules.result_formatter import format_result
from modules.write_log import write_log
from modules.network_info import get_network_info
from modules.result_formatter import format_result_json
from config import DOWNLOAD_URL, UPLOAD_URL

SIZE_1MB = 1 * 1024 * 1024
SIZE_10MB = 10 * 1024 * 1024
SIZE_100MB = 100 * 1024 * 1024
VERSION = '0.1.0'

def parse_arguments():
    parser = argparse.ArgumentParser(description='Measure download and upload speeds and optionally log the results.')
    parser.add_argument('--log', action='store_true', help='Enable logging of speed test results')
    parser.add_argument('--log-file', type=str, default='mbpstester.log', help='Specify the path to the log file (default: mbpstester.log)')
    parser.add_argument('--version', '-v', action='version', version=f'version {VERSION}', help='Show the version of the program and exit')
    parser.add_argument('--no-download', action='store_true', help='Skip the download test and only perform the upload test')
    parser.add_argument('--no-upload', action='store_true', help='Skip the upload test and only perform the download test')
    parser.add_argument('--network-info', action='store_true', help='Display network information')
    parser.add_argument('--json', type=str, help='Output the results in JSON format to the specified file')
    parser.add_argument('--size', type=int, choices=[1, 10, 100], default=1, help='Specify the size of the data to use for testing (1 MB, 10 MB, or 100 MB)')
    return parser.parse_args()

def main():
    args = parse_arguments()
    data_size = {
        1: SIZE_1MB,
        10: SIZE_10MB,
        100: SIZE_100MB
    }[args.size]
    
    if args.no_download and args.no_upload:
        print("Error: Cannot skip both download and upload tests.")
        return

    network_info = {}
    if args.network_info:
        network_info = get_network_info()
        if 'error' in network_info:
            if args.json:
                error_result = json.dumps({'error': network_info['error']}, indent=2)
                try:
                    with open(args.json, 'w') as json_file:
                        json_file.write(error_result)
                    print(f"JSON error output saved to {args.json}")
                except IOError as e:
                    print(f"Error writing JSON file: {str(e)}")
            else:
                print(f"Error getting network information: {network_info['error']}")
            return

    try:
        if not args.no_download:
            if not args.json:
                print("Download Test:")
            downloader = Downloader(DOWNLOAD_URL, data_size, bar_style={'color': Fore.BLUE})
            download_speed = downloader.measure_speed()
        else:
            download_speed = None
            
        if not args.no_upload:
            if not args.json:
                print("Upload Test:")
            uploader = Uploader(UPLOAD_URL, data_size, bar_style={'color': Fore.GREEN})
            upload_speed = uploader.measure_speed()
        else:
            upload_speed = None
            
        if args.json:
            result = format_result_json(download_speed, upload_speed, network_info if args.network_info else None)
            try:
                with open(args.json, 'w') as json_file:
                    json_file.write(result)
                print(f"JSON output saved to {args.json}")
            except IOError as e:
                print(f"Error writing JSON file: {str(e)}")
        else:
            if args.network_info:
                print("Network Information:")
                print(f"  Hostname:  {network_info.get('hostname', 'N/A')}")
                print(f"  Global IP: {network_info.get('global_ip', 'N/A')}")
                print(f"  Provider:  {network_info.get('provider', 'N/A')}")
                print("-" * 40)

            print("Speed Test Results:")
            print("-" * 40)
            result = format_result(download_speed, upload_speed)
            print(result)
        
        if args.log:
            write_log(args.log_file, result, network_info if args.network_info else None)
        
    except Exception as e:
        if args.json:
            error_result = json.dumps({'error': str(e)}, indent=2)
            try:
                with open(args.json, 'w') as json_file:
                    json_file.write(error_result)
                print(f"JSON error output saved to {args.json}")
            except IOError as e:
                print(f"Error writing JSON file: {str(e)}")
        else:
            print(f"An error occurred: {str(e)}")
                
if __name__ == "__main__":
    main()