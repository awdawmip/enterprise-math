#!/usr/bin/env python3
"""PREFIX-941 exact integer verification: brute-force versus quotient-first inverse."""
import json
Q = tuple(range(5, 64, 2))
KS = (1, 3, 5, 7, 9, 11, 13)
I = range(6)
per_k = {}
for k in KS:
    direct = set()
    for a in Q:
        for i in I:
            for j in I:
                d = (k*a ^ (1 << j)) - (1 << i)
                if d <= 0:
                    continue
                for b in Q:
                    if d % b == 0:
                        direct.add((a, b, i, j, d//b))
    inverse = set()
    tmax = (k*max(Q)+(1<<max(I)))//min(Q)+1
    for b in Q:
        for t in range(1, tmax+1):
            for i in I:
                y = t*b+(1<<i)
                for j in I:
                    h = 1<<j
                    e = 1 if y & h else -1
                    x = y-e*h
                    if x <= 0 or x % k:
                        continue
                    a = x//k
                    if a not in Q:
                        continue
                    assert ((k*a ^ h)-(1<<i)) == t*b
                    inverse.add((a,b,i,j,t))
    assert inverse == direct, (k, len(inverse), len(direct))
    assert all((t%2 == 1) == ((i==0)==(j==0)) for a,b,i,j,t in inverse)
    per_k[str(k)] = {
      "direct":len(direct),"inverse":len(inverse),"equal":True,
      "distinct_modulus_pairs":len({(a,b) for a,b,i,j,t in inverse}),
      "quotient_upper_bound":tmax}
out = {"schema":"PREFIX941_R6_QUOTIENT_FIRST_BIT_SIEVE_V1",
       "frozen_science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
       "domain":{"k":list(KS),"odd_a_b_inclusive":[5,63],"source_bits_inclusive":[0,5]},
       "results":per_k,"status":"ALL_EXACT_ASSERTIONS_PASSED"}
print(json.dumps(out,indent=2))
