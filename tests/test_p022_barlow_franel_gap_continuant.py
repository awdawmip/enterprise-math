from enterprise_math.p022_barlow_franel_gap_continuant import (
    affine_gap_mod_value,
    companion_gap_transfer,
    eliminated_gap_transfer,
)


def test_first_fixed_gap_continuants_are_integral() -> None:
    assert tuple(eliminated_gap_transfer(r) for r in range(3, 9)) == (
        1,
        -848,
        2173312,
        -10712812544,
        88888688640000,
        -1120986365845045248,
    )


def test_affine_offset_elimination_is_exact_mod_q() -> None:
    # q=4r+2d-3; these examples only test the algebraic elimination and do not
    # assert that q is a genuine primitive terminal common divisor.
    for rank, d in ((6, 4), (9, 2), (15, 5), (21, 8)):
        q = 4 * rank + 2 * d - 3
        if q % 2 == 0:
            continue
        left, right = affine_gap_mod_value(rank, q, d)
        assert left == right


def test_gap_transfer_normalization() -> None:
    assert companion_gap_transfer(10, 0) == 0
    assert companion_gap_transfer(10, 1) == 1
    assert companion_gap_transfer(10, 2) == -(28 * 11**2 + 1)
