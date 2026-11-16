#!/usr/bin/env python3
"""Unit67: signed-native shortest-path inversion, exact finite counterexample check."""
from itertools import product
from math import factorial
from collections import Counter
import json
from pathlib import Path

def require(test, msg):
    if not test:
        raise ValueError(msg)

def words(z):
    counts = Counter({(i+1 if a>0 else -(i+1)):abs(a) for i,a in enumerate(z) if a})
    out=[]
    def rec(prefix):
        if not sum(counts.values()):
            out.append(tuple(prefix))
            return
        for k in sorted(counts):
            if counts[k]:
                counts[k]-=1
                prefix.append(k)
                rec(prefix)
                prefix.pop()
                counts[k]+=1
    rec([])
    return out

def displacement(w,d=3):
    x=[0]*d
    for s in w:
        x[abs(s)-1]+=(1 if s>0 else -1)
    return tuple(x)

def inverse(w):
    return tuple(-s for s in w[::-1])

def canonicalize(z):
    m=min(z)
    return tuple(a-m for a in z)

def q(z):
    return sum(a*a for a in z)

def audit():
    checked=0
    total=0
    for z in product(range(-2,3), repeat=3):
        w=words(z)
        neg=tuple(-a for a in z)
        expected=factorial(sum(map(abs,z)))
        for a in z:
            expected//=factorial(abs(a))
        require(len(w)==expected, f"multinomial {z}")
        require(len(w)==len(set(w)), f"duplicates {z}")
        require({inverse(a) for a in w}==set(words(neg)),f"inverse {z}")
        require(all(displacement(a)==z and displacement(inverse(a))==neg for a in w),f"endpoint {z}")
        require(all(inverse(inverse(a))==a for a in w),f"involution {z}")
        require(q(z)==q(neg), f"length reversal {z}")
        checked+=1
        total+=len(w)
    require(words((1,0,0))==[(1,)] and words((-1,0,0))==[(-1,)],"unique primitive")
    require(inverse((1,))==(-1,),"native unit inverse")
    require(q((1,0,0))==q((-1,0,0))==1,"native unit norm")
    require(q(canonicalize((1,0,0)))==1 and q(canonicalize((-1,0,0)))==2,"observer asymmetry")
    z=(3,4,0)
    require(len(words(z))==len(words((-3,-4,0)))==35,"3-4-5 fiber")
    require({inverse(w) for w in words(z)}==set(words((-3,-4,0))),"3-4-5 inverse")
    require(q(z)==q((-3,-4,0))==25,"3-4-5 native norm")
    require(q(canonicalize((-3,-4,0)))==17,"3-4-5 observer norm")
    return {"schema":"EM_X6_UNIT67_SIGNED_PATH_INVERSION_V1",
            "status":"AUTHOR_EXACT_EXECUTED_UNREVIEWED_NOT_ADMITTED",
            "science_pins":{"native":"59538f585d037d09ef687b28715c4bc1a3f9fe03",
                            "historical":"fd2bcff10ca6e147348b6c1236027fc0d2877df3"},
            "coverage":{"domain":"Z3 coordinates -2..2 each, plus +/- (3,4,0)",
                        "endpoints":checked,"native_shortest_words":total,
                        "inverse_word_checks":2*total,"mismatches":0},
            "unit_axis":{"forward":[1],"reverse":[-1],"inverse_equal":True,
                        "native_G":[1,1],"relative_minzero_G":[1,2]},
            "three_four":{"native_G":[25,25],"relative_reverse_G":17,"BRC_each":35},
            "not_executed":"Original R061/R062/R063 native benchmark not rerun"}

if __name__=="__main__":
    d=audit()
    Path(__file__).with_name("X6_UNIT67_SIGNED_PATH_INVERSION_RESULTS_20261116.json").write_text(
        json.dumps(d,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(d["coverage"],sort_keys=True))
