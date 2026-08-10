import itertools
import unittest

from enterprise_math.precision_schedule_normalization import (
    mixed_radix_pack,
    mixed_radix_unpack,
    normalized_schedule_codes,
    schedule_local_digits,
)
from enterprise_math.precision_scheduling_slack import (
    incidence_only_slack_witness,
    radix_only_slack_witness,
)


class PrecisionScheduleNormalizationTests(unittest.TestCase):
    def test_mixed_radix_pack_unpack_is_bijective(self) -> None:
        radices = (2, 3, 4)
        seen = set()
        for digits in itertools.product(*(range(radix) for radix in radices)):
            value = mixed_radix_pack(digits, radices)
            self.assertEqual(mixed_radix_unpack(value, radices), digits)
            seen.add(value)
        self.assertEqual(seen, set(range(24)))

    def test_local_digit_words_are_exact_final_joint_classes(self) -> None:
        states, tasks = incidence_only_slack_witness()
        data = schedule_local_digits(states, tasks, ("E", "F"))
        self.assertEqual(data["radices"], (3, 3))
        self.assertEqual(len(set(data["digit_words"].values())), 5)
        self.assertEqual(data["final_joint_class_count"], 5)

    def test_radix_only_witness_is_fixed_by_packing_alone(self) -> None:
        states, tasks = radix_only_slack_witness()
        data = normalized_schedule_codes(states, tasks, ("E", "F"), base=2)
        self.assertEqual(data["product_capacity"], 15)
        self.assertEqual(len(data["realized_packed_codes"]), 15)
        self.assertEqual(data["separate_stage_depth"], 5)
        self.assertEqual(data["product_depth"], 4)
        self.assertEqual(data["realized_joint_depth"], 4)
        self.assertEqual(data["radix_slack_removed_by_packing"], 1)
        self.assertEqual(data["incidence_slack_removed_by_realized_ranking"], 0)

    def test_incidence_only_witness_needs_realized_support_ranking(self) -> None:
        states, tasks = incidence_only_slack_witness()
        data = normalized_schedule_codes(states, tasks, ("E", "F"), base=2)
        self.assertEqual(data["product_capacity"], 9)
        self.assertEqual(len(data["realized_packed_codes"]), 5)
        self.assertEqual(data["separate_stage_depth"], 4)
        self.assertEqual(data["product_depth"], 4)
        self.assertEqual(data["realized_joint_depth"], 3)
        self.assertEqual(data["radix_slack_removed_by_packing"], 0)
        self.assertEqual(data["incidence_slack_removed_by_realized_ranking"], 1)

    def test_two_normalization_steps_remove_exact_total_slack(self) -> None:
        for factory in (radix_only_slack_witness, incidence_only_slack_witness):
            states, tasks = factory()
            data = normalized_schedule_codes(states, tasks, tuple(tasks), base=2)
            self.assertEqual(
                data["separate_stage_depth"] - data["realized_joint_depth"],
                data["radix_slack_removed_by_packing"]
                + data["incidence_slack_removed_by_realized_ranking"],
            )


if __name__ == "__main__":
    unittest.main()
