from enterprise_math.legendre import primes_up_to
from enterprise_math.p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff
from enterprise_math.p017_p018_cutoff_gauge_flow import (
    cutoff_prime_jump,
    squarefree_cutoff_profile,
)


def test_prime_detector_is_cutoff_gauge_invariant_across_stable_p3_band():
    for k in (17, 31, 64, 100):
        z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
        z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
        profiles = [squarefree_cutoff_profile(k, y) for y in range(z3, z2 + 1)]
        prime_counts = {row["prime_count"] for row in profiles}
        assert len(prime_counts) == 1
        for row in profiles:
            assert row["prime_count"] == (
                row["rough_squarefree_count"]
                - row["support_moment_1"]
                + 2 * row["triple_count"]
            )
            assert 3 * row["prime_count"] == (
                2 * row["rough_squarefree_count"]
                - row["mobius_sum"]
                - row["support_moment_1"]
            )


def test_each_prime_cutoff_crossing_has_exact_semiprime_triple_jump_vector():
    for k in (31, 64, 100):
        z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
        z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
        for p in primes_up_to(z2):
            if p <= z3:
                continue
            row = cutoff_prime_jump(k, p)
            assert row["exact_cutoff_gauge_flow"] is True
            assert row["quadratic_invariant_jump"] == 0
            assert row["affine_invariant_jump"] == 0


def test_k100_gauge_endpoints_recover_same_prime_count():
    z3 = int(almost_prime_cutoff(100, 3)["cutoff"])
    z2 = int(almost_prime_cutoff(100, 2)["cutoff"])
    start = squarefree_cutoff_profile(100, z3)
    end = squarefree_cutoff_profile(100, z2)
    assert start["prime_count"] == end["prime_count"]
    assert end["triple_count"] == 0
