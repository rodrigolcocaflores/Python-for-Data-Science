#!/usr/bin/env python
import numpy as np

m1 = np.array(
    [[2, 4, 6],
     [10, 20, 30]]
)  # <1>

m2 = np.array([[1, 15],
                [3, 25],
                [5, 35]])  # <2>

print('m1 =>\n', m1)
print()

print('m2 =>\n', m2)
print()

print('m1 * 10 =>\n', m1 * 10)  # <3>
print()

print('m1 @ m2 =>\n', m1 @ m2)  # <4>
print()

