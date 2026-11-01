#!/usr/bin/env python3
"""R451 reproducible exact right-edge certificates (standard-library only)."""
from math import comb, factorial
from hashlib import sha256
from fractions import Fraction

K0, TOP = 14, 26
F = factorial(2*(TOP+2))
EXPECTED = '9949dc5e0815b362e897c462ddf223a360bc6285b3e05135ed32d4d0e90e42af'

def add(*ps):
    z=[0]*max(map(len,ps))
    for p in ps:
        for j,x in enumerate(p):z[j]+=x
    while len(z)>1 and z[-1]==0:z.pop()
    return z

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def prod(*ps):
    z=[1]
    for p in ps:z=mul(z,p)
    return z

def B(s):
    if s<2:return [0]
    terms=[]
    for q in range((s-1)//2+1):
        p=[comb(s-1,2*q)*2**q]
        omit={-(2*t+1) for t in range(q)}
        for a in range(2-s,s+2):
            if a not in omit:p=mul(p,[2*K0+a,2])
        for t in range(q):p=mul(p,[K0+1-t,1])
        terms.append(p)
    return [v*(F//factorial(2*s)) for v in add(*terms)]

def L(s):return Fraction(2**(3*s-2),factorial(2*s))

def leading(s,m):
    if m==2:
        if s==2:return L(2)**2
        z=2*s
        return L(s)**2 * Fraction(2*(2*z+1),(z+1)*(z+2))
    if s==2:return L(2)**3
    if s==3:return Fraction(128,212625)
    z=2*s
    return L(s)**3 * Fraction(16*(8*z**3+24*z*z+10*z+3),(z+1)**2*(z+2)**2*(z+3)*(z+4))

def enc(h,x):
    assert x>0
    b=x.to_bytes(max(1,(x.bit_length()+7)//8),'big')
    h.update(len(b).to_bytes(4,'big'))
    h.update(b)

bs={s:B(s) for s in range(TOP+3)}
h=sha256(); positive=0
for s in range(2,TOP+1):
    a,b,c,d,e=[bs[s+j] for j in (0,-1,1,-2,2)]
    p2=add(prod(a,a),[-v for v in prod(b,c)])
    p3=add(prod(a,a,a),[-2*v for v in prod(a,b,c)],prod(d,c,c),prod(b,b,e),[-v for v in prod(d,a,e)])
    for m,p in ((2,p2),(3,p3)):
        assert len(p)==2*m*s+1 and all(x>0 for x in p),(s,m)
        assert Fraction(p[-1],F**m)==leading(s,m),(s,m,'leading')
        h.update(bytes((s,m)));h.update((len(p)-1).to_bytes(2,'big'))
        for x in p:enc(h,x)
        positive+=len(p)
assert positive==3550
assert h.hexdigest()==EXPECTED,(h.hexdigest(),EXPECTED)

def at(p,u):
    z=0
    for c in reversed(p):z=z*u+c
    return z

def Cat(k):return comb(2*k,k)//(k+1)

def H(k,s):
    if s<2:return 0
    r=2*k+1
    return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*Cat(k-q)
                              for q in range((s-1)//2+1))

def H_raw(k,s):
    if s<2:return 0
    r=2*k+1; diff=r-s
    def C(n,j):return comb(n,j) if 0<=j<=n else 0
    return comb(r+s,2*s)*sum(comb(diff,q)*(C(2*s,r-2*q)-C(2*s,r-2*q-1))
                              for q in range(diff+1))

coeff_checks=raw_checks=minor_checks=0
for k in (14,15,49,100,250):
    ck=Cat(k)
    for s in range(2,TOP+3):
        assert at(bs[s],k-K0)*ck==H(k,s)*F,(k,s,'B')
        coeff_checks+=1
    for s in (2,3,5,13,26,28):
        assert H_raw(k,s)==H(k,s),(k,s,'raw signed')
        raw_checks+=1
    for s in (2,3,10,13,26):
        a,b,c,d,e=[bs[s+j] for j in (0,-1,1,-2,2)]
        p2=add(prod(a,a),[-v for v in prod(b,c)])
        p3=add(prod(a,a,a),[-2*v for v in prod(a,b,c)],prod(d,c,c),prod(b,b,e),[-v for v in prod(d,a,e)])
        x,y,z,w,v=[H(k,s+j) for j in (0,-1,1,-2,2)]
        direct2=x*x-y*z
        direct3=x**3-2*y*x*z+w*z*z+y*y*v-w*x*v
        assert at(p2,k-K0)*ck**2==F**2*direct2
        assert at(p3,k-K0)*ck**3==F**3*direct3
        minor_checks+=2
assert (coeff_checks,raw_checks,minor_checks)==(135,30,50)
print('R451_EXACT_PASS', 'strict positive coefficients:',positive,
      'direct Catalan/raw/minor checks:',coeff_checks,raw_checks,minor_checks,
      'SHA256:',h.hexdigest())
