#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pwm.py
#
# Solar-boat Project 2019
#   created on: 2019/08/01
#   Author: Tetsuro Ninomiya
#

import RPi.GPIO as GPIO
import threading
import time

class PwmRead:
    num_cycles = 5

    def __init__(self, pin_servo, pin_thruster, pin_mode):
        self.pin_servo = pin_servo
        self.pin_thruster = pin_thruster
        self.pin_mode = pin_mode
        self.pulse_width = [0.0, 0.0, 0.0] # [ms] # mode, servo, thruster

        # setup for GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_servo, GPIO.IN)
        GPIO.setup(pin_thruster, GPIO.IN)
        GPIO.setup(pin_mode, GPIO.IN)
        self.pwmthread = threading.Thread(target=self.measurePulseWidth(), args=())
        self.pwmthread.daemon() = True
        self.pwmthread.start()

    def measurePulseWidth(self):
        '''
        PWM frequency is 50 Hz
        So a pulse width must be under 20 ms
        The range of the receiver's PWM is 1.0 ~ 2.0 ms
        '''

        # mode
        sum = 0.0
        for i in range(PwmRead.num_cycles):
            GPIO.wait_for_edge(self.pin_mode, GPIO.RISING)
            start = time.time()
            GPIO.wait_for_edge(self.pin_mode, GPIO.FALLING)
            sum = sum + (time.time() - start)
        self.pulse_width[0] = sum / PwmRead.num_cycles

        # servo
        sum = 0.0
        for i in range(PwmRead.num_cycles):
            GPIO.wait_for_edge(self.pin_servo, GPIO.RISING)
            start = time.time()
            GPIO.wait_for_edge(self.pin_servo, GPIO.FALLING)
            sum = sum + (time.time() - start)
        self.pulse_width[1] = sum / PwmRead.num_cycles

        # thruster
        sum = 0.0
        for i in range(PwmRead.num_cycles):
            GPIO.wait_for_edge(self.pin_thruster, GPIO.RISING)
            start = time.time()
            GPIO.wait_for_edge(self.pin_thruster, GPIO.FALLING)
            sum = sum + (time.time() - start)
        self.pulse_width[2] = sum / PwmRead.num_cycles

        return
        
    def printPulseWidth(self):
        print("mode:     ", self.pulse_width[0], "[ms]")
        print("servo:    ", self.pulse_width[1], "[ms]")
        print("thruster: ", self.pulse_width[2], "[ms]")
        print("")
        return

    def finalize(self):
        GPIO.cleanup(self.pin_mode)
        GPIO.cleanup(self.pin_servo)
        GPIO.cleanup(self.pin_thruster)
        return

if __name__ == "__main__":
    pwm_read = PwmRead(1,2,3)
    for i in range(20):
        time.sleep(1)
        pwm_read.printPulseWidth()
    pwm_read.finalize()