#!/usr/bin/env python
import numpy as np

sample_data = np.loadtxt(   # <1>
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=float
)

sample_data  /= 10  # <2>

print(sample_data)
print("-" * 60)

file_name = 'sample.dat'

sample_data.tofile(file_name)  # <3>

data = np.fromfile(file_name)  # <4>
data.shape = sample_data.shape  # <5>

print(data)
