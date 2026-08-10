import unittest

from enterprise_math.precision_module_cut_compiler import (
    column_bases_mod_p,
    column_circuits_mod_p,
    hidden_map_is_injective,
    minimal_reset_basis_size,
    minimal_reset_carrier_bases,
    primitive_columns_mod_p,
    retained_module_signature,
)


class ModuleCutCompilerTests(unittest.TestCase):
    def test_triangle_matroid_has_one_three_column_circuit(self):
        A = ((1, 1, 0), (0, 1, 1))
        self.assertTrue(primitive_columns_mod_p(A, 2))
        self.assertEqual(column_circuits_mod_p(A, 2), (frozenset({0, 1, 2}),))
        self.assertEqual(set(column_bases_mod_p(A, 2)), {
            frozenset({0, 1}), frozenset({0, 2}), frozenset({1, 2})
        })
        self.assertEqual(set(minimal_reset_carrier_bases(A, 2)), {
            frozenset({0}), frozenset({1}), frozenset({2})
        })
        self.assertEqual(minimal_reset_basis_size(A, 2), 1)

    def test_parallel_columns_give_pair_circuits(self):
        A = ((1, 1, 1),)
        self.assertEqual(set(column_circuits_mod_p(A, 3)), {
            frozenset({0, 1}), frozenset({0, 2}), frozenset({1, 2})
        })
        self.assertEqual({len(s) for s in minimal_reset_carrier_bases(A, 3)}, {2})

    def test_full_rank_observation_needs_no_reset_for_carrier(self):
        A = ((1, 0), (0, 1))
        self.assertEqual(column_circuits_mod_p(A, 2), tuple())
        self.assertEqual(minimal_reset_carrier_bases(A, 2), (frozenset(),))
        self.assertEqual(minimal_reset_basis_size(A, 2), 0)

    def test_mod_p_rank_controls_hidden_injectivity_for_p_power_world(self):
        A = ((1, 1, 2), (0, 1, 1))
        # mod 3: c2 = c0 + c1, so all three hidden coordinates are dependent.
        self.assertTrue(hidden_map_is_injective(A, 3, {0, 1}))
        self.assertFalse(hidden_map_is_injective(A, 3, {0, 1, 2}))
        x = (8, 5, 7)
        sig = retained_module_signature(x, A, 3, 2, {2})
        self.assertEqual(sig[1], (7,))

    def test_nonprimitive_column_is_rejected_for_exact_reset_recovery(self):
        A = ((1, 3), (0, 6))
        self.assertFalse(primitive_columns_mod_p(A, 3))
        with self.assertRaises(ValueError):
            retained_module_signature((1, 2), A, 3, 2, {1})


if __name__ == "__main__":
    unittest.main()
