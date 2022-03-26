#!/usr/bin/env python
import time
import numpy as np

sample_data = np.loadtxt(   # <1>
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
)

def set_default(value, limit, default): # <2>
    if value > limit:
        value = default

    return value

MAX_VALUE = 50      # <3>
DEFAULT_VALUE = -1  # <4>

print("Version 1: looping over arrays")
start = time.time() # <5>
try:
    version1_array = np.zeros(sample_data.shape, dtype=int)  # <6>
    for i, row in enumerate(sample_data):  # <7>
        for j, column in enumerate(row):
            version1_array[i, j] = set_default(sample_data[i, j], MAX_VALUE, DEFAULT_VALUE)   # <8>
except ValueError as err:
    print("Function failed:", err)
else:
    end = time.time()  # <9>
    elapsed = end - start  # <10>
    print(version1_array)
    print("took {:.5f} seconds".format(elapsed))
finally:
    print()


print("Version 2: broadcast without vectorize()")
start = time.time()
try:
    print("Without sp.vectorize:")
    version2_array = set_default(sample_data, MAX_VALUE, DEFAULT_VALUE) # <11>
except ValueError as err:
    print("Function failed:", err)
else:
    end = time.time()
    elapsed = end - start
    print(version2_array)
    print("took {:.5f} seconds".format(elapsed))
finally:
    print()

print("Version 3: broadcast with vectorize()")
set_default_vect = np.vectorize(set_default)  # <12>

start = time.time()
try:
    print("With sp.vectorize:")
    version3_array = set_default_vect(sample_data, MAX_VALUE, DEFAULT_VALUE) # <13>
except ValueError as err:
    print("Function failed:", err)
else:
    end = time.time()
    elapsed = end - start
    print(version3_array)
    print("took {:.5f} seconds".format(elapsed))
finally:
    print()
