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
    -129938,
    -24939,
    -10305,
    -1362.4,
    -109.29,
    -12.308,
    -4.2188,
]

freq = [
    100,
    500,
    1000,
    10000,
    100000,
    500000,
    1000000
]

phaseZ =[]
normZ = []
for i in range(7):
    Z = (complex(reZ[i], imZ[i]))
    polarZ = (cmath.polar(Z))
    normZ.append(polarZ[0])
    phaseZ.append(polarZ[1])
print(normZ)
print(freq)

plt.xlabel('LOG($\omega$)')
plt.ylabel('LOG(|Z|)')
plt.loglog(freq, normZ)
plt.show()

plt.xlabel('LOG($\omega$)')
plt.ylabel('$\phi_Z$')
plt.semilogx(freq, phaseZ)
plt.ylim(-5, 0)
plt.show()
