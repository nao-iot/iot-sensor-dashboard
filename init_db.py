"""
SQLite データベース初期化スクリプト
sensor.db を作成し、sensor_data テーブルを生成する
"""

import sqlite3
from pathlib import Path

# -----------------------------
# 設定
# -----------------------------
DB_FILE = Path("sensor.db")


# -----------------------------
# DB作成処理
# -----------------------------
def initialize_database():
    """
    SQLiteデータベースとテーブルを作成する
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


# -----------------------------
# 実行
# -----------------------------
if __name__ == "__main__":
    initialize_database()