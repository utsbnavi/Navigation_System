#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Waypoint.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#

class Waypoint:
    def __init__(self):
       self.latitude = []
       self.longitude = []
       self.__index = 0
       self.__num = 0

    def addPoint(self, latitude, longitude):
        self.latitude.append(latitude)
        self.longitude.append(longitude)
        self.__num += 1
        return

    def getPoint(self):
        latitude = self.latitude[self.__index]
        longitude = self.longitude[self.__index]
        return [latitude, longitude]

    def getIndex(self):
        return self.__index + 1

    def nextPoint(self):
        # If the boat has passed the final point,
        # this function returns False
        # If not, this function returns True
        if self.__index < self.__num:
            self.__index = self.__index + 1
            return True
        else:
            return False

if __name__ == "__main__":
    print('waypoint')
