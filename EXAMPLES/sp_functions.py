#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

dt = np.dtype([('Month', 'int8'), ('Day', 'int8'), ('Year', 'int16'), ('Temp', 'float64')])  # <1>
data = np.loadtxt('../DATA/weather/NYNEWYOR.txt', dtype=dt)  # <2>

print(data['Temp'])

temps = data['Temp']  # <3>

plt.plot(temps)  # <4>
plt.show()  # <5>
plt.cla()  # <6>

normalized_data = data[data['Temp'] > -50]  # <7>
temps = normalized_data['Temp']  # <8>
plt.plot(temps)  # <9>
plt.show()
