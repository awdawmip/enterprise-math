#!/usr/bin/env python3
"""R682: exhaustive integer-affine V27 PASS cycle credit certificate.
Self-contained Python 3 standard library; finite combinatorial model only.
"""
from itertools import combinations
from collections import Counter
import json

S = tuple(combinations(range(6), 3))
MATCH = (((0,1),(2,3),(4,5)), ((0,2),(1,4),(3,5)),
         ((0,3),(1,5),(2,4)), ((0,4),(1,3),(2,5)))
EDGES = ((0,1),(1,2),(2,0))
U0 = ((-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),
      (2,4,3,-10),(3,2,4,-10),(4,3,2,-10))
W = (-1,1,-2,-1)
JSETS = tuple(j for n in range(4) for j in combinations(range(3),n))
def code(s,pairs):
    if any(((a in s)+(b in s))!=1 for a,b in pairs): return 0
    return 1 if sum(b in s for a,b in pairs)%2==0 else -1
C = {s:tuple(code(s,p) for p in MATCH) for s in S}
NEI = {s:tuple(t for t in S if len(set(s)&set(t))==2) for s in S}
assert len(S)==20 and len(JSETS)==8 and all(len(x)==9 for x in NEI.values())
assert len(set(C.values()))==20

def compression(m):
    a,b,c=m
    return (a-c,b-a,c-b,0),min(m)
def inverse(d,j):
    x,y,z,q=d
    assert x+y+z==0 and q==0 and j>=0
    v=(0,y,-x)
    t=j-min(v)
    return tuple(t+i for i in v)

def calc(u0,J,s):
    """All nine successor scores as (coefficient of full cycle k, constant)."""
    M=[[0]*4 for _ in range(4)]
    L=[[0]*4 for _ in range(4)]
    u=list(u0)
    for a,b in EDGES: L[a][b]=1
    for e in J:
        a,b=EDGES[e]
        M[a][b]+=1
        u[a]+=1;u[b]-=1
    out={}
    for t in NEI[s]:
        intercept=sum((7*u[i]+W[i])*C[t][i] for i in range(4))
        intercept+=7*sum(C[s][i]*(M[i][j]-M[j][i])*C[t][j]
                         for i in range(4) for j in range(4))
        slope=7*sum(C[s][i]*(L[i][j]-L[j][i])*C[t][j]
                    for i in range(4) for j in range(4))
        out[t]=(slope,intercept)
    return out

def top(a,k):
    best=max(p*k+q for p,q in a.values())
    return tuple(t for t,(p,q) in a.items() if p*k+q==best)

