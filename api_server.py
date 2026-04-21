from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sqlite3
from pathlib import Path

# -----------------------------------
# FastAPI アプリ設定
# -----------------------------------
app = FastAPI(
    title="IoT Sensor Dashboard",
    description="Temperature and humidity monitoring dashboard using FastAPI + SQLite + Chart.js",
    version="1.0.0"
)

# データベースファイル
DB_FILE = Path("sensor.db")


# -----------------------------------
# データ取得関数
# -----------------------------------
def get_sensor_data(limit: int = 20):
    """
    SQLiteから最新データを取得する
    """
    if not DB_FILE.exists():
        return []

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT temperature, humidity, timestamp
        FROM sensor_data
        ORDER BY timestamp DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()
    conn.close()

    # 古い順に並べ替え
    rows.reverse()

    return [
        {
            "temperature": row[0],
            "humidity": row[1],
            "time": row[2]
        }
        for row in rows
    ]


# -----------------------------------
# API
# -----------------------------------
@app.get("/data")
def read_data():
    """
    センサーデータ取得API
    """
    return get_sensor_data()


# -----------------------------------
# ダッシュボード画面
# -----------------------------------
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
<!DOCTYPE html>
<html lang="ja">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Sensor Dashboard</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    text-align: center;
    margin: 0;
    padding: 30px;
}

.container {
    max-width: 900px;
    margin: auto;
}

h1 {
    color: #333;
}

canvas {
    background: #ffffff;
    border-radius: 12px;
    padding: 15px;
    margin-top: 20px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.alert {
    color: red;
    font-weight: bold;
    margin-top: 15px;
    font-size: 18px;
}

.status {
    margin-top: 10px;
    color: #666;
    font-size: 14px;
}
</style>

</head>

<body>

<div class="container">
    <h1>🌡 Sensor Dashboard</h1>

    <canvas id="chart" height="120"></canvas>

    <div id="alert" class="alert"></div>
    <div id="status" class="status">Loading...</div>
</div>

<script>

let chart = null;

// ----------------------------
// グラフ更新
// ----------------------------
function updateChart() {

    fetch('/data')
    .then(response => response.json())
    .then(data => {

        if (data.length === 0) {
            document.getElementById('status').innerText =
                "No sensor data found.";
            return;
        }

        const labels = data.map(item => item.time);
        const temp = data.map(item => item.temperature);
        const hum  = data.map(item => item.humidity);

        const latestTemp = temp[temp.length - 1];

        // 異常検知
        if (latestTemp >= 30) {
            document.getElementById('alert').innerText =
                "⚠ High Temperature Alert!";
        } else {
            document.getElementById('alert').innerText = "";
        }

        // 再生成
        if (chart) {
            chart.destroy();
        }

        const ctx = document.getElementById('chart').getContext('2d');

        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Temperature (°C)',
                        data: temp,
                        tension: 0.3
                    },
                    {
                        label: 'Humidity (%)',
                        data: hum,
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true
            }
        });

        document.getElementById('status').innerText =
            "Last Updated: " + new Date().toLocaleTimeString();
    })
    .catch(error => {
        document.getElementById('status').innerText =
            "Failed to load data.";
        console.error(error);
    });
}

// 初回実行
updateChart();

// 5秒ごと更新
setInterval(updateChart, 5000);

</script>

</body>
</html>
"""