import pytest

from enterprise_math.p022_barlow_twin_escape_midpoint import boundary_escape_residue_classes


def test_surviving_boundary_classes_are_17_or_35_mod_72() -> None:
    assert boundary_escape_residue_classes(6, 17) == (1, 17)
    assert boundary_escape_residue_classes(36, 107) == (3, 35)
    assert boundary_escape_residue_classes(156, 467) == (3, 35)
    assert boundary_escape_residue_classes(174, 521) == (1, 17)


def test_midpoint_zero_excludes_5_and_7_mod_8_boundary_primes() -> None:
    # These ranks satisfy the twin-boundary geometry and q=3r-1 is prime.
    # The forced midpoint zero is visible because q-2=3(r-1) is composite.
    with pytest.raises(ValueError):
        boundary_escape_residue_classes(216, 647)  # 647 = 7 mod 8
    with pytest.raises(ValueError):
        boundary_escape_residue_classes(546, 1637)  # 1637 = 5 mod 8
