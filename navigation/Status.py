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

class Status:
    def __init__(self, state, params):
        self.state = state
        self.params = params
        self.mode = 'AN'
        self.speed = 0.0
        self.direction = 0.0
        self.latitude = 0.0
        self.logitude = 0.0
        self.time_stamp = 0.0



if __name__ = "__main__"