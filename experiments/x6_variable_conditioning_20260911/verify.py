#!/usr/bin/env python3
"""Exact finite checks for prime-dependent X6 conditioning budgets.

Infinite summability, universal open-frontier and fixed-threshold barrier statements
are proved in the accompanying note. This script checks the exact rational
schedule, divisor convolution, partial Euler majorant, critical exponent margins,
and finite inert-prime projective support diagnostics.
"""
from __future__ import annotations
import argparse, itertools, json, math
from fractions import Fraction
from pathlib import Path
import sympy as sp

EPS0 = Fraction(5, 123)


def band_j(p: int) -> int:
    return (p - 1).bit_length()  # ceil(log2 p), including p=2


def ell(j: int) -> int:
    return 1 + (j.bit_length() - 1)  # 1 + floor(log2 j)


def epsilon_p(p: int) -> Fraction:
    j = band_j(p)
    return min(EPS0, Fraction(1, j * ell(j) ** 2))


def local_factor(p: int) -> Fraction:
    e = epsilon_p(p)
    return (1 + e) * (1 + Fraction(1, p))


def Fstar(n: int) -> Fraction:
    out = Fraction(1)
    for p in sp.factorint(n):
        out *= local_factor(int(p))
    return out


def gstar(n: int) -> Fraction:
    fac = sp.factorint(n)
    if any(int(e) > 1 for e in fac.values()):
        return Fraction(0)
    out = Fraction(1)
    for p in fac:
        p = int(p)
        e = epsilon_p(p)
        out *= e + (1 + e) / p
    return out


def projective_normalize(v, p: int):
    w = tuple(int(x) % p for x in v)
    if not any(w):
        return None
    i = next(i for i, x in enumerate(w) if x)
    inv = pow(w[i], -1, p)
    return tuple((x * inv) % p for x in w)


def sphere_vectors(max_q: int, dim: int = 6):
    r = math.isqrt(max_q)
    for v in itertools.product(range(-r, r + 1), repeat=dim):
        q = sum(x * x for x in v)
        if 0 < q <= max_q:
            yield v


def old_threshold_qmax(p: int) -> int:
    # 42^3 Q^3 < p^5; return largest integral Q satisfying the strict inequality.
    q = int((p ** 5 / 42 ** 3) ** (1 / 3))
    while 42 ** 3 * q ** 3 >= p ** 5:
        q -= 1
    while 42 ** 3 * (q + 1) ** 3 < p ** 5:
        q += 1
    return q


