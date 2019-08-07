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
        # pin assign (GPIO)
        self.pin_mode_in      =  4 # GPIO  4 # PIN  7
        self.pin_servo_in     =  2 # GPIO  2 # PIN  3
        self.pin_thruster_in  =  3 # GPIO  3 # PIN  5
        self.pin_servo_out    = 23 # GPIO 23 # PIN 16
        self.pin_thruster_out = 24 # GPIO 24 # PIN 18

if __name__ == "__main__":
    params = Params()