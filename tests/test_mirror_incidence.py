import unittest

from enterprise_math.mirror_incidence import mirror_incidence_summary


class MirrorIncidenceTests(unittest.TestCase):
    def test_state_and_prime_indexed_totals_agree(self):
        for k in range(3, 60):
            data = mirror_incidence_summary(k)
            self.assertEqual(
                data["incidence_total"],
                sum(data["per_prime_incidence"].values()),
            )
            self.assertEqual(
                data["all_composite_required_minimum"],
                2 * data["surviving_pair_count"],
            )

    def test_every_recorded_pair_has_disjoint_supports(self):
        data = mirror_incidence_summary(40)
        for row in data["pairs"]:
            self.assertTrue(
                set(row["lower_support"]).isdisjoint(row["upper_support"])
            )
            self.assertEqual(
                row["incidence"],
                len(row["lower_support"]) + len(row["upper_support"]),
            )

    def test_known_composite_surviving_pair_consumes_two_resources(self):
        data = mirror_incidence_summary(20)
        rows = [row for row in data["pairs"] if row["radius"] == 17]
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["lower"], 403)
        self.assertEqual(row["upper"], 437)
        self.assertEqual(row["lower_support"], [13])
        self.assertEqual(row["upper_support"], [19])
        self.assertEqual(row["incidence"], 2)


if __name__ == "__main__":
    unittest.main()
