"""Exact C78/C87 physical inventory readouts using finite rational operations.

Source snapshot: awdawmip/enterprise-math@63eec225728612d1df6c178b516b5ecf4687ee06.
Closed kernel: C78/critical_bins.py; positive path: C78/check_finite.py.
This file contains no Gamma, logarithm, floating-point arithmetic or roots.
"""

from collections import Counter
from fractions import Fraction as Q
from functools import cache
from math import prod

SOURCE_COMMIT = "63eec225728612d1df6c178b516b5ecf4687ee06"
TAILS = ((5, 5, 7), (5, 7, 5), (7, 5, 5))
TAIL_COEFFICIENTS = ((Q(3, 32), Q(15, 32)),
                     (Q(3, 2), Q(15, 8)), (Q(6), Q(3)))
RATES = (Q(1, 4), Q(1), Q(4))


@cache
def prefix(k, n):
    return prod((Q(4*j+k, 4*(j+k)) for j in range(1, n+1)), start=Q(1))


@cache
def block_coefficients(n, s, k):
    """Return rho,tau for s<=n, k in the original block types 3,5."""
    rho = 4 * prefix(k, n) / prefix(k, s-1)
    factor = Q(28*(k-1+4*s)*prod(range(s+k, s+4*k)),
               (k-1+s)*prod(range(n+k+1, n+4*k+1)))
    return rho, rho*factor


def block(z, n, s, k):
    rho, tau = block_coefficients(n, s, k)
    return (rho+tau*z)/(1+tau*z)


@cache
def terminal_scores(w):
    amplitude = prefix(1, w)/prefix(1, 2)
    t = Q(840, (w+2)*(w+3)*(w+4))
    return tuple(amplitude*(t*a+b)/(1+amplitude*t*a)
                 for a, b in TAIL_COEFFICIENTS)


def kernel_tail_ratios(n, v, w):
    if not 2 <= w <= v <= n:
        raise ValueError("Require 2 <= w <= v <= n")
    return tuple(block(block(z, v, w, 3), n, v, 5)
                 for z in terminal_scores(w))


def consume(masses, stock, symbol):
    """One exact positive-state step; stock is updated in place."""
    weighted = tuple(mass*stock[symbol]*(rate if symbol == 5 else 1)
                     /(stock[2]+stock[3]+rate*stock[5]+stock[7])
                     for rate, mass in zip(RATES, masses))
    stock[symbol] -= 1
    x, y, z = weighted
    if symbol == 2:
        return Q(0), x, y+z
    if symbol == 3:
        return (7*(x+y+z)+x)/8, y/8, z/8
    return weighted


def positive_path_tail_probabilities(n, v, w, preparation):
    if not 2 <= w <= v <= n or preparation not in (0, 1):
        raise ValueError("Require 2 <= w <= v <= n and preparation in {0,1}")
    stock = {2: 2, 3: 2, 5: n, 7: 1}
    state = (Q(7, 8), Q(preparation, 8), Q(1-preparation, 8))
    body = [5]*(n-v)+[2, 3]+[5]*(v-w)+[2, 3]+[5]*(w-2)
    for symbol in body:
        state = consume(state, stock, symbol)
    result = []
    for tail in TAILS:
        tail_state, tail_stock = state, stock.copy()
        for symbol in tail:
            tail_state = consume(tail_state, tail_stock, symbol)
        result.append(sum(tail_state))
    assert sum(result) == sum(state)
    return tuple(result)


def positive_path_tail_ratios(n, v, w):
    a = positive_path_tail_probabilities(n, v, w, 0)
    b = positive_path_tail_probabilities(n, v, w, 1)
    return tuple(y/x for x, y in zip(a, b))


def readout(n, v, w):
    values = kernel_tail_ratios(n, v, w)
    return max(values)/min(values)


def shifted_bin(value, precision, offset=Q(0)):
    """Original half-open output grid floor(2**p*g + offset)."""
    shifted = value*Q(2)**precision+offset
    return shifted.numerator//shifted.denominator


def unique_count(c, stocks, precision, offsets=None):
    """Compare all original c-templates at the requested larger stocks."""
    if any(n < c for n in stocks):
        raise ValueError("Extra 5s must precede the first 23, so n >= c")
    offsets = (Q(0),)*len(stocks) if offsets is None else offsets
    if len(offsets) != len(stocks):
        raise ValueError("One grid offset is required per stock")
    counts = Counter(tuple(shifted_bin(readout(n, v, w), precision, off)
                           for n, off in zip(stocks, offsets))
                     for v in range(2, c+1) for w in range(2, v+1))
    return sum(m == 1 for m in counts.values())


if __name__ == "__main__":
    for n, v, w in ((2, 2, 2), (8, 6, 3), (16, 6, 3)):
        a, b = kernel_tail_ratios(n, v, w), positive_path_tail_ratios(n, v, w)
        print((n, v, w), "equal_tail_ratios", a == b,
              "common_scale", tuple(x/y for x, y in zip(a, b)))
