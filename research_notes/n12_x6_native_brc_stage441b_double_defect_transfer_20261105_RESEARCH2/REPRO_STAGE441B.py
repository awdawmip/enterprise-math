#!/usr/bin/env python3
"""Exact X6 two-source two-defect quotient, population, and full-future verification.
Run: python REPRO_STAGE441B.py  (Python stdlib, arbitrary-precision integers).
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json

DIRECTIONS = 12  # ±E1,...,±E6; A=0, B=1; remaining labels for APPEND

def require(x, why):
    if not x:
        raise AssertionError(why)


def allowed_sites(L):
    return [x for x in combinations(range(2, L), 2) if x[1] - x[0] > 1]


def make_word(L, defects):
    v = [0] * L
    for i in defects:
        v[i - 1] = 1
    return tuple(v)


def class_key(P, Q, budget):
    L = len(P)
    if budget == (1, 1):
        return (P[L-2], Q[L-2])  # one-based L-1
    if budget == (2, 1):
        return (P[L-3], P[L-2], Q[L-2])  # one-based L-2,L-1;Q L-1
    raise ValueError(budget)


def all_keys(budget, overlap):
    # Exactly these keys have completions for all L>=7.
    if budget == (1, 1):
        if overlap == 0:
            return [(0,0),(0,1),(1,0)]
        if overlap == 1:
            return [(0,0),(0,1),(1,0),(1,1)]
        return [(0,0),(1,1)]
    if overlap == 0:
        return [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(1,0,1)]
    if overlap == 1:
        return [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1)]
    return [(0,0,0),(0,1,1),(1,0,0)]


def forced_symbols(L, budget, key, pos):
    # pos: original 1-based path position, interior 2,...,L-1.
    if budget == (1,1):
        if pos == L - 1:
            return key
    elif budget == (2,1):
        if pos == L - 2:
            return (key[0], None)
        if pos == L - 1:
            return (key[1], key[2])
    return (None,None)


def counter(L, overlap, budget, key):
    """Suffix-counting transfer. Counts original ordered path PAIRS per key exactly."""
    @lru_cache(None)
    def count(pos, np, nq, both, last_p, last_q):
        if pos == L:
            return int(np == 2 and nq == 2 and both == overlap)
        fp, fq = forced_symbols(L, budget, key, pos)
        ans = 0
        for p in (0,1):
            if fp is not None and p != fp: continue
            for q in (0,1):
                if fq is not None and q != fq: continue
                if np+p > 2 or nq+q > 2 or both+p*q > overlap: continue
                if last_p and p or last_q and q: continue
                ans += count(pos+1, np+p, nq+q, both+p*q, p, q)
        return ans
    return count


def unrank_pair(L, overlap, budget, key, index):
    count = counter(L, overlap, budget, key)
    m = count(2,0,0,0,0,0)
    require(0 <= index < m, 'within-class index')
    p_bits = [0]*L
    q_bits = [0]*L
    np=nq=both=lastp=lastq=0
    for pos in range(2, L):
        fp,fq = forced_symbols(L, budget, key, pos)
        chosen=False
        for p in (0,1):
            if fp is not None and p!=fp: continue
            for q in (0,1):
                if fq is not None and q!=fq: continue
                if np+p>2 or nq+q>2 or both+p*q>overlap or lastp and p or lastq and q:continue
                ways=count(pos+1,np+p,nq+q,both+p*q,p,q)
                if index>=ways:
                    index-=ways
                    continue
                p_bits[pos-1],q_bits[pos-1]=p,q
                np,nq,both,lastp,lastq=np+p,nq+q,both+p*q,p,q
                chosen=True
                break
            if chosen:break
        require(chosen,'missing rank branch')
    require(index==0,'rank not consumed')
    return (tuple(p_bits), tuple(q_bits))


def rank_pair(P,Q,overlap,budget,key):
    L=len(P)
    count=counter(L,overlap,budget,key)
    k=0
    np=nq=both=lastp=lastq=0
    for pos in range(2,L):
        p0,q0=P[pos-1],Q[pos-1]
        fp,fq=forced_symbols(L,budget,key,pos)
        require((fp is None or p0==fp) and (fq is None or q0==fq),'not in class')
        for p in (0,1):
            if fp is not None and p!=fp:continue
            for q in (0,1):
                if fq is not None and q!=fq:continue
                if np+p>2 or nq+q>2 or both+p*q>overlap or lastp and p or lastq and q:continue
                if (p,q)>=(p0,q0):break
                k+=count(pos+1,np+p,nq+q,both+p*q,p,q)
            # A later p is lexicographically greater.
            if p>=p0:break
        np,nq,both,lastp,lastq=np+p0,nq+q0,both+p0*q0,p0,q0
    return k


def brute(L, overlap, budget):
    groups=defaultdict(list)
    paths=allowed_sites(L)
    for p in paths:
        P=make_word(L,p)
        for q in paths:
            if len(set(p)&set(q))==overlap:
                Q=make_word(L,q)
                groups[class_key(P,Q,budget)].append((P,Q))
    return groups

@lru_cache(None)
def own_observation(w):
    endpoint=[0]*6
    hist=defaultdict(int)
    for d in w:
        endpoint[d//2]+=1 if d%2==0 else -1
    for x,y in zip(w,w[1:]):
        hist[(x,y)]+=1
    return (len(w),tuple(endpoint),tuple(sorted(hist.items())))

@lru_cache(None)
def observation(P,Q):
    return (own_observation(P),own_observation(Q),sum(p==q for p,q in zip(P,Q)))

num_future_observation_checks=0

def compare_full_future(left,right,budget):
    """Independent raw-path exhaustive future trace comparison; return first separator or None."""
    global num_future_observation_checks
    a,b=budget
    seen=set()
    def go(P,Q,R,S,pp,pq,ap,aq,trace):
        global num_future_observation_checks
        num_future_observation_checks+=1
        O1,O2=observation(P,Q),observation(R,S)
        if O1!=O2:
            return {'operations':list(trace), 'K_left':O1[-1],'K_right':O2[-1]}
        state=(P,Q,R,S,pp,pq,ap,aq)
        if state in seen:return None
        seen.add(state)
        options=[]
        if pp<a and len(P)>1:
            options.append((P[:-1],Q,R[:-1],S,pp+1,pq,ap,aq,'P:POP'))
        if pq<b and len(Q)>1:
            options.append((P,Q[:-1],R,S[:-1],pp,pq+1,ap,aq,'Q:POP'))
        if ap<1:
            for d in range(DIRECTIONS):
                options.append((P+(d,),Q,R+(d,),S,pp,pq,ap+1,aq,'P:APPEND('+str(d)+')'))
        if aq<1:
            for d in range(DIRECTIONS):
                options.append((P,Q+(d,),R,S+(d,),pp,pq,ap,aq+1,'Q:APPEND('+str(d)+')'))
        for p1,q1,r1,s1,x,y,z,t,op in options:
            found=go(p1,q1,r1,s1,x,y,z,t,trace+(op,))
            if found:return found
        return None
    return go(left[0],left[1],right[0],right[1],0,0,0,0,())

def main():
    # Exhaustive population + reconstruction checks across all nonadjacent 2-defect words.
    cases=0
    original_pairs=0
    class_checks=0
    reconstruction_checks=0
    examples=[]
    for L in range(7,16):
        for overlap in (0,1,2):
            for budget in ((1,1),(2,1)):
                groups=brute(L,overlap,budget)
                expected=all_keys(budget,overlap)
                require(sorted(groups)==expected,('support',L,overlap,budget,sorted(groups),expected))
                total=sum(len(v) for v in groups.values())
                for key,histories in groups.items():
                    count=counter(L,overlap,budget,key)
                    m=count(2,0,0,0,0,0)
                    require(m==len(histories),('mass',L,overlap,budget,key,m,len(histories)))
                    class_checks+=1
                    sorted_hist=sorted(histories,key=lambda pair: tuple(zip(pair[0],pair[1])))
                    for idx,(P,Q) in enumerate(sorted_hist):
                        require(unrank_pair(L,overlap,budget,key,idx)==(P,Q),'unrank')
                        require(rank_pair(P,Q,overlap,budget,key)==idx,'rank')
                        reconstruction_checks+=1
                cases+=1
                original_pairs+=total
                if L in (7,10,15):
                    examples.append({'L':L,'overlap':overlap,'budget_PQ_POP':budget,'history_pairs':total,'classes':len(groups),'masses':[len(groups[k]) for k in expected]})
    # Independent future comparison for all histories of the small complete fibers.
    test_scope=[]
    eq_checks=sep_checks=0
    shortest_witness=None
    for L,overlap,budget in [(7,h,b) for h in (0,1,2) for b in ((1,1),(2,1))]:
        groups=brute(L,overlap,budget)
        for group in groups.values():
            for other in group[1:]:
                require(compare_full_future(group[0],other,budget) is None,'false merge')
                eq_checks+=1
        keys=sorted(groups)
        for idx,key in enumerate(keys):
            for next_key in keys[idx+1:]:
                witness=compare_full_future(groups[key][0],groups[next_key][0],budget)
                require(witness is not None,'false split')
                sep_checks+=1
                if (shortest_witness is None or len(witness['operations'])<len(shortest_witness['operations'])):
                    shortest_witness={'L':L,'overlap':overlap,'budget':budget,
                        'key_left':key,'key_right':next_key,
                        'positions_left':[[i+1 for i,z in enumerate(w) if z==1] for w in groups[key][0]],
                        'positions_right':[[i+1 for i,z in enumerate(w) if z==1] for w in groups[next_key][0]],
                        **witness}
        test_scope.append({'L':L,'overlap':overlap,'budget':budget,'within_class_pairs':sum(len(g)-1 for g in groups.values()),'between_class_pairs':len(keys)*(len(keys)-1)//2})
    return {'marker':'STAGE441B_DOUBLE_DEFECT_TRANSFER_AND_QUOTIENT_PASS',
         'L_range':[7,15], 'all_L_overlaps_budgets':cases,
         'original_pair_counts_across_checks':original_pairs,
         'transfer_class_population_checks':class_checks,
         'exact_history_rank_unrank_checks':reconstruction_checks,
         'exhaustive_future_cases':test_scope,
         'full_future_within_class_checks':eq_checks,
         'full_future_separating_witnesses':sep_checks,
         'full_future_observation_prefix_checks':num_future_observation_checks,
         'all_12_signed_append_labels':True,
         'examples':examples,
         'shortest_witness':shortest_witness,
         'arithmetic':'Python exact integers; no floating point',
         'model':'static ordered native-X6 words A=+E1,B=-E1; positive-unit K; all 12 future appended labels'}

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,separators=(',',':')))
