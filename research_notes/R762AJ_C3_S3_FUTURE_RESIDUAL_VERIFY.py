#!/usr/bin/env python3
"""R762AJ finite exact tests; standard library; independent word and DP oracles."""
from itertools import product
from collections import defaultdict, deque
from math import factorial
import json
E=(0,1,2)
C=(1,2,0)
CI=(2,0,1)
T=(1,0,2)
GEN={'C+':C,'C-':CI,'X':T}
def mul(g,h):
    return tuple(g[h[i]] for i in range(3))
def inv(g):
    return tuple(g.index(i) for i in range(3))
def typ(g):
    fixed=sum(g[i]==i for i in range(3))
    return 'id' if fixed==3 else ('swap' if fixed==1 else 'cycle')
G={p for p in product(range(3),repeat=3) if len(set(p))==3}
assert len(G)==factorial(3)==6
assert mul(C,CI)==E and mul(T,T)==E and mul(T,mul(C,T))==CI
out={}
for name,alphabet in [('cyclic',{'C+':C,'C-':CI}),('extended',GEN)]:
    reach={E}
    sizes=[]
    for k in range(9):
        oracle=set()
        for letters in product(alphabet.values(),repeat=k):
            x=E
            for g in letters:
                x=mul(g,x)
            oracle.add(x)
        assert reach==oracle, (name,k)
        sizes.append(len(reach))
        reach={mul(g,s) for g in alphabet.values() for s in reach}
    if name=='cyclic':
        assert sizes==[1,2,3,3,3,3,3,3,3]
    else:
        assert sizes==[1,3,5,6,6,6,6,6,6]
    out[name+'_reach_sizes_0_to_8']=sizes
words={E:0}
q=deque([E])
while q:
    g=q.popleft()
    for a in GEN.values():
        z=mul(a,g)
        if z not in words:
            words[z]=words[g]+1
            q.append(z)
assert len(words)==6 and max(words.values())==2
for s in G:
    for u in G:
        sig_s=tuple(typ(mul(g,s)) for g in G)
        sig_u=tuple(typ(mul(g,u)) for g in G)
        assert (sig_s==sig_u)==(s==u)
        if s!=u:
            assert typ(mul(inv(s),s))=='id'
            assert typ(mul(inv(s),u))!='id'
out['max_separating_future_word_length']=max(words.values())
out['distinguished_extended_state_pairs']=15
for g,s in product(G,G):
    assert typ(mul(mul(g,s),inv(g)))==typ(s)
out['conjugation_tests']=len(G)**2
out['current_cycle_types']={k:sum(typ(g)==k for g in G) for k in ['id','swap','cycle']}
weights={'C+':2,'C-':3,'X':5}
hist={E:1}
weight_summary=[]
for k in range(7):
    oracle=defaultdict(int)
    for w in product(tuple(weights),repeat=k):
        x=E
        mass=1
        for symbol in w:
            x=mul(GEN[symbol],x)
            mass*=weights[symbol]
        oracle[x]+=mass
    assert dict(oracle)==hist,(k,dict(oracle),hist)
    assert sum(hist.values())==sum(weights.values())**k
    weight_summary.append({'k':k,'support':len(hist),
        'mass_total':sum(hist.values()),'mass_by_cycle_type':{
            t:sum(v for g,v in hist.items() if typ(g)==t)
            for t in ['id','swap','cycle']}})
    nxt=defaultdict(int)
    for x,v in hist.items():
        for sym,gen in GEN.items():
            nxt[mul(gen,x)]+=v*weights[sym]
    hist=dict(nxt)
out['weighted_BRC_2_3_5_k0_to_6']=weight_summary
out['model_scope']='conditional source permutation algebra; not native TRIADIC_CLOSURE_E admission'
out['verification']='PASS: exhaustive group compositions, all words length<=8, independent weighted history sums length<=6'
print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
