# iot-sensor-dashboard
Python + FastAPI + SQLite によるIoT監視システムです。
センサデータを取得し、グラフ表示・外部公開しています。
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

## Live Demo ＆ Screenshot
URL：https://web.naoki-iot.xyz
## Features（機能）
* 温湿度監視
* グラフ表示
* 自動更新
* Cloudflare Tunnel公開
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
