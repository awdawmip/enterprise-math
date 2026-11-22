"""Native BRC execution of all twelve optimal five-channel phase dictionaries.

The mathematical completeness and root counting proofs are separate.  This
checks the new observables on the pinned integer update and digit readout paths.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations
import json
from math import prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_REL = Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
GAP_REL = Path('research_notes/portable_direct/riesel_spectrum_20261121/gap/small_gap_certificate.json')
BASE_BLOB = 'c1909a5e2e209b0f6bd5f613d0f758dde45caee9'
NATIVE_COMMIT = 'b1efc6c805661ed7b476e6e730107da6043176ee'
ORDER2 = {5: 4, 13: 12, 11: 10, 61: 60, 331: 30}
U = (11, 61, 331)
MINIMAL_NESTED_ROOT = 39741911323337250951212360989279347168190786597922987443929


def blob(data):
    return sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def crt(pairs):
    value, modulus = 0, 1
    for residue, q in pairs:
        value += modulus * ((residue-value)*pow(modulus, -1, q) % q)
        modulus *= q
    return value, modulus


def phase(q, epsilon, category):
    return next(c for c in range(ORDER2[q]//2)
                if c % 5 == category and (q == 11 or c % 3 == 1)
                and (q != 61 or c % 2 == epsilon))


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

    def check_root(a, epsilon, assignment, label):
        assert a > 1 and a % 3 == 0 and (a-astar) % (2*M) == 0
        rows = [(5, 1-epsilon), (13, 3*epsilon)]
        rows += [(q, phase(q, epsilon, r)) for r, q in zip((0, 1, 4), assignment)]
        assert len({q for q, _ in rows}) == 5
        for q, c in rows:
            assert a*a*pow(4, c, q) % q == 1
        x = a*a-1
        missing = [[] for _ in range(6)]
        projections = 0
        old_equalities = 0
        for n in range(1, 421):
            x = advance(x)
            assert x == (a*a << n)-1
            hits = set()
            for q in P + [q for q, _ in rows]:
                quotient, (residual,) = euclidean_digits(x, (q,))
                assert quotient*q + residual == x and 0 <= residual < q
                projections += 1
                if residual == 0:
                    assert 1 < q < x
                    hits.add(q)
                if q in P:
                    assert residual == (astar*astar*pow(2, n, q)-1) % q
                    old_equalities += 1
            old_hole = not bool(hits.intersection(P))
            assert old_hole == (n % 2 == 0 and (n//2) % 105 in H)
            for q, c in rows:
                assert (q in hits) == (n % ORDER2[q] == 2*c % ORDER2[q])
            if old_hole:
                for t in range(6):
                    if not hits.intersection(q for q, _ in rows[:t]):
                        missing[t].append(n % 420)
        counts = [len(v) for v in missing]
        assert counts == [72, 36, 13, 8, 3, 0]
        expected_four = [128, 308, 368] if epsilon == 0 else [98, 158, 338]
        assert sorted(missing[4]) == expected_four
        assert projections == 10500 and old_equalities == 8400
        return {'label': label, 'epsilon': epsilon,
                'category_assignment': dict(zip(('0', '1', '4'), assignment)),
                'root': str(a), 'root_digits': len(str(a)),
                'root_residue_mod_K': a % 14436565,
                'ordered_rows': [{'q': q, 'phase_u': c, 'root_residue': a % q}
                                 for q, c in rows],
                'uncovered_counts_mod_420': counts,
                'four_channel_missing_n_mod_420': expected_four,
                'native_updates': 420, 'native_readouts': projections,
                'old_projection_equalities': old_equalities,
                'last_native_state_sha256': sha256(str(x).encode()).hexdigest()}

    checks = []
    for epsilon in (0, 1):
        for assignment in permutations(U):
            rows = [(5, 1-epsilon), (13, 3*epsilon)]
            rows += [(q, phase(q, epsilon, r))
                     for r, q in zip((0, 1, 4), assignment)]
            pairs = [(astar, 2*M), (0, 3)]
            pairs += [(pow(pow(2, c, q), -1, q), q) for q, c in rows]
            a, modulus = crt(pairs)
            assert modulus == 6*M*14436565
            checks.append(check_root(a, epsilon, assignment, 'positive_inverse_signs'))
    minimal_check = check_root(MINIMAL_NESTED_ROOT, 1, (61, 11, 331),
                              'least_positive_nested_root_from_observer_certificate')
    result = {
        'schema': 'riesel-optimal-observers-native-integration-v1',
        'status': 'AUTHOR_NATIVE_EXECUTION; NOT_INDEPENDENT_REVIEW',
        'native_source_commit': NATIVE_COMMIT,
        'native_source_blobs': source_checks,
        'base_certificate_git_blob': BASE_BLOB,
        'reused_dependency': {'commit': 'af9e1a5e49386a28283781876e10742a71991036',
                              'path': str(GAP_REL),
                              'scope': 'All-future old holes and old residue trajectory'},
        'twelve_phase_dictionaries': checks,
        'minimal_root_native_check': minimal_check,
        'native_updates': 13*420,
        'native_readouts': 13*10500,
        'old_projection_equalities': 13*8400,
        'optimal_missing_counts_per_420': [72, 36, 13, 8, 3, 0],
        'phase_completeness_and_minimality': 'Proved in companion staircase/observer proofs; not inferred from these thirteen runs.',
        'all_future_bridge': 'Old-hole predicate has period210 in n, all five new zero-phase periods divide60; their combined coverage predicate has period420. Both facts have separate exact proofs.',
        'sign_lifting': 'Changing any root residue sign leaves a^2 and every readout at that prime unchanged. CRT independently realizes all32 signs in each phase dictionary.',
        'native_scope': 'Fixed X6 anchor and typed integer register. Positive singleton weight1 and multiplicity1. Index n is an update count, not physical time. Prime readouts are not axes or extra branches.',
        'observer_scope': 'Optimal-budget predicates only; no claim that a modK determines the full integer state, cofactor structure, or unbounded covering complexity.'
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'output': str(args.output),
                      'phase_dictionaries': 12, 'checked_roots': 13,
                      'updates': 13*420, 'readouts': 13*10500,
                      'minimal_root_digits': len(str(MINIMAL_NESTED_ROOT))}))


if __name__ == '__main__':
    main()
