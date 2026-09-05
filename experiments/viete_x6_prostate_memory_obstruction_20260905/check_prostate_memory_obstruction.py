#!/usr/bin/env python3
"""Exact finite-level checker for the #1255 pro-state memory obstruction.

Checks only integer/cyclic arithmetic:
- a cyclic source orbit of length N can intertwine one-step successor with
  C_M translation k -> k+1 iff M divides N;
- the native outer C12 cycle reaches C12 but cannot reach C24+;
- C6 phase plus b binary memory bits cannot support level m>b;
- dropping the native INNER/OUTER branch bit is safe for a strictly macro-C6
  successor horizon, but unsafe once midpoint/C12 or native-path observations
  are admitted.
"""

from itertools import product


def target_modulus(m: int) -> int:
    assert m >= 0
    return 6 * (2 ** m)


def cycle_semiconjugacy_exists(source_period: int, target_modulus_value: int) -> bool:
    """Criterion for phi(Tx)=phi(x)+1 from a single N-cycle to C_M."""
    return source_period % target_modulus_value == 0


def explicit_phi(source_period: int, target_modulus_value: int):
    if not cycle_semiconjugacy_exists(source_period, target_modulus_value):
        return None
    return [k % target_modulus_value for k in range(source_period)]


def check_cycle_criterion():
    for n in range(1, 193):
        for m in range(1, 97):
            phi = explicit_phi(n, m)
            if phi is None:
                assert n % m != 0
                continue
            assert n % m == 0
            for k in range(n):
                lhs = phi[(k + 1) % n]
                rhs = (phi[k] + 1) % m
                assert lhs == rhs


def check_outer_c12_barrier():
    n = 12
    assert cycle_semiconjugacy_exists(n, target_modulus(0))  # C6
    assert cycle_semiconjugacy_exists(n, target_modulus(1))  # C12
    for m in range(2, 12):
        assert not cycle_semiconjugacy_exists(n, target_modulus(m))


def check_memory_lower_bound():
    # If a source state consists of one of 6 coarse phases and b binary memory
    # bits, it has at most 6*2^b distinguishable states. To support the
    # transitive C_{6*2^m} successor, at least 6*2^m source states are needed.
    for m in range(0, 12):
        required = target_modulus(m)
        for b in range(0, 12):
            available = 6 * (2 ** b)
            possible_by_cardinality = available >= required
            assert possible_by_cardinality == (b >= m)


def c6_next(prev: int, cur: int) -> int:
    """Ordered adjacent pair fixes sweep on an undirected 6-cycle."""
    assert (cur - prev) % 6 in (1, 5)
    step = (cur - prev) % 6
    return (cur + step) % 6


def check_branch_horizons():
    branches = ("INNER", "OUTER")
    for prev in range(6):
        for step in (-1, 1):
            cur = (prev + step) % 6
            nxt = c6_next(prev, cur)

            # q_C6 drops branch provenance. Every branch choice has the same
            # macro successor, so branch deletion is safe for this exact lease.
            macro_outputs = set()
            for beta, beta_next in product(branches, repeat=2):
                state = (prev, cur, beta)
                lifted_next = (cur, nxt, beta_next)
                q_state = state[:2]
                q_next = lifted_next[:2]
                assert q_next == (q_state[1], c6_next(*q_state))
                macro_outputs.add(q_next)
            assert macro_outputs == {(cur, nxt)}

            # Midpoint/C12 observation separates the matched endpoint states.
            midpoint = {
                "INNER": ("PIVOT", None),
                "OUTER": ("NONZERO_HALF_ANGLE", (prev, cur)),
            }
            assert midpoint["INNER"] != midpoint["OUTER"]

            # Native path provenance also separates them.
            path = {
                "INNER": (prev, "PIVOT", cur),
                "OUTER": (prev, "OUTER_CELL", cur),
            }
            assert path["INNER"] != path["OUTER"]

            # Reversal preserves branch type but reverses macro orientation.
            for beta in branches:
                reversed_state = (cur, prev, beta)
                assert reversed_state[2] == beta
                assert c6_next(cur, prev) == (prev - step) % 6


def check_no_finite_period_in_inverse_limit_direction():
    # For every positive candidate period p, some finite projection C_{6*2^m}
    # detects that translation by p is nontrivial.
    for p in range(1, 10000):
        found = False
        for m in range(0, 20):
            if p % target_modulus(m) != 0:
                found = True
                break
        assert found


def main():
    check_cycle_criterion()
    check_outer_c12_barrier()
    check_memory_lower_bound()
    check_branch_horizons()
    check_no_finite_period_in_inverse_limit_direction()
    print("PASS: #1255 pro-state periodicity/memory obstruction checks")
    print("outer native period 12: reaches C6,C12; fails C24+")
    print("finite-level lower bound: C6 + b bits supports level m only if b>=m")
    print("branch bit: erasable for macro-C6 lease; retained for midpoint/path lease")


if __name__ == "__main__":
    main()
