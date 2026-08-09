import unittest

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
)
from enterprise_math.material_refined_contact_momentum_bridge import (
    apply_refined_contact_impulses_to_lifted_momentum,
    minimum_contact_momentum_denominator,
)
from enterprise_math.material_star_response_precision_phase import (
    star_general_final_score_numerators,
    star_minimum_response_relation_at_precision,
    star_symmetric_minimum_numerators,
)


def star_state(leaf_count: int) -> ContactNetworkMomentum1D:
    return ContactNetworkMomentum1D(
        masses=(1,) * (leaf_count + 1),
        momenta=(1,) + (0,) * leaf_count,
        contacts=tuple(
            ContactChannel1D(0, leaf, 1)
            for leaf in range(1, leaf_count + 1)
        ),
    )


class RefinedContactMomentumBridgeTests(unittest.TestCase):
    def test_integer_denominator_specializes_exactly_to_contact_network_owner(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1),
            momenta=(3, 2, 1, 0),
            contacts=(
                ContactChannel1D(0, 1),
                ContactChannel1D(1, 2),
                ContactChannel1D(2, 3),
            ),
        )
        impulses = (2, 3, 2)
        coarse = apply_contact_impulse_vector(state, impulses)
        lifted = apply_refined_contact_impulses_to_lifted_momentum(
            state,
            momentum_denominator=1,
            momentum_detail_numerators=(0, 0, 0, 0),
            impulse_numerators=impulses,
            impulse_denominators=(1, 1, 1),
        )
        self.assertEqual(lifted.common_denominator, 1)
        self.assertEqual(lifted.whole_momenta_after, coarse.after.momenta)
        self.assertEqual(lifted.momentum_details_after, (0, 0, 0, 0))
        self.assertEqual(
            lifted.contact_score_numerators_after,
            coarse.relative_scores_after,
        )
        self.assertEqual(
            lifted.total_momentum_numerator_before,
            lifted.total_momentum_numerator_after,
        )

    def test_three_leaf_symmetric_refinement_becomes_exact_body_state_after_lcm_lift(self):
        state = star_state(3)
        numerators = star_symmetric_minimum_numerators(
            leaf_count=3,
            closing_quantum=1,
            denominator=3,
        )
        self.assertEqual(numerators, (1, 1, 1))
        report = apply_refined_contact_impulses_to_lifted_momentum(
            state,
            momentum_denominator=4,
            momentum_detail_numerators=(0, 0, 0, 0),
            impulse_numerators=numerators,
            impulse_denominators=(3, 3, 3),
        )
        self.assertEqual(report.common_denominator, 12)
        self.assertEqual(report.body_numerators_before, (12, 0, 0, 0))
        self.assertEqual(report.body_numerators_after, (0, 4, 4, 4))
        self.assertEqual(report.total_momentum_numerator_before, 12)
        self.assertEqual(report.total_momentum_numerator_after, 12)
        self.assertEqual(report.contact_score_numerators_before, (-12, -12, -12))
        self.assertEqual(report.contact_score_numerators_after, (4, 4, 4))
        phase_scores = star_general_final_score_numerators(
            numerators,
            closing_quantum=1,
            denominator=3,
        )
        self.assertEqual(phase_scores, (1, 1, 1))
        self.assertEqual(
            report.contact_score_numerators_after,
            tuple(4 * score for score in phase_scores),
        )

    def test_denominator_five_nonsymmetric_minimum_relation_keeps_exact_score_witness(self):
        state = star_state(3)
        relation = star_minimum_response_relation_at_precision(
            leaf_count=3,
            closing_quantum=1,
            denominator=5,
        )
        self.assertEqual(set(relation), {(2, 1, 1), (1, 2, 1), (1, 1, 2)})
        for numerators in relation:
            report = apply_refined_contact_impulses_to_lifted_momentum(
                state,
                momentum_denominator=4,
                momentum_detail_numerators=(0, 0, 0, 0),
                impulse_numerators=numerators,
                impulse_denominators=(5, 5, 5),
            )
            self.assertEqual(report.common_denominator, 20)
            phase_scores = star_general_final_score_numerators(
                numerators,
                closing_quantum=1,
                denominator=5,
            )
            self.assertEqual(sum(phase_scores), 1)
            self.assertEqual(
                report.contact_score_numerators_after,
                tuple(4 * score for score in phase_scores),
            )
            self.assertEqual(
                report.total_momentum_numerator_before,
                report.total_momentum_numerator_after,
            )

    def test_mixed_contact_denominators_share_one_lcm_and_preserve_gram_update(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(2, 1, 0),
            contacts=(ContactChannel1D(0, 1), ContactChannel1D(1, 2)),
        )
        report = apply_refined_contact_impulses_to_lifted_momentum(
            state,
            momentum_denominator=6,
            momentum_detail_numerators=(1, -2, 1),
            impulse_numerators=(1, 1),
            impulse_denominators=(2, 3),
        )
        self.assertEqual(report.common_denominator, 6)
        self.assertEqual(report.contact_scale_factors, (3, 2))
        self.assertEqual(report.body_numerators_before, (13, 4, 1))
        self.assertEqual(report.body_delta_numerators, (-3, 1, 2))
        self.assertEqual(report.body_numerators_after, (10, 5, 3))
        self.assertEqual(report.contact_score_numerators_before, (-9, -3))
        self.assertEqual(report.contact_score_numerators_after, (-5, -2))
        self.assertEqual(
            report.contact_score_numerators_after,
            report.contact_score_numerators_expected,
        )

    def test_minimum_denominator_uses_divisibility_lattice_not_numeric_magnitude(self):
        self.assertEqual(minimum_contact_momentum_denominator(4, [3, 10, 6]), 60)
        self.assertEqual(minimum_contact_momentum_denominator(12, [3, 4, 6]), 12)
        self.assertEqual(minimum_contact_momentum_denominator(5, [4]), 20)

    def test_nonzero_details_survive_exact_common_lift_without_hidden_rounding(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3),
            momenta=(1, -1),
            contacts=(ContactChannel1D(0, 1),),
        )
        report = apply_refined_contact_impulses_to_lifted_momentum(
            state,
            momentum_denominator=4,
            momentum_detail_numerators=(1, -1),
            impulse_numerators=(1,),
            impulse_denominators=(6,),
        )
        self.assertEqual(report.common_denominator, 12)
        self.assertEqual(report.total_momentum_numerator_before, 0)
        self.assertEqual(report.total_momentum_numerator_after, 0)
        self.assertEqual(
            tuple(
                report.common_denominator * whole + detail
                for whole, detail in zip(
                    report.whole_momenta_after,
                    report.momentum_details_after,
                )
            ),
            report.body_numerators_after,
        )

    def test_invalid_fractional_contact_state_is_rejected(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1),
            momenta=(1, 0),
            contacts=(ContactChannel1D(0, 1),),
        )
        with self.assertRaises(ValueError):
            apply_refined_contact_impulses_to_lifted_momentum(
                state, 2, (0, 0), (-1,), (3,)
            )
        with self.assertRaises(ValueError):
            apply_refined_contact_impulses_to_lifted_momentum(
                state, 2, (0, 0), (1,), (0,)
            )
        with self.assertRaises(ValueError):
            apply_refined_contact_impulses_to_lifted_momentum(
                state, 2, (2, 0), (1,), (3,)
            )


if __name__ == "__main__":
    unittest.main()
