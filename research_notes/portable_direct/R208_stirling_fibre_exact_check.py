#!/usr/bin/env python3
"""R208: exact source-order fibres, arbitrary tail depth, Stirling pattern checks."""
from collections import defaultdict
from itertools import permutations, product
from math import perm
import json


def S(n, r):
    if r < 0 or r > n: return 0
    if n == 0: return int(r == 0)
    x = [[0] * (n + 1) for _ in range(n + 1)]
    x[0][0] = 1
    for a in range(1,n+1):
        for b in range(1,a+1):
            x[a][b] = x[a-1][b-1] + b*x[a-1][b]
    return x[n][r]


def N(k): return sum(perm(k,r) for r in range(k+1))


def fibre_formula(m,r,L):
    full=m**L * sum(S(L+1,j+1) for j in range(min(r,L)+1))
    short=sum(m**h*S(h+1,r+1) for h in range(L))
    return full+short


def global_formula(m,k,L):
    a=m*(k+1)
    return sum(a**h for h in range(L)) +sum(perm(k,j)*(a-j*m)**L for j in range(k+1))


def order_product(s,t):
    for x in t:
        if x>=0:
            s=tuple(y for y in s if y!=x)+(x,)
    return s


def orders(k):
    return [s for r in range(k+1) for s in permutations(range(k),r)]


def enumerate_provenance(k,L):
    prefix=orders(k)
    full=defaultdict(set)
    alphabet=tuple(range(-1,k))
    for w in product(alphabet,repeat=L):
        for s in prefix:
            full[order_product(s,w)].add(w)
    short=defaultdict(lambda:defaultdict(set))
    for h in range(L):
        for w in product(alphabet,repeat=h):
            short[order_product((),w)][h].add(w)
    return prefix,full,short


def check(k,L):
    prefix,full,short=enumerate_provenance(k,L)
    for s in prefix:
        r=len(s)
        assert len(full[s])==sum(S(L+1,j+1) for j in range(min(r,L)+1)), (k,L,s,len(full[s]))
        for h in range(L):
            assert len(short[s][h])==S(h+1,r+1), (k,L,s,h,len(short[s][h]))
    for m in [1,2,3,4,12]:
        a=sum(fibre_formula(m,len(s),L) for s in prefix)
        b=global_formula(m,k,L)
        assert a==b,(k,L,m,a,b)
    return {"k":k,"L":L,"source_orders":len(prefix),"provenance_patterns_checked":sum(len(v) for v in full.values())+sum(len(t) for short_by_length in short.values() for t in short_by_length.values()),"weighted_m_values":[1,2,3,4,12],"status":"PASS"}


def bitwidth(n): return (n-1).bit_length()


def x6(L):
    k,m=6,12
    fibres=[fibre_formula(m,r,L) for r in range(k+1)]
    num=global_formula(m,k,L)
    assert num==sum(perm(k,r)*fibres[r] for r in range(k+1))
    source_bits=bitwidth(N(k)); fibre_bits=bitwidth(max(fibres)); opt=bitwidth(num)
    return {"L":L,"fibre_sizes_by_source_length":fibres,"total_joint_states":num,"source_bits":source_bits,"fibre_bits":fibre_bits,"split_bits":source_bits+fibre_bits,"optimal_bits":opt,"split_excess_bits":source_bits+fibre_bits-opt}


def main():
    models=[check(k,L) for k in range(5) for L in range(6)]
    models.append(check(6,3))
    x=[x6(L) for L in range(7)]
    assert x[2]['total_joint_states']==1407685
    assert x[3]['total_joint_states']==50583973
    assert x[3]['split_bits']==x[3]['optimal_bits']==26
    assert x[4]['split_bits']==32 and x[4]['optimal_bits']==31
    result={"status":"PASS","input_pin":"awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34","scope":"Exact combinatorial provenance tails; directions independently contribute m^length. Brute enumerates all provenance patterns and source prefix orders for 31 parameter models; five direction multiplicities each; global R200 formula cross-check. X6 total state count is symbolic, not 50-million-state enumeration.","models_checked":len(models),"weighted_count_checks":5*len(models),"model_summary":models,"x6":x}
    with open('R208_verification.json','w') as f:
        json.dump(result,f,ensure_ascii=False,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='model_summary'},indent=2,ensure_ascii=False))

if __name__=='__main__':main()
