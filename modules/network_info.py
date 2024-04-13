import socket
import requests

def get_network_info():
    network_info = {}

    try:
        hostname = socket.gethostname()
        network_info['hostname'] = hostname

        try:
            ip_info = requests.get('https://ipinfo.io/json').json()
            network_info['global_ip'] = ip_info['ip']
            network_info['provider'] = ip_info['org']
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Error getting IP information: {str(e)}")

    except (socket.error, KeyError) as e:
        network_info['error'] = str(e)

    return network_info