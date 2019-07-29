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
import time

class GpsData:
    def __init__(self):
        self.timestamp = [0, 0, 0.0]
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
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

    def read(self):
        if gps.clean_sentence > 20:
            h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] -24
            self.timestamp[0] = self.gps.timestamp[0]
            self.timestamp[1] = self.gps.timestamp[1]
            self.timestamp[2] = self.gps.timestamp[2]
            self.latitude = self.gps.latitude[0]
            self.longitude = self.gps.longitude[0]
            self.altitude = self.gps.altitude

    def print(self):
        t = self.timestamp
        lat = self.latitude
        lon = self.longitutde
        alt = self.altitude
        print('%2d:%02d:%04.1f' % (t[0], t[1], t[2]))
        print('latitude: %2.4f, longitude: %2.4f' % (lat, lon))
        print('altitude: %f' % gps.altitude)
        print('')

if __name__ == "__main__":
    gpsData = GpsData()
    while True:
        time.sleep(2.0)
        self.read()
        self.print()
    