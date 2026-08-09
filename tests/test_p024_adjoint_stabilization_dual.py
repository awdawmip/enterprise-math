import unittest
from itertools import product
from math import lcm

from enterprise_math.adjoint_boundary_precision import natural_collapse_action
from enterprise_math.core import collapse


def _compose(left, right):
    return tuple(left[right[index]] for index in range(len(left)))


def _fixed_points(mapping):
    return {index for index, value in enumerate(mapping) if index == value}


def _stable_value(mapping, start):
    value = start
    for _ in range(len(mapping) + 2):
        nxt = mapping[value]
        if nxt == value:
            return value
        value = nxt
    raise AssertionError("finite monotone stabilization did not terminate")


def _chain_left_adjoint(right):
    size = len(right)
    left = []
    for boundary in range(size):
        candidates = [state for state in range(size) if boundary <= right[state]]
        if not candidates:
            return None
        left.append(min(candidates))
    result = tuple(left)
    for boundary in range(size):
        for state in range(size):
            if (result[boundary] <= state) != (boundary <= right[state]):
                return None
    return result


def _chain_right_adjoint_pairs(size):
    for right in product(range(size), repeat=size):
        if any(right[index] > right[index + 1] for index in range(size - 1)):
            continue
        if any(right[index] > index for index in range(size)):
            continue
        left = _chain_left_adjoint(right)
        if left is not None:
            yield left, right


def _integer_root(value, power):
    low = 0
    high = value + 1
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**power <= value:
            low = middle
        else:
            high = middle
    return low


def _least_perfect_power_at_least(value, power):
    root = _integer_root(value, power)
    if root**power < value:
        root += 1
    return root**power


def _forward_word(value, powers):
    for power in powers:
        value = collapse(value, power)
    return value


def _boundary_word(value, powers):
    # If W = C_pm o ... o C_p1, its left adjoint is
    # N_p1 o ... o N_pm, hence N_pm is applied first to a boundary.
    for power in reversed(powers):
        value = _least_perfect_power_at_least(value, power)
    return value


def _stabilize_word(value, powers, *, boundary):
    for _ in range(128):
        nxt = _boundary_word(value, powers) if boundary else _forward_word(value, powers)
        if nxt == value:
            return value
        value = nxt
    raise AssertionError("word did not stabilize in the audited domain")


class AdjointStabilizationDualTests(unittest.TestCase):
    def test_finite_chain_reductive_right_adjoint_duality(self) -> None:
        audited_pairs = 0
        for size in range(1, 6):
            for left, right in _chain_right_adjoint_pairs(size):
                audited_pairs += 1
                self.assertTrue(all(index <= left[index] for index in range(size)))
                self.assertEqual(_fixed_points(left), _fixed_points(right))

                stable_left = tuple(_stable_value(left, index) for index in range(size))
                stable_right = tuple(_stable_value(right, index) for index in range(size))
                for boundary in range(size):
                    for state in range(size):
                        self.assertEqual(
                            stable_left[boundary] <= state,
                            boundary <= stable_right[state],
                            msg=(size, left, right, boundary, state),
                        )
        self.assertEqual(audited_pairs, 23)

    def test_short_words_share_common_fixed_points_and_stable_adjunction(self) -> None:
        for size in range(1, 5):
            pairs = tuple(_chain_right_adjoint_pairs(size))
            identity = tuple(range(size))
            for first in range(len(pairs)):
                for second in range(len(pairs)):
                    lefts = (pairs[first][0], pairs[second][0])
                    rights = (pairs[first][1], pairs[second][1])

                    forward = identity
                    for right in rights:
                        forward = _compose(right, forward)

                    boundary = identity
                    for left in reversed(lefts):
                        boundary = _compose(left, boundary)

                    common = _fixed_points(rights[0]) & _fixed_points(rights[1])
                    self.assertEqual(_fixed_points(forward), common)
                    self.assertEqual(_fixed_points(boundary), common)

                    stable_boundary = tuple(_stable_value(boundary, index) for index in range(size))
                    stable_forward = tuple(_stable_value(forward, index) for index in range(size))
                    for cut in range(size):
                        for state in range(size):
                            self.assertEqual(
                                stable_boundary[cut] <= state,
                                cut <= stable_forward[state],
                                msg=(size, first, second, cut, state),
                            )

    def test_collapse_word_stabilizes_to_lcm_pair(self) -> None:
        families = (
            (2, 3),
            (3, 2),
            (2, 4),
            (4, 6),
            (2, 3, 5),
            (3, 4, 6),
            (2, 6, 4, 3),
        )
        for powers in families:
            stable_power = 1
            for power in powers:
                stable_power = lcm(stable_power, power)
            for value in range(300):
                self.assertEqual(
                    _stabilize_word(value, powers, boundary=False),
                    collapse(value, stable_power),
                    msg=(powers, value),
                )
                self.assertEqual(
                    _stabilize_word(value, powers, boundary=True),
                    _least_perfect_power_at_least(value, stable_power),
                    msg=(powers, value),
                )

    def test_stable_perfect_power_pair_is_adjoint(self) -> None:
        for power in range(1, 11):
            for boundary in range(80):
                upper = _least_perfect_power_at_least(boundary, power)
                for state in range(180):
                    self.assertEqual(
                        upper <= state,
                        boundary <= collapse(state, power),
                        msg=(power, boundary, state),
                    )

    def test_transient_order_differs_but_lcm_stable_map_agrees(self) -> None:
        value_a = 2
        trace_a = [value_a]
        for _ in range(8):
            value_a = _boundary_word(value_a, (3, 2))
            trace_a.append(value_a)
            if trace_a[-1] == trace_a[-2]:
                break

        value_b = 2
        trace_b = [value_b]
        for _ in range(8):
            value_b = _boundary_word(value_b, (2, 3))
            trace_b.append(value_b)
            if trace_b[-1] == trace_b[-2]:
                break

        self.assertEqual(trace_a[:4], [2, 9, 36, 64])
        self.assertEqual(trace_b[:4], [2, 8, 27, 64])
        self.assertEqual(trace_a[-1], 64)
        self.assertEqual(trace_b[-1], 64)
        self.assertEqual(64, _least_perfect_power_at_least(2, 6))

    def test_existing_collapse_action_exposes_same_upper_selector(self) -> None:
        for power in range(1, 8):
            action = natural_collapse_action(power)
            for boundary in range(100):
                self.assertEqual(
                    action.pullback_cut(boundary),
                    _least_perfect_power_at_least(boundary, power),
                )

    def test_distinct_lcm_classes_have_distinct_stable_boundary_maps(self) -> None:
        for left_power in range(1, 9):
            for right_power in range(1, 9):
                left = _least_perfect_power_at_least(2, left_power)
                right = _least_perfect_power_at_least(2, right_power)
                self.assertEqual(left == right, left_power == right_power)


if __name__ == "__main__":
    unittest.main()
