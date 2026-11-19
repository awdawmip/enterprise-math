"""Verify the two new certificates and the exact exchange structure.

Run from the workspace/repository root:
    python research_notes/portable_direct/riesel_structure_20261119/verify_new_roots.py --source-dir vendor_src

The original prime/order proofs are reused from the prior exact certificate;
their pinned BRC source blobs are checked before the new residual cycles run.
This checks the new certificates, not a fresh independent project Review and
not a repeat of the finite CRT minimization in optimize_local_shapes.py.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, permutations
import json
from math import factorial, gcd, lcm, prod
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parents[3] / 'src')
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    prior_dir = directory.with_name('riesel_mixed_20261119')
    prior = json.loads((prior_dir / 'results.json').read_text())
    original = json.loads((prior_dir / 'certificate.json').read_text())['original']
    local = json.loads((directory / 'local_shapes_results.json').read_text())
    for name, expected in prior['project_source_blobs'].items():
        blob = (args.source_dir / 'enterprise_math' / name).read_bytes()
        assert sha1(b'blob ' + str(len(blob)).encode() + b'\0' + blob).hexdigest() == expected
    sys.path.insert(0, str(args.source_dir.resolve()))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits

    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    double = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (0,)), 1)])

    def advance(packet, value):
        (point, weights), = packet.evaluate((value,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    def rem(value, modulus):
        return euclidean_digits(value, (modulus,))[1][0]

    rows = original['rows']
    primes = [r['p'] for r in rows]
    periods = local['effective_periods']
    phases = local['original_u_phases']
    length = lcm(*periods)
    assert length == 3360 and lcm(*(r['order'] for r in rows)) == 2 * length
    assert [(r['p'], r['order']) for r in rows] == [
        (r['p'], r['order']) for r in prior['shared_channel_proofs']]
    by_prime = {p: i for i, p in enumerate(primes)}
    masks = [[sum(1 << u for u in range(c, length, e)) for c in range(e)]
             for e in periods]
    full = (1 << length) - 1

    def union(vector):
        total = 0
        for i, c in enumerate(vector):
            total |= masks[i][c]
        return total

    assert union(phases) == full
    groups = [(5, [31, 41, 151, 1321]),
              (7, [71, 113, 127, 281, 337, 14449, 29191])]
    duplicate_pairs = [[97, 673], [641, 6700417]]
    all_blocks = [ps for _, ps in groups] + duplicate_pairs
    assert sum(map(len, all_blocks)) == len(set(p for ps in all_blocks for p in ps))
    expected_moves = set()
    group_checks = []
    for q, group in groups:
        indices = [by_prime[p] for p in group]
        residues = [phases[i] % q for i in indices]
        assert len(set(residues)) == len(group)
        if q == 5:
            assert set(residues) == {0, 1, 2, 3}
            assert all(phases[i] % 5 == 4 for i, e in enumerate(periods)
                       if e % 5 == 0 and i not in indices)
        else:
            assert set(residues) == set(range(7))
            assert indices == [i for i, e in enumerate(periods) if e % 7 == 0]

        def with_coordinate(i, r):
            e = periods[i]
            h = e // q
            assert gcd(q, h) == 1
            candidates = [c for c in range(e) if c % q == r and c % h == phases[i] % h]
            assert len(candidates) == 1
            return candidates[0]

        count = 0
        for perm in permutations(residues):
            new = list(phases)
            for i, r in zip(indices, perm):
                new[i] = with_coordinate(i, r)
            assert union(new) == full
            count += 1
        assert count == factorial(len(group))
        group_checks.append({'q': q, 'primes': group, 'permutations_checked': count,
                             'all_cover': True})
        for i, j in combinations(indices, 2):
            new = list(phases)
            new[i] = with_coordinate(i, phases[j] % q)
            new[j] = with_coordinate(j, phases[i] % q)
            expected_moves.add(tuple(new))

    for p, q in duplicate_pairs:
        i, j = by_prime[p], by_prime[q]
        assert periods[i] == periods[j] and phases[i] != phases[j]
        new = list(phases)
        new[i], new[j] = new[j], new[i]
        assert union(new) == full
        expected_moves.add(tuple(new))
    assert len(expected_moves) == 29
    assert expected_moves == {tuple(m['u_phases']) for m in local['double_valid']}
    assert local['single_change_population'] == 474 and not local['single_valid']
    assert local['double_change_population'] == 101906
    assert local['translation_classes_in_radius2'] == 29
    assert factorial(4) * factorial(7) * 2 * 2 == 483840

    def original_hits(n):
        return [r['p'] for r in rows if n % r['order'] == r['exponent_phase']]

    assert original_hits(7) == [97] and original_hits(223) == [673]
    assert (223 % 48, 7 % 48) == (31, 7)

    # Both winners have the same genuinely different radius-two shape.
    neighbor = list(phases)
    neighbor[by_prime[113]] = 5
    neighbor[by_prime[337]] = 7
    assert tuple(neighbor) in expected_moves
    assert union(neighbor) == full
    answers = []
    for filename, branch, expected_shift in [
            ('optimized_results.json', 'unrestricted', 1113),
            ('optimized_results_mod3.json', 'divisible3', 1857)]:
        result = json.loads((directory / filename).read_text())
        a = int(result['minimum_positive_odd_root'])
        k = a * a
        table = [{key: r[key] for key in ('p', 'order', 'exponent_phase', 'a_residue')}
                 for r in result['rows']]
        assert a > 1 and a % 2 == 1 and str(k) == result['minimum_square_k']
        assert [(r['p'], r['order']) for r in table] == [(r['p'], r['order']) for r in rows]
        assert result['distinct_odd_root_classes'] == 29 * 3360 * 2**20 == 102173245440
        assert len(result['all_shape_minima']) == 29
        assert min(int(s['minimum_root']) for s in result['all_shape_minima']) == a
        assert all(r['exponent_phase'] == (2 * ((c + expected_shift) % e) + 1) % r['order']
                   for r, c, e in zip(table, neighbor, periods))
        cycles = {}
        checked_rows = []
        for row in table:
            p, d, b, root_residue = (row[key] for key in ('p', 'order', 'exponent_phase', 'a_residue'))
            assert rem(a, p) == root_residue and 0 < root_residue < p
            current = rem(k - 1, p)
            cycle = []
            for _ in range(d):
                cycle.append(current)
                current = rem(advance(step, current), p)
            assert current == cycle[0]
            assert [n for n, value in enumerate(cycle) if value == 0] == [b]
            cycles[p] = cycle
            checked_rows.append(dict(row, cycle_closed=True, unique_zero_phase=b,
                                     residual_cycle=cycle))
        hits = [[r['p'] for r in table if cycles[r['p']][n % r['order']] == 0]
                for n in range(2 * length)]
        holes = [n for n, hit in enumerate(hits) if not hit]
        assert holes == result['uncovered_phases']
        assert sum(bool(hits[n]) for n in range(1, 2 * length, 2)) == 3360
        assert sum(bool(hits[n]) for n in range(0, 2 * length, 2)) == 2208
        assert len(holes) == 1152 and all(n % 2 == 0 for n in holes)
        assert 2 * k - 1 > max(primes)
        root, modulus = (3, 6) if branch == 'divisible3' else (1, 2)
        for r in table:
            root += modulus * ((r['a_residue'] - root) * pow(modulus, -1, r['p']) % r['p'])
            modulus *= r['p']
        assert root == a and modulus == int(result['odd_crt_modulus'])
        least_hole = min(n for n in holes if n > 0)
        b = a
        for _ in range(least_hole // 2):
            b = advance(double, b)
        value = k - 1
        for _ in range(least_hole):
            value = advance(step, value)
        left, right = b - 1, b + 1
        assert value == left * right and 1 < left < right < value
        residue3 = rem(k - 1, 3)
        residue3_odd = rem(advance(step, residue3), 3)
        assert rem(advance(step, residue3_odd), 3) == residue3
        p_union_3 = a % 3 != 0
        assert p_union_3 == (branch == 'unrestricted')
        assert (residue3 == 0) == p_union_3
        assert not p_union_3 or all(hits[n] or n % 2 == 0 for n in range(2 * length))
        compact = {'a': str(a), 'k': str(k), 'rows': table,
                   'source_url': result['source_url'], 'source_table': result['source_table'],
                   'u_shift_from_113_337_neighbor': expected_shift,
                   'exponent_shift_from_113_337_neighbor': 2 * expected_shift}
        (directory / ('new_table_' + branch + '.json')).write_text(json.dumps(compact, indent=2) + '\n')
        answers.append({
            'branch': branch, 'a': str(a), 'k': str(k),
            'root_digits': len(str(a)), 'square_digits': len(str(k)), 'a_mod3': a % 3,
            'crt_modulus': str(modulus), 'crt_reconstruction_passed': True,
            'modified_primes': [113, 337], 'modified_u_phases': [5, 7],
            'net_u_translation': expected_shift, 'net_exponent_translation': 2 * expected_shift,
            'checked_rows': checked_rows,
            'coverage': {'odd_covered': 3360, 'even_covered': 2208, 'uncovered': 1152,
                         'period': 6720, 'phase_zero_is_hole': 0 in holes},
            'first_positive_fixed_prime_hole': {'n': least_hole, 'value': str(value),
                                               'left_factor': str(left), 'right_factor': str(right)},
            'proper_fixed_factor_bound_passed': True,
            'P_union_3_full_cover': p_union_3,
            'P_union_3_boundary': 'False does not prove absence of another finite prime cover.',
        })
    report = {
        'schema': 'RIESEL_LOCAL_SHAPES_NEW_ROOT_VERIFICATION_V1',
        'researcher_id': 'EM-DIRECT-970E1C',
        'research_activity_id': 'RA-D2EC212845B63844081F9A14',
        'status': 'AUTHOR_PROOF_AND_EXACT_FINITE_CHECK; NOT_INDEPENDENT_PROJECT_REVIEW',
        'project_source_commit': prior['project_source_commit'],
        'project_source_blobs': prior['project_source_blobs'],
        'source_blobs_verified': True,
        'shared_prime_order_proofs_reused': 'research_notes/portable_direct/riesel_mixed_20261119/results.json',
        'shared_proof_sha256': sha256((prior_dir / 'results.json').read_bytes()).hexdigest(),
        'native_carrier': 'Fixed arbitrary X6 anchor; internal integer residual registers. Prime channels are not spatial axes; exponent is not physical heartbeat time.',
        'group_checks': group_checks,
        'pair_move_classification_matches_K4_K7_two_edges': True,
        'constructed_labelled_cover_family_size': 483840,
        'family_count_basis': 'Independent faithful actions on four disjoint labelled channel blocks; no quotient by translation. Only the radius-two family of 29 translation classes is optimized.',
        'intervention_witnesses': {'only97_moved_first_named_hole': 7,
                                 'only673_moved_first_named_hole': 223,
                                 'both_moved_cover': True},
        'certificates': answers,
    }
    (directory / 'new_root_verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'source_blobs_verified': True, 'group_checks': group_checks,
                      'constructed_labelled_cover_family_size': 483840,
                      'certificates': [{k: v for k, v in c.items() if k != 'checked_rows'}
                                       for c in answers]}, indent=2))


if __name__ == '__main__':
    main()
