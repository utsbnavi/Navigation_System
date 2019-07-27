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
        p = 0.0
        i = 0.0
        d = 0.0

    def setPID(self, p, i, d):
        self.p = p
        self.i = i
        self.d = d

    # Implement these function below
    #def getDutyforServo(self, boat_direction, target_direction):
        #return duty_ratio

if __name__ == "__main__":
    print('pid')
    
