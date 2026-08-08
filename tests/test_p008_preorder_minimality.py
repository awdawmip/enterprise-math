import unittest


class TestP008PreorderMinimality(unittest.TestCase):
    def test_galois_connection_on_indiscrete_preorders_can_fail_equality_idempotence(self):
        a_states = (0, 1)
        b_states = (0, 1)

        # Indiscrete preorders: every comparison is true.
        le_a = lambda _left, _right: True
        le_b = lambda _left, _right: True

        lower = {0: 0, 1: 1}
        upper = {0: 1, 1: 0}

        for a in a_states:
            for b in b_states:
                self.assertEqual(le_b(lower[a], b), le_a(a, upper[b]))

        collapse = lambda b: lower[upper[b]]
        self.assertEqual(collapse(0), 1)
        self.assertEqual(collapse(1), 0)
        self.assertNotEqual(collapse(collapse(0)), collapse(0))

    def test_nonlattice_poset_identity_still_forms_an_adjoint(self):
        states = ("zero", "a", "b")

        def le(left, right):
            return left == right or left == "zero"

        # a and b have no common upper bound in this poset, so it is not a lattice.
        self.assertFalse(any(le("a", candidate) and le("b", candidate) for candidate in states))

        # Identity is nevertheless self-adjoint.
        for left in states:
            for right in states:
                self.assertEqual(le(left, right), le(left, right))

    def test_greatest_sublevel_characterization_for_integer_power(self):
        for exponent in range(1, 6):
            for n in range(0, 101):
                admissible = [k for k in range(0, n + 1) if k**exponent <= n]
                greatest = max(admissible)
                self.assertLessEqual(greatest**exponent, n)
                self.assertTrue(all(k <= greatest for k in admissible))

    def test_greatest_sublevel_characterization_for_multiplication(self):
        for divisor in range(1, 10):
            for n in range(0, 101):
                admissible = [q for q in range(0, n + 1) if divisor * q <= n]
                self.assertEqual(max(admissible), n // divisor)


if __name__ == "__main__":
    unittest.main()
