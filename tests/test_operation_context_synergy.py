import unittest

from enterprise_math.operation_quotient import stable_family_partition


def _common_refinement(states, left, right):
    ids = {}
    result = {}
    for state in states:
        signature = (left[state], right[state])
        if signature not in ids:
            ids[signature] = len(ids)
        result[state] = ids[signature]
    return result


class OperationContextSynergyTests(unittest.TestCase):
    def test_combined_language_can_refine_beyond_intersection_of_separate_repairs(self):
        states = (0, 1, 2, 3, 4)
        observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}
        f = {0: 0, 1: 0, 2: 0, 3: 4, 4: 0}
        g = {0: 0, 1: 3, 2: 4, 3: 0, 4: 0}

        f_only = stable_family_partition(states, {"f": f}, observation)
        g_only = stable_family_partition(states, {"g": g}, observation)
        separate_meet = _common_refinement(states, f_only, g_only)
        combined = stable_family_partition(
            states, {"f": f, "g": g}, observation
        )

        self.assertEqual(len(set(f_only.values())), 3)
        self.assertEqual(len(set(g_only.values())), 3)
        self.assertEqual(len(set(separate_meet.values())), 4)
        self.assertEqual(len(set(combined.values())), 5)
        self.assertEqual(len(set(combined.values())), len(states))

    def test_q6_plus2_plus3_mixed_word_separates_pair_neither_generator_separates_alone(self):
        q6 = lambda n: n // 6

        # The residues reached from 0 and 1 by repeated +2 never straddle a
        # six-block boundary; the same holds for repeated +3.  One residue
        # period is enough to witness each cycle.
        for count in range(6):
            self.assertEqual(q6(2 * count), q6(1 + 2 * count))
            self.assertEqual(q6(3 * count), q6(1 + 3 * count))

        # The mixed word +2 followed by +3 produces +5 and immediately exposes
        # the distinction deleted by both separately repaired quotients.
        self.assertNotEqual(q6(0 + 2 + 3), q6(1 + 2 + 3))


if __name__ == "__main__":
    unittest.main()
