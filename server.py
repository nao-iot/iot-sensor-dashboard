import socket
import json
import sqlite3

HOST = "0.0.0.0"
PORT = 5000

conn_db = sqlite3.connect("sensor.db")
cursor = conn_db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    humidity REAL,
    timestamp TEXT
)
""")
conn_db.commit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("サーバ起動...")

try:
    while True:
        conn, addr = s.accept()
        print("接続:", addr)

        data = conn.recv(1024)

        if data:
            sensor_data = json.loads(data.decode())

            cursor.execute(
                "INSERT INTO sensor_data (temperature, humidity, timestamp) VALUES (?, ?, ?)",
                (
                    sensor_data["temperature"],
                    sensor_data["humidity"],
                    sensor_data["time"]
                )
            )
            conn_db.commit()

            conn.send(b"OK")

        conn.close()

except KeyboardInterrupt:
    print("終了します")

finally:
    conn_db.close()
    s.close()