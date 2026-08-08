import unittest


class TestP008Minimality(unittest.TestCase):
    def test_preorder_galois_connection_can_fail_equality_idempotence(self):
        a_states = (0, 1)
        b_states = (0, 1)
        le_a = lambda _x, _y: True
        le_b = lambda _x, _y: True
        lower = {0: 0, 1: 1}
        upper = {0: 1, 1: 0}

        for a in a_states:
            for b in b_states:
                self.assertEqual(le_b(lower[a], b), le_a(a, upper[b]))

        collapse = lambda b: lower[upper[b]]
        self.assertEqual(collapse(0), 1)
        self.assertEqual(collapse(1), 0)
        self.assertNotEqual(collapse(collapse(0)), collapse(0))

    def test_nonlattice_poset_still_supports_identity_adjoint(self):
        states = ("zero", "a", "b")

        def le(left, right):
            return left == right or left == "zero"

        self.assertFalse(any(le("a", z) and le("b", z) for z in states))
        for left in states:
            for right in states:
                self.assertEqual(le(left, right), le(left, right))

    def test_power_sublevels_have_greatest_elements(self):
        for p in range(1, 6):
            for n in range(0, 101):
                admissible = [k for k in range(n + 1) if k**p <= n]
                greatest = max(admissible)
                self.assertTrue(all(k <= greatest for k in admissible))

    def test_multiplication_sublevels_have_greatest_elements(self):
        for d in range(1, 10):
            for n in range(0, 101):
                admissible = [q for q in range(n + 1) if d * q <= n]
                self.assertEqual(max(admissible), n // d)


if __name__ == "__main__":
    unittest.main()
