#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Pid.py
#
# Solar-boat Project 2019
#   created on: 2019/07/29
#   Author: FENG XUANDA
#

class PositionalPID:
    
    def __init__(self):                                           
        self.Kp = 0.0
        self.Ki = 0.0
        self.Kd = 0.0
 
        self.ResultValueBack = 0.0
        self.PidOutput = 0.0
        self.PIDErrADD = 0.0
        self.ErrBack = 0.0

    def setPID(self, P, I, D):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        return
 
    def getStepSignal(self,TargetAngle,SystemOutput):

        import math
        
        Err = TargetAngle - SystemOutput
        KpWork = self.Kp * Err
        KiWork = self.Ki * self.PIDErrADD
        KdWork = self.Kd * (Err - self.ErrBack)
        self.PidOutput = KpWork + KiWork + KdWork
        self.temp = math.exp(-self.PidOutput)

        if self.PidOutput>0:   #scale the output of PID to [-0.5, 0.5] using Sigmoid Funciton                                                   
            self.PidOutput=1/(1+self.temp)
        if self.PidOutput<0:
            self.PidOutput=(1/(1+self.temp))-2

        self.direction = self.PidOutput*30     #scale the angle of servo to [-30, 30]                            

        duty = 2 / 180 * (self.direction + 90) + 0.5    # the output angle is [60, 120]                     
        
        self.PIDErrADD += Err
        self.ErrBack = Err

        return duty

if __name__ == "__main__":
    print('pid')
    
