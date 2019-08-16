#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Logger.py
#
# Solar-boat Project 2019
#   created on: 2019/07/27
#   Author: Tetsuro Ninomiya
#

import csv

class Logger:
    filename = 'gpslog.csv'

    def open(self):
        self.f = open(Logger.filename, "a")
        self.writer = csv.writer(self.f, lineterminator='\n')
        log_list = ['TIME_STAMP', 'MODE', 'LATITUDE', 'LONGITUDE', 'DIRECTION', 'SPEED','T_INDEX', 'T_LATITUDE', 'T_LONGITUDE', 'T_DIRECTION', 'ERR_BACK']
        self.writer.writerow(log_list)

    def write(self, log_list):
        self.writer.writerow(log_list)

    def close(self):
        self.f.write("END\n")
        self.f.close()

if __name__ == "__main__":
    logger = Logger()
    logger.open()
    logger.write([1,1,1])
    logger.close()