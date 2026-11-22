import unittest

from enterprise_math.p017_core_cell_lattice import (
    admissible_partial_core_pair,
    exact_full_core_pair,
    exact_full_core_strata,
    exact_stratum_moebius_count,
    intersect_partial_core_cells,
    partial_cell_zeta_count,
    partial_core_cell,
    raw_partial_core_progression,
    residual_strict_refinement_steps,
)


class P017CoreCellLatticeTests(unittest.TestCase):
    def test_raw_progression_matches_direct_divisibility(self) -> None:
        for k in range(5, 80):
            center = k * (k + 1)
            for a in range(1, min(k, 21), 2):
                for b in range(1, min(k, 21), 2):
                    if not admissible_partial_core_pair(k, a, b):
                        continue
                    data = raw_partial_core_progression(k, a, b)
                    direct = tuple(
                        r
                        for r in range(1, k)
                        if r % 2 == 1 and (center - r) % a == 0 and (center + r) % b == 0
                    )
                    self.assertEqual(data["raw_radii"], direct)

    def test_lcm_intersection_closure(self) -> None:
        for k in range(5, 90):
            pairs = []
            for a in range(1, min(k, 25), 2):
                for b in range(1, min(k, 25), 2):
                    if admissible_partial_core_pair(k, a, b):
                        pairs.append((a, b))
            for index, (a, b) in enumerate(pairs):
                for c, d in pairs[index + 1 : index + 12]:
                    data = intersect_partial_core_cells(k, a, b, c, d)
                    direct = tuple(sorted(set(partial_core_cell(k, a, b)) & set(partial_core_cell(k, c, d))))
                    self.assertEqual(data["intersection"], direct)

    def test_exact_label_is_maximal_partial_label(self) -> None:
        for k in range(3, 90):
            strata = exact_full_core_strata(k)
            reconstructed = []
            for (a, b), radii in strata.items():
                for r in radii:
                    self.assertEqual(exact_full_core_pair(k, r), (a, b))
                    self.assertIn(r, partial_core_cell(k, a, b))
                    reconstructed.append(r)
            center = k * (k + 1)
            direct = [r for r in range(1, k) if __import__("math").gcd(r, center) == 1]
            self.assertEqual(sorted(reconstructed), direct)

    def test_partial_counts_are_exact_stratum_zeta_sums(self) -> None:
        for k in range(5, 75):
            strata = exact_full_core_strata(k)
            targets = {(1, 1)}
            for a, b in list(strata)[:12]:
                targets.add((a, b))
                targets.add((1, b))
                targets.add((a, 1))
            for a, b in targets:
                if admissible_partial_core_pair(k, a, b):
                    data = partial_cell_zeta_count(k, a, b)
                    self.assertEqual(data["direct_count"], data["zeta_count"])

    def test_double_moebius_inversion_recovers_exact_strata(self) -> None:
        for k in range(5, 55):
            strata = exact_full_core_strata(k)
            for a, b in list(strata)[:16]:
                data = exact_stratum_moebius_count(k, a, b)
                self.assertEqual(data["direct_count"], len(strata[(a, b)]))
                self.assertEqual(data["direct_count"], data["moebius_count"])

    def test_residual_refinement_depth_uses_factor_three(self) -> None:
        self.assertEqual(residual_strict_refinement_steps(100, 15), 1)
        self.assertEqual(residual_strict_refinement_steps(500, 15), 3)
        self.assertEqual(residual_strict_refinement_steps(15, 15), 0)
        for k in range(10, 500):
            for product in range(1, k, 2):
                steps = residual_strict_refinement_steps(k, product)
                self.assertLess(3 ** (steps + 1) * product, 3 * k)
                if steps:
                    self.assertLess(3**steps * product, k)
                self.assertGreaterEqual(3 ** (steps + 1) * product, k)


if __name__ == "__main__":
    unittest.main()
