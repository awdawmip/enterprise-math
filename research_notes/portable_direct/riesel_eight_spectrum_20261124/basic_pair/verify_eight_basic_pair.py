#!/usr/bin/env python3
"""Exact new arithmetic for the all-prime forced-basic-pair theorem at budget 8."""
from collections import Counter
from fractions import Fraction as F
import json
from math import isqrt, lcm, prod
from pathlib import Path

H = {0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,
     55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100}
FACTORS32 = (3,5,17,257,65537)


def prime(n):
    return n >= 2 and all(n % d for d in range(2,isqrt(n)+1))


def main():
    assert prod(FACTORS32) == 2**32-1
    assert all(prime(q) for q in FACTORS32)
    incidence = Counter(h % 7 for h in H)
    maximal = [c for c in range(7) if incidence[c] == 7]
    assert maximal == [0,1,2]
    assert all(sum(h % 7 == c and h % 3 == 1 for h in H) == 3
               for c in maximal)
    bounds = {1:F(1,11),3:F(23,216),5:F(11,144),7:F(7,72),
              15:F(1,12),21:F(1,9),35:F(1,18),105:F(1,36)}
    assert all(v <= F(1,9) for v in bounds.values())
    capacity = {29:F(7,36),43:F(7,36),61681:F(11,72),
                19:F(13,108),73:F(13,108)}
    unrestricted = sum(capacity.values())+2*F(1,9)
    assert unrestricted == F(217,216)
    missing = {q:unrestricted-v+F(1,9) for q,v in capacity.items()}
    assert max(missing.values()) == F(215,216) < 1
    assert unrestricted-F(1,36) == F(211,216) < 1
    neither = F(21+13+13+5*12,108)
    assert neither == F(107,108) < 1
    period = lcm(105,2,9)
    overlaps = []
    for parity in (0,1):
        holes = [u for u in range(period) if u % 105 in H and u % 2 == parity]
        assert len(holes) == 108
        for w_phase in (1,4):
            whits = {u for u in holes if u % 9 == w_phase}
            assert F(len(whits),len(holes)) == F(13,108)
            for c in maximal:
                qhits = {u for u in holes if u % 7 == c}
                assert F(len(qhits),len(holes)) == F(7,36)
                intersection = len(qhits & whits)
                assert intersection == 3
                assert F(intersection,len(holes)) == F(1,36)
                overlaps.append({'u_parity':parity,'u_phase_mod9':w_phase,
                                 'u_phase_mod7':c,'hole_count':len(holes),
                                 'intersection_count':intersection})
    density_gap = F(3,35)*(1-F(215,216))
    assert density_gap == F(1,2520)
    assert F(6,35)*(1-neither) == F(1,630) >= density_gap
    result = {
        'status':'PASS_AUTHOR_EXACT_ARITHMETIC_NOT_INDEPENDENT_REVIEW',
        'statement':'Every complete supplement of at most eight primes on R1 contains 5 and 13.',
        'factorization32':FACTORS32,
        'maximal_mod7_classes':maximal,
        'generic_column_bounds':{str(g):str(v) for g,v in bounds.items()},
        'unrestricted_sum':str(unrestricted),
        'upper_bounds_if_exception_absent':{str(q):str(v) for q,v in missing.items()},
        'overlap_period':period,'exact_overlaps':overlaps,
        'global_gap_lower_bound_if_one_basic_prime_missing':str(density_gap),
        'all_prime_argument':'eight_basic_pair_proof.md',
    }
    target=Path(__file__).with_name('eight_basic_pair_certificate.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','certificate':str(target),'overlap_cases':len(overlaps),
                      'gap':str(density_gap)}))


if __name__ == '__main__':
    main()
