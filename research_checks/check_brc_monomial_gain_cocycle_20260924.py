#!/usr/bin/env python3
"""
Exact falsification for the monomial branch-gain cocycle.

Portable research checker only. It does not confer Source authority,
mathematical acceptance, CLAIM, OPEN, Result, review, or Working Truth.

For any exponent vector m,

    Gamma_p(m) := W_infty(m) - W_p(m)
                = sum_j m_j Delta_p(j) + sum_j v_p(m_j!)

and, after expanding Delta,

    Gamma = endpoint_credit + denominator_credit
            - cancellation_debit + factorial_credit.

The checker verifies the identity and the two structural consequences:
  * class 19 mod 24: Gamma >= 0 for every tested monomial;
  * class 13 mod 24: a nonzero monomial supported only on cancellation
    ports has Gamma < 0.
"""

from __future__ import annotations

import random


P_MAX = 500
J_MAX = 80
RANDOM_VECTORS_PER_PRIME = 2000
PURE_CANCEL_VECTORS_PER_CLASS13_PRIME = 500
SEED = 20260924


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def vp_int(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("vp_int(0,p) is not used here")
    n = abs(n)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def vp_factorial(n: int, p: int) -> int:
    e = 0
    q = p
    while q <= n:
        e += n // q
        q *= p
    return e


def vp_one_plus_four_power(j: int, p: int) -> int:
    e = 0
    modulus = p
    while (pow(4, j, modulus) + 1) % modulus == 0:
        e += 1
        modulus *= p
        if e > 12:
            raise RuntimeError("unexpectedly high valuation")
    return e


def multiplicative_order_4(p: int) -> int:
    x = 1
    for k in range(1, p):
        x = (4 * x) % p
        if x == 1:
            return k
    raise RuntimeError("order not found")


def endpoint_indicator(p: int, j: int) -> int:
    return int((2 * j) % (p - 1) == 0)


def beta(p: int, j: int) -> int:
    epsilon = 1 - endpoint_indicator(p, j)
    eta = vp_one_plus_four_power(j, p) - vp_int(j, p)
    return 2 * j + epsilon + eta


def w_generic(m: dict[int, int]) -> int:
    return sum(a * (2 * j + 1) for j, a in m.items())


def w_branch(p: int, m: dict[int, int]) -> int:
    return sum(
        a * beta(p, j) - vp_factorial(a, p)
        for j, a in m.items()
    )


def gamma_direct(p: int, m: dict[int, int]) -> int:
    return w_generic(m) - w_branch(p, m)


def gamma_typed(p: int, m: dict[int, int]) -> tuple[int, tuple[int, int, int, int]]:
    endpoint_credit = sum(
        a * endpoint_indicator(p, j)
        for j, a in m.items()
    )
    denominator_credit = sum(
        a * vp_int(j, p)
        for j, a in m.items()
    )
    cancellation_debit = sum(
        a * vp_one_plus_four_power(j, p)
        for j, a in m.items()
    )
    factorial_credit = sum(
        vp_factorial(a, p)
        for a in m.values()
    )
    total = (
        endpoint_credit
        + denominator_credit
        - cancellation_debit
        + factorial_credit
    )
    return total, (
        endpoint_credit,
        denominator_credit,
        cancellation_debit,
        factorial_credit,
    )


def class13_parameters(p: int) -> tuple[int, int]:
    order = multiplicative_order_4(p)
    assert order % 2 == 0
    s = order // 2
    kappa = vp_one_plus_four_power(s, p)
    return s, kappa


def cancellation_port_class13(p: int, j: int) -> bool:
    s, _ = class13_parameters(p)
    return (j % s == 0) and ((j // s) % 2 == 1)


def main() -> None:
    rng = random.Random(SEED)
    targets = [
        p
        for p in range(13, P_MAX + 1)
        if is_prime(p) and p % 24 in (13, 19)
    ]

    mixed_checked = 0
    pure_cancel_checked = 0

    for p in targets:
        for _ in range(RANDOM_VECTORS_PER_PRIME):
            support_size = rng.randint(1, 5)
            js = rng.sample(range(1, J_MAX + 1), support_size)
            m = {j: rng.randint(1, 2 * p) for j in js}

            direct = gamma_direct(p, m)
            typed, parts = gamma_typed(p, m)
            assert direct == typed, (p, m, direct, typed, parts)

            # Visibility threshold identity.
            generic_first = w_generic(m) + 1
            branch_first = w_branch(p, m) + 1
            assert generic_first - branch_first == direct

            if p % 24 == 19:
                # No cancellation ports in this congruence class.
                assert parts[2] == 0
                assert direct >= 0, (p, m, direct, parts)

            mixed_checked += 1

        if p % 24 == 13:
            s, kappa = class13_parameters(p)
            ports = [
                j
                for j in range(1, 4 * J_MAX + 1)
                if cancellation_port_class13(p, j)
            ]
            assert ports
            for _ in range(PURE_CANCEL_VECTORS_PER_CLASS13_PRIME):
                size = min(len(ports), rng.randint(1, 4))
                js = rng.sample(ports, size)
                m = {j: rng.randint(1, 3 * p) for j in js}

                direct = gamma_direct(p, m)
                total_mult = sum(m.values())
                factorial_credit = sum(vp_factorial(a, p) for a in m.values())

                # On cancellation ports Delta=-kappa exactly, so
                # Gamma=-kappa*M + factorial_credit.
                predicted = -kappa * total_mult + factorial_credit
                assert direct == predicted, (p, m, direct, predicted)
                assert factorial_credit < total_mult
                assert direct < 0, (p, m, direct, kappa)

                pure_cancel_checked += 1

    # Exact mechanism witnesses.
    witnesses = [
        (13, {3: 1}),          # pure cancellation: negative
        (13, {6: 1}),          # endpoint: positive
        (13, {3: 13}),         # factorial cannot defeat cancellation
        (13, {6: 1, 3: 1}),   # one endpoint credit balances one cancellation debit
        (19, {9: 1}),          # endpoint positive
        (19, {19: 1}),         # denominator positive
        (19, {171: 1}),        # endpoint+denominator depth 2
        (19, {1: 19}),         # pure factorial credit
    ]

    witness_out = []
    for p, m in witnesses:
        direct = gamma_direct(p, m)
        typed, parts = gamma_typed(p, m)
        assert direct == typed
        witness_out.append((p, m, direct, parts))

    print("status=PASS")
    print(f"target_primes={len(targets)}")
    print(f"mixed_monomials_checked={mixed_checked}")
    print(f"pure_cancellation_monomials_checked={pure_cancel_checked}")
    for item in witness_out:
        print("witness=", item)


if __name__ == "__main__":
    main()
