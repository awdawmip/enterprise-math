from enterprise_math.p017_p018_walsh_root_kloosterman import (
    even_conductor_reciprocity_cosine,
    root_fourier_kloosterman_split,
    signed_unity_root_from_split,
)


def test_signed_unity_root_from_coprime_split():
    data = signed_unity_root_from_split(5, 7)
    assert data["q"] == 35
    assert data["root_u"] % 5 == 1
    assert data["root_u"] % 7 == 6


def test_root_fourier_equals_divisor_kloosterman_split():
    for primes in ((3,), (3, 5), (3, 5, 7)):
        for h in (1, 2, 5):
            data = root_fourier_kloosterman_split(46, primes, h)
            assert data["root_kloosterman_identity"] is True


def test_even_conductor_reciprocity_pairs_to_real_cosines():
    for primes in ((3, 5), (3, 7), (3, 5, 7, 11)):
        for h in (1, 2, 3):
            data = even_conductor_reciprocity_cosine(46, primes, h)
            assert data["even_conductor_real_fourier"] is True
            assert data["additive_reciprocity_pairing"] is True
