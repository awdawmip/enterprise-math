#!/usr/bin/env python3
"""Exact rational seventh-root threshold generating function, Q[z]/Phi_7."""
from fractions import Fraction as Q
from functools import lru_cache

class Z:
    __slots__=('a',)
    def __init__(self,a=0):
        if isinstance(a,Z): self.a=a.a; return
        if isinstance(a,(int,Q)): self.a=(Q(a),)+(Q(0),)*5; return
        b=list(map(Q,a)); b=(b+[Q(0)]*7)[:7]
        last=b[6]; self.a=tuple(b[i]-last for i in range(6))
    def __add__(self,other):
        o=Z(other); return Z([self.a[i]+o.a[i] for i in range(6)])
    __radd__=__add__
    def __neg__(self): return Z([-v for v in self.a])
    def __sub__(self,other): return self+-Z(other)
    def __rsub__(self,other): return Z(other)-self
    def __mul__(self,other):
        o=Z(other); c=[Q(0)]*7
        for i,x in enumerate(self.a):
            for j,y in enumerate(o.a): c[(i+j)%7]+=x*y
        return Z(c)
    __rmul__=__mul__
    def __eq__(self,other):return self.a==Z(other).a
    def __repr__(self): return str(self.a)
    def __pow__(self,n):
        assert n>=0
        out=Z(1); p=self
        while n:
            if n&1:out*=p
            p*=p; n//=2
        return out
    def as_json(self):return [str(v) for v in self.a]

one=Z(1);zero=Z(0)
z=Z([0,1])
ZETA=[z**i for i in range(7)]
@lru_cache(None)
def inv1(r):
    r%=7
    assert r
    out= -sum((k*ZETA[(r*k)%7] for k in range(1,7)),zero)*Q(1,7)
    assert out*(one-ZETA[r])==one
    return out

def conv(a,b,M):
    out=[zero]*M
    for i,x in enumerate(a[:M]):
        if x==zero: continue
        for j,y in enumerate(b[:M-i]):
            if y!=zero:out[i+j]=out[i+j]+x*y
    return out

def geom(g,M):
    out=[one]
    for i in range(1,M):out.append(out[-1]*g)
    return out

def F(X,Y,W,M):
    # Weighted triple max identity; coefficients of the exact rational form.
    c0=X*inv1(4)+Y*inv1(5)+W*inv1(next(i for i in range(1,7) if ZETA[i]==W))
    xy=X*Y;xw=X*W;yw=Y*W;xyz=X*Y*W
    omega=[c0]+[-(xy**n+xw**n+yw**n)+(xyz**(n//2) if n%2==0 else zero) for n in range(1,M)]
    num=[one+omega[0]]+[omega[n]-omega[n-1] for n in range(1,M)]
    return conv(conv(conv(num,geom(X,M),M),geom(Y,M),M),geom(W,M),M)

def coefficients(M):
    X=ZETA[4];Y=ZETA[5]
    Fsum=[zero]*M
    for j in (2,3,4):
        W=ZETA[j]
        others=[v for v in (2,3,4) if v!=j]
        cj=inv1((others[0]-j)%7)*inv1((others[1]-j)%7)
        f=F(X,Y,W,M)
        Fsum=[Fsum[n]+cj*f[n] for n in range(M)]
    g=conv(conv(conv(geom(one,M),geom(one,M),M),geom(ZETA[1],M),M),geom(ZETA[6],M),M)
    K=7*inv1(5)*inv1(6)
    return [K*a for a in conv(g,Fsum,M)]

if __name__=='__main__':
 import json
 seq=coefficients(84)
 assert all(seq[n+28]-2*seq[n+14]+seq[n]==zero for n in range(56))
 assert any(seq[n+14]-2*seq[n+7]+seq[n]!=zero for n in range(70))
 table=[]
 for r in range(1,15):
     C=seq[r-1]; B=seq[r+13]-C
     assert seq[r+27]-2*seq[r+13]+C==zero
     c=int(C.a[1]); b=int(B.a[1])
     assert (c>0 and b>=0) or (c<0 and b<=0), (r,c,b)
     table.append({'residue_mod14':r,'z_coefficient_at_k0':c,'increment_per_14':b})
 def trace(x):
     a=list(x.a)+[Q(0)]
     return [int(7*v-sum(a)) for v in a]
 assert trace(seq[0])==[-7,14,7,0,7,-14,-7]
 assert trace(seq[1])==[-21,28,14,35,-7,-21,-28]
 out={'status':'PASS','scope':'frozen_R5_scalar_nonadaptive','n_thresholds_exact_coefficients':84,
      'root':'primitive_7','normalization':'T_m=(7^14 P_7) times primitive-7 pole coefficient = (1-z)*S_m',
      'm1_trace':trace(seq[0]),'m2_trace':trace(seq[1]),
      'periodic_rational_denominator':'(1-t^14)^2','recurrence':'T_(m+28)-2*T_(m+14)+T_m=0 for all m>=1',
      'canonical_z_witness_for_every_threshold':table,
      'nonvanishing':'ALL_POSITIVE_INTEGER_m; exact sign witness of z coefficient with each progression r+14*k',
      'minimal_quasipolynomial_period_of_threshold_coefficient':14,
      'minimal_cost_modulus_for_O_m_N11':420,
      'math_status':'AUTHOR_EXACT_DERIVATION_NOT_INDEPENDENTLY_REVIEWED',
      'frozen_input_sha256':'50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b',
      'coefficients_m1_to_28':[v.as_json() for v in seq[:28]]}
 with open('RESULT.json','w',encoding='utf-8') as f:json.dump(out,f,ensure_ascii=False,indent=2)
 print('PASS: 84 coefficients, 56 recurrence tests, 14 all-m sign witnesses and frozen traces')
 for item in table: print(item)
