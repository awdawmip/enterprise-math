"""Exact rational witness for strong lumpability necessity, finite N=3 two-law tree.
Standard library only; enumerates every binary prefix and proves finite model facts.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json

N=3
words={t:list(product((0,1), repeat=t)) for t in range(N+1)}

def count(h):
    return (h.count(0),h.count(1))

def state(h):
    return (len(h),count(h))

p3={}
for h in words[3]:
    if h[:2]==(0,1): p0=F(3,4)
    elif h[:2]==(1,0): p0=F(1,4)
    else: p0=F(1,2)
    p3[h]=F(1,4)*(p0 if h[2]==0 else 1-p0)
weights={(3,0):F(2),(2,1):F(1),(1,2):F(1),(0,3):F(1,2)}
Z=sum((p*weights[count(h)] for h,p in p3.items()),F(0))
q3={h:p*weights[count(h)]/Z for h,p in p3.items()}
assert Z==F(17,16)

def prefix_law(terminal):
    return {h:sum((v for w,v in terminal.items() if w[:len(h)]==h),F(0)) for t in range(N+1) for h in words[t]}

P,Q=prefix_law(p3),prefix_law(q3)
assert P[()]==Q[()]==F(1)
assert all(P[h]>0 and Q[h]>0 for h in P)
ratios=defaultdict(set)
for h in P: ratios[state(h)].add(Q[h]/P[h])
assert all(len(vals)==1 for vals in ratios.values())

# Stop at t=2 except continue exactly 01; at t=3 always stop P.
def original(L):
    out=defaultdict(F)
    for h in words[2]:
        if h!=(0,1): out[(2,count(h),'Q')]+=L[h]
    for h in words[3]:
        if h[:2]==(0,1): out[(3,count(h),'P')]+=L[h]
    return dict(out)

# Any compressed policy matching t=2 terminal joint distribution must use these actions;
# t<2 must continue surely; at t=3 stopping is mandatory by support of T.
def compressed(L):
    out=defaultdict(F)
    for h in words[2]:
        x=count(h)
        continue_fraction=F(1,2) if x==(1,1) else F(0)
        out[(2,x,'Q')]+=L[h]*(1-continue_fraction)
        for a in (0,1):
            child=h+(a,)
            prob=L[child]/L[h]
            out[(3,count(child),'P')]+=L[h]*continue_fraction*prob
    return {k:v for k,v in out.items() if v}

O_P,O_Q=original(P),original(Q)
C_P,C_Q=compressed(P),compressed(Q)
assert O_P[(3,(2,1),'P')]==F(3,16)
assert C_P[(3,(2,1),'P')]==F(1,8)
assert O_Q[(3,(2,1),'P')]==F(3,17)
assert C_Q[(3,(2,1),'P')]==F(2,17)
for L,OO,CC in ((P,O_P,C_P),(Q,O_Q,C_Q)):
    assert sum(OO.values(),F(0))==sum(CC.values(),F(0))==F(1)
    for x in {(2,count(h),'Q') for h in words[2]}:
        assert OO.get(x,F(0))==CC.get(x,F(0))
assert P[(0,1)]==P[(1,0)]==F(1,4)
assert Q[(0,1)]==Q[(1,0)]==F(4,17)
assert P[(0,1,0)]/P[(0,1)]==F(3,4)
assert P[(1,0,0)]/P[(1,0)]==F(1,4)
assert Q[(0,1,0)]/Q[(0,1)]==F(3,4)
assert Q[(1,0,0)]/Q[(1,0)]==F(1,4)

def s(v): return str(v)
def distrib(dic): return {str(k):s(v) for k,v in sorted(dic.items())}
result={
  'schema':'EM_BRC_STRONG_LUMPABILITY_NECESSITY_EXACT_V1',
  'model':'binary depth-3 positive non-IID P and count-terminal-tilt Q',
  'P_terminal':{''.join(map(str,h)):s(p) for h,p in sorted(p3.items())},
  'Q_terminal':{''.join(map(str,h)):s(q) for h,q in sorted(q3.items())},
  'Z':s(Z),
  'prefix_count':sum(map(len,words.values())),
  'quotient_states':len(ratios),
  'ratio_constant_in_each_state':all(len(vals)==1 for vals in ratios.values()),
  'P_path_conditional_0_at_01':s(P[(0,1,0)]/P[(0,1)]),
  'P_path_conditional_0_at_10':s(P[(1,0,0)]/P[(1,0)]),
  'Q_path_conditional_0_at_01':s(Q[(0,1,0)]/Q[(0,1)]),
  'Q_path_conditional_0_at_10':s(Q[(1,0,0)]/Q[(1,0)]),
  'P_original':distrib(O_P),'P_forced_compressed':distrib(C_P),
  'Q_original':distrib(O_Q),'Q_forced_compressed':distrib(C_Q),
  'P_discrepancy_at_t3_count21':s(O_P[(3,(2,1),'P')]-C_P[(3,(2,1),'P')]),
  'Q_discrepancy_at_t3_count21':s(O_Q[(3,(2,1),'P')]-C_Q[(3,(2,1),'P')]),
  'all_assertions':'PASS',
}
print(json.dumps(result,ensure_ascii=False,indent=2))
