#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PwmOut.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: FENG XUANDA
#

import pigpio
import time

class PwmOut:
    # [Servo motor]
    #

    # [T100 ESC]
    # Max Update Rate : 400 Hz
    # Stopped     : 1500 microseconds
    # Max forward : 1900 microseconds
    # Max reverse : 1100 microseconds

    frequency = 50

    def __init__(self, pin_servo, pin_thruster):
        # GPIO number
        self.pin_servo = pin_servo
        self.pin_thruster = pin_thruster
        self.servo_pulsewidth = 1500
        self.thruster_pulsewidth = 1500
        self.coefficient = 1.0

        # Setup for Out
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin_servo, pigpio.OUTPUT)
        self.pi.set_mode(self.pin_thruster, pigpio.OUTPUT)
        self.pi.set_servo_pulsewidth(self.pin_servo, 1500) # neutral
        self.pi.set_servo_pulsewidth(self.pin_thruster, 1500) # neutral
        return

    # This function changes pulsewidth for weather. 
    def shapeThrusterPulsewidth(self):
        self.thruster_pulsewidth = (self.thruster_pulsewidth - 1500) * self.coefficient + 1500
        return

    def finalize(self):
        self.pi.set_servo_pulsewidth(self.pin_servo, 1500) # neutral
        self.pi.set_servo_pulsewidth(self.pin_thruster, 1500) # neutral
        return

    def updatePulsewidth(self):
        self.shapeThrusterPulsewidth()
        self.pi.set_servo_pulsewidth(self.pin_servo, self.servo_pulsewidth)
        self.pi.set_servo_pulsewidth(self.pin_thruster, self.thruster_pulsewidth)
        return

if __name__ == "__main__":
    sample = PwmOut(23, 24)
    num = 80
    neutral_to_max = 1900 - 1500
    dp = neutral_to_max / num
    servo_pulsewidth = 1500
    # move a servo motor
    for i in range(num):
        time.sleep(0.5)
        servo_pulsewidth = servo_pulsewidth + dp
        sample.servo_pulsewidth = servo_pulsewidth
        sample.updatePulsewidth()
    sample.finalize()
        