#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pwm.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#

class Pwm:
    frequency = 50

    def __init__(self, pin_in, pin_out):
        self.duty_ratio_ = 0
        self.error_ = False
        self.pin_in_ = pin_in
        self.pin_out_ = pin_out

    # Implement these functions below
    #def read(self):

    #def out(self):

if __name__ == "__main__":
    print('pwm')