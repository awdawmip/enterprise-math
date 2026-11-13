#!/usr/bin/env python3
"""R137C — exact coefficient-period word inclusion certificate."""
from math import gcd, lcm
from check_r137b import farey_witnesses

def phi(q):
    return sum(gcd(i,q)==1 for i in range(1,q+1))

def run():
    n = 0
    for m in range(1,9):
        P = lcm(*range(1,m+1))
        F = 1 + sum((m+1-q)*phi(q) for q in range(1,m+1))
        for K in range(2,25):
            before = set(farey_witnesses(K,m))
            after = set(farey_witnesses(K+P,m))
            assert before <= after,(m,K,before-after)
            assert len(after) == F,(m,K,len(after),F)
            n += 1
    assert n==184
    print("R137C_COEFFICIENT_PERIOD_INCLUSION_PASS")
    print({"exact_pairs":n,"m_range":[1,8],"K_range":[2,24]})

if __name__=="__main__":
    run()
