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
        self.pin_mode_in      =  7 # GPIO  4
        self.pin_servo_in     =  3 # GPIO  2
        self.pin_thruster_in  =  5 # GPIO  3
        self.pin_servo_out    = 12 # GPIO 18
        self.pin_thruster_out = 33 # GPIO 13

if __name__ == "__main__":
    params = Params()