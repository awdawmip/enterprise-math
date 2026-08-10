from itertools import product

from enterprise_math.p017_p018_square_phase_crt import (
    glue_negative_square_phases,
    negative_square_residues,
    verify_phase_covering_lift,
)


def test_negative_square_residue_cardinality():
    assert negative_square_residues(2) == (0, 1)
    for p in (3, 5, 7, 11, 13):
        assert len(negative_square_residues(p)) == (p + 1) // 2


def test_arbitrary_local_negative_square_phases_glue_across_primes():
    primes = (2, 3, 5, 7)
    phase_sets = [negative_square_residues(p) for p in primes]
    for phases in product(*phase_sets):
        data = glue_negative_square_phases(zip(primes, phases))
        assert data["all_local_negative_square_choices_glue"] is True
        root = data["crt_root"]
        modulus = data["crt_modulus"]
        assert 0 <= root < modulus
        for p, phase in data["assignments"]:
            assert (-root * root) % p == phase


def test_root_class_multiplicity_factors_over_local_root_choices():
    data = glue_negative_square_phases(((3, -1), (5, -1), (7, -1)))
    expected = 1
    for _p, _phase, roots in data["local_roots"]:
        expected *= len(roots)
    assert data["root_class_multiplicity"] == expected


def test_a_local_square_cover_is_automatically_a_global_crt_square_cover():
    # x=1 gives phases -1 mod p.  With primes 2,3,5 the four offsets 1..4
    # are all covered: x^2+r is 2,3,4,5.
    assignments = tuple((p, (-1) % p) for p in (2, 3, 5))
    data = verify_phase_covering_lift(assignments, 4)
    assert data["locally_covers_horizon"] is True
    assert data["glued_root_covers_horizon"] is True
    root = data["crt_root"]
    for offset, p in data["covering_witnesses"]:
        assert (root * root + offset) % p == 0


def test_local_square_admissibility_does_not_claim_small_lift_minimality():
    data = glue_negative_square_phases(((3, 0), (5, -1), (7, -4)))
    assert data["all_local_negative_square_choices_glue"] is True
    # The theorem returns one canonical residue class only.  It deliberately
    # makes no assertion that this representative is the least positive square
    # root relevant to any covering problem.
    assert 0 <= data["crt_root"] < data["crt_modulus"]
