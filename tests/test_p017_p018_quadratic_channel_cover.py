from enterprise_math.p017_p018_quadratic_channel_cover import (
    RELAXED_K73_MIN_CENTERED_ROOT,
    RELAXED_K73_PRIMORIAL,
    actual_square_basin_residues,
    quadratic_allowed_residues,
    verify_k73_relaxed_counterexample,
)


def test_local_quadratic_allowed_residues_are_exact_square_images():
    allowed = quadratic_allowed_residues(7, 3)
    expected = tuple(sorted({((r * r - 3) * pow(2, -1, 7)) % 7 for r in range(7)}))
    assert allowed == expected


def test_k73_relaxed_quadratic_residues_cover_every_channel_index_but_require_huge_crt_height():
    data = verify_k73_relaxed_counterexample()
    assert data["complete_cover"] is True
    assert data["uncovered_indices"] == ()
    assert data["primorial"] == RELAXED_K73_PRIMORIAL
    assert data["minimum_centered_root_height"] == RELAXED_K73_MIN_CENTERED_ROOT
    assert data["minimum_centered_root_height"] > 73 + 1
    assert data["local_quadratic_condition_is_insufficient"] is True


def test_actual_square_basin_uses_the_special_low_height_common_root():
    data = actual_square_basin_residues(73)
    assert data["common_root"] == 74
    assert data["common_root_is_low_height"] is True
    # Legendre is known on this finite scale, but this regression only needs the
    # deterministic channel witness: the actual k=73 phase is not a full cover.
    assert data["complete_cover"] is False
    assert data["uncovered_indices"]
