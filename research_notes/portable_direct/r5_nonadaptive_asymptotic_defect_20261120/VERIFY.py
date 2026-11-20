#!/usr/bin/env python3
"""R5 fixed-m rare-witness theorem: exact integer and rational checks.
Standalone stdlib: python VERIFY.py; optionally --archive PATH for frozen-input checks.
"""
import argparse
import hashlib
import json
import zipfile
from fractions import Fraction
from math import comb, factorial, prod
from pathlib import Path

PRICES = list(range(214, 315))
SETS = [set(range(214, 219)), {214, *range(216, 222)},
        {215, *range(216, 222)}, set(range(223, 291)), set(range(296, 313))]
S0 = SETS[0]
REST = [p for p in PRICES if p not in S0]
P = prod(PRICES)
P_REST = prod(REST)
S1 = sum(PRICES)
S2 = sum(k**2 for k in PRICES)
S4 = sum(k**4 for k in PRICES)
S6 = sum(k**6 for k in PRICES)
S0SUM = sum(S0)
SRESTSUM = sum(REST)


def unbounded(prices, nmax):
    a = [0] * (nmax + 1)
    a[0] = 1
    for p in prices:
        for n in range(p, nmax + 1):
            a[n] += a[n-p]
    return a


def m1_with_masks(nmax):
    # Independent five-mask DP; each price has unbounded multiplicity.
    dp = [[0] * (nmax + 1) for _ in range(32)]
    dp[0][0] = 1
    for p in PRICES:
        bitmask = sum(1 << i for i, witness in enumerate(SETS) if p in witness)
        nxt = [row[:] for row in dp]  # zero copies of this price
        for n in range(p, nmax+1):
            for old_mask in range(32):
                v = nxt[old_mask][n-p]
                if v:
                    nxt[old_mask | bitmask][n] += v
        dp = nxt
    return dp[31]


def laurent_coefficients():
    # Multiply the 101 factors (kx/2)/sinh(kx/2) through x^6.
    c2 = c4 = c6 = Fraction(0)
    for k in PRICES:
        g2 = -Fraction(k**2, 24)
        g4 = Fraction(7*k**4, 5760)
        g6 = -Fraction(31*k**6, 967680)
        c2, c4, c6 = c2+g2, c4+c2*g2+g4, c6+c4*g2+c2*g4+g6
    assert c2 == -Fraction(S2, 24)
    assert c4 == Fraction(5*S2**2+2*S4, 5760)
    assert c6 == -(Fraction(S6, 181440)+Fraction(S2*S4, 69120)+Fraction(S2**3, 82944))
    return [str(c2), str(c4), str(c6)]


def simplex_moments(m):
    num = comb(m+4, 5)
    moment = comb(m+4, 6) if m > 1 else 0
    if m <= 4:
        vectors = []
        for a in range(m):
            for b in range(m-a):
                for c in range(m-a-b):
                    for d in range(m-a-b-c):
                        for e in range(m-a-b-c-d):
                            vectors.append((a,b,c,d,e))
        assert len(vectors) == num
        assert all(sum(v[i] for v in vectors) == moment for i in range(5))
    return {'m':m, 'B':num, 'C':moment,
            'defect_N95_coefficient':str(Fraction(num, factorial(95)*P_REST)),
            'defect_N94_coefficient':str(Fraction(12792*num-1080*moment, factorial(94)*P_REST))}


def inspect_archive(path, feasible):
    sha = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
    with zipfile.ZipFile(path) as z:
        assert hashlib.sha256(z.read('EXACT_R5_ALL_101_BUDGETS.json')).hexdigest() == sha
        earlier = json.loads(z.read('RESULT_R5_MIXED_ERASURE_RIGIDITY.json'))
        assert [set(a) for a in earlier['minimal_sets']] == SETS
        prior = json.loads(z.read('RESULT_R5_GLOBAL_RATIONAL.json'))
    for d, value in prior['samples']['1']['coefficients_425_430'].items():
        assert feasible[735+int(d)] == int(value)
    return {'input_sha256':sha,'five_witness_sets_match':True,'six_prior_coefficients_match':True}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--max-n', type=int, default=1800)
    p.add_argument('--archive', type=Path)
    args = p.parse_args()
    nmax = args.max_n
    assert nmax >= 1165
    unrestricted = unbounded(PRICES, nmax)
    invalid_s0 = unbounded(REST, nmax)  # m=1, no S0 queries permitted
    feasible = m1_with_masks(nmax)
    assert feasible[735] == 1 and all(z == 0 for z in feasible[:735])
    assert all(0 <= f <= u-a for u, a, f in zip(unrestricted, feasible, invalid_s0))
    output = {
        'status': 'PASS_AUTHOR_FINITE_CHECK',
        'model': '256 labels; frozen five minimal witness subsets; nonadaptive multiset',
        'm1_cost_range': [0, nmax],
        'exact_m1_minimum': 735,
        'witness_cardinalities': [len(s) for s in SETS],
        'constants': {'S1':S1,'S2':S2,'S4':S4,'S6':S6,'S0_sum':S0SUM,'S_rest_sum':SRESTSUM,
                      'P_digits':len(str(P)),'P_rest_digits':len(str(P_REST))},
        'laurent_g_coefficients_deg2_4_6': laurent_coefficients(),
        'simplex_moments': [simplex_moments(m) for m in (1,2,3,4,17)],
        'samples': {str(n):{'unrestricted':str(unrestricted[n]),'valid_m1':str(feasible[n]),
                            'invalid':str(unrestricted[n]-feasible[n]),
                            'invalid_s0':str(invalid_s0[n]),
                            'other_invalid_net':str(unrestricted[n]-feasible[n]-invalid_s0[n])}
                    for n in (735,1160,1162,1165,1500,1800) if n <= nmax}
    }
    if args.archive:
        output['frozen_archive_crosscheck'] = inspect_archive(args.archive, feasible)
    (Path(__file__).resolve().parent/'RESULT.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print('PASS', 'm1 exact complete through N='+str(nmax),
          'frozen source checked='+str(bool(args.archive)),
          'leading correction factor m=2:', comb(6,5))

if __name__ == '__main__':
    main()
