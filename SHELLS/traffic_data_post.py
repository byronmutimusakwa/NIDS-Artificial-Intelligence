import requests

# URL of your Flask application
url = 'http://localhost:5000/interpret_traffic'

# Example traffic data
traffic_data = """
IP: 192.168.1.10, Port: 80, Protocol: HTTP
IP: 192.168.1.11, Port: 23, Protocol: Telnet
IP: 192.168.1.12, Port: 443, Protocol: HTTPS
"""

# Payload for the POST request
payload = {
    'traffic': traffic_data
}

try:
    # Send POST request
    response = requests.post(url, json=payload)

    # Print response
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
