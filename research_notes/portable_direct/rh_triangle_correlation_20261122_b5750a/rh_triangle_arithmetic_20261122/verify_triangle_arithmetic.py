#!/usr/bin/env python3
"""Exact kernel checks and a cache-free, local P_256 correction certificate.

The full road is not regenerated. Only D(n), kappa(n), c(n) for n <= 256
are recomputed from the previously fixed rational thickness nodes. All actual
phase samples use the exact harmonic formula with directed 10**-60 intervals.
The same-author dyadic certificate supplies the already fixed tree and q/Q
charges. No float is used for any assertion or certified result.
"""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import hashlib
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'rh_correlation_rational'))
from certify_matched_nodes import (  # noqa: E402
    SCALE, DIGITS, ZERO, ONE, Elementary, rat, add, sub, scale, mul,
    linear_sieve, ceildiv, render,
)


def record(v):
    return {**render(v, 30), 'integer_bounds': [str(v[0]), str(v[1])],
            'denominator_power_of_10': DIGITS}


def read_record(v):
    assert v['denominator_power_of_10'] == DIGITS
    return tuple(map(int, v['integer_bounds']))


def overlap(x, y):
    return max(x[0], y[0]) <= min(x[1], y[1])


def isum(values):
    lo = hi = 0
    for v in values:
        lo += v[0]
        hi += v[1]
    return lo, hi


def sq(v):
    lo = 0 if v[0] <= 0 <= v[1] else min(v[0] ** 2, v[1] ** 2)
    hi = max(v[0] ** 2, v[1] ** 2)
    return lo // SCALE, ceildiv(hi, SCALE)


def harmonic_exact(N):
    hs = [F(0)]
    for n in range(1, N + 1):
        hs.append(hs[-1] + F(1, n))
    return hs


def phi(L, x, R, n):
    if n <= L or n >= R:
        return F(0)
    return F(n - L, x - L) if n <= x else F(R - n, R - x)


def green(L, x, R, n):
    return F((x - L) * (R - x), R - L) * phi(L, x, R, n)


def tri(v, L, x, R):
    return (v[x] - v[L]) / (x - L) - (v[R] - v[x]) / (R - x)


def tri_interval(v, L, x, R):
    return sub(scale(sub(v[x], v[L]), F(1, x - L)),
               scale(sub(v[R], v[x]), F(1, R - x)))


def kernel(L, x, R, d, hs):
    a, b = x - L, R - x
    lo, mid, top = L // d, x // d, (R - 1) // d
    return (F(mid - lo, a) - F(L, a * d) * (hs[mid] - hs[lo])
            + F(R, b * d) * (hs[top] - hs[mid]) - F(top - mid, b))


def kernel_interval(L, x, R, d, hs):
    a, b = x - L, R - x
    lo, mid, top = L // d, x // d, (R - 1) // d
    return add(sub(rat(F(mid - lo, a)), scale(sub(hs[mid], hs[lo]), F(L, a * d))),
               sub(scale(sub(hs[top], hs[mid]), F(R, b * d)), rat(F(top - mid, b))))


def B_phase(d, n):
    r = n % d
    return F(d * d - 1, 12 * d) - F(r * (d - r), 2 * d)


def shifted_quartic(g, r):
    z = (r % g) * (g - r % g)
    return F(g ** 4 + 10 * g * g - 11, 720) - F(z * (z + 2), 24)


