#!/usr/bin/env python

import sys
import os.path

for path_name in sys.argv[1:]:
    if os.path.isdir(path_name):
        print("ERROR! {} is a directory".format(path_name))
        continue
    else:
        print(path_name, os.path.getsize(path_name))
