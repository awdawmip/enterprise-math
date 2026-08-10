import unittest

from enterprise_math.causal_3d_minimum_precision_candidates import (
    three_dimensional_candidate_verdicts,
    unique_passing_candidate,
)


class Causal3DMinimumPrecisionCandidateTests(unittest.TestCase):
    def test_fcc_is_unique_candidate_passing_local_and_global_contracts(self):
        verdicts = {verdict.name: verdict for verdict in three_dimensional_candidate_verdicts()}
        self.assertEqual(set(verdicts), {"SC", "BCC", "FCC", "HCP"})
        self.assertFalse(verdicts["SC"].passes_horizon_two_contract)
        self.assertFalse(verdicts["BCC"].passes_horizon_two_contract)
        self.assertTrue(verdicts["FCC"].passes_horizon_two_contract)
        self.assertFalse(verdicts["HCP"].passes_horizon_two_contract)

        self.assertFalse(verdicts["SC"].passes_global_one_state_reconstruction)
        self.assertFalse(verdicts["BCC"].passes_global_one_state_reconstruction)
        self.assertTrue(verdicts["FCC"].passes_global_one_state_reconstruction)
        self.assertFalse(verdicts["HCP"].passes_global_one_state_reconstruction)
        self.assertEqual(unique_passing_candidate(), "FCC")


if __name__ == "__main__":
    unittest.main()
