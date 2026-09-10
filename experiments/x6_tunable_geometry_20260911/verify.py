#!/usr/bin/env python3
"""Exact finite checks for tunable local geometry and projective witness barriers.

Infinite density/window statements are proved in the accompanying research note.
This script checks exact rational parameter identities and finite projective/Krylov
claims against the frozen intermediate-flag implementation. It does not admit a
Foundation law or claim a second-moment concentration theorem.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json
from fractions import Fraction
from math import isqrt
from pathlib import Path
import numpy as np
import sympy as sp

FLAG_PATH = 'experiments/x6_intermediate_flags_20260910/verify.py'
FLAG_BLOB = 'c41fdd1a468d8d7ee52c96c3a739dd59c78892ec'
EPS = Fraction(1, 200)
BETA = Fraction(1, 1)
GAMMA = Fraction(3, 8)
ALPHA = Fraction(6, 25)


def projective(p: int, dim: int):
    for first in range(dim):
        for tail in itertools.product(range(p), repeat=dim-first-1):
            yield (0,)*first + (1,) + tail


def rref_mod(rows, p: int):
    a = [[int(x) % p for x in row] for row in rows]
    if not a:
        return ()
    m, n, r = len(a), len(a[0]), 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][j]:
                t = a[i][j]
                a[i] = [(x - t*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return tuple(tuple(row) for row in a[:r])


def quotient_u(flags, p: int):
    c = flags.c
    _, _, ub, q, _ = flags.block(p, 0)
    dim = q.rows
    pivots = []
    for j in range(6):
        if len(rref_mod(q[:, pivots+[j]].T.tolist(), p)) > len(pivots):
            pivots.append(j)
        if len(pivots) == dim:
            break
    right = sp.zeros(6, dim)
    inv = q[:, pivots].inv_mod(p)
    for i, pos in enumerate(pivots):
        for j in range(dim):
            right[pos, j] = inv[i, j]
    uu = np.array((q * ub * right).tolist(), dtype=np.int64) % p
    return np.array(q.tolist(), dtype=np.int64) % p, uu


def krylov_signature(v, s: int, p: int, uu):
    cur = np.array(v, dtype=np.int64) % p
    rows = []
    for _ in range(s):
        rows.append(tuple(map(int, cur)))
        cur = cur @ uu.T % p
    return rref_mod(rows, p)


def sphere_vectors(max_q: int, dim: int = 6):
    out = []
    r = isqrt(max_q)
    for v in itertools.product(range(-r, r+1), repeat=dim):
        q = sum(x*x for x in v)
        if 0 < q <= max_q:
            out.append(v)
    return out


def int_root(n: int, degree: int):
    lo, hi = 0, 1
    while hi**degree <= n:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


def verify(root: Path):
    raw = (root / FLAG_PATH).read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert blob == FLAG_BLOB, blob
    spec = importlib.util.spec_from_file_location('x6_tunable_flags', root / FLAG_PATH)
    flags = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(flags)
    flags.configure(root)

    r6 = Fraction(2) * EPS / (5 * (1 + EPS))
    bad_fraction = Fraction(5, 2) * r6
    good_fraction = 1 - bad_fraction
    conditioning = 1 / good_fraction
    assert good_fraction == Fraction(200, 201)
    assert conditioning == 1 + EPS
    assert r6 == Fraction(2, 1005)
    assert r6 < Fraction(1, 64)

    frontier = 6*GAMMA - (1 + BETA + EPS)
    assert frontier == Fraction(49, 200)
    assert ALPHA == Fraction(48, 200)
    assert frontier - ALPHA == Fraction(1, 200)
    single_crit = (1 + BETA + EPS) / 6
    assert single_crit == Fraction(401, 1200)

    injectivity = []
    penultimate = []
    for p in (2, 3, 13):
        q, uu = quotient_u(flags, p)
        f = uu.shape[0]
        lines = list(projective(p, f))
        for s in range(1, f):
            sigs = [krylov_signature(v, s, p, uu) for v in lines]
            assert len(set(sigs)) == len(lines)
            injectivity.append({'p': p, 'f': f, 's': s, 'projective_lines': len(lines),
                                'distinct_krylov_signatures': len(set(sigs))})
        if f > 1:
            P = (p**f - 1)//(p-1)
            assert len(lines) == P
            penultimate.append({'p': p, 'f': f, 'witness_lines': P,
                                'seed_atoms': P, 'event_atoms_per_witness': 1,
                                'union_bound_after_signature_dedup': 'exact'})

    catalogs = []
    for p in (17, 19, 31, 277):
        q, uu = quotient_u(flags, p)
        f = uu.shape[0]
        s = f-1
        max_q = int_root((p**s - 1)//(42**3), 3)
        vv = sphere_vectors(max_q)
        sigs = set()
        mult = {}
        for v in vv:
            t = tuple(map(int, (q @ np.array(v, dtype=np.int64)) % p))
            assert any(t)
            sig = krylov_signature(t, s, p, uu)
            sigs.add(sig)
            mult[sig] = mult.get(sig, 0) + 1
        P = (p**f - 1)//(p-1)
        raw_num = len(vv)
        dedup_num = len(sigs)
        assert dedup_num <= raw_num//2
        catalogs.append({'p': p, 'f': f, 's': s, 'max_Q': max_q,
                         'signed_candidates': raw_num,
                         'distinct_projective_krylov_events': dedup_num,
                         'maximum_integer_witness_multiplicity_per_event': max(mult.values()),
                         'raw_first_moment_numerator': raw_num,
                         'exact_union_numerator_after_signature_dedup': dedup_num,
                         'seed_atom_denominator': P})

    p = 2
    _, uu = quotient_u(flags, p)
    lines = list(projective(p, 3))
    sigs = [krylov_signature(v, 2, p, uu) for v in lines]
    assert len(set(sigs)) == 7
    subset_checks = 0
    for mask in range(1, 1 << 7):
        chosen = {sigs[i] for i in range(7) if (mask >> i) & 1}
        assert len(chosen) == mask.bit_count()
        subset_checks += 1

    return {
        'status': 'PASS_EXACT_FINITE_CHECKS_NOT_INFINITE_PROOF_OR_ADMISSION',
        'source_flag_blob': FLAG_BLOB,
        'tunable_example': {
            'epsilon_conditioning_exponent': str(EPS),
            'r_sixth_power': str(r6),
            'local_good_fraction_lower_bound': str(good_fraction),
            'conditioning_factor_upper_bound': str(conditioning),
            'beta': str(BETA), 'gamma': str(GAMMA),
            'window_alpha_frontier_for_this_epsilon': str(frontier),
            'explicit_alpha': str(ALPHA),
            'summability_margin': str(frontier-ALPHA),
            'single_target_gamma_critical': str(single_crit),
            'local_shape_constant': 'sqrt(6/7)/3 * (2/1005)^(1/6)',
            'old_lock_threshold_dominates_new': True,
        },
        'projective_krylov_injectivity_checks': injectivity,
        'penultimate_disjoint_event_checks': penultimate,
        'penultimate_actual_candidate_catalogs': catalogs,
        'all_nonempty_binary_penultimate_subset_checks': subset_checks,
        'boundaries': [
            'projective/signature compression is scoped to local Boolean seed-survival events',
            'penultimate disjointness blocks a universal second-moment improvement from local rank data alone',
            'the tunable theorem trades a worse fixed geometric constant for a better conditioning exponent',
            'epsilon cannot be set to zero while retaining this proof with a positive uniform local shape constant',
            'no all-integer constant-shape, constant-transport, or Foundation theorem is claimed',
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source-root', type=Path, required=True)
    ap.add_argument('--output')
    args = ap.parse_args()
    out = verify(args.source_root)
    text = json.dumps(out, ensure_ascii=False, separators=(',', ':')) + '\n'
    if args.output:
        Path(args.output).write_text(text, encoding='utf-8')
    print(text, end='')

if __name__ == '__main__':
    main()
