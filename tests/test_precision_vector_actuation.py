import itertools
import unittest
from math import gcd, lcm

from enterprise_math.precision_vector_actuation import (
    centered_vector_state,
    projected_residue_sets,
    reachable_vector_residues,
    reachable_vector_subgroup,
    single_vector_action_horizon_class_count,
    single_vector_action_subgroup_order,
    vector_correlation_expansion_factor,
    vector_horizon_class_count,
    vector_horizon_repair_rank,
    vector_horizon_repaired_key,
    vector_stable_class_count,
    vector_stable_widths,
    vector_translation_certificate,
    vector_translation_descends,
)


class VectorChartTests(unittest.TestCase):
    def test_rectangular_centered_chart_reconstructs_exactly(self) -> None:
        for widths in ((1, 1), (3, 3), (3, 5), (5, 7)):
            for point in itertools.product(range(-12, 13), repeat=2):
                state = centered_vector_state(point, widths)
                self.assertEqual(state.reconstruct(), point)
                self.assertTrue(
                    all(0 <= detail < width for detail, width in zip(state.detail, widths))
                )

    def test_translation_certificate_matches_direct_vector_chart(self) -> None:
        widths = (3, 5)
        for point in itertools.product(range(-8, 9), repeat=2):
            for action in itertools.product(range(-4, 5), repeat=2):
                certificate = vector_translation_certificate(point, widths, action)
                direct = centered_vector_state(
                    tuple(point[index] + action[index] for index in range(2)),
                    widths,
                )
                self.assertEqual(certificate["quotient_after"], direct.quotient)
                self.assertEqual(certificate["detail_after"], direct.detail)

    def test_vector_translation_descends_componentwise(self) -> None:
        widths = (3, 5, 7)
        for action in itertools.product(range(-15, 16), repeat=3):
            expected = all(value % width == 0 for value, width in zip(action, widths))
            self.assertEqual(vector_translation_descends(widths, action), expected)


