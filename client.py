import socket
import time
import random
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        data = {
            "temperature": random.randint(20, 35),
            "humidity": random.randint(30, 70),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        s.send(json.dumps(data).encode())

        response = s.recv(1024)
        print("サーバ応答:", response.decode())

        s.close()

        time.sleep(1)

    except Exception as e:
        print("エラー:", e)
        time.sleep(3)