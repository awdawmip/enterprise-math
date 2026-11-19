#!/usr/bin/env python3
"""Exact Fraction/Bernstein certificate: n=15 K>=j composite minimax phases j=3,4,5,6.
The observer is inherited from BRC16943. No Bellman or native X6 simulation is run.
"""
from fractions import Fraction as Q
from math import comb

BETA=Q(3,637)
ETA=Q(141024,1653649)
U_I=Q(21829245984,45529434409)
U_E=Q(4822040484,8132285009)
# exact (j, enclosing rational width L_j, strict Bernstein lower bound, root bracket / million)
PHASES=[(3,Q(3,50),Q(1,2000),59034,59035),
        (4,Q(123,1000),Q(1,500),121675,121676),
        (5,Q(1,5),Q(1,400),194151,194152),
        (6,Q(7,25),Q(1,200),271729,271731)]

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for k,w in enumerate(b):out[i+k]+=v*w
    return out

def power(a,k):
    out=[Q(1)]
    for _ in range(k):out=mul(out,a)
    return out

def add(a,b,scale=1):
    return [(a[i] if i<len(a) else 0)+scale*(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]

def F_poly(T,j):
    """F_j(T)=P(Bin(15,1-T)<j), in the standard monomial x basis."""
    out=[Q(0)]*31
    one_minus_T=add([Q(1)],T,-1)
    for k in range(j):
        term=mul(power(T,15-k),power(one_minus_T,k))
        for i,val in enumerate(term):out[i]+=comb(15,k)*val
    return out

def J_poly(j):
    te=[Q(1),ETA-1,-ETA]
    ti=[Q(1),-1-BETA,BETA]
    di=add(F_poly(ti,j),F_poly([U_I*a for a in ti],j),-1)
    de=add(F_poly(te,j),F_poly([U_E*a for a in te],j),-1)
    return add(di,de,-1)

def bernstein(a,L):
    n=len(a)-1
    return [sum((a[i]*L**i*Q(comb(k,i),comb(n,i)) for i in range(k+1)),Q(0))
            for k in range(n+1)]

def eval_poly(a,x):
    out=Q(0)
    for v in reversed(a):out=x*out+v
    return out

def T_E(x):return (1-x)*(1+ETA*x)
def T_I(x):return (1-x)*(1-BETA*x)

def F(z,j):return sum((comb(15,k)*(1-z)**k*z**(15-k) for k in range(j)),Q(0))
def D(T,u,j):return F(T,j)-F(T*u,j)
def LR_sign(j,x):
    t=T_E(x)
    return (1-U_E*t)**j*U_E**(15-j)-(1-t)**j

def main():
    assert U_I<U_E<Q(3,5)
    assert LR_sign(2,Q(15172,10**6))>0 and LR_sign(2,Q(15174,10**6))<0
    last_hi=Q(15174,10**6)
    for j,L,bound,lo,hi in PHASES:
        l,r=Q(lo,10**6),Q(hi,10**6)
        assert last_hi<l<r<L
        assert LR_sign(j,l)>0 and LR_sign(j,r)<0
        assert T_I(L)>Q(15-j,14)
        assert U_E<Q(15-j,14)
        a=J_poly(j)
        bs=bernstein(a,L)
        assert len(a)==len(bs)==31
        assert all(b>bound for b in bs)
        assert bs[0]==eval_poly(a,Q(0))
        assert bs[-1]==eval_poly(a,L)
        for x in [Q(0),l,Q((lo+hi),2*10**6),r,L]:
            assert eval_poly(a,x)==D(T_I(x),U_I,j)-D(T_E(x),U_E,j)
        mid=Q((lo+hi),2*10**6)
        risk=(1-D(T_E(mid),U_E,j))/2
        assert 0<risk<Q(1,2)
        print(f'j={j}: PASS, 31/31 Bernstein coefficients > {bound}; x_{j} in ({l},{r});')
        print(f'  lower cert margin exact positive; min approx={float(min(bs)):.14g}; example risk={float(risk):.14g}')
        last_hi=r
    # Especially simple quadratic exact target at j=3.
    target_T3=(1-U_E**4)/(1-U_E**5)
    assert T_E(Q(59034,10**6))>target_T3>T_E(Q(59035,10**6))
    print('PASS all four phases / 124 strictly positive rational Bernstein coefficients')
    print('Scope: AUTHOR_PROVED, EXACT_FRACTION_BERNSTEIN_CHECKED, PARENT_DEPENDENT, NOT_REVIEWED')

if __name__=='__main__':main()
