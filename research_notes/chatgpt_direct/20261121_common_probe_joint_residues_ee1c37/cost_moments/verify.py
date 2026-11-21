"""Exact incremental verification of five low-cost moment families.

The prior 49,500-class centered-moment and 24,000-class cost-747 checks are
inherited rather than rerun. This program checks every one of the 41,000 new
classes with the original finite-menu observer, compares the reconstructed
orbits with the complete selected bank, and scans the complete census seeds
for the stated low-cost spectra. It then verifies the abstract tail-cost
formulae using finite sets over F_5. No disjoint-cover optimum is asserted.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import argparse
import importlib.util
import json
import struct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = list(product(range(5), repeat=3))
PAIRS = ((0, 1), (0, 2), (1, 2))
ZERO = (0, 0, 0)
ALL = frozenset(P)
D = frozenset(tuple(v if i == j else 0 for i in range(3))
              for j in range(3) for v in (1, 4))
F = frozenset(q for q in P if sorted(min(a, 5-a) for a in q) == [0, 2, 2])
E = F | frozenset(q for q in P if sorted(min(a, 5-a) for a in q) == [0, 1, 2])
G = frozenset(q for q in P if sorted(min(a, 5-a) for a in q) == [0, 1, 1])
H = frozenset(product((1, 4), repeat=3))
Z = frozenset(q for q in P if 0 in q)
W = frozenset(q for q in P if any(v in (0, 1, 4) for v in q))
K = frozenset(product((2, 3), repeat=3))
TARGETS = {(9, 564): (D, 12000, 2000),
           (9, 569): (G, 12000, 1000),
           (9, 576): (H, 2000, 250),
           (11, 960): (frozenset([ZERO]), 3000, 3000)}


def points(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask -= bit


def orbit(ids):
    oriented = {tuple(sorted(25*(P[i][perm[0]]*sign[0]*scale % 5)
                             + 5*(P[i][perm[1]]*sign[1]*scale % 5)
                             + P[i][perm[2]]*sign[2]*scale % 5 for i in ids))
                for perm in permutations(range(3))
                for sign in product((1, -1), repeat=3) for scale in (1, 2)}
    return {sum(1 << (25*((P[i][0]+a) % 5)+5*((P[i][1]+b) % 5)
                      +(P[i][2]+c) % 5) for i in row)
            for row in oriented for a, b, c in P}


def raw_moments(mask):
    ps = [P[i] for i in points(mask)]
    mu = tuple(sum(p[i] for p in ps) % 5 for i in range(3))
    q = tuple(sum(p[i]*p[j] for p in ps) % 5 for i, j in PAIRS)
    return mu, q


def centered_moment(mask):
    mu, q = raw_moments(mask)
    inverse = pow(mask.bit_count() % 5, -1, 5)
    return mu, tuple((v-inverse*mu[i]*mu[j]) % 5 for v, (i, j) in zip(q, PAIRS))


def sumset(a, b):
    return frozenset(tuple((x+y) % 5 for x, y in zip(u, v)) for u in a for v in b)


def spectrum(seeds):
    expected = json.loads((HERE/'low_cost_spectrum.json').read_text())
    raw = seeds.read_bytes()
    assert len(raw) == expected['full_seed_bytes']
    assert sha256(raw).hexdigest() == expected['full_seed_sha256']
    caps = {int(n): c for n, c in expected['scope_caps'].items()}
    found = {n: set() for n in caps}
    counts = Counter()
    rows = 0
    for line in raw.splitlines():
        n, c = map(int, line.split(None, 2)[:2])
        rows += 1
        if n in caps and c <= caps[n]:
            found[n].add(c)
            counts[n, c] += 1
    assert rows == expected['full_seed_rows'] == 1495322
    assert {str(n): sorted(v) for n, v in found.items()} == expected['complete_low_costs']
    assert all(expected['native_census_caps'][str(n)] >= c for n, c in caps.items())
    return {'sha256': expected['full_seed_sha256'], 'bytes': len(raw), 'rows': rows,
            'complete_costs': {str(n): sorted(v) for n, v in found.items()},
            'raw_seed_rows_per_low_type': [dict(size=n, cost=c, rows=k)
                                           for (n, c), k in sorted(counts.items())]}


def verify_families(previous, bank):
    spec = importlib.util.spec_from_file_location('cost_moments_native',
                          previous/'fractional/proof/verify.py')
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    bad, pair = native.observation_tables()
    source = json.loads((HERE/'extra_representatives.json').read_text())
    entries = source['families'] + [json.loads((HERE/'ten752_representative.json').read_text())]
    expected_types = set(TARGETS) | {(10, 752)}
    raw = bank.read_bytes()
    assert sha256(raw).hexdigest() == source['source_bank_sha256']
    banks = {kind: set() for kind in expected_types}
    bank_rows = 0
    for lo, hi, cost, tag in struct.iter_unpack('<QQII', raw):
        bank_rows += 1
        kind = tag % 256, cost
        if kind in banks:
            banks[kind].add(lo+(hi << 64))
    assert bank_rows == 426500
    results = []
    total_native = 0
    for entry in entries:
        kind = entry['size'], entry['cost']
        family = set()
        orbit_sizes = []
        for rep, expected_size in zip(entry['representatives'], entry['orbit_counts'], strict=True):
            current = orbit(rep)
            assert len(current) == expected_size and not current & family
            family |= current
            orbit_sizes.append(len(current))
        assert family == banks[kind] and len(family) == entry['count']
        signatures = Counter()
        combined = Counter()
        for mask in family:
            assert native.native_class(mask, bad, pair) == kind
            total_native += 1
            if kind[0] == 10:
                mu, q = raw_moments(mask)
                active = [i for i, a in enumerate(mu) if a]
                assert len(active) == 1 and q[2-active[0]] == 0
                signatures[mu, q] += 1
            else:
                mu, gamma = centered_moment(mask)
                signatures[gamma] += 1
                combined[gamma, mu] += 1
        if kind[0] == 10:
            target = {(tuple(a if i == axis else 0 for i in range(3)), q)
                      for axis in range(3) for a in range(1, 5)
                      for q in P if q[2-axis] == 0}
            assert set(signatures) == target and len(target) == 300
            assert set(signatures.values()) == {40} and len(family) == 12000
            target_name = 'T'; multiplicity = 40; moment_kind = 'raw_joint_mu_Q'
        else:
            target, count, multiplicity = TARGETS[kind]
            assert set(signatures) == target and len(family) == count
            assert set(signatures.values()) == {multiplicity}
            assert set(combined) == set(product(target, P))
            assert set(combined.values()) == {multiplicity//125}
            target_name = {(9, 564): 'D', (9, 569): 'G', (9, 576): 'H', (11, 960): '{0}'}[kind]
            moment_kind = 'centered_Gamma'
        canonical = b''.join(m.to_bytes(16, 'little') for m in sorted(family))
        row = {'type': list(kind), 'classes': len(family), 'orbit_sizes': orbit_sizes,
               'native_menu_checks': len(family), 'full_bank_set_equality': True,
               'moment_kind': moment_kind, 'support_name': target_name,
               'support_values': len(target), 'classes_per_signature': multiplicity,
               'canonical_class_sha256': sha256(canonical).hexdigest()}
        if kind[0] != 10:
            row['means_per_centered_value'] = 125
            row['classes_per_centered_value_and_mean'] = multiplicity//125
        results.append(row)
        print(json.dumps(row), flush=True)
    assert total_native == 41000 and {tuple(r['type']) for r in results} == expected_types
    return {'source_bank_sha256': source['source_bank_sha256'], 'bank_rows': bank_rows,
            'families': results, 'new_native_classes_checked': total_native}


def verify_tail_costs():
    """Exact finite-support minima, with whole cheap spectra as completeness input."""
    powers = [frozenset([ZERO])]
    for _ in range(7):
        powers.append(sumset(powers[-1], D))
    assert list(map(len, powers)) == [1, 6, 19, 44, 85, 117, 125, 125]
    assert len(Z) == 61 and len(W) == 117 and len(K) == 8
    assert sumset(D, Z) == W and ALL-W == K
    assert sumset(E, Z) == ALL
    assert sumset(powers[2], Z) == ALL
    assert sumset(F, D) <= W
    assert K <= sumset(F, Z)
    # Type 752 has exactly the same raw signature support as cheaper 747;
    # type 768 has the same signature support as cheaper 744. They cannot
    # lower an abstract signature minimum. This is not geometric dominance.
    exceptional = {9: [(557, E), (564, D), (569, G), (576, H)],
                   11: [(936, D), (944, F), (960, frozenset([ZERO]))]}
    rows = []
    for n in (9, 11):
        base_exceptional = exceptional[n][0][0]
        for m in range(6):
            base = base_exceptional+744*m
            # Only zero/one T-type ten classes are needed to attain every
            # finite minimum reported here. Cases with >=2 have extra cost
            # >=6 and cannot improve the <=3 minima for m>=2. For m=1 such
            # cases do not exist. For m=0 no ten class is present.
            best = {}
            for cost, support in exceptional[n]:
                for q in sumset(support, powers[m]):
                    best[q] = min(best.get(q, 10**9), cost+744*m)
                if m:
                    for q in sumset(sumset(support, Z), powers[m-1]):
                        best[q] = min(best.get(q, 10**9), cost+744*m+3)
            if m:
                assert set(best) == ALL
                if n == 9:
                    base_support = sumset(E, powers[m])
                    expected = {q: base if q in base_support else base+3 for q in P}
                elif m >= 2:
                    expected = {q: base if q in powers[m+1] else base+3 for q in P}
                else:
                    expected = {q: base if q in powers[2] else base+3 if q in W else base+11 for q in P}
                assert best == expected
                assert max(best.values())-base <= (11 if n == 11 and m == 1 else 3)
            else:
                ceiling = 576 if n == 9 else 960
                # For signatures absent through the complete ceiling, the
                # next unknown integer cost is at least ceiling+1.
                best.update({q: ceiling+1 for q in ALL-set(best)})
            histogram = Counter(cost-base for cost in best.values())
            rows.append({'exceptional_size': n, 'ten_classes': m, 'baseline': base,
                         'minimum_cost_offset_counts': [{'offset': c, 'gamma_values': count}
                                                       for c, count in sorted(histogram.items())],
                         'ceilings_for_unknown_single_class_costs_only': m == 0})
    assert [r['minimum_cost_offset_counts'] for r in rows if r['exceptional_size'] == 9 and r['ten_classes'] == 2] == [
        [{'offset': 0, 'gamma_values': 124}, {'offset': 3, 'gamma_values': 1}]]
    assert [r['minimum_cost_offset_counts'] for r in rows if r['exceptional_size'] == 11 and r['ten_classes'] == 1] == [
        [{'offset': 0, 'gamma_values': 19}, {'offset': 3, 'gamma_values': 98}, {'offset': 11, 'gamma_values': 8}]]
    return {'D_walk_support_sizes': list(map(len, powers)), 'rows': rows,
            'two_ten_one_nine_gamma_zero_lower_bound': 2048,
            'one_ten_one_eleven_gamma_pm2_cube_lower_bound': 1691,
            'scope': 'Universal necessary cost bounds for exactly one size-9 or size-11 class and m size-10 classes; sharp in the abstract moment relaxation for m>=1. No actual disjoint cover or attainable integer optimum is claimed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, default=ROOT/'delivery')
    parser.add_argument('--bank', type=Path, default=ROOT/'r10/lower/work/bank')
    parser.add_argument('--seeds', type=Path, default=ROOT/'r10/lower/work/seeds')
    parser.add_argument('--output', type=Path, default=HERE/'verification.json')
    args = parser.parse_args()
    spectrum_result = spectrum(args.seeds)
    print(json.dumps({'complete_low_cost_spectrum': spectrum_result}), flush=True)
    result = {'schema': 'LOW_COST_MOMENT_APPENDIX_V1',
              'complete_low_cost_spectrum': spectrum_result,
              'new_families': verify_families(args.previous, args.bank),
              'tail_cost_bounds': verify_tail_costs(),
              'review_status': 'NOT_REVIEWED',
              'scope': 'Exact finite original-observer catalogue and necessary tail-cost bounds. Native legality/cost and the completeness of the supplied original enumeration are inherited reductions; this appendix does not change the global twelve-label lower bound.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'all_verified': True, 'native_classes_checked': 41000,
                      'complete_seed_rows_scanned': 1495322,
                      'tail_table_rows': len(result['tail_cost_bounds']['rows'])}), flush=True)


if __name__ == '__main__':
    main()
