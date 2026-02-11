import socket
from config import HOST, PORT, BUFFER_SIZE

if __name__ == "__main__":
    try:
        # สร้าง socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        print("[CLIENT] Connected to server")

        # ใส่ messages ตรงนี้
        messages = [
            "Hello",
            "How are you?",
            "Goodbye"
        ]

        # วนลูปส่งข้อความ
        for message in messages:
            print(f"[CLIENT] Sending: {message}")
            client_socket.sendall(message.encode())

            response = client_socket.recv(BUFFER_SIZE)
            print(f"[CLIENT] Received: {response.decode()}")

    except Exception as e:
        print(f"[CLIENT] Error: {e}")

    finally:
        client_socket.close()
        print("[CLIENT] Closed connection")
