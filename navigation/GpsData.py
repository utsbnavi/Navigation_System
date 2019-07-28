#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GpsData.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: 
#

from serial import Serial
from micropyGPS import MicropyGPS
import threading

class GpsData:
    def __init__(self):
        self.tmp = 0
        self.gps = MicropyGPS(9, 'dd')
        self.gpsthread = threading.Thread(target=self.rungps, args=())
        self.gpsthread.daemon = True
        self.gpsthread.start()

    def runGps(self):
        s = Serial('/dev/serial0', 9600, timeout=10)
        s.readline()
        while True:
            sentence = s.readline().decode('utf-8')
            if sentence[0] != '$':
                continue
            for x in sentence:
                self.gps.update(x)
        
if __name__ == "__main__":
    print('GPS')