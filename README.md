# iot-sensor-dashboard
## Overview（概要）
Raspberry Piから取得したセンサデータをWebで可視化するシステムです。

## Features（機能）
* 温湿度表示
* グラフ表示
* 自動更新
* 異常値アラート

## Tech Stack（使用技術）
* Python
* FastAPI
* SQLite
* Cloudflare Tunnel

## How to Run（起動方法）
```bash id="e7u0ya"
python server.py
python client.py
uvicorn dashboard:app --reload
```
