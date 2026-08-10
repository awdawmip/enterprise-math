from enterprise_math.closure_helper_cache_memory import (
    helper_cache_memory_report,
    saturated_helper_section,
)


def test_saturated_helpers_are_a_deterministic_cache_over_raw_closed_states():
    for arity in range(4, 7):
        report = helper_cache_memory_report(arity)
        assert report.raw_closed_state_count == report.saturated_internal_state_count
        assert report.saturated_section_injective
        assert report.saturated_projection_identity


def test_transient_helpers_are_runtime_memory_under_stepwise_future():
    report = helper_cache_memory_report(4)
    assert report.transient_left != report.transient_right
    assert report.common_raw_projection == frozenset({"a1", "a2", "a3"})
    assert report.left_has_future_update
    assert not report.right_has_future_update
    assert report.runtime_future_separated


def test_saturated_section_is_functional_and_raw_projection_recovers_key():
    section = saturated_helper_section(5)
    assert len(set(section.values())) == len(section)
    raw_labels = frozenset({"a1", "a2", "a3", "a4", "a5", "z"})
    for raw, internal in section.items():
        assert frozenset(label for label in internal if label in raw_labels) == raw
