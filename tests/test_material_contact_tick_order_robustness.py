import unittest
from functools import lru_cache
from itertools import product

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
)
from enterprise_math.material_contact_network_tick_1d import (
    ContactMaterialImpulseState,
    apply_contact_material_tick,
)
from enterprise_math.material_contact_tick_order_robustness import (
    every_target_permutation_is_guarded,
    material_tick_order_robustness,
    negative_cross_enable_band,
    target_order_robustness_report,
    worst_preaction_scores,
)


def direct_step(scores, coupling, action):
    if scores[action] >= 0:
        return None
    return tuple(
        scores[row] + coupling[row][action]
        for row in range(len(scores))
    )


def all_permutations_legal(initial_scores, coupling, target_counts):
    @lru_cache(maxsize=None)
    def visit(scores, remaining):
        if not any(remaining):
            return True
        for action, count in enumerate(remaining):
            if count == 0:
                continue
            after = direct_step(scores, coupling, action)
            if after is None:
                return False
            nxt = tuple(
                value - (1 if index == action else 0)
                for index, value in enumerate(remaining)
            )
            if not visit(after, nxt):
                return False
        return True

    return visit(tuple(initial_scores), tuple(target_counts))


def some_permutation_legal(initial_scores, coupling, target_counts):
    @lru_cache(maxsize=None)
    def visit(scores, remaining):
        if not any(remaining):
            return True
        for action, count in enumerate(remaining):
            if count == 0:
                continue
            after = direct_step(scores, coupling, action)
            if after is None:
                continue
            nxt = tuple(
                value - (1 if index == action else 0)
                for index, value in enumerate(remaining)
            )
            if visit(after, nxt):
                return True
        return False

    return visit(tuple(initial_scores), tuple(target_counts))


class MaterialContactTickOrderRobustnessTests(unittest.TestCase):
    def test_closed_all_permutation_criterion_matches_exhaustive_small_integer_matrices(self):
        # Exhaust all 2x2 integer couplings in a small cube.  This includes
        # positive/negative diagonals and positive/negative cross coupling.
        for entries in product(range(-1, 2), repeat=4):
            coupling = (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for initial in product(range(-1, 2), repeat=2):
                for target in product(range(3), repeat=2):
                    if sum(target) > 3:
                        continue
                    expected = all_permutations_legal(
                        initial,
                        coupling,
                        target,
                    )
                    actual = every_target_permutation_is_guarded(
                        initial,
                        coupling,
                        target,
                    )
                    self.assertEqual(
                        actual,
                        expected,
                        (initial, coupling, target),
                    )

    def test_worst_preaction_score_is_literal_prefix_maximum(self):
        initial = (-2, -1)
        coupling = ((2, 3), (-2, -1))
        target = (2, 2)
        # Contact 0: worst prefix has one prior self action and both positive
        # cross actions: -2 + 2 + 2*3 = 6.
        # Contact 1: negative diagonal/cross entries never increase its score,
        # so the worst pre-action value is the initial -1.
        self.assertEqual(
            worst_preaction_scores(initial, coupling, target),
            (6, -1),
        )

    def test_four_policy_levels_are_strictly_distinct(self):
        # Z-coupled cross-enablement: a completion exists and every enabled-greedy
        # policy succeeds, but not every literal permutation is legal because
        # contact 1 starts disabled.
        z_report = target_order_robustness_report(
            (-1, 0),
            ((2, -1), (-1, 2)),
            (1, 1),
        )
        self.assertTrue(z_report.some_guarded_order)
        self.assertFalse(z_report.every_permutation_guarded)
        self.assertTrue(z_report.z_coupled)
        self.assertTrue(all(value for _, value in z_report.z_greedy_policy_results))

        # Fully order-robust path state.
        robust = target_order_robustness_report(
            (-1, -1),
            ((2, -1), (-1, 2)),
            (1, 1),
        )
        self.assertTrue(robust.some_guarded_order)
        self.assertTrue(robust.every_permutation_guarded)

        # Positive branching batch target with no guarded realization at all.
        batch_only = target_order_robustness_report(
            (-1, -1, -1),
            (
                (2, 1, 1),
                (1, 2, 1),
                (1, 1, 2),
            ),
            (1, 1, 1),
        )
        self.assertFalse(batch_only.some_guarded_order)
        self.assertTrue(batch_only.batched_only)

    def test_negative_cross_enable_band_is_exact(self):
        for coupling in range(-4, 1):
            for score in range(-2, 6):
                expected = coupling < 0 and 0 <= score < -coupling
                self.assertEqual(
                    negative_cross_enable_band(score, coupling),
                    expected,
                )

    def test_guarded_target_realizability_is_neither_lower_nor_upper_set(self):
        coupling = ((2, -1), (-1, 2))
        initial = (-1, 0)

        # Smaller target cannot start contact 1.
        self.assertFalse(
            some_permutation_legal(initial, coupling, (0, 1))
        )
        # Adding contact 0 first cross-enables contact 1.
        self.assertTrue(
            some_permutation_legal(initial, coupling, (1, 1))
        )
        # Adding yet another required contact-0 unit is impossible again.
        self.assertFalse(
            some_permutation_legal(initial, coupling, (2, 1))
        )

    def test_every_permutation_implies_some_order_but_not_conversely(self):
        cases = (
            (
                (-1, -1),
                ((2, -1), (-1, 2)),
                (1, 1),
            ),
            (
                (-1, 0),
                ((2, -1), (-1, 2)),
                (1, 1),
            ),
            (
                (-2, -2),
                ((1, 1), (1, 1)),
                (1, 1),
            ),
        )
        for initial, coupling, target in cases:
            every = every_target_permutation_is_guarded(
                initial,
                coupling,
                target,
            )
            some = some_permutation_legal(initial, coupling, target)
            self.assertFalse(every and not some)

        self.assertTrue(
            some_permutation_legal(
                (-1, 0),
                ((2, -1), (-1, 2)),
                (1, 1),
            )
        )
        self.assertFalse(
            every_target_permutation_is_guarded(
                (-1, 0),
                ((2, -1), (-1, 2)),
                (1, 1),
            )
        )

    def test_material_tick_reports_order_robust_path_and_batch_only_star(self):
        path = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        path_tick = apply_contact_material_tick(
            path,
            (
                ContactMaterialImpulseState(1, 1, 0),
                ContactMaterialImpulseState(1, 1, 0),
            ),
            (1, 1),
        )
        path_report = material_tick_order_robustness(path_tick)
        self.assertTrue(path_report.some_guarded_order)
        self.assertTrue(path_report.every_permutation_guarded)

        star = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(1, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(0, 2, 1),
                ContactChannel1D(0, 3, 1),
            ),
        )
        star_tick = apply_contact_material_tick(
            star,
            tuple(ContactMaterialImpulseState(1, 1, 0) for _ in range(3)),
            (1, 1, 1),
        )
        star_report = material_tick_order_robustness(star_tick)
        self.assertTrue(star_report.batched_only)
        self.assertFalse(star_report.every_permutation_guarded)

    def test_validation(self):
        with self.assertRaises(ValueError):
            worst_preaction_scores((), (), ())
        with self.assertRaises(ValueError):
            worst_preaction_scores((-1,), ((1, 0),), (1,))
        with self.assertRaises(ValueError):
            worst_preaction_scores((-1,), ((1,),), (-1,))
        with self.assertRaises(TypeError):
            negative_cross_enable_band(False, -1)


if __name__ == "__main__":
    unittest.main()
