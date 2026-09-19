#!/usr/bin/env python3
"""Exact finite regression for sharper frozen-family density bounds.

The infinite theorem is proved in the companion note, not by this program.
Run: python verify.py --source-root /path/to/enterprise-math --output results.json
No network access. Frozen source imports are checked by Git blob identifiers.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
import sympy as sp

SOURCE = 'f351f2e9eea720eedb96566d638909bd0b16f5e8'
PARENT_PATH = 'experiments/x6_frozen_density_20260910/verify.py'
PARENT_BLOB = '3d00faa747cf34cfedcc3166331a5ae63add4b8b'
LOCKS = {(2, 0): (1, 1, 1), (3, 0): (1, 2, 2, 2, 1, 0),
         (13, 0): (1, 2), (2, 1): (0, 1, 0)}


def blob(raw: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def parent(root: Path):
    raw = (root / PARENT_PATH).read_bytes()
    if blob(raw) != PARENT_BLOB:
        raise ValueError('Frozen density dependency mismatch')
    spec = importlib.util.spec_from_file_location('x6_density_parent', root / PARENT_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(PARENT_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ceil_scaled(x: Fraction, scale: int) -> int:
    return (x.numerator * scale + x.denominator - 1) // x.denominator


def arithmetic_checks(d, degree, limit: int) -> dict:
    tau = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        for n in range(divisor, limit + 1, divisor):
            tau[n] += 1
    a = Fraction(64, 59)
    assert a ** 8 < 2
    scale = 1 << 40
    upper_f = [0] * (limit + 1)
    upper_b2 = [0] * (limit + 1)
    factors = {}
    examples = []
    for n in range(1, limit + 1):
        primes = sp.factorint(n)
        b = Fraction(1)
        for p in primes:
            b *= 1 + Fraction(1, int(p))
        f = a ** len(primes) * b
        observed = d.filtered_factor(n, degree)  # reuse unchanged parent law
        assert observed <= f and f ** 8 <= tau[n] * b ** 8
        upper_f[n] = ceil_scaled(f, scale)
        upper_b2[n] = ceil_scaled(b * b, scale)
        if n <= 256:
            factors[n] = f
        if n in (6, 26, 39, 78, 210, 1001, 2310, 30030):
            examples.append({'n': n, 'actual_parent_majorant': str(observed),
                             'submultiplicative_majorant': str(f), 'tau': tau[n]})
    # Whole-block averages, with exact upward rounding rather than floating sums.
    dyadic = []
    for k in range(1, limit.bit_length() - 1):
        x = 2 ** (k + 1) - 1
        if x > limit:
            break
        s = sum(upper_f[1:x + 1])
        b2 = sum(upper_b2[1:x + 1])
        assert s ** 8 <= (3 * x * scale) ** 8 * (k + 2)
        assert b2 <= 8 * x * scale
        assert sum(tau[1:x + 1]) <= x * (k + 2)
        dyadic.append({'k': k, 'x': x, 'F_sum_upper_scaled': s,
                       'B_squared_sum_upper_scaled': b2})
    submultiplicative = 0
    for m in range(1, 65):
        for n in range(1, 65):
            fmn = Fraction(1)
            for p in sp.factorint(m * n):
                fmn *= a * (1 + Fraction(1, int(p)))
            assert fmn <= factors[m] * factors[n]
            submultiplicative += 1
    # Rational certificates for fractional-power constants used in the proof.
    assert 3 ** 9 < 4 ** 8
    assert 9 ** 8 * 3 < 16 ** 8
    assert 13 < 2 ** 8
    # Single-scale tails at perfect eighth powers, window tails at 32nd powers.
    tails = [{'K': t ** 8, 'single_tail_upper': str(Fraction(1, t))}
             for t in (1, 2, 10, 100)]
    window_tails = [{'K': t ** 32, 'window_tail_upper': str(Fraction(416, t))}
                    for t in (1, 2, 10)]
    return {'pointwise_majorants': limit, 'submultiplicativity_checks': submultiplicative,
            'rounding_scale': scale, 'dyadic_exact_checks': dyadic, 'examples': examples,
            'single_scale_tail_samples': tails, 'window_tail_samples': window_tails}


def correlation_checks(seeds, flags, t6) -> dict:
    totals = 0
    rows = []
    binary_joint = {}
    for p in (2, 3, 13):
        _, _, ub, q, _ = flags.block(p, 0)
        f = q.rows
        pivots = []
        for j in range(6):
            test = q[:, pivots + [j]]
            padded = [list(row) + [0] * (6 - test.cols) for row in test.tolist()]
            if flags.c.mod_rank(padded, p) > len(pivots):
                pivots.append(j)
            if len(pivots) == f:
                break
        right = sp.zeros(6, f)
        inverse = q[:, pivots].inv_mod(p)
        for i, pos in enumerate(pivots):
            for j in range(f):
                right[pos, j] = inverse[i, j]
        u = np.array((q * ub * right).tolist(), dtype=np.int64) % p
        lines = list(seeds.projective(p, f))
        vectors = lines if p != 3 else lines[:16]
        duals = np.array(lines, dtype=np.int64)
        masks, spans = {}, {}
        for i, v in enumerate(vectors):
            current = np.array(v, dtype=np.int64)
            alive = np.ones(len(lines), dtype=bool)
            span = []
            for s in range(1, f + 1):
                alive &= duals @ current % p == 0
                masks[i, s] = sum(1 << j for j in np.flatnonzero(alive).tolist())
                span.append(list(map(int, current)))
                spans[i, s] = [r[:] for r in span]
                current = u @ current % p
        covariances = Counter()
        for i in range(len(vectors)):
            for j in range(len(vectors)):
                for s in range(1, f + 1):
                    for t in range(1, f + 1):
                        matrix = spans[i, s] + spans[j, t]
                        rank = flags.c.mod_rank([r + [0] * (6 - f) for r in matrix], p)
                        expected = (p ** (f - rank) - 1) // (p - 1)
                        count = (masks[i, s] & masks[j, t]).bit_count()
                        assert count == expected
                        cov = (Fraction(count, len(lines)) -
                               Fraction(masks[i, s].bit_count() * masks[j, t].bit_count(),
                                        len(lines) ** 2))
                        covariances['positive' if cov > 0 else 'negative' if cov < 0 else 'zero'] += 1
                        if p == 2 and s == t == 1:
                            binary_joint[i, j] = count
                        totals += 1
        rows.append({'p': p, 'seed_lines_exhausted': len(lines),
                     'vector_lines_checked': len(vectors), 'horizon_pairs': f * f,
                     'covariance_sign_counts': dict(covariances)})
    domain = tuple(binary_joint)
    coarse = {x: (3, 3) for x in domain}
    witness = t6.fiber_constancy_witness(domain, coarse, binary_joint)
    assert witness is not None
    repaired = t6.coarsest_one_step_repair(domain, coarse, binary_joint)
    assert t6.class_count(repaired) == 2
    return {'joint_incidence_checks': totals, 'blocks': rows,
            'binary_equal_vector_covariance': str(Fraction(3, 7) - Fraction(3, 7) ** 2),
            'binary_independent_vectors_covariance': str(Fraction(1, 7) - Fraction(3, 7) ** 2),
            'T6_marginal_only_witness': witness, 'T6_repaired_joint_classes': 2,
            'scope': 'raw uniform projective seeds; these small blocks have G=E; not general conditional independence'}


def frozen_geometry(flags, walk, transport, t6) -> dict:
    @lru_cache(None)
    def local(p, k):
        f = flags.c.residue_degree(p)
        r, s = divmod(k, f)
        if not s:
            return flags.c.ideal(p ** k)
        if (p, r) not in LOCKS:
            raise ValueError(f'Unfrozen block {(p, r)} requested')
        a, _, u, q, _ = flags.block(p, r)
        ell = sp.Matrix([LOCKS[p, r]]) * q
        rows = sp.Matrix.vstack(*(ell * u ** j for j in range(s)))
        return flags.hnf(a * flags.modular_kernel(rows.applyfunc(lambda v: int(v) % p), p))

    @lru_cache(None)
    def family(n):
        a = sp.eye(6)
        for p, k in sp.factorint(n).items():
            a = flags.intersect(a, local(int(p), int(k)))
        assert a.det() == n
        return a

    expected = {2: 0, 3: 0, 13: 4, 6: 0, 26: 6, 39: 8,
                16: 4, 32: 8, 48: 19, 96: 40, 208: 101, 416: 164}
    costs = {}
    for n, value in expected.items():
        info, _ = flags.repair(family(n), walk, transport)
        assert info['minimum_total_unit_distance'] == value
        costs[str(n)] = value
    horizon_checks = 0
    for n in expected:
        h = family(n)
        for j in range(6):
            assert h == family(flags.rounded(n, j))
            h = flags.intersect(h, flags.c.U ** 6 * h)
            horizon_checks += 1
    return {'locks': [{'p': p, 'r': r, 'coefficients': list(v)} for (p, r), v in LOCKS.items()],
            'unchanged_integer_certified_costs': costs, 'finite_future_identities': horizon_checks,
            'scope': 'regression of the four actual locks, not a new seed optimization'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--limit', type=int, default=32767)
    args = parser.parse_args()
    if args.limit < 4096:
        parser.error('--limit must be at least 4096')
    d = parent(args.source_root)
    seeds, flags = d.load(args.source_root, 'seeds'), d.load(args.source_root, 'flags')
    flags.configure(args.source_root)
    c = flags.c
    walk, transport, t6 = (c.load(args.source_root, n) for n in ('walk', 'transport', 't6'))
    result = {'status': 'PASS_EXACT_FINITE_CHECKS_NOT_INFINITE_EXECUTION_OR_ADMISSION',
              'source_snapshot': SOURCE,
              'arithmetic': arithmetic_checks(d, c.residue_degree, args.limit)}
    print('Exact multiplicative majorants and moment bounds checked', flush=True)
    result['correlations'] = correlation_checks(seeds, flags, t6)
    print('Joint rank incidence and information-loss witness checked', flush=True)
    result['frozen_state'] = frozen_geometry(flags, walk, transport, t6)
    result['theorem'] = {'lambda1_log_exponent': '3/8', 'lambda6_log_exponent': '15/8',
                         'parent_lambda1_log_exponent': '2/3',
                         'exception_count': 'o(X/log X)',
                         'growing_multiplier_window': '1 <= m <= 13*floor(floor(log2 N)^(1/12))',
                         'mean_factor_exponent': '1/8',
                         'single_loss_expectation_upper': '9/8',
                         'window_loss_expectation_upper': '429',
                         'integer_bad_witness_test': '42^12*k^9*Q(z)^12 < N^4'}
    result['reuse'] = {'density_parent_blob': PARENT_BLOB, 'method': 'filtered_factor, pinned source loader',
                       'T6': 'fiber_constancy_witness, coarsest_one_step_repair, class_count',
                       'transport': 'unchanged integer primal/dual checker through flags.repair'}
    result['limits'] = ['not all-integer constant shape', 'not constant mean repair',
                        'not multiplicative closure of the good set', 'no independence of composite bad events',
                        'U remains an extra nonisometric operation', 'infinite selector not executed',
                        'small-scale empty bad tests are not evidence for the density theorem',
                        'no formal proof, independent review or Foundation admission']
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print('PASS; four frozen seeds and twelve previous costs preserved', flush=True)


if __name__ == '__main__':
    main()
