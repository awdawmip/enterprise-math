import unittest

from enterprise_math.dimension_contraction import balanced_power_energy


def _fiber_right_split(receiver_size, donor_size, total, rest_energy, threshold, power=2):
    bound = threshold + abs(total) + 5
    admissible = []
    for receiver_total in range(-bound, bound + 1):
        donor_total = total - receiver_total
        energy = (
            balanced_power_energy(receiver_size, power, receiver_total)
            + balanced_power_energy(donor_size, power, donor_total)
            + rest_energy
        )
        if energy <= threshold:
            admissible.append(receiver_total)
    if not admissible:
        raise AssertionError("expected a non-empty fiber")
    receiver_total = max(admissible)
    return receiver_total, total - receiver_total


def chain_witness_four_slots(threshold: int) -> tuple[int, int, int, int]:
    # Reverse-lift the contraction tree (((0,1),2),3), always taking the unique
    # right boundary exit in the oriented receiver <- donor channel.
    block012, x3 = _fiber_right_split(3, 1, 0, 0, threshold)
    block01, x2 = _fiber_right_split(
        2, 1, block012, balanced_power_energy(1, 2, x3), threshold
    )
    x0, x1 = _fiber_right_split(
        1,
        1,
        block01,
        balanced_power_energy(1, 2, x2) + balanced_power_energy(1, 2, x3),
        threshold,
    )
    return x0, x1, x2, x3


def balanced_witness_four_slots(threshold: int) -> tuple[int, int, int, int]:
    # Reverse-lift ((0,1),(2,3)), with the left parent as receiver at the top.
    block01, block23 = _fiber_right_split(2, 2, 0, 0, threshold)
    x0, x1 = _fiber_right_split(
        1, 1, block01, balanced_power_energy(2, 2, block23), threshold
    )
    x2, x3 = _fiber_right_split(
        1,
        1,
        block23,
        balanced_power_energy(1, 2, x0) + balanced_power_energy(1, 2, x1),
        threshold,
    )
    return x0, x1, x2, x3


class ContractionWitnessHistoryTests(unittest.TestCase):
    def test_value_associativity_does_not_imply_witness_associativity(self):
        threshold = 16
        chain = chain_witness_four_slots(threshold)
        balanced = balanced_witness_four_slots(threshold)
        self.assertEqual(chain, (2, 1, 0, -3))
        self.assertEqual(balanced, (2, 2, -2, -2))
        self.assertNotEqual(sorted(chain), sorted(balanced))
        self.assertNotEqual(sorted(-x for x in chain), sorted(balanced))
        self.assertLessEqual(sum(x * x for x in chain), threshold)
        self.assertLessEqual(sum(x * x for x in balanced), threshold)


if __name__ == "__main__":
    unittest.main()
