# iot-sensor-dashboard
Python + FastAPI + SQLite によるIoT監視システムです。
センサデータを取得し、グラフ表示・外部公開しています。
## Overview（概要）
環境センサ  
   ↓  
client.py（取得・送信）  
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
<img width="1892" height="935" alt="dashboard" src="https://github.com/user-attachments/assets/97231bf9-9e99-46bc-ac68-c6dc83b490c7" />

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
