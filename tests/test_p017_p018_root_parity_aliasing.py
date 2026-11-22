from enterprise_math.p017_p018_root_parity_aliasing import root_parity_aliasing_profile


def test_root_p3_negative_mobius_aliases_prime_and_squarefree_triple() -> None:
    for k in (4, 5, 10, 17, 31, 100, 203, 500, 1000):
        data = root_parity_aliasing_profile(k)
        assert data["z3_negative_sign_aliases_prime_and_squarefree_triple"]
        assert data["z2_negative_sign_is_prime_selector"]
        assert data["status"] == "ROOT_PARITY_ALIASING_LADDER"

        for value, offset in data["z3_negative_prime_rows"]:
            assert value == k * k + offset
        for value, offset, factors in data["z3_negative_squarefree_triple_rows"]:
            assert len(factors) == 3 == len(set(factors))
            assert value == factors[0] * factors[1] * factors[2] == k * k + offset


def test_root_p2_negative_mobius_is_exact_prime_selector() -> None:
    for k in (17, 31, 100, 203, 500):
        data = root_parity_aliasing_profile(k)
        z2_negative = {offset for _value, offset in data["z2_negative_prime_rows"]}
        z3_prime = {offset for _value, offset in data["z3_negative_prime_rows"]}
        # Every prime survives every root cutoff, so the negative z2 rows are
        # exactly the same prime offsets already present in the z3 alias class.
        assert z2_negative == z3_prime
