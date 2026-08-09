from enterprise_math.relation_support_precision import (
    may_supported,
    must_supported,
    support_precision_profile,
)
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_coarse_threshold_can_understate_may_and_must() -> None:
    # Fine normalized values: A={0,10}, B={5,5}. Every cross distance is 5,
    # but the two aggregate normalized values both equal 5.
    sizes = (1, 1, 1, 1)
    totals = (0, 10, 5, 5)
    field = weighted_relation_field(sizes, totals)
    # Zero quotient classes are 0, 10, and the duplicated 5 class.
    profile = support_precision_profile(sizes, field, ((0, 1), (2,)))
    assert profile.may_threshold[0][1] == 5
    assert profile.must_threshold[0][1] == 5
    assert profile.coarse_threshold[0][1] == 0
    assert profile.hidden_must_defect[0][1] == 5
    assert profile.uncertainty_width[0][1] == 0
    assert not may_supported(profile, 0, 1, 4)
    assert may_supported(profile, 0, 1, 5)
    assert not must_supported(profile, 0, 1, 4)
    assert must_supported(profile, 0, 1, 5)


def test_coarse_threshold_can_exceed_may_threshold() -> None:
    # Fine normalized values: A={0,100}, B={1}. A fine pair is distance 1,
    # while the aggregate normalized A value is 50 and the coarse distance is 49.
    sizes = (1, 1, 1)
    totals = (0, 100, 1)
    field = weighted_relation_field(sizes, totals)
    profile = support_precision_profile(sizes, field, ((0, 1), (2,)))
    assert profile.may_threshold[0][1] == 1
    assert profile.must_threshold[0][1] == 99
    assert profile.coarse_threshold[0][1] == 49
    assert profile.uncertainty_width[0][1] == 98
    assert profile.hidden_must_defect[0][1] == 50
    assert may_supported(profile, 0, 1, 1)
    assert not must_supported(profile, 0, 1, 98)
    assert must_supported(profile, 0, 1, 99)


def test_may_must_interval_has_three_zone_semantics() -> None:
    sizes = (1, 1, 1)
    totals = (0, 4, 10)
    field = weighted_relation_field(sizes, totals)
    profile = support_precision_profile(sizes, field, ((0, 1), (2,)))
    # Cross fine distances are 10 and 6, so the query interval is [6,10].
    assert profile.may_threshold[0][1] == 6
    assert profile.must_threshold[0][1] == 10
    assert not may_supported(profile, 0, 1, 5)
    assert may_supported(profile, 0, 1, 6)
    assert not must_supported(profile, 0, 1, 9)
    assert must_supported(profile, 0, 1, 10)


def test_hidden_must_defect_is_nonnegative_for_weighted_blocks() -> None:
    sizes = (2, 3, 4, 5)
    totals = (1, 7, 9, 20)
    field = weighted_relation_field(sizes, totals)
    profile = support_precision_profile(sizes, field, ((0, 1), (2, 3)))
    for row in profile.hidden_must_defect:
        assert all(value >= 0 for value in row)
