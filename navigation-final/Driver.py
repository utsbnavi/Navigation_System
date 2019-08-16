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
from PwmRead import PwmRead
from Pid import PositionalPID

import time

class Driver:
    def __init__(self):
        self.state = State(0)
        self.params = Params()
        self.status = Status(self.params)
        self.sleep_time = 1
        self.pwm_read = PwmRead(self.params.pin_mode_in, self.params.pin_servo_in, self.params.pin_thruster_in)
        self.pwm_out = PwmOut(self.params.pin_servo_out, self.params.pin_thruster_out)
        self.pid = PositionalPID()
        self.logger = Logger()
        self.logger.open()

    def load(self, filename):
        print('loading', filename)
        f = open(filename, "r")

        line = f.readline()
        line = f.readline()
        self.state.time_limit = int(line.split()[1]) # Time Limit
        line = f.readline()
        self.sleep_time = float(line.split()[1]) # Sleep time

        line = f.readline()
        line = f.readline()
        line = f.readline()
        self.pwm_read.num_cycles = int(line.split()[1]) # NUM_CYCLE

        line = f.readline()
        line = f.readline()
        line = f.readline()
        self.pwm_out.coefficient = float(line.split()[1]) # Coefficient

        line = f.readline()
        line = f.readline()
        line = f.readline()
        self.pid.angular_range = int(line.split()[1]) # angular_range
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
        self.status.waypoint_range = float(line.split()[1]) # range of target point
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
            self.readPWM()
            self.readGps()

            mode = self.getMode()
            if mode == 'RC':
                self.remoteControl()
            elif mode == 'AN':
                self.autoNavigation()

            self.outPWM()
            self.printLog()
            time.sleep(self.sleep_time)
        return
            
    def getMode(self):
        return self.status.mode

    def updateMode(self):
        mode_duty_ratio = self.pwm_read.pulse_width[0]
        if  mode_duty_ratio < 1500:
            self.status.mode = 'RC'
        elif mode_duty_ratio >= 1500:
            self.status.mode = 'AN'
        return

    def readGps(self):
        self.status.readGps()
        self.updateMode()
        #if self.status.isGpsError():
            #self.status.mode = 'RC'
        return

    def updateStatus(self):
        status = self.status
        status.calcTargetDirection()
        status.calcTargetDistance()
        status.updateTarget()
        return

    # Read pwm pulsewidth
    # Set the readout signals as the output signals
    def readPWM(self):
        self.pwm_read.measurePulseWidth()
        self.pwm_out.servo_pulsewidth = self.pwm_read.pulse_width[1]
        self.pwm_out.thruster_pulsewidth = self.pwm_read.pulse_width[2]
        return

    def outPWM(self):
        self.pwm_out.updatePulsewidth()
        return

    def autoNavigation(self):
        self.updateStatus()
        if self.status.mode != 'AN_END':
            boat_direction = self.status.boat_direction
            target_direction = self.status.target_direction
            servo_pulsewidth = self.pid.getStepSignal(target_direction, boat_direction)
            self.pwm_out.servo_pulsewidth = servo_pulsewidth
            self.pwm_out.thruster_pulsewidth = 1880
            return
        else:
            # If the boat has passed the last waypoint,
            # the navigation system get RC mode.
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
        servo_pw = self.pwm_out.servo_pulsewidth
        thruster_pw = self.pwm_out.thruster_pulsewidth
        t_index = self.status.waypoint.getIndex()
        t_direction = self.status.target_direction
        t_distance = self.status.target_distance
        target = self.status.waypoint.getPoint()
        t_latitude = target[0]
        t_longitude = target[1]

        # To print logdata
        print(timestamp_string)
        print(
            '[%s MODE] LAT=%.7f, LON=%.7f, SPEED=%.2f [km/h], DIRECTION=%lf' %
            (mode, latitude, longitude, speed, direction)
        )
        print('DUTY (SERVO, THRUSTER):       (%6.1f, %6.1f) [us]' % (servo_pw, thruster_pw))
        print('TARGET No.%2d' % (t_index))
        print('TARGET (LATITUDE, LONGITUDE): (%.7f, %.7f)' % (t_latitude, t_longitude))
        print('TARGET (DIRECTION, DISTANCE): (%5.2f, %5.2f [m])' % (t_direction, t_distance))
        print('')

        # To write logdata (csv file)
        log_list = [timestamp_string, mode, latitude, longitude, direction, speed, t_index, t_latitude, t_longitude, t_direction]
        self.logger.write(log_list)
        return

    def finalize(self):
        self.logger.close()
        self.pwm_out.finalize()
        return

if __name__ == "__main__":
    print('Driver')
    driver = Driver()
    driver.load("parameter_sample.txt")
