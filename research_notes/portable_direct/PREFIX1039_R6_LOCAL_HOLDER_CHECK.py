#!/usr/bin/env python3
"""Exact Fraction recomputation for PREFIX-1039's conditional scalar bounds."""
from fractions import Fraction as Q


def bounds(yl, yu, rl, ru):
    yl, yu, rl, ru = map(Q, (yl, yu, rl, ru))
    assert rl**2 <= yl and ru**2 >= yu
    v = max(abs(36 - 2*yl), abs(36 - 2*yu))
    w = max(abs(17*yl - 91), abs(17*yu - 91))
    z = max(abs(yl - 6), abs(yu - 6))
    R = 1/(2*rl)
    H = yu**2*(36-yl)**2
    Hp = 2*yu*(36-yl)*v
    Hpp = 2*v**2+4*yu*(36-yl)
    P = yu*(36-yl)*w
    Pp = v*w+17*yu*(36-yl)
    A, Ap = 2*Hp+P, 2*Hpp+Pp
    B, Bp = H/rl, Hp/rl+H/(2*rl**3)
    C, Cp = 12*(11+yu), Q(12)
    D, Dp = ru*z, ru+R*z
    E, Ep = 2*yu, Q(2)
    S = (Ap+A*R+Bp+B*R+Cp*(D+E*ru)
         +C*(Dp+D*R+Ep*ru+E*R))/5
    M = Q(2,5)*(Q(11,10)*A+2*B+C*(2*D+6*E))
    L = Q(2,5)*(Q(11,10)*Ap+2*A*R+2*Bp+4*B*R
                 +Cp*(2*D+6*E)+C*(2*Dp+4*D*R+6*Ep+14*E*R))
    return S,M,L


s4,m4,l4 = bounds(Q(7,2),Q(9,2),Q(3,2),Q(9,4))
s16,m16,l16 = bounds(Q(31,2),Q(33,2),Q(15,4),Q(17,4))
assert (s4,m4,l4)==(Q(31329,5),Q(1030149,40),Q(585099,20))
assert (s16,m16,l16)==(Q(13241447,1875),Q(18701001,200),Q(266744147,7500))
assert Q(4,3)**2<2<Q(3,2)**2
assert Q(20,9)**2<5<Q(9,4)**2
co4=s4+3*l4+3*m4
co16=s16+Q(9,2)*l16+Q(9,5)*m16
assert co4==Q(6851673,40)<172000
assert co16==Q(2515632017,7500)<336000
assert 3100**2 < 10**7
assert Q(6371,60)-Q(172000,3100)>50
assert Q(919,90)-Q(336000*9,4*10**5)>Q(5,2)
for name,val in [("S4",s4),("M4",m4),("L4",l4),("co4",co4),
                 ("S16",s16),("M16",m16),("L16",l16),("co16",co16)]:
    print(name,str(val))
print("ALL_EXACT_RATIONAL_ASSERTIONS_PASSED")
