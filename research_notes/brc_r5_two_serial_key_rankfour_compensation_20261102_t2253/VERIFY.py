#!/usr/bin/env python3
"""Exact rational verifier: two serial BRC continuation gates; auxiliary 4-observer model."""
from fractions import Fraction as F
from itertools import product

A0, AI, BB, BI = F(1, 2), F(2, 3), F(1, 2), F(3, 4)
C = F(2, 3)
B = BB + BI
H0 = (A0 + AI) / 4
ALPHA = (A0, AI, BB, BI)
checks = 0

def ck(assertion):
    global checks
    assert assertion
    checks += 1

def full(x, j_b, j_i, z, t, epsilon):
    b = 1 - j_b
    i = (1 - x) * (1 - j_i)
    w = (F(1, 4), (1-x)/4, b/8, i/8)
    d = (BB*b + BI*i)/8
    gamma = tuple(C*a + (epsilon if s == 2 else 0) for s, a in enumerate(ALPHA))
    r1 = sum((w[s]*ALPHA[s]*z[s] for s in range(4)), F(0))
    r2 = sum((w[s]*gamma[s]*z[s]*t[s] for s in range(4)), F(0))
    return (x, d, r1, r2)

def lr(x, y, z, t, epsilon):
    b, i = y, (1-x)*y
    d = (BB*b + BI*i)/8
    aa = A0/4 + AI*(1-x)/4 + d
    gg = C*aa + epsilon*b/8
    return (x, d, z*aa, z*t*gg)

def normal(epsilon):
    return (C*AI/4 - epsilon*BI/(8*B), -(C + epsilon/B), F(0), F(1))

def dot(a,b):
    return sum((v*w for v,w in zip(a,b)), F(0))

def full_vertices(epsilon):
    for bits in product((F(0),F(1)),repeat=11):
        x,jb,ji=bits[:3]
        yield bits, full(x,jb,ji,bits[3:7],bits[7:11],epsilon)

def lr_vertices(epsilon):
    return [lr(*b,epsilon) for b in product((F(0),F(1)),repeat=4)]

def lift(full_arguments):
    x,jb,ji,zs,ts=full_arguments
    b=1-jb; i=(1-x)*(1-ji)
    d=(BB*b+BI*i)/8
    denom=BB+BI*(1-x)
    y=(BB*b+BI*i)/denom
    aa=A0/4+AI*(1-x)/4+d
    r=full(x,jb,ji,zs,ts,F(0))
    z=r[2]/aa
    t=r[3]/(C*r[2]) if r[2] else F(0)
    return (x,y,z,t)

def bernoulli_mixture(params, vertices):
    vals=[F(0) for _ in range(4)]
    total=F(0)
    nonzero=0
    for index,bits in enumerate(product((F(0),F(1)),repeat=4)):
        weight=F(1)
        for p,bit in zip(params,bits):
            weight*=p if bit else 1-p
        if not weight: continue
        nonzero+=1; total+=weight
        for k in range(4): vals[k]+=weight*vertices[index][k]
    return tuple(vals),total,nonzero

base_lr=lr_vertices(F(0))
ck(len(base_lr)==16)
count=0
max_supports=[]
for bits,obs in full_vertices(F(0)):
    x,jb,ji=bits[:3]
    pars=lift((x,jb,ji,bits[3:7],bits[7:11]))
    ck(all(F(0)<=p<=F(1) for p in pars))
    ck(lr(*pars,F(0))==obs)
    mix,total,nonzero=bernoulli_mixture(pars,base_lr)
    ck(total==1 and mix==obs and 1<=nonzero<=16)
    count+=1
ck(count==2048)

# Exact non-corner lifts: deterministic sample grid, with both serial gates active.
for k in range(1,101):
    x=F(k%7+1,9)
    jb=F(k%5+1,7)
    ji=F(k%6+1,8)
    z=tuple(F((k+2*s)%8+1,10) for s in range(4))
    t=tuple(F((2*k+s)%8+1,10) for s in range(4))
    obs=full(x,jb,ji,z,t,F(0))
    params=lift((x,jb,ji,z,t))
    ck(all(0<=p<=1 for p in params))
    ck(lr(*params,F(0))==obs)
    ck(bernoulli_mixture(params,base_lr)[0]==obs)

# Strictly interior natural branch kernels for every tested epsilon.
for e in (F(0),F(1,96),F(1,32),F(1,12),F(1,8)):
    gammas=[C*a+(e if s==2 else 0) for s,a in enumerate(ALPHA)]
    ck(all(0<a<1 for a in ALPHA))
    ck(all(0<gammas[s]<ALPHA[s] for s in range(4)))
    n=normal(e)
    ls=[dot(n,v) for v in lr_vertices(e)]
    fs=[dot(n,v) for _,v in full_vertices(e)]
    hl,hf=max(ls),max(fs)
    delta=e*BI/(8*B)
    ck(hl==C*H0)
    ck(hf==C*H0+delta)
    ck(hf-hl==delta)
    max_supports.append((str(e),str(hl),str(hf),str(delta)))

# Affine observer rank four: LR (x,y,z,t)->(x,d,r1,r2), interior Jacobian.
x=y=z=t=F(1,2)
dcoef=(BB+BI*(1-x))/8
aa=A0/4+AI*(1-x)/4+dcoef*y
jac=C*dcoef*aa*aa*z
ck(dcoef==F(7,64) and aa==F(101,384) and jac>0)

# Perturbed witness and exact separation norm.
e=F(1,8)
w=full(F(0),F(0),F(1),(F(1),)*4,(F(1),)*4,e)
n=normal(e)
ck(w==(F(0),F(1,16),F(17,48),F(145,576)))
ck(n==(F(293,2880),-F(23,30),F(0),F(1)))
ck(dot(n,w)==F(587,2880))
ck(sum(map(abs,n))==F(5381,2880))
ck((dot(n,w)-C*H0)/sum(map(abs,n))==F(27,5381))
print('PASS_EXACT_R5_TWO_SERIAL_GATE_COMPENSATION_AND_PERTURBATION')
print('strictly_positive_nature_parameters', ALPHA, 'serial_factor', C)
print('FULL_deterministic_vertices', count, 'LR_deterministic_vertices', len(base_lr))
print('verified_exact_assertions', checks)
print('supports_epsilon_lr_full_gap', max_supports)
print('LR_interior_jacobian', jac)
print('witness',w,'normal',n,'directed_Linf_lower_bound',F(27,5381))
