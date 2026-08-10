from enterprise_math.closure_async_progress_poset import helper_ideals
from enterprise_math.closure_async_query_ladder import enabled_helpers
from enterprise_math.closure_enabled_frontier import (
    enabled_frontier_report,
    reconstruct_completed_from_enabled,
)


def test_enabled_frontier_is_injective_and_reconstructs_every_ideal():
    for arity in range(4, 9):
        report = enabled_frontier_report(arity)
        assert report.injective
        assert report.reconstruction_verified
        assert report.enabled_signature_count == report.ideal_count
        assert report.maximum_enabled_frontier_size == report.helper_poset_width


def test_reconstruction_round_trip():
    for arity in (4, 5, 8):
        for ideal in helper_ideals(arity):
            signature = enabled_helpers(arity, ideal)
            assert reconstruct_completed_from_enabled(arity, signature) == ideal


def test_four_way_enabled_frontiers_are_all_antichain_states():
    ideals = tuple(helper_ideals(4))
    signatures = {enabled_helpers(4, ideal) for ideal in ideals}
    assert len(ideals) == len(signatures) == 4
    assert frozenset() in signatures  # terminal ideal
    assert max(map(len, signatures)) == 2
