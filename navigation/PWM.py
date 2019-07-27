#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pwm.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: 
#

class Pwm:
    frequency = 50

    def __init__(self, pin_in, pin_out):
        self.duty_ratio = 0
        self.error = False
        self.pin_in = pin_in
        self.pin_out = pin_out

    # Implement these functions below
    #def read(self):

    #def out(self):

if __name__ == "__main__":
    print('pwm')