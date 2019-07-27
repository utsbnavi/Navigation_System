#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# main.py
#
# Solar-boat Project 2019
#   created on: 2019/07/25
#   Author: Tetsuro Ninomiya
#

import sys
from Driver import Driver

'''
NOW I'M MAKING!
WAIT FOR A WHILE!
'''

def main():
    driver = Driver()
    args = sys.argv
    print(args[0])
    print(args[1])
    print('Hello, world!')

if __name__ == "__main__":
    main()
