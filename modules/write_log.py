import datetime

def write_log(log_file, result):
    try:
        with open(log_file, 'a') as file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{timestamp}\n")
            file.write(result)
            file.write("--------------------\n")
    except IOError as e:
        print(f"Error writing to log file: {str(e)}")