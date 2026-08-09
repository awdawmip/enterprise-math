import unittest
from itertools import combinations_with_replacement

from enterprise_math.material_edge_work_relation import (
    MULTIPLE_ENDPOINTS,
    NO_ENDPOINT,
    UNIQUE_ENDPOINT,
    loading_edge_work_candidates,
    material_edge_work_relation_report,
    returning_edge_work_candidates,
    verify_hardening_loading_endpoint_uniqueness,
)
from enterprise_math.material_force_work import uniform_force_law
from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_response import explicit_material_curve_profile


class MaterialEdgeWorkRelationTests(unittest.TestCase):
    def test_hooke_loading_has_one_exact_branch_consistent_endpoint_for_reference_momentum(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2, 3, 4),
                returning=(0, 1, 2, 3, 4),
                amplitude=4,
            )
        )
        report = material_edge_work_relation_report(law, 0, 5, LOADING)
        self.assertEqual(report.relation_status, UNIQUE_ENDPOINT)
        self.assertEqual(report.branch_consistent_relation_status, UNIQUE_ENDPOINT)
        candidate = report.candidates[0]
        self.assertEqual(candidate.end_depth, 4)
        self.assertEqual(candidate.deformation_displacement, 4)
        self.assertEqual(candidate.oriented_momentum_after, 3)
        self.assertEqual(candidate.branch_work_numerator2, 16)
        self.assertEqual(candidate.kinetic_square_change, -16)
        self.assertEqual((candidate.edge_impulse_numerator, candidate.edge_impulse_denominator), (2, 1))
        self.assertTrue(candidate.branch_consistent)
        self.assertFalse(candidate.requires_within_tick_branch_switch)

    def test_same_hooke_law_can_have_no_endpoint_at_fixed_unit_time(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2, 3, 4),
                returning=(0, 1, 2, 3, 4),
                amplitude=4,
            )
        )
        report = material_edge_work_relation_report(law, 0, 4, LOADING)
        self.assertEqual(report.relation_status, NO_ENDPOINT)
        self.assertEqual(report.candidates, ())

    def test_nonmonotone_loading_can_have_multiple_energy_candidates_but_both_cross_branch(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 18, 12, 0, 17),
                returning=(0, 18, 12, 0, 17),
                amplitude=18,
            )
        )
        report = material_edge_work_relation_report(law, 0, 8, LOADING)
        self.assertEqual(report.relation_status, MULTIPLE_ENDPOINTS)
        self.assertEqual(
            [(c.end_depth, c.oriented_momentum_after, c.branch_work_numerator2) for c in report.candidates],
            [(2, -4, 48), (3, -2, 60)],
        )
        self.assertTrue(all(c.requires_within_tick_branch_switch for c in report.candidates))
        self.assertEqual(report.branch_consistent_candidates, ())
        self.assertEqual(report.branch_consistent_relation_status, NO_ENDPOINT)

    def test_negative_loading_endpoint_is_not_a_single_branch_hysteresis_step(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2, 3, 4),
                returning=(0, 0, 0, 0, 0),
                amplitude=4,
            )
        )
        candidates = loading_edge_work_candidates(law, 0, 5)
        # At depth 4, both +3 and -3 solve the work square, but only +3 is the
        # unit-time endpoint.  In the time-free relation the negative root would
        # imply an unrepresented turn/return subsegment and must be marked so.
        from enterprise_math.material_edge_time_compatibility import loading_endpoint_time_candidates
        timed = loading_endpoint_time_candidates(law, 0, 5)
        negative = [c for c in timed if c.end_depth == 4 and c.momentum_after < 0]
        self.assertEqual(len(negative), 1)
        # material_edge_work_candidates fixes unit time, so its p1=+3 candidate is branch-consistent.
        self.assertTrue(all(c.branch_consistent for c in candidates))

    def test_every_candidate_closes_midpoint_and_energy_identities_exactly(self):
        laws = [
            uniform_force_law(
                explicit_material_curve_profile(
                    loading=(0, 1, 2, 3, 4), returning=(0, 1, 2, 3, 4), amplitude=4
                )
            ),
            uniform_force_law(
                explicit_material_curve_profile(
                    loading=(0, 18, 12, 0, 17), returning=(0, 18, 12, 0, 17), amplitude=18
                )
            ),
        ]
        for law in laws:
            for start in range(len(law.profile.loading)):
                for momentum in range(0, 15):
                    for candidate in loading_edge_work_candidates(law, start, momentum):
                        dx = candidate.deformation_displacement
                        self.assertEqual(
                            candidate.oriented_momentum_before + candidate.oriented_momentum_after,
                            2 * dx,
                        )
                        self.assertEqual(
                            candidate.oriented_momentum_before ** 2
                            - candidate.oriented_momentum_after ** 2,
                            candidate.branch_work_numerator2,
                        )
                    for candidate in returning_edge_work_candidates(law, start, momentum):
                        dx = candidate.deformation_displacement
                        self.assertEqual(
                            candidate.oriented_momentum_before + candidate.oriented_momentum_after,
                            2 * dx,
                        )
                        self.assertEqual(
                            candidate.oriented_momentum_after ** 2
                            - candidate.oriented_momentum_before ** 2,
                            candidate.branch_work_numerator2,
                        )
                        self.assertTrue(candidate.branch_consistent)

    def test_hardening_loading_has_at_most_one_exact_endpoint_in_bounded_exhaustion(self):
        for length in range(2, 7):
            for tail in combinations_with_replacement(range(0, 7), length - 1):
                loading = (0,) + tuple(tail)
                amplitude = max(1, *loading)
                law = uniform_force_law(
                    explicit_material_curve_profile(
                        loading=loading,
                        returning=loading,
                        amplitude=amplitude,
                    )
                )
                for start in range(length):
                    for momentum in range(0, 15):
                        self.assertTrue(
                            verify_hardening_loading_endpoint_uniqueness(
                                law, start, momentum
                            )
                        )

    def test_returning_candidate_can_release_exact_static_branch_work(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 4),
                returning=(0, 1, 3),
                amplitude=4,
            )
        )
        candidates = []
        for momentum in range(0, 12):
            for candidate in returning_edge_work_candidates(law, 2, momentum):
                candidates.append(candidate)
                self.assertEqual(candidate.branch, RETURNING)
                self.assertGreaterEqual(candidate.kinetic_square_change, 0)
                self.assertTrue(candidate.branch_consistent)
        self.assertTrue(candidates)

    def test_invalid_branch_and_start_are_rejected(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1), returning=(0, 1), amplitude=1
            )
        )
        with self.assertRaises(ValueError):
            material_edge_work_relation_report(law, 0, 1, "UNKNOWN")
        with self.assertRaises(ValueError):
            loading_edge_work_candidates(law, 2, 1)


if __name__ == "__main__":
    unittest.main()
