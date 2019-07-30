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
from PwmOut import PwmOut
from Pid import PositionalPID

import time

class Driver:
    def __init__(self):
        self.state = State(0)
        self.params = Params()
        self.status = Status(self.params)
        self.pwm_out = PwmOut(self.params.pin_servo_out, self.params.pin_thruster_out)
        self.pid = PositionalPID()
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
        self.pid.setPID(p, i, d)

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
        f.close()
        return

    def doOperation(self):
        while self.state.inTimeLimit():
            self.readGps()
            self.readPWM()
            self.updateStatus()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()
            elif mode == 'TEST':
                self.testNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(2)
        return
            
    def getMode(self):
        return self.status.mode

    def readGps(self):
        self.status.readGps()
        return

    def updateStatus(self):
        status = self.status
        status.calcTargetDirection()
        status.calcTargetDistance()
        status.updateTarget()
        if status.isGpsError():
            status.mode = 'RC'
        return

    def readPWM(self):
        print('no readPWM')
        return

    def outPWM(self):
        self.pwm_out.updateDutyRatio()
        return

    def autoNavigation(self):
        boat_direction = self.status.boat_direction
        target_direction = self.status.target_direction
        servo_duty_ratio = self.pid.getStepSignal(target_direction, boat_direction)
        self.pwm_out.servo_duty_ratio = servo_duty_ratio
        self.pwm_out.thruster_duty_ratio = 9.0
        return

    def remoteControl(self):
        # Do nothing
        return

    def printLog(self):
        timestamp_string = self.status.timestamp_string
        mode = self.getMode()
        latitude = self.status.latitude
        longitude = self.status.longitude
        speed = self.status.speed
        direction = self.status.boat_direction
        servo_dr = self.pwm_out.servo_duty_ratio
        thruster_dr = self.pwm_out.thruster_duty_ratio
        t_direction = self.status.target_direction
        t_distance = self.status.target_distance
        print(timestamp_string)
        print(
            '[%s MODE] LAT=%.5f, LON=%.5f, SPEED=%.2f [km/h], DIRECTION=%lf' %
            (mode, latitude, longitude, speed, direction)
        )
        print('DUTY (SERVO, THRUSTER):       (%lf, %lf)(2.5~12.5)' % (servo_dr, thruster_dr))
        print('TARGET (DIRECTION, DISTANCE): (%lf, %lf [m])' % (t_direction, t_distance))
        print('')
        self.logger.write(timestamp_string, latitude, longitude)
        return

    def finalize(self):
        self.logger.close()
        self.pwm_out.finalize()
        return

    def testNavigation(self):
        duty = 10 / 180 * self.__dir_test + 2.5
        self.pwm_out.servo_duty_ratio = duty
        self.__dir_test += 5
        self.__dir_test = self.__dir_test % 180
        # Constant pwm for thruster
        self.pwm_out.thruster_duty_ratio = 7.25
        return

if __name__ == "__main__":
    print('Driver')
    driver = Driver()
    driver.load("parameter_sample.txt")
