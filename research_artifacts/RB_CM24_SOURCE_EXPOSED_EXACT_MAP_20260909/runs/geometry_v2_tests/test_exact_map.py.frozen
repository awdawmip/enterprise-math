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
        # In dX/Y-phi, clear the actual denominators before cancelling w.
        d = self.data
        left = m.scale(m.multiply(self.W, m.add(d['t'], d['k']), d['t'], d['D0'], d['D0']), 2)
        for sign in (1, -1):
            with self.subTest(Y_multiplier=sign):
                # Squaring either Y sign multiplies the same LHS by sign^2.
                self.assertEqual(sign * sign, 1)
                right = m.scale(left, sign)
                difference = m.difference(left, right)
                if sign == 1:
                    self.assertEqual(difference, {})
                else:
                    self.assertEqual(difference, m.scale(left, 2))
                    self.assertTrue(difference)  # Rational difference is -2 phi.

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


if __name__ == '__main__':
    unittest.main()
