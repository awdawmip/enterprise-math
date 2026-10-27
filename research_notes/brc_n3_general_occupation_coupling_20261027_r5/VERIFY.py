#!/usr/bin/env python3
"""Exact rational audit of the R5 history-to-LR behavioral coupling bound.
Author-side example arithmetic, not a proof of the universal theorem.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
from random import Random

N = 3
S = {'au':F(1,10),'av':F(2,5),'bu':F(1,5),'bv':F(3,10)}
Q = {'':F(1), 'a':F(1,3),'b':F(2,3)}
LR = {'':F(1), 'a':F(2), 'b':F(1,2)}
PARENT = {'a':'','b':''}
CHILDREN = {'':['a','b']}
for z in ['a','b']:
    LR2 = (F(1),F(1),F(7,3) if z=='a' else F(1,3))
    cc=[z+x for x in 'uvw']
    CHILDREN[z]=cc
    for c,l,w in zip(cc,LR2,[F(1,8),F(1,8),F(3,4)]):
        Q[c]=Q[z]*w; LR[c]=l;PARENT[c]=z
for h in ['au','av','bu','bv']:
    cc=[h+k for k in '123']; CHILDREN[h]=cc
    weights=[S[h],F(1)-2*S[h],S[h]]
    for c,l,w in zip(cc,[F(1,2),F(1),F(3,2)],weights):
        Q[c]=Q[h]*w; LR[c]=l; PARENT[c]=h
for h in ['aw','bw']:
    cc=[h+'0'];CHILDREN[h]=cc; c=cc[0]
    Q[c]=Q[h];LR[c]=LR[h];PARENT[c]=h
T={h:len(h) if len(h)<3 else 3 for h in Q}
# The path tokens use length==time (root is time 0).
assert set(CHILDREN)==set(h for h in Q if T[h]<N)
for h,children in CHILDREN.items():
    assert sum((Q[c] for c in children),F(0))==Q[h]
    assert sum((Q[c]*LR[c] for c in children),F(0))==Q[h]*LR[h]
assert sum((Q[h] for h in Q if T[h]==N),F(0))==F(1)
assert sum((Q[h]*LR[h] for h in Q if T[h]==N),F(0))==F(1)
assert all(q>0 and LR[h]>0 for h,q in Q.items())

GROUPS=defaultdict(list)
for h in Q:
    GROUPS[(T[h],LR[h])].append(h)

def trans(h):
    assert h in CHILDREN
    out=defaultdict(F)
    for c in CHILDREN[h]: out[LR[c]]+=Q[c]/Q[h]
    return dict(out)

def tv(p,q):
    return sum((abs(p.get(y,F(0))-q.get(y,F(0))) for y in set(p)|set(q)),F(0))/2

DIAM={}
for g,hh in GROUPS.items():
    if g[0]==N: continue
    DIAM[g]=max([tv(trans(x),trans(y)) for x,y in combinations(hh,2)]+[F(0)])

def main_full_policy():
    actions={}
    for h in Q:
        r=LR[h]
        # Costs: e_P+(3/4)e_Q, so P if r>=3/4, else Q.
        stop=(F(1),F(0),F(0)) if r>=F(3,4) else (F(0),F(1),F(0))
        actions[h]=stop
    actions['']=(F(0),F(0),F(1))
    actions['b']=(F(0),F(0),F(1))
    actions['bv']=(F(0),F(0),F(1))
    return actions

def evaluate(actions):
    alive={'':F(1)}
    flows={}; O=[F(0)]*4
    for t in range(N+1):
        later=defaultdict(F)
        for h in sorted(h for h in Q if T[h]==t):
            z=alive.get(h,F(0));p,q,c=actions[h]
            assert all(isinstance(x,F) and x>=0 for x in (p,q,c)) and p+q+c==1
            assert (t<N) or c==0
            flows[h]=(z,z*p,z*q,z*c)
            O[0]+=z*q*LR[h]
            O[1]+=z*p
            O[2]+=z*(p+q)*LR[h]*t
            O[3]+=z*(p+q)*t
            if c:
                for child in CHILDREN[h]:
                    later[child]+=z*c*Q[child]/Q[h]
        alive=later
    return tuple(O),flows

def avg_seedless(full_flows):
    totals=defaultdict(lambda:[F(0)]*4)
    for h,(alive,stopP,stopQ,cont) in full_flows.items():
        a=totals[T[h],LR[h]]
        for i,v in enumerate((alive,stopP,stopQ,cont)):
            a[i]+=v
    aa={}
    for g,hh in GROUPS.items():
        alive,p,q,c=totals[g]
        if alive:
            aa[g]=(p/alive,q/alive,c/alive)
        else: aa[g]=(F(1),F(0),F(0))
    return {h:aa[(T[h],LR[h])] for h in Q}

def conditional_k(flows,g):
    w=F(0);out=defaultdict(F)
    for h in GROUPS[g]:
        cont=flows[h][3]
        if cont:
            w+=cont
            for y,pr in trans(h).items():out[y]+=cont*pr
    return {y:v/w for y,v in out.items()} if w else {}

def audit(policy, show=False):
    O1,flow1=evaluate(policy)
    policy2=avg_seedless(flow1)
    O2,flow2=evaluate(policy2)
    B=sum((flow1[h][3]*DIAM[T[h],LR[h]] for h in CHILDREN),F(0))
    # Pairwise kernel TV transport bound: evaluated where full has positive continuing mass.
    BC=F(0)
    for g in DIAM:
        m=sum((flow1[h][3] for h in GROUPS[g]),F(0))
        if m:
            k1=conditional_k(flow1,g)
            k2=conditional_k(flow2,g)
            assert k2 # if full mass present and groups share policy, seedless flow is positive
            BC+=m*tv(k1,k2)
    M=max(LR.values()); cap=min(F(1),B); cap2=min(F(1),BC)
    limits=(M*cap,cap,M*N*cap,N*cap)
    limits_ref=(M*cap2,cap2,M*N*cap2,N*cap2)
    assert all(abs(x-y)<=bound for x,y,bound in zip(O1,O2,limits))
    assert all(abs(x-y)<=bound for x,y,bound in zip(O1,O2,limits_ref))
    if show: return O1,O2,B,BC,tuple(x-y for x,y in zip(O2,O1)),limits,limits_ref
    return B,BC

POL=main_full_policy()
O1,O2,B,BC,diff,lim,lim_ref=audit(POL,True)
assert O1 ==(F(43,240),F(19,40),F(17,12),F(7,4))
assert O2 ==(F(17,96),F(23,48),F(17,12),F(7,4))
assert diff ==(F(-1,480),F(1,240),F(0),F(0))
assert B==F(1,20)
assert BC==F(1,120)
assert DIAM[(2,F(1))]==F(3,5)
assert {g:d for g,d in DIAM.items() if d} =={(2,F(1)):F(3,5)}
J=lambda o:o[0]+F(3,4)*o[1]+F(11,200)*o[3]
assert J(O1)==F(379,600)
assert J(O2)-J(O1)==F(1,960)

# All 2^9 full-history binary stop/continue patterns using Bayes actions at stop,
# plus arbitrary rational behavioral-policy draws. The proof itself covers all real probabilities.
internal=sorted(CHILDREN)
for bits in range(1<<len(internal)):
    a={h: ((F(1),F(0),F(0)) if LR[h]>=F(3,4) else (F(0),F(1),F(0))) for h in Q}
    for i,h in enumerate(internal):
        if (bits>>i)&1: a[h]=(F(0),F(0),F(1))
    audit(a)
assert len(internal)==9
rng=Random(2602705)
for _ in range(128):
    a={}
    for h in Q:
        n=[rng.randrange(1,8) for j in range(3 if h in CHILDREN else 2)]
        den=sum(n)
        a[h]=tuple(F(x,den) for x in n)+( (F(0),) if h not in CHILDREN else () )
    audit(a)
print('model_nodes:',len(Q),'positive_terminal_leaves:',sum(T[h]==N for h in Q))
print('nonterminal_nodes:',len(internal),'terminal_QP:',sum(Q[h] for h in Q if T[h]==N),sum(Q[h]*LR[h] for h in Q if T[h]==N))
print('nonzero_diameters:',[(g,str(d)) for g,d in sorted(DIAM.items()) if d])
print('O_full:',tuple(map(str,O1)))
print('O_seedless_occupation_average:',tuple(map(str,O2)))
print('delta_O_seedless_minus_full:',tuple(map(str,diff)))
print('B_diameter:',B,'B_pairwise:',BC)
print('J_full:',J(O1),'J_average:',J(O2),'J_difference:',J(O2)-J(O1))
print('tests: 512 deterministic stop modes and 128 arbitrary rational behavioral full policies PASSED')
print('ALL EXACT CHECKS PASSED')
