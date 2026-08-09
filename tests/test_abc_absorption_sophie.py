import unittest

from enterprise_math.abc_absorption_sophie import sophie_germain_absorption_access


class AbcAbsorptionSophieTests(unittest.TestCase):
    def test_small_calibration_cases(self) -> None:
        q3 = sophie_germain_absorption_access(3)
        self.assertEqual((q3["eta_min"], q3["mu"], q3["nu"]), (1, 1, 1))
        self.assertEqual(q3["pareto_frontier"], ((1, 1),))

        q5 = sophie_germain_absorption_access(5)
        self.assertEqual((q5["eta_min"], q5["mu"], q5["nu"]), (1, 2, 2))
        self.assertEqual(q5["pareto_frontier"], ((2, 1),))

    def test_access_delay_grows_across_exact_working_examples(self) -> None:
        expected = {
            11: (2, 5, 3),
            23: (2, 11, 9),
            29: (2, 14, 12),
            41: (2, 20, 18),
        }
        for q, (mu, nu, delta) in expected.items():
            data = sophie_germain_absorption_access(q)
            self.assertEqual(data["eta_min"], 1)
            self.assertEqual(data["mu"], mu)
            self.assertEqual(data["nu"], nu)
            self.assertEqual(data["delta_abs"], delta)
            self.assertEqual(data["pareto_frontier"], ((2, 2), (nu, 1)))

    def test_floor_witness_is_exact(self) -> None:
        data = sophie_germain_absorption_access(23)
        x2, xq, xc = data["floor_witness_2_q_c"]
        self.assertEqual(23 * x2 + 2 * xq, 1)
        self.assertEqual(xc, 1)
        self.assertEqual(max(abs(x2), abs(xq), abs(xc)), 11)

    def test_non_sophie_input_rejected(self) -> None:
        with self.assertRaises(ValueError):
            sophie_germain_absorption_access(7)  # 15 is not prime.


if __name__ == "__main__":
    unittest.main()
