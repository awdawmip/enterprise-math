import unittest

from enterprise_math.semantic_shortcut_frontier import (
    semantic_shortcut_frontier_depths_closed_form,
    semantic_shortcut_frontier_matches_enumeration,
)


class SemanticShortcutFrontierTests(unittest.TestCase):
    def test_k8_reference(self):
        self.assertEqual(
            semantic_shortcut_frontier_depths_closed_form(8),
            (1, 2, 3, 4, 8),
        )

    def test_closed_form_matches_enumeration_through_large_prefix(self):
        for generator_count in range(1, 101):
            self.assertTrue(
                semantic_shortcut_frontier_matches_enumeration(generator_count)
            )

    def test_frontier_is_sparse(self):
        for k in (10, 100, 1000):
            depths = semantic_shortcut_frontier_depths_closed_form(k)
            self.assertLess(len(depths), k)
            self.assertEqual(depths[0], 1)
            self.assertEqual(depths[-1], k)

    def test_validation(self):
        with self.assertRaises(ValueError):
            semantic_shortcut_frontier_depths_closed_form(0)


if __name__ == "__main__":
    unittest.main()
