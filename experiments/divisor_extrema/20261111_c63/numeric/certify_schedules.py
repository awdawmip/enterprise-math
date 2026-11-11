"""Exact lower-bound certificates for the C62 finite schedule minimum.

Run: python3 certify_schedules.py 32 -o certificates.json
Uses only the Python standard library; every comparison uses integers or Fraction.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, gcd, lcm
from pathlib import Path


def block_maps(r: int, c: int):
    """Yield integer coefficients (A,B,C) of F(u)=A/[A+C+(B-C)u]."""
    K = 2*r + 1
    hidden = [Fraction(1)] * 3
    for n in range(c, 1, -1):
        # n is the stock still present after the hidden run.
        d0 = Fraction(4*K+n, 4)
        d1, d2 = K+n, K+4*n
        a = 7*hidden[0] / (d0*(d1-1))
        b = hidden[1] / (d1*(d2-1))
        h = hidden[2] / (d2*(d2-1))
        scale = lcm(a.denominator, b.denominator, h.denominator)
        yield tuple(x.numerator * (scale//x.denominator) for x in (a,b,h))
        # The common numerator n cancels in the next three weights.
        hidden[0] /= 4*K+n
        hidden[1] /= K+n
        hidden[2] *= Fraction(4, K+4*n)


def derivative_lower(mobius):
    a, b, h = mobius
    return Fraction(a*abs(b-h), (a+max(b,h))**2)


def apply_map(mobius, u):
    a, b, h = mobius
    return a/(a+h+(b-h)*u)


def terminal_lower(stock):
    # Derivative in TV of normalized (7*l0, u*l1, (1-u)*l2).
    l0 = l1 = l2 = Fraction(1)
    for n in range(3, stock+1):
        l0 *= Fraction(n,n+4)
        l1 *= Fraction(n,n+1)
        l2 *= Fraction(4*n,4*n+1)
    return l2*(7*l0+l1)/(7*l0+l2)**2


def top_two(items):
    # A path has a distinct first m or a distinct sibling suffix.
    lo = hi = None
    for item in items:
        if lo is None or item < lo:
            lo, hi = item, lo
        elif hi is None or item < hi:
            hi = item
    return [x for x in (lo,hi) if x is not None]


def compute(max_k, cut_output=None):
    """Retain the two smallest products over distinct paths, at every state."""
    data = {c: [(terminal_lower(c), (c-2,))] for c in range(2,max_k+2)}
    matrix = (1,0,0,1)  # S(u)=(p*u+q)/(s*u+t)
    ahead_maps = {}
    results = []
    for r in range(1, max_k):
        current = {}
        for c in range(2, max_k+2):
            candidates = []
            for m, mobius in enumerate(block_maps(r,c)):
                if c == r+1 and m == (0 if r==1 else 1):
                    ahead_maps[r] = mobius
                bound = derivative_lower(mobius)
                for value, suffix in data[c-m]:
                    candidates.append((value*bound,(m,)+suffix))
            current[c] = top_two(candidates)
        data = current
        # Compose S_old with F_r on the right: an incoming interval can be
        # arbitrarily short or anywhere inside [0,1].
        a, b, h = ahead_maps[r]
        p, q, s, t = matrix
        matrix = (q*(b-h), p*a + q*(a+h), t*(b-h), s*a + t*(a+h))
        common = gcd(*matrix)
        p, q, s, t = matrix = tuple(x//common for x in matrix)
        suffix_upper = Fraction(abs(p*t-q*s),8*min(t,s+t)**2)
        if r==63 and cut_output is not None:
            cut_rows = []
            for stock in range(2,97):
                canonical_suffix = (1,)*(r-1)+(0,0)
                # When stock differs from 64 there is no canonical suffix with
                # this inventory. Compare every path at these stocks.
                value, path = next((value, path) for value, path in current[stock]
                                   if stock != r+1 or path != canonical_suffix)
                ratio = value/suffix_upper
                cut_rows.append(dict(stock=stock, lower=[str(value.numerator),str(value.denominator)],
                                     ratio_floor=ratio.numerator//ratio.denominator,
                                     weighted_ratio_floor=(ratio*Fraction(16)**(stock-64))//1,
                                     witness=list(path)))
            cut_output.write_text(json.dumps(dict(remaining_pairs=r,
                ahead_derivative_sup=[str(suffix_upper.numerator),str(suffix_upper.denominator)],
                rows=cut_rows),indent=2)+'\n', encoding='utf-8')
        k = r+1
        final = top_two((value,(k+1-c,)+suffix)
                        for c in range(2,k+2) for value,suffix in data[c])
        ahead = (1,)*(k-1)+(0,0)
        u, v = Fraction(1), Fraction(0)
        for j in range(r,0,-1):
            u, v = apply_map(ahead_maps[j],u), apply_map(ahead_maps[j],v)
        delta = abs(u-v)/8
        competitors = [value for value,word in final if word != ahead]
        ratio = min(competitors)/delta
        # If ahead is the least bound, the runner-up covers every competitor.
        # Otherwise the least bound itself covers them.
        suffix_ahead = ahead[1:]
        suffix_competitors = [value for value,word in current[r+1] if word != suffix_ahead]
        suffix_competitor_lower = min(suffix_competitors, default=None)
        uniform_ratio = suffix_competitor_lower/suffix_upper if suffix_competitors else None
        results.append(dict(k=k, covered_schedules=str(comb(2*k-1,k)),
                            ahead_is_first_bound=final[0][1]==ahead,
                            unique_ahead_certified=ratio>1,
                            floor_competitor_bound_over_ahead=ratio.numerator//ratio.denominator,
                            first_competitor_bound_schedule=list(next(word for value,word in final if word!=ahead)),
                            suffix_pairs=r,
                            arbitrary_incoming_interval_certified=uniform_ratio is None or uniform_ratio>1,
                            floor_suffix_competitor_lower_over_ahead_sup=(None if uniform_ratio is None
                                 else uniform_ratio.numerator//uniform_ratio.denominator),
                            exact_suffix_ahead_derivative_sup=[str(suffix_upper.numerator),str(suffix_upper.denominator)],
                            exact_suffix_competitor_lower=(None if not suffix_competitors else
                                 [str(suffix_competitor_lower.numerator),str(suffix_competitor_lower.denominator)]),
                            exact_ahead_delta=[str(delta.numerator),str(delta.denominator)],
                            exact_competitor_lower=[str(min(competitors).numerator),str(min(competitors).denominator)]))
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('max_k', type=int, nargs='?', default=32)
    parser.add_argument('-o','--output', type=Path)
    parser.add_argument('--cut-output',type=Path,
                        help='also write r=63, c=2,...,96 comparison (requires max_k>=95)')
    args = parser.parse_args()
    if args.cut_output is not None and args.max_k<95:
        parser.error('--cut-output requires max_k at least 95')
    if args.max_k<2:
        parser.error('max_k must be at least 2')
    result = compute(args.max_k,args.cut_output)
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for row in result:
        print(row['k'], row['unique_ahead_certified'], row['floor_competitor_bound_over_ahead'])
