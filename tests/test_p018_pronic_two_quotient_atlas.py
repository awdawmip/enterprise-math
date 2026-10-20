from enterprise_math.p018_pronic_two_quotient_atlas import (
    pronic_two_quotient_state,
    two_quotient_cell_width_ceiling,
    two_quotient_cells,
    two_quotient_kloosterman_channel,
)


def test_two_quotient_state_linearizes_Q_exactly():
    for k in (46, 82, 862):
        for n in range(1, min(k, 80) + 1):
            data = pronic_two_quotient_state(k, n)
            assert data["center_quotient_Q"] == data["linearized_center_quotient"]
            assert data["two_quotient_state_exact"] is True


def test_kloosterman_channel_identity_matches_euclidean_channel():
    for k, n, d in (
        (46, 11, 35),
        (82, 17, 15),
        (862, 37, 55),
        (8191, 127, 105),
    ):
        data = two_quotient_kloosterman_channel(k, n, d)
        assert data["two_quotient_kloosterman_identity"] is True
        assert data["euclidean_channel_residue"] == data["linear_inverse_kloosterman_residue"]


def test_fixed_a_cells_are_consecutive_and_obey_convexity_width_ceiling():
    for k in (46, 82, 862):
        for a in range(1, min(k, 30) + 1):
            data = two_quotient_cells(k, a)
            assert data["all_cells_within_ceiling"] is True
            assert data["observed_max_cell_width"] <= data["integer_n_cell_width_ceiling"]
            for _c, values in data["cells"]:
                if values:
                    assert values == tuple(range(values[0], values[-1] + 1))


def test_cell_ceiling_enters_bounded_width_past_cube_root_scale():
    k = 8191
    # This test records the actual integer bound rather than relying on floating cube roots.
    for a in range(21, 91):
        data = two_quotient_cell_width_ceiling(k, a)
        # Around and above k^(1/3), the ceiling is a small absolute integer.
        assert data["integer_n_cell_width_ceiling"] <= 3
