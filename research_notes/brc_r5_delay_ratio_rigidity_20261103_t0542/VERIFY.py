#!/usr/bin/env python3
"""Exact independent-delay BRC source-flow support / ratio-rigidity regression.
All arithmetic is Python stdlib Fraction; no floating point or numerical LP.
"""
from fractions import Fraction as F
from itertools import product

C = F(2, 3)
ALPHA = (F(1,2), F(2,3), F(1,2), F(3,4))
WEIGHTS = (F(1,8), F(1,6), F(1,16), F(3,32))
W = sum(WEIGHTS)
checks = 0

def eq(x, y):
    global checks
    checks += 1
    assert x == y, (x, y)

def obs(x, b, i, zs, ts, a, beta, p, q):
    w = (F(1,4), (1-x)/4, b/8, i/8)
    Q = tuple(w[s]*ALPHA[s]*zs[s] for s in range(4))
    S = tuple(C*Q[s]*ts[s] for s in range(4))
    d = b/16 + 3*i/32
    return (F(107,128)-21*x/128+d/4-sum(p[s]*S[s] for s in range(4)),
            F(13,64)+3*x/64-d/2+sum(q[s]*S[s]/4 for s in range(4)),
            3+sum(Q)+sum(S)+sum(a[s]*S[s] for s in range(4)),
            3+sum(Q)/2+sum(S)/4+sum(beta[s]*S[s]/4 for s in range(4)))

def vertices(a, beta, p, q):
    full = []
    for x, b, ii in product((F(0), F(1)), repeat=3):
        i = (1-x)*ii
        for choices in product((F(0), F(1)), repeat=8):
            full.append(obs(x, b, i, choices[:4], choices[4:], a, beta, p, q))
    lr = []
    for x, y, z, t in product((F(0), F(1)), repeat=4):
        lr.append(obs(x, y, (1-x)*y, (z,)*4, (t,)*4, a, beta, p, q))
    eq(len(full), 2048)
    eq(len(lr), 16)
    return full, lr

def dot(n, v):
    return sum(n[j]*v[j] for j in range(4))

def full_closed_form(n, a, beta, p, q):
    n0,n1,n2,n3 = n
    k0 = n0*F(107,128)+n1*F(13,64)+3*n2+3*n3
    hx = -n0*F(21,128)+n1*F(3,64)
    hd = n0/4-n1/2
    h1 = n2+n3/2
    ks = tuple(-n0*p[s]+n1*q[s]/4+n2*(1+a[s])+n3*(1+beta[s])/4 for s in range(4))
    L = tuple(max(F(0), h1+C*max(F(0), k)) for k in ks)
    return (k0 + L[0]/8 + max(F(0), (hd+L[2])/16)
            + max(hx, L[1]/6 + max(F(0), 3*(hd+L[3])/32)))

def time_certificate(a, beta):
    rho = tuple((1+beta[s])/(1+a[s]) for s in range(4))
    m, M = min(rho), max(rho)
    if m == M:
        return None
    eps = min((M-m)/2, F(3,14)*(2-m))
    u = m+eps
    k = tuple(1+beta[s]-u*(1+a[s]) for s in range(4))
    h = 2-u
    assert eps>0 and m<u<M and h>0
    assert min(h+C*min(F(0), t) for t in k)>0
    plus = sum(WEIGHTS[s]*max(F(0),k[s]) for s in range(4))
    minus = sum(WEIGHTS[s]*max(F(0),-k[s]) for s in range(4))
    assert plus>0 and minus>0
    base = 12-3*u+h*W
    hfull = base+C*plus
    hlr = base+C*max(F(0),plus-minus)
    eq(hfull-hlr, C*min(plus,minus))
    return (u,hfull,hlr,C*min(plus,minus))

def fvec(vals):
    return tuple(F(v) for v in vals)

cases = [
    ("one_sided_BJ", fvec((F(1,4),)*4), fvec((F(1,4),F(1,4),F(1,2),F(1,4))), fvec((F(1,2),)*4), fvec((F(1,2),)*4)),
    ("mixed_sign", fvec((F(3,8),F(5,8),F(3,8),F(5,8))), fvec((F(5,8),F(3,8),F(5,8),F(3,8))), fvec((F(1,2),)*4), fvec((F(1,2),)*4)),
    ("diagonal_varying", fvec((F(1,4),F(1,2),F(1,4),F(1,2))), fvec((F(1,4),F(1,2),F(1,4),F(1,2))), fvec((F(1,4),F(3,8),F(1,4),F(3,8))), fvec((F(1,4),F(3,8),F(1,4),F(3,8)))),
    ("general_A", fvec((F(1,3),F(2,5),F(1,2),F(1,6))), fvec((F(2,3),F(1,4),F(2,5),F(3,4))), fvec((F(1,4),F(2,3),F(3,5),F(4,7))), fvec((F(3,7),F(2,5),F(1,3),F(5,8)))),
    ("general_B", fvec((F(5,8),F(1,5),F(3,7),F(2,3))), fvec((F(1,5),F(4,5),F(1,4),F(3,4))), fvec((F(1,3),F(1,2),F(1,4),F(2,5))), fvec((F(2,3),F(1,4),F(3,5),F(3,8)))),
]

for name,a,beta,p,q in cases:
    for seq in (a,beta,p,q):
        assert all(F(0)<v<F(1) for v in seq)
    full,lr=vertices(a,beta,p,q)
    tests = ((F(0),F(0),F(-1),F(4)),
             (F(2,3),F(-3,7),F(1,2),F(-5,4)),
             (F(-4,5),F(1,2),F(7,6),F(-2,3)),
             (F(0),F(0),F(5,3),F(-4)))
    cert=time_certificate(a,beta)
    if cert:
        u,hf,hl,gap=cert
        tests += ((F(0),F(0),-u,F(4)),)
    for n in tests:
        Hf=max(dot(n,v) for v in full)
        Hl=max(dot(n,v) for v in lr)
        eq(Hf,full_closed_form(n,a,beta,p,q))
        eq(Hf>=Hl,True)
        if cert and n==(F(0),F(0),-cert[0],F(4)):
            eq(Hf,cert[1]); eq(Hl,cert[2]); eq(Hf-Hl,cert[3])
    print(f"CASE {name} full_corners=2048 lr_corners=16 tilt_gap={cert[3] if cert else 'RATIO_CONSTANT'}")

name,a,beta,p,q=cases[0]
u,Hf,Hl,gap=time_certificate(a,beta)
eq(u,F(11,10)); eq(Hl,F(2913,320)); eq(Hf,F(1093,120)); eq(gap,F(1,192))
WIT=obs(F(0),F(1),F(1),(F(1),)*4,(F(0),F(0),F(1),F(0)),a,beta,p,q)
eq(WIT,(F(41,48),F(25,192),F(7,2),F(311,96)))
n=(F(0),F(0),-u,F(4))
eq(dot(n,WIT),Hf)
full,lr=vertices(a,beta,p,q)
v=(F(0),F(0),F(-1),F(4))
eq(max(dot(v,w) for w in full),max(dot(v,w) for w in lr))
eq(gap/sum(abs(x) for x in n), F(5,4896))
print(f"WITNESS {WIT}; n={n}; FULL={Hf}; LR={Hl}; GAP={gap}; DIST_INF_LOWER={F(5,4896)}")
print(f"PASS_EXACT_R5_PQ_DELAY_RATIO_RIGIDITY assertions={checks}")
