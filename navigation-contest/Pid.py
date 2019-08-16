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
        print("PID Err: ",Err)
        KpWork = self.Kp * Err
        KiWork = self.Ki * self.PIDErrADD
        KdWork = self.Kd * (Err - self.ErrBack)
        self.PidOutput = KpWork + KiWork + KdWork
        self.temp = math.exp(-self.PidOutput)

        if self.PidOutput>0:                                                      
            self.PidOutput=1/(1+self.temp)-0.5
        if self.PidOutput<0:
            self.PidOutput=(1/(1+self.temp))-0.5

        self.direction = self.PidOutput*150                             

        duty = 1000 / 180 * (self.direction + 90) + 1000                         
        
        self.PIDErrADD += Err
        self.ErrBack = Err

        return duty

if __name__ == "__main__":
    print('pid')
    
