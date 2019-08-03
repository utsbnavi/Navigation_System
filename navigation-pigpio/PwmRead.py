#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pwm.py
#
# Solar-boat Project 2019
#   created on: 2019/08/01
#   Author: Tetsuro Ninomiya
#

import pigpio
import time

class PwmRead:
    watchdog_time = 10000

    def __init__(self, pin_mode, pin_servo, pin_thruster):
        self.pin_servo = pin_servo
        self.pin_thruster = pin_thruster
        self.pin_mode = pin_mode
        self.pulse_width = [0, 0, 0] # [us] # mode, servo, thruster

        # setup for pigpio
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin_mode, pigpio.INPUT)
        self.pi.set_mode(self.pin_servo, pigpio.INPUT)
        self.pi.set_mode(self.pin_thruster, pigpio.INPUT)

        # set watchdog on pin_mode
        self.pi.set_watchdog(self.pin_mode, PwmRead.watchdog_time)

        # callback
        self.cb_mode = self.pi.callback(self.pin_mode, pigpio.EITHER_EDGE, self.cbf_mode)
        self.cb_servo = self.pi.callback(self.pin_mode, pigpio.EITHER_EDGE, self.cbf_servo)
        self.cb_thruster = self.pi.callback(self.pin_mode, pigpio.EITHER_EDGE, self.cbf_thruster)

    def cbf_mode(self, gpio, level, thick):
        if level == 1:
            self.cb_mode_start = time.time()
        if level == 0:
            pw = (time.time() - self.cb_mode_start) * 1000 * 1000
            if (pw > 700) and (pw < 2300):
                self.pulse_width[0] = pw
        return
        
    def cbf_servo(self, gpio, level, thick):
        if level == 1:
            self.cb_servo_start = time.time()
        if level == 0:
            pw = (time.time() - self.cb_servo_start) * 1000 * 1000
            if (pw > 700) and (pw < 2300):
                self.pulse_width[1] = pw
        return

    def cbf_thruster(self, gpio, level, thick):
        if level == 1:
            self.cb_thruster_start = time.time()
        if level == 0:
            pw = (time.time() - self.cb_thruster_start) * 1000 * 1000
            if (pw > 700) and (pw < 2300):
                self.pulse_width[2] = pw
        return

    def printPulseWidth(self):
        print("mode:     ", self.pulse_width[0], "[ms]")
        print("servo:    ", self.pulse_width[1], "[ms]")
        print("thruster: ", self.pulse_width[2], "[ms]")
        print("")
        return

    def finalize(self):
        self.pi.stop()
        return

if __name__ == "__main__":
    pwm_read = PwmRead(7,3,5)
    for i in range(20):
        time.sleep(1)
        pwm_read.printPulseWidth()
    pwm_read.finalize()