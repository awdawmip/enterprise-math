#!/usr/bin/env python3
"""Exact rational certificate for S23/AV auxiliary observation plateaux 18-19.
All comparisons use integers / Fraction bounds; no floating decision.
"""
from fractions import Fraction as F

Q = 10**26
LO = 545569623581288298975349314
HI = LO + 1
HMAX = 7226984
W0_V, W0_K = 380295, 2074774


def logarithm_bounds(z):
    s = F(0)
    p = z
    for m in range(45):
        s += 2*p/(2*m + 1)
        p *= z*z
    return s, s + 2*p/(91*(1-z*z))


a,b = logarithm_bounds(F(1,3))
c,d = logarithm_bounds(F(1,9))
e,f = logarithm_bounds(F(1,15))
assert F(LO,Q) < (3*a-f)/(d+f)
assert (3*b-e)/(c+e) < F(HI,Q)


def enc(A,B):
    return (A*Q+B*(LO if B>=0 else HI),
            A*Q+B*(HI if B>=0 else LO))

el,eu = enc(-431,79)       # epsilon = 79r-431
tl,tu = enc(-60,11)       # eta     = 11r-60
gl,gu = enc(371,-68)      # gamma   = eta-epsilon
dl,du = enc(W0_K,-W0_V) # d       = K0-r V0
assert 0 < dl < du < el < eu
assert tl > 4800*eu and gl > 6*eu
assert eu*(HMAX+79) < 20*Q
assert 79*60-431*11 == -1

# All differences with 0 < width < epsilon satisfy |b| < 20,
# where b = 79*width-epsilon*delta_v belongs to Z.
small = []
for beta in range(-19,20):
    if beta == 0:
        continue
    floor_lo = abs(beta)*tl//eu
    floor_hi = abs(beta)*tu//el
    assert floor_lo == floor_hi, (beta,floor_lo,floor_hi)
    aa = -floor_lo if beta>0 else floor_lo+1
    dv,dj = 79*aa+11*beta,431*aa+60*beta
    low,high = enc(-dj,dv)
    assert 0 < low < high < el
    cost = max(max(dv,0)+max(dj,0), max(-dv,0)+max(-dj,0))
    if cost <= HMAX:
        small.append((beta,aa,dv,dj,cost,low,high))
assert [s[:5] for s in small] == [
    (-2,9630,760748,4150410,4911158),
    (-1,4815,380374,2075205,2455579),
    (1,-4814,-380295,-2074774,2455069),
    (2,-9629,-760669,-4149979,4910648)]
print('PASS_H19_GLOBAL_SUBEPS_CLASS', HMAX, 'types', len(small),
      'beta_candidates', 38)

witnesses = {}
for i in range(1,20):
    ai = i*dl//eu
    assert ai*eu < i*dl and i*du < (ai+1)*el
    v,k = i*W0_V+79*ai, i*W0_K+431*ai
    low,high = enc(k,-v)
    assert 0 < low < high < el
    witnesses[i] = (ai,v,k,low,high)
assert [witnesses[i][0] for i in range(1,20)] == [
    0,1,1,2,2,3,4,4,5,5,6,7,7,8,8,9,9,10,11]
V7=witnesses[7][1]; V12=witnesses[12][1]; V14=witnesses[14][1]
V17=witnesses[17][1]; V18=witnesses[18][1]; V19=witnesses[19][1]
# At v<=V12, delta7 or delta12 is below ALL sub-epsilon widths.
for i in (7,12):
    assert all(s[5] > witnesses[i][4] for s in small)
# Between V12 and V14, the b=2 gap (width 2d-epsilon)
# cannot originate because its j-decrease exceeds HMAX-v.
assert HMAX-(V12+1)<4149979
# Other sub-epsilon gaps are all wider than delta14.
assert all(s[5]>witnesses[14][4] for s in small if s[0]!=2)
# Above V14, no sub-epsilon gap can originate inside S_HMAX:
for beta,aa,dv,dj,cost,low,high in small:
    if dv<0:
        assert dj<0 and HMAX-(V14+1)<-dj, (beta,dj)
    else:
        assert dv>0 and dj>0 and HMAX-cost<V14+1, (beta,cost)
print('PASS_H19_LOCALIZED_SPACING', 'V7',V7,'V12',V12,'V14',V14,
      'subepsilon_above_V14',0)

# Low blocks valid at BOTH endpoints, measured at their earliest left v.
lowblocks=[(0,V7,7),(V7+1,V12,12),(V12+1,V14,14)]
M18=witnesses[18][2]+V18-(V17+1)
for left,right,i in lowblocks:
    ai,v,k,low,high=witnesses[i]
    assert v>=right and k>HMAX
    assert k+v-left <= M18
    print('PASS_LOW_BLOCK',i,left,right,'max_length',k+v-left)

for i in (18,19):
    ai,v,k,low,high=witnesses[i]
    prev=witnesses[i-1][1]
    Mi=k+v-(prev+1)
    Hi=v+510
    assert Hi<=HMAX and k>HMAX and Mi>k+3498
    start=V14
    for s in range(15,i+1):
        _,vs,ks,s_low,s_high=witnesses[s]
        assert 0<s_low<s_high<el and ks>Hi and vs<=v
        assert ks+vs-(start+1)<=Mi
        start=vs
    assert start==v
    # For each top v>Vi, j<=509; unchanged exact gamma lemma.
    for m in range(1,7):
        L=v+68+79*m
        K=k+371+431*m
        g_low,g_high=enc(K,-L)
        assert 0<g_low and g_high<gl
        if m==6:
            assert L>=Hi
        assert K+L-(v+1)<=Mi
    left=Hi*Q//LO+1
    right=HI*Hi//Q+1
    assert LO*left>Hi*Q and right*Q>HI*Hi
    assert max(left,right)<=Mi
    print('PASS_PLATEAU',i,'h_start',prev+511,'h_end',Hi,
          'N_exact',Mi,'exterior_left',left,'exterior_right',right)
assert HMAX==V19+510
print('PASS_S23_AV_ANALYTIC_PLATEAUX_18_TO_19')
