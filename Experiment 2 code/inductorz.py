import matplotlib.pyplot as plt
import numpy as np
import cmath

reZ = [
    47.029,
    44.943,
    46.9138,
    44,969,
    -211.64,
    -133587,
    1454999.186
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
plt.ylim(0, cmath.pi)
plt.show()
