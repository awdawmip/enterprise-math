#!/usr/bin/env python3
"""Exact rational cross-word fiber-discrepancy covariance checks (R149)."""
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm
import random, json

def frac_bounds(word):
    m=len(word); p=[0]
    for bit in word: p.append(p[-1]+bit)
    lo=F(0); hi=F(1)
    for i in range(m):
        for j in range(i+1,m+1):
            lo=max(lo,F(p[j]-p[i]-1,j-i))
            hi=min(hi,F(p[j]-p[i]+1,j-i))
    if lo>=hi: return None
    a,b=lo.numerator,lo.denominator
    c,d=hi.numerator,hi.denominator
    U=min(b*(p[j]+1)-a*j for j in range(m+1))
    V=max(d*p[j]-c*j for j in range(m+1))
    return (a,b,c,d,U,V)

def H(n,s,u,m,t,v):
    g=gcd(n,m); q=F(g-1,2)
    return sum(((s*j+u)%g-q)*((t*j+v)%g-q) for j in range(g))/ (g*n*m)

def epairs(x):
    a,b,c,d,U,V=x
    return ((b,a,-U),(d,-c,V))

def ec(x,L):
    a,b,c,d,U,V=x
    return F(U,b)-F(V,d)-1+F((a*L-U)%b,b)+F((V-c*L)%d,d)

def cov_formula(x,y,h):
    return sum(H(n,s,u,m,t,v+t*h) for n,s,u in epairs(x) for m,t,v in epairs(y))

def direct_cov(x,y,h):
    ns=[z[0] for z in epairs(x)+epairs(y)]
    Q=lcm(*ns)
    xs=[ec(x,L) for L in range(1,Q+1)]
    ys=[ec(y,L+h) for L in range(1,Q+1)]
    xm=sum(xs)/Q;ym=sum(ys)/Q
    return sum((a-xm)*(b-ym) for a,b in zip(xs,ys))/Q

def A(n,k):
    k=k%n
    return F(n*n-1-6*k*(n-k),12*n*n)

def gamma(x,h):
    a,b,c,d,U,V=x
    return H(b,a,-U,d,-c,V-c*h)

def auto_formula(x,h):
    a,b,c,d,U,V=x
    return A(b,a*h)+A(d,-c*h)+gamma(x,h)+gamma(x,-h)

words=[]
for m in range(1,9):
    for bits in product((0,1),repeat=m):
        x=frac_bounds(bits)
        if x is not None: words.append((m,''.join(map(str,bits)),x))
assert len(words)==2+4+8+14+24+36+54+76, len(words)

checks=0
for m,w,x in words:
    for h in range(0,5):
        lhs=direct_cov(x,x,h)
        rhs=auto_formula(x,h)
        assert lhs==rhs,("auto",m,w,h,lhs,rhs)
        assert cov_formula(x,x,h)==rhs
        checks+=1
rng=random.Random(149)
pairs=[]
for i in range(350):
    xx=rng.choice(words)
    yy=rng.choice(words)
    for lag in (-3,0,1,4):
        a=direct_cov(xx[2],yy[2],lag)
        b=cov_formula(xx[2],yy[2],lag)
        assert a==b,(xx,yy,lag,a,b)
        checks+=1
        pairs.append((a,b))
g2_checks=0
zero_sums=0
for n in range(2,18):
    for m in range(2,18):
        g=gcd(n,m)
        if g==1: continue
        s=next(s for s in range(1,n) if gcd(s,n)==1)
        t=next(t for t in range(1,m) if gcd(t,m)==1)
        for u,v in ((0,0),(2,3)):
            vals=[H(n,s,u,m,t,v+t*h) for h in range(g)]
            assert sum(vals)==0
            zero_sums+=1
            if g==2:
                assert vals[1]==-vals[0]
                assert abs(vals[0])==F(1,4*n*m)
                g2_checks+=1

print(json.dumps({'status':'R149_CROSS_WORD_COVARIANCE_PASS',
    'full_sturmian_words_m_1_8':len(words),
    'autocorrelation_tests':5*len(words),
    'cross_word_tests':1400,'total_correlation_checks':checks,
    'gcd_shift_zero_sum_checks':zero_sums,
    'gcd2_sign_alternation_checks':g2_checks,
    'r148b_witness_gamma_lag1':
       str(gamma(frac_bounds(tuple(int(c) for c in '00001000010000')),1))
    },ensure_ascii=False,indent=2))
