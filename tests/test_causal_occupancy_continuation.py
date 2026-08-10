import unittest
from itertools import permutations

from enterprise_math.causal_occupancy_continuation import (
    coarse_transfer_histogram_profile,
    histogram_capacity,
    histogram_labeled_multiplicity,
    histogram_orbit_transition_incidence,
    histogram_total,
    histogram_transition_orbit_balance,
    occupancy_histogram,
    total_only_is_one_step_sufficient,
    total_outgoing_endpoint_multiplicity,
    transfer_histogram_update,
)
from enterprise_math.causal_coarse_transfer_incidence import fiber_count


def _weak_compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in _weak_compositions(total - first, slots - 1):
            yield (first,) + rest


class CausalOccupancyContinuationTests(unittest.TestCase):
    def test_histogram_orbit_multiplicity_partitions_all_labeled_fine_states(self):
        for capacity in range(1, 6):
            for total in range(8):
                histograms = {}
                for occupancy in _weak_compositions(total, capacity):
                    hist = occupancy_histogram(occupancy)
                    histograms.setdefault(hist, 0)
                    histograms[hist] += 1
                self.assertEqual(sum(histograms.values()), fiber_count(capacity, total))
                for histogram, direct_count in histograms.items():
                    self.assertEqual(histogram_capacity(histogram), capacity)
                    self.assertEqual(histogram_total(histogram), total)
                    self.assertEqual(histogram_labeled_multiplicity(histogram), direct_count)

    def test_total_only_can_fail_at_first_future_step(self):
        concentrated = occupancy_histogram((3, 0, 0))
        dispersed = occupancy_histogram((1, 1, 1))
        self.assertEqual(histogram_capacity(concentrated), histogram_capacity(dispersed))
        self.assertEqual(histogram_total(concentrated), histogram_total(dispersed))
        self.assertFalse(total_only_is_one_step_sufficient(concentrated, dispersed))
        receiver = occupancy_histogram((0, 0))
        self.assertEqual(total_outgoing_endpoint_multiplicity(receiver, concentrated), 2)
        self.assertEqual(total_outgoing_endpoint_multiplicity(receiver, dispersed), 6)

    def test_histogram_transition_profile_is_label_permutation_invariant(self):
        receiver_labeled = (2, 0, 1)
        donor_labeled = (0, 1, 2)
        receiver_hist = occupancy_histogram(receiver_labeled)
        donor_hist = occupancy_histogram(donor_labeled)
        expected = coarse_transfer_histogram_profile(receiver_hist, donor_hist)
        for receiver_perm in set(permutations(receiver_labeled)):
            for donor_perm in set(permutations(donor_labeled)):
                self.assertEqual(
                    coarse_transfer_histogram_profile(
                        occupancy_histogram(receiver_perm),
                        occupancy_histogram(donor_perm),
                    ),
                    expected,
                )

    def test_every_elementary_histogram_transfer_has_exact_reverse_orbit_balance(self):
        receiver = occupancy_histogram((0, 1, 2, 2))
        donor = occupancy_histogram((0, 1, 1, 3))
        for receiver_level, _ in receiver:
            for donor_level, _ in donor:
                if donor_level <= 0:
                    continue
                self.assertTrue(
                    histogram_transition_orbit_balance(
                        receiver,
                        donor,
                        receiver_level,
                        donor_level,
                    )
                )

    def test_histogram_update_preserves_capacity_and_moves_exactly_one_unit(self):
        receiver = occupancy_histogram((0, 0, 2))
        donor = occupancy_histogram((1, 1, 3, 0))
        new_receiver, new_donor, multiplicity = transfer_histogram_update(
            receiver,
            donor,
            receiver_level=0,
            donor_level=1,
        )
        self.assertEqual(histogram_capacity(new_receiver), histogram_capacity(receiver))
        self.assertEqual(histogram_capacity(new_donor), histogram_capacity(donor))
        self.assertEqual(histogram_total(new_receiver), histogram_total(receiver) + 1)
        self.assertEqual(histogram_total(new_donor), histogram_total(donor) - 1)
        self.assertEqual(multiplicity, 2 * 2)

    def test_orbit_incidence_is_orbit_size_times_per_microstate_profile(self):
        receiver = occupancy_histogram((0, 1, 1))
        donor = occupancy_histogram((0, 2, 2))
        profile = coarse_transfer_histogram_profile(receiver, donor)
        incidence = histogram_orbit_transition_incidence(receiver, donor)
        orbit_size = histogram_labeled_multiplicity(receiver) * histogram_labeled_multiplicity(donor)
        self.assertEqual(
            incidence,
            {target: orbit_size * count for target, count in profile.items()},
        )


if __name__ == "__main__":
    unittest.main()
