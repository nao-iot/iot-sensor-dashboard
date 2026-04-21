# iot-sensor-dashboard
## Overview（概要）
Pythonで作成したIoTセンサ監視システムです。
クライアントから温湿度データを送信し、サーバで受信してSQLiteへ保存します。
Web画面でデータ確認も可能です。

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
* server.py : データ受信サーバ
* client.py : 疑似センサ送信

## How to Run（起動方法）
```bash id="e7u0ya"
python server.py
python client.py
uvicorn dashboard:app --reload
```
