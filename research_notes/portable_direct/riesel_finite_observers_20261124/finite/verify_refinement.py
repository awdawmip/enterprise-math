"""Complete finite checks of members of the proved refinement family C_k.

The all-k and arbitrary-modulus statements are written proofs, not conclusions
from these small checks. Each checked example uses its complete period.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from math import gcd, lcm
from pathlib import Path


def covering_rows(k):
    assert k >= 2
    a = 2**k-1
    half = 3*2**(k-1)
    full = 3*2**k
    rows = [(2**j, 2**(j-1)-1) for j in range(1, k+1)]
    rows.append((3, 0))
    rows.append((half, half-1 if k % 2 == 0 else a))
    rows.append((full, 2**(k+1)-1 if k % 2 == 0 else full-1))
    return rows


def private_witnesses(k):
    assert k >= 2
    a = 2**k-1
    full = 3*2**k
    dyadic = [(2**(j-1)-1 if j % 2 == 0 else 3*2**(j-1)-1)
              for j in range(1, k+1)]
    tail = ([a, full-1, 2**(k+1)-1] if k % 2 == 0
            else [2**(k+1)-1, a, full-1])
    return dyadic+tail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('refinement_certificate.json'))
    args = parser.parse_args()
    records = []
    for k in range(2, 7):
        rows = covering_rows(k)
        period = lcm(*(m for m, _ in rows))
        assert len(rows) == k+3 and len({m for m, _ in rows}) == len(rows)
        assert period == max(m for m, _ in rows) == 3*2**k
        assert gcd(period, 35) == 1
        hits = [[i for i, (m, b) in enumerate(rows) if v % m == b]
                for v in range(period)]
        assert all(hits)
        private = [[v for v, indices in enumerate(hits) if indices == [i]]
                   for i in range(len(rows))]
        assert all(private)
        witnesses = private_witnesses(k)
        assert len(witnesses) == len(rows)
        assert all(0 <= v < period and v in cells
                   for v, cells in zip(witnesses, private))
        leftover = [v for v in range(period)
                    if not any(v % m == b for m, b in rows[:k])]
        assert leftover == [2**k-1+2**k*t for t in range(3)]
        tail_phases = []
        for m, b in rows[k:]:
            phases = [t for t, v in enumerate(leftover) if v % m == b]
            assert len(phases) == 1
            tail_phases.append(phases[0])
        assert tail_phases == ([0, 2, 1] if k % 2 == 0 else [1, 0, 2])
        records.append({
            'k': k,
            'rows': [{'modulus': m, 'phase': b} for m, b in rows],
            'full_period': period, 'cost_increment': k+2,
            'largest_period_factor': period,
            'private_residue_sets': private,
            'selected_private_residues': witnesses,
            'covering_multiplicity_counts': dict(sorted(Counter(map(len, hits)).items())),
            'dyadic_complement': leftover,
            'three_complementary_t_phases': tail_phases,
            'relative_child_order_multipliers': [2*m for m, _ in rows],
        })
    assert set(covering_rows(2)) == {(2, 0), (3, 0), (4, 1), (6, 5), (12, 7)}
    assert set(covering_rows(3)) == {(2, 0), (3, 0), (4, 1), (8, 3), (12, 7), (24, 23)}
    assert records[1]['covering_multiplicity_counts'] == {1: 16, 2: 8}
    result = {
        'schema': 'riesel-uniform-refinement-family-input-v2',
        'status': 'AUTHOR_EXACT_FINITE_CHECK; NOT_INDEPENDENT_REVIEW',
        'checked_k_values': list(range(2, 7)),
        'patterns': records,
        'all_k_proof': 'Section 2 of proof.md: dyadic partition and three complementary t classes; every row has an explicit private witness.',
        'cost_increment_formula': 'k+2 for every integer k>=2; therefore every increment>=4.',
        'observer_threshold_formula': 'k_N=min{k>=2:216*2^k>B_N}; all costs>=k_N+12 in one residue fiber.',
        'necessary_budget_order_bound': 'B_N>=(27/512)*2^b for any modulus deciding delta_P<=b throughout R1, b>=14.',
        'scope': 'Complete finite covering periods for the displayed k values; universal assertions use the written proof, not extrapolation.',
        'inherited_primitive_prime_input': 'For every requested base-2 order>6, a prime of that exact order exists; same dependency as v7 spectrum/proof.md.',
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'checked_k': list(range(2, 7)),
                      'full_periods': [r['full_period'] for r in records],
                      'cost_increments': [r['cost_increment'] for r in records],
                      'output': str(args.output)}))


if __name__ == '__main__':
    main()
