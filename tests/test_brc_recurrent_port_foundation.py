from fractions import Fraction
import unittest

from enterprise_math.brc_recurrent_ports import (
    recurrent_port_context_matrix,
    recurrent_port_dynamic_equivalent,
    recurrent_port_signature,
    recurrent_port_zeta_equivalent,
)

Q = Fraction


class RecurrentPortFoundationTests(unittest.TestCase):
    def test_same_dynamic_signature_different_hidden_zeta(self) -> None:
        m1 = [[Q(0), Q(1, 4)], [Q(1, 4), Q(1, 10)]]
        m2 = [[Q(1, 2), Q(1, 8)], [Q(1, 4), Q(1, 10)]]
        s1 = recurrent_port_signature(m1, [0])
        s2 = recurrent_port_signature(m2, [0])
        self.assertEqual(s1.effective_matrix, ((Q(13, 80),),))
        self.assertEqual(s2.effective_matrix, s1.effective_matrix)
        self.assertEqual(s1.hidden_loop_zeta, Q(1))
        self.assertEqual(s2.hidden_loop_zeta, Q(2))
        self.assertTrue(recurrent_port_dynamic_equivalent(s1, s2))
        self.assertFalse(recurrent_port_zeta_equivalent(s1, s2))

    def test_different_weff_is_not_dynamic_equivalence(self) -> None:
        m1 = [[Q(0), Q(1, 4)], [Q(1, 4), Q(1, 10)]]
        m3 = [[Q(0), Q(1, 4)], [Q(1, 4), Q(1, 8)]]
        s1 = recurrent_port_signature(m1, [0])
        s3 = recurrent_port_signature(m3, [0])
        self.assertEqual(s1.hidden_loop_zeta, s3.hidden_loop_zeta)
        self.assertNotEqual(s1.effective_matrix, s3.effective_matrix)
        self.assertFalse(recurrent_port_dynamic_equivalent(s1, s3))

    def test_context_matrix(self) -> None:
        matrix = [[Q(0), Q(1, 4)], [Q(1, 4), Q(1, 10)]]
        signature = recurrent_port_signature(matrix, [0])
        context = recurrent_port_context_matrix(
            signature,
            [[Q(1, 20)]],
            [[Q(1, 10)]],
            [[Q(1, 12)]],
            [[Q(1, 8)]],
        )
        self.assertEqual(
            context,
            ((Q(17, 80), Q(1, 10)), (Q(1, 12), Q(1, 8))),
        )

    def test_two_port_signature(self) -> None:
        matrix = [
            [Q(1, 10), Q(1, 12), Q(1, 8), Q(1, 11)],
            [Q(1, 15), Q(1, 10), Q(1, 13), Q(1, 9)],
            [Q(1, 14), Q(1, 10), Q(1, 10), Q(1, 18)],
            [Q(1, 12), Q(1, 16), Q(1, 17), Q(1, 10)],
        ]
        signature = recurrent_port_signature(matrix, [0, 1])
        self.assertEqual(signature.boundary_indices, (2, 3))
        self.assertEqual(signature.port_count, 2)
        self.assertEqual(len(signature.effective_matrix), 2)
        self.assertGreaterEqual(signature.hidden_loop_zeta, 1)

    def test_typing_and_scope_guards(self) -> None:
        with self.assertRaises(TypeError):
            recurrent_port_signature([[False, 0], [0, 0]], [0])
        with self.assertRaises(ValueError):
            recurrent_port_signature([[0, 0], [0, 0]], [])
        with self.assertRaises(ValueError):
            recurrent_port_signature([[1, 0], [0, 0]], [0])
        signature = recurrent_port_signature([[0, 0], [0, 0]], [0])
        with self.assertRaises(TypeError):
            recurrent_port_context_matrix(signature, [[True]], [[]], [], [])


if __name__ == "__main__":
    unittest.main()
