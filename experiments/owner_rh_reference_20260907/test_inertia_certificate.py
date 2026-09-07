"""Independent exact constructions and adversarial interval-certificate tests."""

import copy
from fractions import Fraction as F
import hashlib
from itertools import product
import json
import random
import unittest
from unittest.mock import patch

import inertia_certificate as ic


def point(matrix):
    return [[{"lo": F(v), "hi": F(v)} for v in row] for row in matrix]


def labels(n):
    return [{"branch": "O-" if i % 2 == 0 else "S+", "k": i + 1,
             "endpoints": {"a": "log(1/2)", "b": "log(1)"}} for i in range(n)]


def multiply(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


class InertiaCertificateTests(unittest.TestCase):
    def check_count(self, matrix, count):
        bounds, tags = point(matrix), labels(len(matrix))
        certificate = ic.certify_interval_inertia(bounds, tags)
        result = ic.verify_interval_inertia(bounds, tags, certificate)
        self.assertEqual(result["status"], "CERTIFIED")
        self.assertEqual(result["negative_count"], count)
        self.assertEqual(result["negative_count_bounds"], [count, count])
        self.assertTrue(result["verification_complete"])
        self.assertEqual(result["scope"], "INPUT_INTERVAL_FAMILY_ONLY")
        return certificate

    def test_zero_diagonal_indefinite_two_by_two(self):
        certificate = self.check_count([[0, 1], [1, 0]], 1)
        self.assertTrue(any(b["size"] == 2 for b in certificate["minus"]["blocks"]))
        self.assertEqual(certificate["minus"]["inertia"], {"negative": 1, "zero": 0, "positive": 1})

    def test_singular_zero_and_nonnegative_are_not_positive_definite(self):
        zero = self.check_count([[0, 0], [0, 0]], 0)
        self.assertEqual(zero["minus"]["inertia"]["zero"], 2)
        rank_one = self.check_count([[1, 1], [1, 1]], 0)
        self.assertEqual(rank_one["minus"]["inertia"]["zero"], 1)
        self.check_count([[-2, 0], [0, 0]], 1)

    def test_later_permutation_and_two_by_two_pivot(self):
        # A 1x1 pivot is found at index 2, then the remaining saddle needs 2x2.
        certificate = self.check_count([[0, 3, 0], [3, 0, 0], [0, 0, 2]], 1)
        self.assertNotEqual(certificate["minus"]["permutation"], [0, 1, 2])
        self.assertEqual([b["size"] for b in certificate["minus"]["blocks"]], [1, 2])
        # After the first pivot the next usable diagonal is moved over a zero.
        self.check_count([[2, 2, 2], [2, 2, 2], [2, 2, 5]], 0)

    def test_crossing_zero_is_undetermined(self):
        bounds = [[{"lo": "-1/1", "hi": "1/1"}]]
        certificate = ic.certify(bounds, ["axis"])
        result = ic.verify(bounds, ["axis"], certificate)
        self.assertEqual(result["status"], "UNDETERMINED")
        self.assertIsNone(result["negative_count"])
        self.assertEqual(result["negative_count_bounds"], [0, 1])
        self.assertTrue(result["verification_complete"])

    def test_nonzero_interval_family_with_independent_two_by_two_check(self):
        bounds = [[{"lo": F(3), "hi": F(4)}, {"lo": F(1, 5), "hi": F(2, 5)}],
                  [{"lo": F(1, 5), "hi": F(2, 5)}, {"lo": F(-4), "hi": F(-3)}]]
        certificate = ic.certify(bounds, labels(2))
        self.assertEqual(certificate["delta"], "3/5")
        self.assertEqual(ic.verify(bounds, labels(2), certificate)["negative_count"], 1)
        # At all rational corners, and indeed throughout these sign-separated
        # diagonal intervals, determinant a*d-b^2 is strictly negative.
        for a, b, d in product((F(3), F(4)), (F(1, 5), F(2, 5)), (F(-4), F(-3))):
            self.assertLess(a * d - b * b, 0)

    def test_input_validation(self):
        malformed = [
            [], [[{"lo": 0, "hi": 1}, {"lo": 0, "hi": 0}]],
            [[{"lo": 2, "hi": 1}]], [[{"lo": 0.0, "hi": 1}]],
            [[{"lo": False, "hi": 1}]], [[{"lo": "2/4", "hi": "1/1"}]],
            [[{"lo": "0", "hi": "1/1"}]], [[{"lo": "-0/1", "hi": "1/1"}]],
            [[{"lo": "0/1", "hi": "1/-2"}]], [[{"lo": "0/1", "hi": "NaN"}]],
            [[{"lo": 0, "hi": 1, "trusted": True}]],
            [[{"lo": 0, "hi": 1}, {"lo": 0, "hi": 0}],
             [{"lo": 0, "hi": 1}, {"lo": 0, "hi": 1}]],
        ]
        for bounds in malformed:
            with self.subTest(bounds=bounds):
                with self.assertRaises(ic.InvalidInput):
                    ic.certify(bounds, labels(len(bounds)))

    def test_label_types_distinctness_and_order_binding(self):
        bounds = point([[2, 0], [0, -3]])
        for tags in (["a"], ["a", "a"], [0.5, "b"], [{1: "bad"}, "b"]):
            with self.subTest(tags=tags), self.assertRaises(ic.InvalidInput):
                ic.certify(bounds, tags)
        tags = [{"b": [None, True, 3], "a": "x"}, {"a": "y", "b": False}]
        certificate = ic.certify(bounds, tags)
        reordered_keys = [{"a": "x", "b": [None, True, 3]}, {"b": False, "a": "y"}]
        self.assertEqual(ic.verify(bounds, reordered_keys, certificate)["status"], "CERTIFIED")
        self.assertEqual(ic.verify(bounds, tags[::-1], certificate)["status"], "INVALID_CERTIFICATE")

    def test_bounds_binding_and_semantically_equal_rationals(self):
        bounds = point([[2, F(1, 3)], [F(1, 3), -2]])
        tags = labels(2)
        certificate = ic.certify(bounds, tags)
        as_strings = [[{k: f"{v.numerator}/{v.denominator}" for k, v in item.items()}
                       for item in row] for row in bounds]
        self.assertEqual(ic.verify(as_strings, tags, certificate)["status"], "CERTIFIED")
        changed = point([[3, F(1, 3)], [F(1, 3), -2]])
        self.assertEqual(ic.verify(changed, tags, certificate)["status"], "INVALID_CERTIFICATE")
        # Even a correctly recomputed binding hash cannot fix false witnesses.
        certificate["input_sha256"] = ic.certify(changed, tags)["input_sha256"]
        self.assertEqual(ic.verify(changed, tags, certificate)["status"], "INVALID_CERTIFICATE")

    def test_tampered_witnesses_and_reported_status(self):
        bounds = point([[2, 1], [1, -3]])
        tags = labels(2)
        baseline = ic.certify(bounds, tags)
        mutations = [
            lambda c: c["minus"]["L"][1].__setitem__(0, "4/1"),
            lambda c: c["minus"]["L"][0].__setitem__(1, "1/1"),
            lambda c: c["minus"]["L"][0].__setitem__(0, "2/1"),
            lambda c: c["minus"]["blocks"][0]["D"][0].__setitem__(0, "5/1"),
            lambda c: c["minus"]["permutation"].__setitem__(1, 0),
            lambda c: c["minus"]["permutation"].__setitem__(0, False),
            lambda c: c["minus"]["blocks"].pop(),
            lambda c: c["minus"]["blocks"][0].__setitem__("start", 1),
            lambda c: c["minus"]["inertia"].__setitem__("negative", 0),
            lambda c: c["minus"]["inertia"].__setitem__("negative", True),
            lambda c: c.__setitem__("delta", "1/1"),
            lambda c: c.__setitem__("status", "UNDETERMINED"),
            lambda c: c.__setitem__("negative_count", False),
            lambda c: c.__setitem__("schema", "self_reported_truth"),
        ]
        for mutate in mutations:
            altered = copy.deepcopy(baseline)
            mutate(altered)
            self.assertEqual(ic.verify(bounds, tags, altered)["status"], "INVALID_CERTIFICATE")

    def test_two_by_two_block_tamper(self):
        bounds, tags = point([[0, 1], [1, 0]]), labels(2)
        certificate = ic.certify(bounds, tags)
        certificate["plus"]["blocks"][0]["D"][0][1] = "2/1"
        self.assertEqual(ic.verify(bounds, tags, certificate)["status"], "INVALID_CERTIFICATE")

    def test_verifier_does_not_reexecute_elimination(self):
        bounds, tags = point([[0, 2], [2, 0]]), labels(2)
        certificate = ic.certify(bounds, tags)
        with patch.object(ic, "_congruence", side_effect=AssertionError("not an independent verifier")):
            result = ic.verify(bounds, tags, json.loads(json.dumps(certificate)))
        self.assertEqual(result["status"], "CERTIFIED")

    def test_exact_random_congruence_oracle(self):
        rng = random.Random(20260907)
        for trial in range(96):
            n = 1 + trial % 8
            lower = [[F(int(i == j)) if j >= i else F(rng.randint(-4, 4), rng.randint(1, 5))
                      for j in range(n)] for i in range(n)]
            diagonal = [[F(0) for _ in range(n)] for _ in range(n)]
            expected_negative = 0
            index = 0
            while index < n:
                if index + 1 < n and rng.randrange(3) == 0:
                    off = F(rng.choice((-3, -1, 1, 2)), rng.randint(1, 5))
                    diagonal[index][index + 1] = diagonal[index + 1][index] = off
                    expected_negative += 1
                    index += 2
                else:
                    value = F(rng.randint(-3, 3), rng.randint(1, 5))
                    diagonal[index][index] = value
                    expected_negative += int(value < 0)
                    index += 1
            constructed = multiply(multiply(lower, diagonal), transpose(lower))
            permutation = list(range(n))
            rng.shuffle(permutation)
            permuted = [[constructed[permutation[i]][permutation[j]] for j in range(n)] for i in range(n)]
            with self.subTest(trial=trial, dimension=n):
                self.check_count(permuted, expected_negative)

    def test_high_precision_rationals_and_32_dimension(self):
        # Independent diagonal congruence oracle; 32 rows matches N8 payload size.
        n = 32
        diagonal = [[F(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            diagonal[i][i] = F((-1 if i < 11 else 1) * (2**180 + i + 1), 2**191)
        self.check_count(diagonal, 11)

    def test_budget_exhaustion_is_not_invalid_or_a_mathematical_decision(self):
        bounds, tags = point([[1, 0], [0, -1]]), labels(2)
        certificate = ic.certify(bounds, tags)
        with self.assertRaises(ic.ComputationBudgetExceeded):
            ic.certify(bounds, tags, max_dimension=1)
        result = ic.verify(bounds, tags, certificate, max_dimension=1)
        self.assertEqual(result["status"], "UNDETERMINED")
        self.assertFalse(result["verification_complete"])
        self.assertIsNone(result["negative_count_bounds"])
        self.assertIn("budget incomplete", result["reason"])

    def test_large_rational_serialization_without_global_integer_setting(self):
        # More than Python's default 4300 decimal-digit conversion limit.
        huge = 10**4500 + 1
        certificate = self.check_count([[F(-huge, 7)]], 1)
        self.assertGreater(len(certificate["minus"]["blocks"][0]["D"][0][0]), 4300)


if __name__ == "__main__":
    unittest.main()
