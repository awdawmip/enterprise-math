"""Independent m=1/O(N^2) extension of frozen R5 scalar cost observer.

Exact integer arithmetic in Z[q]/(q^d-1); no numerical root evaluation.
The previously published m=1/O(N^3) theorem is an explicit dependency.
"""
import json
from collections import defaultdict
from math import lcm

PRICES = range(214, 315)
SETS = [
    set(range(214, 219)),
    {214, 216, 217, 218, 219, 220, 221},
    {215, 216, 217, 218, 219, 220, 221},
    set(range(223, 291)),
    set(range(296, 313)),
]


def candidate_orders(min_pole):
    return [d for d in range(1, 315)
            if 314 // d - 213 // d >= min_pole]


def cyclic_full(d):
    """31-mask inclusion/exclusion, dense cyclic coefficient vectors."""
    total = [0] * d
    for mask in range(1, 32):
        selected = [SETS[i] for i in range(5) if mask & (1 << i)]
        union = sorted(set.union(*selected))
        value = [1] + [0] * (d - 1)
        for p in union:
            # In Z[q]/(q^d-1), multiply by 1 - q^p.
            value = [value[k] - value[(k - p) % d] for k in range(d)]
        sign = 1 if len(selected) % 2 else -1
        total = [v + sign * w for v, w in zip(total, value)]
    return total


def cyclic_three_sparse(d):
    """Independent seven-mask sparse-dictionary calculation for d=23,25.

    The original masks containing S3 or S4 vanish at these roots.
    """
    assert all(any(p % d == 0 for p in s) for s in SETS[3:])
    assert all(all(p % d for p in s) for s in SETS[:3])
    total = defaultdict(int)
    for mask in range(1, 8):
        selected = [SETS[i] for i in range(3) if mask & (1 << i)]
        union = set.union(*selected)
        value = {0: 1}
        for p in union:
            step = defaultdict(int)
            for exponent, coef in value.items():
                step[exponent] += coef
                step[(exponent + p) % d] -= coef
            value = {k: v for k, v in step.items() if v}
        sign = 1 if len(selected) % 2 else -1
        for k, v in value.items():
            total[k] += sign * v
    return [total[k] for k in range(d)]


def vanishes_at_primitive_root(d, vector):
    if d == 23:  # Phi_23=1+q+...+q^22
        return len(set(vector)) == 1
    if d == 25:  # Phi_25=1+q^5+q^10+q^15+q^20
        return all(len({vector[r + 5 * j] for j in range(5)}) == 1
                   for r in range(5))
    raise ValueError(d)


def main():
    orders4 = candidate_orders(4)
    orders5 = candidate_orders(5)
    assert orders4 == list(range(1, 29)) + [31]
    assert orders5 == list(range(1, 21)) + [22, 24]
    assert lcm(*orders5) == 232792560

    # Every failure event contains a multiple of 27 and of 31.
    witnesses = {
        d: [min(p for p in s if p % d == 0) for s in SETS]
        for d in (27, 31)
    }
    assert witnesses == {27: [216, 216, 216, 243, 297],
                         31: [217, 217, 217, 248, 310]}
    assert all(v == 0 for v in cyclic_full(27))
    assert all(v == 0 for v in cyclic_full(31))

    cyclotomic = {}
    for d in (23, 25):
        dense = cyclic_full(d)
        sparse = cyclic_three_sparse(d)
        assert dense == sparse
        assert not vanishes_at_primitive_root(d, dense)
        cyclotomic[str(d)] = {
            'vector_mod_qd_minus_1': dense,
            'first_coordinate': dense[0],
            'witness_coordinate': (1 if d == 23 else 5),
            'witness_value': dense[1] if d == 23 else dense[5],
            'difference': dense[0] - (dense[1] if d == 23 else dense[5]),
            'independent_seven_mask_agreement': True,
            'primitive_root_nonzero': True,
        }
    assert cyclotomic['23']['difference'] == -5
    assert cyclotomic['25']['difference'] == 7
    L2 = lcm(*(d for d in orders4 if d not in (27, 31)))
    assert L2 == 26771144400
    assert L2 // lcm(*orders5) == 115
    return {
        'schema': 'R5_M1_O2_EXACT_PERIOD_CERTIFICATE_V1',
        'scientific_scope': 'Frozen scalar observer, m=1; counting-cost quasipolynomial O(N^2)',
        'previous_m1_O3_period_dependency': 232792560,
        'candidate_root_orders_k_ge_4': orders4,
        'candidate_root_orders_k_ge_5': orders5,
        'globally_vanishing_order_witnesses_27_31_by_event': witnesses,
        'new_primitive_root_certificates': cyclotomic,
        'universal_upper_bound_m_ge_1_O2': L2,
        'm1_exact_period_O2_conditional_on_previous_O3_theorem': L2,
        'status': 'EXACT_INTEGER_CHECKED_NOT_INDEPENDENTLY_REVIEWED',
    }


if __name__ == '__main__':
    result = main()
    with open('CERTIFICATE.json', 'w', encoding='utf-8') as output:
        json.dump(result, output, ensure_ascii=False, indent=2)
        output.write('\n')
    print('PASS', result['universal_upper_bound_m_ge_1_O2'],
          'm=1 exact period conditional on prior O3 theorem')
