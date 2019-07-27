#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pid.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#

class Pid:
    def __init__(self):
        p_ = 0.0
        i_ = 0.0
        d_ = 0.0

    def setPID(self, p, i, d):
        self.p_ = p
        self.i_ = i
        self.d_ = d

    # Implement these function below
    #def getDutyforServo(self, boat_direction, target_direction):
        #return duty_ratio

if __name__ == "__main__":
    print('pid')
    
