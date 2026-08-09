import unittest

from enterprise_math.causal_code_event_context import (
    e7_provenance_context_histogram,
    e8_provenance_context_histogram,
    local_context_forgets_provenance,
)
from enterprise_math.causal_code_lattice import extended_hamming_8_code
from enterprise_math.causal_code_root_shadow import simplex_7_code


class CausalCodeEventContextTests(unittest.TestCase):
    def test_e7_axis_and_glue_provenance_have_identical_local_relation_context(self):
        histogram = e7_provenance_context_histogram()
        expected_context = (32, 240, (32,), ((15, 32),))
        self.assertEqual(
            histogram,
            {
                ("axis", 32, expected_context): 14,
                ("glue", 32, expected_context): 112,
            },
        )
        self.assertTrue(local_context_forgets_provenance(simplex_7_code()))

    def test_e8_axis_and_glue_provenance_have_identical_local_relation_context(self):
        histogram = e8_provenance_context_histogram()
        expected_context = (56, 756, (56,), ((27, 56),))
        self.assertEqual(
            histogram,
            {
                ("axis", 56, expected_context): 16,
                ("glue", 56, expected_context): 224,
            },
        )
        self.assertTrue(local_context_forgets_provenance(extended_hamming_8_code()))


if __name__ == "__main__":
    unittest.main()
