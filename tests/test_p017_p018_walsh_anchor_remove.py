from enterprise_math.p017_p018_walsh_anchor_remove import (
    anchor_removed_root_column,
    raw_signed_root_column,
)


def test_raw_root_column_uses_rescaled_center_only():
    assert raw_signed_root_column(20, 100, (3, 7)) == raw_signed_root_column(20, 100 + 3 * 7, (3, 7))


def test_anchor_surviving_column_is_mobius_sum_of_rescaled_raw_columns():
    for k, primes in ((46, (3, 5)), (82, (3, 7)), (325, (7, 11))):
        data = anchor_removed_root_column(k, primes)
        assert data["anchor_removal_identity"] is True
        assert data["direct_anchor_surviving_column"] == data["mobius_rescaled_raw_sum"]
