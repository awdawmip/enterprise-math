"""Certify a physical single-g fiber against every word at a fixed two-block stock."""
from itertools import permutations
from math import isqrt, prod
import json

import numpy as np
from blind_center_decoder import simulate

P = 1_000_003


def inverse(n):
    return pow(int(n) % P, -1, P)


def rising(n, k):
    return prod(range(n, n + k)) % P


def tables(k, stock):
    prefix = [1]
    for n in range(1, stock + 1):
        prefix.append(prefix[-1] * (4*n+k) * inverse(4*(n+k)) % P)
    lower_rate = []
    lower_scale = []
    upper_scale = []
    for v in range(2, stock + 1):
        lower_rate.append(4 * inverse(prefix[v-1]) % P)
        lower_scale.append(28*(k-1+4*v)*rising(v+k,3*k)*inverse(k-1+v) % P)
        upper_scale.append(inverse(rising(v+k+1,3*k)))
    return [np.array(row, dtype=np.int64) for row in
            (prefix[2:],lower_rate,lower_scale,upper_scale)]


def terminal_columns(stock):
    nums, dens = [], []
    for a, b in [(3,15),(48,60),(192,96)]:
        ns, ds = [], []
        y = 1
        for w in range(2, stock+1):
            if w > 2:
                y = y*(4*w+1)*inverse(4*(w+1)) % P
            j = (w+2)*(w+3)*(w+4) % P
            ns.append(y*(840*a+j*b) % P)
            ds.append((32*j + 840*a*y) % P)
        nums.append(ns)
        dens.append(ds)
    return np.array(nums, dtype=np.int64), np.array(dens, dtype=np.int64)


def all_matches(stock, observed):
    if 4*stock+30 >= P:
        raise ValueError("this prime is chosen for the bundled test stocks")
    large, inv_large, first_factor, outer = tables(5, stock)
    small, inv_small, second_factor, inner = tables(3, stock)
    tail_num, tail_den = terminal_columns(stock)
    g_num, g_den = observed.numerator % P, observed.denominator % P
    confirmed = []
    candidates = 0
    for v in range(2, stock+1):
        idx = v-2
        subset = slice(0, v-1)
        rho = small[idx]*inv_small[subset] % P
        tau = (rho*second_factor[subset] % P)*inner[idx] % P
        term = tail_num[:,subset]*tau % P
        num = (rho*tail_den[:,subset]+term) % P
        den = (tail_den[:,subset]+term) % P
        rho1 = large[-1]*inv_large[idx] % P
        tau1 = (rho1*first_factor[idx] % P)*outer[-1] % P
        correction = tau1*num % P
        num = (rho1*den+correction) % P
        den = (den+correction) % P
        possible = np.zeros(v-1,dtype=bool)
        # Projective cross products stay valid even if a column has a pole mod P.
        for i, j in permutations(range(3), 2):
            possible |= ((num[i]*den[j] % P)*g_den -
                         (den[i]*num[j] % P)*g_num) % P == 0
        for pos in np.flatnonzero(possible):
            w = int(pos)+2
            candidates += 1
            if simulate((stock-v,v-w,w-2))[0] == observed:
                confirmed.append((v,w))
    return candidates, confirmed


if __name__ == "__main__":
    assert all(P % d for d in range(2, isqrt(P)+1))
    # Exact check of the full modular survivor procedure at a small stock.
    for gaps in ((0,0,5), (1,3,1), (3,2,0)):
        c = sum(gaps)+2
        g = simulate(gaps)[0]
        full = [(v,w) for v in range(2,c+1) for w in range(2,v+1)
                if simulate((c-v,v-w,w-2))[0] == g]
        assert all_matches(c, g)[1] == full
    reports = []
    for gaps in ((450,505,470),(1250,1294,1352)):
        c = sum(gaps)+2
        g = simulate(gaps)[0]
        possibles, matches = all_matches(c, g)
        answer = (c-gaps[0],gaps[-1]+2)
        assert matches == [answer]
        reports.append(dict(stock=c, total_words=c*(c-1)//2, prime=P,
                            modular_candidates=possibles, exact_matches=matches))
    print(json.dumps(reports,indent=2))
