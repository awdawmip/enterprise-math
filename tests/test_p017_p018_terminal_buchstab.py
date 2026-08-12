from enterprise_math.legendre import is_prime
from enterprise_math.p017_p018_terminal_buchstab import (
    high_prime_odd_quotient_candidates,
    terminal_buchstab_staircase,
)


def test_high_prime_candidates_are_explicit_and_complete():
    for k in range(10, 61):
        for p in range(k // 2 + 1, k + 1):
            if not is_prime(p):
                continue
            data = high_prime_odd_quotient_candidates(k, p)
            candidates = data["candidates"]
            assert 1 <= len(candidates) <= 2
            for item in candidates:
                q = item["q"]
                offset = item["offset"]
                assert q % 2 == 1
                assert k < q < 2 * k + 4
                assert 1 <= offset <= 2 * k
                assert p * q == k * k + offset
            if len(candidates) == 2:
                assert candidates[1]["q"] == candidates[0]["q"] + 2
                assert candidates[0]["half"] == 1
                assert candidates[1]["half"] == 2


def test_primary_candidate_is_a_goldbach_shell_reflection():
    for k in range(10, 81):
        for p in range(k // 2 + 1, k + 1):
            if not is_prime(p):
                continue
            data = high_prime_odd_quotient_candidates(k, p)
            primary = data["candidates"][0]
            u = data["shell_index"]
            assert p + primary["q"] == 2 * (k + u + 1)
            a = k - p
            assert 2 * p * u <= a * a < 2 * p * (u + 1)


def test_terminal_staircase_recovers_exact_semiprime_deletion_and_prime_gap():
    for k in range(10, 81):
        data = terminal_buchstab_staircase(k)
        assert data["terminal_identity_exact"] is True
        assert data["recovered_prime_count"] == data["direct_prime_count"]
        assert data["half_rough_count"] == (
            data["recovered_prime_count"] + data["deletion_count"]
        )
        assert all(step["jump"] in (0, 1, 2) for step in data["steps"])


def test_double_staircase_jump_is_exactly_a_cross_half_twin_event():
    for k in range(10, 101):
        data = terminal_buchstab_staircase(k)
        for step in data["steps"]:
            if step["jump"] != 2:
                continue
            first, second = step["prime_candidates"]
            assert first["half"] == 1
            assert second["half"] == 2
            assert second["q"] - first["q"] == 2
            assert is_prime(first["q"])
            assert is_prime(second["q"])
