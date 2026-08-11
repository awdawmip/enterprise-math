from enterprise_math.p022_barlow_twin_general_high_c18 import (
    c18_interior_twin_mod5_obstruction,
    c18_secondary_low,
    c18_source_lines_cover_mod5_at_gap_one,
    c18_source_low_boundary_mod5_obstruction,
    c18_source_low_boundary_parameter,
)


def test_interior_low_twin_has_a_mod5_obstruction_in_every_gap_class() -> None:
    expected = {
        0: "2b-1",
        1: "source-lines",
        2: "2b-1",
        3: "2b+1",
        4: "2b+1",
    }
    for residue, label in expected.items():
        gap = residue if residue else 5
        if gap == 1:
            gap = 6
        # Preserve only the requested mod-five class; divisibility by three is
        # not needed by this local helper.
        while gap % 5 != residue:
            gap += 1
        assert c18_interior_twin_mod5_obstruction(gap)[0] == label


def test_h_one_source_prime_lines_cover_every_rank_residue_mod5() -> None:
    expected = {
        0: "4r-5",
        1: "2(r+h)+1",
        2: "2r+1",
        3: "2r-1",
        4: "q",
    }
    for residue, label in expected.items():
        assert c18_source_lines_cover_mod5_at_gap_one(residue) == label


def test_source_low_boundary_forces_h_multiple_of_eighteen() -> None:
    t, rank, prime = c18_source_low_boundary_parameter(18)
    assert (t, rank, prime) == (1, 492, 3773)
    assert c18_secondary_low(rank, 18) == rank
    assert c18_source_low_boundary_mod5_obstruction(18) == "2r+1"

    t, rank, prime = c18_source_low_boundary_parameter(36)
    assert (t, rank, prime) == (2, 1845, 14453)
    assert c18_secondary_low(rank, 36) == rank
    assert c18_source_low_boundary_mod5_obstruction(36) == "4r-5"
