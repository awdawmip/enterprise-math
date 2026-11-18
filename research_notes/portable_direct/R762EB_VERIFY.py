#!/usr/bin/env python3
"""R762EB exact finite proof certificate for BRC cyclotomic strata.

Run: python3 R762EB_VERIFY.py > R762EB_EVIDENCE.json
Uses only integers and stdlib; no numerical roots or external mathematics packages.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb
import json

BRANCHES = ((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))


def lucas_mod3(n, m):
    """Lucas reduction for nonnegative integer n,m."""
    ans = 1
    while m:
        a, b = n % 3, m % 3
        if b > a:
            return 0
        ans = ans * comb(a, b) % 3
        n //= 3
        m //= 3
    return ans


def e_m(i,j,k,m,method="lucas"):
    """[t^m] sum_{b in B} (1+t)^((b.(i,j,k)) mod 27) modulo 3."""
    exps = ((u*i+v*j+w*k) % 27 for u,v,w in BRANCHES)
    if method == "lucas":
        return sum(lucas_mod3(e,m) for e in exps) % 3
    if method == "direct":
        return sum(comb(e,m) if e>=m else 0 for e in exps) % 3
    raise ValueError(method)


def main():
    for n in range(27):
        for m in range(27):
            want = comb(n,m)%3 if m <= n else 0
            assert lucas_mod3(n,m) == want, (n,m)
    hist18, hist27 = Counter(), Counter()
    low9 = Counter()
    deg18_bytes, deg27_bytes = bytearray(), bytearray()
    witnesses = {}
    # Explicit exhaustive enumeration is the finite lemma: 27^3 triples.
    for i,j,k in product(range(27),repeat=3):
        seq = tuple(e_m(i,j,k,m) for m in range(27))
        for m in range(27):
            assert seq[m] == e_m(i,j,k,m,"direct"), (i,j,k,m)
        a = next((m for m,v in enumerate(seq[:18]) if v),18)
        b = next((m for m,v in enumerate(seq) if v),27)
        assert a in (2,4,6,10,12,18), (i,j,k,a)
        assert b in (2,4,6,10,12,18,27), (i,j,k,b)
        hist18[a]+=1; hist27[b]+=1
        deg18_bytes.append(a);deg27_bytes.append(b)
        witnesses.setdefault(str(b),(i,j,k))
    assert hist18=={2:13122,4:3888,6:1782,10:432,12:144,18:315},hist18
    assert hist27=={2:13122,4:3888,6:1782,10:432,12:144,18:210,27:105},hist27
    assert sum(hist27.values()) == 27**3

    for i,j,k in product(range(9),repeat=3):
        c = next((m for m in range(9) if e_m(i,j,k,m)),9)
        assert c in (2,4,6,9)
        low9[c]+=1
    assert low9 == {2:486,4:144,6:66,9:33}

    lift10 = Counter()
    for i,j,k in product(range(9),repeat=3):
        if all(e_m(i,j,k,m)==0 for m in range(9)):
            nonzero = sum(e_m(i+9*a,j+9*b,k+9*c,10)!=0
                          for a,b,c in product(range(3),repeat=3))
            assert nonzero in (0,18)
            lift10[nonzero]+=1
    assert lift10 == {0:9,18:24}

    result = {
       "record":"R762EB_HIGHER_CYCLOTOMIC_STRATA",
       "date":"2026-11-18",
       "task":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
       "model":"P=1+X+Z+XY+YZ+XYZ over six named positive BRC branches, Q=3^a, pi=zeta_Q-1",
       "verification":"PASS",
       "exhaustive_domain":"all (i,j,k) in {0,...,26}^3 = 19683 triples",
       "exact_arithmetic":"Lucas mod 3; every one of 27 coefficients independently crosschecked by direct Python integer binomial",
       "lemma":"For m<27, the coefficient of pi^m modulo 3 depends only on (i,j,k) modulo 27, via Lucas. The expansion is in integer powers of pi.",
       "valuation_threshold_a_ge_3":"v_pi(3)=2*3^(a-1)>=18; first nonzero reduced coefficient at m<18 gives exact v_pi=m",
       "valuation_threshold_a_ge_4":"v_pi(3)=2*3^(a-1)>=54; first nonzero reduced coefficient at m<27 gives exact v_pi=m",
       "histogram_a_ge_3_at_degrees_2_4_6_10_12_or_at_least_18":{str(x):hist18[x] for x in (2,4,6,10,12,18)},
       "histogram_a_ge_4_at_degrees_2_4_6_10_12_18_or_at_least_27":{str(x):hist27[x] for x in (2,4,6,10,12,18,27)},
       "fraction_of_Q_cubed_a_ge_3":{"2":"2/3","4":"16/81","6":"22/243","10":"16/729","12":"16/2187","at_least_18":"35/2187"},
       "fraction_of_Q_cubed_a_ge_4":{"18":"70/6561","at_least_27":"35/6561"},
       "mod9_prefix_counts":{str(x):low9[x] for x in (2,4,6,9)},
       "mod9_deep_prefix_lift10_counts":{str(x):lift10[x] for x in (0,18)},
       "witnesses_by_leading_degree_or_lower_bound":witnesses,
       "byte_order":"outer i, middle j, inner k ascending; one byte per first nonzero mod3 coefficient degree, or threshold",
       "degree_table_sha256_a_ge_3":sha256(deg18_bytes).hexdigest(),
       "degree_table_sha256_a_ge_4":sha256(deg27_bytes).hexdigest(),
       "scientific_boundary":"Candidate BRC endpoint character spectrum only. No native signed Cell/Link/Port event license or independent review. a=2 exceptional due to v_pi(3)=6.",
       "next_question":"Classify the >=18 cases for a=3 with exact cyclotomic carry terms and the >=27 class for a>=4; separately relate to coefficient-content witnesses."
    }
    print(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False))


if __name__ == '__main__':
    main()
