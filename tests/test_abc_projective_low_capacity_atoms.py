import unittest

from enterprise_math.abc_projective_low_capacity_atoms import (
    cutoff_five_atom,
    populated_nontrivial_cutoff_five_shells,
    prime_prime_complements_cannot_activate,
)


class ProjectiveLowCapacityAtomTests(unittest.TestCase):
    def test_prime_prime_shell_is_impossible(self) -> None:
        for p, q in ((2, 3), (3, 5), (5, 11), (17, 29)):
            self.assertTrue(prime_prime_complements_cannot_activate(p, q))

    def test_every_other_unordered_shell_has_an_exact_fixture(self) -> None:
        fixtures = populated_nontrivial_cutoff_five_shells()
        self.assertEqual(
            set(fixtures),
            {
                (1, 2), (1, 3), (1, 4),
                (2, 2), (2, 3), (2, 4),
                (3, 3), (3, 4),
                (4, 4),
            },
        )
        for shell, triple in fixtures.items():
            atom = cutoff_five_atom(*triple, threshold=1)
            self.assertIsNotNone(atom)
            assert atom is not None
            self.assertEqual(atom.exponent_shell, shell)
            self.assertGreaterEqual(atom.active_residual, atom.cross_capacity)

    def test_sum_and_difference_modes_both_occur(self) -> None:
        sum_atom = cutoff_five_atom(2, 25, 27)
        self.assertIsNotNone(sum_atom)
        assert sum_atom is not None
        self.assertEqual(sum_atom.mode, "sum")
        self.assertEqual(sum_atom.exponent_shell, (1, 2))
        self.assertEqual(sum_atom.active_residual, sum_atom.cross_capacity)

        diff_atom = cutoff_five_atom(49, 576, 625)
        self.assertIsNotNone(diff_atom)
        assert diff_atom is not None
        self.assertEqual(diff_atom.mode, "difference")
        self.assertEqual(diff_atom.exponent_shell, (2, 4))
        self.assertGreater(diff_atom.active_residual, diff_atom.cross_capacity)

    def test_subunit_triple_has_no_atom(self) -> None:
        self.assertIsNone(cutoff_five_atom(2, 3, 5))


if __name__ == "__main__":
    unittest.main()
