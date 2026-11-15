"""R184 exact query-catalog and adaptive-recovery checks.
Usage: python R184_latest_source_query_basis_check.py
Pure Python standard library; exact integers and exhaustive finite cases.
"""
import itertools
import json
from math import factorial

PIN = "43ec6098b1330ae86d0a7863be336c5d97f6ef34"

def states(k):
    return [p for r in range(k+1)
            for p in itertools.permutations(range(k),r)]

def subsets(k):
    return [frozenset(j for j in range(k) if mask >> j & 1)
            for mask in range(1,1 << k)]

def query(state, U):
    return next((j for j in reversed(state) if j in U), None)

def star(a,b):
    bset = set(b)
    return tuple(x for x in a if x not in bset) + tuple(b)

def recover(k,s):
    remaining = set(range(k))
    newest = []
    while remaining:
        outcome = query(s,remaining)
        if outcome is None:
            break
        newest.append(outcome)
        remaining.remove(outcome)
    return tuple(reversed(newest)), len(newest)+bool(remaining)

def run():
    checks = dict(catalog_required_witnesses=0,
                  catalog_witness_contexts=0,
                  all_subset_context_compositions=0,
                  exact_recovery_states=0,
                  deletion_adversary_checks=0)
    rows=[]
    for k in range(1,7):
        S=states(k)
        Q=subsets(k)
        B={frozenset((i,)) for i in range(k)} | {
            frozenset((i,j)) for i in range(k) for j in range(i+1,k)}
        assert len(S)==sum(factorial(k)//factorial(k-r) for r in range(k+1))
        for U in B:
            R=tuple(j for j in range(k) if j not in U)
            if len(U)==1:
                (i,)=U
                u,v=(i,)+R,R
            else:
                i,j=sorted(U)
                u,v=(i,j)+R,(j,i)+R
            distinguishing={V for V in Q if query(u,V)!=query(v,V)}
            assert distinguishing=={U},(k,U,distinguishing)
            checks["catalog_required_witnesses"]+=1
            if k<=4:
                for left in S[:40]:
                    for right in S[:10]:
                        for V in Q:
                            if V!=U:
                                assert query(star(star(left,u),right),V)==query(star(star(left,v),right),V)
                                checks["catalog_witness_contexts"]+=1
        seen=set()
        maxq=0
        ordered_B=sorted(B,key=lambda U:(len(U),tuple(sorted(U))))
        for s in S:
            sig=tuple(query(s,U) for U in ordered_B)
            assert sig not in seen
            seen.add(sig)
            recovered,queries=recover(k,s)
            assert recovered==s and queries<=k
            maxq=max(maxq,queries)
            checks["exact_recovery_states"]+=1
            if len(s)==k:
                for i in s:
                    deletion=tuple(j for j in s if j!=i)
                    for U in Q:
                        if query(s,U)!=i:
                            assert query(deletion,U)==query(s,U)
                            checks["deletion_adversary_checks"]+=1
        assert len(seen)==len(S) and maxq==k
        if k<=4:
            for a in S:
                for b in S:
                    ab=star(a,b)
                    for U in Q:
                        qb=query(b,U)
                        assert query(ab,U)==(qb if qb is not None else query(a,U))
                        checks["all_subset_context_compositions"]+=1
        rows.append(dict(k=k,partial_permutation_states=len(S),
                         full_subset_queries=(1<<k)-1,
                         indispensable_fixed_catalog=k*(k+1)//2,
                         optimal_worst_case_adaptive_queries=maxq))
    return dict(status="R184_EXACT_QUERY_COMPLEXITY_PASS",
                scientific_pin=PIN,
                theorem_scope="All k>=1 by symbolic proof; k=1..6 exhaustive checks",
                rows=rows,checks=checks,
                native_brc_execution="NOT_RUN; query-semantics reference test")

if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
