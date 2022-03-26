#!/usr/bin/env python
import numpy as np

sample_data = np.loadtxt(   # <1>
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
)

print("first 5 rows of sample_data:")
print(sample_data[:5, :], '\n')

selected = sample_data[  # <2>
    (sample_data[:, 0] < 10) &  # <3>
    (sample_data[:, -1] > 35)
]

print("selected")
print(selected)
