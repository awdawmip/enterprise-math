#!/usr/bin/env python3
"""R694 exact E* S3 contextual-return certificate. Python standard library only.
Input integers are copied from immutable R692C source at 3dacca501... Git blob 0c6d51f9...
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

N={
0:[{'012':6,'021':9},{'012':6,'021':6,'120':3},{'012':6,'021':3,'201':6},{'012':6,'120':3,'201':6}],
1:[{'012':6,'120':6,'201':3},{'012':9,'120':6},{'012':12,'201':3},{'012':15}],
2:[{'012':15},{'012':12,'021':3},{'012':9,'021':6},{'012':6,'021':9}]}
GROUP=('012','021','120','201','102','210')
INVERSE={'012':'012','021':'021','120':'201','201':'120','102':'102','210':'210'}

def multiply(g,h): return ''.join(g[int(i)] for i in h)

def kernel(a,mask):
    c=defaultdict(int)
    for j in range(4):
        if mask & (1<<j):
            for g,w in N[a][j].items(): c[g]+=w
    d=15*mask.bit_count()
    assert sum(c.values())==d
    return {g:F(w,d) for g,w in c.items()}

def one(mu): return mu.get('012',F(0))

def two(mu,nu): return sum((w*nu.get(INVERSE[g],F(0)) for g,w in mu.items()),F(0))

def full(mu): return tuple(mu.get(g,F(0)) for g in GROUP)

def convolution(mu,nu):
    z=defaultdict(F)
    for g,p in mu.items():
        for h,q in nu.items():
            z[multiply(g,h)]+=p*q
    return dict(z)

def homogeneous(mu,limit):
    z={'012':F(1)}
    out=[one(z)]
    for k in range(limit):
        z=convolution(z,mu)
        out.append(one(z))
    return out

results={'schema':'R694_CONTEXTUAL_ESTAR_EXACT_V1',
'upstream_commit':'3dacca5010104893d96301af4d61608d5a5a0879',
'upstream_blob':'0c6d51f99eac5903a30770c8c393c972a68d93ad',
'probe_mask':3,'phases':{},'ordered_pair_checks':0}
for a in range(3):
    kernels={m:kernel(a,m) for m in range(1,16)}
    probe=kernels[3]
    full_class=defaultdict(list)
    obs_class=defaultdict(list)
    rows=[]
    for m,mu in kernels.items():
        pair=(one(mu),two(mu,probe))
        full_class[full(mu)].append(m)
        obs_class[pair].append(m)
        rows.append({'mask':m,'r1':str(pair[0]),'r2_with_mask3':str(pair[1])})
    for m,j in product(range(1,16),repeat=2):
        same=full(kernels[m])==full(kernels[j])
        measured=(one(kernels[m])==one(kernels[j]) and
                  two(kernels[m],probe)==two(kernels[j],probe))
        assert same==measured,(a,m,j)
        results['ordered_pair_checks']+=1
        if not same:
            assert (one(kernels[m])!=one(kernels[j]) or
                    any(two(kernels[m],kernels[k])!=two(kernels[j],kernels[k])
                        for k in (1,2,4,8))),(a,m,j,'singleton separation')
        results['ordered_pair_checks']+=1
    assert len(full_class)==len(obs_class)==(13,13,9)[a]
    dup=sorted(sorted(v) for v in full_class.values() if len(v)>1)
    expected=([[6,9,15]],[[6,9,15]],[[2,5,7],[4,10,14],[6,9,15]])[a]
    assert dup==expected,(a,dup)
    results['phases'][str(a)]={'full_kernel_classes':len(full_class),
                               'probe_classes':len(obs_class),
                               'duplicate_classes':dup,'rows':rows}
A=kernel(0,2)
B=kernel(0,5)
L=kernel(0,4)
assert full(A)!=full(B) and one(A)==one(B)==F(2,5)
assert homogeneous(A,12)==homogeneous(B,12)
assert two(A,L)==F(8,25) and two(B,L)==F(6,25)
results['witness']={'phase':0,'first_mask_a':2,'first_mask_b':5,
                    'continuation_mask':4,'return_a':str(two(A,L)),
                    'return_b':str(two(B,L)),'difference':str(two(A,L)-two(B,L)),
                    'homogeneous_powers_verified':'0..12'}
results['status']='R694_ALL_EXACT_ASSERTIONS_PASS'
if __name__=='__main__':
    import json
    print(json.dumps(results,ensure_ascii=False,indent=2))
