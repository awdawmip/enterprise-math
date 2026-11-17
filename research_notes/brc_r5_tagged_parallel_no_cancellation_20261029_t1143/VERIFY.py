"""Exact rational checks for the R5 tagged-mixture factorization theorem.
Finite arithmetic examples are regression, not the proof of the universal theorem.
"""
from fractions import Fraction as F
from itertools import product

S = (F(1,2), F(1), F(3,2))
ETA = ((F(1,4), F(1,2), F(1,4)),
       (F(1,8), F(3,4), F(1,8)))
Q = (F(1,2), F(1,2))
P = (F(7,20), F(13,20))
W = (F(40,7), F(4), F(0), F(3,8))

# At time 1, each component's two origins have conditional P/Q mass 1/2.
# At time 2, conditional Q terminal row ETA[o], P row ETA[o][k]*S[k].
assert sum(Q) == sum(P) == 1
assert all(sum(e)==1 and sum(x*s for x,s in zip(e,S))==1 and all(x>0 for x in e) for e in ETA)
LR = (P[0]/Q[0], P[1]/Q[1])
assert LR == (F(7,10), F(13,10))
for t in (1,2):
    labels = ((LR[0],), (LR[1],)) if t==1 else (tuple(LR[0]*s for s in S), tuple(LR[1]*s for s in S))
    assert set(labels[0]).isdisjoint(set(labels[1]))

def costs(j,w):
    cp = w[0]*P[j]
    cq = w[1]*Q[j]
    tc = w[2]*P[j]+w[3]*Q[j]
    stopP = cq+tc # declare P: only Q-measure error
    stopQ = cp+tc # declare Q: only P-measure error
    cont = [sum(e*min(cp*s,cq) for e,s in zip(eta,S))+2*tc for eta in ETA]
    return (stopP,stopQ,cont)

def local_support(j,w):
    stopP,stopQ,cont=costs(j,w)
    full=sum((min(stopP,stopQ,cont[o]) for o in range(2)),F(0))/2
    lr=min(stopP,stopQ,(cont[0]+cont[1])/2)
    assert full<=lr
    return full,lr

def gap_via_threshold(j,w):
    stopP,stopQ,cont=costs(j,w)
    stop=min(stopP,stopQ)
    ds=[c-stop for c in cont]
    full=stop+sum((min(F(0),d) for d in ds),F(0))/2
    lr=stop+min(F(0),sum(ds,F(0))/2)
    return full,lr

for j in range(2):
    assert local_support(j,W)==gap_via_threshold(j,W)

f1,l1=local_support(0,W)
f2,l2=local_support(1,W)
assert (f1,l1)==(F(69,32),F(35,16))
assert (f2,l2)==(F(35,16),F(35,16))
assert (f1+f2,l1+l2)==(F(139,32),F(35,8))
assert l1+l2-f1-f2==F(1,32)

# A full-information witness: continue only in component 1, origin A;
# otherwise stop and declare P. Terminal declares Q only at s=1/2.
eP=P[0]/2 * ETA[0][0]*S[0]
eQ=1-Q[0]/2*ETA[0][0]
tP=1+P[0]/2
tQ=1+Q[0]/2
obs=(eP,eQ,tP,tQ)
assert obs==(F(7,320),F(15,16),F(47,40),F(5,4))
assert sum((a*b for a,b in zip(W,obs)), F(0))==F(139,32)
distance=(F(1,32))/sum((abs(x) for x in W),F(0))
assert distance==F(7,2260)

# Exact signed direction regression: all 5^4-1 nonzero integer 4-vectors.
checked=0
positive_gaps=0
for v in product((-2,-1,0,1,2),repeat=4):
    if v==(0,0,0,0): continue
    w=tuple(map(F,v))
    f=sum((local_support(j,w)[0] for j in range(2)),F(0))
    l=sum((local_support(j,w)[1] for j in range(2)),F(0))
    f2_=sum((gap_via_threshold(j,w)[0] for j in range(2)),F(0))
    l2_=sum((gap_via_threshold(j,w)[1] for j in range(2)),F(0))
    assert (f,l)==(f2_,l2_) and l>=f
    assert l-f == sum((local_support(j,w)[1]-local_support(j,w)[0] for j in range(2)),F(0))
    checked+=1
    positive_gaps+=l>f
assert checked==624
print('GLOBAL_MAIN_BOUNDED_INPUT: snapshot separately pinned in RESEARCH.md')
print('conditional Q masses:',Q,'conditional P masses:',P)
print('LR tag multipliers:',LR,'terminal local signatures:',S)
print('eta_A:',ETA[0],'eta_B:',ETA[1])
print('signed witness w:',W)
print('component 1 full/LR min:',f1,l1)
print('component 2 full/LR min:',f2,l2)
print('total full/LR min:',F(139,32),F(35,8))
print('gap:',F(1,32),'witness O:',obs,'L_infinity distance >=',distance)
print('signed direction regression:',checked,'positive gaps:',positive_gaps)
print('PASS_EXACT_R5_TAGGED_MINKOWSKI_NO_CANCELLATION')
