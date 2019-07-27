# Software PWM Servo.py
# -*- coding: utf-8 -*-
#
# Solar-boat Project 2019
# created on: 2019/07/25
# Author: FENG XUANDA
#
#----------------------

import RPi.GPIO as GPIO
import time

P_SERVO = 22           # No. of GPIO port
fPWM = 50              # Hz (software PWM，frequency cannot be too high)
a = 10
b = 2

def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO, GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)

def setDirection(direction):
    duty = 10 / 180 * direction + 2.5
    pwm.ChangeDutyCycle(duty)
    print ("direction =", direction, "-> duty =", duty)
    time.sleep(1) 
   
print ("starting")
setup()
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0    
setDirection(0)    
GPIO.cleanup() 
print ("done")
