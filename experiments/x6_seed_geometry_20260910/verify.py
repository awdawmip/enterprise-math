#!/usr/bin/env python3
"""Exact domain regression: information-optimal flags, geometry and mixed costs.

Run: python verify.py --source-root /path/to/enterprise-math --output results.json
Uses the frozen flag, ideal, native-path and integer assignment certificate modules.
No network I/O. General probability/geometry statements are proved in the note;
finite exhaustive searches and sampled filters are reported separately.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from math import isqrt
from pathlib import Path
import random
import numpy as np
import sympy as sp

SOURCE = '902318ee8a5dd5065fa43710c3521898bec4120b'
FLAG_PATH = 'experiments/x6_intermediate_flags_20260910/verify.py'
FLAG_BLOB = 'c41fdd1a468d8d7ee52c96c3a739dd59c78892ec'


def projective(p, dim):
    """One representative per nonzero dual line; first nonzero entry is one."""
    for first in range(dim):
        for tail in product(range(p), repeat=dim-first-1):
            yield (0,)*first+(1,)+tail


def sphere_vectors(max_q, dim=6):
    def visit(prefix, budget, remaining):
        if not remaining:
            if any(prefix):
                yield tuple(prefix)
            return
        r = isqrt(budget)
        for a in range(-r, r+1):
            yield from visit(prefix+[a], budget-a*a, remaining-1)
    return sorted(visit([], max_q, dim), key=lambda v: (sum(x*x for x in v), v))


def int_root(n, degree):
    low, high = 0, 1
    while high**degree <= n:
        high *= 2
    while high-low > 1:
        mid = (low+high)//2
        if mid**degree <= n:
            low = mid
        else:
            high = mid
    return low


def verify(root):
    data = (root/FLAG_PATH).read_bytes()
    actual = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if actual != FLAG_BLOB:
        raise ValueError('Frozen flag module mismatch: '+actual)
    spec = importlib.util.spec_from_file_location('seed_flags', root/FLAG_PATH)
    f = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(f)
    f.configure(root)
    c = f.c
    walk = c.load(root, 'walk')
    transport = c.load(root, 'transport')
    t6 = c.load(root, 't6')
    u = np.array(c.U.tolist(), dtype=np.int64)
    points = np.array([walk.point(k) for k in range(243)], dtype=np.int64)
    seeds, local_histograms = {}, {}
    for p in (2, 3, 13):
        a, b, ub, q, _ = f.block(p, 0)
        qq = np.array(q.tolist(), dtype=np.int64)
        rows = []
        for coeff in projective(p, q.rows):
            normal = tuple(map(int, np.array(coeff)@qq % p))
            result, cert, _ = transport.repair_case(points[:p]@normal % p, normal)
            rows.append({'coeff': list(coeff), 'normal': list(normal),
                         'cost': result['minimum_total_unit_distance']})
        seeds[p] = rows
        local_histograms[p] = dict(sorted(Counter(x['cost'] for x in rows).items()))
    print('All local seeds and integer optimality certificates checked', flush=True)

    # Exact incidence counts over all nonzero quotient vectors (not samples).
    incidence = []
    for p in (2, 3, 13):
        a, b, ub, q, _ = f.block(p, 0)
        dim = q.rows
        pivots = []
        for j in range(6):
            test = q[:, pivots+[j]]
            if c.mod_rank([list(row)+[0]*(6-test.cols) for row in test.tolist()], p) > len(pivots):
                pivots.append(j)
            if len(pivots) == dim:
                break
        right = sp.zeros(6, dim)
        inverse = q[:, pivots].inv_mod(p)
        for i, pos in enumerate(pivots):
            for j in range(dim):
                right[pos, j] = inverse[i, j]
        uu = np.array((q*ub*right).tolist(), dtype=np.int64) % p
        vectors = np.array([x for x in product(range(p), repeat=dim) if any(x)], dtype=np.int64)
        duals = np.array([x['coeff'] for x in seeds[p]], dtype=np.int64)
        allowed = np.ones((len(duals), len(vectors)), dtype=bool)
        current = vectors.copy()
        for s in range(1, dim+1):
            allowed &= (duals@current.T % p == 0)
            expected = (p**(dim-s)-1)//(p-1)
            assert np.all(allowed.sum(axis=0) == expected)
            incidence.append({'p': p, 's': s, 'nonzero_vectors': len(vectors),
                              'seed_lines': len(duals), 'annihilating_lines': expected,
                              'probability': str(Fraction(expected, len(duals)))})
            current = current@uu.T % p
    print('Exact flag incidence law checked on every nonzero vector', flush=True)

    # Complete local Euclidean successive minima for the small p=2,3 blocks.
    geometry = {}
    for p in (2, 3):
        vv = np.array(sphere_vectors(p*p), dtype=np.int64)
        qq = np.sum(vv*vv, axis=1)
        dim = c.residue_degree(p)
        profiles = []
        for seed in seeds[p]:
            normal = np.array(seed['normal'], dtype=np.int64)
            alive = np.ones(len(vv), dtype=bool)
            profile = []
            for s in range(1, dim):
                alive &= (vv@normal % p == 0)
                normal = normal@u % p
                independent, minima = [], []
                # Every minor is bounded by p^6 < 1000003 (Hadamard).
                # Thus this modular rank equals the rational rank here.
                for v, qv in zip(vv[alive], qq[alive]):
                    trial = independent+[list(map(int, v))]
                    if c.mod_rank(trial, 1000003) > len(independent):
                        independent = trial
                        minima.append(int(qv))
                    if len(independent) == 6:
                        break
                assert len(independent) == 6
                assert int(sp.Matrix(independent).det()) != 0
                assert minima[0]**3 * 42**3 >= p**s
                profile.append(minima)
            profiles.append(profile)
        raw_profiles = json.dumps(profiles, separators=(',', ':')).encode()
        geometry[p] = {'seeds': len(profiles), 'levels': dim-1,
                       'profile_sha256': hashlib.sha256(raw_profiles).hexdigest(),
                       'distinct_profiles': len(set(map(str, profiles))),
                       'shortest_squares': [dict(sorted(Counter(x[s][0] for x in profiles).items()))
                                            for s in range(dim-1)],
                       'sixth_squares': [dict(sorted(Counter(x[s][5] for x in profiles).items()))
                                         for s in range(dim-1)]}
    print('Exact small-block successive minima checked', flush=True)

    # First-level mixed-prime quotients are cyclic. The CRT coefficient vector
    # is built from BOTH retained normals; all assignment claims have exact duals.
    joint = {}
    all_tables = {}
    for p, q in ((2, 3), (2, 13), (3, 13)):
        n = p*q
        cp, cq = q*pow(q, -1, p), p*pow(p, -1, q)
        table = []
        for ia, a in enumerate(seeds[p]):
            line = []
            for ib, b in enumerate(seeds[q]):
                weights = (cp*np.array(a['normal'])+cq*np.array(b['normal'])) % n
                result, cert, _ = transport.repair_case(points[:n]@weights % n, weights)
                line.append(int(result['minimum_total_unit_distance']))
            table.append(line)
        all_tables[n] = table
        global_best = min(map(min, table))
        min_p = min(x['cost'] for x in seeds[p]); min_q = min(x['cost'] for x in seeds[q])
        local_pairs = [(i, j) for i, a in enumerate(seeds[p]) for j, b in enumerate(seeds[q])
                       if a['cost'] == min_p and b['cost'] == min_q]
        locally_best = min((table[i][j], i, j) for i, j in local_pairs)
        global_pair = min((table[i][j], i, j) for i in range(len(table)) for j in range(len(table[i])))
        witnesses = {}
        for name, (_, i, j) in [('local_minima', locally_best), ('joint_minimum', global_pair)]:
            a, b = seeds[p][i], seeds[q][j]
            weights = (cp*np.array(a['normal'])+cq*np.array(b['normal'])) % n
            result, cert, _ = transport.repair_case(points[:n]@weights % n, weights)
            witnesses[name] = {'seed_indices': [i, j], 'normals': [a['normal'], b['normal']],
                               'local_costs': [a['cost'], b['cost']], 'joint_cost': table[i][j],
                               'crt_generators': list(map(int, weights)), 'integer_dual': cert}
        joint[n] = {'primes': [p, q], 'all_pairs': len(seeds[p])*len(seeds[q]),
                    'global_minimum': global_best, 'local_minima_joint_minimum': locally_best[0],
                    'local_minima_pairs': len(local_pairs),
                    'cost_histogram': dict(sorted(Counter(x for row in table for x in row).items())),
                    'witnesses': witnesses}
        if n == 26:
            joint[n]['full_cost_table'] = table
        assert global_best <= locally_best[0]
    assert joint[26]['global_minimum'] == 6 and joint[26]['local_minima_joint_minimum'] == 9
    assert joint[39]['global_minimum'] == 7 and joint[39]['local_minima_joint_minimum'] == 9
    print('7742 joint selections checked; strict local/global tradeoffs found', flush=True)

    # One frozen choice across three composite targets, using the same computed
    # tables. No separate re-optimization of a seed at each composite is allowed.
    best_composite = None
    best_six = None
    simultaneous = 0
    for i, a in enumerate(seeds[2]):
        for j, b in enumerate(seeds[3]):
            for k, d in enumerate(seeds[13]):
                costs = (all_tables[6][i][j], all_tables[26][i][k], all_tables[39][j][k])
                simultaneous += int(costs == (0, 6, 7))
                row = (sum(costs), i, j, k, costs)
                if best_composite is None or row < best_composite:
                    best_composite = row
                total = (sum(costs)+a['cost']+b['cost']+d['cost'], i, j, k, costs)
                if best_six is None or total < best_six:
                    best_six = total
    assert simultaneous == 0 and best_composite[0] == 14 and best_six[0] == 18
    _, i, j, k, costs = best_six
    portfolio = {'frozen_seed_triples': 7*364*14, 'simultaneous_composite_minima': simultaneous,
                 'sum_of_separate_composite_minima': 13, 'minimum_composite_sum': 14,
                 'six_target_equal_weight_minimum': 18, 'seed_indices': [i, j, k],
                 'normals': [seeds[2][i]['normal'], seeds[3][j]['normal'], seeds[13][k]['normal']],
                 'costs_at_2_3_13': [seeds[2][i]['cost'], seeds[3][j]['cost'], seeds[13][k]['cost']],
                 'costs_at_6_26_39': list(costs), 'weights': 'one per separately declared target'}

    # Exact collision expectation on a FIXED same-prime source population.
    collision_checks = []
    for p in (2, 3, 13):
        a, b, ub, q, _ = f.block(p, 0)
        pop = points[:p]
        coarse = np.array(q.tolist(), dtype=np.int64)
        labels = [tuple(map(int, coarse@v % p)) for v in pop]
        always = sum(k*(k-1)//2 for k in Counter(labels).values())
        total_pairs = p*(p-1)//2
        for s in range(1, q.rows):
            observed = 0
            for seed in seeds[p]:
                normal = np.array(seed['normal'], dtype=np.int64)
                rows = []
                for _ in range(s):
                    rows.append(normal.copy()); normal = normal@u % p
                labs = [tuple(map(int, np.array(rows)@v % p)) for v in pop]
                observed += sum(k*(k-1)//2 for k in Counter(labs).values())
            prob = Fraction(p**(q.rows-s)-1, p**q.rows-1)
            expected = always+(total_pairs-always)*prob
            assert Fraction(observed, len(seeds[p])) == expected
            collision_checks.append({'p': p, 's': s, 'expected_pairs': str(expected)})

    # Non-vacuous short-vector filter tests at larger primes. Sampled seeds are
    # NOT described as exhaustive or as a proof of the universal probability bound.
    rng = random.Random(2026091008)
    filter_tests = []
    for p in (17, 19, 31, 277):
        a, b, ub, q, _ = f.block(p, 0)
        dim = q.rows
        max_q = int_root((p**(dim-1)-1)//42**3, 3)
        vv = np.array(sphere_vectors(max_q), dtype=np.int64)
        norms = np.sum(vv*vv, axis=1)
        qs = np.array(q.tolist(), dtype=np.int64)
        passed = 0
        for _ in range(128):
            coeff = [rng.randrange(p) for _ in range(dim)]
            while not any(coeff):
                coeff = [rng.randrange(p) for _ in range(dim)]
            normal = np.array(coeff)@qs % p
            alive = np.ones(len(vv), dtype=bool)
            good = True
            for s in range(1, dim):
                alive &= (vv@normal % p == 0)
                normal = normal@u % p
                bad = np.array([int(v)**3*42**3 < p**s for v in norms], dtype=bool)
                if np.any(alive & bad):
                    good = False
            passed += int(good)
        filter_tests.append({'p': p, 'f': dim, 'sampled_seeds': 128,
                             'passed': passed, 'candidate_vectors': len(vv),
                             'max_squared_norm_enumerated': max_q})
    print('Nontrivial finite short-vector filters checked', flush=True)

    # Operation-safe refinements for the actual witness flags, not only numbers.
    t6_rows = []
    for p, seed_index in ((2, 3), (13, 2), (3, 24), (13, 4), (3, 237)):
        a, b, ub, q, _ = f.block(p, 0)
        quotient = c.Quotient(b)
        domain = tuple(range(int(b.det())))
        transition = {i: quotient.label(c.U*sp.Matrix(quotient.points[i])) for i in domain}
        normal = sp.Matrix([seeds[p][seed_index]['normal']])
        obs = {i: int((normal*sp.Matrix(quotient.points[i]))[0]) % p for i in domain}
        seq = [t6.class_count(x) for x in t6.future_partition_sequence(domain, transition, obs)]
        assert seq == [p**s for s in range(1, q.rows+1)]
        t6_rows.append({'p': p, 'seed_index': seed_index, 'sequence': seq})
    constants = {'shortest_squared_constant': '1/42',
                 'per_block_bad_fraction_upper': '5/64',
                 'mixed_single_target_bad_fraction_upper': '1/64',
                 'uniform_prime_power_lambda6_constant': '384*42^(5/2)/pi^3',
                 'sharpness': 'constants deliberately coarse; general proof, not fitted'}
    return {'status': 'PASS_EXACT_ENUMERATION_AND_INTEGER_DUALS_NOT_ADMITTED',
            'source_snapshot': SOURCE, 'prime_seed_counts': {p: len(v) for p, v in seeds.items()},
            'local_cost_histograms': local_histograms, 'incidence_checks': incidence,
            'small_block_geometry': geometry, 'mixed_prime_search': joint, 'frozen_portfolio': portfolio,
            'collision_expectation_checks': collision_checks, 'sampled_short_vector_filters': filter_tests,
            'witness_T6_sequences': t6_rows, 'theorem_constants': constants,
            'reuse': {'flag_blob': FLAG_BLOB, **c.PINS},
            'boundaries': ['not a uniform all-integer shape theorem for one frozen seed choice',
                           'not constant average repair cost', 'U is not a native isometry',
                           'joint optimum only within declared prime blocks and first-layer seeds',
                           'no independent review, formal proof or Foundation promotion']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.source_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, separators=(',', ':'))+'\n')
    print('PASS; '+str(args.output), flush=True)


if __name__ == '__main__':
    main()
