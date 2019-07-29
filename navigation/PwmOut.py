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

class PwmOut:
    frequency = 50

    def __init__(self, pin_servo, pin_thruster):
        self.pin_servo = pin_servo
        self.pin_thruster = pin_thruster
        self.servo_duty_ratio = 0
        self.thruster_duty_ratio = 0

        # Setup for Out
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_servo, GPIO.OUT)
        GPIO.setup(self.pin_thruster, GPIO.OUT)
        self.pwm_servo = GPIO.PWM(self.pin_servo, Pwm.frequency)
        self.pwm_thruster = GPIO.PWM(self.pin_thruster, Pwm.frequency)
        self.pwm_servo.start(0)
        self.pwm_thruster.start(0)
        return

    def gpioCleanUp(self):
        GPIO.cleanup()
        return

    def updateDutyRatio(self):
        self.pwm_servo.ChangeDutyCycle(self.servo_duty_ratio)
        self.pwm_thruster.ChangeDutyCycle(self.thruster_duty_ratio)
        return

if __name__ == "__main__":
    pwm_sample = PwmOut(22, 22)
    pwm_sample.out()
    pwm_sample.finalize()