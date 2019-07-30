#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GpsData.py
#
# Solar-boat Project 2019
#   created on: 2019/07/29
#   Author: Xu Guanglei
#

from serial import Serial
from micropyGPS import MicropyGPS
import threading
import time

class GpsData:
    def __init__(self):
        self.timestamp = [0, 0, 0.0]
        self.timestamp_string = ''
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        self.speed = []
        self.course = 0.0
        self.satellites_used = []
        self.satellite_data = {}
        self.gps = MicropyGPS(9, 'dd')
        self.gpsthread = threading.Thread(target=self.runGps, args=())
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
        if self.gps.clean_sentences > 20:
            h = self.gps.timestamp[0] if self.gps.timestamp[0] < 24 else self.gps.timestamp[0] -24
            self.timestamp[0] = h
            self.timestamp[1] = self.gps.timestamp[1]
            self.timestamp[2] = self.gps.timestamp[2]
            t = self.timestamp
            self.timestamp_string = '%2d:%02d:%04.1f' % (t[0], t[1], t[2])
            self.latitude = self.gps.latitude[0]
            self.longitude = self.gps.longitude[0]
            self.altitude = self.gps.altitude
            self.course = self.gps.course
            self.speed = self.gps.speed
            self.satellites_used = self.gps.satellites_used
            self.satellite_data = self.gps.satellite_data
            return True
        else:
            return False

    def print(self):
        t = self.timestamp
        lat = self.latitude
        lon = self.longitude
        alt = self.altitude
        print('%2d:%02d:%04.1f' % (t[0], t[1], t[2]))
        print('latitude: %2.4f, longitude: %2.4f' % (lat, lon))
        print('altitude: %f' % (alt))
        print('course: %f' % (self.course))
        print('speed:', self.speed)
        print('Satellites Used: ', self.satellites_used)
        for k, v in self.satellite_data.items():
            print('%d: %s' % (k, v))
        print('')
        return

if __name__ == "__main__":
    gpsData = GpsData()
    while True:
        time.sleep(3.0)
        if gpsData.read():
            gpsData.print()
    