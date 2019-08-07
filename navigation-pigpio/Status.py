#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Status.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#

from State import State
from Params import Params
from Waypoint import Waypoint
from GpsData import GpsData

import math

class Status:
    def __init__(self, params):
        self.params = params
        self.waypoint = Waypoint()
        self.mode = 'TEST'
        self.speed = 0.0
        self.boat_direction = 0.0
        self.latitude = 0.0
        self.longitude = 0.0
        self.timestamp_string = ''
        self.target_direction = 0.0
        self.target_distance = 0.0
        self.gps_data = GpsData()

    def readGps(self):
        if self.gps_data.read():
            self.timestamp_string = self.gps_data.timestamp_string
            self.latitude = self.gps_data.latitude
            self.longitude = self.gps_data.longitude
            self.speed = self.gps_data.speed[2] #kph
            self.boat_direction = self.gps_data.course
            return True
        else:
            return False

    def isGpsError(self):
        if self.latitude < 0.00001 and self.longitude < 0.00001:
            return True
        else:
            return False

    def calcTargetDistance(self):
        r = 6378.137 #[km] # radius of the Earth
        wp = self.waypoint
        lon1 = math.radians(self.longitude)
        lon2 = math.radians(wp.getPoint()[1])
        lat2 = math.radians(wp.getPoint()[0])
        lat1 = math.radians(self.latitude)
        dlon = lon2 - lon1  
        dlat = lat2 - lat1  
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2 
        c = 2 * math.asin(math.sqrt(a))  
       
        self.target_distance = c * r * 1000 # [m]
        return

    def calcTargetDirection(self):
        wp = self.waypoint
        radLonA = math.radians(self.longitude)
        radLonB = math.radians(wp.getPoint()[1])
        radLatB = math.radians(wp.getPoint()[0])
        radLatA = math.radians(self.latitude)
        dLong = radLonB - radLonA
        y = math.sin(dLong) * math.cos(radLatB) 
        x = math.cos(radLatA) * math.sin(radLatB) - math.sin(radLatA) * math.cos(radLatB) * math.cos(dLong) 
        dir = math.degrees(math.atan2(y, x)) 
        dir = (dir + 360) % 360 
        if dir < 0:
            dir = 360 + dir
        self.target_direction = dir # degrees
        return

    def hasPassedWayPoint(self):
        if self.target_distance < 1.0:
            return True
        else:
            return False

    def updateTarget(self):
        if self.hasPassedWayPoint():
            key = self.waypoint.nextPoint()
            if not key:
                print('AN has finished!')
                self.mode = 'RC'
        return

if __name__ == "__main__":
    params = Params()
    status = Status(params)
