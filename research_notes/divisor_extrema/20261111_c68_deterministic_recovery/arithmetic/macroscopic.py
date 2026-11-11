"""Exact limiting alphabet decoder and native, finite positive-branch comparisons."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import cache
from itertools import product
from pathlib import Path
import json
import sys


def v(a,p):
    assert a
    return va(a.numerator,p)-va(a.denominator,p)


def va(n,p):
    s=0
    while n%p==0:
        s+=1
        n//=p
    return s


@cache
def kernel(k,gap):
    t=Q(7,8)**(2**gap)
    return 448*t**(15*k),4*t**(3*k)


def encode(r,word):
    z=Q(0)
    for i in reversed(range(len(word))):
        label=word[i]
        h,p=(Q(448),Q(4)) if label=='s' else kernel(2*(r-i)+1,label)
        z=(h*z+p)/(h*z+1)
    return z


def decode(z):
    labels=[]
    r=None
    while z:
        e=v(z,7)
        if e:
            assert e>0 and e%3==0
            j=va(e//3,2)
            k=(e//3)//2**j
            new_r=(k-1)//2+len(labels)
            assert k>=3 and (r is None or r==new_r)
            r=new_r
            label=j
            h,p=kernel(k,j)
        else:
            assert (z.numerator-4*z.denominator)%7==0
            label='s'
            h,p=448,4
        assert z!=1
        z=(z-p)/(h*(1-z))
        labels.append(label)
    return tuple(labels),r


def census(limit):
    rows=[];words_tested=0
    for r in range(1,limit+1):
        count=0
        centers=[]
        for end in range(r+1):
            for word in product(('s',0,1),repeat=end):
                z=encode(r,word)
                got,rhat=decode(z)
                assert got==word and (rhat==r if any(a!='s' for a in word) else rhat is None)
                count+=1
                centers.append(z/(1+z))
        centers.sort()
        gap=min(y-x for x,y in zip(centers,centers[1:]))
        assert gap>0
        lower=gap.denominator.bit_length()-gap.numerator.bit_length()
        if Q(2)**(-lower)<gap:lower-=1
        assert Q(2)**(-lower-1)<gap<=Q(2)**(-lower)
        height=896**r*8**(15*2*r*(r+2))
        assert gap>=Q(1,25*height*height)
        if r>1:
            assert gap<=4*1344**(r-1)*Q(7,8)**(30*(r*(r+2)-3))
        rows.append(dict(r=r,count=count,negative_log2_min_gap_floor=lower))
        words_tested+=count
    return dict(max_r=limit,alphabet_indices=[0,1],tested=words_tested,rows=rows)


def scaled_path(r,c,letters):
    prefix=[]
    initial=c
    for i in range(r):
        if i<len(letters):
            if letters[i]=='s':m=1 if c>2 else 0
            else:
                ratio=Q(7,8)**(4*2**letters[i])
                m=c-max(2,c*ratio.numerator//ratio.denominator)
        elif i==len(letters):m=c-2
        else:m=0
        prefix.append(m)
        c-=m
    prefix.append(c-2)
    assert sum(prefix)==initial-2
    return tuple(prefix)


def scaled(x,units=10**9):
    return [x.numerator*units//x.denominator,-((-x.numerator*units)//x.denominator)]


def examples(c64,c67,native_root):
    sys.path[:0]=list(map(str,(c64,c67,native_root)))
    from observed_four import tail_forms
    from suffix_limits import block
    from mixed_kernel import responses,simplex_rows
    from enterprise_math import brc_histogram as brc
    from moving_gap import native
    results=[]
    branches=0
    for w in ((0,1),(1,0),('s',0),(0,'s')):
        r=3
        z=encode(r,w)
        records=[]
        for c in (32,128,512):
            path=scaled_path(r,c,w)
            values=native(r,c,path,block,tail_forms)
            if c==32:
                m,n=responses(r,c,path,brc)
                lo,hi=simplex_rows(m,7)
                assert values==[hi[j]/lo[j] for j in (3,4,5)]
                branches+=n
            records.append(dict(c=c,path=path,extreme_interval_in_1e_minus9=[scaled(min(values))[0],scaled(max(values))[1]]))
        results.append(dict(letters=w,center_enclosed_in_1e_minus9=scaled(z),stocks=records))
    return dict(native_BRC_positive_branches_with_multiplicity=branches,examples=results)


if __name__=='__main__':
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--c64',type=Path,required=True)
    ap.add_argument('--c67',type=Path,required=True)
    ap.add_argument('--native-root',type=Path,required=True)
    ap.add_argument('--limit',type=int,default=6)
    a=ap.parse_args()
    print(json.dumps(dict(exact=census(a.limit),finite=examples(a.c64.resolve(),a.c67.resolve(),a.native_root.resolve())),indent=2))
