import unittest
from itertools import product

from enterprise_math.material_ledger_redistribution import (
    apply_queued_whole,
    classify_scalar_ledger_observable,
    contact_matrix_expiry_invariant,
    contact_matrix_full_redistribution_invariant,
    contact_matrix_scheduler_invariant,
    expire_queued_whole,
    scalar_expiry_invariant,
    scalar_full_redistribution_invariant,
    scalar_ledger_readout,
    scalar_scheduler_invariant,
    whole_ledger_total,
)


class MaterialLedgerRedistributionTests(unittest.TestCase):
    def test_applied_live_ever_have_exact_expected_invariance_classes(self):
        applied = classify_scalar_ledger_observable((1, 0, 0))
        live = classify_scalar_ledger_observable((1, 1, 0))
        ever = classify_scalar_ledger_observable((1, 1, 1))

        self.assertFalse(applied.scheduler_invariant)
        self.assertFalse(applied.expiry_invariant)
        self.assertFalse(applied.full_redistribution_invariant)

        self.assertTrue(live.scheduler_invariant)
        self.assertFalse(live.expiry_invariant)
        self.assertFalse(live.full_redistribution_invariant)

        self.assertTrue(ever.scheduler_invariant)
        self.assertTrue(ever.expiry_invariant)
        self.assertTrue(ever.full_redistribution_invariant)

    def test_scheduler_invariance_iff_applied_and_queued_weights_equal(self):
        ledgers = tuple(product(range(4), repeat=3))
        for weights in product(range(-2, 3), repeat=3):
            predicted = weights[0] == weights[1]
            self.assertEqual(scalar_scheduler_invariant(weights), predicted)
            observed = True
            for ledger in ledgers:
                for amount in range(ledger[1] + 1):
                    moved = apply_queued_whole(ledger, amount)
                    if scalar_ledger_readout(ledger, weights) != scalar_ledger_readout(
                        moved,
                        weights,
                    ):
                        observed = False
                        break
                if not observed:
                    break
            self.assertEqual(observed, predicted, weights)

    def test_expiry_invariance_iff_queued_and_expired_weights_equal(self):
        ledgers = tuple(product(range(4), repeat=3))
        for weights in product(range(-2, 3), repeat=3):
            predicted = weights[1] == weights[2]
            self.assertEqual(scalar_expiry_invariant(weights), predicted)
            observed = True
            for ledger in ledgers:
                for amount in range(ledger[1] + 1):
                    moved = expire_queued_whole(ledger, amount)
                    if scalar_ledger_readout(ledger, weights) != scalar_ledger_readout(
                        moved,
                        weights,
                    ):
                        observed = False
                        break
                if not observed:
                    break
            self.assertEqual(observed, predicted, weights)

    def test_full_redistribution_invariance_iff_all_weights_equal(self):
        for weights in product(range(-2, 3), repeat=3):
            predicted = weights[0] == weights[1] == weights[2]
            self.assertEqual(
                scalar_full_redistribution_invariant(weights),
                predicted,
            )
            self.assertEqual(
                classify_scalar_ledger_observable(weights).full_redistribution_invariant,
                predicted,
            )

    def test_every_elementary_redistribution_preserves_whole_total(self):
        for ledger in product(range(5), repeat=3):
            total = whole_ledger_total(ledger)
            for amount in range(ledger[1] + 1):
                self.assertEqual(
                    whole_ledger_total(apply_queued_whole(ledger, amount)),
                    total,
                )
                self.assertEqual(
                    whole_ledger_total(expire_queued_whole(ledger, amount)),
                    total,
                )

    def test_scheduler_and_expiry_moves_generate_zero_sum_compartment_differences(self):
        ledger = (2, 5, 3)
        applied = apply_queued_whole(ledger, 4)
        expired = expire_queued_whole(ledger, 4)
        self.assertEqual(
            tuple(a - b for a, b in zip(applied, ledger, strict=True)),
            (4, -4, 0),
        )
        self.assertEqual(
            tuple(a - b for a, b in zip(expired, ledger, strict=True)),
            (0, -4, 4),
        )
        self.assertEqual(sum(applied) - sum(ledger), 0)
        self.assertEqual(sum(expired) - sum(ledger), 0)

    def test_contact_matrix_criteria_are_exact_componentwise_equalities(self):
        applied = (
            (1, 2, 0),
            (0, -1, 3),
        )
        same = (
            (1, 2, 0),
            (0, -1, 3),
        )
        different = (
            (1, 2, 0),
            (0, -1, 4),
        )
        self.assertTrue(contact_matrix_scheduler_invariant(applied, same))
        self.assertFalse(contact_matrix_scheduler_invariant(applied, different))
        self.assertTrue(contact_matrix_expiry_invariant(applied, same))
        self.assertFalse(contact_matrix_expiry_invariant(applied, different))
        self.assertTrue(
            contact_matrix_full_redistribution_invariant(applied, same, same)
        )
        self.assertFalse(
            contact_matrix_full_redistribution_invariant(
                applied,
                same,
                different,
            )
        )

    def test_constant_scalar_weights_are_multiples_of_total_whole_history(self):
        ledger = (4, 7, 2)
        for coefficient in range(-5, 6):
            weights = (coefficient,) * 3
            self.assertEqual(
                scalar_ledger_readout(ledger, weights),
                coefficient * whole_ledger_total(ledger),
            )
            self.assertTrue(scalar_full_redistribution_invariant(weights))

    def test_validation(self):
        with self.assertRaises(ValueError):
            whole_ledger_total((1, 2))
        with self.assertRaises(ValueError):
            whole_ledger_total((1, -1, 0))
        with self.assertRaises(ValueError):
            apply_queued_whole((1, 2, 3), 3)
        with self.assertRaises(ValueError):
            expire_queued_whole((1, 2, 3), -1)
        with self.assertRaises(ValueError):
            scalar_ledger_readout((1, 2, 3), (1, 2))
        with self.assertRaises(TypeError):
            scalar_scheduler_invariant((1, False, 1))
        with self.assertRaises(ValueError):
            contact_matrix_scheduler_invariant((), ())


if __name__ == "__main__":
    unittest.main()
