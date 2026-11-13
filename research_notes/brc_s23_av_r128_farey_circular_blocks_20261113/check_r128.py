#!/usr/bin/env python3
"""Exact Farey-sector signature enumeration for R128; standard-library fractions only."""
from fractions import Fraction as Q
from math import gcd
from random import Random
import json


def frac(t):
    return t - (t.numerator // t.denominator)


def signature(m, alpha, beta, threshold):
    return sum((1 << i) for i in range(m) if frac(alpha + i*beta) < threshold)


def farey_cutpoints(m):
    return sorted({Q(p,q) for q in range(2,m) for p in range(1,q) if gcd(p,q)==1})


def beta_representatives(m):
    cuts=farey_cutpoints(m)
    return [Q(0)] + cuts + [(a+b)/2 for a,b in zip([Q(0)]+cuts,cuts+[Q(1)])]


def group_order(m,beta):
    groups={}
    for i in range(m):
        groups.setdefault(frac(i*beta),0)
        groups[frac(i*beta)] |= 1 << i
    return sorted(groups.items())


def word_witnesses(m,beta):
    ordered=group_order(m,beta)
    n=len(ordered)
    positions=[x[0] for x in ordered]
    masks=[x[1] for x in ordered]
    yield 0,(Q(0),Q(0))
    # All ones: the complementary short arc lies within a cyclic gap.
    gap=positions[0]+1-positions[-1]
    s=positions[-1]+2*gap/3
    e=positions[-1]+1+gap/3
    yield (1<<m)-1,(frac(-s),e-s)
    for size in range(1,n):
        for j in range(n):
            last=j+size-1
            next_index=j+size
            left=positions[j-1] if j else positions[-1]-1
            start=positions[j]
            right=positions[last % n]+last//n
            next_position=positions[next_index%n]+next_index//n
            s=(left+start)/2
            e=(right+next_position)/2
            mask=0
            for v in range(size):
                mask|=masks[(j+v)%n]
            yield mask,(frac(-s),e-s)


def all_patterns(m):
    output={}
    for beta in beta_representatives(m):
        for mask, (alpha,tau) in word_witnesses(m,beta):
            assert Q(0)<=tau<Q(1)
            assert signature(m,alpha,beta,tau)==mask, (m,beta,mask,alpha,tau)
            output.setdefault(mask,(alpha,beta,tau))
    return output


def cuts_affine(c,b,l,h):
    if b==0: return []
    lo=min(c+b*l,c+b*h); hi=max(c+b*l,c+b*h)
    return [(Q(n)-c)/b for n in range(lo.numerator//lo.denominator, hi.numerator//hi.denominator+2)
            if l<(Q(n)-c)/b<h]


def complete_s23_patterns(m,x,A,d,E,l,h):
    cuts={l,h}
    for i in range(m):
        b=A+i*d
        cuts.update(cuts_affine(x,b,l,h))
        cuts.update(cuts_affine(x,b-E,l,h))
    cuts.update(cuts_affine(Q(0),E,l,h))
    cuts=sorted(cuts)
    samples=cuts[1:-1]+[(u+v)/2 for u,v in zip(cuts,cuts[1:])]
    words=set()
    for t in samples:
        words.add(signature(m,frac(x+A*t),frac(d*t),frac(E*t)))
    return words,len(samples)


def main():
    counts={}
    for m in range(2,14):
        w=all_patterns(m)
        F=len(farey_cutpoints(m))
        bound=(2*F+1)*(m*(m-1)+2)
        assert len(w)<=bound
        counts[str(m)]={"critical_rationals":F,"universal_words":len(w),"bound":bound}
    rng=Random(12820261113)
    cases=0; samples=0
    for _ in range(120):
        m=rng.randrange(2,9)
        x=Q(rng.randrange(-8,9),rng.randrange(1,8))
        A=rng.randrange(-9,10); d=rng.randrange(-9,10); E=rng.randrange(-9,10)
        observed,num=complete_s23_patterns(m,x,A,d,E,Q(0),Q(1))
        assert observed<=set(all_patterns(m))
        cases+=1; samples+=num
    output={"status":"R128_FAREY_CIRCULAR_BLOCK_PASS","count_table":counts,
            "exact_s23_cases":cases,"exact_s23_cell_and_singleton_samples":samples,
            "seed":12820261113,"arithmetic":"fractions.Fraction exact"}
    with open("verification_r128.json","w",encoding="utf8") as f:
        json.dump(output,f,ensure_ascii=False,indent=2)
    print(json.dumps(output,ensure_ascii=False))

if __name__=="__main__": main()
