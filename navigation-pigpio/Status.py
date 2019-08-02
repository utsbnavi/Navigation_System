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
        y1 = math.radians(self.longitude)
        y2 = math.radians(wp.getPoint()[1])
        dx = math.radians(wp.getPoint()[0] - self.latitude)
        d = r * math.acos(
            math.sin(y1) * math.sin(y2) +
            math.cos(y1) * math.cos(y2) * math.cos(dx)
        ) # [km]
        self.target_distance = d * 1000 # [m]
        return

    def calcTargetDirection(self):
        wp = self.waypoint
        y1 = math.radians(self.longitude)
        y2 = math.radians(wp.getPoint()[1])
        dx = math.radians(wp.getPoint()[0] - self.latitude)
        dir = 90 - math.degrees(math.atan2(
            math.cos(y1) * math.tan(y2) - math.sin(y1) * math.cos(dx),
            math.sin(dx) 
        ))
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
