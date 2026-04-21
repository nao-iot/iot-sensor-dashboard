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
* Uvicorn
* SQLite
* Cloudflare Tunnel
* HTML/CSS/JavaScript
* Chart.js

## Install
* pip install -r requirements.txt

## Files（プログラム）
* init_db.py：データを保存するsensor.dbを作成
* server.py : データ受信サーバ
* client.py : 疑似センサ送信
* api_server.py：FastAPIを起動

## Setup（起動方法）
### 1. 仮想環境を作成
```bash
python -m venv myenv
```
### 2. 仮想環境を有効化
#### Linux / Mac
```bash
source myenv/bin/activate
```
#### Windows
```bash
myenv\Scripts\activate
```
### 3. データ受信サーバを起動
```bash
python server.py
```
### 4. センサ送信クライアントを起動
```bash
python client.py
```
### 5. Webダッシュボードを起動
```bash
uvicorn api_server:app --host 0.0.0.0 --port 8000
```
