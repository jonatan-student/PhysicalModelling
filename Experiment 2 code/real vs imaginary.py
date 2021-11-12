import matplotlib.pyplot as plt
import numpy as np
import cmath

reZ = [
    1368.14,
    743.91,
    -98.39,
    26.63,
    -1.60,
    -4.26,
    -2.69
]


imZ = [
    16.373,
    31.399,
    64.634,
    627.93,
    6549.3,
    57629.7,
    1555.088
]

freq = [
    250.0,
    500.0,
    1000.0,
    10000.0,
    100000.0,
    500000.0,
    750000.0
]

plt.xlabel('LOG($\omega$)')
plt.ylabel('Real Z')
plt.semilogx(freq, reZ)
plt.show()

plt.xlabel('LOG($\omega$)')
plt.ylabel('LOG(Imaginary Z)')
plt.loglog(freq, imZ)
plt.show()