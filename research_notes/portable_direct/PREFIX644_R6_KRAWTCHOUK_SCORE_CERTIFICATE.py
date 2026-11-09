#!/usr/bin/env python3
"""PREFIX-644: exact rational high-order binomial score and valley-strip implication."""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json

N=189; Pp=Q(96,5); Pz=Q(39,2); R=Q(1040)
z0=Q(19,128); h=Q(3,2**19); h_inner=Q(5,2**20)
Z0,Z1=Q(37,256),Q(39,256)
a=Q(51,400); alpha=Q(8103,65536)

def fall(n,j):
    v=1
    for k in range(j): v*=n-k
    return v

def pmf(n,k,u):
    return comb(n,k)*u**k*(1-u)**(n-k)

def score(n,k,j,u):
    out=Q(0)
    for a_ in range(j+1):
        b=j-a_
        if a_<=k and b<=n-k:
            out+=Q(comb(j,a_)*fall(k,a_)*fall(n-k,b)*(-1)**b,u**a_*(1-u)**b)
    return out

def delta(r,k,j):
    return sum((-1)**(j-b)*comb(j,b)*r[k+b] for b in range(j+1))

nexact=0
for n in range(1,9):
    for u in [Q(2,7),Q(3,8)]:
        r=[Q((3*k+2*n)%7,7) for k in range(n+1)]
        for j in range(1,min(n,4)+1):
            lhs=sum(r[k]*pmf(n,k,u)*score(n,k,j,u) for k in range(n+1))
            rhs=fall(n,j)*sum(delta(r,k,j)*pmf(n-j,k,u) for k in range(n-j+1))
            mean=sum(pmf(n,k,u)*score(n,k,j,u) for k in range(n+1))
            moment=sum(pmf(n,k,u)*score(n,k,j,u)**2 for k in range(n+1))
            assert lhs==rhs and mean==0 and moment==Q(factorial(j)*fall(n,j))/(u*(1-u))**j
            nexact+=3
A=N*Pp; E=N*Pz; B=N*R; C=N*Pp*Pz
D=N*R*Pz; J=Q(N*(N+1),2)*R*Pz
K=2*(J+2*A*C+E*B+197*D)+D/12
tests={
 'first_p':Q(188)<4*Pp**2*a,
 'first_z':Q(188)<4*Pz**2*alpha,
 'second_p':Q(188*187,2)<(R*a)**2,
 'domain':Z0<z0-h<z0+h<Z1,
 'score_sanity':nexact==156,
 'K_exact':K==Q(117867680658,25),
 'K_improved':K<Q(6598084500),
 'A_exact':A==Q(14553,4),
 'C_exact':C==Q(567567,8),
 'D_exact':D==3832920,
 'J_exact':J==364127400,
 'h_ratio':h/Q(1,2**18)==Q(3,2),
 'h_convexity':K*h<27100,
 'wide_mu':C*h<1,
 'wide_fpp':Q(27100)-K*h>122 and Q(48100)+K*h<75078,
 'inner_ratio':h_inner/Q(1,2**18)==Q(5,4),
 'inner_fpp':Q(27100)-K*h_inner>4600 and Q(48100)+K*h_inner<70600,
 'gap_control':Q(322,24*4600)<Q(1,60),
}
assert all(tests.values()),[k for k,v in tests.items() if not v]
res={
 'schema':'PREFIX644_R6_HIGHER_SCORE_V1',
 'date':'2026-11-10',
 'frozen_scientific_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'score_theorem':'|d^j E[r(Bin(n,u))]| <= sqrt(j!(n)_j)/(2[u(1-u)]^(j/2)) for 1<=j<=n; 0<=r<=1',
 'K':str(K),'C':str(C),
 'halfwidth':str(h),'ratio_to_PREFIX643':'3/2',
 'wide_bounds':['273<mu_p<322','122<F_q_pp<75078','unique interior minimizer for every q in [12,24] and z in centered strip'],
 'nested_halfwidth':str(h_inner),
 'nested_bounds':['4600<F_q_pp<70600'],
 'exact_checks':len(tests),'finite_sanity_assertions':nexact,
 'status':'ALL_CHECKS_PASS',
 'review':'AUTHOR_PROVED_ANALYTIC_LEMMA / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED',
 'next':'Certified 2D Bernstein intervals over I×Z'
}
Path(__file__).with_name('PREFIX644_R6_RESULTS.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('ALL_CHECKS_PASS',len(tests),'SCORE_CHECKS',nexact)
print('K',K,'K*h',K*h)
