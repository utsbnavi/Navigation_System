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

class Status:
    def __init__(self, params):
        self.params = params
        self.waypoint = Waypoint()
        self.mode = 'TEST'
        self.speed = 0.0
        self.boat_direction = 0.0
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0
        self.time_stamp = 0
        self.target_direction = 0.0
        self.gps_data = GpsData()

    def readGps(self):
        self.gps_data.read()
        self.timestamp = self.gps_data.timestamp
        self.latitude = self.gps_data.latitude
        self.longitude = self.gps_data.longitude
        self.altitude = self.gps_data.altitude

    # Implement these functions below
    #def calcBoatDirection(self):
    #def calcTargetDirection(self):
        #self.target_direction =


if __name__ == "__main__":
    params = Params()
    status = Status(params)
