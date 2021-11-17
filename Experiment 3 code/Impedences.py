import matplotlib.pyplot as plt
import numpy as np
import cmath

from numpy.lib.type_check import real

table = np.array([
#[frequency, resistor setting, Phase difference, U_0, V_0]
[10,        5000,               -0.5,           2.02, 0.07],
[100,       5000,               -2.9,           2.02, 0.67],
[250,       5000,               -7.05,          2.03, 0.68],
[500,       5000,               -13.4,          2.03, 0.71],
[900,       5000,               -21.5,          2.01, 0.79],
[1000,      5000,               -22.9,          2.01, 0.81],
[10000,     500,                -62.5,          1.99, 0.67],
[100000,    100,                -53.6,          1.67, 0.99],
[500000,    10,                 -92.3,          0.67, 0.39],
[750000,    40,                 -14.4,          0.92, 0.98]]
)

Ztheory = np.array([
    [999.9, -0.54],
    [995.6, -5.38],
    [973.35, -13.2582],
    [904.592, -25.2316],
    [762.605, -40.3056],
    [727.727, -43.3038],
    [105.511, -83.9434],
    [10.6097, -89.3921],
    [2.12206, -89.8784],
    [1.41471, -89.9189]
])
ImpNorm = Ztheory[:, 0]
ImpPhase = Ztheory[:, 1]
Impedence = [cmath.rect(ImpNorm[i], ImpPhase[i]) for i in range(10)]
ImpReal = [i.real for i in Impedence]
ImpImag = [i.imag for i in Impedence]

freq = table[:,0]
R = table[:, 1]
phi = table[:, 2]
U_0 = table[:,3]
V_0 = table[:,4]


def FindZ(U, V, phi, Res):
    z = (U / V * np.exp(1j * phi) - 1) * Res
    return z

def Findnorm(z):
    polarz = cmath.polar(z)
    norm = polarz[0]
    return norm

def Findphase(z):
    polarz = cmath.polar(z)
    phase = polarz[1]
    return phase

Z = [FindZ(U_0[x], V_0[x], phi[x], 1000) for x in range(10)]
normz = [Findnorm(x) for x in Z]
phasez = [Findphase(x) for x in Z]
realZ = [x.real for x in Z]
imZ = [x.imag for x in Z]


plt.title('$|Z| vs. \omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$\log(|Z|)$')
plt.loglog(freq, Ztheory[:,0], '*-')
plt.loglog(freq, normz,'o-')
plt.show()

plt.title('$\phi_Z$ vs. $\omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$\phi_Z$')
plt.semilogx(freq, Ztheory[:, 1], '*-')
plt.semilogx(freq, phasez, 'o-')
plt.show()

plt.title('$Z\'$ vs. $\omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$Z\'$')
plt.semilogx(freq, ImpReal, '*-')
plt.semilogx(freq, realZ,'o-')
plt.show()

plt.title('$Z_imaginary$ vs. \omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$Z\")$')
plt.semilogx(freq, ImpImag,'*-')
plt.semilogx(freq, imZ,'o-')
plt.show()