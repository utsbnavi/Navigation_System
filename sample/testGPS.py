# -*- coding: utf-8 -*-
#
# Solar-boat Project 2019
# created on: 2019/07/25
# Author: XU GUANGLEI
#
#----------------------

from serial import Serial
from micropyGPS import MicropyGPS
import threading
import time

gps = MicropyGPS(9, 'dd')                          #generate MicropyGPS object
def rungps():                                      #read from GPS module and refresh gps object
    s = Serial('/dev/serial0', 9600, timeout=10)
    s.readline()
    while True:
        sentence = s.readline().decode('utf-8')    #read GPS data and transform it into string
        if sentence[0] != '$':                     #ignore it if the first character isn't '$'
            continue
        for x in sentence:
            gps.update(x)
        
gpsthread = threading.Thread(target=rungps, args=()) #run the parameter and generate thread
gpsthread.daemon = True
gpsthread.start()                                  #start thread

while True:
    if gps.clean_sentences > 20:
        h = gps.timestamp[0] if gps.timestamp[0] < 24 else gps.timestamp[0] - 24
        print('%2d:%02d:%04.1f' % (h, gps.timestamp[1], gps.timestamp[2]))
        print('latitude: %2.4f, longitude: %2.4f' % (gps.latitude[0], gps.longitude[0]))
        print('altitude: %f' % gps.altitude)
        print('')
    time.sleep(2.0)                                #output the data every 2 seconds
