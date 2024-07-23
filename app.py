# app.py
from flask import Flask, render_template, jsonify, request, url_for, flash, Response
import nmap
import openai
import logging
import secrets
import os
import requests

# Initialize Flask app
app = Flask(__name__)

# Generate a secret key
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Set OpenAI API key from environment variable
openai.api_key = 'YOUR_SECRET_API_KEY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize nmap scanner
nm = nmap.PortScanner()

# Function to detect netcat connections
def detect_netcat_connections(traffic_data):
    if 'netcat' in traffic_data.lower():
        return True
    return False

# Function to detect SQL injection attacks
def detect_sql_injection(traffic_data):
    if 'sql' in traffic_data.lower() and 'injection' in traffic_data.lower():
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan_network', methods=['GET', 'POST'])
def scan_network():
    try:
        target_ip = '192.168.159.0/24'  # Adjust as needed

        nm.scan(hosts=target_ip, arguments='-p 1-65535')  # Scanning all ports
        hosts_list = []
        
        for host in nm.all_hosts():
            if nm[host].state() == 'up':
                host_info = {'ip': host, 'ports': []}
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        port_info = {
                            'port': port,
                            'state': nm[host][proto][port]['state']
                        }
                        host_info['ports'].append(port_info)
                hosts_list.append(host_info)

        if not hosts_list:
            message = "No active hosts detected in the network range"
        else:
            message = f"Network scan completed successfully. {len(hosts_list)} hosts found:\n" + "\n".join(
                [f"IP: {host['ip']}, Ports: {', '.join([str(port['port']) + '/' + port['state'] for port in host['ports']])}" for host in hosts_list])

        logging.info(message)
        return Response(message, mimetype='text/plain')
    except Exception as e:
        logging.error(f"Error during network scan: {e}")
        return Response("Error during network scan", mimetype='text/plain')

@app.route('/interpret_traffic', methods=['POST'])
def interpret_traffic():
    try:
        traffic_data = request.json.get('traffic', '')
        if not traffic_data:
            return Response("No traffic data provided", mimetype='text/plain')

        is_netcat = detect_netcat_connections(traffic_data)
        is_sql_injection = detect_sql_injection(traffic_data)

        prompt = f"Describe how the traffic is malicious and describe how the subject IPs are unsafe and give recommendations."
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )

        description = response.choices[0].text.strip()

        if is_netcat:
            description += "\nDetected netcat connection."
        if is_sql_injection:
            description += "\nDetected SQL injection attempt."

        logging.info("Traffic interpretation completed successfully.")
        return Response(description, mimetype='text/plain')
    except Exception as e:
        logging.error(f"Error interpreting traffic: {e}")
        return Response(f"Error interpreting traffic: {e}", mimetype='text/plain')

@app.route('/describe_traffic', methods=['POST'])
def describe_traffic():
    try:
        traffic_data = request.json.get('traffic', '')
        if not traffic_data:
            return Response("No traffic data provided", mimetype='text/plain')

        is_netcat = detect_netcat_connections(traffic_data)
        is_sql_injection = detect_sql_injection(traffic_data)

        prompt = f"Describe the traffic and any suspicious activities observed. Include details on the types of connections and IPs involved, and provide recommendations on actions to take. Traffic data:"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=350
        )

        description = response.choices[0].text.strip()

        if is_netcat:
            description += "\nDetected netcat connection."
        if is_sql_injection:
            description += "\nDetected SQL injection attempt."

        logging.info("Traffic description completed successfully.")
        return Response(description, mimetype='text/plain')
    except Exception as e:
        logging.error(f"Error describing traffic: {e}")
        return Response(f"Error describing traffic: {e}", mimetype='text/plain')
    
@app.route('/simulate_traffic', methods=['POST'])
def simulate_traffic():
    try:
        # Replace <your-kali-ip> with the actual IP address of your Kali Linux machine
        kali_ip = '192.168.1.100'  # Example IP address
        url = f'http://192.168.159.130/vulnerable.php?id=1 OR 1=1'

        response = requests.get(url)
        traffic_data = response.text

        is_sql_injection = detect_sql_injection(traffic_data)

        prompt = f"Describe how the traffic is malicious and describe how the subject IPs are unsafe and give recommendations. Traffic data: {traffic_data}"
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )

        description = response.choices[0].text.strip()

        if is_sql_injection:
            description += "\nDetected SQL injection attempt."

        logging.info("Traffic simulation and detection completed successfully.")
        return Response(description, mimetype='text/plain')
    except Exception as e:
        logging.error(f"Error simulating traffic: {e}")
        return Response(f"Error simulating traffic: {e}", mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
