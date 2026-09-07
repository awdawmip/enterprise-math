from __future__ import annotations

import unittest

from enterprise_math.brc_multiplier_priority_jump import (
    prioritized_odd_multiplier_order,
)
from enterprise_math.brc_opportunistic_shortcuts import (
    LEARNED_COVER_PREFIX,
    RATIO_COVER_PREFIX,
    SQUAREFREE_KERNEL13,
    ShortcutContext,
    ShortcutLedger,
    RegimeShortcutLedger,
    flatten_probe_batches,
    multiplier_probe_batches,
    low12_compact_raw_table_bytes,
    passes_low12_compact_square_filter,
    regime_key,
    gap_sorted_order_from_materialized_states,
    brc_shadow_signature,
    adaptive_trial_plan,
    kernel13_order,
    kernel13_prefix,
    learned_cover_order,
    opportunistic_trial_plan,
    ratio_cover_order,
    squarefree_kernel,
)


class BRCOpportunisticShortcutTests(unittest.TestCase):
    def test_specialist_orders_preserve_complete_structural_set(self) -> None:
        baseline = prioritized_odd_multiplier_order(100)
        for order in (learned_cover_order(100), ratio_cover_order(100)):
            self.assertEqual(set(order), set(baseline))
            self.assertEqual(len(order), len(baseline))
            self.assertEqual(order[0], 1)

    def test_preserved_prefixes_remain_exactly_as_recorded(self) -> None:
        self.assertEqual(learned_cover_order(100)[:20], LEARNED_COVER_PREFIX)
        self.assertEqual(ratio_cover_order(100)[:20], RATIO_COVER_PREFIX)

    def test_kernel13_prefix_matches_historical_probe_size(self) -> None:
        prefix = kernel13_prefix(1000)
        self.assertEqual(len(prefix), 98)
        selected = set(SQUAREFREE_KERNEL13)
        self.assertTrue(prefix)
        self.assertTrue(all(squarefree_kernel(m) in selected for m in prefix))

        full = prioritized_odd_multiplier_order(1000)
        complete = kernel13_order(1000)
        self.assertEqual(set(complete), set(full))
        self.assertEqual(len(complete), len(full))

    def test_squarefree_kernel_examples(self) -> None:
        self.assertEqual(squarefree_kernel(1), 1)
        self.assertEqual(squarefree_kernel(12), 3)
        self.assertEqual(squarefree_kernel(72), 2)
        self.assertEqual(squarefree_kernel(98), 2)
        with self.assertRaises(ValueError):
            squarefree_kernel(0)

    def test_gap_sort_requires_materialized_complete_set(self) -> None:
        baseline = prioritized_odd_multiplier_order(100)
        gaps = {m: (m * 17) % 101 for m in baseline}
        order = gap_sorted_order_from_materialized_states(
            gaps, max_multiplier=100
        )
        self.assertEqual(set(order), set(baseline))
        self.assertEqual(
            tuple(gaps[m] for m in order),
            tuple(sorted(gaps[m] for m in baseline)),
        )
        incomplete = dict(gaps)
        incomplete.pop(baseline[-1])
        with self.assertRaises(ValueError):
            gap_sorted_order_from_materialized_states(
                incomplete, max_multiplier=100
            )

    def test_context_plan_keeps_partial_shortcuts_as_bounded_probes(self) -> None:
        context = ShortcutContext(
            n_bits=32768,
            max_multiplier=1000,
            expected_transitions=5000,
            states_materialized=True,
            likely_moderate_factor_imbalance=True,
            gap_filter_dominates=True,
            pisano_period_available=True,
        )
        plan = opportunistic_trial_plan(context)
        ids = tuple(item.shortcut_id for item in plan)
        self.assertEqual(ids[0], "pisano_metadata_probe")
        for expected in (
            "structural_priority",
            "learned_cover_prefix",
            "kernel13_prefix",
            "gap_sort_if_materialized",
            "ratio_cover_prefix",
            "quotient_jet_large_bits",
            "energy_jet_very_large_bits",
            "gap_residue_jet_ultralarge",
        ):
            self.assertIn(expected, ids)

    def test_ledger_tracks_empirical_expected_value(self) -> None:
        ledger = ShortcutLedger()
        ledger.record(
            "local_probe", hit=False, probe_cost=1.0, saved_cost=0.0
        )
        ledger.record(
            "local_probe", hit=True, probe_cost=1.0, saved_cost=10.0
        )
        stat = ledger.stats["local_probe"]
        self.assertEqual(stat.attempts, 2)
        self.assertEqual(stat.hits, 1)
        self.assertAlmostEqual(stat.empirical_hit_rate, 0.5)
        self.assertAlmostEqual(stat.expected_net_saving, 4.0)
        restored = ShortcutLedger.from_dict(ledger.to_dict())
        self.assertEqual(restored.to_dict(), ledger.to_dict())

    def test_adaptive_plan_uses_only_mature_regime_evidence(self) -> None:
        context = ShortcutContext(n_bits=8192, expected_transitions=1000)
        ledger = RegimeShortcutLedger()
        base_ids = tuple(x.shortcut_id for x in opportunistic_trial_plan(context))
        self.assertEqual(
            tuple(x.shortcut_id for x in adaptive_trial_plan(context, ledger)),
            base_ids,
        )

        for _ in range(4):
            ledger.record(
                context,
                "energy_jet_very_large_bits",
                hit=True,
                probe_cost=1.0,
                saved_cost=10.0,
            )
        self.assertEqual(
            tuple(x.shortcut_id for x in adaptive_trial_plan(context, ledger)),
            base_ids,
        )

        ledger.record(
            context,
            "energy_jet_very_large_bits",
            hit=True,
            probe_cost=1.0,
            saved_cost=10.0,
        )
        adapted = tuple(
            x.shortcut_id for x in adaptive_trial_plan(context, ledger)
        )
        self.assertEqual(adapted[0], "energy_jet_very_large_bits")

    def test_round_robin_batches_are_scan_complete_and_deduplicated(self) -> None:
        batches = multiplier_probe_batches(
            max_multiplier=1000,
            include_ratio_specialist=True,
            include_kernel_specialist=True,
            quantum=3,
        )
        flat = flatten_probe_batches(batches)
        baseline = prioritized_odd_multiplier_order(1000)
        self.assertEqual(set(flat), set(baseline))
        self.assertEqual(len(flat), len(baseline))
        self.assertEqual(len(flat), len(set(flat)))
        self.assertEqual(batches[-1][0], "structural_fallback")

    def test_shadow_signature_is_exact_and_cheap_to_bucket(self) -> None:
        n = 12345
        root = 111
        remainder = n - root * root
        tag = brc_shadow_signature(n, root, remainder, modulus=64)
        self.assertIn("M64:", tag)
        context = ShortcutContext(
            n_bits=n.bit_length(),
            shadow_tag=tag,
        )
        self.assertIn("shadow=", regime_key(context))
        with self.assertRaises(ValueError):
            brc_shadow_signature(n, root + 1, remainder, modulus=64)

    def test_low12_compact_filter_has_zero_false_negatives_on_squares(self) -> None:
        self.assertEqual(low12_compact_raw_table_bytes(), 2559)
        for root in range(10000):
            self.assertTrue(passes_low12_compact_square_filter(root * root))
        with self.assertRaises(ValueError):
            passes_low12_compact_square_filter(-1)

    def test_regime_ledger_separates_hidden_local_value(self) -> None:
        low = ShortcutContext(n_bits=512, expected_transitions=100)
        high = ShortcutContext(n_bits=8192, expected_transitions=1000)
        self.assertNotEqual(regime_key(low), regime_key(high))

        ledger = RegimeShortcutLedger()
        ledger.record(
            low,
            "probe",
            hit=False,
            probe_cost=2.0,
            saved_cost=0.0,
        )
        ledger.record(
            high,
            "probe",
            hit=True,
            probe_cost=2.0,
            saved_cost=20.0,
        )
        self.assertLess(ledger.ranking(low)[0][1], 0.0)
        self.assertGreater(ledger.ranking(high)[0][1], 0.0)


if __name__ == "__main__":
    unittest.main()
