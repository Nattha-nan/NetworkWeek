#Step 0: Shared Configuration
# config.py
import sys

HOST = "127.0.0.1"
BUFFER_SIZE = 1024
RETRY_INTERVAL = 5

BASE_PORT = int(sys.argv[1])

if BASE_PORT == 8000:
    PEER_PORTS = [8001, 8002]
elif BASE_PORT == 8001:
    PEER_PORTS = [8000, 8002]
elif BASE_PORT == 8002:
    PEER_PORTS = [8000, 8001]
else:
    PEER_PORTS = []