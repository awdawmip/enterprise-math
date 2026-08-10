import unittest

from enterprise_math.causal_kappa11_profile import kappa11_minimal_vectors
from enterprise_math.causal_primitive_group_presentation import (
    certify_translation_rank_with_realization,
    unique_primitive_difference_target,
)
from enterprise_math.causal_primitive_link_profile import a_roots, primitive_direction_graph


def negate(vector):
    return tuple(-value for value in vector)


class CausalPrimitiveGroupPresentationTests(unittest.TestCase):
    def test_fcc_inverse_difference_presentation_certifies_rank_three(self):
        roots = a_roots(3)
        adjacency = primitive_direction_graph(roots)
        certificate = certify_translation_rank_with_realization(adjacency, negate, roots)
        self.assertEqual(certificate.primitive_count, 12)
        self.assertEqual(certificate.modular_relation_rank, 9)
        self.assertEqual(certificate.realization_span_rank, 3)
        self.assertEqual(certificate.certified_translation_rank, 3)
        self.assertTrue(certificate.relations_hold_in_realization)

    def test_kappa11_local_inverse_difference_relations_certify_rank_eleven(self):
        roots = kappa11_minimal_vectors()
        adjacency = primitive_direction_graph(roots)
        certificate = certify_translation_rank_with_realization(adjacency, negate, roots)
        self.assertEqual(certificate.primitive_count, 432)
        self.assertEqual(certificate.modular_relation_rank, 421)
        self.assertEqual(certificate.realization_span_rank, 11)
        self.assertEqual(certificate.certified_translation_rank, 11)
        self.assertTrue(certificate.relations_hold_in_realization)

    def test_kappa11_every_primitive_compatible_pair_has_unique_difference_target(self):
        roots = kappa11_minimal_vectors()
        adjacency = primitive_direction_graph(roots)
        for left in roots:
            for right in adjacency[left]:
                target = unique_primitive_difference_target(adjacency, negate, left, right)
                # Coordinate subtraction is only an audit of the relation selected
                # by inverse + primitive compatibility.
                self.assertEqual(target, tuple(b - a for a, b in zip(left, right)))


if __name__ == "__main__":
    unittest.main()
