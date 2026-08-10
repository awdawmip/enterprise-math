import unittest

from enterprise_math.precision_suffix_certificate_compiler import (
    erasure_failure_witness,
    erasure_safe,
    suffix_partitions,
)


class SuffixCertificateCompilerTests(unittest.TestCase):
    def test_count_can_demote_to_may_after_last_exact_use(self):
        # Certificate states are counts 0,1,2.  Before the last exact-count use the
        # certificate must stay discrete; afterwards only zero/nonzero matters.
        identity = (0, 1, 2)
        exact = (0, 1, 2)
        may = (0, 1, 1)
        parts = suffix_partitions((identity,), (exact, may))
        self.assertEqual(parts[0], ((0,), (1,), (2,)))
        self.assertEqual(parts[1], ((0,), (1, 2)))

    def test_candidate_erasure_safe_iff_it_refines_suffix_partition(self):
        identity = (0, 1, 2)
        may = (0, 1, 1)
        parts = suffix_partitions((identity,), (may, may))
        self.assertTrue(erasure_safe(((0,), (1, 2)), parts[0]))
        self.assertFalse(erasure_safe(((0, 1), (2,)), parts[0]))

    def test_failure_witness_is_exact(self):
        suffix = ((0,), (1, 2))
        erasure = ((0, 1), (2,))
        witness = erasure_failure_witness(erasure, suffix)
        self.assertIn(witness, ((0, 1), (1, 0)))

    def test_backward_pullback_keeps_future_distinction(self):
        # Current observation sees nothing, but the stage maps 0 differently from 1/2
        # into a future observable split.
        f = (0, 1, 1)
        now = (0, 0, 0)
        future = (0, 1, 1)
        parts = suffix_partitions((f,), (now, future))
        self.assertEqual(parts[0], ((0,), (1, 2)))

    def test_constant_future_allows_universal_certificate(self):
        f = (2, 2, 2)
        now = (0, 0, 0)
        future = (0, 1, 2)
        parts = suffix_partitions((f,), (now, future))
        self.assertEqual(parts[0], ((0, 1, 2),))


if __name__ == "__main__":
    unittest.main()
