import unittest

from enterprise_math.exact_resource_pareto import (
    AccountingMismatch,
    Comparison,
    InvalidWeights,
    Representation,
    ResourceVector,
    ROOT_VERDICT,
    ROUTING,
    SemanticMismatch,
    UndefinedResource,
    canonical_semantic_digest,
    compare,
    pareto_frontier,
)


FIBRE = canonical_semantic_digest(
    {
        "accepted_state": ["p", "q", "U", "V", "c"],
        "future_language": ["0", "1", "2", "3"],
        "domain": "same",
        "continuation": "executable",
    }
)
REGIME = "r014-fixture-v1"


def rep(name, storage, work, depth, channel, reconstruction, *, fibre=FIBRE, regime=REGIME):
    return Representation(
        name=name,
        semantic_fibre=fibre,
        accounting_regime=regime,
        resources=ResourceVector(
            storage=storage,
            work=work,
            depth=depth,
            channel=channel,
            reconstruction=reconstruction,
        ),
    )


class ExactResourceParetoTests(unittest.TestCase):
    def test_root_routing_is_machine_readable(self):
        self.assertEqual(
            ROOT_VERDICT,
            "ROOTING_SUCCESS / METHODOLOGY_AND_TOOLING_ONLY / "
            "NO_NEW_FOUNDATION_RESOURCE_CALCULUS",
        )
        self.assertEqual(
            ROUTING,
            {
                "new_enterprise_specific_calculus": False,
                "methodology_and_tooling": True,
                "ordinary_implementation_pareto_only": True,
            },
        )

    def test_semantic_digest_is_canonical_for_key_order(self):
        left = canonical_semantic_digest({"b": 2, "a": 1})
        right = canonical_semantic_digest({"a": 1, "b": 2})
        self.assertEqual(left, right)

    def test_semantic_digest_changes_when_contract_changes(self):
        left = canonical_semantic_digest({"continuation": "terminal"})
        right = canonical_semantic_digest({"continuation": "executable"})
        self.assertNotEqual(left, right)

    def test_semantic_mismatch_fails_before_resource_comparison(self):
        left = rep("left", 1, 1, 1, 1, 1)
        right = rep(
            "right", 1, 1, 1, 1, 1,
            fibre=canonical_semantic_digest({"different": True}),
        )
        with self.assertRaises(SemanticMismatch):
            compare(left, right)

    def test_accounting_mismatch_fails(self):
        left = rep("left", 1, 1, 1, 1, 1)
        right = rep("right", 1, 1, 1, 1, 1, regime="different-regime")
        with self.assertRaises(AccountingMismatch):
            compare(left, right)

    def test_same_fibre_strict_pareto_dominance_passes(self):
        left = rep("left", 2, 3, 4, 1, 0)
        right = rep("right", 3, 5, 4, 2, 1)
        self.assertEqual(compare(left, right), Comparison.LEFT_DOMINATES)
        self.assertEqual(compare(right, left), Comparison.RIGHT_DOMINATES)

    def test_cross_coordinate_tradeoff_is_incomparable(self):
        compact = rep("compact", 2, 10, 8, 1, 4)
        materialized = rep("materialized", 12, 2, 1, 2, 0)
        self.assertEqual(compare(compact, materialized), Comparison.INCOMPARABLE)

    def test_resource_equivalent_is_not_representation_identity(self):
        left = rep("encoding-a", 2, 3, 4, 1, 0)
        right = rep("encoding-b", 2, 3, 4, 1, 0)
        self.assertEqual(compare(left, right), Comparison.RESOURCE_EQUIVALENT)

    def test_active_none_is_an_error(self):
        left = rep("left", 2, 3, 4, None, 0)
        right = rep("right", 3, 4, 5, 2, 1)
        with self.assertRaises(UndefinedResource):
            compare(left, right)

    def test_zero_weight_explicitly_disables_none_coordinate(self):
        left = rep("left", 2, 3, 4, None, 0)
        right = rep("right", 3, 4, 5, None, 1)
        self.assertEqual(
            compare(left, right, weights={"channel": 0}),
            Comparison.LEFT_DOMINATES,
        )

    def test_positive_common_weights_do_not_scalarize_tradeoff(self):
        left = rep("left", 1, 100, 1, 1, 1)
        right = rep("right", 100, 1, 1, 1, 1)
        self.assertEqual(
            compare(left, right, weights={"storage": 1000, "work": 0.001}),
            Comparison.INCOMPARABLE,
        )

    def test_all_zero_weights_are_invalid(self):
        left = rep("left", 1, 1, 1, 1, 1)
        right = rep("right", 2, 2, 2, 2, 2)
        with self.assertRaises(InvalidWeights):
            compare(left, right, weights={key: 0 for key in (
                "storage", "work", "depth", "channel", "reconstruction"
            )})

    def test_frontier_removes_dominated_point(self):
        compact = rep("compact", 2, 10, 8, 1, 4)
        materialized = rep("materialized", 12, 2, 1, 2, 0)
        dominated = rep("dominated", 20, 20, 20, 3, 5)
        self.assertEqual(
            [item.name for item in pareto_frontier([compact, materialized, dominated])],
            ["compact", "materialized"],
        )


if __name__ == "__main__":
    unittest.main()
