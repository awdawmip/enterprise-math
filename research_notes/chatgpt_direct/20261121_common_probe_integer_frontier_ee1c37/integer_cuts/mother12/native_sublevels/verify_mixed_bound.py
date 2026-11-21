"""Bind the proper-size8..12 marginal cost guard to complete native inputs.

For n=8,9,10 check all native census seeds through the finite price cutoff.
For proper n=11,12 check the complete origin-anchored bank through its cutoff.
Every checked row is validated again with the original native menu, including
properness for the two larger sizes. Above the cutoffs, delta<=3(n-2) proves
the inequality analytically. Translation/signed/common-scale/axis actions
preserve delta and uniform cost, so normalized complete input is sufficient.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import argparse
import importlib.util
import json
import struct

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OFFSETS = {8: 419, 9: 557, 10: 744, 11: 993, 12: 1226}
CUTOFFS = {n: a+9*(n-2) for n, a in OFFSETS.items()}
SEED_SHA = 'c42e0b14760595a242864c53bb4946182b02a347a273c642e8bc03f4edae315d'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, default=ROOT/'delivery')
    parser.add_argument('--seeds', type=Path, default=ROOT/'r10/lower/work/seeds')
    parser.add_argument('--parents', type=Path, default=ROOT/'r10/bias/work/parent')
    parser.add_argument('--proper11-bank', type=Path, default=ROOT/'r10/bias/work/B11')
    parser.add_argument('--proper12-bank', type=Path, default=ROOT/'r10/bias/work/B12')
    parser.add_argument('--output', type=Path, default=HERE/'mixed_bound_verification.json')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('mixed_bound_native', args.previous/'fractional/proof/verify.py')
    native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
    bad, pairs = native.observation_tables()
    coords = [(i//25, i//5 % 5, i % 5) for i in range(125)]
    mothers = [int(line.split()[0])+(int(line.split()[1]) << 64) for line in args.parents.read_text().splitlines()[:250]]
    assert len(set(mothers)) == 250
    counts = Counter(); min_slack = {n: 10**9 for n in OFFSETS}; seen = {n: set() for n in OFFSETS}
    maximum_delta = Counter()
    def check(n, price, ids):
        mask = sum(1 << i for i in ids)
        assert len(ids) == len(set(ids)) == n
        assert native.native_class(mask, bad, pairs) == (n, price)
        if n >= 11:
            assert not any(mask & ~mother == 0 for mother in mothers)
        h = [[0]*5 for _ in range(3)]
        for p in ids:
            for j, a in enumerate(coords[p]):
                h[j][a] += 1
        delta = sum(max(value-2, 0) for row in h for value in row)
        assert delta <= 3*(n-2)
        slack = price-OFFSETS[n]-3*delta
        assert slack >= 0
        counts[n] += 1; seen[n].add(mask); min_slack[n] = min(min_slack[n], slack)
        maximum_delta[n] = max(maximum_delta[n], delta)
    raw = args.seeds.read_bytes()
    assert len(raw) == 46531165 and sha256(raw).hexdigest() == SEED_SHA
    total_rows = 0
    for line in raw.splitlines():
        size, cost, rest = line.split(None, 2)
        n, price = int(size), int(cost); total_rows += 1
        if n in (8, 9, 10) and price <= CUTOFFS[n]:
            check(n, price, list(map(int, rest.split())))
    assert total_rows == 1495322
    assert {n: counts[n] for n in (8, 9, 10)} == {8: 24867, 9: 14344, 10: 5327}
    banks = []
    for n, path, expected in ((11, args.proper11_bank, 18920), (12, args.proper12_bank, 540)):
        data = path.read_bytes(); assert len(data) == expected*24
        prices = Counter()
        for lo, hi, price in struct.iter_unpack('<QQQ', data):
            mask = lo+(hi << 64); assert mask & 1
            prices[price] += 1
            if price <= CUTOFFS[n]:
                check(n, price, [i for i in range(125) if mask >> i & 1])
        banks.append({'size': n, 'rows': expected, 'sha256': sha256(data).hexdigest(),
                      'cost_counts': sorted(prices.items())})
    assert counts[11] == 5852 and counts[12] == 288
    assert all(min_slack[n] == 0 for n in OFFSETS)
    # The finite checks include the cutoff, so every omitted higher integer
    # price has a strict >=1 safety margin even under the crude delta bound.
    assert all(CUTOFFS[n]+1-OFFSETS[n]-9*(n-2) == 1 for n in OFFSETS)
    result = {'schema': 'PROPER_EIGHT_TO_TWELVE_MARGINAL_COST_BOUND_V1',
              'inequality': 'c(C)>=a_size+3*sum_axis,value max(h_C-2,0)',
              'offsets': OFFSETS, 'finite_cutoffs': CUTOFFS,
              'finite_native_rows_checked': dict(counts),
              'distinct_native_masks_checked': {n: len(v) for n, v in seen.items()},
              'minimum_integer_slack': min_slack, 'maximum_delta_observed': dict(maximum_delta),
              'complete_seed_sha256': SEED_SHA, 'complete_seed_rows': total_rows,
              'proper_anchored_banks': banks,
              'high_cost_proof': 'For any n>=2 point set, each coordinate has sum max(h-2,0)<=n-2; thus delta<=3(n-2). If c>finite_cutoff=a_n+9(n-2), then c-a_n-3delta>=1.',
              'normalization_proof': 'delta and uniform native cost are invariant under translations, signed axis permutations and common multiplication; these are the normalization actions of the complete source enumerations.',
              'guard_consequence': 'For remaining proper classes of sizes8..12, actual union U contains all obliged outside pointsF. Therefore remaining cost >=sum a_size+3*sum max(h_F-2*kLeft,0).',
              'review_status': 'NOT_REVIEWED',
              'scope': 'Exact cost-observer inequality and a safe native-search guard; no whole-domain exclusion is inferred from the bound alone.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'native_rows_checked': dict(counts), 'total': sum(counts.values()), 'minimum_slacks': min_slack, 'all_verified': True}))


if __name__ == '__main__':
    main()
