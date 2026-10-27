#!/usr/bin/env python3
"""PREFIX-273: exact Z2 ordered-path-pair BRC effect and coding checks.

Declared formal scope only. This is NOT a native H_n -> H_(n+1) experiment.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product, combinations_with_replacement
import json


def intensity(weights, signs):
    # The equality with this square is the exact ordered (p,q) Z2 BRC identity.
    brc_pairs = sum((weights[i]*weights[j]*signs[i]*signs[j]
                     for i in range(len(signs)) for j in range(len(signs))),
                    Fraction(0))
    return brc_pairs


def all_signs(k):
    return product((-1, 1), repeat=k)


def full_gram(signs):
    return tuple(signs[i]*signs[j]
                 for i in range(len(signs)) for j in range(i+1,len(signs)))


def coded(k):
    assert k >= 2
    return tuple([2**i for i in range(k-1)] + [2**(k-1)-1])


def separates(weights):
    outputs = {}
    k=len(weights)
    for s in all_signs(k):
        result=intensity(weights,s)
        gram=full_gram(s)
        if result in outputs and outputs[result] != gram:
            return False
        outputs[result] = gram
    return len(outputs)==2**(k-1)


def check_cut_identity(k):
    w=coded(k)
    n=0
    for s in all_signs(k):
        total = sum(w[i]*s[i] for i in range(k))
        for mask in range(1,2**k-1):
            A=sum(w[i]*s[i] for i in range(k) if mask>>i&1)
            B=total-A
            t=tuple(-s[i] if mask>>i&1 else s[i] for i in range(k))
            assert intensity(w,s)-intensity(w,t)==4*A*B
            assert A and B  # For coded weights every nonempty proper subset is signed-dissociation.
            n += 1
    return n


def brute_first(k):
    for S in range(k,2**k-1):
        for w in combinations_with_replacement(range(1,S-k+2),k):
            if sum(w)==S and separates(w):
                return {"sum":S,"weights":list(w)}
    raise AssertionError("no witness at predicted bound")


def main():
    out={"schema":"PREFIX273_EXACT_CHECK_V1", "coded":[], "cut_checks":0}
    for k in range(2,11):
        w=coded(k)
        assert sum(w)==2**k-2
        assert separates(w)
        values={int(intensity(w,s)) for s in all_signs(k)}
        expected={4*j*j for j in range(2**(k-1))}
        assert values==expected
        out["coded"].append({"k":k,"weights":list(w),"classes":len(values),
                             "min_value":min(values),"max_value":max(values),
                             "min_gap":min(b-a for a,b in zip(sorted(values),sorted(values)[1:]))})
        if k<=8:
            out["cut_checks"]+=check_cut_identity(k)
    out["brute_minima"]={str(k):brute_first(k) for k in range(2,5)}
    assert all(out["brute_minima"][str(k)]["sum"]==2**k-2 for k in range(2,5))
    uniform=(Fraction(1),)*3
    a=(1,1,-1);b=(1,-1,1)
    assert intensity(uniform,a)==intensity(uniform,b)==1
    assert full_gram(a)!=full_gram(b)
    out["connected_support_nonseparating_witness"]={"k":3,"weights":[1,1,1],
        "signs_a":list(a),"signs_b":list(b),"shared_intensity":1}
    magnitudes=[Fraction(1,2),Fraction(2,3),Fraction(5,4),Fraction(7,6)]
    w=coded(4)
    c=[Fraction(w[i],1)/magnitudes[i] for i in range(4)]
    assert tuple(c[i]*magnitudes[i] for i in range(4))==w
    out["rational_compilation"]={"magnitudes":[str(x) for x in magnitudes],
                                 "control_coefficients":[str(x) for x in c]}
    out["checks"]="PASS"
    print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
