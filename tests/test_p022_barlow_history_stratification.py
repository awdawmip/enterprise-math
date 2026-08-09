from enterprise_math.p022_barlow_coordination_history import (
    unordered_drift_pair_successors,
)
from enterprise_math.p022_barlow_history_stratification import (
    coordination_history_from_terminal_stratified_profile,
    drift_history_from_terminal_stratified_profile,
    terminal_stratified_profile_from_drift_history,
)


def _all_drift_histories(radius: int):
    histories = {((0, 0),)}
    for _ in range(radius):
        histories = {
            history + (successor,)
            for history in histories
            for successor in unordered_drift_pair_successors(history[-1])
        }
    return histories


def _coordination_history(drift_history):
    from enterprise_math.p022_barlow_coordination import (
        barlow_shell_vertex_count_from_extreme_imbalances,
    )

    output = [1]
    for radius in range(1, len(drift_history)):
        left, right = drift_history[radius]
        output.append(
            barlow_shell_vertex_count_from_extreme_imbalances(radius, left, right)
        )
    return tuple(output)


def test_terminal_profile_roundtrips_every_short_hidden_history() -> None:
    for radius in range(0, 9):
        for history in _all_drift_histories(radius):
            profile = terminal_stratified_profile_from_drift_history(radius, history)
            assert drift_history_from_terminal_stratified_profile(profile) == history
            assert coordination_history_from_terminal_stratified_profile(
                profile
            ) == _coordination_history(history)


def test_coordination_history_and_terminal_profile_are_bijective_on_reachable_states() -> None:
    for radius in range(1, 8):
        history_to_profile = {}
        profile_to_coordination = {}
        for history in _all_drift_histories(radius):
            coordination = _coordination_history(history)
            profile = terminal_stratified_profile_from_drift_history(radius, history)
            if coordination in history_to_profile:
                assert history_to_profile[coordination] == profile
            history_to_profile[coordination] = profile
            if profile in profile_to_coordination:
                assert profile_to_coordination[profile] == coordination
            profile_to_coordination[profile] = coordination

        assert len(history_to_profile) == len(profile_to_coordination)


def test_extreme_layer_needs_cardinality_because_path_total_is_constant() -> None:
    from enterprise_math.p022_barlow_layer_tradeoff import (
        layer_ball_slice_count,
        layer_shell_geodesic_total,
    )

    radius = 6
    path_totals = {
        layer_shell_geodesic_total(radius, radius, drift)
        for drift in range(0, radius + 1, 2)
    }
    vertex_counts = {
        layer_ball_slice_count(radius, radius, drift)
        for drift in range(0, radius + 1, 2)
    }
    assert path_totals == {3**radius}
    assert len(vertex_counts) == radius // 2 + 1


def test_nonextreme_layer_path_total_is_injective_in_absolute_drift() -> None:
    from enterprise_math.p022_barlow_layer_tradeoff import layer_shell_geodesic_total

    for radius in range(2, 12):
        for height in range(1, radius):
            values = [
                layer_shell_geodesic_total(radius, height, drift)
                for drift in range(height % 2, height + 1, 2)
            ]
            assert values == sorted(values)
            assert len(values) == len(set(values))