def verify(limit: int) -> dict:
    assert limit >= 2048
    schedule_primes = [2, 3, 5, 7, 13, 17, 19, 31, 43, 277, 1009, 10007]
    schedule = []
    for p in schedule_primes:
        assert sp.isprime(p)
        e = epsilon_p(p)
        assert 0 < e <= EPS0
        j = band_j(p)
        L = ell(j)
        r6 = Fraction(2) * e / (5 * (1 + e))
        assert r6 <= Fraction(1, 64)
        good = 1 - Fraction(5, 2) * r6
        assert good >= 1 / (1 + e)
        schedule.append({
            'p': p, 'j': j, 'ell': L, 'epsilon': str(e),
            'r_sixth_power': str(r6),
            'good_fraction_lower_bound': str(good),
            'conditioning_factor_upper_bound': str(1 / good),
        })

    conv = 0
    sum_f = Fraction(0)
    snapshots = []
    snap_targets = {255, 1023, 4095, 16383, 32767, 65535}
    for n in range(1, limit + 1):
        fn = Fstar(n)
        if n <= 2048:
            rec = sum((gstar(int(d)) for d in sp.divisors(n)), Fraction(0))
            assert rec == fn
            conv += 1
        sum_f += fn
        if n in snap_targets:
            snapshots.append({'X': n, 'mean_Fstar': float(sum_f / n)})

    eps_over_p = Fraction(0)
    gp_over_p = Fraction(0)
    euler_partial = Fraction(1)
    prime_count = 0
    for p in sp.primerange(2, limit + 1):
        p = int(p)
        e = epsilon_p(p)
        gp = e + (1 + e) / p
        eps_over_p += e / p
        gp_over_p += gp / p
        euler_partial *= 1 + gp / p
        prime_count += 1

    # The explicit schedule is dominated by a summable dyadic-band series.
    band_terms = []
    band_bound = Fraction(0)
    for j in range(1, 4097):
        term = Fraction(1, j * ell(j) ** 2)
        band_bound += term
        if j in (1, 2, 4, 8, 16, 64, 256, 1024, 4096):
            band_terms.append({'j': j, 'partial_sum': float(band_bound)})
    assert band_bound < 2

    # Open-frontier and critical-log examples.
    beta = Fraction(1)
    gamma = Fraction(3, 8)
    alpha = Fraction(6, 25)
    margin = 6 * gamma - (1 + beta + alpha)
    assert margin == Fraction(1, 100)
    gamma_open = Fraction(17, 50)
    assert 6 * gamma_open - 2 == Fraction(1, 25)
    delta_single = Fraction(1, 5)
    assert 6 * delta_single > 1
    eta_window = Fraction(6, 5)
    assert eta_window > 1
    delta_mix = Fraction(1, 12)
    eta_mix = Fraction(3, 5)
    assert 6 * delta_mix + eta_mix == Fraction(11, 10)

    # Finite inert-prime projective diagnostics at the old fixed 1/sqrt(42) threshold.
    inert = []
    for p in (17, 31, 59, 73):
        assert sp.isprime(p) and sp.n_order(p % 7, 7) == 6
        qmax = old_threshold_qmax(p)
        signed = 0
        lines = set()
        for v in sphere_vectors(qmax):
            signed += 1
            key = projective_normalize(v, p)
            assert key is not None
            lines.add(key)
        P = (p ** 6 - 1) // (p - 1)
        inert.append({
            'p': p, 'f': 6, 's': 5, 'max_Q': qmax,
            'signed_candidates': signed,
            'distinct_projective_events': len(lines),
            'seed_projective_atoms': P,
            'bad_fraction': float(Fraction(len(lines), P)),
        })

    return {
        'status': 'PASS_EXACT_FINITE_CHECKS_NOT_INFINITE_PROOF_OR_ADMISSION',
        'limit': limit,
        'schedule': schedule,
        'dirichlet_convolution_checks': conv,
        'prime_count_in_partial_euler': prime_count,
        'partial_sums': {
            'sum_epsilon_p_over_p': float(eps_over_p),
            'sum_g_p_over_p': float(gp_over_p),
            'partial_euler_constant': float(euler_partial),
            'band_schedule_partial_below_2': float(band_bound),
        },
        'mean_Fstar_snapshots': snapshots,
        'band_schedule_snapshots': band_terms,
        'frontier_examples': {
            'beta': str(beta),
            'gamma': str(gamma),
            'alpha_open_example': str(alpha),
            'open_margin': str(margin),
            'single_target_gamma_open_example': str(gamma_open),
            'single_target_margin': str(6 * gamma_open - 2),
            'critical_single_gamma': '1/3',
            'critical_single_iterated_log_delta': str(delta_single),
            'critical_window_gamma': '3/8',
            'critical_window_alpha': '1/4',
            'critical_window_log_thinning_eta': str(eta_window),
            'mixed_critical_delta_eta': [str(delta_mix), str(eta_mix)],
            'mixed_critical_log_sum': str(6 * delta_mix + eta_mix),
        },
        'inert_penultimate_fixed_threshold_diagnostics': inert,
        'boundaries': [
            'finite checks do not prove the infinite Euler-product or density/window theorem',
            'bounded-average conditioning uses prime-dependent local geometry constants, not a uniform positive prime-power constant',
            'the fixed-threshold inert-prime obstruction is proved in the note; finite fractions are diagnostics only',
            'critical unthinned equality remains outside the nonnegative first-moment proof',
            'all composite observers and four previous seed locks remain retained',
            'no Foundation or Working Truth promotion',
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=32767)
    ap.add_argument('--output')
    args = ap.parse_args()
    out = verify(args.limit)
    text = json.dumps(out, ensure_ascii=False, separators=(',', ':')) + '\n'
    if args.output:
        Path(args.output).write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
