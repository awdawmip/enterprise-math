#!/usr/bin/env python3
"""Finite symbolic proof of exact A6 recurrence via symmetric-sixth-power closure.
No floating-point mathematics; scalar observer only, not native X6 dynamics.
"""
import sympy as sp
z=sp.Symbol('z')

def th(v):
    out=[sp.expand(z*sp.diff(w,z)-k*w) for k,w in enumerate(v)]
    # theta (f**(6-k) fp**k) = z*(6-k)*V[k+1]+k*V[k-1]-k*V[k]
    for k,w in enumerate(v):
        if k<6: out[k+1]=sp.expand(out[k+1]+z*(6-k)*w)
        if k>0: out[k-1]=sp.expand(out[k-1]+k*w)
    return out

def op(v,p):
    p=sp.Poly(p,sp.Symbol('T'))
    acc=[sp.S.Zero]*7
    w=v
    for n in range(p.degree()+1):
        coeff=p.nth(n)
        acc=[sp.expand(x+coeff*y) for x,y in zip(acc,w)]
        w=th(w)
    return acc

T=sp.Symbol('T')
init=[sp.S.One]+[sp.S.Zero]*6
O7=op(init,T**7)
O5=op(init,-2*(2*T+1)*(14*T**4+28*T**3+28*T**2+14*T+3))
O3=op(init,4*(T+1)*(196*(T+1)**2+59))
O1=op(init,-1152*(2*T+3))
ans=[sp.expand(a+z*b+z**2*c+z**3*d) for a,b,c,d in zip(O7,O5,O3,O1)]
print('7 COMPONENT CERTIFICATE:',ans)
assert ans==[0]*7
print('PASS symbolic all-order A6 recurrence via f(z)=sum z^n/(n!)^2, z f\'\'+f\'=f and F=f^6')
