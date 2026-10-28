#!/usr/bin/env python3
"""Exact two-root-collision P/Q loss-separation checker.
Pure rational arithmetic; external passive statistical tree, not native X6 dynamics.
"""
from fractions import Fraction as F
from itertools import product

f=lambda n,d=1:F(n,d)
# name: ((P_plus,Q_plus),(P_minus,Q_minus))
LEAVES={
  'HA': ((f(9,32),f(1,16)), (f(3,32),f(3,16))),
  'HB': ((f(3,16),f(1,8)),  (f(3,16),f(1,8))),
  'LA': ((f(3,32),f(1,16)), (f(1,32),f(3,16))),
  'LB': ((f(1,16),f(1,8)),  (f(1,16),f(1,8))),
}
ROOTS=tuple(LEAVES)
assert ROOTS==('HA','HB','LA','LB')
P={h:sum(a for a,b in LEAVES[h]) for h in ROOTS}
Q={h:sum(b for a,b in LEAVES[h]) for h in ROOTS}
assert sum(P.values())==sum(Q.values())==1
assert all(a>0 and b>0 for h in ROOTS for a,b in LEAVES[h])
assert [P[h]/Q[h] for h in ROOTS]==[f(3,2),f(3,2),f(1,2),f(1,2)]

# Loss observer O=(e_P,e_Q,T_P,T_Q); declare P => Q-error, declare Q => P-error.
def vec_stop(p,q,label):
    return (p if label=='Q' else f(0), q if label=='P' else f(0),p,q)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def score(O):return O[0]+O[1]+O[2]/8

def root_action(h, act):
    """act 0/1 are stop-and-declare P/Q; 2..5 continue and label plus/minus."""
    if act in (0,1):return vec_stop(P[h],Q[h],'P' if act==0 else 'Q')
    pairs=LEAVES[h]
    labels={2:('P','P'),3:('P','Q'),4:('Q','P'),5:('Q','Q')}[act]
    res=(f(0),f(0),f(0),f(0))
    for (p,q),label in zip(pairs,labels):
        a=vec_stop(p,q,label)
        res=add(res,(a[0],a[1],2*p,2*q))
    return res

all_full={}
for acts in product(range(6),repeat=4):
    O=(f(0),)*4
    for h,a in zip(ROOTS,acts):O=add(O,root_action(h,a))
    all_full[acts]=score(O)
min_full=min(all_full.values())
witness=min(acts for acts,s in all_full.items() if s==min_full)

# LR at t=1 has two signatures 3/2 and 1/2.
# At t=2 same-time ratio signatures are 9/2, 3/2, 1/2, 1/6.
RATIOS=(f(9,2),f(3,2),f(1,2),f(1,6))
assert {p/q for h in ROOTS for p,q in LEAVES[h]}==set(RATIOS)
all_lr={}
for high_action,low_action in product(range(3),repeat=2):
    # 0 stop P, 1 stop Q, 2 continue
    for terminal in product(('P','Q'),repeat=len(RATIOS)):
        labels=dict(zip(RATIOS,terminal));O=(f(0),)*4
        for h in ROOTS:
            act= high_action if h[0]=='H' else low_action
            if act<2:O=add(O,root_action(h,act))
            else:
                for p,q in LEAVES[h]:
                    v=vec_stop(p,q,labels[p/q]);O=add(O,(v[0],v[1],2*p,2*q))
        all_lr[(high_action,low_action,terminal)]=score(O)
min_lr=min(all_lr.values())

# A/B source-specific one-step marginal loss with Bayes terminal labels.
gain={}
for h in ROOTS:
    p,q=P[h],Q[h]
    gain[h]=min(p,q)-sum(min(lp,lq) for lp,lq in LEAVES[h])
assert gain=={'HA':f(3,32),'HB':f(0),'LA':f(1,32),'LB':f(0)}
base=sum(min(P[h],Q[h]) for h in ROOTS)+f(1,8)
assert base==f(7,8)
assert min_full==f(13,16)
assert min_lr==f(7,8)
assert min_lr-min_full==f(1,16)

# Exact triangle law for one class of two equally-weighted sources:
# k = extra time cost per continued source; g = information gain in A.
def delta(g,k):
    return min(f(0),2*k-g)-min(f(0),k-g)-min(f(0),k)
assert delta(f(3,32),f(3,64))==f(3,64)
assert delta(f(1,32),f(1,64))==f(1,64)
assert sum((delta(f(3,32),f(3,64)),delta(f(1,32),f(1,64))))==f(1,16)

# For each class, LR pure endpoints have same score after Bayes terminal optimization.
for pair in (('HA','HB'),('LA','LB')):
    roots=pair
    c_stop=sum(min(P[h],Q[h]) for h in roots)
    c_cont=sum(sum(min(lp,lq) for lp,lq in LEAVES[h])+P[h]/8 for h in roots)
    assert c_stop==c_cont

# Terminal declaration quotient: same (t,r) can be replaced by Q-stop-mass
# weighted average without changing either error coordinate or either time.
# At t=2 r=3/2 occurs at HB+, HB-, LA+; unequal conditional reach weights.
qweights=(f(1,8)*f(1,2),f(1,8)*f(1,2),f(1,16)*f(3,4))
probs=(f(1),f(0),f(1,3))
W=sum(qweights); dbar=sum(q*d for q,d in zip(qweights,probs))/W
assert W==f(11,64) and dbar==f(5,11)
old_err=(sum(f(3,2)*q*(1-d) for q,d in zip(qweights,probs)),sum(q*d for q,d in zip(qweights,probs)))
new_err=(f(3,2)*W*(1-dbar), W*dbar)
assert old_err==new_err==(f(9,64),f(5,64))

# Source-wise marginal advantage at each shared t=1 information set.
D={h:P[h]/8-gain[h] for h in ROOTS}
assert D=={'HA':-f(3,64),'HB':f(3,64),'LA':-f(1,64),'LB':f(1,64)}
for roots in (('HA','HB'),('LA','LB')):
    assert sum(D[h] for h in roots)==0
    # Shared (flat) continue probability can never erase hidden sign disagreement.
    assert -sum(min(f(0),D[h]) for h in roots)==sum(abs(D[h]) for h in roots)/2

print('MODEL: four t=1 roots, eight strictly positive P/Q terminal leaves')
print('P/Q root ratios:', ', '.join(f'{h}={P[h]/Q[h]}' for h in ROOTS))
print('t=2 ratio signatures:', ', '.join(str(r) for r in RATIOS))
print('local Bayes gains:', ', '.join(f'{h}={gain[h]}' for h in ROOTS))
print('full pure policies checked:',len(all_full))
print('LR pure policies checked:',len(all_lr))
print('min full:',min_full,' witness t1/terminal action codes:',witness)
print('min LR:',min_lr)
print('exact separation LR minus full:',min_lr-min_full)
print('both LR collision classes have zero aggregate advantage at gamma=1/8')
print('sourcewise local deltas:', ', '.join(f'{h}={D[h]}' for h in ROOTS))
print('terminal ratio 3/2 fibre collapse: W=',W,' shared label-P probability=',dbar,' errors=',old_err)
print('triangular gaps:',f(3,64),'+',f(1,64),'=',f(1,16))
print('ALL EXACT DOUBLE-COLLISION SIGN-COHERENCE CHECKS PASSED')
