import datetime

def write_log(log_file, result, network_info):
    try:
        with open(log_file, 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{timestamp}\n")
            file.write("Network Information:\n")
            file.write(f"  Hostname:  {network_info.get('hostname', 'N/A')}\n")
            file.write(f"  Global IP: {network_info.get('global_ip', 'N/A')}\n")
            file.write(f"  Provider:  {network_info.get('provider', 'N/A')}\n")
            file.write("Speed Test Results:\n")
            file.write(result)
            file.write("--------------------\n")
    except IOError as e:
        print(f"Error writing to log file: {str(e)}")