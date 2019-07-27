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
from Status import Status

class Driver:
    def __init__(self):
        self.state_ = State(0)
        self.params_ = Params()
        self.status_ = Status(self.params_)

    def load(self, filename):
        print(filename)

    def readGPS(self):
        status = self.status_
        #status.readGPS

    #def readPWM(self):

    #def outPWM(self):

    #def finalize(self):

    #def autoNavigation(self):

    #def remoteControl(self):

if __name__ == "__main__":
    print('Driver')
    driver = Driver()
    print(driver.state_.inTimeLimit())
