#!/usr/bin/env python3
from fractions import Fraction as F
from statistics import median
from time import perf_counter
from check_r131 import CyclicIndex,brute_vocabulary,cuts

def repeat(fn):
    t=[]; r=None
    for _ in range(3):
        s=perf_counter();r=fn();t.append((perf_counter()-s)*1000)
    return round(median(t),3),r

for g in (1,10,30,100):
    x=F(1,5); m=5; A,d,E=2*g,g,3*g
    p,idx=repeat(lambda:CyclicIndex(x,A,d,E,m))
    b,v=repeat(lambda:brute_vocabulary(x,A,d,E,m,F(0),F(2)))
    c=len(cuts(x,A,d,E,m,F(0),F(2)))
    assert idx.vocabulary(F(0),F(2))==v
    print(f'g={g} raw_cuts={c} primitive_cuts={len(idx.cuts)} raw_vocabulary_ms={b} cyclic_build_ms={p} vocabulary_size={len(v)}')
