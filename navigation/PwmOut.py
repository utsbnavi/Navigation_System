#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pwm.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: FENG XUANDA
#

import RPi.GPIO as GPIO

class PwmOut:
    frequency = 50

    def __init__(self, pin_servo, pin_thruster):
        self.pin_servo = pin_servo
        self.pin_thruster = pin_thruster
        self.servo_duty_ratio = 2.5
        self.thruster_duty_ratio = 7.5

        # Setup for Out
        GPIO.setup(self.pin_servo, GPIO.OUT)
        GPIO.setup(self.pin_thruster, GPIO.OUT)
        self.pwm_servo = GPIO.PWM(self.pin_servo, PwmOut.frequency)
        self.pwm_thruster = GPIO.PWM(self.pin_thruster, PwmOut.frequency)
        self.pwm_servo.start(0)
        self.pwm_thruster.start(0)
        return

    def finalize(self):
        GPIO.cleanup(self.pin_servo)
        self.pwm_thruster.ChangeDutyCycle(5)
        return

    def updateDutyRatio(self):
        self.pwm_servo.ChangeDutyCycle(self.servo_duty_ratio)
        self.pwm_thruster.ChangeDutyCycle(self.thruster_duty_ratio)
        return

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    pwm_sample = PwmOut(22, 22)
    pwm_sample.updateDutyRatio()
    pwm_sample.finalize()