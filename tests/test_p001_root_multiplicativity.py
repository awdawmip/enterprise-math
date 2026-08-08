import unittest

from enterprise_math.core import integer_nth_root


def delta(p: int, k: int) -> int:
    return (k + 1) ** p - k**p


def root_gap(n: int, p: int) -> int:
    r = integer_nth_root(n, p)
    return n - r**p


def carry_load(a: int, b: int, p: int) -> tuple[int, int, int, int, int]:
    r = integer_nth_root(a, p)
    s = integer_nth_root(b, p)
    u = a - r**p
    v = b - s**p
    load = s**p * u + r**p * v + u * v
    return r, s, u, v, load


class RootMultiplicativityTests(unittest.TestCase):
    def test_supermultiplicativity(self) -> None:
        for p in range(1, 6):
            for a in range(0, 151):
                for b in range(0, 151):
                    self.assertGreaterEqual(
                        integer_nth_root(a * b, p),
                        integer_nth_root(a, p) * integer_nth_root(b, p),
                    )

    def test_exact_no_carry_criterion(self) -> None:
        for p in range(1, 6):
            for a in range(0, 121):
                for b in range(0, 121):
                    r, s, _, _, load = carry_load(a, b, p)
                    multiplicative = integer_nth_root(a * b, p) == r * s
                    self.assertEqual(multiplicative, load < delta(p, r * s))

    def test_carry_count_characterization(self) -> None:
        for p in range(1, 5):
            for a in range(0, 101):
                for b in range(0, 101):
                    r, s, _, _, load = carry_load(a, b, p)
                    carry = integer_nth_root(a * b, p) - r * s
                    c = 0
                    while (r * s + c + 1) ** p - (r * s) ** p <= load:
                        c += 1
                    self.assertEqual(carry, c)

    def test_downward_closed_no_carry_region(self) -> None:
        for p in range(1, 5):
            for r in range(0, 8):
                for s in range(0, 8):
                    du = delta(p, r)
                    dv = delta(p, s)
                    good = {
                        (u, v)
                        for u in range(du)
                        for v in range(dv)
                        if s**p * u + r**p * v + u * v < delta(p, r * s)
                    }
                    for u, v in good:
                        for up in range(u + 1):
                            for vp in range(v + 1):
                                self.assertIn((up, vp), good)

    def test_one_perfect_factor_is_not_sufficient(self) -> None:
        self.assertEqual(integer_nth_root(4, 2), 2)
        self.assertEqual(integer_nth_root(3, 2), 1)
        self.assertEqual(integer_nth_root(12, 2), 3)

    def test_smallest_square_carry_hits_threshold(self) -> None:
        r, s, u, v, load = carry_load(2, 2, 2)
        self.assertEqual((r, s, u, v), (1, 1, 1, 1))
        self.assertEqual(load, delta(2, 1))
        self.assertEqual(integer_nth_root(4, 2), 2)


if __name__ == "__main__":
    unittest.main()
