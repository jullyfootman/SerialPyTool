#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Refer to https://tanudon.work/499/
from serial.tools import list_ports
import serial
import time

USB_PORT = None
devices = [info.device for info in list_ports.comports()]
for dev in devices:
    if '/dev/cu.usbserial-' in dev:
        USB_PORT = dev
        print(dev)

BAUDRATAE = 9600
TIMEOUT = 1
if USB_PORT is not None:
    ser = serial.Serial(USB_PORT,BAUDRATAE,timeout=TIMEOUT)

    # 送信
    sendByte = input('>')
    ser.write(sendByte.encode())

    # 受信
    while True:
        serialData = ser.readline().decode('utf-8')
        print(serialData,end='')

else:
    print('該当ポートなし',devices)
