import math
import unittest


def integer_root(n: int, p: int) -> int:
    if n < 0 or p < 1:
        raise ValueError
    if n < 2 or p == 1:
        return n
    lo = 0
    hi = n + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**p <= n:
            lo = mid
        else:
            hi = mid
    return lo


def scale_state(n: int, p: int, d: int) -> int:
    if d < 1:
        raise ValueError
    return integer_root(n * d**p, p)


def project(m: int, fine: int, coarse: int) -> int:
    if coarse < 1 or fine < 1 or fine % coarse:
        raise ValueError
    return m // (fine // coarse)


class MultiBaseScaleTests(unittest.TestCase):
    def test_general_scale_compatibility(self) -> None:
        for p in range(1, 6):
            for d in range(1, 9):
                for ratio in range(1, 8):
                    e = d * ratio
                    for n in range(0, 301):
                        self.assertEqual(
                            project(scale_state(n, p, e), e, d),
                            scale_state(n, p, d),
                        )

    def test_projection_composition(self) -> None:
        for d in range(1, 8):
            for r in range(1, 6):
                for s in range(1, 6):
                    e = d * r
                    f = e * s
                    for m in range(0, 501):
                        self.assertEqual(
                            project(project(m, f, e), e, d),
                            project(m, f, d),
                        )

    def test_multibase_refinement_order_is_canonical(self) -> None:
        for p in range(1, 5):
            for d in range(1, 6):
                for a in range(1, 6):
                    for b in range(1, 6):
                        for n in range(0, 101):
                            self.assertEqual(
                                scale_state(n, p, d * a * b),
                                scale_state(n, p, d * b * a),
                            )

    def test_gcd_lcm_projection_diamond(self) -> None:
        for p in range(1, 5):
            for d in range(1, 10):
                for e in range(1, 10):
                    g = math.gcd(d, e)
                    L = math.lcm(d, e)
                    for n in range(0, 151):
                        fine = scale_state(n, p, L)
                        via_d = project(project(fine, L, d), d, g)
                        via_e = project(project(fine, L, e), e, g)
                        self.assertEqual(via_d, via_e)
                        self.assertEqual(via_d, scale_state(n, p, g))

    def test_base_level_is_only_a_scale_factor_representation(self) -> None:
        for p in range(1, 6):
            for n in range(0, 501):
                self.assertEqual(scale_state(n, p, 4), scale_state(n, p, 2**2))
                self.assertEqual(scale_state(n, p, 8), scale_state(n, p, 2**3))

    def test_no_state_only_refinement_for_square_root_1_to_10(self) -> None:
        coarse_2 = scale_state(2, 2, 1)
        coarse_3 = scale_state(3, 2, 1)
        fine_2 = scale_state(2, 2, 10)
        fine_3 = scale_state(3, 2, 10)
        self.assertEqual(coarse_2, 1)
        self.assertEqual(coarse_3, 1)
        self.assertEqual(fine_2, 14)
        self.assertEqual(fine_3, 17)
        self.assertNotEqual(fine_2, fine_3)


if __name__ == "__main__":
    unittest.main()
