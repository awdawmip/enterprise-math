"""Small distinct counterchecks for the pinned, source-exposed exact map."""
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from research_artifacts.RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909 import check_exact_map as m


class ExactMapCounterchecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        m.enforce_limits(json.loads(ROOT.joinpath(m.REL, 'execution_policy.json').read_bytes()))
        cls.data = m.formula()
        cls.remainder, cls.W = m.ode_residual(cls.data)

    def test_full_ode_and_no_critical_restriction(self):
        with patch.object(m.base, 'restrict_to_critical_divisor', side_effect=AssertionError('forbidden necessary-only reduction')):
            remainder, W = m.ode_residual(self.data)
        self.assertEqual(remainder, {})
        self.assertTrue(W)

    def test_fixed_k_sign_is_not_a_silent_symmetry(self):
        changed = dict(self.data, k=m.scale(self.data['k'], -1))
        self.assertTrue(m.ode_residual(changed)[0])

    def test_source_numerator_one_coefficient_change_rejected(self):
        changed = dict(self.data, N=m.add(self.data['N'], m.constant(1)))
        self.assertTrue(m.ode_residual(changed)[0])

    def test_wrong_ode_normalization_rejected(self):
        changed = dict(self.data, C4=m.scale(self.data['C4'], -1))
        self.assertTrue(m.ode_residual(changed)[0])

    def test_squared_equation_does_not_set_unsquared_y_sign(self):
        # The changed input is the actual numerator of Y/w, not a copied
        # common cross product.  Its square remains unchanged.
        d = self.data
        changed_Y_num = m.scale(self.W, -1)
        self.assertEqual(m.power(changed_Y_num, 2), m.power(self.W, 2))
        self.assertEqual(m.unsquared_input_residual(d, self.W), {})
        actual_difference = m.unsquared_input_residual(d, self.W, y_numerator=changed_Y_num)
        self.assertTrue(actual_difference)
        expected = m.scale(m.multiply(self.W, m.add(d['t'], d['k']), d['t'], d['D0'], d['D0']), 4)
        self.assertEqual(actual_difference, expected)

    def test_actual_y_missing_denominator_two_is_rejected(self):
        d = self.data
        changed_Y_den = m.multiply(m.add(d['t'], d['k']), d['D0'], d['D0'])
        self.assertTrue(m.unsquared_input_residual(d, self.W, y_denominator=changed_Y_den))

    def test_common_multiplier_is_not_a_degree_certificate(self):
        d = self.data
        rho = m.add(d['R'], m.constant(2))
        changed = dict(d, N=m.multiply(rho, d['N']), D0=m.multiply(rho, d['D0']))
        remainder, changed_W = m.ode_residual(changed)
        self.assertEqual(remainder, {})
        self.assertEqual(changed_W, m.multiply(rho, rho, self.W))
        self.assertEqual(m.evaluate(changed['D0'], m.constant(-2), m.multiply(d['i'], d['beta'])), {})
        self.assertTrue(m.evaluate(d['D0'], m.constant(-2), m.multiply(d['i'], d['beta'])))

    def test_exact_complex_and_real_generator_relations(self):
        d = self.data
        self.assertEqual(m.add(m.power(d['alpha'], 4), m.constant(-3)), {})
        self.assertEqual(m.add(m.power(d['beta'], 2), m.constant(-2)), {})
        self.assertEqual(m.add(m.power(d['i'], 2), m.constant(1)), {})
        self.assertEqual(m.add(m.power(d['i'], 2), m.constant(-1)), m.constant(-2))

    def test_strict_integer_and_symbol_carriers(self):
        with self.assertRaises(TypeError):
            m.constant(True)
        with self.assertRaises(TypeError):
            m.scale(self.data['N'], '1')
        invalid = list(m.base.ZERO_MONOMIAL)
        invalid[0] = -1
        with self.assertRaises(TypeError):
            m.normalize({tuple(invalid): 1})
        with self.assertRaises(TypeError):
            m.normalize(m.base.variable(8))  # Legacy free k is not frozen k.

    def test_geometry_identity_and_exact_nonzero_inputs(self):
        value = m.geometry_checkpoint(self.data, self.W)
        self.assertTrue(all(not r for r in value['identities'].values()))
        self.assertTrue(all(value['field_nonzero_witnesses'].values()))
        self.assertEqual(value['N_zero_orders_on_C'], {'Pplus': 1, 'Pminus': 1, 'Tminus': 1, 'B0': 1, 'Z': 2})

    def test_full_fibers_and_L_rational_square_class_reconstruction(self):
        value = m.special_fiber_checkpoint(self.data, self.W)
        placement = value['placement_checkpoint']
        self.assertTrue(all(value['nonzero_witnesses'].values()))
        self.assertEqual(placement['geometric_twist_triple_for_Xnew'], ['Tplus', 'T0', 'Tminus'])
        for row in placement['L_rational_square_class_representatives_for_Xnew'].values():
            self.assertEqual(row['cleared_reconstruction_remainder'], [])
            self.assertTrue(row['u_numerator'] and row['u_denominator'])
        binding = m.matching_classification_entry(ROOT)
        self.assertEqual(binding['historical_row']['infinity_empty_representative'], [1, 2, 2, 1, 1, 1])

    def test_a_repeated_fiber_point_is_rejected(self):
        polynomial = m.power(m.add(self.data['R'], m.constant(1)), 2)
        with self.assertRaisesRegex(AssertionError, 'common root'):
            m.coprime_R_witness(polynomial, m.R_derivative(polynomial))

    def test_nonmonic_formal_quotient_preserves_integer_content(self):
        R = self.data['R']
        divisor = m.add(m.scale(R, 2), m.constant(1))
        q = m.add(m.power(R, 2), R, m.constant(3))
        dividend = m.add(m.multiply(divisor, q), m.constant(5))
        multiplier, actual_q, remainder = m.pseudo_quotient_R(dividend, divisor)
        self.assertEqual(multiplier, m.constant(8))
        self.assertEqual(actual_q, m.scale(q, 8))
        self.assertEqual(remainder, m.constant(40))


if __name__ == '__main__':
    unittest.main()
