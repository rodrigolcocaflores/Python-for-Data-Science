#!/usr/bin/env python

# count number of files and dirs in  a directory tree
# note "files" includes devices, symbolic links, and pipes
import os
import sys

if sys.platform == 'win32':  # <1>
    target = 'C:/Users'
else:
    target = '/etc'

total_files = 0  # <2>
total_dirs = 0

for currdir, subdirs, files in os.walk(target):  # <3>
    total_dirs += 1  # increment number of directories seen
    total_files += len(files)  # add the number of files in this dir

print("{} contains {} dirs and {} files".format(target, total_dirs, total_files))  # <4>
