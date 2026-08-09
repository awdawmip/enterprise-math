import unittest
from itertools import product

from enterprise_math.clearance_horizon_precision import (
    INSIDE,
    OUTSIDE,
    advance_clearance_horizon_state,
    anisotropic_named_horizon_class_count,
    compile_clearance_horizon_state,
    isotropic_horizon_growth_increment,
    isotropic_named_horizon_class_count,
    isotropic_named_horizon_closed_form,
    permutation_symmetric_isotropic_class_count,
    residual_escape_depth_after_action_counts,
)


def action_count_vectors(dimension, horizon):
    result = []
    for total in range(horizon + 1):
        def rec(index, remaining, prefix):
            if index == dimension - 1:
                result.append(tuple(prefix + [remaining]))
                return
            for count in range(remaining + 1):
                rec(index + 1, remaining - count, prefix + [count])
        rec(0, total, [])
    return tuple(result)


def full_scalar_future(clearance, factors, horizon):
    return tuple(
        residual_escape_depth_after_action_counts(clearance, factors, actions)
        for actions in action_count_vectors(len(factors), horizon)
    )


class ClearanceHorizonPrecisionTests(unittest.TestCase):
    def test_capped_deficit_partition_equals_complete_future_partition(self):
        for dimension in range(1, 4):
            for factors in product(range(1, 5), repeat=dimension):
                states = [
                    clearance
                    for clearance in product(*[range(factor) for factor in factors])
                    if any(clearance)
                ]
                for horizon in range(5):
                    compact_to_full = {}
                    full_to_compact = {}
                    for clearance in states:
                        compact = compile_clearance_horizon_state(
                            clearance, factors, horizon
                        )
                        full = full_scalar_future(clearance, factors, horizon)
                        compact_to_full.setdefault(compact, set()).add(full)
                        full_to_compact.setdefault(full, set()).add(compact)
                    self.assertTrue(
                        all(len(outputs) == 1 for outputs in compact_to_full.values())
                    )
                    self.assertTrue(
                        all(len(signatures) == 1 for signatures in full_to_compact.values())
                    )
                    self.assertEqual(
                        len(compact_to_full),
                        anisotropic_named_horizon_class_count(factors, horizon),
                    )

    def test_compact_action_transition_matches_fresh_full_state_compile(self):
        for dimension in range(1, 4):
            for factors in product(range(1, 5), repeat=dimension):
                for clearance in product(*[range(factor) for factor in factors]):
                    for horizon in range(1, 5):
                        compact = compile_clearance_horizon_state(
                            clearance, factors, horizon
                        )
                        self.assertEqual(compact.status, INSIDE)
                        for axis in range(dimension):
                            updated = advance_clearance_horizon_state(compact, axis)
                            full = list(clearance)
                            full[axis] += 1
                            expected = compile_clearance_horizon_state(
                                tuple(full), factors, horizon - 1
                            )
                            self.assertEqual(updated, expected)

    def test_outside_state_remains_outside_when_consuming_future_actions(self):
        state = compile_clearance_horizon_state((3, 0), (3, 5), 2)
        self.assertEqual(state.status, OUTSIDE)
        next_state = advance_clearance_horizon_state(state, 1)
        self.assertEqual(next_state.status, OUTSIDE)
        self.assertEqual(next_state.horizon, 1)
        self.assertEqual(next_state.escape_depth, 0)
        self.assertEqual(next_state.capped_deficits, ())

    def test_isotropic_closed_form_and_boundary_values(self):
        for dimension in range(1, 6):
            for factor in range(1, 9):
                for horizon in range(0, factor + 3):
                    exact = isotropic_named_horizon_class_count(
                        dimension, factor, horizon
                    )
                    self.assertEqual(
                        exact,
                        isotropic_named_horizon_closed_form(
                            dimension, factor, horizon
                        ),
                    )
                    if horizon == 0:
                        self.assertEqual(exact, factor - 1)
                    if horizon == 1:
                        self.assertEqual(
                            exact,
                            (2**dimension - 1) * (factor - 1),
                        )
                    if horizon >= factor - 1:
                        self.assertEqual(exact, factor**dimension - 1)

    def test_horizon_growth_increment_matches_class_count_difference(self):
        for dimension in range(1, 6):
            for factor in range(1, 9):
                for horizon in range(0, factor + 2):
                    current = isotropic_named_horizon_class_count(
                        dimension, factor, horizon
                    )
                    following = isotropic_named_horizon_class_count(
                        dimension, factor, horizon + 1
                    )
                    self.assertEqual(
                        following - current,
                        isotropic_horizon_growth_increment(
                            dimension, factor, horizon
                        ),
                    )
        # In one dimension scalar depth is already a complete Markov state.
        for factor in range(1, 10):
            for horizon in range(0, factor + 2):
                self.assertEqual(
                    isotropic_horizon_growth_increment(1, factor, horizon),
                    0,
                )

    def test_anisotropic_origin_class_separates_at_axis_slack_horizon(self):
        factors = (2, 5)
        # d_min=2, d_max-d_min=3.  Before h=3 the primitive origin shares its
        # capped signature with positive mixed-deepest states; at h=3 it is
        # separately identifiable and excluding it removes one quotient class.
        including_h2 = anisotropic_named_horizon_class_count(
            factors, 2, exclude_primitive_origin=False
        )
        excluding_h2 = anisotropic_named_horizon_class_count(
            factors, 2, exclude_primitive_origin=True
        )
        self.assertEqual(including_h2, excluding_h2)

        including_h3 = anisotropic_named_horizon_class_count(
            factors, 3, exclude_primitive_origin=False
        )
        excluding_h3 = anisotropic_named_horizon_class_count(
            factors, 3, exclude_primitive_origin=True
        )
        self.assertEqual(including_h3 - excluding_h3, 1)

    def test_permutation_symmetric_count_matches_sorted_capped_deficit_orbits(self):
        for dimension in range(1, 5):
            for factor in range(1, 7):
                states = [
                    clearance
                    for clearance in product(range(factor), repeat=dimension)
                    if any(clearance)
                ]
                for horizon in range(4):
                    signatures = set()
                    for clearance in states:
                        state = compile_clearance_horizon_state(
                            clearance,
                            (factor,) * dimension,
                            horizon,
                        )
                        signatures.add(
                            (
                                state.escape_depth,
                                tuple(sorted(state.capped_deficits)),
                            )
                        )
                    self.assertEqual(
                        len(signatures),
                        permutation_symmetric_isotropic_class_count(
                            dimension, factor, horizon
                        ),
                    )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            compile_clearance_horizon_state((0,), (), 1)
        with self.assertRaises(ValueError):
            compile_clearance_horizon_state((0, 0), (2,), 1)
        with self.assertRaises(ValueError):
            compile_clearance_horizon_state((-1,), (2,), 1)
        with self.assertRaises(ValueError):
            compile_clearance_horizon_state((0,), (2,), -1)
        state = compile_clearance_horizon_state((0,), (2,), 0)
        with self.assertRaises(ValueError):
            advance_clearance_horizon_state(state, 0)
        with self.assertRaises(ValueError):
            advance_clearance_horizon_state(
                compile_clearance_horizon_state((0,), (2,), 1), 1
            )


if __name__ == "__main__":
    unittest.main()