class VectorHorizonTests(unittest.TestCase):
    @staticmethod
    def _words(actions: tuple[tuple[int, ...], ...], horizon: int):
        words = [()]
        for length in range(1, horizon + 1):
            words.extend(itertools.product(actions, repeat=length))
        return tuple(words)

    @staticmethod
    def _signature(
        detail: tuple[int, ...],
        widths: tuple[int, ...],
        actions: tuple[tuple[int, ...], ...],
        horizon: int,
    ) -> tuple[tuple[int, ...], ...]:
        center = tuple((width - 1) // 2 for width in widths)
        point = tuple(detail[index] - center[index] for index in range(len(widths)))
        result = []
        for word in VectorHorizonTests._words(actions, horizon):
            total = [0] * len(widths)
            for action in word:
                for index, value in enumerate(action):
                    total[index] += value
            output = centered_vector_state(
                tuple(point[index] + total[index] for index in range(len(widths))),
                widths,
            )
            result.append(output.quotient)
        return tuple(result)

    def test_projection_product_count_matches_direct_future_partition(self) -> None:
        action_families = (
            ((1, 1),),
            ((1, 2),),
            ((1, 1), (2, 0)),
            ((2, 1), (0, 2)),
            ((-1, 2), (2, -1)),
        )
        for widths in ((1, 1), (3, 3), (3, 5), (5, 5)):
            for actions in action_families:
                for horizon in range(0, 4):
                    signatures = {
                        self._signature(detail, widths, actions, horizon)
                        for detail in itertools.product(*(range(width) for width in widths))
                    }
                    residues = reachable_vector_residues(widths, actions, horizon)
                    projections = projected_residue_sets(widths, residues)
                    predicted = 1
                    for projection in projections:
                        predicted *= len(projection)
                    self.assertEqual(len(signatures), predicted)
                    self.assertEqual(
                        vector_horizon_class_count(widths, actions, horizon),
                        predicted,
                    )

    def test_coordinate_rank_is_exact_minimal_partition_key(self) -> None:
        widths = (3, 5)
        actions = ((1, 2), (2, -1))
        horizon = 3
        center = tuple((width - 1) // 2 for width in widths)
        by_rank = {}
        by_signature = {}
        for detail in itertools.product(*(range(width) for width in widths)):
            point = tuple(detail[index] - center[index] for index in range(len(widths)))
            rank = vector_horizon_repair_rank(point, widths, actions, horizon)
            signature = self._signature(detail, widths, actions, horizon)
            previous_signature = by_rank.setdefault(rank, signature)
            self.assertEqual(previous_signature, signature)
            previous_rank = by_signature.setdefault(signature, rank)
            self.assertEqual(previous_rank, rank)
        self.assertEqual(len(by_rank), vector_horizon_class_count(widths, actions, horizon))

    def test_repaired_key_works_across_neighboring_vector_cells(self) -> None:
        widths = (3, 5)
        actions = ((1, 2), (-1, 1))
        horizon = 2
        by_key = {}
        for point in itertools.product(range(-10, 11), repeat=2):
            state = centered_vector_state(point, widths)
            detail = state.detail
            # build the future signature directly from the actual point
            values = []
            for word in self._words(actions, horizon):
                total = [0, 0]
                for action in word:
                    total[0] += action[0]
                    total[1] += action[1]
                values.append(
                    centered_vector_state(
                        (point[0] + total[0], point[1] + total[1]),
                        widths,
                    ).quotient
                )
            key = vector_horizon_repaired_key(point, widths, actions, horizon)
            previous = by_key.setdefault(key, tuple(values))
            self.assertEqual(previous, tuple(values))

    def test_diagonal_action_is_minimal_counterexample_to_subgroup_count(self) -> None:
        widths = (3, 3)
        actions = ((1, 1),)
        residues = reachable_vector_residues(widths, actions, 2)
        self.assertEqual(residues, ((0, 0), (1, 1), (2, 2)))
        self.assertEqual(len(residues), 3)
        self.assertEqual(vector_horizon_class_count(widths, actions, 2), 9)

    def test_bounded_two_dimensional_reconstruction(self) -> None:
        action_options = tuple(itertools.product(range(-2, 3), repeat=2))
        families = [(action,) for action in action_options]
        families.extend(
            (action_options[left], action_options[right])
            for left in range(0, len(action_options), 4)
            for right in range(left, len(action_options), 7)
        )
        for widths in itertools.product((1, 3, 5), repeat=2):
            for actions in families:
                for horizon in range(0, 3):
                    residues = reachable_vector_residues(widths, actions, horizon)
                    projections = projected_residue_sets(widths, residues)
                    predicted = 1
                    for projection in projections:
                        predicted *= len(projection)
                    self.assertEqual(
                        vector_horizon_class_count(widths, actions, horizon),
                        predicted,
                    )


class VectorStableTests(unittest.TestCase):
    def test_coordinatewise_gcd_widths_are_arbitrary_horizon_safe(self) -> None:
        cases = (
            ((3, 5), ((1, 1),)),
            ((3, 5), ((3, 2), (0, 4))),
            ((5, 7), ((10, 14), (-5, 21))),
            ((9, 15), ((6, 10), (12, -5))),
        )
        for widths, actions in cases:
            expected = []
            for index, width in enumerate(widths):
                common = width
                for action in actions:
                    common = gcd(common, abs(action[index]))
                expected.append(common)
            self.assertEqual(vector_stable_widths(widths, actions), tuple(expected))
            expected_count = 1
            for width, common in zip(widths, expected):
                expected_count *= width // common
            self.assertEqual(vector_stable_class_count(widths, actions), expected_count)

    def test_full_subgroup_size_can_understate_vector_precision_classes(self) -> None:
        widths = (3, 3)
        actions = ((1, 1),)
        subgroup = reachable_vector_subgroup(widths, actions)
        self.assertEqual(len(subgroup), 3)
        self.assertEqual(vector_stable_class_count(widths, actions), 9)
        self.assertEqual(vector_correlation_expansion_factor(widths, actions), 3)

    def test_correlation_expansion_factor_is_product_projection_index(self) -> None:
        for widths in ((3, 3), (3, 5), (5, 5)):
            for actions in (
                ((1, 1),),
                ((1, 2),),
                ((1, 0), (0, 1)),
                ((1, 1), (1, -1)),
            ):
                subgroup = reachable_vector_subgroup(widths, actions)
                projections = projected_residue_sets(widths, subgroup)
                rectangular = 1
                for projection in projections:
                    rectangular *= len(projection)
                self.assertEqual(
                    vector_correlation_expansion_factor(widths, actions),
                    rectangular // len(subgroup),
                )
                self.assertEqual(rectangular % len(subgroup), 0)

    def test_independent_action_axes_have_no_correlation_expansion(self) -> None:
        widths = (3, 5)
        actions = ((1, 0), (0, 1))
        self.assertEqual(vector_correlation_expansion_factor(widths, actions), 1)
        self.assertEqual(len(reachable_vector_subgroup(widths, actions)), 15)
        self.assertEqual(vector_stable_class_count(widths, actions), 15)

    def test_single_vector_action_closed_forms(self) -> None:
        for widths in ((3, 3), (3, 5), (5, 7)):
            for action in itertools.product(range(-3, 4), repeat=2):
                periods = tuple(
                    width // gcd(width, abs(value))
                    for width, value in zip(widths, action)
                )
                expected_order = 1
                for period in periods:
                    expected_order = lcm(expected_order, period)
                self.assertEqual(
                    single_vector_action_subgroup_order(widths, action),
                    expected_order,
                )
                for horizon in range(0, 8):
                    expected_count = 1
                    for period in periods:
                        expected_count *= min(horizon + 1, period)
                    self.assertEqual(
                        single_vector_action_horizon_class_count(widths, action, horizon),
                        expected_count,
                    )
                    self.assertEqual(
                        vector_horizon_class_count(widths, (action,), horizon),
                        expected_count,
                    )

    def test_diagonal_equal_period_growth_is_power_law(self) -> None:
        widths = (5, 5, 5)
        action = (1, 1, 1)
        self.assertEqual(single_vector_action_subgroup_order(widths, action), 5)
        self.assertEqual(
            tuple(single_vector_action_horizon_class_count(widths, action, h) for h in range(6)),
            (1, 8, 27, 64, 125, 125),
        )
        self.assertEqual(vector_stable_class_count(widths, (action,)), 125)
        self.assertEqual(vector_correlation_expansion_factor(widths, (action,)), 25)


if __name__ == "__main__":
    unittest.main()
