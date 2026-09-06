from __future__ import annotations

import unittest
from math import isqrt

from enterprise_math.brc_multiplier_basin import (
    endpoint_resonance_defect,
    multiplier_basin_profile,
    nonsquare_stable_support_law,
    point_cost_state,
    square_multiplier_law,
    squarefree_composition_state,
    squarefree_decomposition,
)


class BRCMultiplierBasinTests(unittest.TestCase):
    def test_cost_complement(self) -> None:
        for n in range(1, 200):
            for multiplier in range(1, 40):
                state = point_cost_state(n, multiplier)
                self.assertEqual(
                    state.subtraction_cost + state.addition_cost,
                    2 * state.target_root + 1,
                )

    def test_generic_profile_conserves_source_multiplicity(self) -> None:
        for k in range(0, 30):
            for multiplier in range(1, 80):
                profile = multiplier_basin_profile(k, multiplier)
                self.assertEqual(profile.total_multiplicity, 2 * k + 1)
                for branch in profile.branches:
                    self.assertEqual(branch.cwm.count, branch.count)
                    self.assertEqual(branch.cwm.total, branch.count)
                    self.assertEqual(branch.cwm.dominant, 1)

    def test_square_multiplier_full_law(self) -> None:
        for k in range(0, 60):
            source_count = 2 * k + 1
            for s in range(1, 100):
                law = square_multiplier_law(k, s)
                self.assertEqual(law.support_size, min(s, source_count))
                self.assertEqual(sum(branch.count for branch in law.branches), source_count)
                exact = multiplier_basin_profile(k, s * s)
                self.assertEqual(
                    tuple((b.target_root, b.count) for b in law.branches),
                    tuple((b.target_root, b.count) for b in exact.branches),
                )
                if s <= source_count:
                    q, a = divmod(source_count, s)
                    self.assertTrue(law.dense_regime)
                    self.assertEqual(
                        tuple(branch.target_root for branch in law.branches),
                        tuple(range(s * k, s * (k + 1))),
                    )
                    counts = tuple(branch.count for branch in law.branches)
                    self.assertTrue(all(count in (q, q + 1) for count in counts))
                    self.assertEqual(sum(count == q + 1 for count in counts), a)
                else:
                    self.assertFalse(law.dense_regime)
                    self.assertTrue(all(branch.count == 1 for branch in law.branches))

    def test_nonsquare_stable_beatty_pell_formula(self) -> None:
        for multiplier in range(2, 250):
            floor_root = isqrt(multiplier)
            if floor_root * floor_root == multiplier:
                continue
            k0 = max(1, (floor_root + 1) // 2)
            while multiplier > 4 * k0 * k0:
                k0 += 1
            for k in range(k0, k0 + 40):
                law = nonsquare_stable_support_law(k, multiplier)
                self.assertIn(
                    law.beatty_step,
                    (law.floor_sqrt_multiplier, law.floor_sqrt_multiplier + 1),
                )
                exact = multiplier_basin_profile(k, multiplier)
                self.assertTrue(exact.consecutive_support)
                self.assertEqual(law.support_size, exact.support_size)

    def test_known_endpoint_resonances(self) -> None:
        observed = []
        for q in range(1, 1000):
            defect, event = endpoint_resonance_defect(q, 2)
            if event:
                observed.append((q, defect))
        self.assertEqual(
            observed[:5],
            [(1, 1), (5, 1), (29, 1), (169, 1), (985, 1)],
        )

    def test_squarefree_composition_identity(self) -> None:
        for multiplier in range(1, 250):
            a, d = squarefree_decomposition(multiplier)
            self.assertEqual(a * a * d, multiplier)
            for n in range(1, 350, 7):
                state = squarefree_composition_state(n, multiplier)
                self.assertEqual(state.square_part, a)
                self.assertEqual(state.squarefree_kernel, d)
                self.assertTrue(0 <= state.refinement_phase < a)
                self.assertEqual(
                    state.target_remainder,
                    multiplier * n - state.target_root * state.target_root,
                )


if __name__ == "__main__":
    unittest.main()
