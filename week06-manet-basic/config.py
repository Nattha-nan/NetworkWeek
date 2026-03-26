#Step 0: Shared Configuration
# config.py
import sys

HOST = "127.0.0.1"

BUFFER_SIZE = 1024
FORWARD_PROBABILITY = 0.5
TTL = 3

# รับ PORT จาก command line
BASE_PORT = int(sys.argv[1])

# กำหนด neighbors ตาม port
if BASE_PORT == 7000:
    NEIGHBORS = [7001]
elif BASE_PORT == 7001:
    NEIGHBORS = [7000, 7002]
elif BASE_PORT == 7002:
    NEIGHBORS = [7001]
else:
    NEIGHBORS = []
