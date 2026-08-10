from enterprise_math.closure_helper_invalidation import (
    required_fixed_helper_reset_count,
    stale_helper_counterexample,
)


def test_every_sequential_helper_can_corrupt_some_next_job_if_retained():
    for arity in range(3, 7):
        for helper_index in range(2, arity):
            witness = stale_helper_counterexample(arity, helper_index)
            assert witness.corrupts_raw_semantics
            assert "z" in witness.stale_compiled_raw_projection
            assert "z" not in witness.expected_next_raw_closure


def test_fixed_deletion_only_policy_must_clear_all_helpers():
    for arity in range(3, 8):
        assert required_fixed_helper_reset_count(arity) == arity - 2


def test_five_way_middle_helper_witness():
    witness = stale_helper_counterexample(5, 3)
    assert witness.helper == "e3"
    assert witness.prior_raw_seed == frozenset({"a1", "a2", "a3"})
    assert witness.next_raw_seed == frozenset({"a4", "a5"})
    assert witness.stale_internal_seed == frozenset({"e3", "a4", "a5"})
    assert witness.corrupts_raw_semantics
