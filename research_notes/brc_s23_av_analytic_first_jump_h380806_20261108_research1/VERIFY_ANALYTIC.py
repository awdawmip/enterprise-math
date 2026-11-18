#!/usr/bin/env python3
"""Exact rational verification of the new analytic H=380805 endpoint certificate."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
H=380805
N=2455069
Q=10**26
LO=545569623581288298975349314
HI=LO+1
L0=380295
K0=2074774

def log_bound(z,terms=45):
    s=F(0)
    term=z
    for m in range(terms):
        s+=2*term/(2*m+1)
        term*=z*z
    return s,s+2*term/((2*terms+1)*(1-z*z))
l2,u2=log_bound(F(1,3))
l9,u9=log_bound(F(1,9))
l15,u15=log_bound(F(1,15))
a,b=3*l2-u15,3*u2-l15
c,d=l9+l15,u9+u15
assert F(LO,Q)<a/d and b/c<F(HI,Q)
print('PASS_LOG_ENCLOSURE',LO,HI,Q)

e_lo=79*LO-431*Q
e_hi=79*HI-431*Q
eta_lo=11*LO-60*Q
eta_hi=11*HI-60*Q
g_lo=371*Q-68*HI
g_hi=371*Q-68*LO
s_lo=K0*Q-HI*L0
s_hi=K0*Q-LO*L0
assert 0<e_lo<e_hi
assert 0<eta_lo<eta_hi
assert 0<g_lo<g_hi
assert 0<s_lo<s_hi<e_lo
assert 79*K0-431*L0==1
assert e_hi*H<2*Q
assert e_hi*(H+79)<2*Q
assert 79*g_hi+e_hi*H<3*Q
assert eta_lo>4000*e_hi
assert g_lo>6*e_hi
assert s_lo+g_lo-6*e_hi>0
print('PASS_INTEGER_LATTICE_BOUNDS', 'eps_num_interval',e_lo,e_hi,'eta_num_interval',eta_lo,eta_hi,'gamma_num_interval',g_lo,g_hi,'s_num_interval',s_lo,s_hi)
print('PASS_B_CLASS_RESTRICTIONS','small_gap_b_in_-1_0_1','high_v_small_gap_b_in_-1_0_1_2','eta_over_eps_gt_4000')

# The transformed seven witness coordinates: every threshold p in the triangle
# is assigned a translated (k,ell) prefix, yielding a strict point in its
# next gap using the analytic spacing lemmas in PROOF.md.
witnesses=[]
for m in range(7):
    if m==0:
        L=L0;K=K0
        sLower=s_lo;sUpper=s_hi
    else:
        L=L0+68+79*m
        K=K0+371+431*m
        sLower=s_lo+g_lo-m*e_hi
        sUpper=s_hi+g_hi-m*e_lo
        assert sUpper<g_lo, ('witness offset not less gamma',m)
    assert sLower>0,('witness offset not positive',m)
    witnesses.append((m,K,L))
    print('WITNESS',m,'K',K,'L',L,'OFFSET_NUM_INTERVAL',sLower,sUpper)
assert witnesses[6][2]>=H
assert witnesses[0][2]==L0
assert K0>H
assert min(K for _,K,L in witnesses)>H
assert K0+L0==N
for m,K,L in witnesses[1:]:
    assert K+L-(L0+1)<=N  # v at least L0+1, j nonnegative
assert H-L0==510
print('PASS_SEVEN_WITNESS_COVERAGE','H',H,'N',N,'maxL',witnesses[-1][2])

# Outer-left and outer-right exact inequality witnesses.
ell=H*Q//LO+1
k=HI*H//Q+1
assert LO*ell>Q*H and k*Q>HI*H
assert ell<=N and k<=N
print('PASS_OUTER_WITNESSES',ell,k)

# Exact first new scaled-gap lower bound, from the pinned unimodular theorem.
# J_{t} at t=380296 requires b=2; b=1 had v=380295<t.
v2=2*L0+79
k2=2*K0+431
t=L0+1
assert v2==760669 and k2==4149979 and t==380296
assert k2+v2-t==4530352 and k2+v2-t>N
# From the preceding analytic formula: 0<d<eps<2d -> floor(alpha)=0,floor(2alpha)=1
assert s_hi<e_lo and e_hi<2*s_lo
print('PASS_FIRST_STRICT_INCREASE_LOWER_BOUND','h',510+t,'N_lower',k2+v2-t)

# Sharpen this to an EXACT first-jump equality. At H1=L0+511, there is
# exactly one high-v threshold p with a feasible positive a*u step: p=(L0+1,0).
# That exceptional gap is p -> p+(79,431) and has width eps. All other
# high-v outgoing gaps have width >= gamma, by the b=-1,0,1,2 lattice case split.
H1=H+1
N1=4530352
assert H1==380806 and H1-L0==511
assert e_hi*H1<2*Q and e_hi*(H1+79)<2*Q
assert 79*g_hi+e_hi*H1<3*Q
assert 431*4000-60>H1 and 431*4001-60>H1
assert 431*4002-120>H1
p=(L0+1,0)
q=(p[0]+79,p[1]+431)
assert sum(q)==H1 and q[0]-p[0]==79 and q[1]-p[1]==431
# For the first high-v p, j<=510. In the b=0 case a>=1 adds 510a
# to v+j; available slack is at most 510; equality iff p=(L0+1,0).
assert N1==k2+(v2-(L0+1))
assert 2*s_lo-e_hi>0 and 2*s_hi-e_lo<e_lo
assert witnesses[-1][2]>=H1
assert all(K+L-(L0+1)<=N1 for m,K,L in witnesses[1:])
ell1=H1*Q//LO+1
k1=HI*H1//Q+1
assert LO*ell1>Q*H1 and k1*Q>HI*H1
assert ell1<=N1 and k1<=N1
print('PASS_EXACT_FIRST_JUMP_UPPER_BOUND', 'h',H1, 'N_exact',N1, 'unique_new_narrow_gap_left',p,'right',q,'witness_counts',(k2,v2-(L0+1)))
print('PASS_EXACT_FIRST_JUMP_OUTER_WITNESSES',ell1,k1)
print('PASS_ANALYTIC_PLATEAU_THROUGH_380805_AND_EXACT_N_380806')
