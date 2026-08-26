import unittest

from enterprise_math.p017_full_block_token_incidence import (
    canonical_full_block_incidence_mobius,
    canonical_full_block_partition,
    exact_full_block_signed_points,
)


class P017FullBlockTokenIncidenceTests(unittest.TestCase):
    def test_k22_radical15_lifts_to_full_block75(self):
        # M=506, upper r=19 gives n=525=3*5^2*7.
        data = canonical_full_block_incidence_mobius(22, 75)
        self.assertEqual(data["radical"], 15)
        self.assertEqual(data["prime_exponents"], ((3, 1), (5, 2)))
        self.assertEqual(data["canonical_signed_points"], (-19,))
        self.assertEqual(data["exact_full_block_incidence"], 1)
        self.assertTrue(data["full_block_single_use"])
        self.assertEqual(data["full_block_cg12_capacity"], 1)
        self.assertEqual(exact_full_block_signed_points(22, 75), (-19,))

        partition = canonical_full_block_partition(22, 15)
        self.assertEqual(partition["canonical_squarefree_incidence"], 1)
        self.assertEqual(partition["full_block_incidence"], 1)
        self.assertEqual(partition["reusable_full_block_incidence"], 0)
        self.assertEqual(partition["single_use_full_block_incidence"], 1)
        self.assertEqual(
            tuple(row["full_block"] for row in partition["full_block_rows"]),
            (75,),
        )

    def test_k22_radical21_remains_reusable_full_block(self):
        # The same state 525 has exact selected block 3*7=21 for the {3,7} token.
        data = canonical_full_block_incidence_mobius(22, 21)
        self.assertEqual(data["canonical_signed_points"], (-19,))
        self.assertEqual(data["exact_full_block_incidence"], 1)
        self.assertFalse(data["full_block_single_use"])

        partition = canonical_full_block_partition(22, 21)
        self.assertEqual(partition["canonical_squarefree_incidence"], 1)
        self.assertEqual(partition["reusable_full_block_incidence"], 1)
        self.assertEqual(partition["single_use_full_block_incidence"], 0)

    def test_prime_power_multiplicity_strictly_reduces_reusable_token_mass(self):
        # Squarefree order-one reusable tokens at k=22 are D=15 and D=21.
        # Exact p-adic lifting moves D=15 to A=75>21, so only one reusable
        # full-block token remains.
        reusable = 0
        single_use = 0
        total = 0
        for radical in (15, 21, 39, 57):
            partition = canonical_full_block_partition(22, radical)
            total += partition["full_block_incidence"]
            reusable += partition["reusable_full_block_incidence"]
            single_use += partition["single_use_full_block_incidence"]
        self.assertEqual(total, 4)
        self.assertEqual(reusable, 1)
        self.assertEqual(single_use, 3)

    def test_nonmatching_exponent_vector_has_zero_incidence(self):
        # No canonical k=22 token state has exact selected block 3^2*5=45.
        data = canonical_full_block_incidence_mobius(22, 45)
        self.assertEqual(data["exact_full_block_incidence"], 0)
        self.assertEqual(data["canonical_signed_points"], ())

    def test_invalid_nontransverse_block(self):
        with self.assertRaises(ValueError):
            canonical_full_block_incidence_mobius(22, 33)  # includes anchor prime 11


if __name__ == "__main__":
    unittest.main()
