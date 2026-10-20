from enterprise_math.p017_p018_walsh_child_harmonic_staircase import (
    child_harmonic_shell,
    child_quotient_rows,
    declared_shell_ceiling,
)


def test_large_child_shell_has_only_quotient_one():
    # k=46, r=19 lies in (k/3,k/2); only a=1 may occur.
    data = declared_shell_ceiling(46, 19, 1)
    assert data["all_quotients_at_most_j"] is True
    assert all(row["quotient_a"] == 1 for row in data["quotient_rows"])


def test_next_child_shell_has_only_quotients_one_or_two():
    # k=46, r=13 lies in (k/4,k/3].
    data = declared_shell_ceiling(46, 13, 2)
    assert data["all_quotients_at_most_j"] is True
    assert all(row["quotient_a"] <= 2 for row in data["quotient_rows"])


def test_co_divisor_is_exact_euclidean_quotient():
    for k, r in ((46, 4), (46, 7), (82, 13), (100, 9)):
        for row in child_quotient_rows(k, r):
            m = row["conductor_m"]
            a = row["quotient_a"]
            assert k == a * m + r
            assert a == (k - r) // m


def test_deeper_child_opens_more_quotient_worlds_but_has_smaller_weight():
    for k, r in ((46, 4), (82, 7), (100, 9)):
        data = child_harmonic_shell(k, r)
        assert data["candidate_conductor_count"] <= data["maximum_quotient_world"]
        assert data["parent_weight_r_over_k"] <= data["reciprocal_weight_ceiling"]
        assert data["quotient_precision_opens_with_depth"] is True