def exact_checks():
    hs = harmonic_exact(32)
    kernels = curvature = 0
    for L in range(1, 9):
        for a in range(1, 6):
            for b in range(1, 6):
                x, R = L + a, L + a + b
                w = {n: (phi(L, x, R, n) / n if n else F(0))
                     for n in range(L - 1, R + 2)}
                mass = sum(max(F(0), w[n + 1] - 2 * w[n] + w[n - 1])
                           for n in range(L, R + 1))
                Mw = F(1, a * (L + 1)) + F(R, b * x * (x + 1))
                assert mass == Mw
                curvature += 1
                for d in range(1, 13):
                    kd = kernel(L, x, R, d, hs)
                    direct = sum((w[n] for n in range(L + 1, R) if n % d == 0), F(0))
                    assert kd == direct
                    delta = kd - kernel(L, x, R, 1, hs) / d
                    # P_d after dropping the affine -n log(d)/d term.
                    P = {n: F(n, d) * (hs[n] - hs[n // d]) - F(n % d, d)
                         + F(d - 1, 2 * d) for n in (L, x, R)}
                    assert tri(P, L, x, R) == delta
                    bound1 = F(d - 1, d * x)
                    bound2 = F(d * d // 4, 2 * d) * Mw
                    assert abs(delta) <= min(bound1, bound2)
                    poisson = sum(B_phase(d, n) * (-w[n + 1] + 2 * w[n] - w[n - 1])
                                  for n in range(L, R + 1))
                    assert poisson == delta
                    kernels += 1

    grams = 0
    for d in range(1, 10):
        for e in range(1, 10):
            period, g = lcm(d, e), gcd(d, e)
            for r in range(g):
                actual = sum((B_phase(d, n + r) * B_phase(e, n)
                              for n in range(period)), F(0)) / period
                assert actual == shifted_quartic(g, r) / (d * e)
                grams += 1

    # Nonuniform tree, including short/asymmetric final cells.
    nodes = [2, 4, 7, 9, 14, 19]
    alive = nodes[:]
    packets = []
    while len(alive) > 2:
        for j in range(1, len(alive) - 1, 2):
            packets.append(tuple(alive[j - 1:j + 2]))
        alive = [n for j, n in enumerate(alive) if j % 2 == 0 or j == len(alive) - 1]
    T = [{n: green(*p, n) for n in range(nodes[0], nodes[-1] + 1)} for p in packets]
    for i, p in enumerate(packets):
        for j, tq in enumerate(T):
            assert tri(tq, *p) == (1 if i == j else 0)
            dp = sum((T[i][n + 1] - T[i][n]) * (tq[n + 1] - tq[n])
                     for n in range(nodes[0], nodes[-1]))
            tau = F((p[1] - p[0]) * (p[2] - p[1]), p[2] - p[0])
            assert dp == (tau if i == j else 0)
    coefficients = [F((-1) ** j * (j + 2), j + 3) for j in range(len(packets))]
    C = {n: sum((v * t[n] for v, t in zip(coefficients, T)), F(0))
         for n in range(nodes[0], nodes[-1] + 1)}
    diag = sum(F((x - L) * (R - x), R - L) * d * d
               for (L, x, R), d in zip(packets, coefficients))
    assert diag == sum((C[n + 1] - C[n]) ** 2 for n in range(nodes[0], nodes[-1]))
    return {'exact_rational_kernel_phase_bound_checks': kernels,
            'exact_curvature_mass_checks': curvature,
            'exact_shifted_Gram_checks': grams,
            'exact_tree_biorthogonality_and_Dirichlet_pair_checks': len(packets) ** 2,
            'all_passed': True}


def prefix_coefficients(H, nodes, weights, elem):
    spf, mu = linear_sieve(H)
    primes = [p for p in range(2, H + 1) if spf[p] == p]
    D = [ZERO] * (H + 1)
    for a, nu in zip(nodes, weights):
        factors = {p: sub(ONE, elem.exp_negative(scale(elem.log_integer(p), a))) for p in primes}
        road = [ONE] * (H + 1)
        for n in range(2, H + 1):
            p, k = spf[n], n // spf[n]
            road[n] = road[k] if k % p == 0 else mul(road[k], factors[p])
            D[n] = add(D[n], scale(road[n], nu / a))
    kappa = [ZERO] * (H + 1)
    kappa[1] = scale(elem.log_integer(2), 2)
    for n in range(2, H + 1):
        kappa[n] = scale(add(sub(scale(elem.log_integer(n + 1), n + 1),
                                scale(elem.log_integer(n), 2 * n)),
                            scale(elem.log_integer(n - 1), n - 1)), n)
    c = [ZERO] * (H + 1)
    for d in range(1, H + 1):
        if mu[d]:
            for n in range(d, H + 1, d):
                c[n] = add(c[n], scale(sub(D[n // d], kappa[n // d]), mu[d]))
    return c, len(primes)


def interpolant(nodes, values, first, last):
    result = [ZERO] * (last + 1)
    for L, R in zip(nodes, nodes[1:]):
        for n in range(L, R + 1):
            result[n] = add(scale(values[L], F(R - n, R - L)),
                            scale(values[R], F(n - L, R - L)))
    return result


def actual_certificate():
    fixed_path = ROOT / 'rh_correlation_rational/rational_window_certificate.json'
    tree_path = ROOT / 'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
    fixed, source = (json.loads(p.read_text()) for p in (fixed_path, tree_path))
    A, B, H = 1024, 32768, 256
    nodes = list(map(F, fixed['node_certificate']['nodes']))
    weights = list(map(F, fixed['node_certificate']['weights']))
    elem = Elementary()
    c, prime_count = prefix_coefficients(H, nodes, weights, elem)
    sigma = isum(scale(c[d], F(1, d)) for d in range(1, H + 1))
    assert overlap(sigma, read_record(source['sigma_H']))
    hs = [ZERO]
    hs2 = [ZERO]
    for n in range(1, B + 1):
        hs.append(add(hs[-1], rat(F(1, n))))
        hs2.append(add(hs2[-1], rat(F(1, n * n))))
    fine_nodes = source['partition']['fine_nodes']
    backbone = source['partition']['backbone']
    P = {}
    for n in fine_nodes:
        P[n] = isum(mul(c[d], add(scale(sub(sub(hs[n], hs[n // d]), elem.log_integer(d)), F(n, d)),
                                    rat(-F(n % d, d) + F(d - 1, 2 * d))))
                    for d in range(2, H + 1))
    I = interpolant(fine_nodes, P, A, B)
    J = interpolant(backbone, P, A, B)
    C = [ZERO] * (B + 1)
    for n in range(A, B + 1):
        C[n] = sub(I[n], J[n])
    packet_sum = [ZERO] * (B + 1)
    blocks = []
    total_diag = total_energy = total_bound = ZERO
    packet_count = 0
    for block_index, grid in enumerate(source['partition']['dyadic_blocks']):
        X, Y = grid['X'], grid['Y']
        q_block = source['roads']['q']['dyadic_blocks'][block_index]
        Q_block = source['roads']['Q']['dyadic_blocks'][block_index]
        diag = ZERO
        packets = []
        for level, (q_level, Q_level) in enumerate(zip(q_block['levels'], Q_block['levels']), 1):
            for p, Pq in zip(q_level['packets'], Q_level['packets']):
                L, x, R = (p[k] for k in ('L', 'x', 'R'))
                d = tri_interval(P, L, x, R)
                charge_difference = sub(read_record(Pq['signed_charge']), read_record(p['signed_charge']))
                assert overlap(d, charge_difference)
                K1 = kernel_interval(L, x, R, 1, hs)
                kernel_d = isum(mul(c[v], sub(kernel_interval(L, x, R, v, hs), scale(K1, F(1, v))))
                                for v in range(2, H + 1))
                assert overlap(d, kernel_d)
                assert max(d[0], kernel_d[0], charge_difference[0]) <= min(d[1], kernel_d[1], charge_difference[1])
                tau = F((x - L) * (R - x), R - L)
                diag = add(diag, scale(sq(d), tau))
                for n in range(L + 1, R):
                    packet_sum[n] = add(packet_sum[n], scale(d, green(L, x, R, n)))
                packets.append({'L': L, 'x': x, 'R': R, 'level': level,
                                'phase_charge_secant': record(d),
                                'phase_charge_centered_divisor_kernel': record(kernel_d),
                                'Q_minus_q_charge': record(charge_difference),
                                'all_three_intervals_overlap': True,
                                'Dirichlet_coefficient': str(tau)})
                packet_count += 1
        direct_D = isum(sq(sub(C[n + 1], C[n])) for n in range(X, Y))
        assert overlap(direct_D, diag)
        energy = isum(scale(sq(C[n]), F(1, n * n)) for n in range(X + 1, Y))
        J_trace = isum(rat(F((n - X) * (Y - n), (Y - X) * n * n))
                       for n in range(X + 1, Y))
        J_closed = scale(sub(sub(scale(sub(hs[Y - 1], hs[X]), X + Y), rat(Y - X - 1)),
                             scale(sub(hs2[Y - 1], hs2[X]), X * Y)), F(1, Y - X))
        assert overlap(J_trace, J_closed)
        bound = mul(J_trace, diag)
        assert energy[1] <= bound[0]
        blocks.append({'X': X, 'Y': Y, 'packets': packets,
                       'Dirichlet_energy_diagonal': record(diag),
                       'Dirichlet_energy_direct_differences': record(direct_D),
                       'weighted_correction_energy': record(energy),
                       'Green_trace_direct': record(J_trace),
                       'Green_trace_harmonic_closed': record(J_closed),
                       'trace_times_Dirichlet_bound': record(bound),
                       'bound_separated_with_directed_intervals': True})
        total_diag = add(total_diag, diag)
        total_energy = add(total_energy, energy)
        total_bound = add(total_bound, bound)
    for n in range(A, B + 1):
        assert overlap(C[n], packet_sum[n])
    for n in backbone:
        assert C[n][0] <= 0 <= C[n][1]
        assert packet_sum[n] == ZERO  # Exact vanishing of every compact packet.
    return {'scope': 'Uniform H=256 local phase corrector only; no adaptive minimum screening; no full-road regeneration.',
            'window': {'A': A, 'B': B, 'H': H, 'theta': '1/2'},
            'inputs': [{'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                       for p in (fixed_path, tree_path, ROOT / 'rh_correlation_rational/certify_matched_nodes.py')],
            'cost': {'road_prefix_recomputed_only_through': H,
                     'thickness_count': len(nodes), 'prefix_prime_count': prime_count,
                     'exponential_oracle_calls': elem.exp_calls,
                     'phase_samples': len(fine_nodes), 'tree_packets': packet_count,
                     'scratch_pickle_not_read_or_required': True},
            'sigma_H': record(sigma),
            'c_prefix': [{'d': d, 'c': record(c[d])} for d in range(1, H + 1)],
            'phase_samples': [{'n': n, 'P256': record(P[n]), 'is_backbone': n in backbone} for n in fine_nodes],
            'dyadic_blocks': blocks,
            'total_Dirichlet_energy': record(total_diag),
            'actual_weighted_C_energy': record(total_energy),
            'local_Green_trace_bound': record(total_bound),
            'checks': {'all_38_phase_charges_three_routes_overlap': packet_count == 38,
                       'interpolant_difference_equals_packet_sum_at_every_integer': True,
                       'all_backbone_and_true_endpoints_zero': True,
                       'all_local_Dirichlet_identities_overlap': True,
                       'all_local_trace_bounds_separated': True,
                       'mixed_Hp_selection_implemented': False,
                       'author_checks_are_not_independent_project_review': True}}


def main():
    started = time.perf_counter()
    result = {'status': 'AUTHOR_PROVED_KERNEL_PHASE_TREE_IDENTITIES_WITH_STRICT_FINITE_CERTIFICATE',
              'arithmetic': {'interval_denominator': str(SCALE), 'directed_rounding': True,
                             'generic_checks_use_exact_Fraction': True},
              'exact_checks': exact_checks(), 'actual_uniform_phase_corrector': actual_certificate()}
    result['elapsed_seconds_diagnostic_only'] = round(time.perf_counter() - started, 3)
    destination = OUT / 'triangle_arithmetic_certificate.json'
    destination.write_text(json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n')
    actual = result['actual_uniform_phase_corrector']
    print(json.dumps({'status': result['status'], 'exact_checks': result['exact_checks'],
                      'actual_weighted_C_energy': actual['actual_weighted_C_energy'],
                      'trace_bound': actual['local_Green_trace_bound'],
                      'elapsed_seconds_diagnostic_only': result['elapsed_seconds_diagnostic_only']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
