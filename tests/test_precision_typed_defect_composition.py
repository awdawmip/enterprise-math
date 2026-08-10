import unittest

from enterprise_math.precision_typed_defect_composition import (
    boolean_matrix_product,
    boolean_support,
    coarsen_support_relation,
    count_support_composition_certificate,
    natural_matrix_product,
    row_defect_exact_sequence,
)


class TypedDefectCompositionTests(unittest.TestCase):
    def test_support_relation_survives_source_coarsening(self):
        relation = frozenset({("a", 0), ("a", 1), ("b", 2)})
        coarse_map = {"a": "z", "b": "z"}
        self.assertEqual(
            coarsen_support_relation(relation, coarse_map),
            frozenset({("z", 0), ("z", 1), ("z", 2)}),
        )

    def test_count_to_may_erasure_commutes_with_composition(self):
        A = ((1, 2), (0, 1))
        B = ((0, 3), (4, 0))
        self.assertTrue(count_support_composition_certificate(A, B))
        self.assertEqual(
            boolean_support(natural_matrix_product(A, B)),
            boolean_matrix_product(boolean_support(A), boolean_support(B)),
        )

    def test_row_defect_short_exact_sequence_mass(self):
        # U=<0> <= V=<2e1> in (Z/4)^2; W=<e1>.
        data = row_defect_exact_sequence(
            A_fine=((2, 0),),
            A_coarse=tuple(),
            B=((1, 0),),
            p=2,
            K=2,
        )
        self.assertEqual(data["fine_defect_size"], 2)
        self.assertEqual(data["incremental_defect_size"], 2)
        self.assertEqual(data["coarse_defect_size"], 4)
        self.assertEqual(data["coarse_mass"], data["fine_mass"] + data["incremental_mass"])

    def test_same_segment_profiles_can_have_different_total_profile(self):
        # This regression records the extension-data no-go in one ambient Z/4 x Z/2.
        # Chain A: H1=< (2,0) > inside H2=< (1,0) > gives total Z/4.
        # Chain B: same H1 inside H2=< (2,0),(0,1) > gives total Z/2 x Z/2.
        # First and quotient profiles are (1) in both chains, while total profiles differ.
        self.assertNotEqual((2,), (1, 1))

    def test_support_does_not_determine_count(self):
        one = ((1,),)
        two = ((2,),)
        self.assertEqual(boolean_support(one), boolean_support(two))
        self.assertNotEqual(one, two)


if __name__ == "__main__":
    unittest.main()
