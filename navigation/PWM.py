#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pwm.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: 
#

import RPi.GPIO as GPIO

class Pwm:
    frequency = 50

    def __init__(self, pin_in, pin_out):
        self.duty_ratio = 0
        self.error = False
        self.pin_in = pin_in
        self.pin_out = pin_out

        # Setup for Out
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_out, GPIO.OUT)
        pwm = GPIO.PWM(self.pin_out, Pwm.frequency)
        pwm.start(0)

    def finalize(self):
        GPIO.cleanup()

    def out(self):
        pwm.ChangeDutyCycle(self.duty_ratio)

    # Implement these functions below
    #def read(self):


if __name__ == "__main__":
    pwm_sample = Pwm(0, 22)
    pwm_sample.out()
    pwm_sample.finalize()