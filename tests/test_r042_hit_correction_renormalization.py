import importlib.util
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

MODULE = TOOLS / "r042_hit_correction_renormalization.py"
spec = importlib.util.spec_from_file_location("r042renorm", MODULE)
ren = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ren
spec.loader.exec_module(ren)


class R042CorrectionRenormalizationTests(unittest.TestCase):
    def test_known_revisit_paths_satisfy_exact_correction_cocycle(self):
        cases = [
            (6, 11, [2, 6, 20, 65], [4, 12, -20]),
            (6, 15, [1, 3, 10], [-12, -28]),
            (7, 7, [1, 2, 5, 13, 33, 86, 228, 603, 1595, 4220, 11165, 29540],
             [-2, 8, -2, -32, -12, 28, 8, 8, 18, 18, 18]),
            (8, 14, [4, 14, 51, 190], [-8, -20, 4]),
        ]
        for s, r, path, qs in cases:
            cert = ren.correction_block(s, r, path)
            self.assertEqual(cert["q_digits"], qs)
            B = (r - 1) * (s - 4) ** 2
            self.assertEqual(cert["source_norm"], -B)
            self.assertEqual(cert["target_norm"], -B)
            self.assertNotEqual(cert["P"], (0, 0))
            self.assertNotEqual(cert["P_norm"], 0)

    def test_pell_seed_rank_and_unit_translation(self):
        cases = [(6, 11, 2), (6, 11, 65), (6, 15, 1), (6, 15, 10),
                 (7, 7, 1), (7, 7, 29540), (8, 14, 4), (8, 14, 190)]
        for s, r, seed in cases:
            c0 = ren.pell_coordinate(s, r, seed)
            self.assertEqual((c0.seed_hit, c0.unit_rank), (seed, 0))
            h1 = ren.unit_translate_hit(s, r, seed, 1)
            c1 = ren.pell_coordinate(s, r, h1)
            self.assertEqual((c1.seed_hit, c1.unit_rank), (seed, 1))

    def test_triangular_representative_reduced_seed_orbits(self):
        for seed in (1, 3):
            c0 = ren.pell_coordinate(3, 6, seed)
            self.assertEqual((c0.seed_hit, c0.unit_rank), (seed, 0))
            for n in range(1, 5):
                h = ren.unit_translate_hit(3, 6, seed, n)
                cn = ren.pell_coordinate(3, 6, h)
                self.assertEqual((cn.seed_hit, cn.unit_rank), (seed, n))

    def test_reverse_transition_is_exact_divisibility_plus_accessibility(self):
        y, z = ren.hit_pair(6, 11, 65)
        rev = ren.reverse_transition(6, 11, y, z)
        self.assertEqual(rev["parent_index"], 20)
        self.assertEqual(rev["q"], -20)
        self.assertEqual((y - rev["q"]) // 11, rev["parent_z"])

    def test_fixed_diagonal_difference_scales_by_unit(self):
        s, r, h0, h1, d = 6, 11, 2, 65, 3
        xi0 = ren.hit_pair(s, r, h0)
        xi1 = ren.hit_pair(s, r, h1)
        base_scaled = ren.alpha_power_times(r, xi0, d)
        delta0 = (xi1[0] - base_scaled[0], xi1[1] - base_scaled[1])

        _, eta = ren.residue_pell_unit(s, r)
        xi0u = ren.apply_unit(r, xi0, eta)
        xi1u = ren.apply_unit(r, xi1, eta)
        scaled_u = ren.alpha_power_times(r, xi0u, d)
        delta1 = (xi1u[0] - scaled_u[0], xi1u[1] - scaled_u[1])
        self.assertEqual(delta1, ren.apply_unit(r, delta0, eta))

    def test_bounded_unit_orbit_explorer_is_explicitly_non_theorem(self):
        atlas = ren.bounded_unit_orbit_reachability(3, 6, [1, 3], 12)
        self.assertEqual(atlas["classification"], "BOUNDED_EXHAUSTIVE_FOR_DECLARED_UNIT_TRANSLATES_ONLY")
        self.assertTrue(any(
            f["ancestor_hit"] == 1 and f["target_hit"] == 3
            for f in atlas["findings"]
        ))
        self.assertFalse(any(
            f["target_unit_rank"] > 0
            for f in atlas["findings"]
        ))


if __name__ == "__main__":
    unittest.main()
