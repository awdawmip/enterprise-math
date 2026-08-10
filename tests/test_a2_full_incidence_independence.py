import unittest
from itertools import product

from enterprise_math.a2_full_incidence import (
    full_incidence_independent,
    full_independence_repair_formula,
    subset_joint_partition,
)
from enterprise_math.a2_precision_incidence import (
    directed_repair_depth,
    directed_repair_factor,
    directed_repair_spectrum,
    symmetric_repair_distance,
)


class A2FullIncidenceIndependenceTests(unittest.TestCase):
    def test_heterogeneous_full_product_repair_formula(self):
        for radices in ((2, 3), (2, 3, 4), (3, 2, 5)):
            states = tuple(product(*[range(r) for r in radices]))
            family = [
                {state: state[index] for state in states}
                for index in range(len(radices))
            ]
            self.assertTrue(full_incidence_independent(states, family))
            m = len(radices)
            for mask_s in range(1 << m):
                known = {i for i in range(m) if mask_s & (1 << i)}
                for mask_t in range(1 << m):
                    added = {i for i in range(m) if mask_t & (1 << i)}
                    data = full_independence_repair_formula(
                        states, family, known, added
                    )
                    expected = 1
                    for index in added - known:
                        expected *= radices[index]
                    self.assertEqual(data["actual"], expected)

    def test_binary_full_product_is_exact_hamming_geometry(self):
        for m in range(1, 6):
            states = tuple(product((0, 1), repeat=m))
            family = [
                {state: state[index] for state in states}
                for index in range(m)
            ]
            for mask_s in range(1 << m):
                known = {i for i in range(m) if mask_s & (1 << i)}
                e_s = subset_joint_partition(states, family, known)
                for mask_t in range(1 << m):
                    added = {i for i in range(m) if mask_t & (1 << i)}
                    e_t = subset_joint_partition(states, family, added)
                    self.assertEqual(
                        directed_repair_factor(states, e_s, e_t),
                        2 ** len(added - known),
                    )
                    self.assertEqual(
                        directed_repair_depth(states, e_s, e_t, 2),
                        len(added - known),
                    )
                    self.assertEqual(
                        symmetric_repair_distance(states, e_s, e_t, 2),
                        len(known ^ added),
                    )

    def test_uniform_directed_repair_spectrum(self):
        states = tuple(product((0, 1), repeat=4))
        family = [
            {state: state[index] for state in states}
            for index in range(4)
        ]
        known = subset_joint_partition(states, family, (0, 1))
        added = subset_joint_partition(states, family, (1, 2, 3))
        self.assertEqual(directed_repair_spectrum(states, known, added), (16, 24, 16, 4))


if __name__ == "__main__":
    unittest.main()
