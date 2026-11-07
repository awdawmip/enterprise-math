#!/usr/bin/env python3
"""Exact R604 all-k fixed-contour certificate for the auxiliary scalar observer."""
from fractions import Fraction as Q
from math import factorial
K,L,J,M=4096,64,18,16384
A=[Q(24*8**j,factorial(2*j+4)) for j in range(L+2)]
def low_envelope(j):
    E=Q(3*j,2*K)+Q(3*(j+1),2*(2*K-j-1))
    assert 0<=E<1
    return E/(1-E)
C=lambda k:1+21*(k+1)*(2*k+1)
b=lambda j,r:Q((8*r)**j,factorial(2*j))
assert Q(112,132*131)<Q(1,100)
assert Q(112,(2*K+4)*(2*K+3))<Q(1,400)
assert C(K+1)<4*C(K)
medium_tail=24*82*Q(100,99)*b(L+1,14)
high_tail=24*C(K)*Q(100,99)*b(K+1,14)
assert medium_tail<Q(1,10**30) and high_tail<Q(1,10**30)
U={}
for r,limit in ((13,Q(57,1000)),(14,Q(76,1000))):
    u=sum((A[j]*r**j*low_envelope(j) for j in range(L+1)),Q(0))+Q(2,10**30)
    assert 0<u<limit
    U[r]=u
    print('R604_UNIFORM_ALL_K','k_ge',K,'radius',r,
          'coefficient_error_lt',str(limit),'exact_low_terms',L+1)
def cmul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def fj(z):
    w=(Q(0),Q(0))
    for j in range(J,-1,-1):
        w=cmul(w,z)
        w=(w[0]+(-1)**j*A[j],w[1])
    return w
def upper_nodes(r):
    for m in range(M+1):
        t=Q(m,M); den=1+t*t
        yield fj((r*(1-t*t)/den,r*2*t/den))
    for m in range(M-1,-1,-1):
        t=Q(m,M); den=1+t*t
        yield fj((-r*(1-t*t)/den,r*2*t/den))
for r,floor in ((13,Q(69,1000)),(14,Q(96,1000))):
    T=A[J+1]*r**(J+1)/(1-Q(8*r,(2*J+6)*(2*J+5)))
    D=sum((j*A[j]*r**(j-1) for j in range(1,J+1)),Q(0))
    arc=T+2*r*D/M
    top=list(upper_nodes(r))
    assert len(top)==2*M+1
    nearest=min(w[0]*w[0]+w[1]*w[1] for w in top)
    assert nearest>floor**2
    assert arc+U[r]<floor
    print('R604_CONTOUR_CERT','radius',r,'M',M,'nodes',4*M,
          'node_mod_gt',str(floor),'arc_plus_uniform_error_lt',str(floor),
          'reference_F_zero_count',2)
assert Q(76,1000)<Q(81,784)
assert (43*Q(25,36))**2<64*14
assert (42*Q(56,81))**2>64*13
print('R604_UNIFORM_K_GE_4096_TWO_CONTOURS_PASS')
