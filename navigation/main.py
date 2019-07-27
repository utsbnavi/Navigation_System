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

def main():
    # Initilize
    driver = Driver()
    # Command line arguments
    args = sys.argv
    # Load parameters
    driver.load(args[1])
    # Control Loop
    driver.doOperation()

if __name__ == "__main__":
    main()
