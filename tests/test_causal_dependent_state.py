import unittest

from enterprise_math.causal_dependent_state import (
    bulk_dependent_compression,
    continuation_classes_by_bulk,
    dependent_state_count,
    rectangular_upper_bound,
    stable_dependent_types,
)


class CausalDependentStateTests(unittest.TestCase):
    def test_saturation_makes_relation_type_bulk_dependent(self):
        states = ("0A", "0B", "1A", "1B")
        bulk = {"0A": 0, "0B": 0, "1A": 1, "1B": 1}
        raw_relation = {"0A": "A", "0B": "B", "1A": "A", "1B": "B"}
        # Current observation exposes bulk but not raw relation identity.
        extra = {state: None for state in states}
        # A one-step probe distinguishes A/B only below saturation.  Once bulk=1,
        # both raw relation identities flow to the same saturated future.
        actions = {
            "probe": {
                "0A": "0A",
                "0B": "1B",
                "1A": "1A",
                "1B": "1A",
            }
        }
        classes, _ = stable_dependent_types(bulk, extra, actions)
        by_bulk = continuation_classes_by_bulk(bulk, classes)
        self.assertEqual(len(by_bulk[0]), 2)
        self.assertEqual(len(by_bulk[1]), 1)
        self.assertEqual(dependent_state_count(bulk, classes), 3)
        self.assertEqual(rectangular_upper_bound(bulk, raw_relation), 4)
        self.assertEqual(bulk_dependent_compression(bulk, raw_relation, classes), 1)

    def test_if_relation_matters_at_every_bulk_product_state_can_be_exact(self):
        states = ("0A", "0B", "1A", "1B")
        bulk = {"0A": 0, "0B": 0, "1A": 1, "1B": 1}
        raw_relation = {"0A": "A", "0B": "B", "1A": "A", "1B": "B"}
        extra = {state: None for state in states}
        actions = {
            "probe": {
                "0A": "0A",
                "0B": "1B",
                "1A": "1A",
                "1B": "0B",
            }
        }
        classes, _ = stable_dependent_types(bulk, extra, actions)
        self.assertEqual(dependent_state_count(bulk, classes), 4)
        self.assertEqual(bulk_dependent_compression(bulk, raw_relation, classes), 0)

    def test_if_relation_never_matters_each_bulk_has_one_type(self):
        states = ("0A", "0B", "1A", "1B")
        bulk = {"0A": 0, "0B": 0, "1A": 1, "1B": 1}
        raw_relation = {"0A": "A", "0B": "B", "1A": "A", "1B": "B"}
        extra = {state: None for state in states}
        actions = {
            "step": {
                "0A": "1A",
                "0B": "1A",
                "1A": "1A",
                "1B": "1A",
            }
        }
        classes, _ = stable_dependent_types(bulk, extra, actions)
        by_bulk = continuation_classes_by_bulk(bulk, classes)
        self.assertEqual(len(by_bulk[0]), 1)
        self.assertEqual(len(by_bulk[1]), 1)
        self.assertEqual(dependent_state_count(bulk, classes), 2)
        self.assertEqual(bulk_dependent_compression(bulk, raw_relation, classes), 2)


if __name__ == "__main__":
    unittest.main()
