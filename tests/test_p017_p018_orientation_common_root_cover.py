from enterprise_math.p017_p018_orientation_common_root_cover import (
    K73_COMMON_ROOT_RESIDUES,
    k73_common_root_negative_witness,
    root_height_exponent_from_short_prime_exponent,
    symmetric_cover_profile,
)


def test_k73_common_root_assignment_covers_both_orientations_at_every_odd_radius():
    data = k73_common_root_negative_witness()
    assert data["complete_signed_odd_cover"] is True
    assert all(row["both_orientations_covered"] for row in data["rows"])
    assert data["centered_root_height"] == 92747351382044010019593226
    assert data["physical_pronic_center"] == 5402
    assert data["centered_root_height"] > data["physical_pronic_center"]


def test_crt_root_realizes_every_stored_local_residue():
    data = symmetric_cover_profile(73, dict(K73_COMMON_ROOT_RESIDUES))
    root = data["canonical_root"]
    for prime, residue in K73_COMMON_ROOT_RESIDUES.items():
        assert root % prime == residue % prime


def test_short_prime_exponent_translates_to_root_height_exponent():
    exponent = root_height_exponent_from_short_prime_exponent(0.52)
    assert abs(exponent - (25 / 13)) < 1e-12
    assert exponent < 2
    assert root_height_exponent_from_short_prime_exponent(0.49) > 2
