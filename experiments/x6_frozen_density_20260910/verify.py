#!/usr/bin/env python3
"""Exact finite checks for a frozen-seed density-one extension theorem.

The accompanying note proves the infinite statement. This script tests its
arithmetic majorants, finite no-revision extension, and retained lattice laws.
It does NOT run an infinite selector or claim that a finite test proves density.

Run: python verify.py --source-root /path/to/enterprise-math --output results.json
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

SOURCE = '4fffe9f6353242ce5c7c514325da8b9a63c18f8b'
PINS = {
    'seeds': ('experiments/x6_seed_geometry_20260910/verify.py',
              'e155621d04f0e354f06d48e5075bc5d43d4d0f71'),
    'flags': ('experiments/x6_intermediate_flags_20260910/verify.py',
              'c41fdd1a468d8d7ee52c96c3a739dd59c78892ec'),
}
TARGETS = (16, 32, 48, 96, 208, 416)
OLD_TARGETS = (2, 3, 13, 6, 26, 39)


def load(root: Path, name: str):
    path, expected = PINS[name]
    raw = (root / path).read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if actual != expected:
        raise ValueError(f'Frozen dependency mismatch for {path}: {actual}')
    spec = importlib.util.spec_from_file_location('frozen_density_' + name, root / path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def tail_bound(k: int) -> Fraction:
    """Unconditional E[H-H_k] <= (k+1)/(32*k^2), k >= 1."""
    if not isinstance(k, int) or k < 1:
        raise ValueError('k must be a positive integer')
    return Fraction(k + 1, 32 * k * k)


def filtered_factor(n: int, degree) -> Fraction:
    """Upper cost of conditioning each active prime block to good seeds."""
    value = Fraction(1)
    for p, a in sp.factorint(n).items():
        p, a = int(p), int(a)
        f = degree(p)
        s = a % f
        if s:
            value *= Fraction(64, 59) * (1 + Fraction(1, p ** (f - s)))
    return value


def verify(root: Path) -> dict:
    seeds = load(root, 'seeds')
    flags = load(root, 'flags')
    flags.configure(root)
    c = flags.c
    walk, transport, t6 = (c.load(root, name) for name in ('walk', 'transport', 't6'))

    # This is the already published portfolio, not a newly optimized old state.
    locks: dict[tuple[int, int], tuple[int, ...]] = {}
    old_normals = {}
    for p, index in ((2, 3), (3, 237), (13, 2)):
        q = flags.block(p, 0)[3]
        coeff = list(seeds.projective(p, q.rows))[index]
        locks[p, 0] = coeff
        old_normals[str(p)] = [int(x) % p for x in sp.Matrix([coeff]) * q]
        # R_s < lambda_1(I), so ALL seeds of these blocks pass the coarse filter.
        assert p ** (c.residue_degree(p) - 1) < 6 ** 6
    assert old_normals == {
        '2': [1, 0, 0, 1, 1, 1], '3': [1, 2, 2, 2, 1, 0],
        '13': [6, 2, 1, 8, 1, 2]}

    candidates = list(seeds.projective(2, flags.block(2, 1)[3].rows))
    assert len(candidates) == 7

    def build_family(parameters):
        @lru_cache(None)
        def local(p, k):
            f = c.residue_degree(p)
            r, s = divmod(k, f)
            if s == 0:
                return c.ideal(p ** k)
            if (p, r) not in parameters:
                raise ValueError(f'Unspecified finite block {(p, r)}; no silent reselection')
            a, _, u, q, _ = flags.block(p, r)
            ell = sp.Matrix([parameters[p, r]]) * q
            rows = sp.Matrix.vstack(*(ell * u ** j for j in range(s)))
            rows = rows.applyfunc(lambda v: int(v) % p)
            return flags.hnf(a * flags.modular_kernel(rows, p))

        @lru_cache(None)
        def family(n):
            h = sp.eye(6)
            for p, a in sp.factorint(n).items():
                h = flags.intersect(h, local(int(p), int(a)))
            assert int(h.det()) == n
            return h
        return family

    initial = build_family(locks)
    frozen_bases = {n: initial(n) for n in OLD_TARGETS}
    old_costs = [int(flags.repair(initial(n), walk, transport)[0]
                     ['minimum_total_unit_distance']) for n in OLD_TARGETS]
    assert old_costs == [0, 0, 4, 0, 6, 8]

    vv = np.array(seeds.sphere_vectors(9), dtype=np.int64)
    qv = np.sum(vv * vv, axis=1)
    table, evidence = [], {}
    for i, coeff in enumerate(candidates):
        family = build_family({**locks, (2, 1): coeff})
        assert all(family(n) == frozen_bases[n] for n in OLD_TARGETS)
        row, minima, retained = [], [], {}
        for n in TARGETS:
            h = family(n)
            result, cert = flags.repair(h, walk, transport)
            row.append(int(result['minimum_total_unit_distance']))
            adj = np.array((n * h.inv()).tolist(), dtype=np.int64)
            # The dot products here have an explicit small integer range.
            assert int(np.max(np.abs(adj))) < 100000
            alive = np.all(vv @ adj.T % n == 0, axis=1)
            assert np.any(alive), 'Increase the explicitly enumerated sphere'
            first = int(np.flatnonzero(alive)[0])
            minima.append({'n': n, 'lambda1_squared': int(qv[first]),
                           'witness': [int(x) for x in vv[first]]})
            if n == 416:
                retained = cert
        table.append({'seed_index': i, 'coefficient': list(coeff), 'costs': row,
                      'total': sum(row), 'shortest_vectors': minima})
        evidence[i] = retained
    winner = min(range(len(table)), key=lambda i: (table[i]['total'], i))
    assert winner == 4 and table[winner]['total'] == 336
    assert table[0]['total'] == 337
    family = build_family({**locks, (2, 1): candidates[winner]})
    independent_sum = sum(min(row['costs'][j] for row in table) for j in range(6))
    assert independent_sum == 302
    conditional_mean = Fraction(sum(row['total'] for row in table), 7)
    assert table[winner]['total'] <= conditional_mean
    print('42 certified new costs; old three block seeds and six bases unchanged', flush=True)

    # The new block belongs to one unchanged local chain. No matrix is chosen
    # separately at each target. Check exact finite-future and gcd/lcm laws.
    indices = (1, 2, 3, 4, 6, 8, 12, 13, 16, 24, 26, 32, 39, 48,
               64, 96, 104, 208, 312, 416)
    horizons = 0
    for n in indices:
        h = family(n)
        for step in range(6):
            assert h == family(flags.rounded(n, step))
            h = flags.intersect(h, c.U ** 6 * h)
            horizons += 1
    pairs = 0
    for m in indices:
        for n in indices:
            a, b = family(m), family(n)
            assert flags.intersect(a, b) == family(int(sp.ilcm(m, n)))
            assert flags.hnf(a.row_join(b)) == family(int(sp.gcd(m, n)))
            pairs += 1
    sequences = {}
    for n in (2, 4, 16, 32):
        core = c.Quotient(c.ideal(flags.rounded(n, up=True)))
        current = c.Quotient(family(n))
        transition = {z: core.points[core.label((-z[5], z[0]-z[5], z[1]-z[5],
                      z[2]-z[5], z[3]-z[5], z[4]-z[5]))] for z in core.points}
        observation = {z: current.label(z) for z in core.points}
        seq = [t6.class_count(x) for x in t6.future_partition_sequence(
            core.points, transition, observation)]
        assert seq == list(dict.fromkeys(flags.rounded(n, j) for j in range(6)))
        sequences[str(n)] = seq

    # New proof's arithmetic majorant; tests do not evaluate its infinite event.
    limit = 16383
    tau = [0] * (limit + 1)
    for d in range(1, limit + 1):
        for n in range(d, limit + 1, d):
            tau[n] += 1
    factor_rows = []
    for n in range(1, limit + 1):
        fac = filtered_factor(n, c.residue_degree)
        assert fac <= tau[n]
        if n in (6, 26, 39, 78, 210, 1001, 2310, 30030):
            factor_rows.append({'n': n, 'conditioned_factor': str(fac), 'tau': tau[n]})
    dyadic = []
    for k in range(1, 13):
        divisor_total = sum(tau[n] for n in range(2 ** k, 2 ** (k + 1)))
        assert divisor_total <= 2 ** (k + 1) * (k + 2)
        expectation_bound = Fraction(k + 2, 32 * k ** 3)
        assert Fraction(divisor_total, 64 * k ** 3 * 2 ** k) <= expectation_bound
        dyadic.append({'k': k, 'tau_sum': divisor_total,
                      'weighted_expectation_bound': str(expectation_bound)})
    partial = sum((Fraction(k + 2, 32 * k ** 3) for k in range(1, 1001)), Fraction(0))
    assert partial < Fraction(5, 32)
    tails = []
    for k in (1, 2, 10, 100, 1000):
        subtotal = sum((Fraction(j + 2, 32 * j ** 3)
                        for j in range(k + 1, k + 101)), Fraction(0))
        assert subtotal <= tail_bound(k)
        tails.append({'k': k, 'unconditional_tail_upper': str(tail_bound(k))})
    print('Exact future kernels, arithmetic factors, and summable-tail bounds checked', flush=True)

    return {
        'status': 'PASS_EXACT_FINITE_REGRESSION_NOT_INFINITE_EXECUTION_OR_ADMISSION',
        'source_snapshot': SOURCE,
        'old_locked_seed_indices': {'2': 3, '3': 237, '13': 2},
        'old_locked_coefficients': {str(p): list(locks[p, 0]) for p in (2, 3, 13)},
        'old_locked_normals': old_normals,
        'old_targets': list(OLD_TARGETS), 'old_costs_unchanged': old_costs,
        'new_block': {'p': 2, 'r': 1, 'seed_count': 7,
                      'all_seeds_pass_coarse_geometry_filter': True},
        'new_targets': list(TARGETS), 'complete_extension_table': table,
        'new_cost_count': 42, 'selected_index': winner,
        'selected_coefficient': list(candidates[winner]),
        'selected_total': 336, 'sum_of_separate_minima': independent_sum,
        'uniform_remaining_seed_mean_cost': str(conditional_mean),
        'declared_cost_objective': 'equal weight on six new targets, old three blocks fixed',
        'selected_416_integer_dual': evidence[winner],
        'finite_horizon_identities': horizons, 'gcd_lcm_pairs': pairs,
        'T6_sequences': sequences, 'factor_majorant_checks': limit,
        'factor_examples': factor_rows, 'dyadic_checks': dyadic, 'tail_checks': tails,
        'global_expectation_upper': '5/32',
        'old_cylinder_probability': '1/35672',
        'four_block_cylinder_probability': '1/249704',
        'theorem_bad_test': '42^3 * floor(log2(N))^4 * Q(z)^3 < N for some nonzero z in M(N)',
        'infinite_claim_status': 'proved in note; entire infinite seed sequence not enumerated',
        'infinite_selector_status': 'effective construction specified and proved; not run end-to-end',
        'finite_conditional_choice_scope': 'six-target cost, not a claimed evaluation of infinite H',
        'reuse': {name: {'path': path, 'blob': blob, 'state': 'REUSE_EXECUTED'}
                  for name, (path, blob) in PINS.items()},
        'boundaries': ['density one is not every integer', 'no exceptional modulus is deleted',
            'no uniform all-integer shape constant', 'no O(1) mean transport theorem',
            'U is not a native isometry', 'no strict local nested representative construction',
            'no independent review, formal proof or Foundation promotion']}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.source_root.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('PASS', flush=True)


if __name__ == '__main__':
    main()
