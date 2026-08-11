import unittest

from enterprise_math.semantic_shortcut_generator_pareto import (
    decompose_target_into_shortcuts,
    literal_free_word_cache_entries,
    minimum_canonical_shortcut_storage_for_geodesic_budget,
    minimum_shortcut_depth_for_geodesic_budget,
    semantic_shortcut_distance,
    semantic_shortcut_generator_count,
    semantic_shortcut_pareto_frontier,
    semantic_to_literal_storage_ratio,
    shortcut_masks,
    worst_case_semantic_shortcut_distance,
)


class SemanticShortcutGeneratorParetoTests(unittest.TestCase):
    def test_exact_storage_counts(self):
        self.assertEqual(semantic_shortcut_generator_count(8, 1), 8)
        self.assertEqual(semantic_shortcut_generator_count(8, 2), 36)
        self.assertEqual(semantic_shortcut_generator_count(8, 3), 92)
        self.assertEqual(semantic_shortcut_generator_count(8, 4), 162)
        self.assertEqual(semantic_shortcut_generator_count(8, 8), 255)

    def test_exact_target_distance_and_constructive_decomposition(self):
        k = 8
        target = 0b11101101
        support = target.bit_count()
        for depth in range(1, k + 1):
            expected = (support + depth - 1) // depth
            self.assertEqual(semantic_shortcut_distance(target, k, depth), expected)
            pieces = decompose_target_into_shortcuts(target, k, depth)
            self.assertEqual(len(pieces), expected)
            combined = 0
            for piece in pieces:
                self.assertLessEqual(piece.bit_count(), depth)
                combined |= piece
            self.assertEqual(combined, target)

    def test_worst_case_full_mask_distance(self):
        for k in range(1, 21):
            for depth in range(1, k + 1):
                self.assertEqual(
                    worst_case_semantic_shortcut_distance(k, depth),
                    (k + depth - 1) // depth,
                )
                self.assertEqual(
                    semantic_shortcut_distance((1 << k) - 1, k, depth),
                    worst_case_semantic_shortcut_distance(k, depth),
                )

    def test_shortcut_catalogue_contains_exactly_masks_of_weight_at_most_d(self):
        masks = shortcut_masks(5, 2)
        self.assertEqual(len(masks), 5 + 10)
        self.assertTrue(all(1 <= mask.bit_count() <= 2 for mask in masks))
        self.assertEqual(len(set(masks)), len(masks))

    def test_binary_like_k8_frontier(self):
        frontier = semantic_shortcut_pareto_frontier(8)
        depths = tuple(point.shortcut_depth for point in frontier)
        self.assertEqual(depths, (1, 2, 3, 4, 8))
        resources = tuple(
            (point.primitive_shortcut_count, point.worst_case_geodesic)
            for point in frontier
        )
        self.assertEqual(
            resources,
            ((8, 8), (36, 4), (92, 3), (162, 2), (255, 1)),
        )

    def test_minimum_depth_and_storage_for_geodesic_budget(self):
        k = 20
        expected_depth = {1: 20, 2: 10, 3: 7, 4: 5, 5: 4, 7: 3, 10: 2, 20: 1}
        for budget, depth in expected_depth.items():
            self.assertEqual(minimum_shortcut_depth_for_geodesic_budget(k, budget), depth)
            storage = minimum_canonical_shortcut_storage_for_geodesic_budget(k, budget)
            self.assertEqual(storage, semantic_shortcut_generator_count(k, depth))

    def test_semantic_quotient_before_cache_reduces_storage(self):
        semantic, literal = semantic_to_literal_storage_ratio(20, 3)
        self.assertEqual(semantic, 1350)
        self.assertEqual(literal, 8420)
        self.assertLess(semantic, literal)

        semantic2, literal2 = semantic_to_literal_storage_ratio(8, 4)
        self.assertEqual(semantic2, 162)
        self.assertEqual(literal2, 4680)
        self.assertLess(semantic2, literal2)

    def test_full_semantic_table_is_two_to_k_minus_one(self):
        for k in range(1, 15):
            self.assertEqual(
                semantic_shortcut_generator_count(k, k),
                (1 << k) - 1,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            semantic_shortcut_generator_count(0, 1)
        with self.assertRaises(ValueError):
            semantic_shortcut_generator_count(3, 4)
        with self.assertRaises(ValueError):
            semantic_shortcut_distance(8, 3, 1)


if __name__ == "__main__":
    unittest.main()
