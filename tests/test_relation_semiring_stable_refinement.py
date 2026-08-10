import unittest

from enterprise_math.relation_branching_semiring import (
    boolean_semiring,
    joint_partition,
    modular_semiring,
    natural_semiring,
)
from enterprise_math.relation_semiring_stable_refinement import (
    branching_signature_sequence_matches_weighted_refinement,
    candidate_refines_shared_coarsest,
    coarsest_shared_semiring_refinement,
    multi_semiring_relation_stable_on_partition,
    product_semiring_refinement_matches_shared_pair,
    semiring_relation_stable_on_partition,
)
from enterprise_math.relation_support_stable_refinement import (
    normalize_partition,
    partition_from_observation,
    partition_refines,
)


def all_set_partitions(values):
    values = tuple(values)

    def rec(index, blocks):
        if index == len(values):
            yield normalize_partition(tuple(frozenset(block) for block in blocks))
            return
        value = values[index]
        for block_index in range(len(blocks)):
            nxt = [set(block) for block in blocks]
            nxt[block_index].add(value)
            yield from rec(index + 1, nxt)
        yield from rec(index + 1, [*blocks, {value}])

    seen = set()
    for partition in rec(0, []):
        if partition not in seen:
            seen.add(partition)
            yield partition


def product_correlation_fixture():
    states = (
        "p",
        "q",
        "a1",
        "a2",
        "c",
        "d",
        "z1",
        "z2",
    )
    relations = {
        "a": frozenset(
            {
                ("p", "a1"),
                ("p", "d"),
                ("q", "a1"),
                ("q", "a2"),
                ("q", "c"),
                ("q", "d"),
            }
        ),
        "b": frozenset(
            {
                ("c", "z1"),
                ("c", "z2"),
                ("d", "z1"),
            }
        ),
    }
    return states, relations, lambda _state: "visible"


def small_shared_fixture():
    states = (0, 1, 2, 3)
    relations = {
        "a": frozenset({(0, 2), (1, 2), (1, 3), (2, 0)}),
        "b": frozenset({(0, 3), (1, 3), (2, 2), (3, 2)}),
    }
    observation = lambda _state: 0
    return states, relations, observation


class RelationSemiringStableRefinementTests(unittest.TestCase):
    def test_weighted_fixed_point_matches_recursive_branching_signatures(self):
        states, relations, observation = small_shared_fixture()
        for semiring in (
            natural_semiring(),
            boolean_semiring(),
            modular_semiring(2),
            modular_semiring(3),
        ):
            self.assertTrue(
                branching_signature_sequence_matches_weighted_refinement(
                    states,
                    relations,
                    observation,
                    semiring,
                )
            )

    def test_product_semiring_equals_coupled_shared_interface_refinement(self):
        states, relations, observation = product_correlation_fixture()
        initial = partition_from_observation(states, observation)
        self.assertTrue(
            product_semiring_refinement_matches_shared_pair(
                initial,
                relations,
                boolean_semiring(),
                modular_semiring(2),
            )
        )

    def test_naive_joint_of_individually_stable_quotients_can_be_unsafe_again(self):
        states, relations, observation = product_correlation_fixture()
        initial = partition_from_observation(states, observation)
        B = boolean_semiring()
        Z2 = modular_semiring(2)

        B_report = coarsest_shared_semiring_refinement(
            initial,
            relations,
            (B,),
        )
        Z2_report = coarsest_shared_semiring_refinement(
            initial,
            relations,
            (Z2,),
        )
        self.assertTrue(
            semiring_relation_stable_on_partition(
                B_report.final_partition,
                relations,
                B,
            )
        )
        self.assertTrue(
            semiring_relation_stable_on_partition(
                Z2_report.final_partition,
                relations,
                Z2,
            )
        )

        naive_join = joint_partition(
            B_report.final_partition,
            Z2_report.final_partition,
        )
        self.assertIn(frozenset({"p", "q"}), naive_join)

        # Refining the targets by the other coefficient view makes p/q's
        # Boolean and parity target-block vectors diverge.  Safe-operation
        # capability is not monotone under raw state refinement.
        self.assertFalse(
            multi_semiring_relation_stable_on_partition(
                naive_join,
                relations,
                (B, Z2),
            )
        )

        coupled = coarsest_shared_semiring_refinement(
            initial,
            relations,
            (B, Z2),
        )
        self.assertIn(frozenset({"p"}), coupled.final_partition)
        self.assertIn(frozenset({"q"}), coupled.final_partition)
        self.assertTrue(partition_refines(coupled.final_partition, naive_join))
        self.assertTrue(
            multi_semiring_relation_stable_on_partition(
                coupled.final_partition,
                relations,
                (B, Z2),
            )
        )

    def test_shared_compositional_join_is_coarsest_among_stable_candidates(self):
        states, relations, observation = small_shared_fixture()
        initial = partition_from_observation(states, observation)
        semirings = (boolean_semiring(), modular_semiring(2))
        report = coarsest_shared_semiring_refinement(
            initial,
            relations,
            semirings,
        )
        stable_candidates = 0
        for candidate in all_set_partitions(states):
            if not partition_refines(candidate, initial):
                continue
            if not multi_semiring_relation_stable_on_partition(
                candidate,
                relations,
                semirings,
            ):
                continue
            stable_candidates += 1
            self.assertTrue(
                candidate_refines_shared_coarsest(
                    report,
                    candidate,
                    relations,
                    semirings,
                )
            )
        self.assertGreater(stable_candidates, 0)

    def test_independent_readout_join_and_compositional_join_answer_different_tasks(self):
        states, relations, observation = product_correlation_fixture()
        initial = partition_from_observation(states, observation)
        B = boolean_semiring()
        Z2 = modular_semiring(2)
        B_final = coarsest_shared_semiring_refinement(
            initial,
            relations,
            (B,),
        ).final_partition
        Z2_final = coarsest_shared_semiring_refinement(
            initial,
            relations,
            (Z2,),
        ).final_partition

        # Pairing only the two final readout labels requires the ordinary joint
        # state partition and leaves p/q merged.
        independent = joint_partition(B_final, Z2_final)
        self.assertIn(frozenset({"p", "q"}), independent)

        # Requiring both weighted transition interfaces to continue operating on
        # one shared successor state space forces additional closure.
        compositional = coarsest_shared_semiring_refinement(
            initial,
            relations,
            (B, Z2),
        ).final_partition
        self.assertNotEqual(independent, compositional)
        self.assertTrue(partition_refines(compositional, independent))

    def test_validation(self):
        initial = normalize_partition(({0, 1},))
        with self.assertRaises(ValueError):
            coarsest_shared_semiring_refinement(initial, {}, (boolean_semiring(),))
        with self.assertRaises(ValueError):
            coarsest_shared_semiring_refinement(
                initial,
                {"a": frozenset()},
                (),
            )
        with self.assertRaises(ValueError):
            candidate_refines_shared_coarsest(
                coarsest_shared_semiring_refinement(
                    initial,
                    {"a": frozenset()},
                    (boolean_semiring(),),
                ),
                ({0}, {1}),
                {"a": frozenset()},
                (boolean_semiring(), modular_semiring(2)),
            )


if __name__ == "__main__":
    unittest.main()
