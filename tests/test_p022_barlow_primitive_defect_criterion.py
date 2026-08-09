from enterprise_math.p022_barlow_primitive_defect_criterion import (
    is_primitive_franel_divisor,
    primitive_certificate_diagonal,
    primitive_certificate_is_unimodular,
    primitive_defect_pivot,
    primitive_row_is_triangular,
)

# One exact simple primitive Franel divisor for every composite odd-boundary
# segment through n=20.  These are verification examples, not a claim that such
# a marker exists globally.
MARKERS_THROUGH_20 = (
    (5, 563),
    (8, 369581),
    (11, 337),
    (13, 2141),
    (14, 12148537),
    (17, 59),
    (18, 37),
    (20, 151),
)


def test_declared_markers_are_first_occurrence_franel_divisors() -> None:
    for segment, prime in MARKERS_THROUGH_20:
        assert is_primitive_franel_divisor(segment, prime)
        assert primitive_defect_pivot(segment, prime) == 1


def test_primitive_rows_are_triangular_in_composite_segment_order() -> None:
    earlier = []
    for segment, prime in MARKERS_THROUGH_20:
        assert primitive_row_is_triangular(segment, prime, tuple(earlier))
        earlier.append(segment)


def test_primitive_marker_certificate_is_unimodular_through_20() -> None:
    diagonal = primitive_certificate_diagonal(20, MARKERS_THROUGH_20)
    assert diagonal == (1,) * 9  # tail plus eight composite defects
    assert primitive_certificate_is_unimodular(20, MARKERS_THROUGH_20)


def test_nonprimitive_old_prime_is_rejected() -> None:
    # 5 divides earlier Franel terms before segment 11, so it is not a primitive
    # marker for F_11 even though 5 divides F_11.
    assert not is_primitive_franel_divisor(11, 5)
