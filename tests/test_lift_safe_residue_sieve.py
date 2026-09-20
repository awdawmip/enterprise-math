import math
import random

from enterprise_math.lift_safe_residue_sieve import (
    ALL,
    NEVER,
    ONE_CLASS,
    divisibility_observer_globally_descends,
    lift_divisibility_class,
    lift_value,
    repair_period,
    surviving_window,
    wheel_rejects_lift,
)


def brute_class(prefix, stride, modulus, x):
    return (prefix + stride * x) % modulus == 0


def test_power_false_negative_witness_is_preserved():
    M = 16_796_160_000
    r = 7
    x = 2
    p = r + M * x
    assert p == 33_592_320_007
    assert math.gcd(r, 30_030) == 7
    assert math.gcd(p, 30_030) == 1
    cert7 = lift_divisibility_class(r, M, 7)
    assert cert7.status == ONE_CLASS
    assert cert7.period == 7
    assert cert7.residue == 0
    assert not cert7.contains(x)
    assert not wheel_rejects_lift(r, M, x, (2, 3, 5, 7, 11, 13))


def test_constant_fibers_when_modulus_divides_stride():
    M = 2**12 * 3**8 * 5**4
    assert divisibility_observer_globally_descends(M, 2)
    assert divisibility_observer_globally_descends(M, 3)
    assert divisibility_observer_globally_descends(M, 5)
    assert not divisibility_observer_globally_descends(M, 7)
    assert lift_divisibility_class(7, M, 2).status == NEVER
    assert lift_divisibility_class(6, M, 2).status == ALL


def test_general_linear_congruence_certificate_matches_bruteforce():
    rng = random.Random(20260920)
    for _ in range(1000):
        prefix = rng.randint(-100, 100)
        stride = rng.randint(1, 80)
        modulus = rng.randint(2, 80)
        cert = lift_divisibility_class(prefix, stride, modulus)
        period = modulus // math.gcd(stride, modulus)
        for x in range(0, max(1, period) * 2):
            assert cert.contains(x) == brute_class(prefix, stride, modulus, x)


def test_window_filter_matches_direct_candidate_gcd():
    rng = random.Random(20260921)
    primes = (2, 3, 5, 7, 11, 13)
    W = math.prod(primes)
    for _ in range(200):
        prefix = rng.randint(1, 200)
        stride = rng.randint(1, 300)
        got = surviving_window(prefix, stride, 0, 200, primes)
        want = tuple(
            x
            for x in range(200)
            if (
                math.gcd(lift_value(prefix, stride, x), W) == 1
                or lift_value(prefix, stride, x) in primes
            )
        )
        assert got == want


def test_repair_period_preserves_all_wheel_observations():
    M = 16_796_160_000
    r = 7
    primes = (2, 3, 5, 7, 11, 13)
    P = repair_period(r, M, primes)
    assert P == math.lcm(7, 11, 13)
    for x in range(P):
        y = x + P
        for p in primes:
            assert ((r + M * x) % p == 0) == ((r + M * y) % p == 0)
