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
from Logger import Logger

import time

class Driver:
    def __init__(self):
        self.state = State(0)
        self.params = Params()
        self.status = Status(self.params)
        self.logger = Logger()
        self.logger.open()

        self.__dir_test = 0

    def load(self, filename):
        print('loading', filename)
        f = open(filename, "r")

        line = f.readline()
        line = f.readline()
        self.state.time_limit = int(line.split()[1]) # Time Limit

        line = f.readline()
        line = f.readline()
        line = f.readline()
        p = float(line.split()[1]) # P
        line = f.readline()
        i = float(line.split()[1]) # I
        line = f.readline()
        d = float(line.split()[1]) # D
        self.status.pid.setPID(p, i, d)

        line = f.readline()
        line = f.readline()
        line = f.readline()
        num = int(line.split()[1]) # Number of waypoints
        line = f.readline()
        for i in range(num):
            line = f.readline()
            self.status.waypoint.addPoint(
                float(line.split()[0]),
                float(line.split()[1])
            )

        line = f.readline()
        line = f.readline()

        line = f.readline()
        self.params.pin_gps_in = int(line.split()[1])
        line = f.readline()
        self.params.pin_mode_in = int(line.split()[1])
        line = f.readline()
        self.params.pin_servo_in = int(line.split()[1])
        line = f.readline()
        self.params.pin_servo_out = int(line.split()[1])
        line = f.readline()
        self.params.pin_thruster_in = int(line.split()[1])
        line = f.readline()
        self.params.pin_thruster_in = int(line.split()[1])

        f.close()

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGPS()
            self.readPWM()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()
            elif mode == 'TEST':
                self.testNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(1)
        self.finalize()


        f.close()

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGPS()
            self.readPWM()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()
            elif mode == 'TEST':
                self.testNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(1)
        self.finalize()


        f.close()

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGPS()
            self.readPWM()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()
            elif mode == 'TEST':
                self.testNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(1)
        self.finalize()


        f.close()

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGPS()
            self.readPWM()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()
            elif mode == 'TEST':
                self.testNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(1)
        self.finalize()


        f.close()

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGPS()
            self.readPWM()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()
            elif mode == 'TEST':
                self.testNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(1)
        self.finalize()


        f.close()

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGPS()
            self.readPWM()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()
            elif mode == 'TEST':
                self.testNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(1)
        self.finalize()
            
    def getMode(self):
        return self.status.mode

    def readGps(self):
        self.status.readGps()

    def readPWM(self):
        print('no readPWM')

    def outPWM(self):
        self.status.outPwm()

    def autoNavigation(self):
        print('no autoNavigation')

    def remoteControl(self):
        print('no remoteControl')

    def printLog(self):
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
        self.logger.write(time_stamp, latitude, longitude)

    def finalize(self):
        self.logger.close()

    def testNavigation(self):
        duty = 10 / 180 * self.__dir_test + 2.5
        status.servo_pwm.duty_ratio = duty
        self.__dir_test += 5
        self.__dir_test = self.__dir_test % 180
        # Constant pwm for thruster
        status.thruster_pwm.duty_ratio = 7.25

if __name__ == "__main__":
    print('Driver')
    driver = Driver()
    driver.load("parameter_sample.txt")
