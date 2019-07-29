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
from Pid import Pid
#from GpsData import GpsData
#from Pwm import Pwm

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
        self.pid = Pid()
        self.gps_data = GpsData()
        self.mode_pwm = Pwm(
            params.pin_mode_in, 0)
        self.servo_pwm = Pwm(
            params.pin_servo_in, params.pin_servo_out)
        self.thruster_pwm_ = Pwm(
            params.pin_thruster_in, params.pin_thruster_out)

    def outPwm(self):
        self.servo_pwm.out()
        self.thruster_pwm.out()

    def readGps(self):
        self.gps_data.read()
        self.timestamp = self.gps_data.timestamp
        self.latitude = self.gps_data.latitude
        self.longitude = self.gps_data.longitude
        self.altitude = self.gps_data.altitude

    # Implement these functions below
    #def readPwm(self):
    #def calcBoatDirection(self):
    #def calcTargetDirection(self):
        #self.target_direction =


if __name__ == "__main__":
    params = Params()
    status = Status(params)
