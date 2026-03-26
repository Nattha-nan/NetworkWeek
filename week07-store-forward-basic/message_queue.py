# Step 1: Implement a Message Queue
# message_queue.py
import time
from collections import deque

class MessageQueue:
    def __init__(self):
        self.queue = deque()

    def add_message(self, message, peer_port):
        entry = {
            "message": message,
            "peer": peer_port,
            "timestamp": time.time(),
            "attempts": 0
        }
        self.queue.append(entry)

    def get_messages(self):
        return list(self.queue)

    def remove_message(self, msg):
        self.queue.remove(msg)

    def inc_attempts(self, msg):
        msg["attempts"] += 1

    def size(self):
        return len(self.queue)
