#!/usr/bin/env python
"""
    find files whose size is greater than or equal to specified number of bytes
"""
import sys
import os

MINIMUM_SIZE = 1000

if len(sys.argv) < 2: # <1>
    print('Syntax: walk2.py START-DIR')
    sys.exit(1)

for currdir, subdirs, files in os.walk(sys.argv[1]):
    for file in files: # <2>
        fullpath = os.path.join(currdir, file) # <3>
        if os.path.isfile(fullpath): # <4>
            fsize = os.path.getsize(fullpath) # <5>
            if fsize >= MINIMUM_SIZE: # <6>
                print("{:40s} {:8d}".format(fullpath, fsize))
