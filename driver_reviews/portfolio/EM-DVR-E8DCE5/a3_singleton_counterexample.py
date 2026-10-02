#!/usr/bin/env python3
"""Minimal alphabet-quantifier probe for the A3 scale-coherence return.

Source inspected: enterprise-math PR1491 head
9c482061b4fc64b3ef936d90a9e21590d52f16f8,
research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/result.md,
lines 20 and 98-102. The text permits a finite alphabet A and states universal
labelled-state equality iff K=id without excluding |A|=1.

This tests only that quantifier. It does not reject the carrier/operator
identity K=L U^-1, the rigid-state statement, or the frozen marker regression.
It uses standard Python only, performs no full checker replay, and writes no files.
"""

from itertools import product
import json


def main() -> None:
    # Minimal scale/depth: n=d=1. On B1 the upper scale-2 depth-1 action
    # affects only S2 and hence restricts to U=id; the lower action is R_(23).
    ball = {x for x in product(range(-1, 2), repeat=4) if sum(x) == 0}
    permutation = (0, 2, 1, 3)

    def lower_action(x: tuple[int, ...]) -> tuple[int, ...]:
        result = [0] * 4
        for index, value in enumerate(x):
            result[permutation[index]] = -value  # sign((23)) = -1
        return tuple(result)

    upper = {x: x for x in ball}
    lower = {x: lower_action(x) for x in ball}
    assert set(lower.values()) == ball
    point = (1, -1, 0, 0)
    assert lower[point] == (-1, 0, 1, 0) != point
    assert upper != lower  # Since U=id, the nonidentity K is L itself.

    # A={0}: this is the sole element of X1=A^B1, so agreement here proves
    # agreement for every labelled state in this explicitly chosen domain.
    state = {x: 0 for x in ball}

    def push_forward(mapping, labelled_state):
        return {mapping[x]: label for x, label in labelled_state.items()}

    assert push_forward(upper, state) == push_forward(lower, state) == state
    assert len(set(state.values())) == 1
    print(json.dumps({
        "probe": "singleton_alphabet_quantifier",
        "n": 1,
        "d": 1,
        "carrier_size": len(ball),
        "alphabet_size": 1,
        "distinct_carrier_operators": True,
        "all_states_agree": True,
        "result": "PASS_COUNTEREXAMPLE",
        "scope": "quantifier repair only; no formal mathematical disposition",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
