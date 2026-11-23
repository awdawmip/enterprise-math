#!/usr/bin/env python3
"""Exact rational verification for PREFIX-1040; no Bessel sampling or native propagation."""
from fractions import Fraction as Q

def envelopes(c):
    delta = Q(1, 10000)
    a, b = Q(c)-delta, Q(c)+delta
    r0, r1 = Q(10000*(2 if c == 4 else 4)-1, 10000), Q(10000*(2 if c == 4 else 4)+1, 10000)
    assert r0*r0 <= a and r1*r1 >= b
    v = max(abs(36-2*a), abs(36-2*b))
    w = max(abs(17*a-91), abs(17*b-91))
    z = max(abs(a-6), abs(b-6))
    R = 1/(2*r0)
    H = b*b*(36-a)**2
    H1 = 2*b*(36-a)*v
    H2 = 2*v*v+4*b*(36-a)
    P = b*(36-a)*w
    P1 = v*w+17*b*(36-a)
    A,A1 = 2*H1+P,2*H2+P1
    B,B1 = H/r0,H1/r0+H/(2*r0**3)
    C,C1 = 12*(11+b),Q(12)
    D,D1 = r1*z,r1+R*z
    E,E1 = 2*b,Q(2)
    S = (A1+A*R+B1+B*R+C1*(D+E*r1)+C*(D1+D*R+E1*r1+E*R))/5
    M = Q(2,5)*(Q(11,10)*A+2*B+C*(2*D+6*E))
    L = Q(2,5)*(Q(11,10)*A1+2*A*R+2*B1+4*B*R+C1*(2*D+6*E)+C*(2*D1+4*D*R+6*E1+14*E*R))
    return S,M,L

S4,M4,L4 = envelopes(4)
S16,M16,L16 = envelopes(16)
C4 = S4+3*L4+Q(8,3)*M4
C16 = S16+Q(14,3)*L16+Q(12,7)*M16
assert C4 < 104400, C4
assert C16 < 291700, C16
assert Q(6371,60)-Q(104400,1000) > Q(7,4)
assert 31622**2 < 10**9
assert Q(919,90)-Q(291700,31622) > Q(49,50)
assert Q(6371,60)-Q(104400,2000) > 53
assert Q(919,90)-Q(291700,40000) > Q(29,10)
print("EXACT_FRACTION_CERTIFICATE_PASSED")
for name,val in [("S4",S4),("M4",M4),("L4",L4),("C4",C4),("S16",S16),("M16",M16),("L16",L16),("C16",C16)]:
    print(name, str(val))
