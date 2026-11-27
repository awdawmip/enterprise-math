#!/usr/bin/env python3
"""Exact positive-branch audit for external ternary IID Stage247; stdlib only."""
from fractions import Fraction as F

P = (F(3,24), F(1,24), F(20,24))
Q = (F(2,24), F(2,24), F(20,24))
COUPLING = [((0,0),F(2,24)), ((1,1),F(1,24)), ((2,2),F(20,24)), ((0,1),F(1,24))]
assert sum((w for _,w in COUPLING),F(0)) == 1
for i in range(3):
    assert sum((w for (x,y),w in COUPLING if x==i),F(0)) == P[i]
    assert sum((w for (x,y),w in COUPLING if y==i),F(0)) == Q[i]
assert sum((w for (x,y),w in COUPLING if x!=y),F(0)) == F(1,24)

# A leaf carries the full ordered signal identity, its P/Q branch mass,
# terminal decision and observation count. No likelihood mass is merged
# until after its observables are evaluated.
def dfs_witness(n, w, q):
    leaves = []
    for choice,frac in [('P',1-q),('Q',q)]:
        leaves.append(('time0',choice,0,(1-w)*frac,(1-w)*frac))
    def go(prefix,depth,p_mass,q_mass):
        if depth==n:
            for choice,frac in [('P',1-q),('Q',q)]:
                leaves.append((prefix,choice,depth,p_mass*frac,q_mass*frac))
            return
        for x in range(3):
            newp = p_mass*P[x]
            newq = q_mass*Q[x]
            seq = prefix+str(x)
            if x==0:
                leaves.append((seq,'P',depth+1,newp,newq))
            elif x==1:
                leaves.append((seq,'Q',depth+1,newp,newq))
            else:
                go(seq,depth+1,newp,newq)
    go('',0,w,w)
    assert len(leaves)==2*n+4
    assert all(x>=0 for _,_,_,pp,qq in leaves for x in (pp,qq))
    assert sum((z[3] for z in leaves),F(0))==1
    assert sum((z[4] for z in leaves),F(0))==1
    ep=sum((pp for _,dec,_,pp,qq in leaves if dec=='Q'),F(0))
    eq=sum((qq for _,dec,_,pp,qq in leaves if dec=='P'),F(0))
    tp=sum((depth*pp for _,_,depth,pp,qq in leaves),F(0))
    tq=sum((depth*qq for _,_,depth,pp,qq in leaves),F(0))
    return ep,eq,tp,tq,leaves

def analytic_observers(n,w,q):
    s=w*(1-F(5,6)**n)
    z=(1-s)*q
    return (s/4+z, s/2+1-s-z,6*s,6*s)

def sharp_region(n,a,b):
    r=F(5,6)**n
    return a+b<1 and 4*(1-a-b)<=1-r and 2*a+b>=1 and 2*a+3*b>=2

# An explicit N=14-sharp point, N<=12 obstructed by a strict rational margin.
a,b,n = F(3,10),F(19,40),14
assert sharp_region(14,a,b)
assert not sharp_region(12,a,b)
assert not sharp_region(9,a,b)
s=4*(1-a-b)
r=F(5,6)**n
w=s/(1-r)
q=(a-s/4)/(1-s)
assert (s,w,q)==(F(9,10), F(352638738432,361303242355), F(3,4))
assert 0<=w<=1 and 0<=q<=1
observed=dfs_witness(n,w,q)
expect=(a,b,F(27,5),F(27,5))
assert observed[:4] == analytic_observers(n,w,q) == expect
assert expect[2] == 24*(1-a-b)
assert s-(1-F(5,6)**12) == F(132311957,10883911680)>0
assert (1-r)-s == F(8664503923,391820820480)>0

# Spot-check exact rational boundary cases; universality rests on the proof,
# rather than on this finite test.
for n2 in [1,3,9,12,14]:
    r2=F(5,6)**n2
    for signal in [F(0), (1-r2)/2, 1-r2]:
        for guess_q in [F(0),F(1,3),F(1)]:
            weight=signal/(1-r2) if signal else F(0)
            got=dfs_witness(n2,weight,guess_q)
            assert got[:4]==analytic_observers(n2,weight,guess_q)
            assert got[0]+got[1] == 1-signal/4
            assert got[2] == 24*(1-got[0]-got[1])
print('STAGE247_ASYMMETRIC_EXACT_PASS')
print('model P=',P,'Q=',Q,'tv=',F(1,24))
print('criterion: a+b<1; a+b>=(3+(5/6)^N)/4; 2a+b>=1; 2a+3b>=2')
print('witness N=',n,'a=',a,'b=',b,'s=',s,'activation=',w,'no_signal_guess_Q=',q)
print('observed eP,eQ,tP,tQ=',observed[:4],'ordered_leaves=',len(observed[4]))
for m in [9,12,14]:
    print('N=',m,'max_signal=',1-F(5,6)**m,'cap_sum_threshold=',(3+F(5,6)**m)/4)
print('obstruction_N12_exact=', s-(1-F(5,6)**12))
print('N14_feasibility_margin_exact=',(1-r)-s)
