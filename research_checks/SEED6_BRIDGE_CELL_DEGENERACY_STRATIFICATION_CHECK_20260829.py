#!/usr/bin/env python3
"""Exact checker for RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION."""
from collections import Counter
import json
from math import gcd

PAIRINGS=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
EXPECTED={(1,1,1,1):3,(2,1,1):2,(2,2):2,(3,1):1,(4,):1}

def factorint(n):
    x=n; f={}; p=2
    while p*p<=x:
        while x%p==0:
            f[p]=f.get(p,0)+1; x//=p
        p=3 if p==2 else p+2
    if x>1: f[x]=f.get(x,0)+1
    return f

def is_prime(n):
    f=factorint(n)
    return n>=2 and len(f)==1 and next(iter(f.values()))==1

def is_prime_power(n):
    return n>=2 and len(factorint(n))==1

def partition_type(vals):
    return tuple(sorted(Counter(vals).values(),reverse=True))

def symbolic_pairings(vals):
    out=set()
    for (i,j),(k,l) in PAIRINGS:
        a=tuple(sorted((vals[i],vals[j])))
        b=tuple(sorted((vals[k],vals[l])))
        out.add(tuple(sorted((a,b))))
    return out

def states(r,s):
    return [tuple(sorted((6,r*s))),
            tuple(sorted((2*r,3*s))),
            tuple(sorted((2*s,3*r)))]

def rectangle_vertices(r,s):
    return (2*r,2*s,3*r,3*s)

def predicted_rectangle_count(r,s):
    if r==s: return 2
    if 2*r==3*s or 2*s==3*r: return 3
    return 4

def gcd_labels(r,s):
    A,B,C,D=rectangle_vertices(r,s)
    return (gcd(A,B),gcd(C,D),gcd(A,C),gcd(B,D),gcd(A,D),gcd(B,C))

def run(limit=200):
    equality=Counter(); state_counts=Counter(); rect_counts=Counter(); joint=Counter()
    resonances=[]
    for r in range(1,limit+1):
        for s in range(1,limit+1):
            P0,P1,P2=states(r,s)
            assert (P1==P2)==(r==s)
            assert (P0==P1)==(r==3 or s==2)
            assert (P0==P2)==(r==2 or s==3)
            pt=partition_type([2,3,r,s])
            nstate=len({P0,P1,P2})
            assert nstate==EXPECTED[pt]==len(symbolic_pairings([2,3,r,s]))
            nrect=len(set(rectangle_vertices(r,s)))
            assert nrect==predicted_rectangle_count(r,s)
            d=gcd(r,s)
            assert gcd_labels(r,s)==(2*d,3*d,r,s,gcd(2*r,3*s),gcd(2*s,3*r))
            equality['+'.join(map(str,pt))]+=1
            state_counts[str(nstate)]+=1
            rect_counts[str(nrect)]+=1
            joint[f"{nstate},{nrect}"]+=1
            if r!=s and (2*r==3*s or 2*s==3*r):
                resonances.append((r,s))
    assert len(resonances)==2*(limit//3)

    primes=[n for n in range(2,limit+1) if is_prime(n)]
    prime_powers=[n for n in range(2,limit+1) if is_prime_power(n)]
    pp=Counter()
    for r in prime_powers:
        pr,ar=next(iter(factorint(r).items()))
        for s in prime_powers:
            ps,bs=next(iter(factorint(s).items()))
            if pr<=3 or ps<=3:
                continue
            pp["checked_ordered_pairs"]+=1
            if pr!=ps:
                pp["different_base"]+=1
                assert len(set(states(r,s)))==3
                assert len(set(rectangle_vertices(r,s)))==4
                assert gcd(r,s)==1
            elif ar!=bs:
                pp["same_base_unequal_exponent"]+=1
                m=pr**min(ar,bs)
                assert len(set(states(r,s)))==3
                assert len(set(rectangle_vertices(r,s)))==4
                assert gcd_labels(r,s)[4:]==(m,m)
            else:
                pp["same_base_equal_exponent"]+=1
                assert r==s
                assert len(set(states(r,s)))==2
                assert len(set(rectangle_vertices(r,s)))==2

    assert len(set(states(6,4)))==3 and len(set(rectangle_vertices(6,4)))==3
    assert len(set(states(35,55)))==3 and len(set(rectangle_vertices(35,55)))==4
    assert gcd_labels(35,55)[4:]==(5,5)

    return {
      "task_id":"RS-SEED6-BRIDGE-CELL-DEGENERACY-STRATIFICATION",
      "limit":limit,
      "ordered_pairs_checked":limit*limit,
      "prime_count":len(primes),
      "prime_power_count_including_primes":len(prime_powers),
      "equality_partition_counts":dict(sorted(equality.items())),
      "pairing_state_count_distribution":dict(sorted(state_counts.items())),
      "rectangle_vertex_count_distribution":dict(sorted(rect_counts.items())),
      "joint_signature_counts":dict(sorted(joint.items())),
      "ratio_resonance_ordered_pair_count":len(resonances),
      "ratio_resonance_formula":"2*floor(limit/3)",
      "prime_power_fiber_checks":dict(pp),
      "verdict":"PASS"
    }

if __name__=="__main__":
    print(json.dumps(run(200),ensure_ascii=False,indent=2,sort_keys=True))
