import pytest

from enterprise_math.p022_barlow_twin_escape_reflection_transport import (
    boundary_hidden_interior_reflection_obstruction,
    boundary_reflection_partner,
    intermediate_tail_reflection_obstruction,
    intermediate_transport_index,
    intermediate_transport_survivor,
)


def test_boundary_reflection_swaps_source_and_endpoint() -> None:
    # r=36 is a twin center and q=3r-1=107 is prime.
    assert boundary_reflection_partner(36, 36) == 70
    assert boundary_reflection_partner(36, 70) == 36


def test_hidden_boundary_interior_twin_reflects_to_nonhidden_site() -> None:
    # s=51 is a twin center (101,103), but its q=107 reflection is 55,
    # whose upper odd boundary 111 is composite.
    assert boundary_hidden_interior_reflection_obstruction(36, 51) == 55

    # The final interior twin center s=69 reflects to r+1=37, adjacent to the
    # primitive source and therefore forbidden as another q-zero.
    assert boundary_hidden_interior_reflection_obstruction(36, 69) == 37


def test_intermediate_reflected_endpoint_must_be_a_twin_center() -> None:
    # r=30, q=113 gives s=54, another twin center, and survives the midpoint
    # residue sieve in class 17 mod 24.
    assert intermediate_transport_index(30, 113) == 54
    assert intermediate_transport_survivor(30, 113) == (54, 17)

    # r=69, q=227 gives the other surviving class 11 mod 24.
    assert intermediate_transport_survivor(69, 227) == (90, 11)

    # r=21, q=67 reflects to s=26, which is not a twin center.
    with pytest.raises(ValueError):
        intermediate_transport_survivor(21, 67)


def test_forced_midpoint_kills_intermediate_5_or_7_mod8_candidates() -> None:
    # r=21, q=71 reflects the endpoint to twin center s=30, but q=7 mod8.
    # The forced Franel midpoint zero is internal and visible.
    assert intermediate_transport_index(21, 71) == 30
    with pytest.raises(ValueError):
        intermediate_transport_survivor(21, 71)


def test_no_second_hidden_twin_can_live_above_transported_endpoint() -> None:
    # r=69,q=233 survives with transported twin s=96.  The higher twin center
    # 99 reflects to 133, which cannot be a twin center because q-1=1 mod3.
    assert intermediate_transport_survivor(69, 233) == (96, 17)
    assert intermediate_tail_reflection_obstruction(69, 233, 99) == 133
