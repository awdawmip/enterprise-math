import unittest
from itertools import product

from enterprise_math.material_future_markov import (
    PureMaterialFutureState,
    advance_pure_material_future_state,
    compile_pure_material_future_state,
)
from enterprise_math.material_future_precision import (
    OUTSIDE,
    REPRESENTED,
    compile_material_future_precision,
)


class PureMaterialFutureMarkovTests(unittest.TestCase):
    def test_inside_and_outside_can_merge_when_material_cannot_see_boundary(self):
        samples = (7, 7, 7, 7)
        inside = compile_pure_material_future_state((2, 0), 3, samples, 2)
        outside = compile_pure_material_future_state((3, 0), 3, samples, 2)
        self.assertEqual(inside, outside)

        inside_diag = compile_material_future_precision((2, 0), 3, samples, 2)
        outside_diag = compile_material_future_precision((3, 0), 3, samples, 2)
        self.assertEqual(inside_diag.status, REPRESENTED)
        self.assertEqual(outside_diag.status, OUTSIDE)
        self.assertNotEqual(inside_diag, outside_diag)

    def test_pure_transition_matches_fresh_full_geometry_compile_exhaustively(self):
        response_families = (
            (0, 0, 0, 0, 0),
            (0, 1, 2, 3, 4),
            (0, 0, 1, 1, 2),
            (0, 1, 1, 1, 2),
            (0, 1, 0, 1, 0),
            (2, 2, 3, 2, 3),
        )
        checked = 0
        for dimension in range(1, 4):
            for factor in range(2, 6):
                for samples in response_families:
                    for horizon in range(1, 4):
                        for state in product(range(factor + 1), repeat=dimension):
                            if not any(state):
                                continue
                            diagnostic = compile_material_future_precision(
                                state, factor, samples, horizon
                            )
                            if diagnostic.status not in (REPRESENTED, OUTSIDE):
                                continue
                            compact = compile_pure_material_future_state(
                                state, factor, samples, horizon
                            )
                            for axis in range(dimension):
                                updated = advance_pure_material_future_state(
                                    compact, axis
                                )
                                post = list(state)
                                post[axis] += 1
                                expected = compile_pure_material_future_state(
                                    tuple(post),
                                    factor,
                                    samples,
                                    horizon - 1,
                                )
                                self.assertEqual(updated, expected)
                                checked += 1
        self.assertGreater(checked, 20_000)

    def test_constant_word_transition_needs_no_active_axis_identity(self):
        state = PureMaterialFutureState(
            horizon=3,
            response_word=(5, 5, 5, 5),
            capped_deficits=(0, 0, 0),
        )
        transitions = {
            advance_pure_material_future_state(state, axis)
            for axis in range(3)
        }
        self.assertEqual(len(transitions), 1)
        only = transitions.pop()
        self.assertEqual(only.response_word, (5, 5, 5))
        self.assertEqual(only.capped_deficits, (0, 0, 0))

    def test_nonconstant_word_uses_zero_deficit_as_active_witness(self):
        state = PureMaterialFutureState(
            horizon=2,
            response_word=(9, 9, 4),
            capped_deficits=(0, 1),
        )
        active = advance_pure_material_future_state(state, 0)
        nonactive = advance_pure_material_future_state(state, 1)
        self.assertEqual(active.response_word, (9, 4))
        self.assertEqual(nonactive.response_word, (9, 9))
        self.assertNotEqual(active, nonactive)

    def test_primitive_and_underresolved_geometry_are_not_given_fake_material_states(self):
        with self.assertRaises(ValueError):
            compile_pure_material_future_state((0, 0), 5, (0, 10), 2)
        with self.assertRaises(ValueError):
            compile_pure_material_future_state((1, 0), 5, (0, 10), 2)

    def test_invalid_compact_states_or_actions_are_rejected(self):
        with self.assertRaises(ValueError):
            advance_pure_material_future_state(
                PureMaterialFutureState(1, (1, 0), (2,)), 0
            )
        with self.assertRaises(ValueError):
            advance_pure_material_future_state(
                PureMaterialFutureState(0, (1,), (0,)), 0
            )
        with self.assertRaises(ValueError):
            advance_pure_material_future_state(
                PureMaterialFutureState(1, (1, 0), (0,)), 1
            )


if __name__ == "__main__":
    unittest.main()
