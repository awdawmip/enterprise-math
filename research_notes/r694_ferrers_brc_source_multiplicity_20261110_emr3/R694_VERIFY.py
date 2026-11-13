#!/usr/bin/env python3
"""Exact R694 source-count distribution for static BRC X6 four-step source gates."""
from collections import Counter
from itertools import combinations, product
from fractions import Fraction
from math import comb
from pathlib import Path
import json

def move(z,i,s):
    a=list(z);a[i]+=s;return tuple(a)

def build():
    z=(0,)*6; paths={}
    for i,j in combinations(range(6),2):
        for s,t in product((-1,1),repeat=2):
            here=z; gates=[]
            for axis,sign in ((i,s),(j,t),(i,-s),(j,-t)):
                gates.append((here,axis,sign));here=move(here,axis,sign)
            assert here==z
            paths[(i,j,s,t)]=tuple(gates)
    return paths

def eligibility_ternary():
    h=Counter()
    for x in product(range(3),repeat=5):
        wx=1
        for a in x: wx*=comb(2,a)
        for y in product(range(3),repeat=5):
            w=wx
            for b in y:w*=comb(2,b)
            k=sum(x[i]*sum(y[j-1] for j in range(i+1,6)) for i in range(5))
            h[k]+=w
    return h

def eligibility_binary():
    h=Counter();bc=(0,1,1,2)
    for a in range(1<<10):
        x=[bc[(a>>(2*i))&3] for i in range(5)]
        for b in range(1<<10):
            y=[bc[(b>>(2*i))&3] for i in range(5)]
            suf=0;k=0
            for i in range(4,-1,-1):
                suf+=y[i];k+=x[i]*suf
            h[k]+=1
    return h

def verify():
    paths=build()
    assert len(paths)==60
    cnt=Counter(g for gs in paths.values() for g in gs)
    assert len(cnt)==140
    assert sum(v==1 for v in cnt.values())==120
    assert sum(v>1 for v in cnt.values())==20
    assert Counter(v for v in cnt.values() if v>1)=={2:4,4:4,6:4,8:4,10:4}
    assert len({g for gs in paths.values() for g in gs[1:3]})==120
    assert all(cnt[g]==1 for gs in paths.values() for g in gs[1:3])
    overlap=Counter(len(set(paths[q])&set(paths[r])) for q,r in combinations(paths,2))
    assert overlap=={0:1390,1:380}
    kh=eligibility_ternary()
    assert sum(kh.values())==2**20
    assert kh==eligibility_binary()
    coefficients=[
        sum(h*(4**(60-k))*comb(k,n)*(3**(k-n))
            for k,h in kh.items() if k>=n)
        for n in range(61)]
    den=2**140
    assert sum(coefficients)==den and coefficients[60]==1
    first=sum(n*c for n,c in enumerate(coefficients))
    second=sum(n*n*c for n,c in enumerate(coefficients))
    mean=Fraction(first,den)
    var=Fraction(second,den)-mean**2
    assert (mean,var)==(Fraction(15,4),Fraction(415,64))
    assert coefficients[0]==93848107613304762202165927229732737047025
    assert set(range(61))-set(kh)=={51,53,55,57,59}
    evidence={
        "schema":"R694_ESTAR_FERRERS_BRC_SOURCE_MULTIPLICITY_V1",
        "frozen_R462":"18783e01e3646c72b7aab3b16d3f565e83e6446f",
        "frozen_R687":"028d5612f9562bc22ac7593f03426fc32b1a9259",
        "R693":"20b8c376b9e9b89ff72b4f7b3e202398cb9b6297",
        "scope":"E* candidate, 60 labeled X6 four-step returns, 140 independent static binary directed gates",
        "source_count":60, "gate_count":140, "private_gates":120, "shared_gates":20,
        "source_pair_intersections":{"0":1390,"1":380},
        "eligible_histogram":{str(k):v for k,v in sorted(kh.items())},
        "N_distribution":{str(n):str(c) for n,c in enumerate(coefficients)},
        "total_gate_fields":str(den),
        "zero_source_fields":str(coefficients[0]),
        "mean":{"numerator":mean.numerator,"denominator":mean.denominator},
        "variance":{"numerator":var.numerator,"denominator":var.denominator},
        "verification_marker":"R694_FERRERS_BRC_SOURCE_MULTIPLICITY_EXACT_PASS"}
    Path(__file__).with_name("R694_EVIDENCE.json").write_text(
        json.dumps(evidence,indent=2,ensure_ascii=False,sort_keys=True)+"\n",
        encoding="utf-8")
    print(evidence["verification_marker"])
    return evidence

if __name__=="__main__":verify()
