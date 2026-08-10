import unittest

from enterprise_math.material_contact_ttl_operation_order import (
    expiry_first_reduces_current_applied_impulse,
    ttl_operation_order_report,
)


class MaterialContactTTLOperationOrderTests(unittest.TestCase):
    def test_same_current_impulse_can_hide_different_ttl_loss(self):
        report = ttl_operation_order_report(
            total_queue=10,
            oldest_bucket=2,
            apply_capacity=5,
        )
        self.assertEqual(report.apply_then_expire.applied_whole_quanta, 5)
        self.assertEqual(report.expire_then_apply.applied_whole_quanta, 5)
        self.assertTrue(report.current_body_impulse_same)
        self.assertEqual(report.apply_then_expire.expired_whole_quanta, 0)
        self.assertEqual(report.expire_then_apply.expired_whole_quanta, 2)
        self.assertFalse(report.ttl_history_same)
        self.assertEqual(report.expiry_sink_defect, 2)
        self.assertEqual(report.final_queue_defect, 2)

    def test_expire_first_can_reduce_current_applied_impulse(self):
        report = ttl_operation_order_report(
            total_queue=4,
            oldest_bucket=2,
            apply_capacity=3,
        )
        self.assertEqual(
            (
                report.apply_then_expire.applied_whole_quanta,
                report.apply_then_expire.expired_whole_quanta,
                report.apply_then_expire.final_queue,
            ),
            (3, 0, 1),
        )
        self.assertEqual(
            (
                report.expire_then_apply.applied_whole_quanta,
                report.expire_then_apply.expired_whole_quanta,
                report.expire_then_apply.final_queue,
            ),
            (2, 2, 0),
        )
        self.assertEqual(report.applied_impulse_defect, 1)
        self.assertTrue(expiry_first_reduces_current_applied_impulse(4, 2, 3))

    def test_if_capacity_can_consume_everything_expiry_first_loses_exact_oldest_bucket(self):
        for total in range(0, 8):
            for oldest in range(total + 1):
                report = ttl_operation_order_report(total, oldest, total + 3)
                self.assertEqual(report.apply_then_expire.applied_whole_quanta, total)
                self.assertEqual(report.apply_then_expire.expired_whole_quanta, 0)
                self.assertEqual(
                    report.expire_then_apply.applied_whole_quanta,
                    total - oldest,
                )
                self.assertEqual(report.expire_then_apply.expired_whole_quanta, oldest)
                self.assertEqual(report.applied_impulse_defect, oldest)

    def test_expiry_sink_defect_is_exactly_min_oldest_and_capacity(self):
        for total in range(0, 10):
            for oldest in range(total + 1):
                for capacity in range(0, 12):
                    report = ttl_operation_order_report(
                        total,
                        oldest,
                        capacity,
                    )
                    self.assertEqual(
                        report.expiry_sink_defect,
                        min(oldest, capacity),
                    )
                    self.assertGreaterEqual(report.applied_impulse_defect, 0)
                    self.assertEqual(
                        report.final_queue_defect,
                        report.expiry_sink_defect
                        - report.applied_impulse_defect,
                    )
                    self.assertEqual(
                        report.apply_then_expire.accounted_total,
                        total,
                    )
                    self.assertEqual(
                        report.expire_then_apply.accounted_total,
                        total,
                    )

    def test_applied_impulse_defect_closed_formula(self):
        for total in range(0, 10):
            for oldest in range(total + 1):
                for capacity in range(0, 12):
                    report = ttl_operation_order_report(
                        total,
                        oldest,
                        capacity,
                    )
                    expected = min(capacity, total) - min(
                        capacity,
                        total - oldest,
                    )
                    self.assertEqual(report.applied_impulse_defect, expected)
                    self.assertEqual(
                        expiry_first_reduces_current_applied_impulse(
                            total,
                            oldest,
                            capacity,
                        ),
                        expected > 0,
                    )

    def test_no_oldest_bucket_or_zero_capacity_makes_order_identical(self):
        for total in range(0, 8):
            report = ttl_operation_order_report(total, 0, 4)
            self.assertEqual(report.applied_impulse_defect, 0)
            self.assertEqual(report.expiry_sink_defect, 0)
            self.assertEqual(report.final_queue_defect, 0)

        for total in range(0, 8):
            for oldest in range(total + 1):
                report = ttl_operation_order_report(total, oldest, 0)
                self.assertEqual(report.applied_impulse_defect, 0)
                self.assertEqual(report.expiry_sink_defect, 0)
                self.assertEqual(report.final_queue_defect, 0)
                self.assertTrue(report.ttl_history_same)

    def test_validation(self):
        with self.assertRaises(ValueError):
            ttl_operation_order_report(2, 3, 1)
        with self.assertRaises(ValueError):
            ttl_operation_order_report(-1, 0, 0)
        with self.assertRaises(TypeError):
            ttl_operation_order_report(1, False, 1)


if __name__ == "__main__":
    unittest.main()
