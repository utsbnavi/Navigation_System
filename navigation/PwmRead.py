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
import time

class PwmRead:
    num_cycles = 5

    def __init__(self, pin_mode, pin_servo, pin_thruster):
        self.pin_servo = pin_servo
        self.pin_thruster = pin_thruster
        self.pin_mode = pin_mode
        self.pulse_width = [0.0, 0.0, 0.0] # [ms] # mode, servo, thruster
        self.duty_ratio = [0.0, 0.0, 0.0] # [%] # mode, servo, thruster

        # setup for GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_servo, GPIO.IN)
        GPIO.setup(pin_thruster, GPIO.IN)
        GPIO.setup(pin_mode, GPIO.IN)

    def measurePulseWidth(self):
        '''
        PWM frequency is 50 Hz
        So a pulse width must be under 20 ms
        The range of the receiver's signal(ON) is 1.0 ~ 2.0 ms
        1.0 ms : LOW
        1.5 ms : Neutral
        2.0 ms : HIGH

        There is a little delay, 0.01 ~ 0.03 ms
        For an error, if range is above 2.0 ms, not counted

        (M-02)
        [MODE]
        above 2.0 ms : DOWN
        under 1.0 ms : UP

        [SERVO][THRUSTER]
        max 1.94 ms     : DOWN
        neutral 1.53 ms
        min 1.13 ms     : UP
        '''
        #print(PwmRead.num_cycles)
        #a = time.time()

        # mode
        sum = 0.0
        for i in range(PwmRead.num_cycles):
            GPIO.wait_for_edge(self.pin_mode, GPIO.RISING)
            start = time.time()
            GPIO.wait_for_edge(self.pin_mode, GPIO.FALLING)
            sum = sum + (time.time() - start)
        ave = sum * 1000 / PwmRead.num_cycles
        if (ave > 0.7) and (ave < 2.3):
            self.pulse_width[0] = ave

        # servo
        sum = 0.0
        for i in range(PwmRead.num_cycles):
            GPIO.wait_for_edge(self.pin_servo, GPIO.RISING)
            start = time.time()
            GPIO.wait_for_edge(self.pin_servo, GPIO.FALLING)
            sum = sum + (time.time() - start)
        ave = sum * 1000 / PwmRead.num_cycles
        if (ave > 0.8) and (ave < 2.2):
            self.pulse_width[1] = ave

        # thruster
        sum = 0.0
        for i in range(PwmRead.num_cycles):
            GPIO.wait_for_edge(self.pin_thruster, GPIO.RISING)
            start = time.time()
            GPIO.wait_for_edge(self.pin_thruster, GPIO.FALLING)
            sum = sum + (time.time() - start)
        ave = sum * 1000 / PwmRead.num_cycles
        if (ave > 0.8) and (ave < 2.2):
            self.pulse_width[2] = ave

        #b = time.time() - a
        #print("It takes ", b, "[s] to measure PWM")

        return
        
    def calcDutyRatio(self):
        # One cycle : 20 ms
        # Pulth width : 1.0 ~ 2.0 ms
        # Duty Ratio : 5.0 ~ 10.0%
        self.measurePulseWidth()
        one_cycle = 20 #[ms]
        for i in range(3):
            # Round off the second decimal place of pulse width and calculate duty_ratio
            self.duty_ratio[i] = (round(self.pulse_width[i], 2) / one_cycle) * 100
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
    pwm_read = PwmRead(7,3,5)
    for i in range(20):
        time.sleep(1)
        pwm_read.measurePulseWidth()
        pwm_read.printPulseWidth()
    pwm_read.finalize()