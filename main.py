import json
import re

import serial

from switchbot_py3 import *


def main():
    #  COMポートを開く
    print("Open Port")
    ser = serial.Serial("/dev/ttyUSB0", 115200)

    # 設定ファイル読み込み
    with open("./config.json", "r") as f:
        config = json.load(f)
    print(config)

    # Switchbot初期化
    driver = Driver(device=config["bt_addr"], bt_interface=config["bt_interface"],
                    timeout_secs=config["timeout_secs"])

    switch_flag = False
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            data = float(data)
            print(data)
            if (data >= 30) and (not switch_flag):
                switch_flag = True
                driver.run_command(config["command"])
            elif data < 30:
                switch_flag = False
        except KeyboardInterrupt:
            break

    print("Close Port")
    ser.close()


if __name__ == "__main__":
    main()
