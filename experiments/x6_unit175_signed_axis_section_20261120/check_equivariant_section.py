#!/usr/bin/env python3
"""Unit175: exact finite C12 signed-axis vs unsigned-axis equivariant section check.
Independent checker; does not import the project modules or assert physical rotation.
"""
from __future__ import annotations
import itertools
import json
import hashlib

N = 6

def verify(condition, label):
    if not condition:
        raise ArithmeticError("UNIT175_ALWAYS_ON_" + label)
# Total labels (axis, sign), sign +1 or -1. Base labels are 0..5.
total = tuple((i, sign) for i in range(N) for sign in (-1, 1))
base = tuple(range(N))

def A(v):
    i, s = v
    return (i + 1, s) if i < N - 1 else (0, -s)

def power(v, k):
    for _ in range(k):
        v = A(v)
    return v

def group_action(k):
    return {v: power(v, k) for v in total}

def base_action(k):
    return {i: (i + k) % N for i in base}

def subgroup(d):
    verify(12 % d == 0, "SUBGROUP_DIVISOR")
    return tuple(range(0, 12, d))

def section(bits):
    return {i: (i, bits[i]) for i in base}

equivariance_check_count = [0]
def is_equivariant(sec, H):
    valid = True
    for k in H:
        for i in base:
            equivariance_check_count[0] += 1
            if sec[base_action(k)[i]] != power(sec[i], k):
                valid = False
    return valid

def fixed_lift_product(H):
    unseen = set(base)
    product = 1
    per_orbit = []
    while unseen:
        b = min(unseen)
        orb = {base_action(k)[b] for k in H}
        unseen.difference_update(orb)
        stab = tuple(k for k in H if base_action(k)[b] == b)
        fixed = tuple(e for e in total if e[0] == b and all(power(e, k) == e for k in stab))
        per_orbit.append({'base_representative': b, 'orbit_size': len(orb),
                          'stabilizer_powers': list(stab), 'fixed_lifts': len(fixed)})
        product *= len(fixed)
    return product, per_orbit

# Check signed and unsigned actions are exact C12 representations.
for k in range(12):
    verify(len(set(group_action(k).values())) == 12, "TOTAL_PERMUTATION")
    verify(len(set(base_action(k).values())) == 6, "BASE_PERMUTATION")
    for e in total:
        verify(power(e, k)[0] == base_action(k)[e[0]], "PROJECTION_EQUIVARIANCE")
        verify(power(e, k + 12) == power(e, k), "PERIOD12")
        for ell in range(12):
            verify(power(power(e, k), ell) == power(e, (k + ell) % 12), "GROUP_COMPOSITION")
verify(all(power(e, 6) == (e[0], -e[1]) for e in total), "KERNEL_SIGN_FLIP")
verify(all(power(e, 12) == e for e in total), "IDENTITY12")

result = {'schema': 'X6_UNIT175_EQUIVARIANT_SECTION_EXACT_FINITE_V1',
          'model': 'C12 signed six-axis integer-label action A; no physical rotation asserted',
          'total_labels': 12, 'unoriented_labels': 6, 'tested_choice_maps': 2 ** 6,
          'subgroups': []}
expected = {1: 0, 2: 0, 3: 0, 4: 4, 6: 0, 12: 64}
for d in (1, 2, 3, 4, 6, 12):
    H = subgroup(d)
    selections = 0
    for bits in itertools.product((-1, 1), repeat=6):
        if is_equivariant(section(bits), H):
            selections += 1
    formula, detail = fixed_lift_product(H)
    verify(formula == selections == expected[d], f"STABILIZER_COUNT_D{d}")
    verify((6 in H) == (selections == 0), f"SHARP_SUBGROUP_BOUNDARY_D{d}")
    result['subgroups'].append({'generator_exponent_d': d, 'group_order': len(H),
                                'action_powers': list(H), 'enumerated_sections': selections,
                                'stabilizer_product': formula, 'orbit_certificates': detail})
result['equivariance_tests'] = equivariance_check_count[0]
verify(equivariance_check_count[0] == 6 * 64 * sum(12 // d for d in (1,2,3,4,6,12)), 'EXECUTED_COUNT')
result['violations'] = 0
serialized = json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(',',':'))
result['canonical_sha256'] = hashlib.sha256(serialized.encode()).hexdigest()
print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
