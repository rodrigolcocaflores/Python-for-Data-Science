#!/usr/bin/env python
import numpy as np

a = np.loadtxt(  # <1>
    '../DATA/columns_of_numbers.txt',
    usecols=[2, 5], # <2>
   skiprows=1,  # <3>
)

print(a)
print(a.shape)  # <4>
print(a.size)  # <5>

print(np.where(a < 30, a, 1000))  # <6>

