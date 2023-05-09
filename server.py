from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Run the stress_cpu.py script in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "CPU stress process started", 200

@app.route('/', methods=['GET'])
def get_ip():
    # Get the private IP address of the current machine
    hostname = socket.gethostname()    
    ip_address = socket.gethostbyname(hostname)
    return ip_address, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
