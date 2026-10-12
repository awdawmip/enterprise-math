"""Independent exact static certificate audit; never imports author checkers.

This is a bounded review aid, not a census or a native research identity.
It reads only JSON certificates and records. All arithmetic uses Python ints
and fractions; no LLL proposal library or author arithmetic implementation.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import platform
import time

BASE = Path('/workspace/em-owner-resume-20261011/new-round-20261011/geo6-atomic-repair-current-20261011/validation-root/research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC')
OUT = Path(__file__).resolve().parent


def load(name):
    return json.loads((BASE / name).read_text())


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def det(matrix):
    """Fraction-free Bareiss determinant with exact division."""
    a = [row[:] for row in matrix]
    n = len(a)
    sign, previous = 1, 1
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        assert pivot is not None, 'singular certificate matrix'
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = value * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = value
    return sign * a[-1][-1]


def gs(rows):
    stars, norms, mu = [], [], []
    for row in rows:
        vector = list(map(Fraction, row))
        coefficients = []
        for star, norm in zip(stars, norms):
            coefficient = dot(row, star) / norm
            coefficients.append(coefficient)
            vector = [v - coefficient * u for v, u in zip(vector, star)]
        norm = dot(vector, vector)
        assert norm > 0
        stars.append(vector)
        norms.append(norm)
        mu.append(coefficients)
    return stars, norms, mu


def basis_audit(prime, weighted, unweighted, declared_norms):
    n = prime - 1
    assert len(weighted) == len(unweighted) == n
    weights = [prime * r - 1 for r in range(1, prime)]
    assert all(len(row) == n for row in weighted + unweighted)
    assert weighted == [[value * weight for value, weight in zip(row, weights)] for row in unweighted]
    determinant = det(unweighted)
    assert abs(determinant) == prime ** 21
    for row in unweighted:
        for k in range(1, 7):
            modulus = prime ** k
            assert sum(value * pow(r ** k, -1, modulus) for r, value in enumerate(row, 1)) % modulus == 0
    minor = [[pow(r ** k, -1, prime) for r in range(1, 7)] for k in range(1, 7)]
    minor_mod = det(minor) % prime
    assert minor_mod != 0
    stars, norms, mu = gs(weighted)
    assert norms == [Fraction(*pair) for pair in declared_norms]
    return {'prime': prime, 'dimension': n, 'unweighted_determinant': str(determinant),
            'index': str(prime ** 21), 'unit_minor_mod_p': minor_mod,
            'weighted_relationship': True, 'all_six_mixed_congruences': True,
            'gram_schmidt_exact_match': True,
            'minimum_D': [min(norms).numerator, min(norms).denominator],
            'minimum_D_floor': min(norms).numerator // min(norms).denominator}, stars, norms, mu


def main():
    start = time.monotonic()
    d19 = load('input.json')
    p19, stars19, norms19, mu19 = basis_audit(19, d19['weighted_basis'], d19['unweighted_basis'], d19['gram_schmidt_norms'])
    assert abs(det(d19['proposal_transform'])) == 1
    weighted_saturated = [[x * (19 * r - 1) for r, x in enumerate(row, 1)] for row in d19['saturated_basis']]
    transformed = [[sum(d19['proposal_transform'][i][k] * weighted_saturated[k][j] for k in range(18)) for j in range(18)] for i in range(18)]
    assert transformed == d19['weighted_basis']
    for i in range(18):
        denominator = d19['projector_denominators'][i]
        assert denominator > 0
        assert [Fraction(x, denominator) for x in d19['projector_numerators'][i]] == [x / norms19[i] for x in stars19[i]]
        for j in range(i + 1, 18):
            assert Fraction(d19['mu_scaled'][j][i], denominator) == mu19[j][i]
    p19['projector_and_mu_exact_match'] = True
    p19['proposal_unimodular_transform_exact_match'] = True
    atoms = [[q, r, 361 * q + 19 * r - 1] for q in range(1, 7) for r in range(1, 19) if 361 * q + 19 * r - 1 <= 2331]
    assert atoms == d19['atoms']
    assert len(d19['atom_representatives']) == len(atoms)
    for (q, r, _), representative in zip(atoms, d19['atom_representatives']):
        assert len(representative) == 18
        for k in range(1, 7):
            modulus = 19 ** k
            total = sum(value * pow(s ** k, -1, modulus) for s, value in enumerate(representative, 1))
            assert (total + pow((r + 19 * q) ** k, -1, modulus)) % modulus == 0
    p19['vertical_atom_count'] = len(atoms)
    p19['all_atom_particular_representatives_exact_match'] = True
    radius19 = {(3, 6): 1230 ** 2 + 147 ** 2, (4, 5): 869 ** 2 + 508 ** 2,
                (4, 6): 869 ** 2 + 147 ** 2, (5, 5): 2 * 508 ** 2,
                (5, 6): 508 ** 2 + 147 ** 2, (6, 6): 2 * 147 ** 2}
    p19['flatness_for_all_six_blocks'] = {str(split): {'R2': radius, 'all_D_strictly_above_4R2': all(x > 4 * radius for x in norms19)} for split, radius in radius19.items()}
    assert all(row['all_D_strictly_above_4R2'] for row in p19['flatness_for_all_six_blocks'].values())
    d17 = load('p17_q0_certificate.json')
    p17, _, norms17, _ = basis_audit(17, d17['weighted_basis'], d17['unweighted_basis'], d17['gram_schmidt_squared'])
    assert all(x > 2 * 2331 ** 2 for x in norms17)
    assert min(norms17) == Fraction(*d17['minimum_gram_schmidt_squared'])
    p17['homogeneous_q0_static_exclusion_verified'] = True
    p17['q0_R2'] = 2 * 2331 ** 2
    order1 = []
    for r in range(1, 17):
        cost = 289 + 17 * r - 1
        R2 = 2331 ** 2 + (2331 - cost) ** 2
        order1.append({'r': r, 'cost': cost, 'R2': R2,
                       'all_D_above_R2': all(x > R2 for x in norms17),
                       'single_nearest_integer_uniform_gate': all(x > 4 * R2 for x in norms17)})
    assert all(x['all_D_above_R2'] for x in order1)
    p17['order1_feasibility'] = {'representatives': order1, 'at_most_integers_per_coordinate': 2,
                                'max_total_leaves': 16 * 2 ** 16, 'max_total_nodes': 16 * (2 ** 17 - 1),
                                'not_a_census': True, 'does_not_prove_order1_empty': True}
    coverage = load('coverage_4_5.json')
    records, previous, primitive, shared = [], 0, 0, 0
    for row in coverage['intervals']:
        rec = load(row['path'])
        assert rec['completed_rows'] == rec['requested_rows'] == row['rows']
        lo, hi = rec['completed_rows']
        assert lo == previous and hi > lo
        previous = hi
        assert rec['state_counts'] == [8124, 8506]
        assert rec['primitive_cosets_checked'] == sum(rec['rejection_depth_counts'])
        assert rec['primitive_cosets_checked'] == row['primitive_cosets']
        assert rec['primitive_cosets_checked'] + rec['cancelled_pairs'] == (hi - lo) * 8506
        assert rec['kernel'] is None
        primitive += rec['primitive_cosets_checked']
        shared += rec['cancelled_pairs']
        records.append({'path': row['path'], 'rows': [lo, hi], 'reported_rejections': rec['primitive_cosets_checked']})
    assert previous == 8124
    assert primitive == coverage['primitive_cosets'] == 45287075
    assert shared == coverage['shared_atom_pairs'] == 23815669
    assert primitive + shared == coverage['state_pairs'] == 8124 * 8506
    higher = []
    for name in ['audit_3_6.json', 'block_4_6.json', 'block_5_5.json', 'block_5_6.json', 'block_6_6.json']:
        rec = load(name)
        assert sum(rec['rejection_depth_counts']) == rec['primitive_cosets_checked']
        assert rec['kernel'] is None
        if name != 'audit_3_6.json':
            a, b = rec['state_counts']
            pairs = a * b if a != b else a * (a - 1) // 2
            assert pairs == rec['oriented_pairs']
            assert pairs == rec['primitive_cosets_checked'] + rec['shared_atom_pairs']
        else:
            assert 1482 * 262 == rec['primitive_cosets_checked'] + rec['shared_atom_pairs']
        radius_field = 'applicability_radius_squared_upper_bound' if name == 'audit_3_6.json' else 'radius_squared_upper_bound'
        assert rec[radius_field] == radius19[tuple(rec['split'])]
        higher.append({'path': name, 'split': rec['split'], 'reported_rejections': rec['primitive_cosets_checked']})
    ledger = load('coverage_p19.json')
    assert sum(x['primitive_instances'] for x in ledger['remaining_primitive_blocks']) == ledger['total_primitive_instances'] == 70285694
    assert primitive + sum(x['reported_rejections'] for x in higher) == ledger['total_primitive_instances']
    result = {'schema': 'T6_INDEPENDENT_STATIC_PAPER_CERTIFICATE_CHECK_V1', 'status': 'PASS',
              'source_commit_pinned_by_continuation278': '2f257c02d95b9cd630c23284bea2516a1be3f853',
              'p19': p19, 'p17': p17,
              'coverage_metadata': {'three_contiguous_intervals': records, 'higher_or_old_claim_records': higher,
                                    'total_reported_primitive_instances': 70285694, 'arithmetic_consistency': True,
                                    'producer_campaign_or_implementation_not_replayed': True},
              'scope': 'Static exact matrix algebra, congruences, GS, atom representatives, and record arithmetic only. No independent p19 rejection census or global T6 proof.',
              'author_checkers_imported_or_executed': False, 'native_claim_or_identity': False,
              'python': platform.python_version(), 'elapsed_seconds': time.monotonic() - start,
              'review_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT / 'INDEPENDENT_STATIC_CERTIFICATE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'elapsed_seconds': result['elapsed_seconds'], 'p19_min_D_floor': p19['minimum_D_floor'], 'p17_min_D_floor': p17['minimum_D_floor'], 'p19_reported_census_not_replayed': True, 'p17_q0_independently_proved': True}))


if __name__ == '__main__':
    main()
