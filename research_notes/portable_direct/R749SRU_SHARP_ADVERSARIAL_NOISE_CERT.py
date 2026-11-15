#!/usr/bin/env python3
"""R749SRU: exact L-infinity adversarial robustness for the 0,1,5 Walsh phase decoder.

Standard-library-only exact rational certificate. Independent of predecessor PR imports.
No floating-point arithmetic, stochastic approximation, or external solver.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
import json

WEIGHTS = (1, 1, 2, 3, 6)
READS = (0, 1, 5)
SMOOTH = (F(1, 6), F(1, 2), -F(115, 36), F(115, 6), -F(16315, 108))
PHASE = tuple(F(v, 36) for v in (455, -295, -25, 185, -25, -295))
SIGNATURES = tuple(tuple(PHASE[(a + h) % 6] for h in READS) for a in range(6))
LENGTH = 600

def counts():
    """Exact unbounded labeled-source coefficient DP, and strict-prefix totals."""
    c = [0] * LENGTH
    t = [0] * LENGTH
    c[0] = 1
    for index, weight in enumerate(WEIGHTS):
        for v in range(weight, LENGTH):
            t[v] += t[v - weight] + (c[v - weight] if index == 0 else 0)
            c[v] += c[v - weight]
    C, T = [0], [0]
    for v in range(LENGTH):
        C.append(C[-1] + c[v])
        T.append(T[-1] + t[v])
    return C, T

def independent_count(r):
    def rec(j, budget, marked):
        if j == len(WEIGHTS):
            return (1, marked)
        c = t = 0
        for k in range(budget // WEIGHTS[j] + 1):
            cc, tt = rec(j + 1, budget - k * WEIGHTS[j], marked + (k if j == 0 else 0))
            c += cc
            t += tt
        return c, t
    return rec(0, r - 1, 0)

def smooth_scaled(r):
    return sum(v * r ** (4 - i) for i, v in enumerate(SMOOTH))

def residual(r, C, T):
    return F(r ** 3 * T[r], C[r]) - smooth_scaled(r)

def pa(a, b):
    return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]

def pm(a, b):
    z = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return z

def ps(a, k):
    return [x * k for x in a]

def pp(a, k):
    z = [F(1)]
    for _ in range(k):
        z = pm(z, a)
    return z

def interpolate(ys):
    differences = list(map(F, ys))
    result = [F(0)]
    for k in range(len(ys)):
        basis = [F(1)]
        for i in range(k):
            basis = pm(basis, [-F(i), F(1)])
        result = pa(result, ps(basis, differences[0] / factorial(k)))
        differences = [differences[i + 1] - differences[i]
                       for i in range(len(differences) - 1)]
    return result

def evaluate(poly, n):
    return sum(x * n**i for i, x in enumerate(poly))

def positive_tail_certificate(C, T):
    """Rebuild prior all-r strict bound from exact 6-quasipolynomial identities."""
    rows = []
    for a in range(6):
        start = next(r for r in range(512, 518) if r % 6 == a)
        cp = interpolate([C[start + 6*n] for n in range(6)])
        tp = interpolate([T[start + 6*n] for n in range(7)])
        assert all(evaluate(cp, n) == C[start + 6*n] and
                   evaluate(tp, n) == T[start + 6*n] for n in range(8))
        rp = [F(start), F(6)]
        expected = [PHASE[a]]
        for j, coef in enumerate(SMOOTH):
            expected = pa(expected, ps(pp(rp, 4-j), coef))
        numerator = pa(pm(pp(rp, 3), tp), ps(pm(cp, expected), -1))
        upper = pa(ps(cp, F(35, 12)), ps(numerator, -1))
        while numerator[-1] == 0: numerator.pop()
        while upper[-1] == 0: upper.pop()
        assert (len(cp),len(tp),len(numerator),len(upper)) == (6,7,5,6)
        assert all(x > 0 for x in cp + numerator + upper)
        rows.append({'phase':a,'start':start,
                     'C_degree':5,'numerator_degree':4,'upper_degree':5,
                     'minimum_positive_coefficient':str(min(cp + numerator + upper))})
    return rows

def cone_radius(y, A, B):
    """Exact L-inf distance to {z: ||z-B||_inf <= ||z-A||_inf}.

    Union of cones indexed by the active A-coordinate i and its sign sigma.
    Each cone is a system of linear halfspaces; the formula below eliminates z.
    """
    best = None
    for i in range(len(y)):
        signs = (1, -1) if A[i] == B[i] else ((1,) if B[i] > A[i] else (-1,))
        for sigma in signs:
            midpoint = (A[i] + B[i]) / 2
            lower = [F(0), sigma * (midpoint-y[i])]
            lower.extend((abs(y[j]-B[j])-sigma*(y[i]-A[i]))/2
                         for j in range(len(y)) if j != i)
            candidate = (max(lower), i, sigma)
            if best is None or candidate[0] < best[0]:
                best = candidate
    return best

def main():
    C,T = counts()
    for r in range(1,25):
        assert (C[r],T[r]) == independent_count(r)
    tail = positive_tail_certificate(C,T)
    sep = min(max(abs(x-z) for x,z in zip(SIGNATURES[a], SIGNATURES[b]))
              for a in range(6) for b in range(a+1,6))
    assert sep == F(15,2)
    tail_guaranteed_radius = sep/2 - F(35,12)
    assert tail_guaranteed_radius == F(5,6)
    candidate = None
    finite_margins = []
    for r in range(35,512):
        y = tuple(residual(r+h,C,T) for h in READS)
        true = r%6
        A = SIGNATURES[true]
        d_true = max(abs(y[i]-A[i]) for i in range(len(READS)))
        rival_distances = [max(abs(y[i]-SIGNATURES[b][i]) for i in range(len(READS)))
                           for b in range(6) if b != true]
        margin = min(rival_distances) - d_true
        assert margin > 0, (r,margin)
        finite_margins.append((margin, r))
        for b in range(6):
            if b == true: continue
            radius,i,sigma = cone_radius(y,A,SIGNATURES[b])
            entry = (radius,r,b,i,sigma)
            if candidate is None or entry < candidate: candidate = entry
    radius,r,b,i,sigma = candidate
    assert (r,b,i,sigma) == (36,3,1,1)
    assert radius == F(1118645,45039528)
    assert radius < tail_guaranteed_radius
    y = tuple(residual(r+h,C,T) for h in READS)
    eta = (-radius, radius, F(0))
    z = tuple(y[j]+eta[j] for j in range(3))
    d_a = max(abs(z[j]-SIGNATURES[r%6][j]) for j in range(3))
    d_b = max(abs(z[j]-SIGNATURES[b][j]) for j in range(3))
    assert d_a == d_b and max(map(abs,eta)) == radius
    assert min(finite_margins)[1] == 36
    return {'status':'PASS', 'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'predecessor':'R749SRT@990a7324b1950fd0d31ae3b07313c87e2c3e3303',
            'model':list(WEIGHTS),'read_set':list(READS),
            'definition':'adversarial L-infinity perturbation of all exact scaled residual readings; unique nearest among six ideal phase signatures',
            'claim':'For every integer r>=35, all ||eta||_infty < rho yield correct phase; at rho an explicit r=36 perturbation causes a tie; this rho is the sharp uniform strict guarantee.',
            'exact_sharp_noise_radius':str(radius), 'attaining_r':r,
            'true_phase':r%6,'rival_phase':b,
            'r36_observation':[str(v) for v in y],
            'witness_eta':[str(v) for v in eta],
            'witness_tied_distance':str(d_a),
            'finite_range':[35,511], 'finite_r_count':477,
            'finite_rival_cones':477*5,
            'minimum_finite_gap':[str(x) for x in min(finite_margins)],
            'tail_range':'all r>=512',
            'tail_strict_error':'0 < R(r)-P(r mod 6) < 35/12',
            'tail_guaranteed_radius':str(tail_guaranteed_radius),
            'tail_positive_polynomials':tail,
            'independent_direct_recursions':24,
            'review':'AUTHOR_EXACT_NOT_REVIEWED'}

if __name__ == '__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
