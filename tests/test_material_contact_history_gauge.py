import itertools
import unittest

from enterprise_math.material_contact_history_gauge import (
    repair_coordinate_with_forest,
    repair_gauge_correction,
    repair_generators_with_forest,
    transform_repair_between_forests,
    tree_section_from_chosen_forest,
)


TRIANGLE_B = (
    (-1, 0, 1),
    (1, -1, 0),
    (0, 1, -1),
)

PATH_B = (
    (-1, 0),
    (1, -1),
    (0, 1),
)

TOTAL_WITNESS = ((1, 1, 1),)
FULL_WITNESS = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)
DIFFERENCE_WITNESS = ((1, -1, 0),)

TRIANGLE_TREES = (
    (0, 1),
    (0, 2),
    (1, 2),
)


class MaterialContactHistoryGaugeTests(unittest.TestCase):
    def test_every_triangle_spanning_tree_gives_exact_integer_section(self):
        for tree in TRIANGLE_TREES:
            for body_delta in (
                (-1, 1, 0),
                (0, -2, 2),
                (3, -1, -2),
            ):
                section = tree_section_from_chosen_forest(
                    TRIANGLE_B,
                    body_delta,
                    tree,
                )
                reconstructed = tuple(
                    sum(
                        TRIANGLE_B[body][edge] * section[edge]
                        for edge in range(3)
                    )
                    for body in range(3)
                )
                self.assertEqual(reconstructed, body_delta)
                self.assertTrue(
                    all(
                        section[edge] == 0
                        for edge in range(3)
                        if edge not in tree
                    )
                )

    def test_repair_gauge_transform_is_exact_for_same_history(self):
        histories = tuple(itertools.product(range(-2, 4), repeat=3))
        for witness in (
            TOTAL_WITNESS,
            FULL_WITNESS,
            DIFFERENCE_WITNESS,
        ):
            for history in histories[::5]:
                body_delta = tuple(
                    sum(
                        TRIANGLE_B[body][edge] * history[edge]
                        for edge in range(3)
                    )
                    for body in range(3)
                )
                for source_tree in TRIANGLE_TREES:
                    source_repair = repair_coordinate_with_forest(
                        TRIANGLE_B,
                        witness,
                        history,
                        source_tree,
                    )
                    for target_tree in TRIANGLE_TREES:
                        target_repair = repair_coordinate_with_forest(
                            TRIANGLE_B,
                            witness,
                            history,
                            target_tree,
                        )
                        transformed = transform_repair_between_forests(
                            TRIANGLE_B,
                            witness,
                            body_delta,
                            source_repair,
                            source_tree,
                            target_tree,
                        )
                        self.assertEqual(
                            transformed.target_repair,
                            target_repair,
                        )

    def test_gauge_correction_depends_only_on_body_not_hidden_cycle_history(self):
        left = (1, 0, 0)
        right = (2, 1, 1)
        body_left = tuple(
            sum(TRIANGLE_B[body][edge] * left[edge] for edge in range(3))
            for body in range(3)
        )
        body_right = tuple(
            sum(TRIANGLE_B[body][edge] * right[edge] for edge in range(3))
            for body in range(3)
        )
        self.assertEqual(body_left, body_right)

        for witness in (TOTAL_WITNESS, FULL_WITNESS):
            correction = repair_gauge_correction(
                TRIANGLE_B,
                witness,
                body_left,
                (0, 1),
                (1, 2),
            )
            left_source = repair_coordinate_with_forest(
                TRIANGLE_B,
                witness,
                left,
                (0, 1),
            )
            left_target = repair_coordinate_with_forest(
                TRIANGLE_B,
                witness,
                left,
                (1, 2),
            )
            right_source = repair_coordinate_with_forest(
                TRIANGLE_B,
                witness,
                right,
                (0, 1),
            )
            right_target = repair_coordinate_with_forest(
                TRIANGLE_B,
                witness,
                right,
                (1, 2),
            )
            self.assertEqual(
                tuple(t - s for s, t in zip(left_source, left_target, strict=True)),
                correction,
            )
            self.assertEqual(
                tuple(t - s for s, t in zip(right_source, right_target, strict=True)),
                correction,
            )

    def test_event_generators_transform_covariantly(self):
        for witness in (TOTAL_WITNESS, FULL_WITNESS, DIFFERENCE_WITNESS):
            for source_tree in TRIANGLE_TREES:
                source_generators = repair_generators_with_forest(
                    TRIANGLE_B,
                    witness,
                    source_tree,
                )
                for target_tree in TRIANGLE_TREES:
                    target_generators = repair_generators_with_forest(
                        TRIANGLE_B,
                        witness,
                        target_tree,
                    )
                    for edge in range(3):
                        body_delta = tuple(
                            TRIANGLE_B[body][edge]
                            for body in range(3)
                        )
                        correction = repair_gauge_correction(
                            TRIANGLE_B,
                            witness,
                            body_delta,
                            source_tree,
                            target_tree,
                        )
                        self.assertEqual(
                            target_generators[edge],
                            tuple(
                                value + delta
                                for value, delta in zip(
                                    source_generators[edge],
                                    correction,
                                    strict=True,
                                )
                            ),
                        )

    def test_gauge_change_commutes_with_one_event_update(self):
        witness = TOTAL_WITNESS
        source_tree = (0, 1)
        target_tree = (1, 2)
        history = (2, 1, 1)
        body_delta = tuple(
            sum(TRIANGLE_B[body][edge] * history[edge] for edge in range(3))
            for body in range(3)
        )
        source_repair = repair_coordinate_with_forest(
            TRIANGLE_B,
            witness,
            history,
            source_tree,
        )
        target_before = transform_repair_between_forests(
            TRIANGLE_B,
            witness,
            body_delta,
            source_repair,
            source_tree,
            target_tree,
        ).target_repair
        source_generators = repair_generators_with_forest(
            TRIANGLE_B,
            witness,
            source_tree,
        )
        target_generators = repair_generators_with_forest(
            TRIANGLE_B,
            witness,
            target_tree,
        )

        for edge in range(3):
            body_after = tuple(
                body_delta[body] + TRIANGLE_B[body][edge]
                for body in range(3)
            )
            source_after = tuple(
                value + increment
                for value, increment in zip(
                    source_repair,
                    source_generators[edge],
                    strict=True,
                )
            )
            transformed_after = transform_repair_between_forests(
                TRIANGLE_B,
                witness,
                body_after,
                source_after,
                source_tree,
                target_tree,
            ).target_repair
            target_direct = tuple(
                value + increment
                for value, increment in zip(
                    target_before,
                    target_generators[edge],
                    strict=True,
                )
            )
            self.assertEqual(transformed_after, target_direct)

    def test_coboundary_witness_has_zero_repair_in_every_gauge(self):
        for tree in TRIANGLE_TREES:
            self.assertEqual(
                repair_generators_with_forest(
                    TRIANGLE_B,
                    DIFFERENCE_WITNESS,
                    tree,
                ),
                ((0,), (0,), (0,)),
            )

    def test_path_has_unique_spanning_forest_and_zero_gauge_correction(self):
        witness = ((3, -5),)
        tree = (0, 1)
        body_delta = (-2, 3, -1)
        correction = repair_gauge_correction(
            PATH_B,
            witness,
            body_delta,
            tree,
            tree,
        )
        self.assertEqual(correction, (0,))

    def test_invalid_forest_choices_are_rejected(self):
        with self.assertRaises(ValueError):
            tree_section_from_chosen_forest(
                TRIANGLE_B,
                (-1, 1, 0),
                (0,),
            )
        with self.assertRaises(ValueError):
            tree_section_from_chosen_forest(
                TRIANGLE_B,
                (-1, 1, 0),
                (0, 1, 2),
            )
        with self.assertRaises(ValueError):
            tree_section_from_chosen_forest(
                TRIANGLE_B,
                (-1, 1, 0),
                (0, 0),
            )
        with self.assertRaises(ValueError):
            repair_coordinate_with_forest(
                TRIANGLE_B,
                ((1, 0),),
                (1, 0, 0),
                (0, 1),
            )


if __name__ == "__main__":
    unittest.main()
