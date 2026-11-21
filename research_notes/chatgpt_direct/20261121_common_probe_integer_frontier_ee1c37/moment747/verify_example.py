"""Verify the 20-point marginal counterexample without rerunning all native costs."""
from pathlib import Path
import argparse
import importlib.util
import json
from verify import P, points, orbit, raw_moments, ZERO, predicted_two

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, default=ROOT/'delivery')
    parser.add_argument('--output', type=Path, default=HERE/'example_verification.json')
    args = parser.parse_args()
    example = json.loads((HERE/'counterexample.json').read_text())
    ids = example['points']; mask = sum(1 << p for p in ids)
    assert len(ids) == len(set(ids)) == 20 and mask == int(example['mask'])
    mu, q = raw_moments(mask)
    assert mu == ZERO and q == (3, 4, 2) and q not in predicted_two()[ZERO]
    hist = lambda rows: [[sum(P[p][j] == a for p in rows) for a in range(5)] for j in range(3)]
    assert hist(ids) == [[4]*5 for _ in range(3)]
    displayed = [sum(1 << p for p in part) for part in example['marginal_cover_classes']]
    assert len(displayed) == 2 and all(m & mask == m for m in displayed)
    assert hist(sum(example['marginal_cover_classes'], [])) == hist(ids)
    assert sorted(points(displayed[0] & displayed[1])) == example['overlap'] == [18, 21]
    assert sorted(points(mask & ~(displayed[0] | displayed[1]))) == example['inserted_trade'] == [16, 23]
    spec = importlib.util.spec_from_file_location('example_native', args.previous/'fractional/proof/verify.py')
    native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
    bad, pair = native.observation_tables()
    assert all(native.native_class(m, bad, pair) == (10, 747) for m in displayed)
    source = json.loads((HERE/'class_representatives.json').read_text())
    family = set()
    for row in source['representatives']:
        current = orbit(row['points'])
        assert len(current) == row['orbit_size'] and not family & current
        family |= current
    assert len(family) == 24000
    from hashlib import sha256
    assert sha256(b''.join(m.to_bytes(16, 'little') for m in sorted(family))).hexdigest() == source['canonical_class_sha256']
    candidates = {m for m in family if m & mask == m}
    assert candidates == set(displayed) and len(candidates) == example['available_type747_classes'] == 2
    assert not any(mask ^ m in candidates for m in candidates)
    covered = 0
    for m in candidates:
        covered |= m
    result = {'schema': 'TWENTY_POINT_TWO747_EXAMPLE_VERIFICATION_V1',
              'points': 20, 'mu': mu, 'q': q, 'marginal_counts': hist(ids),
              'native_displayed_classes_checked': 2, 'complete_family_reconstructed': 24000,
              'available_classes': 2, 'candidate_type_capacity_passes': True,
              'displayed_candidate_marginals_add_to_target': True,
              'joint_moment_excludes_disjoint_cover': True,
              'direct_complement_check_finds_cover': False,
              'uncovered_by_any_candidate': sorted(points(mask & ~covered)),
              'scope': 'This separates raw joint moments from coordinate marginals plus type capacity. The basic candidate-union test also rejects it; no stronger LP separation or search-speed improvement is asserted.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
