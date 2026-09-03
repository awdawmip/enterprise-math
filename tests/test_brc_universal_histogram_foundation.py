from fractions import Fraction
import unittest

from enterprise_math.brc_histogram import (
    LeadingPair,
    WeightHistogram,
    dominant_degeneracy_error_bound,
    histogram_recoalesce,
    histogram_serial,
    leading_recoalesce,
    leading_serial,
    power_sum_root_polynomial,
    weight_histogram,
)
from enterprise_math.brc_moment_transfer import (
    equal_loop_moment_critical_z,
    finite_moment_signature,
    moment_matrix_power,
    moment_port_kernel_at_z,
    moment_star_at_z,
    moment_transition_matrix,
    moment_walk_series_coefficients,
)

Q = Fraction


class HistogramFoundationTests(unittest.TestCase):
    def test_histogram_readouts_and_semiring(self) -> None:
        left = weight_histogram([Q(1), Q(1), Q(1, 4)])
        right = weight_histogram([Q(1, 2), Q(1, 4)])
        self.assertEqual(left.count, 3)
        self.assertEqual(left.total_mass, Q(9, 4))
        self.assertEqual(left.dominant_mass, Q(1))
        self.assertEqual(left.dominant_degeneracy, 2)
        self.assertEqual(left.moment(2), Q(33, 16))

        union = histogram_recoalesce(left, right)
        serial = histogram_serial(left, right)
        for order in range(5):
            self.assertEqual(union.moment(order), left.moment(order) + right.moment(order))
            self.assertEqual(serial.moment(order), left.moment(order) * right.moment(order))
        self.assertEqual(
            serial.leading_pair,
            leading_serial(left.leading_pair, right.leading_pair),
        )
        self.assertEqual(
            union.leading_pair,
            leading_recoalesce(left.leading_pair, right.leading_pair),
        )

    def test_cwm_collision_exposes_dominant_degeneracy(self) -> None:
        a = weight_histogram([Q(1), Q(1), Q(1, 4), Q(1, 4)])
        b = weight_histogram([Q(1), Q(1, 2), Q(1, 2), Q(1, 2)])
        self.assertEqual((a.count, a.total_mass, a.dominant_mass), (4, Q(5, 2), Q(1)))
        self.assertEqual((b.count, b.total_mass, b.dominant_mass), (4, Q(5, 2), Q(1)))
        self.assertEqual(a.leading_pair, LeadingPair(Q(1), 2))
        self.assertEqual(b.leading_pair, LeadingPair(Q(1), 1))

    def test_dominant_degeneracy_bound(self) -> None:
        histogram = weight_histogram([Q(1), Q(1), Q(1, 2), Q(1, 4)])
        for order in range(8):
            excess, bound = dominant_degeneracy_error_bound(histogram, order)
            self.assertGreaterEqual(excess, 0)
            self.assertLessEqual(excess, bound)
        excess, bound = dominant_degeneracy_error_bound(weight_histogram([Q(2), Q(2)]), 7)
        self.assertEqual((excess, bound), (Q(0), Q(0)))

    def test_prime_terms_and_newton_root_polynomial(self) -> None:
        histogram = weight_histogram([Q(1, 2), Q(2, 3), Q(3, 5)])
        terms = histogram.prime_valuation_terms()
        self.assertEqual(len(terms), 3)
        moments = [histogram.moment(order) for order in range(1, 4)]
        coefficients = power_sum_root_polynomial(3, moments)
        # Product (t-1/2)(t-2/3)(t-3/5).
        self.assertEqual(coefficients, (Q(1), Q(-53, 30), Q(31, 30), Q(-1, 5)))

    def test_typed_inputs_reject_bool(self) -> None:
        with self.assertRaises(TypeError):
            weight_histogram([True])
        with self.assertRaises(TypeError):
            WeightHistogram.from_counts({Q(1): True})
        with self.assertRaises(TypeError):
            power_sum_root_polynomial(1, [True])


class MomentTransferFoundationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.edges = (
            (0, 1, Q(1, 2)),
            (0, 1, Q(1, 3)),
            (1, 0, Q(2, 3)),
            (1, 1, Q(1, 4)),
        )

    def test_moment_matrix_and_powers(self) -> None:
        w0 = moment_transition_matrix(2, self.edges, 0)
        w1 = moment_transition_matrix(2, self.edges, 1)
        self.assertEqual(w0, ((Q(0), Q(2)), (Q(1), Q(1))))
        self.assertEqual(w1, ((Q(0), Q(5, 6)), (Q(2, 3), Q(1, 4))))
        coefficients = moment_walk_series_coefficients(2, self.edges, 1, 4)
        self.assertEqual(coefficients[3], moment_matrix_power(w1, 3))

    def test_finite_moment_signature(self) -> None:
        signature = finite_moment_signature(2, self.edges)
        self.assertEqual(signature.max_parallel_multiplicity, 2)
        self.assertEqual(len(signature.matrices), 3)
        self.assertEqual(signature.matrices[0], moment_transition_matrix(2, self.edges, 0))
        self.assertEqual(signature.matrices[2], moment_transition_matrix(2, self.edges, 2))

    def test_length_aware_port_kernel(self) -> None:
        # 0 is hidden, 1 is the retained port.  Hidden self-loop 1/2,
        # port->hidden 1/3, hidden->port 1/4, direct port loop 1/5.
        matrix = (
            (Q(1, 2), Q(1, 4)),
            (Q(1, 3), Q(1, 5)),
        )
        z = Q(1, 2)
        kernel = moment_port_kernel_at_z(matrix, [0], z)
        expected = z * Q(1, 5) + z * z * Q(1, 3) * (Q(1) / (Q(1) - z * Q(1, 2))) * Q(1, 4)
        self.assertEqual(kernel, ((expected,),))
        full_star = moment_star_at_z(matrix, z)
        reduced_star = moment_star_at_z(kernel, Q(1))
        self.assertEqual(full_star[1][1], reduced_star[0][0])

    def test_equal_loop_critical_law(self) -> None:
        self.assertEqual(equal_loop_moment_critical_z(2, Q(3, 5), 1), Q(5, 6))
        self.assertEqual(equal_loop_moment_critical_z(2, Q(3, 5), 2), Q(25, 18))

    def test_typed_inputs_reject_bool(self) -> None:
        with self.assertRaises(TypeError):
            moment_transition_matrix(2, [(0, 1, True)], 1)
        with self.assertRaises(TypeError):
            moment_star_at_z(((Q(0),),), True)


if __name__ == "__main__":
    unittest.main()
