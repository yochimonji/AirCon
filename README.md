# AirCon
## エアコンIoT化計画

## 概要
IoT特論の成果発表で開発したものです。  
温度が上がるとSwithcbotを動かすことができます。  
今回はエアコンの制御に利用しました。

## 使い方
- 講義資料のとおりにESPr Developer・BME280の配線をします。
- 本リポジトリをクローンします。
- 講義資料を参考にarduino/temperature.inoのssid / passward / channelId / writeKey を変更します。
- [参考文献](#参考文献)の上2つを見ながら環境を構築します。（Python3で動作確認しています。）
- スイッチボットのBLE MACを調べます。（https://chasuke.com/switchbot-raspi/）
- example_config.jsonの"YOUR-Switchbot-BLE-MAC"を調べたBLE MACに変更してconfig.jsonというファイル名に変更します。
- `python main.py`を実行すると、BME280の温度変化に応じてSwitchbotが動きます。現在は30℃以上になると動きます。指で熱を与えるといい感じに動かせます。
- Ambientで温度・湿度・気圧のモニタリングができます。

## 参考文献
- [PythonでSwitchbotを動かすためのGitHub](https://github.com/OpenWonderLabs/python-host)
- [Python - Arduinoで通信するためのライブラリのGitHub](https://github.com/pyserial/pyserial)
- [SwitchBot（スイッチボット）をラズパイ経由で遠隔操作する方法](https://chasuke.com/switchbot-raspi/)