#!/usr/bin/env python3
"""Independent Fraction-only original-matrix reproduction of PREFIX-409 rational witness.
This intentionally does not import the SymPy checker or its transformed-port coefficients.
"""
from fractions import Fraction as F

def C(x=0,y=0):
    return (F(x),F(y))

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def adj(a):return (a[0],-a[1])
def norm(a):return a[0]*a[0]+a[1]*a[1]
def div(a,b):
    z=mul(a,adj(b)); t=norm(b)
    return (z[0]/t,z[1]/t)

def mm_row(row,vec):
    z=C()
    for a,b in zip(row,vec):z=add(z,mul(a,b))
    return z

def solve_3(M,rhs):
    a=[[M[i][j] for j in range(3)]+[rhs[i]] for i in range(3)]
    for p in range(3):
        q=next(i for i in range(p,3) if norm(a[i][p]))
        a[p],a[q]=a[q],a[p]
        pivot=a[p][p]
        a[p]=[div(z,pivot) for z in a[p]]
        for i in range(3):
            if i!=p:
                f=a[i][p]
                a[i]=[sub(a[i][j],mul(f,a[p][j])) for j in range(4)]
    return [a[i][3] for i in range(3)]

A=[
    [C(4),C(4),C(0)],
    [C(0),C(-4),C(4)],
    [C(-5,3),C(0),C(-3,1)],
    [C(-2,-2),C(4,4),C(2,2)],
    [C(-2),C(0),C(5,2)],
]

eta=F(1,10000); beta=F(1,1000000)
x=F(2499,50000000); y=-F(69,500000)
v=C(x,y)
u=C(0,1)
W=[C(1),u,v]
Y=solve_3(A[:3],W)
assert [mm_row(row,Y) for row in A[:3]]==W
ports=[norm(mm_row(row,Y)) for row in A]
i1,i2,i3,i4,i5=ports
cu=norm(add(W[0],W[1])); cv=norm(add(W[0],W[2]))
t=x*x+y*y
h=cv-1
k=i5-F(709,32)
assert i1==i2==cu/2==1
assert i3==t and 0<t<beta
assert 0<h<eta and 0<k<eta
assert i4==37+48*x+8*y+16*t
assert i5==F(709,32)+23*x+F(61,8)*y+F(53,8)*t
kappa_w=41-i4
assert kappa_w>0
assert kappa_w==F(624797596144999,156250000000000)
assert kappa_w<F(4)

# Zero-noise baselines from the raw original A, for both source signs.
for sigma,expect4 in [(1,F(37)),(-1,F(45))]:
    W0=[C(1),C(0,sigma),C(0)]
    Y0=solve_3(A[:3],W0)
    p0=[norm(mm_row(row,Y0)) for row in A]
    assert p0==[F(1),F(1),F(0),expect4,F(709,32)]
    assert norm(add(W0[0],W0[1]))==2
    assert norm(add(W0[0],W0[2]))==1

print('PASS_PREFIX409_INDEPENDENT_FRACTION_ORIGINAL_A_RATIONAL_NOISY_WITNESS')
print('original A exact normalized W:',W)
print('realized Y from exact Gaussian elimination:',Y)
print('exact port observations:',ports)
print('Cu=',cu,'Cv=',cv,'h=',h,'k=',k,'I3=',i3)
print('attained kappa witness:',kappa_w,'decimal=',float(kappa_w))
