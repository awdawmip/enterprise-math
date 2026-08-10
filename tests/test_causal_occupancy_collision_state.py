import unittest
from itertools import product

from enterprise_math.causal_occupancy_collision_state import (
    collision_profile_matches_histogram_profile,
    collision_spectrum_recovers_histogram,
    collision_spectrum_transfer_profile,
    histogram_collision_spectrum,
    histogram_from_collision_spectrum,
    nonempty_slot_count_from_spectrum,
    occupancy_collision_spectrum,
    transfer_collision_delta,
    transfer_collision_spectrum_identity,
)
from enterprise_math.causal_occupancy_continuation import (
    histogram_total,
    occupancy_histogram,
)


class CausalOccupancyCollisionStateTests(unittest.TestCase):
    def test_full_collision_spectrum_recovers_anonymous_histogram(self):
        for slots in range(1, 6):
            for occupancy in product(range(5), repeat=slots):
                spectrum = occupancy_collision_spectrum(occupancy)
                self.assertTrue(collision_spectrum_recovers_histogram(occupancy))
                self.assertEqual(
                    histogram_from_collision_spectrum(spectrum),
                    occupancy_histogram(occupancy),
                )

    def test_k0_is_capacity_and_k1_is_total_value(self):
        occupancies = ((3, 0, 0), (1, 1, 1), (0, 2, 4, 1), (5,))
        for occupancy in occupancies:
            spectrum = occupancy_collision_spectrum(occupancy)
            self.assertEqual(spectrum[0], len(occupancy))
            self.assertEqual(spectrum[1], sum(occupancy))

    def test_same_total_can_have_different_hidden_collision_state(self):
        concentrated = occupancy_collision_spectrum((3, 0, 0))
        dispersed = occupancy_collision_spectrum((1, 1, 1))
        self.assertEqual(concentrated[0:2], dispersed[0:2])
        self.assertNotEqual(concentrated, dispersed)
        self.assertEqual(concentrated, (3, 3, 3, 1))
        self.assertEqual(dispersed, (3, 3, 0, 0))
        self.assertEqual(nonempty_slot_count_from_spectrum(concentrated), 1)
        self.assertEqual(nonempty_slot_count_from_spectrum(dispersed), 3)

    def test_pascal_transfer_delta_is_exact_at_every_collision_order(self):
        for occupancy in product(range(4), repeat=4):
            if sum(occupancy) == 0:
                continue
            for receiver in range(4):
                for donor in range(4):
                    if receiver == donor or occupancy[donor] == 0:
                        continue
                    self.assertTrue(
                        transfer_collision_spectrum_identity(
                            occupancy, receiver, donor
                        )
                    )

    def test_transfer_delta_conserves_k1(self):
        for receiver_level in range(5):
            for donor_level in range(1, 6):
                self.assertEqual(
                    transfer_collision_delta(receiver_level, donor_level, 1),
                    0,
                )

    def test_collision_spectrum_compiles_same_anonymous_future_profile_as_histogram(self):
        cases = (
            ((0, 1, 1), (0, 2, 2)),
            ((3, 0, 0), (1, 1, 1)),
            ((0, 1, 3, 3), (0, 2, 2, 4)),
            ((2, 2), (1, 3, 0)),
        )
        for receiver, donor in cases:
            self.assertTrue(collision_profile_matches_histogram_profile(receiver, donor))
            r_hist = occupancy_histogram(receiver)
            d_hist = occupancy_histogram(donor)
            profile = collision_spectrum_transfer_profile(
                histogram_collision_spectrum(r_hist),
                histogram_collision_spectrum(d_hist),
            )
            self.assertTrue(profile)
            self.assertTrue(
                all(
                    histogram_total(histogram_from_collision_spectrum(new_r))
                    == histogram_total(r_hist) + 1
                    and histogram_total(histogram_from_collision_spectrum(new_d))
                    == histogram_total(d_hist) - 1
                    for new_r, new_d in profile
                )
            )


if __name__ == "__main__":
    unittest.main()
