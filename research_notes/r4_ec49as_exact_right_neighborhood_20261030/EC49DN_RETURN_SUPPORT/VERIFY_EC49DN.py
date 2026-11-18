#!/usr/bin/env python3
"""Exact native signed-X6 future-operation reachability and positive BRC mass checks.

Independent direct word enumeration through h=7 and a distinct multinomial
coefficient computation through h=12. This checks operation support and total
BRC masses, not the richer A/B ordered-label observation rank except zero rows.
"""
import itertools
import json
from collections import defaultdict
from math import factorial

OPS = {
    'a': (-1,-1), 'b': (-2,-2),
    'c': (1,2,-1,-2), 'd': (2,1,-2,-1),
    'e': (3,1,1,-3),
}
X=(2,3,1,2,3,4)
Y=(5,7,3,5,7,9)

def native6(seq):
    out=[0]*6
    for step in seq:
        out[abs(step)-1]+=1 if step>0 else -1
    return tuple(out)

def brc(seq,weights):
    z=1
    for step in seq:
        if step>0: z*=weights[step-1]
    return z

def closed_form(h, D, weights):
    if any(D[2:]) or D[0]%2 or D[1]%2 or D[1]<0:
        return 0
    k=D[0]//2
    b=D[1]//2
    if h < b+abs(k):
        return 0
    ax=weights[0]*weights[1]
    ex=weights[2]*weights[0]**2
    out=0
    for e in range(max(0,-k),h+1):
        a=e+k
        ell=h-a-b-e
        if ell<0: break
        out += factorial(h)//(factorial(a)*factorial(b)*factorial(e)*factorial(ell))*(2*ax)**ell*ex**e
    return out

def main():
    assert native6(OPS['a'])==(-2,0,0,0,0,0)
    assert native6(OPS['b'])==(0,-2,0,0,0,0)
    assert native6(OPS['c'])==native6(OPS['d'])==(0,0,0,0,0,0)
    assert native6(OPS['e'])==(2,0,0,0,0,0)
    assert [brc(OPS[z],X) for z in OPS]==[1,1,6,6,4]
    assert [brc(OPS[z],Y) for z in OPS]==[1,1,35,35,75]
    keys=list(OPS)
    sizes={}
    witness={}
    total_words=0
    for h in range(0,8):
        agg=defaultdict(lambda:[0,0,0])
        for word in itertools.product(keys, repeat=h):
            steps=tuple(step for z in word for step in OPS[z])
            d2=native6(steps)
            arr=agg[d2]
            arr[0]+=1
            arr[1]+=brc(steps,X)
            arr[2]+=brc(steps,Y)
            total_words+=1
        assert sum(v[0] for v in agg.values())==5**h
        for suffix_disp,(count,wx,wy) in agg.items():
            D=tuple(-z for z in suffix_disp)
            assert count==closed_form(h,D,(1,)*6), (h,D,count)
            assert wx==closed_form(h,D,X), (h,D,wx)
            assert wy==closed_form(h,D,Y), (h,D,wy)
        assert closed_form(h,(0,-2,0,0,0,0),X)==0
        assert closed_form(h,(0,-2,0,0,0,0),Y)==0
        sizes[h]=len(agg)
        if h in (1,2,3):
            for D in ((0,2,0,0,0,0),(-2,0,0,0,0,0),(0,-2,0,0,0,0)):
                witness[f'h{h}:{D[0]},{D[1]}']={
                    'count':closed_form(h,D,(1,)*6),
                    'BRC_x':closed_form(h,D,X),
                    'BRC_y':closed_form(h,D,Y),
                }
    # independent direct dynamic programming for h<=12 (integer BRC)
    dp={(0,0,0,0,0,0):(1,1,1)}
    for h in range(1,13):
        new=defaultdict(lambda:[0,0,0])
        for disp,(n,wx,wy) in dp.items():
            for op in keys:
                delta=native6(OPS[op])
                target=tuple(p+q for p,q in zip(disp,delta))
                r=new[target]
                r[0]+=n
                r[1]+=wx*brc(OPS[op],X)
                r[2]+=wy*brc(OPS[op],Y)
        dp=new
        assert sum(val[0] for val in dp.values())==5**h
        for suffix_disp,(n,wx,wy) in dp.items():
            D=tuple(-z for z in suffix_disp)
            assert (n,wx,wy)==(closed_form(h,D,(1,)*6), closed_form(h,D,X), closed_form(h,D,Y))
        assert (0,2,0,0,0,0) not in dp  # forbidden return from D=-2E2
    # Native nonempty history fiber D=-2E2 at n=2.
    history=(-2,-2)
    assert native6(history)==(0,-2,0,0,0,0)
    for h in range(0,8):
        for word in itertools.product(keys,repeat=h):
            steps=tuple(step for z in word for step in OPS[z])
            assert native6(history+steps)!=(0,0,0,0,0,0)
    report={
        'status':'PASS',
        'exact_operation_words_h_0_through_7':total_words,
        'word_displacement_support_sizes':sizes,
        'weighted_bruteforce_vs_multinomial':'PASS: all observed fibers and 3 channels, h=0..7',
        'weighted_dynamic_program_vs_multinomial':'PASS: all observed fibers and 3 channels, h=1..12',
        'D_minus_2E2':{'all_h_return':'NONE','exact_rank':'0','cumulative_rank':'0'},
        'sample_return_mass':witness,
        'boundary':'Finite tests validate implementation. All-h reachability and zero ranks follow from the exact displacement equation.'
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
