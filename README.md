# iot-sensor-dashboard
クライアントから温湿度データを送信し、サーバで受信してSQLiteへ保存、Webブラウザ上でリアルタイム可視化する IoT ダッシュボードです。外部ネットワークからも安全にアクセスできるよう、Cloudflare Tunnel を利用して公開しています。
## Overview（概要）
環境センサ
↓
client.py（センサ取得・送信）
↓ Socket通信 
server.py（受信・DB保存）
↓ SQLite 
FastAPI（APIサーバ） 
↓ 
Chart.js（Webダッシュボード） 
↓ 
Cloudflare Tunnel（外部公開）

## Features（機能）
* Socket通信
* JSONデータ送受信
* SQLite保存
* Webダッシュボード
* グラフ表示
* 警告アラート
* 自動更新
* Cloudflare Tunnel外部公開

## Tech Stack（使用技術）
* Python
* FastAPI
* SQLite
* Cloudflare Tunnel
* HTML/CSS/JavaScript
* Chart.js

## Files
* init_db.py：データを保存するsensor.dbを作成
* server.py : データ受信サーバ
* client.py : 疑似センサ送信
* api_server.py：FastAPIを起動

## How to Run（起動方法）
```bash id="e7u0ya"
python init_db.py
python server.py
python client.py
uvicorn api_server:app --reload
```
