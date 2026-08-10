import unittest

from enterprise_math.material_contact_ttl_transfer_policy import (
    same_quantizer_return_blocks_genuine_expiry,
    same_quantizer_ttl_return,
)


class MaterialContactTTLTransferPolicyTests(unittest.TestCase):
    def test_same_quantizer_return_recreates_every_expired_whole_quantum(self):
        for amplitude in range(1, 12):
            for expired in range(0, 8):
                for remainder in range(amplitude):
                    report = same_quantizer_ttl_return(
                        amplitude,
                        expired,
                        remainder,
                    )
                    self.assertEqual(
                        report.returned_raw_numerator,
                        amplitude * expired + remainder,
                    )
                    self.assertEqual(report.requantized_whole_quanta, expired)
                    self.assertEqual(report.pending_remainder_after, remainder)
                    self.assertTrue(report.exactly_reconstitutes_expired_queue)

    def test_nonzero_expiry_requires_sink_or_transformed_state_to_be_genuine(self):
        self.assertFalse(
            same_quantizer_return_blocks_genuine_expiry(10, 0, 6)
        )
        for expired in range(1, 6):
            self.assertTrue(
                same_quantizer_return_blocks_genuine_expiry(
                    10,
                    expired,
                    6,
                )
            )

    def test_six_plus_whole_return_example(self):
        report = same_quantizer_ttl_return(
            amplitude=10,
            expired_whole_quanta=2,
            pending_remainder=6,
        )
        self.assertEqual(report.returned_raw_numerator, 26)
        self.assertEqual(report.requantized_whole_quanta, 2)
        self.assertEqual(report.pending_remainder_after, 6)

    def test_validation(self):
        with self.assertRaises(ValueError):
            same_quantizer_ttl_return(0, 1, 0)
        with self.assertRaises(ValueError):
            same_quantizer_ttl_return(10, -1, 0)
        with self.assertRaises(ValueError):
            same_quantizer_ttl_return(10, 1, 10)
        with self.assertRaises(TypeError):
            same_quantizer_ttl_return(False, 1, 0)


if __name__ == "__main__":
    unittest.main()
