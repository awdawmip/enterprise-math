import unittest

from enterprise_math.problem_legitimacy import (
    analyze_signature,
    coarsest_static_repair,
    equivalence_failure_witness,
    finite_signature_basis,
    joint_signature_partition,
    partitions_equivalent,
    semantic_erasure_report,
    signature_descends,
)


class ProblemLegitimacyTests(unittest.TestCase):
    def test_signature_descent_and_repair(self):
        states = (0, 1, 2, 3)
        coarse = {0: "a", 1: "a", 2: "b", 3: "b"}
        good = {0: 0, 1: 0, 2: 1, 3: 1}
        bad = {0: 0, 1: 1, 2: 1, 3: 1}

        self.assertTrue(signature_descends(states, coarse, good))
        self.assertFalse(signature_descends(states, coarse, bad))

        repair = coarsest_static_repair(states, coarse, bad)
        self.assertEqual(len(set(repair.values())), 3)

        report = analyze_signature(states, coarse, bad)
        self.assertFalse(report.valid_now)
        self.assertIsNotNone(report.witness)
        self.assertEqual(report.current_class_count, 2)
        self.assertEqual(report.required_class_count, 3)

    def test_semantic_erasure_certificate(self):
        states = (0, 1, 2, 3)
        rich = {state: state for state in states}
        lossless = {state: (state // 2, state % 2) for state in states}
        lossy = {state: state % 2 for state in states}

        report = semantic_erasure_report(states, rich, lossless)
        self.assertTrue(report.lossless)
        self.assertIsNone(report.witness)

        report = semantic_erasure_report(states, rich, lossy)
        self.assertFalse(report.lossless)
        self.assertIsNotNone(report.witness)
        left, right = report.witness
        self.assertEqual(lossy[left], lossy[right])
        self.assertNotEqual(rich[left], rich[right])

    def test_erasure_must_be_post_summary(self):
        states = (0, 1, 2)
        rich = {0: 0, 1: 0, 2: 1}
        refining = {0: 0, 1: 1, 2: 2}
        with self.assertRaises(ValueError):
            semantic_erasure_report(states, rich, refining)

    def test_joint_signature_partition(self):
        states = tuple(range(8))
        signatures = {
            "b0": {state: state & 1 for state in states},
            "b1": {state: (state >> 1) & 1 for state in states},
            "b2": {state: (state >> 2) & 1 for state in states},
        }
        partition = joint_signature_partition(states, signatures)
        self.assertEqual(len(set(partition.values())), 8)

    def test_finite_signature_basis_bound(self):
        states = tuple(range(8))
        signatures = {
            "b0": {state: state & 1 for state in states},
            "b1": {state: (state >> 1) & 1 for state in states},
            "b2": {state: (state >> 2) & 1 for state in states},
            "parity": {state: state.bit_count() % 2 for state in states},
            "dup": {state: state & 1 for state in states},
        }
        full = joint_signature_partition(states, signatures)
        basis = finite_signature_basis(states, signatures)
        selected = {name: signatures[name] for name in basis.names}
        reduced = joint_signature_partition(states, selected)
        self.assertTrue(partitions_equivalent(states, full, reduced))
        self.assertLessEqual(len(basis.names), basis.final_class_count - 1)

    def test_uniform_tolerance_is_not_equivalence_on_chain(self):
        states = (0, 1, 2)
        failure = equivalence_failure_witness(
            states, lambda x, y: abs(x - y) <= 1
        )
        self.assertIsNotNone(failure)
        self.assertEqual(failure.law, "transitivity")
        self.assertEqual(failure.witness, (0, 1, 2))

    def test_exact_equality_is_equivalence(self):
        states = (0, 1, 2)
        self.assertIsNone(equivalence_failure_witness(states, lambda x, y: x == y))


if __name__ == "__main__":
    unittest.main()
