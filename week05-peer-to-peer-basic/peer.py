# Step 1: Create a Peer Node (Listener + Sender)
# peer.py
import socket
import threading
import sys
from config import HOST, BASE_PORT, BUFFER_SIZE

peer_id = int(sys.argv[1])
PORT = BASE_PORT + peer_id

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"[PEER {peer_id}] Listening on {PORT}")

    while True:
        conn, addr = sock.accept()
        data = conn.recv(BUFFER_SIZE)
        print(f"[PEER {peer_id}] From {addr}: {data.decode()}")
        conn.close()

def send_message(target_peer_id, message):
    target_port = BASE_PORT + target_peer_id
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, target_port))
        sock.sendall(message.encode())
        print(f"[PEER {peer_id}] Sent to {target_peer_id}: {message}")
        sock.close()
    except ConnectionRefusedError:
        print(f"[PEER {peer_id}] ERROR: Peer {target_peer_id} not online")

threading.Thread(target=listen, daemon=True).start()

while True:
    try:
        target = int(input("Send to peer ID: "))
        msg = input("Message: ")
        send_message(target, msg)
    except ValueError:
        print("[PEER] Invalid ID")
    except KeyboardInterrupt:
        print(f"\n[PEER {peer_id}] Exit")
        break