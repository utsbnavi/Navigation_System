#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Driver.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#

from State import State
from Params import Params

class Driver:
    def __init__(self):
        self.state = State(0)
        self.params = Params()

    def load(self, filename):
        print(filename)

    #def readGPS(self):

    #def readPWM(self):

    #def outPWM(self):

    #def finalize(self):

    #def autoNavigation(self):

    #def remoteControl(self):

if __name__ == "__main__":
    print('Driver')
    driver = Driver()
    print(driver.state.inTimeLimit())
