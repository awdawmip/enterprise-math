import unittest

from enterprise_math.p017_root_factor_schedule import root_factor_two_task_schedule


class P017RootFactorScheduleTests(unittest.TestCase):
    def test_k11_strictly_prefers_root_first(self) -> None:
        data = root_factor_two_task_schedule(11, base=2)
        self.assertEqual(data["factor_classes"], 5)
        self.assertEqual(data["root_classes"], 6)
        self.assertEqual(data["joint_classes"], 6)
        self.assertEqual(data["factor_to_root_factor"], 2)
        self.assertEqual(data["root_to_factor_factor"], 1)
        self.assertEqual(data["factor_first_depth"], 4)
        self.assertEqual(data["root_first_depth"], 3)
        self.assertEqual(data["joint_lower_bound_depth"], 3)
        self.assertEqual(data["preferred"], "ROOT_FIRST")

    def test_k1737_strictly_prefers_factor_first(self) -> None:
        data = root_factor_two_task_schedule(1737, base=2)
        self.assertEqual(data["factor_classes"], 157)
        self.assertEqual(data["root_classes"], 109)
        self.assertEqual(data["joint_classes"], 164)
        self.assertEqual(data["factor_to_root_factor"], 2)
        self.assertEqual(data["root_to_factor_factor"], 8)
        self.assertEqual(data["factor_first_depth"], 9)
        self.assertEqual(data["root_first_depth"], 10)
        self.assertEqual(data["joint_lower_bound_depth"], 8)
        self.assertEqual(data["preferred"], "FACTOR_FIRST")

    def test_no_fixed_two_task_order_is_globally_optimal(self) -> None:
        self.assertEqual(root_factor_two_task_schedule(11)["preferred"], "ROOT_FIRST")
        self.assertEqual(root_factor_two_task_schedule(1737)["preferred"], "FACTOR_FIRST")

    def test_preference_is_exact_integer_cost_comparison(self) -> None:
        for k in range(3, 80):
            data = root_factor_two_task_schedule(k, base=2)
            left = data["factor_first_depth"]
            right = data["root_first_depth"]
            expected = "FACTOR_FIRST" if left < right else "ROOT_FIRST" if right < left else "TIE"
            self.assertEqual(data["preferred"], expected)
            self.assertGreaterEqual(left, data["joint_lower_bound_depth"])
            self.assertGreaterEqual(right, data["joint_lower_bound_depth"])

    def test_factor_first_is_always_within_one_bit_of_joint_lower_bound(self) -> None:
        for k in range(3, 300):
            data = root_factor_two_task_schedule(k, base=2)
            self.assertLessEqual(
                data["factor_first_depth"],
                data["joint_lower_bound_depth"] + 1,
            )

    def test_any_strict_root_first_advantage_is_exactly_one_bit(self) -> None:
        witnessed = False
        for k in range(3, 300):
            data = root_factor_two_task_schedule(k, base=2)
            if data["root_first_depth"] < data["factor_first_depth"]:
                witnessed = True
                self.assertEqual(
                    data["root_first_depth"],
                    data["joint_lower_bound_depth"],
                )
                self.assertEqual(
                    data["factor_first_depth"],
                    data["joint_lower_bound_depth"] + 1,
                )
        self.assertTrue(witnessed)


if __name__ == "__main__":
    unittest.main()
