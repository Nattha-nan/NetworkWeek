#  Step 2: Node Detects Link Availability and Stores Messages
# node.py
import socket
import threading
import time
from config import HOST, BASE_PORT, PEER_PORTS, BUFFER_SIZE, RETRY_INTERVAL
from message_queue import MessageQueue

queue = MessageQueue()

# =============================
# SEND MESSAGE
# =============================
def send_message(peer_port, message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((HOST, peer_port))
        s.sendall(message.encode())
        s.close()
        return True
    except:
        return False

# =============================
# RETRY LOOP
# =============================
def retry_loop():
    while True:
        time.sleep(RETRY_INTERVAL)

        for msg_entry in queue.get_messages():
            peer = msg_entry["peer"]
            message = msg_entry["message"]

            print(f"[NODE {BASE_PORT}] Retrying to {peer}... (attempt {msg_entry['attempts'] + 1})")

            if send_message(peer, message):
                print(f"[NODE {BASE_PORT}] Sent stored message to {peer}")
                queue.remove_message(msg_entry)
            else:
                queue.inc_attempts(msg_entry)

# =============================
# SERVER
# =============================
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, BASE_PORT))
    server.listen()

    print(f"[NODE {BASE_PORT}] Listening for messages...")

    while True:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE).decode()
        print(f"[NODE {BASE_PORT}] Received: {data} from {addr}")
        conn.close()

# =============================
# MAIN
# =============================
if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    threading.Thread(target=retry_loop, daemon=True).start()

    for peer in PEER_PORTS:
        msg = f"Hello from node {BASE_PORT}"

        if send_message(peer, msg):
            print(f"[NODE {BASE_PORT}] Sent to {peer}")
        else:
            print(f"[NODE {BASE_PORT}] Peer {peer} unavailable, storing message")
            queue.add_message(msg, peer)

    print(f"[NODE {BASE_PORT}] Queue size: {queue.size()}")

    while True:
        time.sleep(1)
