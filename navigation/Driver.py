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
        self.state = State(0)
        self.params = Params()
        self.status = Status(self.params)

    def load(self, filename):
        print(filename)

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGPS()
            self.readPWM()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()

            self.outPWM()
            self.log()
            
    def getMode(self):
        return self.status.mode

    def readGPS(self):
        status = self.status
        #status.readGPS

    def readPWM(self):
        print('readPWM')

    def outPWM(self):
        print('outPWM')

    def autoNavigation(self):
        print('autoNavigation')

    def remoteControl(self):
        print('remoteControl')

    def log(self):
        time_stamp = self.time_stamp
        mode = self.getMode()
        latitude = self.status.latitude
        longitude = self.status.longitude
        speed = self.status.speed
        direction = self.status.boat_direction
        servo_duty_ratio = self.status.servo_pwm.duty_ratio
        print(
            '%d: MODE=%s, LAT=%lf, LON=%lf, SPEED=%lf, DIRECTION=%lf, SERVO_DR=%lf' %
            (time_stamp, mode, latitude, longitude, speed, direction, servo_duty_ratio)
        )

if __name__ == "__main__":
    print('Driver')
    driver = Driver()
    print(driver.state.inTimeLimit())
