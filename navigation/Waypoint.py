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
       self.index = 0

    def addPoint(self, latitude, longitude):
        self.latitude.append(latitude)
        self.longitude.append(longitude)