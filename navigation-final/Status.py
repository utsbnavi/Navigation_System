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
        self.waypoint_range = 0.0
        self.gps_data = GpsData()

    def readGps(self):
        if self.gps_data.read():
            # If the boat doesn't move in 1 [m], don't update the direciton
            if self.getDistance(self.longitude, self.latitude, self.gps_data.longitude, self.gps_data.latitude) > 1:
                self.boat_direction = self.getDirection(self.longitude, self.latitude, self.gps_data.longitude, self.gps_data.latitude)
            self.timestamp_string = self.gps_data.timestamp_string
            self.latitude = self.gps_data.latitude
            self.longitude = self.gps_data.longitude
            self.speed = self.gps_data.speed[2] #kph
            return True
        else:
            return False

    # Not Use
    def isGpsError(self):
        if self.latitude < 0.000001 and self.longitude < 0.000001:
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
        self.target_direction = dir # degrees
        return

    def getDirection(self, LonA, LatA, LonB, LatB):
        radLonA = math.radians(LonA)
        radLatA = math.radians(LatA)
        radLonB = math.radians(LonB)
        radLatB = math.radians(LatB)
        dLong = radLonB - radLonA
        y = math.sin(dLong) * math.cos(radLatB) 
        x = math.cos(radLatA) * math.sin(radLatB) - math.sin(radLatA) * math.cos(radLatB) * math.cos(dLong) 
        dir = math.degrees(math.atan2(y, x)) 
        dir = (dir + 360) % 360 
        return dir

    def getDistance(self, LonA, LatA, LonB, LatB):
        r = 6378.137 #[km] # radius of the Earth
        radLonA = math.radians(LonA)
        radLatA = math.radians(LatA)
        radLonB = math.radians(LonB)
        radLatB = math.radians(LatB)
        dlon = radLonB - radLonA
        dlat = radLatB - radLonA
        a = math.sin(dlat/2)**2 + math.cos(radLatA) * math.cos(radLatB) * math.sin(dlon/2)**2 
        c = 2 * math.asin(math.sqrt(a))
        return c * r * 1000

    def hasPassedWayPoint(self):
        if self.target_distance < self.waypoint_range:
            return True
        else:
            return False

    def updateTarget(self):
        if self.hasPassedWayPoint():
            # If the boat has passed all waypoints, key is false
            # If not, key is true
            key = self.waypoint.nextPoint()
            if not key:
                print('AN has finished!')
                self.mode = 'AN_END'
        return

if __name__ == "__main__":
    params = Params()
    status = Status(params)
