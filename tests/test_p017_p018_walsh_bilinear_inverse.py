from enterprise_math.p017_p018_walsh_bilinear_inverse import (
    additive_character_inverse_indicator,
    physical_dyadic_geometry,
    walsh_bilinear_divisor_rows,
    walsh_upper_sequence_weight,
)


def test_nonprime_physical_state_exposes_exact_inverse_residue_rows():
    # k=46, M=2162, s=2189=11*199, opposite=2135=5*7*61.
    data = walsh_bilinear_divisor_rows(46, 11, 199, critical_only=True)
    assert data["state"] == 2189
    assert data["opposite_state"] == 2135
    assert data["opposite_transverse_support"] == (5, 7)
    assert data["returned_divisors"] == (1, 5, 7, 35)
    rows = {row["divisor"]: row for row in data["inverse_residue_rows"]}
    assert rows[35]["inverse_residue_identity"] is True
    assert rows[35]["gcd_divisor_mn"] == 1
    assert rows[35]["actual_n_residue"] == rows[35]["target_n_residue"]


def test_additive_character_expansion_recovers_actual_divisor_indicator():
    for divisor in (5, 7, 35):
        data = additive_character_inverse_indicator(46, 11, 199, divisor)
        assert data["direct_congruence_indicator"] == 1
        assert data["additive_character_identity"] is True
        assert abs(data["additive_character_value"] - 1) < 1e-9


def test_sequence_weight_expands_as_squarefree_divisor_terms_on_composite_state():
    data = walsh_upper_sequence_weight(46, 2189)
    assert data["admissible"] is True
    assert data["opposite_transverse_support"] == (5, 7)
    assert data["squarefree_divisor_terms"] == (1, 5, 7, 35)
    assert data["walsh_sequence_weight"] == 4


def test_balanced_dyadic_geometry_is_square_root_thin():
    data = physical_dyadic_geometry(46, 32)
    assert data["balanced_square_root_regime"] is True
    assert data["rough_m_scale_M_over_N"] > 46
    assert data["rough_vertical_width_k_over_N"] < 2
    assert data["maximum_vertical_fiber_size"] <= 2
    assert data["total_physical_lattice_pairs"] > 0


def test_geometry_rows_are_exact_for_every_nonempty_fiber():
    data = physical_dyadic_geometry(46, 32)
    M = data["center"]
    for row in data["rows"]:
        n = row["n"]
        for m in range(row["m_min"], row["m_max"] + 1):
            if row["physical_m_count"]:
                assert M < m * n < M + 46
