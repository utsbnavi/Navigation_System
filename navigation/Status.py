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
from GpsData import GpsData
from Pwm import Pwm

class Status:
    def __init__(self, params):
        self.params_ = params
        self.waypoint_ = Waypoint()
        self.mode_ = 'AN'
        self.speed_ = 0.0
        self.boat_direction_ = 0.0
        self.latitude_ = 0.0
        self.longitude_ = 0.0
        self.time_stamp_ = 0.0
        self.target_direction_ = 0.0
        self.pid_ = Pid()
        self.gps_data_ = GpsData()
        self.mode_pwm_ = Pwm(
            params.pin_mode_in_, 0)
        self.servo_pwm_ = Pwm(
            params.pin_servo_in_, params.pin_servo_out_)
        self.thruster_pwm_ = Pwm(
            params.pin_thruster_in_, params.pin_thruster_out_)

    # Implement these functions below
    #def readPwm(self):
    #def outPwm(self):
    #def calcBoatDirection(self):
    #def readGPS(self):
    #def calcTargetDirection(self):
        #self.target_direction_ =


if __name__ == "__main__":
    params = Params()
    status = Status(params)
