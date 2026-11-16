#!/usr/bin/env python3
"""PREFIX-850 exact pair-trajectory and arithmetic certificates.

Model: p named binary sources, at most one bit flip per heartbeat,
Y_t=2^{floor(t/2)}(S+U(x_t)) mod m_t, and predetermined odd moduli.
After an initial finite time, all width-B moduli have an effective odd part.
This enumerator searches all possible odd effective moduli at given bounds.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
import json

@lru_cache(None)
def domain(p):
    n = 1 << p
    nbr = tuple((1 << x) | sum(1 << (x ^ (1 << i)) for i in range(p)) for x in range(n))
    congr = {q: tuple(sum(1 << y for y in range(n) if (x-y) % q == 0)
                       for x in range(n)) for q in range(1,n,2)}
    return n,nbr,congr

@lru_cache(None)
def next_relation(p, old, q):
    n,nbr,congr=domain(p)
    reached=[]
    for row in old:
        s=0
        while row:
            least=row & -row
            s |= nbr[least.bit_length()-1]
            row ^= least
        reached.append(s)
    out=[]
    for x in range(n):
        before=nbr[x]
        s=0
        while before:
            least=before & -before
            s |= reached[least.bit_length()-1]
            before ^= least
        out.append(s & congr[q][x])
    return tuple(out)

def good_pair(p, q, r):
    _,_,congr=domain(p)
    rel=next_relation(p,congr[q],r)
    return all((row & ~(1 << x)) == 0 for x,row in enumerate(rel))

def check_all_two_words(p,B):
    n,_,_=domain(p)
    qs=range(1,min(n-1,(1<<B)-1)+1,2)
    good=[(q,r) for q,r in product(qs,repeat=2) if good_pair(p,q,r)]
    edges=set(good)
    # w=2 overlap graph uses q as vertex and (q,r) as directed edge.
    vertices=set(x for edge in good for x in edge)
    indeg={v:0 for v in vertices}
    successors=defaultdict(list)
    for q,r in good:
        indeg[r]+=1
        successors[q].append(r)
    ready=[q for q in vertices if indeg[q]==0]
    removed=0
    while ready:
        q=ready.pop(); removed+=1
        for r in successors[q]:
            indeg[r]-=1
            if indeg[r]==0:ready.append(r)
    cycles=sorted((q,r) for q,r in good if (r,q) in edges)
    return {'p':p,'B':B,'candidate_moduli':len(qs),
            'tested_ordered_modulus_pairs':len(qs)**2,'good_two_words':len(good),
            'good_two_word_examples':good[:12],
            'vertices':len(vertices),'acyclic':removed==len(vertices),
            'two_cycle_orientations':len(cycles),'two_cycle_examples':cycles[:12],
            'unique_good_word':good[0] if len(good)==1 else None}

def signed_weight(n):
    """Non-adjacent form weight: minimal number of signed powers of two."""
    n=abs(n); total=0
    while n:
        if n&1:
            digit=1 if n==1 else 2-(n%4)
            n-=digit
            total+=1
        n//=2
    return total

def arithmetic_family(p):
    d=1<<(p-5)
    q=7*d+1; r=12*d-1
    assert p>=8 and q%2==r%2==1 and max(q,r)<=(1<<(p-1))
    # Any distinct final endpoints with equal r-reading: v*r,
    # v=±1,±2. Prior difference u*q, u=-4,...,+4.
    probes=[]
    for u in range(-4,5):
        for v in (-2,-1,1,2):
            change=v*r-u*q
            w=signed_weight(change)
            assert w>=3, ('arithmetic collision',p,u,v,change)
            probes.append(w)
    return {'p':p,'d':d,'first_modulus':q,'second_modulus':r,
            'checked_difference_patterns':len(probes),
            'minimum_signed_binary_weight':min(probes),
            'signed_weight_histogram':dict(sorted(Counter(probes).items()))}

results={
 'schema':'EM_PREFIX850_TWO_HEARTBEAT_EXACT_CERTIFICATE_V1',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'scope':'binary named source updates Hamming<=1, fixed public S, gain 2^floor(t/2), odd moduli, current-state decoding from last two readings without baseline',
 'all_two_word_enumerations':[check_all_two_words(p,B) for p,B in [(6,5),(6,6),(7,6),(7,7),(8,6),(8,7)]],
 'general_constructions':[],
}
for p in (6,7,8,9,10):
    h=1<<(p-1); q=h-7; Q=(1<<p)-1
    assert good_pair(p,q,Q) and good_pair(p,Q,q)
    results['general_constructions'].append({'p':p,'q':q,'Q':Q,'both_cyclic_two_words_good':True})
results['secondary_general_construction']=[arithmetic_family(p) for p in range(8,25)]
assert all(r['two_cycle_orientations']==0 for r in results['all_two_word_enumerations'] if (r['p'],r['B']) in [(6,5),(7,6),(8,6)])
assert all(r['two_cycle_orientations']>0 for r in results['all_two_word_enumerations'] if (r['p'],r['B']) in [(6,6),(7,7),(8,7)])
assert all(good_pair(8,q,r) and good_pair(8,r,q) for q,r in [(57,95)])
results['exact_two_window_widths']={'p6':6,'p7':7,'p8':7}
results['verification']='ALL_EXACT_ASSERTIONS_PASSED'
print(json.dumps(results,indent=2,ensure_ascii=False))
