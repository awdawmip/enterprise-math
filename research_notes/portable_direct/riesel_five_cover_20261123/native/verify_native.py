"""Native integer BRC execution of new complete-cover families and fixed fibers.

Completeness and optimality are proved in the companion mathematical notes.
This execution validates the new examples on the previously frozen native code.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
import json
from math import lcm, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_REL = Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
GAP_REL = Path('research_notes/portable_direct/riesel_spectrum_20261121/gap/small_gap_certificate.json')
BASE_BLOB = 'c1909a5e2e209b0f6bd5f613d0f758dde45caee9'
NATIVE_COMMIT = 'b1efc6c805661ed7b476e6e730107da6043176ee'
PREVIOUS_COMMIT = 'a2ae4d93398425e67dacbb4c99b7f3a6755e5771'
V = (5, 13, 11, 61, 331)
W = (19, 37, 73, 109)
K, L = 14436565, 80754838636615
ORDER2 = {5: 4, 13: 12, 19: 18, 37: 36, 73: 9, 109: 36,
          433: 72, 38737: 72}
CASES = [
    {'label': 'W_H1_least_root',
     'a': 61222665924684986635031943105967801542609331745630965435461,
     'rows': [(5, 0), (13, 3), (19, 1), (37, 7), (109, 13)],
     'period_n': 1260, 'expected_missing': [216, 108, 39, 26, 13, 0]},
    {'label': 'W_H0_least_root',
     'a': 62924692928616911047137866279148034266265445978646078445719,
     'rows': [(5, 0), (13, 1), (37, 3), (19, 0), (109, 15)],
     'period_n': 1260, 'expected_missing': [216, 108, 69, 46, 23, 0]},
    {'label': 'R0_least_cost_five_root',
     'a': 73841986537470627371286709939739215853723074973610308115228565383,
     'rows': [(5, 1), (13, 0), (37, 4), (19, 1), (73, 7)],
     'period_n': 1260, 'expected_missing': [216, 108, 39, 26, 13, 0],
     'fiber_modulus': K, 'fiber_residue': 666303, 'fiber_primes': list(V)},
    {'label': 'R1_least_nested_optimal_six_root',
     'a': 1597463687996365290740241630260436015028835427889255944107518938773290244463,
     'rows': [(5, 1), (13, 0), (19, 4), (73, 1), (433, 34), (38737, 16)],
     'period_n': 2520, 'expected_missing': [432, 216, 78, 52, 26, 13, 0],
     'fiber_modulus': L, 'fiber_residue': 12926327728523,
     'fiber_primes': list(V + W)}
]


def blob(data):
    return sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def main():
    root = next(p for p in HERE.parents if (p/BASE_REL).is_file())
    source_default = next((p for p in (root/'src', root/'vendor_src')
                           if (p/'enterprise_math/brc_transport.py').is_file()), None)
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, default=source_default)
    parser.add_argument('--output', type=Path, default=HERE/'native_certificate.json')
    args = parser.parse_args()
    if args.source_dir is None:
        parser.error('Pass --source-dir for the pinned native source directory.')
    base_bytes = (root/BASE_REL).read_bytes()
    assert blob(base_bytes) == BASE_BLOB
    base = json.loads(base_bytes)
    assert base['project_source_commit'] == NATIVE_COMMIT
    source_checks = []
    for filename, expected in base['project_source_blobs'].items():
        observed = blob((args.source_dir/'enterprise_math'/filename).read_bytes())
        assert observed == expected
        source_checks.append({'module': filename, 'git_blob': observed})
    gap = json.loads((root/GAP_REL).read_text())
    astar, M = int(gap['a_star']), int(gap['M'])
    P, H = gap['P'], set(gap['H'])
    assert prod(P) == M and len(H) == 36
    assert prod(V) == K and prod(V + W) == L

    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    twice = step.then(step)
    assert step.entries == ((Fraction(1), Affine(((2,),), (1,)), 1),)
    assert twice.entries == ((Fraction(1), Affine(((4,),), (3,)), 1),)

    def advance(value):
        (point, weight), = step.evaluate((value,)).items()
        assert weight.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    checks = []
    for case in CASES:
        a, rows, period = case['a'], case['rows'], case['period_n']
        assert a >= astar and a % 2 == 1 and (a-astar) % (6*M) == 0
        assert len(set(q for q, _ in rows)) == len(rows)
        assert lcm(210, *(ORDER2[q] for q, _ in rows)) == period
        fiber_primes = case.get('fiber_primes', [])
        if fiber_primes:
            assert a % case['fiber_modulus'] == case['fiber_residue']
        for q, c in rows:
            assert a*a*pow(4, c, q) % q == 1
        channels = sorted(set(P) | set(V) | set(W) | {q for q, _ in rows})
        x = a*a-1
        missing = [0] * (len(rows)+1)
        readouts = old_equalities = fiber_equalities = 0
        private = {}
        for n in range(1, period+1):
            x = advance(x)
            assert x == (a*a << n)-1
            hits = set()
            for q in channels:
                quotient, (residual,) = euclidean_digits(x, (q,))
                assert quotient*q + residual == x and 0 <= residual < q
                readouts += 1
                if residual == 0:
                    assert 1 < q < x
                    hits.add(q)
                if q in P:
                    assert residual == (astar*astar*pow(2, n, q)-1) % q
                    old_equalities += 1
                if q in fiber_primes:
                    r = case['fiber_residue']
                    assert residual == (r*r*pow(2, n, q)-1) % q
                    fiber_equalities += 1
            old_hole = not bool(hits.intersection(P))
            assert old_hole == (n % 2 == 0 and (n//2) % 105 in H)
            for q, c in rows:
                assert (q in hits) == (n % ORDER2[q] == 2*c % ORDER2[q])
            if old_hole:
                for t in range(len(rows)+1):
                    if not hits.intersection(q for q, _ in rows[:t]):
                        missing[t] += 1
                selected_hits = hits.intersection(q for q, _ in rows)
                if len(selected_hits) == 1:
                    q, = selected_hits
                    private.setdefault(q, n)
        assert missing == case['expected_missing']
        assert set(private) == {q for q, _ in rows}
        checks.append({
            'label': case['label'], 'root': str(a), 'root_digits': len(str(a)),
            'ordered_rows': [{'q': q, 'phase_u': c, 'root_residue': a % q}
                             for q, c in rows],
            'period_n': period, 'uncovered_counts': missing,
            'proper_private_old_hole_indices': private,
            'native_updates': period, 'native_readouts': readouts,
            'old_projection_equalities': old_equalities,
            'additional_fixed_fiber_equalities': fiber_equalities,
            'fixed_fiber_modulus': case.get('fiber_modulus'),
            'fixed_fiber_residue': case.get('fiber_residue'),
            'last_native_state_sha256': sha256(str(x).encode()).hexdigest()
        })
    result = {
        'schema': 'riesel-complete-five-cover-and-fiber-native-v1',
        'status': 'AUTHOR_NATIVE_EXECUTION; NOT_INDEPENDENT_REVIEW',
        'native_source_commit': NATIVE_COMMIT,
        'native_source_blobs': source_checks,
        'base_certificate_git_blob': BASE_BLOB,
        'cases': checks,
        'native_updates': sum(c['native_updates'] for c in checks),
        'native_readouts': sum(c['native_readouts'] for c in checks),
        'old_projection_equalities': sum(c['old_projection_equalities'] for c in checks),
        'additional_fixed_fiber_equalities': sum(c['additional_fixed_fiber_equalities'] for c in checks),
        'reused_least_cost_five_native_membership': {
            'commit': PREVIOUS_COMMIT,
            'path': 'research_notes/portable_direct/riesel_observers_20261122/native/native_certificate.json',
            'field': 'minimal_root_native_check',
            'scope': 'Same root and phase rows; new global minimum proof is in companion global/observer notes.'
        },
        'all_future_bridge': 'The old-hole predicate has exact known period210 in n. New zero predicates have periods ord_q(2). Their least common multiples are1260 or2520 as checked; integer readouts themselves need not have these smaller periods.',
        'completeness_and_optimality_scope': 'Proved in companion mathematical notes; not inferred from four representative trajectories. No total-minimum equality is inferred from private witnesses for a single dictionary.',
        'native_scope': 'Fixed X6 anchor and typed integer register; positive singleton weight1 and multiplicity1; n counts updates and is not physical time; prime readouts are not axes or extra branches.',
        'observer_scope': 'Finite residue predicates retain their stated observation scope. The integer state and unbounded joint cofactor information are not replaced by residues.'
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['native_updates', 'native_readouts',
          'old_projection_equalities', 'additional_fixed_fiber_equalities']}
          | {'status': 'PASS', 'cases': len(checks), 'output': str(args.output)}))


if __name__ == '__main__':
    main()
