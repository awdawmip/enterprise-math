#!/usr/bin/env python3
"""Exact rational/int verification of R477 PF3 tail-appending interval.

No floating-point decisions. It independently enumerates every order <= 3
minor of the leading (length+2)x(length+2) Toeplitz block.
"""
from fractions import Fraction as F
from itertools import combinations, product
import hashlib
import json

def at(a, k):
    return a[k] if 0 <= k < len(a) else 0

def det2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def det3(m):
    x,y,z=m[0]; u,v,w=m[1]; p,q,r=m[2]
    return x*(v*r-w*q)-y*(u*r-w*p)+z*(u*q-v*p)

def d2(a, j):
    return at(a,j)**2-at(a,j-1)*at(a,j+1)

def d3(a, j):
    return det3([[at(a,j+c-r) for c in range(3)] for r in range(3)])

def interval_decision(a):
    """R477 exact feasibility test. a=(prefix,t), length >=3, all positive."""
    n=len(a)-1; A,B=F(a[n-1]),F(a[n-2]); t=F(a[n])
    if not (t>0 and all(v>0 for v in a)):
        return False
    if n==2:
        return 2*B*t <= A*A
    C=F(a[n-3]); delta=B*B-C*A
    if any(d2(a,j)<=0 for j in range(1,n-1)):
        return False
    if any(d3(a,j)<0 for j in range(1,n-2)):
        return False
    if delta<=0:
        return False
    Q=d3(a[:-1],n-2)  # append zero at index n
    d=d2(a,n-3)
    if d<=0 or Q+t*d<0:
        return False
    P=A**3-2*A*B*t+C*t*t
    # Exact rational equivalent of t <= U=A^2/(B+sqrt(delta)).
    return B*t<A*A and P>=0

def local_decision(a):
    return all(d2(a,j)>0 and d3(a,j)>=0 for j in range(len(a)))

def leading_block_oracle(a):
    """All 1x1, 2x2 and 3x3 minors of the leading (L+2)x(L+2) block."""
    size=len(a)+2
    matrix=[[at(a,c-r) for c in range(size)] for r in range(size)]
    checked=0
    for k in (1,2,3):
        subsets=list(combinations(range(size),k))
        for rows in subsets:
            for cols in subsets:
                checked+=1
                minor=[[matrix[r][c] for c in cols] for r in rows]
                v=(minor[0][0] if k==1 else det2(minor) if k==2 else det3(minor))
                if v<0:
                    return False,checked,{'order':k,'rows':list(rows),'cols':list(cols),'value':str(v)}
    return True,checked,None

def main():
    tested=0; passing=0; checked=0; broken=0; length_cases={}
    hash_stream=hashlib.sha256()
    for L in range(3,7):
        count=0; pass_L=0
        for a in product((1,2,3),repeat=L):
            a=tuple(F(x) for x in a)
            predicted=interval_decision(a)
            local=local_decision(a)
            oracle,steps,_=leading_block_oracle(a)
            assert predicted == local == oracle, ('mismatch',a,predicted,local,oracle)
            hash_stream.update(f'{L}:{",".join(map(str,a))}:{int(predicted)}\n'.encode())
            tested+=1;count+=1;checked+=steps
            if oracle:
                passing+=1;pass_L+=1
        length_cases[str(L)]={'tested':count,'pf3':pass_L}
    prefix=(F(1),F(1),F(1,2),F(1,6))
    repaired=prefix+(F(1,30),)
    assert d3(prefix,2)==F(-1,72)
    assert d3(repaired,2)==F(1,360)
    assert d3(repaired,3)==F(1,5400)
    assert not leading_block_oracle(prefix)[0] and leading_block_oracle(repaired)[0]
    A,B,C=prefix[-1],prefix[-2],prefix[-3]
    Q=d3(prefix,2);d=d2(prefix,1)
    assert -Q/d == F(1,36)
    t=F(1,30)
    assert 0 < t and Q+t*d>=0 and B*t<A*A and (A**3-2*A*B*t+C*t*t)>=0
    lower_edge=prefix+(F(1,36),)
    assert d3(lower_edge,2)==0 and leading_block_oracle(lower_edge)[0]
    upper_edge=(F(1),F(5),F(9),F(9))
    above_edge=(F(1),F(5),F(9),F(10))
    assert d3(upper_edge,2)==0 and leading_block_oracle(upper_edge)[0]
    assert d3(above_edge,2)==F(-71) and not leading_block_oracle(above_edge)[0]
    t_e=F(1,6)
    exp_cut=(F(1),F(1),F(1,2),t_e)
    assert d3(exp_cut,2)==F(-1,72)
    result={
        'status':'R477_EXACT_PASS',
        'domain':'positive integer coefficient tuples of length 3..6, each entry in {1,2,3}',
        'tested':tested,'pf3':passing,'not_pf3':tested-passing,
        'minor_checks_until_first_negative_or_complete':checked,
        'per_length':length_cases,
        'compared':['R477 exact rational interval test','R474 local PF3 test',
                    'all minors of order <=3 in leading (L+2)x(L+2) Toeplitz block'],
        'classification_stream_sha256':hash_stream.hexdigest(),
        'rescue_example':{'prefix':['1','1','1/2','1/6'],
            'appended_t':'1/30','lower_bound':'1/36',
            'prefix_D3_2':'-1/72','full_D3_2':'1/360','full_D3_3':'1/5400'},
        'truncated_exponential_example':{'prefix':['1','1','1/2','1/6'], 'D3_2':'-1/72'},
        'endpoint_checks':{'lower_repair_t':'1/36','lower_D3_2':'0',
                           'upper_t':'9','upper_coefficients':['1','5','9','9'],'upper_D3_2':'0',
                           'above_t':'10','above_D3_2':'-71'},
        'arithmetic':'Python Fraction + integer minors; no floats',
        'general_real_theorem_basis':'symbolic proof, not finite enumeration'}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
