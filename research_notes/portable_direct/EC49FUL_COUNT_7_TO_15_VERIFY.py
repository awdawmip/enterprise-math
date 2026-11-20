#!/usr/bin/env python3
"""EC49FUL: exact standard-library certificate for count thresholds 7..15.
Model/input: frozen BRC16943 / EC49FUK, commit 136595d2efef0da4a17924f94c58a1982e182285.
Proof status AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.
"""
from fractions import Fraction as Q
from math import comb

BETA=Q(3,637); ETA=Q(141024,1653649)
UI=Q(21829245984,45529434409); UE=Q(4822040484,8132285009)
# Each pair strictly encloses root of endpoint LR(j,x)=1; endpoints / 1e6.
BR={6:(271729,271731),7:(351933,351935),8:(433404,433407),
    9:(515356,515360),10:(597317,597321),11:(678992,678996),
    12:(760196,760200),13:(840810,840814),14:(920760,920764)}
MARGINS={7:Q(18,1000),8:Q(23,1000),9:Q(29,1000),
         10:Q(33,1000),11:Q(37,1000),12:Q(38,1000)}
C=Q(21829245984); H=Q(45529434409); B=Q(-456083905)
UPI=-C*B/H**2

def te(x): return (1-x)*(1+ETA*x)
def ti(x): return (1-x)*(1-BETA*x)
def lr(j,x):
    t=te(x); return (1-UE*t)**j*UE**(15-j)-(1-t)**j

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for k,w in enumerate(b):
                if w: out[i+k]+=v*w
    return out

def power(a,k):
    out=[Q(1)]
    for _ in range(k): out=mul(out,a)
    return out

def sub(a,b):
    return [(a[i] if i<len(a) else Q(0))-(b[i] if i<len(b) else Q(0))
            for i in range(max(len(a),len(b)))]

def fpoly(t,j):
    out=[Q(0)]*31
    for k in range(j):
        term=mul(power(t,15-k),power(sub([Q(1)],t),k))
        for i,v in enumerate(term): out[i]+=comb(15,k)*v
    return out

def jpoly(j):
    e=[Q(1),ETA-1,-ETA]; i=[Q(1),-1-BETA,BETA]
    return sub(sub(fpoly(i,j),fpoly([UI*a for a in i],j)),
               sub(fpoly(e,j),fpoly([UE*a for a in e],j)))

def interval_bernstein(p,lo,hi):
    # x=lo+(hi-lo)*y; degree n Bernstein on y in [0,1].
    n=len(p)-1; d=hi-lo; q=[Q(0)]*(n+1)
    for i,v in enumerate(p):
        if v:
            for k in range(i+1): q[k]+=v*comb(i,k)*lo**(i-k)*d**k
    return [sum((q[i]*Q(comb(k,i),comb(n,i)) for i in range(k+1)),Q(0))
            for k in range(n+1)]

def f(z,j):return sum((comb(15,k)*(1-z)**k*z**(15-k) for k in range(j)),Q(0))
def d(t,u,j):return f(t,j)-f(t*u,j)
def val(p,x):
    z=Q(0)
    for a in reversed(p): z=x*z+a
    return z

def q_endpoint(x): return (1-UE*te(x))/(1-te(x))
def q_independent_lower(x): return (1-UE*ti(x))/(1-ti(x))
def a_lower(x): return UI+UPI*(1/(BETA*x)-1)

def main():
    assert UI==C/H and 0<UI<UE<1 and B<0 and UPI>0
    # Endpoint Bayes likelihood-ratio switch checks for j=7..14.
    for j in range(6,15):
        l,r=(Q(v,10**6) for v in BR[j])
        assert 0<l<r<1 and lr(j,l)>0 and lr(j,r)<0,(j,'switch')
        if j>6: assert Q(BR[j-1][1],10**6)<l,(j,'ordered')
    # On each j=7..12 phase, exact concavity in theta and endpoint gap.
    total=0
    for j in range(7,13):
        lo=Q(BR[j-1][0],10**6); hi=Q(BR[j][1],10**6)
        cut=Q(15-j,14)
        assert ti(hi)>cut and UE*te(lo)<cut,(j,'concavity domains')
        p=jpoly(j); bs=interval_bernstein(p,lo,hi)
        assert len(p)==len(bs)==31
        assert all(b>MARGINS[j] for b in bs),(j,'Bernstein')
        for x in (lo,(lo+hi)/2,hi):
            assert val(p,x)==d(ti(x),UI,j)-d(te(x),UE,j),(j,'identity')
        total+=len(bs)
        print('j',j,'PASS:',len(bs),'positive Bernstein coefficients, lower bound',MARGINS[j],
              'minimum approx',float(min(bs)))
    # For j=13, log-ratio R=F_j'(S)S'/[F_j'(T)T'] >1,
    # hence D_j'(theta)<0. First show Q=(1-uT)/(1-T) decreases in theta.
    a=Q(BR[12][0],10**6); b=Q(BR[13][1],10**6)
    assert a>Q(1,2)
    # Numerator Q_theta = ((1-u)t1-u' T(1-T))/(1-T)^2.
    # Bound t1<=beta*a*(1-a), u'>=UPI, T>=ti(b), 1-T>=1-te(a).
    assert UPI*ti(b)*(1-te(a)) > (1-UI)*BETA*a*(1-a)
    # Q_theta<0; Q decreases x, so Q>=Q_E(b).
    r13=UI**2*q_endpoint(b)**12*a_lower(b)
    assert r13>1
    print('j 13 PASS: R lower bound >1, approx',float(r13))
    # For j=14 use independent conservative bounds u>=UI, T>=ti(b), u<=UE.
    b=Q(BR[14][1],10**6)
    r14=UI*q_independent_lower(b)**13*a_lower(b)
    assert r14>1
    print('j 14 PASS: R lower bound >1, approx',float(r14))
    # For j=15 entire [x14,1): Q>=1 and u^(15-j)=1.
    r15=a_lower(Q(1))
    assert r15>1
    print('j 15 PASS: R lower bound >1, approx',float(r15))
    print('PASS: 9 phases j=7..15, exact LR roots,',total,
          'positive Bernstein inequalities; all other rational bounds exact.')
    print('Validation: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED')

if __name__=='__main__': main()