def equal_pair_ever_maximal(a,pair):
    """The two affine functions are identical; solve all k>=0 dominance inequalities."""
    f,g=pair
    p,q=a[f]
    assert a[g]==(p,q)
    lo,hi=0,None
    for t,(r,z) in a.items():
        if t in pair: continue
        d=p-r
        rhs=z-q
        if d>0:
            lo=max(lo,-((-rhs)//d))
        elif d<0:
            ub=rhs//d
            hi=ub if hi is None else min(hi,ub)
        elif rhs>0:
            return False
    return hi is None or lo<=hi

inversions=0
for a in range(9):
    for b in range(9):
        for c in range(9):
            m=(a,b,c)
            assert inverse(*compression(m))==m
            inversions+=1

contexts=pairs=identical=identical_max=0
equalroots=set()
peak=Counter()
witnesses={}
for u0 in U0:
    for j in JSETS:
        for s in S:
            contexts+=1
            a=calc(u0,j,s)
            for (t,(p,q)),(v,(r,z)) in combinations(a.items(),2):
                pairs+=1
                if p==r:
                    if q==z:
                        identical+=1
                        identical_max+=equal_pair_ever_maximal(a,(t,v))
                    continue
                n,d=z-q,p-r
                if n%d or n//d<0: continue
                k=n//d
                equalroots.add(k)
                winners=top(a,k)
                if t in winners and v in winners:
                    peak[k]+=1
                    witnesses.setdefault(k,{'u':u0,'J':''.join('ABC'[x] for x in j),
                                             'S':s,'winners':winners})

assert contexts==960 and pairs==34560 and identical==16 and identical_max==0
assert equalroots==set(range(19))
assert dict(sorted(peak.items()))=={10:2,11:8,12:14,13:14,14:8,15:2}
# Redundant independent 51-round check, including values above all intersection roots.
direct=Counter()
for k in range(51):
    for u0 in U0:
        for j in JSETS:
            for s in S:
                if len(top(calc(u0,j,s),k))>1: direct[k]+=1
assert direct==peak

def word(u0):
    unused=set(range(3))
    u=list(u0); ans=[]
    while unused:
        sc={i:2*(u[EDGES[i][0]]-u[EDGES[i][1]])+
            (W[EDGES[i][0]]-W[EDGES[i][1]]) for i in unused}
        high=max(sc.values())
        best=[i for i in sc if sc[i]==high]
        assert len(best)==1
        e=best[0]
        ans.append(e);unused.remove(e)
        a,b=EDGES[e];u[a]+=1;u[b]-=1
    assert tuple(u)==u0
    return tuple(ans)

def inherit(F,T):
    old=set(F)-set(T)
    new=set(T)-set(F)
    assert len(old)==len(new)==1
    return tuple(next(iter(new)) if x in old else x for x in F)

first=Counter();first_examples=[]
orders={}
for u0 in U0:
    sequence=word(u0)
    orders[','.join(map(str,u0))]=''.join('ABC'[i] for i in sequence)
    for s0 in S:
        F=tuple(s0); halt=None
        for k in range(19):
            for i,e in enumerate(sequence):
                j=tuple(sorted(sequence[:i+1]))
                win=top(calc(u0,j,tuple(sorted(F))),k)
                if len(win)>1:
                    halt=(k,j,tuple(sorted(F)),win)
                    break
                F=inherit(F,win[0])
            if halt is not None: break
        if halt is None:
            first['no_tie_through_18']+=1
        else:
            first[str(halt[0])]+=1
            if len(first_examples)<4:
                first_examples.append({'u':u0,'initial_triad':s0,
                                       'first_k':halt[0],
                                       'partial_events':''.join('ABC'[i] for i in halt[1]),
                                       'current_triad':halt[2],
                                       'tied_successors':halt[3]})
assert list(orders.values())==['CBA','BCA','ABC','BCA','CAB','BAC']
assert first==Counter({'no_tie_through_18':100,'10':10,'11':10})
witness=calc((-2,-4,-3,10),(0,),(2,4,5))
assert witness[(0,2,4)]==(7,-1) and witness[(1,4,5)]==(0,69)
assert (0,2,4) in top(witness,10) and (1,4,5) in top(witness,10)
result={
  'schema':'R682_CYCLE_CREDIT_AFFINE_TIE_EXACT_V1',
  'proof_scope':'Declared three-internal-PASS nonnegative integer model, six baseline biases, 20 triads, 8 partial event subsets, all k>=0',
  'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
  'predecessor':'R681-A+B@7100596fe14a71b5d5543f712dbca9e3d83d0fb8',
  'inversion_checks':inversions,
  'affine_contexts':contexts,'candidate_pairs':pairs,
  'identical_score_functions':identical,
  'identical_pairs_can_be_maximal':identical_max,
  'nonnegative_crossing_roots':sorted(equalroots),
  'highest_tie_counts_by_k':dict(sorted(peak.items())),
  'all_contexts_strict_for_k_0_to_9_and_k_ge_16':True,
  'examples_by_tie_round':witnesses,
  'scheduler_event_orders':orders,
  'bounded_scheduler_first_tie':dict(first),
  'first_tie_witnesses':first_examples,
  'model_limits':'Auxiliary per-cycle capacity; j*=min(M01,M12,M20) is not established as V39 current; not native BRC physics or Driver acceptance.'
}
with open('R682_EVIDENCE.json','w',encoding='utf-8') as f:
    json.dump(result,f,sort_keys=True,indent=2,ensure_ascii=False)
    f.write('\n')
print(json.dumps({k:result[k] for k in ('inversion_checks','affine_contexts',
 'candidate_pairs','identical_score_functions','highest_tie_counts_by_k',
 'bounded_scheduler_first_tie')},ensure_ascii=False,indent=2))
print('R682_CYCLE_CREDIT_AFFINE_TIE_EXACT_PASS')
