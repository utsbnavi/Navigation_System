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
        self.value = 100
        # pin assign
        self.pin_gps_in_ = 0
        self.pin_mode_in_ = 0
        self.pin_servo_in_ = 0
        self.pin_servo_out_ = 0
        self.pin_thruster_in_ = 0
        self.pin_thruster_out_ = 0

if __name__ == "__main__":
    params = Params()