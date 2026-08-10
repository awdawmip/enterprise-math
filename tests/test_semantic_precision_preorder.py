import unittest

from enterprise_math.semantic_precision_preorder import (
    observationally_refines_but_semantically_not,
    operation_safe_on_partition,
    partition_refines,
    safe_operation_refinement_switch,
    semantic_precision_state,
    semantically_incomparable,
    semantically_refines,
)


class SemanticPrecisionPreorderTests(unittest.TestCase):
    def test_finer_partition_can_lose_safe_operation(self):
        coarse = ({0, 1, 2}, {3})
        fine = ({0, 1}, {2}, {3})
        operation = {
            0: 0,
            1: 2,
            2: 0,
            3: 3,
        }
        self.assertTrue(partition_refines(fine, coarse))
        self.assertTrue(operation_safe_on_partition(coarse, operation))
        self.assertFalse(operation_safe_on_partition(fine, operation))
        switch = safe_operation_refinement_switch(coarse, fine, operation)
        self.assertTrue(switch.lost_under_refinement)
        self.assertFalse(switch.gained_under_refinement)

    def test_finer_partition_can_gain_safe_operation(self):
        coarse = ({0, 1}, {2, 3})
        fine = ({0}, {1}, {2}, {3})
        operation = {
            0: 0,
            1: 2,
            2: 2,
            3: 3,
        }
        self.assertFalse(operation_safe_on_partition(coarse, operation))
        self.assertTrue(operation_safe_on_partition(fine, operation))
        switch = safe_operation_refinement_switch(coarse, fine, operation)
        self.assertTrue(switch.gained_under_refinement)
        self.assertFalse(switch.lost_under_refinement)

    def test_observational_refinement_without_capability_preservation_is_not_semantic_refinement(self):
        coarse = semantic_precision_state(
            ({0, 1, 2}, {3}),
            {"t", "branch_reflection"},
            description="coarse but operation-safe",
        )
        fine = semantic_precision_state(
            ({0, 1}, {2}, {3}),
            {"numeric_detail"},
            description="finer states but lost theory",
        )
        self.assertTrue(partition_refines(fine.partition, coarse.partition))
        self.assertTrue(observationally_refines_but_semantically_not(fine, coarse))
        self.assertFalse(semantically_refines(fine, coarse))

    def test_product_order_semantic_refinement(self):
        coarse = semantic_precision_state(
            ({0, 1}, {2, 3}),
            {"addition"},
        )
        fine = semantic_precision_state(
            ({0}, {1}, {2}, {3}),
            {"addition", "multiplication", "branch_reflection"},
        )
        self.assertTrue(semantically_refines(fine, coarse))
        self.assertFalse(semantically_refines(coarse, fine))

    def test_numeric_and_logical_capability_tradeoff_can_make_states_incomparable(self):
        # Abstract coefficient analogue of mod p versus mod p^2:
        # p^2 distinguishes more numeric states but lacks the domain-law
        # capability enjoyed by the prime field.
        mod_p = semantic_precision_state(
            ({0, 2}, {1, 3}),
            {"product_branch_reflection"},
            description="prime-field quotient",
        )
        mod_p2 = semantic_precision_state(
            ({0}, {1}, {2}, {3}),
            {"finer_residue_numeric"},
            description="prime-power quotient",
        )
        self.assertTrue(partition_refines(mod_p2.partition, mod_p.partition))
        self.assertTrue(semantically_incomparable(mod_p, mod_p2))

    def test_capability_superset_without_observational_refinement_is_not_enough(self):
        left = semantic_precision_state(
            ({0, 1}, {2, 3}),
            {"A", "B"},
        )
        right = semantic_precision_state(
            ({0, 2}, {1, 3}),
            {"A", "B", "C"},
        )
        self.assertFalse(partition_refines(right.partition, left.partition))
        self.assertFalse(semantically_refines(right, left))

    def test_validation(self):
        with self.assertRaises(ValueError):
            semantic_precision_state(())
        with self.assertRaises(ValueError):
            semantic_precision_state(({0, 1}, {1, 2}))
        with self.assertRaises(ValueError):
            semantically_refines(
                semantic_precision_state(({0}, {1})),
                semantic_precision_state(({0}, {2})),
            )
        with self.assertRaises(ValueError):
            safe_operation_refinement_switch(
                ({0}, {1}, {2}),
                ({0, 1}, {2}),
                {0: 0, 1: 1, 2: 2},
            )


if __name__ == "__main__":
    unittest.main()
