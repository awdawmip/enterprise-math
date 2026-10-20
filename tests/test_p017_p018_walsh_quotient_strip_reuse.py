from enterprise_math.p017_p018_walsh_quotient_strip_reuse import (
    first_two_strip_pareto,
    quotient_strip_reuse_ceiling,
)


def test_first_strip_is_unsmoothed_but_single_use():
    # k=100: odd m in (50,100] has quotient strip a=1.
    for m in (51, 67, 99):
        data = first_two_strip_pareto(100, m)
        assert data["quotient_strip_a"] == 1
        assert data["reciprocal_mobius_kernel"] == 1
        assert data["strip_reuse_ceiling"] == 1
        assert data["first_strip_single_use"] is True


def test_second_strip_is_unsmoothed_but_reuse_at_most_two():
    # k=100: m in (100/3,50] has quotient strip a=2.
    for m in (35, 41, 49):
        data = first_two_strip_pareto(100, m)
        assert data["quotient_strip_a"] == 2
        assert data["reciprocal_mobius_kernel"] == 1
        assert data["strip_reuse_ceiling"] == 2
        assert data["second_strip_reuse_at_most_two"] is True


def test_general_strip_reuse_ceiling_is_floor_a_over_two_plus_one():
    for k in (100, 257):
        for m in range(3, k + 5, 2):
            data = quotient_strip_reuse_ceiling(k, m)
            a = data["quotient_strip_a"]
            if a == 0:
                assert data["strip_reuse_ceiling"] == 1
            else:
                assert data["strip_reuse_ceiling"] == a // 2 + 1
            assert data["exact_one_class_capacity_ceiling"] <= data["strip_reuse_ceiling"]
