import unittest

from enterprise_math.precision_repair_support import repair_support_summary


class PrecisionRepairSupportTests(unittest.TestCase):
    def test_binary_refinement_collapses_global_burden_statistics(self) -> None:
        states = tuple(range(8))
        coarse = {
            0: "A", 1: "A",
            2: "B", 3: "B",
            4: "C", 5: "C",
            6: "D", 7: "D",
        }
        fine = {
            0: "a0", 1: "a1",  # split
            2: "b0", 3: "b0",  # unsplit
            4: "c0", 5: "c1",  # split
            6: "d0", 7: "d0",  # unsplit
        }
        data = repair_support_summary(states, fine, coarse)
        self.assertEqual(data["maximum_local_repair_alphabet"], 2)
        self.assertEqual(data["active_repair_support"], 2)
        self.assertEqual(data["class_gain"], 2)
        self.assertEqual(data["pair_repair_ambiguity"], 2)
        self.assertEqual(data["repair_spectrum"], (6, 2))

    def test_fixed_local_width_can_coexist_with_arbitrarily_many_active_blocks(self) -> None:
        for active in (1, 2, 5, 20):
            states = tuple(range(2 * active))
            coarse = {state: state // 2 for state in states}
            fine = {state: state for state in states}
            data = repair_support_summary(states, fine, coarse)
            self.assertEqual(data["maximum_local_repair_alphabet"], 2)
            self.assertEqual(data["active_repair_support"], active)
            self.assertEqual(data["class_gain"], active)
            self.assertEqual(data["pair_repair_ambiguity"], active)

    def test_general_width_bounds_active_support_and_pair_spectrum(self) -> None:
        states = tuple(range(10))
        coarse = {
            0: "A", 1: "A", 2: "A", 3: "A",
            4: "B", 5: "B", 6: "B",
            7: "C", 8: "C", 9: "C",
        }
        fine = {
            0: "a0", 1: "a1", 2: "a2", 3: "a2",  # size 3
            4: "b0", 5: "b0", 6: "b1",            # size 2
            7: "c0", 8: "c0", 9: "c0",            # size 1
        }
        data = repair_support_summary(states, fine, coarse)
        self.assertEqual(data["maximum_local_repair_alphabet"], 3)
        self.assertEqual(data["active_repair_support"], 2)
        self.assertEqual(data["class_gain"], 3)
        self.assertEqual(data["pair_repair_ambiguity"], 4)
        self.assertEqual(data["repair_spectrum"], (6, 4, 1))


if __name__ == "__main__":
    unittest.main()
