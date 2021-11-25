import matplotlib.pyplot as plt
import numpy as np
import cmath

from numpy.lib.type_check import real

table = np.array([
#[frequency, resistor setting, Phase difference, U_0, V_0]
[10,        100000,             -0.3,           2.03, 1.83],
[100,       10000,              -1.8,           2.03, 1.01],
[250,       5000,               -7.1,           2.03, 0.68],
[500,       1500,               -18.1,          2.02, 0.28],
[900,       1100,               -30.8,          2.01, 0.24],
[1000,      1000,               -33.5,          2.01, 0.23],
[10000,     500,                -62.2,          1.99, 0.68],
[100000,    50,                 -68.5,          1.68, 0.61],
[500000,    10,                 -80.7,          0.64, 0.37],
[650000,    0.1,                -147.3,         0.31, 0.30]]
)

freq = table[:,0]
omega = [2*np.pi*x for x in freq]
R = table[:, 1]
phideg = table[:, 2]
phi = [x * (np.pi/180) for x in phideg]
U_0 = table[:,3] /2
V_0 = table[:,4] /2


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

resistor = 10000
t=0.000120
C = t/resistor

omegaTheory = np.logspace(1,7)
Impedence = resistor * (1 /(1 + (1j * omegaTheory*t)))
ImpNorm = [Findnorm(x) for x in Impedence]
ImpPhase = [Findphase(x) for x in Impedence]
ImpReal = [i.real for i in Impedence]
ImpImag = [-1*i.imag for i in Impedence]

Gtheory = 1j * omegaTheory * Impedence
GnormTheory = [Findnorm(x) for x in Gtheory]
GphaseTheory = [Findphase(x) for x in Gtheory]
GRealTheory = [g.real for g in Gtheory]
GImTheory = [g.imag for g in Gtheory]

Z = [FindZ(U_0[x], V_0[x], phi[x], R[x]) for x in range(10)]
normz = [Findnorm(x) for x in Z]
phasez = [Findphase(x) for x in Z]
realZ = [x.real for x in Z]
imZ = [-1*x.imag for x in Z]

G = [1j*omega[x]*Z[x] for x in range(10)]
Gnorm = [Findnorm(x) for x in G]
Gphase = [Findphase(x) for x in G]
Greal = [x.real for x in G]
GIm = [x.imag for x in G]

print(Z)
print(G)


plt.title('$|Z| vs. \omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$|Z|$')
plt.semilogx(omegaTheory, ImpNorm)
plt.semilogx(omega, normz,'o')
plt.show()


plt.title('$\phi_Z$ vs. $\omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$\phi_Z$')
plt.semilogx(omegaTheory, ImpPhase)
plt.semilogx(omega, phasez, 'o')
plt.show()


plt.title('$Re(Z)$ vs. $\omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$Re(Z)$')
plt.semilogx(omegaTheory, ImpReal)
plt.semilogx(omega, realZ,'o')
plt.show()

plt.title('$Im(Z)$ vs. $\omega$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$Im(Z)$')
plt.semilogx(omegaTheory, ImpImag)
plt.semilogx(omega, imZ,'o')
plt.show()


plt.title('$|G|$ vs $\log(\omega)$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$|G|$')
plt.semilogx(omegaTheory, GnormTheory)
plt.semilogx(omega, Gnorm, 'o')
plt.show()

plt.title('$\phi_G$ vs $\log(\omega)$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$\phi_G$')
plt.semilogx(omegaTheory, GphaseTheory)
plt.semilogx(omega, Gphase, 'o')
plt.show()

plt.title('$Re(G)$ vs $\log(\omega)$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$Re(G)$')
plt.semilogx(omegaTheory, GRealTheory)
plt.semilogx(omega, Greal, 'o')
plt.show()

plt.title('$Im(G)$ vs $\log(\omega)$')
plt.xlabel('$\log(\omega)$')
plt.ylabel('$Im(G)$')
plt.semilogx(omegaTheory, GImTheory)
plt.semilogx(omega, GIm,'o')
plt.show()
