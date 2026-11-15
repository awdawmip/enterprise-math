#!/usr/bin/env python3
"""Independent exact rational validation of the R167 final-horizon alias non-remergence theorem.
External finite binary Sturmian tied-phase signature model; no floating point.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json

@lru_cache(maxsize=None)
def signature(w):
    n=len(w); prefix=[0]
    for c in w: prefix.append(prefix[-1]+int(c))
    low,high=Q(0),Q(1)
    for i in range(n):
        for k in range(i+1,n+1):
            diff=prefix[k]-prefix[i]; d=k-i
            low=max(low,Q(diff-1,d));high=min(high,Q(diff+1,d))
    if low>=high:return None
    A=min(Q(prefix[i])-i*low for i in range(n+1))
    B=max(Q(prefix[i])-i*high for i in range(n+1))
    return low,high,int(low.denominator*(1+A)),int(high.denominator*B)

def collision_pairs(n):
    group=defaultdict(list)
    for k in range(1<<n):
        w=format(k,f'0{n}b');sig=signature(w)
        if sig is not None: group[sig].append(w)
    pairs=[]
    for words in group.values():
        assert len(words)<=2, (n,words)
        if len(words)==2: pairs.append(tuple(words))
    return pairs

def contact_data(u,v):
    a=[0];b=[0]
    for c,d in zip(u,v): a.append(a[-1]+int(c));b.append(b[-1]+int(d))
    idx=[i for i in range(len(a)) if a[i]!=b[i]]
    assert len(idx)==1
    j=idx[0];return j,max(a[j],b[j]),a[-1]

def certify_final_suffix(u,v,z):
    sig=signature(u)
    assert sig is not None and sig==signature(v)
    alpha,beta,_,_=sig
    j,q,N=contact_data(u,v)
    total=N
    for h,bit in enumerate(z,1):
        total+=int(bit)
        t=len(u)+h-j
        if not (q+t*beta-1<=total<=q+t*alpha): return False
    return True

def main():
    mmax=16
    all_pairs=0; aliases_with_prior_alias=0; prior_collisions=0
    violation_examples=[]; all_lengths=[]
    for n in range(2,mmax+1):
        pairs=collision_pairs(n)
        all_pairs+=len(pairs)
        for u,v in pairs:
            j,_,_=contact_data(u,v)
            stages=[]
            for k in range(j+1,n+1):
                a=signature(u[:k]);b=signature(v[:k])
                stages.append(a is not None and a==b)
            seen_alias=False
            for status in stages:
                if status:
                    seen_alias=True
                if seen_alias and not status:
                    violation_examples.append(dict(n=n,u=u,v=v,stages=stages))
            if any(stages[:-1]):aliases_with_prior_alias+=1
            prior_collisions+=sum(stages[:-1])
        all_lengths.append(dict(n=n,pairs=len(pairs)))
    assert not violation_examples, violation_examples[:3]
    initial_pairs=0; all_suffixes=0; final_same=0; predicted_same=0; broken_rejoin=0
    broken_example=None
    for m in range(2,10):
        for u,v in collision_pairs(m):
            initial_pairs+=1
            for length in range(1,7):
                for tailbits in product('01',repeat=length):
                    z=''.join(tailbits)
                    final_a=signature(u+z);final_b=signature(v+z)
                    actual=final_a is not None and final_a==final_b
                    predicted=certify_final_suffix(u,v,z)
                    statuses=[signature(u+z[:k]) is not None and signature(u+z[:k])==signature(v+z[:k]) for k in range(1,length+1)]
                    if any((not statuses[h]) and any(statuses[h+1:]) for h in range(len(statuses)-1)):
                        broken_rejoin+=1;broken_example=(u,v,z,statuses)
                    assert actual==predicted==(all(statuses)),(u,v,z,actual,predicted,statuses)
                    all_suffixes+=1
                    final_same+=actual;predicted_same+=predicted
    assert broken_rejoin==0,broken_example
    return {'marker':'R167_FINAL_ALIAS_NONREMERGENCE_EXACT_PASS',
            'model':'finite-Sturmian tied-phase exact scalar signature (alpha,beta,U,V)',
            'arithmetic':'fractions.Fraction and exact integer loops',
            'candidate_final_words_to_length_16':sum(1<<n for n in range(2,mmax+1)),
            'final_collision_pairs_to_length_16':all_pairs,
            'final_collision_pairs_with_prior_collision':aliases_with_prior_alias,
            'prefix_collision_stages_checked':prior_collisions,
            'prefix_revocation_then_final_recovery':len(violation_examples),
            'initial_collision_pairs_m2_to_m9':initial_pairs,
            'all_suffixes_lengths_1_to_6_checked':all_suffixes,
            'final_alias_suffixes':final_same,
            'interval_certificate_successes':predicted_same,
            'temporary_split_then_rejoin':broken_rejoin,
            'full_pairs_per_length':all_lengths,
            'verification_scope':'exact exhaustive lengths 2..16 and all 1..6 bit common suffixes for all initial collisions lengths 2..9',
            'independent_review':'NOT_REVIEWED'}

if __name__ == '__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
