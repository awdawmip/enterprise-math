#!/usr/bin/env python3
"""
Task-local regression checker for
RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION.

This checker is evidence, not the universal proof.  It independently checks:
1. exact kernel recurrence against direct binomial integers;
2. the fixed-public-prefix finite-support adversarial mechanism;
3. zero-amplification on semiprimes outside that support;
4. synchronized gcd=N examples for the fixed-prefix route;
5. the accepted N-only valuation-wall splitter on all prime pairs 5<=p<q<1000;
6. the exact synchronized fallback inequalities used by that splitter.

No factor is supplied to the splitter. Hidden p,q are used only by the
regression oracle after the public-N computation finishes.
"""
from math import comb, gcd, isqrt, prod
from collections import Counter

def sieve(limit: int):
    mark = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        mark[0] = 0
    if limit >= 1:
        mark[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if mark[p]:
            start = p * p
            mark[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i, v in enumerate(mark) if v]

def A_direct(s: int) -> int:
    return comb(2 * s, s) ** 2 * comb(3 * s, s)

def B(s: int) -> int:
    return (216 ** s) * A_direct(s)

def F(L: int) -> int:
    ds = [2 * m + 1 for m in range(L + 1)]
    return sum(
        ((-1) ** (L - j))
        * B(j)
        * prod(ds[m] for m in range(L + 1) if m != j)
        for j in range(L + 1)
    )

def check_exact_recurrence(max_s: int = 40):
    a = 1
    checks = 0
    for s in range(1, max_s + 1):
        num = 6 * (2 * s - 1) * (3 * s - 2) * (3 * s - 1)
        den = s ** 3
        assert (a * num) % den == 0
        a = (a * num) // den
        assert a == A_direct(s)
        checks += 1
    return checks

def residue_A(N: int, s: int):
    a = 1 % N
    for k in range(1, s + 1):
        g = gcd(k, N)
        if 1 < g < N:
            return None, g
        den = pow(k, 3, N)
        a = (
            a
            * (6 * (2 * k - 1) * (3 * k - 2) * (3 * k - 1) % N)
            * pow(den, -1, N)
        ) % N
    return a, None

def nonly_split(N: int):
    a = 1 % N
    next_dyadic = 1
    first_s = None
    first_g = None
    recurrence_steps = 0

    for s in range(1, isqrt(N) + 2):
        gden = gcd(s, N)
        if 1 < gden < N:
            return gden, "DENOMINATOR_GCD", s, recurrence_steps, False

        a = (
            a
            * (6 * (2 * s - 1) * (3 * s - 2) * (3 * s - 1) % N)
            * pow(pow(s, 3, N), -1, N)
        ) % N
        recurrence_steps += 1

        if s == next_dyadic:
            g = gcd(a, N)
            if g > 1:
                first_s, first_g = s, g
                if g < N:
                    return g, "DYADIC", s, recurrence_steps, False
                break
            next_dyadic *= 2

    assert first_g == N
    t = isqrt(N) // 3
    for u, label in ((t, "FALLBACK_T"), (t + 1, "FALLBACK_T1")):
        r, factor_from_den = residue_A(N, u)
        if factor_from_den is not None:
            return factor_from_den, label + "_DEN", u, recurrence_steps + u, True
        g = gcd(r, N)
        if 1 < g < N:
            return g, label, u, recurrence_steps + u, True

    raise AssertionError(("fallback failed", N, first_s, t))

def fixed_prefix_no_go(seed_max: int = 8):
    seeds = list(range(seed_max + 1))
    fs = [F(L) for L in seeds]
    primes = [p for p in sieve(20000) if p > 3]

    outside = [p for p in primes if all(x % p for x in fs)]
    assert len(outside) >= 80

    adversarial_semiprimes = 0
    alpha_zero = 0
    for i in range(0, 60, 2):
        p, q = outside[i], outside[i + 1]
        N = p * q
        gcds = [gcd(x, N) for x in fs]
        assert set(gcds) == {1}
        adversarial_semiprimes += 1
        alpha = sum(1 for g in gcds if 1 < g < N) / len(gcds)
        assert alpha == 0.0
        for k in (1, 2, 8, 64):
            amplified = 1.0 - (1.0 - alpha) ** k
            assert amplified == 0.0
        alpha_zero += 1

    # Infinite prime-power family mechanism: any prime outside support gives gcd=1
    # for every fixed seed at all positive powers as well.
    prime_power_checks = 0
    for p in outside[:20]:
        for exponent in (2, 3, 4):
            N = p ** exponent
            assert all(gcd(x, N) == 1 for x in fs)
            prime_power_checks += 1

    # Multifactor analogue: if every prime factor lies outside support, every
    # observed gcd remains 1.
    multifactor_checks = 0
    for i in range(0, 30, 3):
        N = outside[i] * outside[i + 1] * outside[i + 2]
        assert all(gcd(x, N) == 1 for x in fs)
        multifactor_checks += 1

    # A synchronized proper-failure example: F_3 is divisible by both 5 and 7,
    # so the bridge observable returns N rather than splitting N=35.
    assert gcd(F(3), 35) == 35

    return {
        "seeds": len(seeds),
        "adversarial_semiprimes": adversarial_semiprimes,
        "alpha_zero_cases": alpha_zero,
        "prime_power_checks": prime_power_checks,
        "multifactor_checks": multifactor_checks,
        "synchronized_example": "L=3,N=35,gcd(F_3,N)=N",
    }

def check_nonly_splitter():
    primes = [p for p in sieve(999) if p >= 5]
    mode_counts = Counter()
    exhaustive = 0
    synchronized = 0
    near_neighbor = 0
    unbalanced = 0
    max_steps_over_p_num = 0
    max_steps_over_p_den = 1

    for i, p in enumerate(primes):
        for j in range(i + 1, len(primes)):
            q = primes[j]
            N = p * q
            factor, mode, probe, steps, was_synchronized = nonly_split(N)
            assert factor in (p, q)
            exhaustive += 1
            mode_counts[mode] += 1

            if j == i + 1:
                near_neighbor += 1
            if q >= 4 * p:
                unbalanced += 1

            if was_synchronized:
                synchronized += 1
                # Recover the first synchronized dyadic probe and verify its
                # theorem-side certificate q < 2p.
                a = 1 % N
                next_dyadic = 1
                first_sync_s = None
                for s in range(1, p):
                    a = (
                        a
                        * (6 * (2 * s - 1) * (3 * s - 2) * (3 * s - 1) % N)
                        * pow(pow(s, 3, N), -1, N)
                    ) % N
                    if s == next_dyadic:
                        g = gcd(a, N)
                        if g > 1:
                            if g == N:
                                first_sync_s = s
                            break
                        next_dyadic *= 2
                assert first_sync_s is not None
                assert first_sync_s < p < q < 2 * p

                t = isqrt(N) // 3
                assert t + 1 < p
                rt, fd = residue_A(N, t)
                assert fd is None
                gt = gcd(rt, N)
                rt1, fd1 = residue_A(N, t + 1)
                assert fd1 is None
                gt1 = gcd(rt1, N)
                assert (gt == p) or (gt == 1 and gt1 == p)

            if steps * max_steps_over_p_den > max_steps_over_p_num * p:
                max_steps_over_p_num = steps
                max_steps_over_p_den = p

    return {
        "prime_count": len(primes),
        "exhaustive_semiprimes": exhaustive,
        "synchronized_cases": synchronized,
        "near_neighbor_pairs": near_neighbor,
        "unbalanced_q_ge_4p": unbalanced,
        "mode_counts": dict(sorted(mode_counts.items())),
        "max_observed_steps_over_p": f"{max_steps_over_p_num}/{max_steps_over_p_den}",
    }

def main():
    recurrence_checks = check_exact_recurrence()
    fixed = fixed_prefix_no_go()
    nonly = check_nonly_splitter()
    print(
        "PASS",
        f"recurrence_checks={recurrence_checks}",
        f"fixed_prefix_adversarial_semiprimes={fixed['adversarial_semiprimes']}",
        f"alpha_zero_cases={fixed['alpha_zero_cases']}",
        f"prime_power_checks={fixed['prime_power_checks']}",
        f"multifactor_checks={fixed['multifactor_checks']}",
        f"nonly_semiprimes={nonly['exhaustive_semiprimes']}",
        f"nonly_synchronized={nonly['synchronized_cases']}",
        f"nonly_near_neighbor={nonly['near_neighbor_pairs']}",
        f"nonly_unbalanced={nonly['unbalanced_q_ge_4p']}",
        f"modes={nonly['mode_counts']}",
        f"max_steps_over_p={nonly['max_observed_steps_over_p']}",
    )

if __name__ == "__main__":
    main()
