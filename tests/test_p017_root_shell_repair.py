from enterprise_math.p017_root_shell_repair import (
    minimal_root_shell_repair_alphabet_size,
    p2_bit_matches_shell,
    p2_shell_bit,
    repaired_root_images,
    repaired_root_overlaps,
    root_shell_split_multiplicities,
)
from enterprise_math.quotient_window import square_basin_window


def test_complete_small_collision_classification_is_pinned() -> None:
    expected = {
        5: {3: 2},
        6: {4: 2},
        8: {5: 2},
    }
    actual = {}
    for k in range(4, 12):
        splits = {
            root: multiplicity
            for root, multiplicity in root_shell_split_multiplicities(k).items()
            if multiplicity > 1
        }
        if splits:
            actual[k] = splits
    assert actual == expected


def test_p2_bit_is_exact_shell_indicator() -> None:
    for k in range(4, 500):
        assert p2_bit_matches_shell(k)


def test_p2_threshold_separates_actual_p2_and_p3_windows() -> None:
    for k in range(4, 100):
        w2 = square_basin_window(k, 2)
        if w2 is not None:
            assert all(p2_shell_bit(k, q) == 1 for q in range(w2.lo, w2.hi + 1))
        w3 = square_basin_window(k, 3)
        if w3 is not None:
            assert all(p2_shell_bit(k, q) == 0 for q in range(w3.lo, w3.hi + 1))


def test_repaired_root_images_are_disjoint_from_k4_onward() -> None:
    for k in range(4, 2000):
        assert repaired_root_overlaps(k) == (), (k, repaired_root_overlaps(k))


def test_exact_minimum_repair_alphabet_profile() -> None:
    for k in range(4, 500):
        expected = 2 if k in {5, 6, 8} else 1
        assert minimal_root_shell_repair_alphabet_size(k) == expected


def test_repaired_images_pin_the_three_collision_repairs() -> None:
    assert (3, 1) in repaired_root_images(5)[2]
    assert (3, 0) in repaired_root_images(5)[3]

    assert (4, 1) in repaired_root_images(6)[2]
    assert (4, 0) in repaired_root_images(6)[3]

    assert (5, 1) in repaired_root_images(8)[2]
    assert (5, 0) in repaired_root_images(8)[3]
