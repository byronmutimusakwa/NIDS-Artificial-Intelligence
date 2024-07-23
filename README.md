# NIDS-Artificial-Intelligence
A simple Network Intrusion Detection System Built using Python making use of ChatGPT API to interpret traffic data


This project is a Network Intrusion Detection System (NiDS) designed to identify and interpret suspicious network traffic. The system leverages Python, the OpenAI API, and the Flask web framework to provide real-time analysis and actionable insights for network security.

Key Features

# 1. Network Scanning
   - Utilizes `nmap` to scan network hosts and ports.
   - Provides detailed information on active hosts and their open ports.

# 2. Traffic Detection
   - Detects specific types of malicious traffic such as netcat connections and SQL injection attempts.
   - Offers real-time monitoring and alerts for detected threats.

# 3. Traffic Interpretation with OpenAI
   - Uses OpenAI's GPT-3.5 API to interpret network traffic data.
   - Generates detailed descriptions and recommendations based on the traffic analysis.

# 4. Web Interface
   - Built with Flask to provide an easy-to-use web interface.
   - Allows users to initiate network scans, submit traffic data for interpretation, and view results.

# Installation

To set up the project locally, follow these steps:

# 1. Clone the repository
   ```bash
   git clone https://github.com/byronmutimusakwa/NIDS-Artificial-Intelligence2024.git
   cd NIDS-Artificial-Intelligence2024
   ```

# 2. Set up a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

# 3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

# 4. Set environment variables
   Create a `.env` file and add necessary environment variables, including your `OPENAI_API_KEY`:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

# 5. Run the application
   ```bash
   flask run
   ```

Usage

# 1. Network Scanning
   - Access the web interface and initiate a network scan to gather information about active hosts and open ports.

# 2. Traffic Interpretation
   - Submit network traffic data through the web interface for interpretation.
   - The system will analyze the data, detect potential threats, and provide detailed descriptions and recommendations.

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

![Python](https://img.shields.io/badge/language-Python-blue.svg)


