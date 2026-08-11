import unittest

from experiments.r028_retrospective_credit_calculus import (
    MODELS,
    core_exhaustive,
    meet,
    nested_regime_checks,
    pair_coverage_checks,
    raw_B,
    raw_M,
    refines,
    req_mask,
    cover_mask,
    shapley_values,
    support_bridge_checks,
    witness_search,
)


class R028CreditCalculusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w = witness_search()

    def test_basic_debt(self):
        e = (0, 0, 0)
        f = (0, 0, 1)
        self.assertEqual(raw_M(e, f), 2)
        self.assertEqual(raw_B(e, f), 1)
        self.assertFalse(refines(e, f))
        self.assertTrue(refines((0, 1, 2), f))

    def test_zero_debt_iff_refinement_small(self):
        for n in range(1, 5):
            for e in MODELS[n].ps:
                for f in MODELS[n].ps:
                    self.assertEqual(raw_M(e, f) == 1, refines(e, f))
                    self.assertEqual(raw_B(e, f) == 0, refines(e, f))

    def test_completion_iff_pair_cover(self):
        e = (0, 0, 0); f = (0, 0, 1); a = (0, 1, 0); b = (0, 1, 1)
        refined = meet(meet(e, a), b)
        self.assertTrue(refines(refined, f))
        self.assertEqual(cover_mask(e, f, a) | cover_mask(e, f, b), req_mask(e, f))

    def test_order_dependence_distinct_kernels(self):
        x = self.w["order_M"]
        self.assertEqual(x["n"], 3)
        self.assertEqual((x["marginal_at_empty"], x["marginal_after_other"]), (1, 0))

    def test_submodularity_killed_by_synergy(self):
        x = self.w["submod_M"]
        self.assertEqual(x["n"], 3)
        self.assertEqual((x["marginal_at_empty"], x["marginal_after_other"]), (0, 1))
        self.assertEqual(self.w["submod_B"]["n"], 3)

    def test_supermodularity_killed_by_redundancy(self):
        x = self.w["supermod_M"]
        self.assertEqual(x["n"], 3)
        self.assertEqual((x["marginal_at_empty"], x["marginal_after_other"]), (1, 0))
        self.assertEqual(self.w["supermod_B"]["n"], 3)

    def test_pair_coverage_not_debt_credit(self):
        x = self.w["pair_positive_debt_zero"]
        self.assertEqual(x["n"], 3)
        self.assertGreater(x["pair_coverage"], 0)
        self.assertEqual(x["M_before"], x["M_after"])
        self.assertEqual(x["B_before"], x["B_after"])

    def test_same_pair_count_different_debt(self):
        x = self.w["same_pair_count_different_debt"]
        self.assertEqual(x["n"], 5)
        self.assertEqual(x["credit_A"]["M"], 1)
        self.assertEqual(x["credit_B"]["M"], 0)

    def test_declared_vs_realized_hindsight_boundary(self):
        x = self.w["declared_realized_strict"]
        self.assertEqual(x["realized_pair_credit"], 0)
        self.assertEqual(x["declared_pair_credit"], 1)
        self.assertLess(x["M_realized"], x["M_declared"])

    def test_future_shrink_can_increase_individual_M_credit(self):
        x = self.w["future_shrink_individual_M"]
        self.assertEqual(x["n"], 4)
        self.assertLess(x["credit_before"], x["credit_after"])

    def test_future_shrink_can_increase_individual_B_credit(self):
        x = self.w["future_shrink_individual_B"]
        self.assertEqual(x["n"], 4)
        self.assertLess(x["credit_before"], x["credit_after"])

    def test_local_global_mismatch(self):
        x = self.w["local_positive_global_zero"]
        self.assertEqual(x["global_M_credit"], 0)
        self.assertTrue(any(v > 0 for v in x["local_credit"]))

    def test_shapley_symmetrizes_synergy_and_redundancy(self):
        syn = shapley_values((0,0,0), (0,0,1), [(0,1,0), (0,1,1)])
        red = shapley_values((0,0,0), (0,0,1), [(0,0,1), (0,1,2)])
        self.assertEqual(syn, ["1/2", "1/2"])
        self.assertEqual(red, ["1/2", "1/2"])

    def test_rewind_debt_order_mismatch_witnesses(self):
        a = self.w["same_B_different_rewind"]
        self.assertEqual(a["current_B_F1"], a["current_B_F2"])
        self.assertNotEqual(a["rewind_F1"], a["rewind_F2"])
        b = self.w["same_rewind_different_B"]
        self.assertEqual(b["rewind_F1"], b["rewind_F2"])
        self.assertNotEqual(b["current_B_F1"], b["current_B_F2"])

    def test_full_partition_core(self):
        x = core_exhaustive()
        self.assertEqual(x["status"], "PASS")
        self.assertEqual(x["ordered_EF"], 2959)
        self.assertEqual(x["single_feature_checks"], 144117)
        self.assertEqual(x["triple_family_checks_n_le_4"], 762533)

    def test_pair_coverage_submodular(self):
        self.assertEqual(pair_coverage_checks()["status"], "PASS")

    def test_nested_kernel_special_regime(self):
        self.assertEqual(nested_regime_checks()["status"], "PASS")

    def test_support_level_bridge(self):
        x = support_bridge_checks()
        self.assertEqual(x["status"], "PASS")
        self.assertTrue(x["boundary"]["point_signature_x_eq_y"])
        self.assertFalse(x["boundary"]["support_signature_A_eq_H"])

    def test_product_binary_target_still_synergistic(self):
        x = self.w["submod_product_binary_target"]
        self.assertEqual(x["n"], 4)
        self.assertEqual((x["M_marginal_at_empty"], x["M_marginal_after_A"]), (0, 1))
        self.assertEqual((x["B_marginal_at_empty"], x["B_marginal_after_A"]), (0, 1))

    def test_future_shrink_releases_pairs_and_total_debt(self):
        x = core_exhaustive()
        self.assertGreater(x["target_coarsening_checks"], 0)
        self.assertEqual(x["target_coarsening_checks"], x["pair_release_monotonicity_checks"])
        self.assertGreater(x["pair_credit_shrink_checks"], 900000)

    def test_exact_r022_eight_state_pareto_replay(self):
        x = self.w["eight_state_storage_rewind_pareto"]
        self.assertEqual(x["target"], "four-pairs (R022 E1)")
        self.assertEqual([(o["metadata_bits"], o["rewind"]) for o in x["options"]], [(0,2),(1,1),(2,0)])
        self.assertEqual(x["dominated_option"]["dominated_by"], "E1")


if __name__ == "__main__":
    unittest.main()
