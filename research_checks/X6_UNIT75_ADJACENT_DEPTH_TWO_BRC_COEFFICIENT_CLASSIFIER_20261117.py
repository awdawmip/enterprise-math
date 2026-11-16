#!/usr/bin/env python3
"""X6 Unit75 exact six-axis positive uniform-BRC two-coefficient audit.

For all sorted six-tuples in [-M,M]^6, enumerate distinct depth-translated
states with identical can6, G, T, and shortest N_BRC. Compare the first
extra-backtrack coefficient. A permutation class is counted once.

Proof kernel in accompanying research note; arithmetic uses Python integers
and Fraction only, no floating arithmetic or removable asserts.
"""
import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction


def reciprocal_sum(abs_components):
    return sum((Fraction(1, u + 1) for u in abs_components), Fraction(0, 1))


def check_adjacent_positive_triple(a, b):
    """Independent exact elementary-symmetric check for c=1 candidates.

    Input a,b are positive triples A_i=z_i+1 on the >=0 positions,
    B_i=-z_i on negative positions, with sum(A)=sum(B).
    """
    if len(a) != 3 or len(b) != 3 or min(*a, *b) < 1:
        raise ValueError("not two positive triples")
    S = sum(a)
    P = math.prod(a)
    if S != sum(b) or P != math.prod(b):
        raise ValueError("preconditions S,P equality not met")

    def e2(v):
        return v[0]*v[1] + v[0]*v[2] + v[1]*v[2]

    def F_direct(v):
        return sum((Fraction(1, t * (t + 1)) for t in v), Fraction(0))

    def F_formula(E):
        return Fraction(E, P) - Fraction(E + 2*S + 3, P + E + S + 1)

    ea, eb = e2(a), e2(b)
    fa, fb = F_direct(a), F_direct(b)
    if fa != F_formula(ea) or fb != F_formula(eb):
        raise RuntimeError("exact rational F(E) identity failed")
    if (fa == fb) != (ea == eb):
        raise RuntimeError("strict F(E) criterion failed")
    if (ea == eb) != (sorted(a) == sorted(b)):
        raise RuntimeError("equal e1,e2,e3 triples failed")
    return True


def census(M):
    fac = [math.factorial(i) for i in range(M+1)]
    stats = {
        "max_coordinate_abs": M,
        "sorted_six_tuples_scanned": 0,
        "G_equal_distinct_depth_pairs": 0,
        "G_T_equal_pairs": 0,
        "G_T_shortest_mass_equal_pairs": 0,
        "different_absolute_multiset_pairs": 0,
        "different_abs_but_first_backtrack_equal": 0,
        "adjacent_depth_shortest_equal_pairs": 0,
        "adjacent_depth_different_abs_pairs": 0,
        "adjacent_depth_adjacent_triple_criterion_checks": 0,
    }
    examples=[]
    for z in itertools.combinations_with_replacement(range(-M, M+1), 6):
        stats["sorted_six_tuples_scanned"] += 1
        s = sum(z)
        if s >= 0 or s % 3:
            continue
        c = -s // 3
        if z[-1] + c > M:
            continue
        y = tuple(u+c for u in z)
        if sum(u*u for u in y) != sum(u*u for u in z):
            raise RuntimeError("G exact translation condition failed")
        stats["G_equal_distinct_depth_pairs"] += 1
        az = tuple(abs(u) for u in z)
        ay = tuple(abs(u) for u in y)
        if sum(az) != sum(ay):
            continue
        stats["G_T_equal_pairs"] += 1
        prodz = math.prod(fac[u] for u in az)
        prody = math.prod(fac[u] for u in ay)
        if prodz != prody:
            continue
        stats["G_T_shortest_mass_equal_pairs"] += 1
        shortest = math.factorial(sum(az)) // prodz
        if c == 1:
            stats["adjacent_depth_shortest_equal_pairs"] += 1
            positive = tuple(u+1 for u in z if u >= 0)
            negative = tuple(-u for u in z if u < 0)
            if len(positive) != 3 or len(negative) != 3:
                raise RuntimeError("adjacent-depth T requires exactly 3 positive/3 negative sectors")
            check_adjacent_positive_triple(positive, negative)
            stats["adjacent_depth_adjacent_triple_criterion_checks"] += 1
        same_abs = sorted(az) == sorted(ay)
        fz, fy = reciprocal_sum(az), reciprocal_sum(ay)
        if (fz == fy) != (same_abs):
            stats["different_abs_but_first_backtrack_equal"] += 1
            if len(examples) < 5:
                examples.append({"z":z,"y":y,"c":c,"first_backtrack_reciprocal_difference":str(fy-fz)})
        if not same_abs:
            stats["different_absolute_multiset_pairs"] += 1
            if c == 1:
                stats["adjacent_depth_different_abs_pairs"] += 1
    if stats["different_abs_but_first_backtrack_equal"]:
        raise RuntimeError("FOUND COUNTEREXAMPLE / first-backtrack criterion: " + str(examples))
    return stats


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--max-M",type=int,default=20)
    p.add_argument("--output",default="")
    a=p.parse_args()
    if not (1 <= a.max_M <= 28):
        raise ValueError("max-M must be 1..28 (declared finite census)")
    caps=sorted(set([m for m in [8,12,16,20,24,28] if m<=a.max_M] + [a.max_M]))
    results=[census(m) for m in caps]
    out={
        "schema":"ENTERPRISE_MATH_X6_UNIT75_EXACT_ADJACENT_TWO_COEFFICIENT_CERT_V1",
        "scientific_model":"signed native X6, P000 V5, six named signed integer step axes",
        "scope":"sorted coordinate-permutation representatives; every integer six-tuple in [-M,M]^6 modulo axis permutations, both translated states within cube; finite census only",
        "proof":"independent math note; c=1 universal necessity/sufficiency not inferred from finite scan",
        "max_M":a.max_M,
        "results":results,
        "failure_count":0,
        "python_optimization_mode":sys.flags.optimize,
        "numerical_semantics":"exact integer factorial products and fractions; no floats",
    }
    canonical=json.dumps({k:v for k,v in out.items() if k != 'python_optimization_mode'},sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
    out["semantic_sha256_excluding_python_optimization_mode"]=hashlib.sha256(canonical).hexdigest()
    text=json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    if a.output:
        with open(a.output,'w',encoding='utf-8') as f:f.write(text)
    print(text)


if __name__ == '__main__':
    main()
