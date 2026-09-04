#!/usr/bin/env python3
"""V22 algebra/support checks and optional numerical stress tests.

The universal real-variable barrier theorem is proved in the companion note.
This script does NOT constitute a formal verification of that theorem.
Exact checks use fractions.Fraction. Numerical stress tests are explicitly
separate and require NumPy/SciPy; they are not evidence for an asymptotic claim.
"""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as Q
from itertools import product
from pathlib import Path


def exact_checks() -> dict[str, object]:
    actions = (2, 3, 4, 5, 7)
    w = {a: Q((a % 3) + 1, a + 1) for a in actions}
    n = 35
    A = sum(w.values(), Q(0))
    p = {a: w[a] / A for a in actions}
    f = {0: Q(0), **{k: Q((k*k + 3*k) % 17 - 8, 9)
                       for k in range(1, n + 1)}}

    def mass(x: int) -> Q:
        return sum((w[a] for a in actions if a <= x), Q(0))

    def c2(x: int) -> Q:
        return sum((w[a]*w[b] for a, b in product(actions, repeat=2)
                    if a*b <= x), Q(0))

    def phi(a: int, b: int) -> int:
        return n // (a*b) if a*b <= n else n // a

    def mean_pair(F: dict[tuple[int, int], Q]) -> Q:
        return sum((p[a]*p[b]*F[a,b] for a,b in product(actions, repeat=2)), Q(0))

    count = 0
    d4 = Q(0)
    second = Q(0)
    for c in actions:
        F = {(a,b): f[phi(a,b)] + f[phi(a,b)//c]
             for a,b in product(actions, repeat=2)}
        row = {a: sum((p[b]*F[a,b] for b in actions), Q(0)) for a in actions}
        col = {b: sum((p[a]*F[a,b] for a in actions), Q(0)) for b in actions}
        m2 = mean_pair({k: v*v for k,v in F.items()})
        swap = mean_pair({(a,b): (F[a,b]-F[b,a])**2
                          for a,b in product(actions, repeat=2)})
        direct = sum((p[a]*p[b]*p[d] * (
            (F[a,b]-F[b,a])**2 + (F[a,b]-F[d,b])**2
            + (F[a,b]-F[a,d])**2) / 6
            for a,b,d in product(actions, repeat=3)), Q(0))
        compressed = swap/6 + (2*m2
            - sum((p[a]*row[a]**2 for a in actions), Q(0))
            - sum((p[b]*col[b]**2 for b in actions), Q(0)))/3
        var = m2 - mean_pair(F)**2
        assert direct == compressed
        assert Q(0) <= direct <= 2*m2
        assert var <= 3*direct
        d4 += p[c]*direct
        second += p[c]*m2
        count += 3
    assert d4 <= 2*second
    count += 1

    # No quotient-zero point is included in the bad positive endpoint event.
    for Z in range(2, 15):
        actual = sum((p[a]*p[b] for a,b in product(actions, repeat=2)
                      if phi(a,b) < Z), Q(0))
        valid = c2(n) - c2(n//Z)
        stopped = sum((w[a]*(A-mass(n//a)) for a in actions
                       if a > n//Z), Q(0))
        assert actual == (valid+stopped)/(A*A)
        count += 1
        for X in range(1, n+1):
            prob = sum((p[c] for c in actions if 1 <= X//c < Z), Q(0))
            assert prob == (mass(X)-mass(X//Z))/A
            count += 1

    # Exact coefficient arithmetic in the block-loss proof.
    for m in (Q(1,10), Q(1,2), Q(1), Q(2)):
        ell, K = Q(10), Q(20)
        delta = 8*K/m
        h = m/(8*ell)
        loss = m*h/4
        assert loss == m*m/(32*ell)
        assert loss/(8*delta) == m**3/(2048*ell*K)
        count += 2

    return {"exact_assertions": count,
            "status": "passed",
            "scope": "finite algebra and endpoint supports only",
            "analytic_barrier_formalized": False}


def numerical_checks() -> dict[str, object]:
    import numpy as np
    from scipy.integrate import quad

    barrier_rows = []
    # Integrate in y=-log(s), avoiding a tiny integration mesh near s=0.
    for z in (16., 24., 40., 64., 128.):
        def log_e_plus_exp(x: float) -> float:
            return float(np.logaddexp(1., x))
        ell = log_e_plus_exp(z)
        b = 1/math.sqrt(ell)
        def integrand(y: float) -> float:
            return 2*(math.exp(-y)-math.exp(-2*y)) / math.sqrt(log_e_plus_exp(z-y))
        hb, err = quad(integrand, 0., z+50., epsabs=1e-12, epsrel=1e-12)
        ratio = (hb-b)*ell**1.5
        assert ratio < 4.0
        barrier_rows.append({"log_T": z, "scaled_H2_barrier_excess": ratio,
                             "proved_upper_bound": 4.0, "quadrature_error": err})

    Nmax = 2000
    sieve = np.ones(Nmax+1, dtype=bool)
    sieve[:2] = False
    for q in range(2, math.isqrt(Nmax)+1):
        if sieve[q]:
            sieve[q*q::q] = False
    lam = np.zeros(Nmax+1)
    for q in np.flatnonzero(sieve):
        q = int(q)
        power = q
        while power <= Nmax:
            lam[power] = math.log(q)
            power *= q
    psi = np.cumsum(lam)
    f = np.zeros(Nmax+1)
    f[1:] = psi[1:]/np.arange(1, Nmax+1)-1
    rows = []
    for N in (100, 300, 1000, 2000):
        acts = np.flatnonzero(lam[:N+1])
        ww = lam[acts]/acts
        pp = ww/ww.sum()
        a, b = acts[:,None], acts[None,:]
        prod = a*b
        Phi = np.where(prod <= N, N//prod, N//a)
        d4 = 0.0
        second = 0.0
        for c, pc in zip(acts, pp):
            F = f[Phi]+f[Phi//int(c)]
            row, col = F@pp, pp@F
            m2 = float(pp@((F*F)@pp))
            swap = float(pp@(((F-F.T)**2)@pp))
            D = swap/6 + (2*m2-float(pp@(row*row))-float(pp@(col*col)))/3
            d4 += pc*D
            second += pc*m2
        assert -1e-12 <= d4 <= 2*second+1e-12
        rows.append({"N":N, "actions":len(acts), "r_N":float(f[N]),
                     "D4":float(d4), "two_times_folded_second_moment":float(2*second)})
    return {"status":"passed", "classification":"numerical stress tests, not proof",
            "barrier":barrier_rows, "prime_D4":rows}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--numerical', action='store_true')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    result = {"exact":exact_checks()}
    if args.numerical:
        result['numerical'] = numerical_checks()
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        args.out.write_text(text+'\n', encoding='utf-8')
    print(text)

if __name__ == '__main__':
    main()
