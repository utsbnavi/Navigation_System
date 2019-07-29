#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Params.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#

class Params:
    def __init__(self):
        # pin assign
        self.pin_gps_in = 0
        self.pin_mode_in = 0
        self.pin_servo_in = 0
        self.pin_servo_out = 12 # GPIO 18
        self.pin_thruster_in = 0
        self.pin_thruster_out = 35 # GPIO 19

if __name__ == "__main__":
    params = Params()