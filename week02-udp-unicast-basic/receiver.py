# Step 1: Create UDP Receiver
# receiver.py
import socket
from config import HOST, PORT, BUFFER_SIZE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"[RECEIVER] Listening on {HOST}:{PORT}")

# Step 2: Receive Datagram
received_ids = set()
while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
#    print(f"[RECEIVER] From {addr}: {data.decode()}")
message = data.decode()
msg_id, text = message.split('|', 1)
msg_id, text = message.split('|', 1)
msg_id = int(msg_id)
if msg_id in received_ids:
    print(f"[RECEIVER] Duplicate: {msg_id}")
else:
    received_ids.add(msg_id)
    print(f"[RECEIVER] New: {msg_id} -> {text}")
