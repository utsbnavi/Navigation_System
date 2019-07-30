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
        self.__num++
        return

    def getPoint(self):
        latitude = self.latitude[self.index]
        longitude = self.longitude[self.index]
        return [latitude, longitude]

    def nextPoint(self):
        self.__index++
        if self.__index == self.__num:
            return False
        else:
            return True

if __name__ == "__main__":
    print('waypoint')
