#!/usr/bin/env python3
"""Exact R762DJ signed paired-block area/BRC verifier (Python 3; integer only)."""
import json
import math
from collections import Counter
from itertools import permutations, product

ORDERINGS = list(permutations(range(3)))
PAIRS = ((0,1),(0,2),(1,2))

def sign_of_order(order):
    pos={v:k for k,v in enumerate(order)}
    return tuple(1 if pos[i]<pos[j] else -1 for i,j in PAIRS)

def area_of_word(word):
    return tuple(sum(x[i]*y[j]-x[j]*y[i]
                     for ix,x in enumerate(word) for y in word[ix+1:])
                 for i,j in PAIRS)

def one_block_counts(modulus, signs=(1,1,1)):
    out=Counter()
    for u,w in product(ORDERINGS,repeat=2):
        v=[tuple(signs[i] if j==i else 0 for j in range(3)) for i in u]
        v += [tuple(-signs[i] if j==i else 0 for j in range(3)) for i in w]
        assert tuple(map(sum,zip(*v)))==(0,0,0)
        actual=area_of_word(v)
        expected=tuple(signs[i]*signs[j]*(sign_of_order(u)[k]+sign_of_order(w)[k])
                       for k,(i,j) in enumerate(PAIRS))
        assert actual==expected
        out[tuple(x%modulus for x in actual)]+=1
    assert sum(out.values())==36
    return out

def convolve(f,g,q):
    out=Counter()
    for x,n in f.items():
        for y,m in g.items():
            out[tuple((u+v)%q for u,v in zip(x,y))]+=n*m
    return out

def character_F(t,signs):
    # Omega^a + Omega^-a = 2 when a=0 mod 3; -1 otherwise
    n0=sum(sum(a*b for a,b in zip(t,s))%3==0 for s in signs)
    assert (3*n0-len(signs))%2==0
    return (3*n0-len(signs))//2

def character_tables():
    signs=[sign_of_order(p) for p in ORDERINGS]
    domain=list(product(range(3),repeat=3))
    f={t:character_F(t,signs) for t in domain}
    assert Counter(f.values())=={6:1,-3:8,0:12,3:6}
    active=[t for t in domain if t!=(0,0,0) and f[t]!=0]
    assert len(active)==14
    R={}
    for x in domain:
        n0=sum(sum(a*b for a,b in zip(t,x))%3==0 for t in active)
        assert (3*n0-len(active))%2==0
        R[x]=(3*n0-len(active))//2
    assert Counter(R.values())=={14:1,2:12,-4:8,-1:6}
    return R,f

def run():
    R,F=character_tables()
    checks=0
    output=[]
    domains={3:list(product(range(3),repeat=3)),4:list(product((0,2),repeat=3))}
    for q in (3,4):
        for signs in product((-1,1),repeat=3):
            hist=one_block_counts(q,signs)
            assert Counter(hist.values())==({1:6,2:12,6:1} if q==3 else {4:6,6:2})
            checks+=36
        base=one_block_counts(q)
        counts=Counter({(0,0,0):1})
        for k in range(1,9):
            counts=convolve(counts,base,q)
            assert sum(counts.values())==36**k
            if q==3:
                for x in domains[q]:
                    expected=(4+R[x])//3 if k==1 else 3**(2*k-3)*(4**k+R[x])
                    assert counts[x]==expected,(q,k,x,counts[x],expected)
                    checks+=1
                g=math.gcd(*(counts[x] for x in domains[q]))
                assert g==3**(2*k-2)
                assert 36**k//g==9*4**k
                tv_num,tv_den=38,27*4**k
                joint=36**k
            else:
                for x in domains[q]:
                    y=tuple(v//2 for v in x)
                    numerator=4**k*(9**k+(3 if y in ((0,0,0),(1,1,1)) else -1))
                    assert numerator%8==0 and counts[x]==numerator//8
                    checks+=1
                g=math.gcd(*(counts[x] for x in domains[q]))
                assert g==2**(2*k-1)
                assert 36**k//g==2*9**k
                tv_num,tv_den=3,4*9**k
                joint=18**k
            output.append(dict(q=q,k=k,states=sum(v>0 for v in counts.values()),
                               gcd_path_counts=g,endpoint_equal_seeds=36**k//g,
                               joint_trajectory_equal_seeds=joint,total_named_paths=36**k,
                               tv_to_reachable_uniform=f"{tv_num}/{tv_den}"))
            checks+=len(domains[q])+6
    return dict(schema="ENTERPRISE_MATH_R762DJ_EXACT_EVIDENCE_V1",status="PASS",
                method="Exact integer signed path enumeration + Fourier tables + convolution, k=1..8",
                character_F_histogram=dict(sorted(Counter(F.values()).items())),
                character_R_histogram=dict(sorted(Counter(R.values()).items())),
                signed_single_block_paths_checked=36*8*2,
                exact_assertion_checks=checks,result_rows=output,
                theorem_scope="conditional equiprobable independent paired-triad X6 candidate paths; NOT native force closure",
                review_status="NOT_REVIEWED")

if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False))
