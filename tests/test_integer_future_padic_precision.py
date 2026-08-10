import itertools
import unittest

from enterprise_math.integer_future_modular_precision import (
    modular_smith_precision_report,
)
from enterprise_math.integer_future_padic_precision import (
    p_adic_valuation,
    prime_power_precision_ladder,
    prime_power_smith_precision,
)


class IntegerFuturePadicPrecisionTests(unittest.TestCase):
    def test_scalar_p_power_factor_is_invisible_then_reveals_one_digit_per_level(self):
        # d=12 has v_2(d)=2.  Mod 2 and mod 4 the scalar is completely hidden;
        # from mod 8 onward each extra 2-adic level adds one observable bit.
        ladder = prime_power_precision_ladder(((12,),), 2, 6)
        self.assertEqual(
            tuple(step.smith_p_adic_valuations for step in ladder),
            ((2,),) * 6,
        )
        self.assertEqual(
            tuple(step.kernel_exponent for step in ladder),
            (1, 2, 2, 2, 2, 2),
        )
        self.assertEqual(
            tuple(step.observable_phase_exponent for step in ladder),
            (0, 0, 1, 2, 3, 4),
        )
        self.assertEqual(
            tuple(step.kernel_size for step in ladder),
            (2, 4, 4, 4, 4, 4),
        )

    def test_free_hidden_direction_keeps_growing_while_finite_torsion_saturates(self):
        finite = prime_power_precision_ladder(((4,),), 2, 5)
        free = prime_power_precision_ladder(((1, 0),), 2, 5)

        self.assertEqual(
            tuple(step.kernel_exponent for step in finite),
            (1, 2, 2, 2, 2),
        )
        self.assertEqual(
            tuple(step.kernel_exponent for step in free),
            (1, 2, 3, 4, 5),
        )
        self.assertEqual(
            tuple(step.hidden_free_rank for step in free),
            (1,) * 5,
        )

    def test_prime_power_report_matches_general_modular_smith_formula_on_small_matrices(self):
        matrices = (
            ((2, 0), (0, 3)),
            ((1, 1), (1, -1)),
            ((4, 2),),
            ((1, 0, 0),),
        )
        for matrix in matrices:
            for prime in (2, 3, 5):
                for exponent in range(1, 5):
                    padic = prime_power_smith_precision(
                        matrix,
                        prime,
                        exponent,
                    )
                    modular = modular_smith_precision_report(
                        matrix,
                        prime ** exponent,
                    )
                    self.assertEqual(padic.kernel_size, modular.kernel_size)
                    self.assertEqual(
                        padic.observable_phase_count,
                        modular.image_size,
                    )
                    self.assertEqual(
                        padic.kernel_exponent + padic.observable_phase_exponent,
                        exponent * padic.state_dimension,
                    )

    def test_three_pair_ledger_has_one_persistent_mod_two_torsion_factor(self):
        pair_rows = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
        )
        ladder = prime_power_precision_ladder(pair_rows, 2, 5)
        self.assertEqual(ladder[0].smith_factors, (1, 1, 1, 2))
        self.assertEqual(
            tuple(step.kernel_exponent for step in ladder),
            (1, 1, 1, 1, 1),
        )
        self.assertEqual(
            tuple(step.observable_phase_exponent for step in ladder),
            (3, 7, 11, 15, 19),
        )
        self.assertEqual(
            tuple(step.kernel_size for step in ladder),
            (2, 2, 2, 2, 2),
        )

    def test_unimodular_ttl_observation_is_injective_at_every_prime_power_level(self):
        ttl = (
            (1, 1, 1),
            (1, 1, 0),
            (1, 0, 0),
        )
        for prime in (2, 3, 5, 7):
            ladder = prime_power_precision_ladder(ttl, prime, 5)
            for step in ladder:
                self.assertEqual(step.hidden_free_rank, 0)
                self.assertEqual(step.smith_factors, (1, 1, 1))
                self.assertEqual(step.kernel_exponent, 0)
                self.assertEqual(step.kernel_size, 1)
                self.assertTrue(step.fully_modularly_injective)

    def test_p_adic_valuation(self):
        self.assertEqual(p_adic_valuation(72, 2), 3)
        self.assertEqual(p_adic_valuation(-81, 3), 4)
        self.assertEqual(p_adic_valuation(35, 2), 0)

    def test_validation(self):
        with self.assertRaises(ValueError):
            p_adic_valuation(0, 2)
        with self.assertRaises(ValueError):
            p_adic_valuation(4, 4)
        with self.assertRaises(ValueError):
            prime_power_smith_precision(((1,),), 1, 1)
        with self.assertRaises(ValueError):
            prime_power_smith_precision(((1,),), 2, 0)
        with self.assertRaises(TypeError):
            prime_power_smith_precision(((1,),), False, 1)


if __name__ == "__main__":
    unittest.main()
