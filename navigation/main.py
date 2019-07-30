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
    try:
        # Initilize
        driver = Driver()
        # Command line arguments
        args = sys.argv
        if len(args) < 2:
            raise InitialArgumentsError
        # Load parameters
        driver.load(args[1])
        # Control Loop
        driver.doOperation()
    except InitialArgumentsError:
        print('[ERROR] NO ARGUMENTS')
        print('Usage: python3 main.py (parameter_file)')
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        driver.finalize()
        print('finish')

class InitialArgumentsError(Exception):
    pass

if __name__ == "__main__":
    main()
