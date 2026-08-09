import unittest
from itertools import product

from enterprise_math.clearance_horizon_precision import (
    isotropic_named_horizon_class_count,
)
from enterprise_math.material_future_precision import (
    PRIMITIVE_CONTACT,
    REPRESENTED,
    UNDERRESOLVED,
    compile_material_future_precision,
    full_material_future_signature,
    material_future_class_count,
    material_response_word,
    material_visible_deficit_cap,
    permutation_symmetric_material_future_class_count,
)


class MaterialFuturePrecisionTests(unittest.TestCase):
    def test_constant_response_word_erases_direction_and_raw_depth(self):
        samples = (0, 10, 10, 10, 20)
        first = compile_material_future_precision((3, 0), 5, samples, 1)
        second = compile_material_future_precision((2, 2), 5, samples, 1)
        # Raw depths are 2 and 3, but both material futures are (10,10).
        self.assertEqual(first.status, REPRESENTED)
        self.assertEqual(second.status, REPRESENTED)
        self.assertEqual(first.response_word, (10, 10))
        self.assertEqual(second.response_word, (10, 10))
        self.assertEqual(first.visible_deficit_cap, 0)
        self.assertEqual(second.visible_deficit_cap, 0)
        self.assertEqual(first.capped_deficits, (0, 0))
        self.assertEqual(second.capped_deficits, (0, 0))
        self.assertEqual(first, second)

    def test_first_visible_material_boundary_reduces_raw_horizon_cap(self):
        # Depth-4 response stays 9 for two decrements, then changes at step 3.
        samples = (0, 4, 9, 9, 9)
        word = material_response_word(samples, depth=4, horizon=4)
        self.assertEqual(word, (9, 9, 9, 4, 0))
        self.assertEqual(material_visible_deficit_cap(word), 2)
        state = compile_material_future_precision((3, 0, 1), 7, samples, 4)
        self.assertEqual(state.status, REPRESENTED)
        self.assertEqual(state.response_word, word)
        self.assertEqual(state.visible_deficit_cap, 2)
        self.assertEqual(state.capped_deficits, (0, 2, 2))

    def test_compact_material_partition_equals_complete_material_future_partition(self):
        response_families = (
            (0, 0, 0, 0, 0),
            (0, 1, 2, 3, 4),
            (0, 0, 1, 1, 2),
            (0, 1, 1, 1, 2),
            (0, 1, 0, 1, 0),
        )
        for dimension in range(1, 4):
            for factor in range(2, 6):
                states = [
                    state
                    for state in product(range(factor), repeat=dimension)
                    if any(state)
                ]
                for samples in response_families:
                    max_depth = min(len(samples) - 1, factor - 1)
                    represented = [
                        state
                        for state in states
                        if factor - max(state) <= max_depth
                    ]
                    for horizon in range(4):
                        compact_to_full = {}
                        full_to_compact = {}
                        for state in represented:
                            compact = compile_material_future_precision(
                                state, factor, samples, horizon
                            )
                            full = full_material_future_signature(
                                state, factor, samples, horizon
                            )
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
                            material_future_class_count(
                                dimension, factor, samples, horizon
                            ),
                        )

    def test_nonmonotone_material_words_are_supported(self):
        samples = (0, 1, 0, 1, 0)
        for dimension in range(1, 4):
            for factor in range(2, 6):
                max_depth = min(len(samples) - 1, factor - 1)
                represented = [
                    state
                    for state in product(range(factor), repeat=dimension)
                    if any(state) and factor - max(state) <= max_depth
                ]
                for horizon in range(4):
                    compact_to_full = {}
                    full_to_compact = {}
                    for state in represented:
                        compact = compile_material_future_precision(
                            state, factor, samples, horizon
                        )
                        full = full_material_future_signature(
                            state, factor, samples, horizon
                        )
                        compact_to_full.setdefault(compact, set()).add(full)
                        full_to_compact.setdefault(full, set()).add(compact)
                    self.assertTrue(
                        all(len(outputs) == 1 for outputs in compact_to_full.values())
                    )
                    self.assertTrue(
                        all(len(signatures) == 1 for signatures in full_to_compact.values())
                    )

    def test_strictly_distinguishing_response_recovers_raw_horizon_precision(self):
        # R(k)=k is injective in represented scalar depth, so material-aware
        # quotient must exactly recover canonical raw P024 horizon precision.
        for dimension in range(1, 5):
            for factor in range(2, 8):
                samples = tuple(range(factor))
                for horizon in range(4):
                    self.assertEqual(
                        material_future_class_count(
                            dimension, factor, samples, horizon
                        ),
                        isotropic_named_horizon_class_count(
                            dimension, factor, horizon
                        ),
                    )

    def test_h1_plateau_erases_active_set_exactly_when_adjacent_response_is_equal(self):
        samples = (0, 10, 10, 20, 30)
        factor = 5
        # depth 2 has R(2)=R(1)=10, so every nonempty active set merges.
        depth2 = set()
        # depth 3 has 20 != 10, so active sets remain visible.
        depth3 = set()
        for state in product(range(factor), repeat=3):
            if not any(state):
                continue
            depth = factor - max(state)
            if depth not in (2, 3):
                continue
            compiled = compile_material_future_precision(
                state, factor, samples, 1
            )
            (depth2 if depth == 2 else depth3).add(compiled)
        self.assertEqual(len(depth2), 1)
        self.assertEqual(len(depth3), 2**3 - 1)

    def test_permutation_symmetric_count_matches_sorted_material_signatures(self):
        samples = (0, 0, 1, 1, 2, 3)
        for dimension in range(1, 5):
            for factor in range(2, 7):
                max_depth = min(len(samples) - 1, factor - 1)
                for horizon in range(4):
                    orbits = set()
                    for state in product(range(factor), repeat=dimension):
                        if not any(state):
                            continue
                        if factor - max(state) > max_depth:
                            continue
                        compiled = compile_material_future_precision(
                            state, factor, samples, horizon
                        )
                        orbits.add(
                            (
                                compiled.response_word,
                                tuple(sorted(compiled.capped_deficits)),
                            )
                        )
                    self.assertEqual(
                        len(orbits),
                        permutation_symmetric_material_future_class_count(
                            dimension, factor, samples, horizon
                        ),
                    )

    def test_underresolved_and_primitive_contact_are_explicit_diagnostic_states(self):
        samples = (0, 100)
        under = compile_material_future_precision((1, 0), 5, samples, 2)
        self.assertEqual(under.status, UNDERRESOLVED)
        primitive = compile_material_future_precision((0, 0), 5, samples, 2)
        self.assertEqual(primitive.status, PRIMITIVE_CONTACT)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            material_response_word((), 0, 1)
        with self.assertRaises(ValueError):
            material_response_word((0, 1), 2, 1)
        with self.assertRaises(ValueError):
            compile_material_future_precision((), 3, (0, 1), 1)
        with self.assertRaises(ValueError):
            compile_material_future_precision((0,), 0, (0, 1), 1)


if __name__ == "__main__":
    unittest.main()
