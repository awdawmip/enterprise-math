#!/usr/bin/env python3
"""Exact error tolerance for the frozen R5 three-count decoder.

Run alongside VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py:
  python VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py > tomography.json
  python VERIFY_R5_THREE_READOUT_ROBUSTNESS.py tomography.json > robustness.json
Standard-library Python only; every pair of 256 states tested with exact integers
and rational comparisons. Author-side finite certificate, not independent review.
"""
import hashlib
import json
import sys
from fractions import Fraction

BITS = (3, 8, 9, 10, 15, 17, 25, 27)
BUDGETS = (214, 223, 294)
EXPECTED_INPUT_SHA256 = '261b3945e9efdcf1a3f4be215a42b19bccac3fee9e06e2ef3bd3eba4dc279f41'


def count(row, active):
    total = 0
    for label, value in row['a_mask'].items():
        prerequisites = set(map(int, label.split(','))) if label else set()
        if prerequisites <= active:
            total += int(value)
    return total


def main(path):
    with open(path, 'rb') as f:
        payload = f.read()
    source_hash = hashlib.sha256(payload).hexdigest()
    data = json.loads(payload)
    assert data['scientific_input_commit'] == '435e77af0d180eac32bd1f9c4c464bc4010b7551'
    assert data['status'] == 'PASS_EXACT_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY'
    rows = {row['K']: row for row in data['rows_214_to_315']}
    signatures = []
    for state in range(256):
        active = {bit for j, bit in enumerate(BITS) if state & (1 << j)}
        signatures.append(tuple(count(rows[k], active) for k in BUDGETS))
    assert len(set(signatures)) == 256

    smallest_distance = None
    smallest_relative = None
    distance_pairs = []
    relative_pairs = []
    for a in range(256):
        for b in range(a + 1, 256):
            u, v = signatures[a], signatures[b]
            distance = max(abs(x - y) for x, y in zip(u, v))
            critical = max(Fraction(abs(x - y), x + y) for x, y in zip(u, v))
            if smallest_distance is None or distance < smallest_distance:
                smallest_distance, distance_pairs = distance, [[a, b]]
            elif distance == smallest_distance:
                distance_pairs.append([a, b])
            if smallest_relative is None or critical < smallest_relative:
                smallest_relative, relative_pairs = critical, [[a, b]]
            elif critical == smallest_relative:
                relative_pairs.append([a, b])

    projected = {}
    for omitted in range(3):
        projection = {tuple(x[j] for j in range(3) if j != omitted) for x in signatures}
        projected[str(BUDGETS[omitted])] = len(projection)

    assert smallest_distance == 76289178155959966960189440
    assert smallest_relative == Fraction(4022840, 4361603107999)
    assert len(distance_pairs) == len(relative_pairs) == 64
    assert projected == {'214': 16, '223': 128, '294': 64}
    print(json.dumps({
        'status': 'PASS_EXACT_R5_THREE_READOUT_ROBUSTNESS',
        'scientific_pin': data['scientific_input_commit'],
        'input_json_sha256': source_hash,
        'previous_known_stdout_sha256_match': source_hash == EXPECTED_INPUT_SHA256,
        'budgets': BUDGETS,
        'bits': BITS,
        'states': 256,
        'unordered_pairs': 256 * 255 // 2,
        'min_L_infty_distance': str(smallest_distance),
        'maximum_uniform_integer_absolute_error': str((smallest_distance - 1) // 2),
        'absolute_critical_pair_count': len(distance_pairs),
        'absolute_critical_pair_example': distance_pairs[0],
        'relative_epsilon_critical_numerator': str(smallest_relative.numerator),
        'relative_epsilon_critical_denominator': str(smallest_relative.denominator),
        'relative_critical_pair_count': len(relative_pairs),
        'relative_critical_pair_example': relative_pairs[0],
        'distinct_signatures_after_one_readout_erasure': projected,
        'independent_math_review': 'NOT_REVIEWED',
    }, sort_keys=True, indent=2))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python VERIFY_R5_THREE_READOUT_ROBUSTNESS.py tomography.json')
    main(sys.argv[1])
