#!/usr/bin/env python


import numpy as np

sample_data = np.loadtxt(   # <1>
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=int
)

sample_data  *= 100  # <2>

print(sample_data)

file_name = 'sampledata'

np.save(file_name, sample_data)  # <3>

retrieved_data = np.load(file_name + '.npy')  # <4>

print('-' * 60)
print(retrieved_data)

