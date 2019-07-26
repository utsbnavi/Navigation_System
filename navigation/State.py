#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Solar-boat Project 2019
#   created on: 2019/07/25
#   Author: Tetsuro Ninomiya
#

import time

class State:
    # Constructor
    #   Argument: time_limit[sec]
    # Stopwatch starts when this class is called
    def __init__(self, time_limit):
        self.time_limit_ = time_limit
        self.startStopWatch()

    def startStopWatch(self):
        self.start_time_ = time.time()

    def getElapsedTime(self):
        elapsed_time = time.time() - self.start_time_
        return elapsed_time

    # This function returns:
    #   Within the time limit -> True
    #   Not -> False
    def inTimeLimit(self):
        elapsed_time = self.getElapsedTime()
        return elapsed_time < self.time_limit_


if __name__ == "__main__":
    state = State(10)
    time.sleep(5)
    print(state.inTimeLimit())
    time.sleep(5)
    print(state.inTimeLimit())
