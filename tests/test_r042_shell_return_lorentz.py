import importlib.util
import pathlib
import sys
import unittest
from math import isqrt

MODULE = pathlib.Path(__file__).resolve().parents[1] / "tools" / "r042_shell_return_lorentz.py"
spec = importlib.util.spec_from_file_location("r042_lorentz", MODULE)
r042 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r042
spec.loader.exec_module(r042)


class R042ShellReturnLorentzTests(unittest.TestCase):
    def test_known_return_blocks_reconstruct_source(self):
        cases = [
            (3, 6, 1, -1, 0, (7, 3)),
            (6, 11, 3, 24, 12, (46, 14)),
            (6, 15, 2, -28, -12, (22, 6)),
            (7, 7, 11, -41996, 9678, (17, 7)),
            (8, 14, 3, -108, -20, (164, 44)),
        ]
        for s, r, d, p, q, expected in cases:
            got = {(c.Y, c.Z) for c in r042.shell_return_candidates(s, r, d, p, q)}
            self.assertIn(expected, got)

    def test_norm_divisibility_on_known_returns(self):
        cases = [
            (3, 6, 1, -1, 0),
            (6, 11, 3, 24, 12),
            (6, 15, 2, -28, -12),
            (7, 7, 11, -41996, 9678),
            (8, 14, 3, -108, -20),
        ]
        for args in cases:
            self.assertTrue(r042.norm_divisibility_holds(*args))

    def test_digit_aggregation(self):
        self.assertEqual(r042.aggregate_from_digits(11, [4, 12, -20]), (24, 12))
        self.assertEqual(r042.aggregate_from_digits(15, [-12, -28]), (-28, -12))
        self.assertEqual(r042.aggregate_from_digits(14, [-8, -20, 4]), (-108, -20))

    def test_arithmetic_shell_certificate_is_not_dynamic_legality(self):
        digits = [-12, -32, -22, 18]
        p, q = r042.aggregate_from_digits(7, digits)
        self.assertEqual((p, q), (-206, -106))
        got = {(c.Y, c.Z) for c in r042.shell_return_candidates(7, 7, 4, p, q)}
        self.assertEqual(got, {(17, 7)})

        def exact_children(s, r, k):
            a = s - 2
            c = s - 4
            z = 2 * a * k - c
            B = (r - 1) * c * c
            root = isqrt(r * z * z - B)
            den = 2 * a
            if root * root == r * z * z - B and (c + root) % den == 0:
                return ((c + root) // den,)
            lo = (c + root) // den
            return (lo, lo + 1)

        self.assertIn(2, exact_children(7, 7, 1))
        self.assertIn(4, exact_children(7, 7, 2))
        self.assertNotIn(9, exact_children(7, 7, 4))
        self.assertEqual(exact_children(7, 7, 4), (10, 11))
        self.assertEqual(exact_children(7, 7, 24), (63,))
        m = 10
        B = 54
        z_parent = 37
        z_child = 87
        E = 7 * z_parent * z_parent - z_child * z_child - B
        self.assertEqual(E, 1960)
        self.assertFalse(-2 * m * z_child + m * m < E < 2 * m * z_child + m * m)
        self.assertEqual((-2 * m * z_child + m * m, 2 * m * z_child + m * m), (-1640, 1840))

    def test_shell_correction_even_gap_field_obstruction(self):
        for r in [5, 6, 7, 8, 10, 11, 14, 15]:
            if int(r ** 0.5) ** 2 == r:
                continue
            for d in [2, 4, 6, 8]:
                self.assertFalse(r042.shell_correction_field_possible(r, d))

    def test_shell_correction_odd_examples_and_tail_obstruction(self):
        self.assertTrue(r042.shell_correction_field_possible(5, 1))
        self.assertTrue(r042.shell_correction_field_possible(12, 1))
        for r in [5, 6, 7, 8, 10, 11, 12, 14, 15, 21, 32]:
            for d in [3, 5, 7, 9]:
                self.assertFalse(r042.shell_correction_field_possible(r, d))

    def test_correction_word_eliminates_to_unique_reverse_certificate(self):
        def exact_children(s, r, k):
            a = s - 2
            c = s - 4
            z = 2 * a * k - c
            B = (r - 1) * c * c
            root = isqrt(r * z * z - B)
            den = 2 * a
            if root * root == r * z * z - B and (c + root) % den == 0:
                return ((c + root) // den,)
            lo = (c + root) // den
            return (lo, lo + 1)

        def predecessor(s, r, child):
            if child < 1:
                return None
            a = s - 2
            c = s - 4
            zc = 2 * a * child - c
            B = (r - 1) * c * c
            root = isqrt((zc * zc + B) // r)
            p0 = (c + root) // (2 * a)
            found = []
            for parent in range(max(1, p0 - 3), p0 + 4):
                if child in exact_children(s, r, parent):
                    found.append(parent)
            if len(found) > 1:
                raise AssertionError("recoalescence in separated test regime")
            return found[0] if found else None

        cand = next(c for c in r042.shell_return_candidates(6, 11, 3, 24, 12)
                    if (c.Y, c.Z) == (46, 14))
        self.assertEqual(
            r042.verify_dynamic_chord(6, 11, 3, 24, 12, cand, predecessor),
            (2, 6, 20, 65, 215),
        )

        p, q = r042.aggregate_from_digits(7, [-12, -32, -22, 18])
        cand = r042.shell_return_candidates(7, 7, 4, p, q)[0]
        self.assertIsNone(r042.verify_dynamic_chord(7, 7, 4, p, q, cand, predecessor))


if __name__ == "__main__":
    unittest.main()
