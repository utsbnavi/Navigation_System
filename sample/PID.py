
class PositionalPID:

    
    def __init__(self, P, I, D):                                           
        self.Kp = P
        self.Ki = I
        self.Kd = D
 
        self.ResultValueBack = 0.0
        self.PidOutput = 0.0
        self.PIDErrADD = 0.0
        self.ErrBack = 0.0
 
    def SetStepSignal(self,TargetAngle,SystemOutput):

        import math
        
        Err = TargetAngle - SystemOutput
        KpWork = self.Kp * Err
        KiWork = self.Ki * self.PIDErrADD
        KdWork = self.Kd * (Err - self.ErrBack)
        self.PidOutput = KpWork + KiWork + KdWork
        self.temp = math.exp(-self.PidOutput)

        if self.PidOutput>0:                                                      
            self.PidOutput=1/(1+self.temp)
        if self.PidOutput<0:
            self.PidOutput=(1/(1+self.temp))-2

        self.direction = self.PidOutput*30                                 

        duty = 2 / 180 * (self.direction + 90) + 0.5                         
        
        self.PIDErrADD += Err
        self.ErrBack = Err

        return duty
