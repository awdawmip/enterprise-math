#!/usr/bin/env python3
"""Stage278-B exact finite BRC/count-state observer Markovization witness.

No numpy, simulation, randomness, floating point, or external network.
Finite calculations illustrate independently proved arbitrary-horizon theorem.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

ALPHABET=(0,1,2)
N=3
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
ACTIONS=('P','Q','C')
assert sum(P)==sum(Q)==1

def counts(word):
    return tuple(word.count(i) for i in ALPHABET)

def law_mass(word, law):
    out=F(1)
    for v in word: out*=law[v]
    return out

def orig_decision(h):
    n=len(h)
    if n==0: return {'P':F(0),'Q':F(0),'C':F(1)}
    if n==1:
        c={0:F(3,4),1:F(2,3),2:F(4,5)}[h[0]]
        pshare={0:F(1,3),1:F(1,2),2:F(3,4)}[h[0]]
        return {'P':(1-c)*pshare,'Q':(1-c)*(1-pshare),'C':c}
    if n==2:
        c=F(1,2) if h[0]==h[1] else F(1,3)
        pshare=F(1+(2*h[0]+h[1])%3,4)
        return {'P':(1-c)*pshare,'Q':(1-c)*(1-pshare),'C':c}
    assert n==N
    pshare=F(1+sum(h)%3,4)
    return {'P':pshare,'Q':1-pshare,'C':F(0)}

def rollout(policy):
    reach={(): F(1)}
    M=defaultdict(F)
    W=defaultdict(F)
    leaf=[]
    for n in range(N+1):
        for h in product(ALPHABET,repeat=n):
            r=reach.get(h,F(0))
            if r==0: continue
            acts=policy(h)
            assert all(isinstance(acts[a],F) and acts[a]>=0 for a in ACTIONS)
            assert sum(acts.values())==1
            if n==N: assert acts['C']==0
            s=counts(h)
            W[s]+=r
            for a in ACTIONS: M[(s,a)]+=r*acts[a]
            for a in ('P','Q'):
                if acts[a]: leaf.append((h,a,r*acts[a]))
            if n<N:
                for z in ALPHABET: reach[h+(z,)]=r*acts['C']
    return W,M,leaf

Wo,Mo,leaves_o=rollout(orig_decision)

def bar_decision(h):
    s=counts(h)
    return {a:(Mo[(s,a)]/Wo[s] if Wo[s] else (F(1) if a=='P' else F(0))) for a in ACTIONS}

Wb,Mb,leaves_b=rollout(bar_decision)
assert Wo==Wb, (Wo,Wb)
assert all(Mo[key]==Mb[key] for key in set(Mo)|set(Mb))

def readout(leaves, law):
    result={
        'mass_P':sum((law_mass(h,law)*r for h,a,r in leaves if a=='P'),F(0)),
        'mass_Q':sum((law_mass(h,law)*r for h,a,r in leaves if a=='Q'),F(0)),
        'E_time':sum((len(h)*law_mass(h,law)*r for h,a,r in leaves),F(0)),
        'first_0_then_P':sum((law_mass(h,law)*r for h,a,r in leaves if h and h[0]==0 and a=='P'),F(0)),
    }
    assert result['mass_P']+result['mass_Q']==1
    return result

for label,law in (('P',P),('Q',Q)):
    x=readout(leaves_o,law); y=readout(leaves_b,law)
    assert all(x[k]==y[k] for k in ('mass_P','mass_Q','E_time'))
    assert x['first_0_then_P']!=y['first_0_then_P']
    print(label+' original ',{k:str(v) for k,v in x.items()})
    print(label+' quotient ',{k:str(v) for k,v in y.items()})
    print(label+' loss of ordered observer (original-minus-quotient) =',x['first_0_then_P']-y['first_0_then_P'])
print('N=3 prefix-classes=',len(Wo),'action-class entries=',len(Mo),'reachable full words=',len([x for x in product(ALPHABET,repeat=N)]))
print('All count/action occupancy entries and all four source-error/time observables EXACTLY preserved.')

# Counterexample 1: even with iid sources, native/path-sensitive future operation fails.
# Horizon 2, always continue to depth 2. All words containing 2 declare P.
def original2(h):
    assert len(h)==2
    return 'P' if h not in ((1,0),(1,1)) else 'Q'
def quotient2(h):
    assert len(h)==2
    if counts(h)==(1,1,0):return {'P':F(1,2),'Q':F(1,2)}
    a=original2(h)
    return {'P':F(1) if a=='P' else F(0),'Q':F(1) if a=='Q' else F(0)}
for label,law in (('P',P),('Q',Q)):
    orig_decl_p=sum((law_mass(h,law) for h in product(ALPHABET,repeat=2) if original2(h)=='P'),F(0))
    quo_decl_p=sum((law_mass(h,law)*quotient2(h)['P'] for h in product(ALPHABET,repeat=2)),F(0))
    orig_F=sum((law_mass(h,law) for h in product(ALPHABET,repeat=2) if h[0]==0 and original2(h)=='P'),F(0))
    quo_F=sum((law_mass(h,law)*quotient2(h)['P'] for h in product(ALPHABET,repeat=2) if h[0]==0),F(0))
    assert orig_decl_p==quo_decl_p
    assert orig_F-quo_F==law[0]*law[1]/2
    print('N=2 '+label+' terminal-P mass ',orig_decl_p,'ordered-provenance observer before/after ',orig_F,quo_F)

# Counterexample 2: nonexchangeable sources cannot share a count action kernel
# if their within-fiber conditional word distributions differ.
p_non={'00':F(1,2),'01':F(1,4),'10':F(1,8),'11':F(1,8)}
q_non={'00':F(1,2),'01':F(1,8),'10':F(1,4),'11':F(1,8)}
assert sum(p_non.values())==sum(q_non.values())==1
xP=p_non['01']/(p_non['01']+p_non['10'])
xQ=q_non['01']/(q_non['01']+q_non['10'])
assert xP==F(2,3) and xQ==F(1,3) and xP!=xQ
print('NONIID impossible one shared count-(1,1) P-declare kernel:',xP,'versus',xQ)
print('STAGE278_BRC_COUNT_MARKOVIZATION_EXACT_PASS')