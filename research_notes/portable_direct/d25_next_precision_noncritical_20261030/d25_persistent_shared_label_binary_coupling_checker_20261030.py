#!/usr/bin/env python3
"""Exact finite checks for an author-side, auxiliary two-copy BRC kernel.
No native X6 program, Source session, or scientific admission is invoked.
"""
from itertools import product
from collections import defaultdict
from json import dump
from pathlib import Path

Z=(1,-1,-1,1)

def k_interval(a,b):
    p=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return p,-min(p[0],p[3]),min(p[1],p[2])

def plus(p,k):
    return tuple(x+k*z for x,z in zip(p,Z))

def margins(v):
    return (v[0]+v[1],v[2]+v[3]), (v[0]+v[2],v[1]+v[3])

def tensor(a,b):
    return tuple(x*y for x in a for y in b)

def persistent(p,ks,ws,t):
    rows=[plus(p,k) for k in ks]
    out=[0]*(4**t)
    for row,w in zip(rows,ws):
        v=(1,)
        for _ in range(t):
            v=tensor(v,row)
        out=[x+w*y for x,y in zip(out,v)]
    return tuple(out)

def moments(ks,ws,t):
    return tuple(sum(w*k**j for k,w in zip(ks,ws)) for j in range(t+1))

count_configs=count_couplings=count_all_tables=0
for a in product(range(4), repeat=2):
    for b in product(range(4), repeat=2):
        p,lo,hi=k_interval(a,b)
        expected=set()
        for k in range(lo,hi+1):
            v=plus(p,k)
            assert min(v)>=0
            assert margins(v)==((a[0]*sum(b),a[1]*sum(b)),
                                (b[0]*sum(a),b[1]*sum(a)))
            expected.add(v)
            count_couplings+=1
        # An independent exhaustive reconstruction from fixed row and column sums.
        r0=a[0]*sum(b); r1=a[1]*sum(b)
        c0=b[0]*sum(a); c1=b[1]*sum(a)
        observed=set()
        for j00 in range(sum(a)*sum(b)+1):
            row=(j00,r0-j00,c0-j00,r1-c0+j00)
            if min(row)>=0 and margins(row)==((r0,r1),(c0,c1)):
                observed.add(row)
        assert expected==observed
        count_all_tables+=len(observed)
        count_configs+=1
assert count_couplings==count_all_tables

# Branch label persists once, while conditional emissions are independent in time.
p=(4,4,4,4)
ws=(1,2)
kA=(2,-1); kB=(0,0)
assert moments(kA,ws,1)==moments(kB,ws,1)==(3,0)
assert moments(kA,ws,2)==(3,0,6)
assert moments(kB,ws,2)==(3,0,0)
h1A=persistent(p,kA,ws,1)
h1B=persistent(p,kB,ws,1)
assert h1A==h1B==(12,12,12,12)
h2A=persistent(p,kA,ws,2)
h2B=persistent(p,kB,ws,2)
assert sum(abs(x-y) for x,y in zip(h2A,h2B))==96
assert set(x-y for x,y in zip(h2A,h2B))=={-6,6}
assert sum(h2A)==sum(h2B)==3*16**2
# A fresh, unobserved shared label drawn each tick has instead the product of sums.
assert tensor(h1A,h1A)==tensor(h1B,h1B)

# An unequal-mass, nonnegative integer contingency witness.
p_unequal,lo,hi=k_interval((1,2),(2,3))
assert p_unequal==(2,3,4,6) and (lo,hi)==(-2,3)
j_lo=plus(p_unequal,-2)
j_hi=plus(p_unequal,3)
assert j_lo==(0,5,6,4) and j_hi==(5,0,1,9)
assert sum(j_lo)==sum(j_hi)==15
assert sum(abs(x-y) for x,y in zip(j_lo,j_hi))==20

# Every admissible two-label assignment: finite moments exactly characterize
# finite persistent-branch observations on their checked horizon.
count_moment_pair_checks=count_histogram_checks=0
for a,b in [((1,1),(1,1)),((1,2),(2,3)),((2,2),(2,2))]:
    base,lo,hi=k_interval(a,b)
    cases=list(product(range(lo,hi+1),repeat=2))
    hist=lambda ks: tuple(sum(w for k,w in zip(ks,ws) if k==j)
                          for j in range(lo,hi+1))
    for t in (1,2,3):
        sig={ks:persistent(base,ks,ws,t) for ks in cases}
        mom={ks:moments(ks,ws,t) for ks in cases}
        for x in cases:
            for y in cases:
                assert (sig[x]==sig[y])==(mom[x]==mom[y])
                count_moment_pair_checks+=1
                if mom[x]==mom[y] and t>=min(hi-lo,2*len(ws)-1):
                    assert hist(x)==hist(y)
                    count_histogram_checks+=1

res={
 'status':'PASS', 'date':'2026-10-30',
 'scope':'author-only auxiliary positive-integer two-copy BRC, no native X6',
 'bounded_grid':'a0,a1,b0,b1 in {0,1,2,3}',
 'margin_configurations':count_configs,
 'admissible_couplings_checked':count_couplings,
 'independent_reconstructed_tables':count_all_tables,
 'persistent_moment_pair_comparisons':count_moment_pair_checks,
 'histogram_comparisons_within_bound':count_histogram_checks,
 'witness':{
    'label_weights':[1,2], 'P':[4,4,4,4],
    'k_class_A':[2,-1], 'k_class_B':[0,0],
    't1_equal':True, 't2_L1_difference':96,
    't2_signed_entry_differences':[-6,6],
    't2_integer_total_each':768,
    'redrawn_label_t2_equal':True,
    'unequal_total_sources':[3,5],
    'unequal_mass_k_interval':[-2,3],
    'unequal_mass_L1_witness':20
 }
}
path=Path(__file__).with_name('d25_persistent_shared_label_binary_coupling_author_check_20261030.json')
with path.open('w',encoding='utf-8') as f:
    dump(res,f,indent=2,ensure_ascii=False)
    f.write('\n')
print(res)
