#!/usr/bin/env python3
"""Direct small-prime Jacobsthal first-moment tests of the CM z=9 condition.
Independent of the Hasse/Legendre coefficient construction and finite-log moment.
Finite scan only; not a proof of all-prime vanishing.
"""
from math import isqrt

def prime(p):
    return p>1 and all(p%d for d in range(2,isqrt(p)+1))

for p in range(11,401):
    if p%8!=3 or not prime(p):
        continue
    # F_(p^2) = F_p[r]/(r^2-2), T=2r/3, B=(1+T)/8.
    inv=[0]*p
    inv[1]=1
    for z in range(2,p):
        inv[z]=-(p//z)*inv[p%z]%p
    leg=[0]*p
    for z in range(1,p):
        leg[z]=1 if pow(z,(p-1)//2,p)==1 else -1
    b0,b1=pow(8,-1,p),pow(12,-1,p)
    sq=[z*z%p for z in range(p)]
    cube=[z*sq[z]%p for z in range(p)]
    trace=0; m0=m1=0; count=0
    for a in range(p):
        for b in range(p):
            u=(cube[a]+6*a*sq[b]+sq[a]+2*sq[b]+b0*a+2*b1*b)%p
            v=(3*sq[a]*b+2*cube[b]+2*a*b+b0*b+b1*a)%p
            n=(u*u-2*v*v)%p
            chi=leg[n]
            trace-=chi
            if n:
                count+=1
                coeff=chi*inv[n]
                m0+=(a*u-2*b*v)*coeff
                m1+=(b*u-a*v)*coeff
    trace_mod=trace%p
    moment=(m0%p,m1%p)
    # 18*T*trace = (0,12*r*trace), as T=2*r/3.
    expected=(0,12*trace_mod%p)
    assert moment==expected,(p,trace,moment,expected)
    assert count==p*p-3
    print(f'p={p} branch={p%24} trace={trace} S={moment} predicted={expected}')
print('PASS_GH125_SMALL_PRIME_MARKED_JACOBSTHAL_MOMENT_UP_TO_400')
