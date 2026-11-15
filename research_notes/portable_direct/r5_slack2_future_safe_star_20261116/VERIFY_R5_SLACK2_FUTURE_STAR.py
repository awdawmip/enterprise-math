"""R5: exact future-safe belief characterization and finite MILP optima.

Run: python VERIFY_R5_SLACK2_FUTURE_STAR.py 3 4 5 6
Requires Python >=3.10, NumPy and SciPy (HiGHS MILP). Integer model
and returned witness are exact; optimizer is a floating-point MILP solver.
"""
import json
import sys
from math import comb
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix, csc_matrix


def q(u, k):
    return sum(((u >> i) & 1) * ((u >> ((i + 1) % k)) & 1) for i in range(k))


def transition(B, i, b, raw_count):
    result = 0
    for u in range(raw_count):
        if (B >> u) & 1:
            result |= 1 << ((u & ~(1 << i)) | (b << i))
    return result


def all_future_safe_beliefs(k):
    raw_count = 1 << k
    result = []
    for center in range(raw_count):
        neighbors = [center] + [center ^ (1 << i)
                                for i in range(k) if (center >> i) & 1]
        for choice in range(1, 1 << len(neighbors)):
            B = 0
            union = 0
            for j, u in enumerate(neighbors):
                if (choice >> j) & 1:
                    B |= 1 << u
                    union |= u
            if union == center:
                result.append(B)
    expected = 2 * 3**k - (k + 2) * 2**(k - 1)
    assert len(result) == len(set(result)) == expected
    for B in result:
        members = [u for u in range(raw_count) if (B >> u) & 1]
        union = 0
        for u in members:
            union |= u
        assert all((union & ~u).bit_count() <= 1 for u in members)
        assert all(q(union, k) - q(u, k) <= 2 for u in members)
    return result


def solve(k):
    raw_count = 1 << k
    beliefs = all_future_safe_beliefs(k)
    variable_count = len(beliefs)
    constraints = []
    # Every raw state has an initial internal state.
    for u in range(raw_count):
        constraints.append(({j: 1 for j, B in enumerate(beliefs)
                             if (B >> u) & 1}, 1))
    # A selected state must have a selected successor containing its image.
    for j, B in enumerate(beliefs):
        for i in range(k):
            for b in (0, 1):
                image = transition(B, i, b, raw_count)
                successors = [l for l, C in enumerate(beliefs)
                              if (image & C) == image]
                assert successors
                row = {l: 1 for l in successors}
                row[j] = row.get(j, 0) - 1
                constraints.append(({l: x for l, x in row.items() if x}, 0))
    matrix = lil_matrix((len(constraints), variable_count), dtype=np.float64)
    lower = np.empty(len(constraints))
    for r, (coefficients, bound) in enumerate(constraints):
        lower[r] = bound
        for j, val in coefficients.items():
            matrix[r, j] = val
    result = milp(np.ones(variable_count),
                  integrality=np.ones(variable_count),
                  bounds=Bounds(np.zeros(variable_count), np.ones(variable_count)),
                  constraints=LinearConstraint(csc_matrix(matrix), lower, np.inf),
                  options={'mip_rel_gap': 0, 'time_limit': 120})
    assert result.status == 0 and result.x is not None, result.message
    selected = [B for B, flag in zip(beliefs, result.x) if flag > 0.5]
    # Witness checks are exact integer operations and independent of MILP tolerances.
    for u in range(raw_count):
        assert any((B >> u) & 1 for B in selected)
    for B in selected:
        for i in range(k):
            for b in (0, 1):
                image = transition(B, i, b, raw_count)
                assert any((image & C) == image for C in selected)
    assert len(selected) == 1 << (k - 1)
    assert abs(result.fun - len(selected)) < 1e-7
    assert abs(result.mip_dual_bound - len(selected)) < 1e-7
    assert result.mip_gap == 0
    return {
        'k': k, 'frozen_science_pin': '435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'slack': 2, 'control': 'all named Set_i(0/1)',
        'raw_masks': raw_count, 'future_safe_belief_count': variable_count,
        'integer_program_rows': len(constraints),
        'optimal_state_count': len(selected),
        'solver_status': result.status, 'solver_primal': result.fun,
        'solver_dual_bound': result.mip_dual_bound,
        'solver_mip_gap': result.mip_gap,
        'verified_beliefs_hex': [hex(B) for B in selected],
        'finite_inference': 'HiGHS MIP optimum, exact integer witness checks',
        'universal_inference': 'only the future-safe star characterization is proved for all k>=3',
        'independent_review': 'NOT_REVIEWED',
    }


def main():
    cases = [int(v) for v in sys.argv[1:]] or [3, 4, 5, 6]
    assert all(3 <= k <= 6 for k in cases)
    results = [solve(k) for k in cases]
    print(json.dumps({'status': 'PASS_R5_FUTURE_SAFE_STAR_MILP',
                      'cases': results}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
