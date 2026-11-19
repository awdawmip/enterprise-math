#!/usr/bin/env python3
"""Exact-rational conditional law / monotone-coupling regressions for EC49FTM."""
from fractions import Fraction as Q
import json
M0,M1,M2,M3=Q(11457,512),Q(1461,64),Q(1469,64),Q(187,8)
TOP=Q(3,4)
C=Q(131072,945)
def za(m): return (4*m+2647)/3696
def zb0(m): return (8*m+173)/480
def zb1(m): return (64*m+1411)/3840
def gapline(m): return Q(0) if m<M2 else Q(64,25515)*(64*m-1055)
def bounds(m):
    if M0<=m<=M1: return za(m),zb1(m)
    if M1<m<=M2: return zb0(m),zb1(m)
    if M2<m<=M3: return zb0(m),TOP
    raise ValueError('outside support')
def fm(m):
    if M0<m<M1:return Q(512,121275)*(512*m-11457)
    if M1<=m<M2:return Q(512,525)
    if M2<=m<M3:return (6555968-274432*m)/127575
    raise ValueError('use open support')
def q(m):
    lo,hi=bounds(m)
    return gapline(m)/fm(m)
def q_cond(m,t):
    lo,hi=bounds(m)
    w=1-q(m)
    return lo+(hi-lo)*t/w if t<=w else TOP
for low,high in ((M0,M1),(M1,M2),(M2,M3)):
    for k in range(1,100):
        m=low+(high-low)*Q(k,100)
        lo,hi=bounds(m)
        assert M0<m<M3 and lo<hi<=TOP
        assert fm(m)==C*(hi-lo)+gapline(m)
        if m<M2:assert q(m)==0
        else:assert q(m)==5*(64*m-1055)/(102437-4288*m)
samples=sorted(set(low+(high-low)*Q(k,100) for low,high in ((M0,M1),(M1,M2),(M2,M3)) for k in range(1,100)))
for k in range(41):
    t=Q(k,40)
    seq=[q_cond(m,t) for m in samples]
    assert all(x<=y for x,y in zip(seq,seq[1:])),(k,t)
assert za(M1)==zb0(M1)==Q(569,768)
assert zb1(M2)==TOP
assert za(M0)==zb1(M0)==Q(4549,6144)
assert zb0(M3)==TOP
assert Q(5)*(64*M2-1055)/(102437-4288*M2)==Q(115,223)
assert Q(5)*(64*M3-1055)/(102437-4288*M3)==1
jump=Q(115,223)*(TOP-zb0(M2))/2
assert jump==Q(207,114176)
assert 5*(64*102437-4288*1055)==10160640
result={
 'schema':'EC49FTM_CONDITIONAL_LAW_EXACT_V1',
 'm_breaks':['11457/512','1461/64','1469/64','187/8'],
 'conditional_uniform_interval_1':['(4*m+2647)/3696','(64*m+1411)/3840'],
 'conditional_uniform_interval_2':['(8*m+173)/480','(64*m+1411)/3840'],
 'conditional_uniform_interval_3':['(8*m+173)/480','3/4'],
 'boundary_atom_weight_3':'5*(64*m-1055)/(102437-4288*m)',
 'right_hand_atom_weight_at_m2':'115/223',
 'atom_weight_limit_at_m3':'1/1',
 'conditional_mean_upward_jump_at_m2':'207/114176',
 'analytical_result':'first-order stochastic monotonicity of Z conditioned on M=m',
 'regression':'297 exact marginal-density identities and 41x297 monotone quantile checks',
 'status':'AUTHOR_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED'}
print(json.dumps(result,indent=2))
