#!/usr/bin/env python3
"""
Exact falsification for the singleton branch-event transducer.

Portable research checker only. It does not confer Source authority,
mathematical acceptance, CLAIM, OPEN, Result, review, or Working Truth.

For target primes p == 13 or 19 (mod 24), compare the direct signed
singleton threshold displacement

    Delta_p(j) = (2j+1) - beta_p(j)

against the structural classifier:
  * p == 19 (mod 24): Delta = H + v_p(j);
  * p == 13 (mod 24):
      - on the cancellation progression j = s*m, m odd,
        Delta = -c_p;
      - otherwise Delta = H + v_p(j).

Here H marks harmonic endpoints, ord_p(4)=2s in class 13, and
c_p=v_p(1+4^s).
"""

from __future__ import annotations


P_MAX = 5000
J_MAX = 5000


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


def vp_one_plus_four_power(j: int, p: int) -> int:
    """Compute v_p(1+4^j) exactly without constructing 4^j."""
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


def beta_direct(p: int, j: int) -> int:
    epsilon = 1 - endpoint_indicator(p, j)
    eta = vp_one_plus_four_power(j, p) - vp_int(j, p)
    return 2 * j + epsilon + eta


def delta_direct(p: int, j: int) -> int:
    return (2 * j + 1) - beta_direct(p, j)


def class13_parameters(p: int) -> tuple[int, int]:
    order = multiplicative_order_4(p)
    assert order % 2 == 0
    s = order // 2
    c_p = vp_one_plus_four_power(s, p)
    return s, c_p


def delta_predicted(p: int, j: int) -> tuple[int, str]:
    H = endpoint_indicator(p, j)
    d = vp_int(j, p)

    if p % 24 == 19:
        return H + d, "endpoint/denominator"

    assert p % 24 == 13
    s, c_p = class13_parameters(p)
    cancellation = (j % s == 0) and ((j // s) % 2 == 1)
    if cancellation:
        # LTE gives v_p(1+4^j)=c_p+v_p(j), while cancellation
        # and harmonic endpoint states are disjoint.
        return -c_p, "cancellation-delay"
    return H + d, "endpoint/denominator"


def first_visibility_interval(p: int, j: int) -> tuple[int, int, int]:
    """Return (branch_first, generic_first, signed_depth)."""
    delta = delta_direct(p, j)
    generic_first = 2 * j + 2
    branch_first = generic_first - delta
    return branch_first, generic_first, delta


def main() -> None:
    targets = [
        p
        for p in range(3, P_MAX + 1)
        if is_prime(p) and p % 24 in (13, 19)
    ]

    checked = 0
    cancellation_checked = 0
    collision_checked = 0

    for p in targets:
        if p % 24 == 13:
            s, c_p = class13_parameters(p)
            j0 = (p - 1) // 2
            # Exact disjointness of endpoint and cancellation progressions:
            # j0/s is even.
            assert j0 % s == 0
            assert (j0 // s) % 2 == 0
            assert c_p >= 1

        for j in range(1, J_MAX + 1):
            direct = delta_direct(p, j)
            predicted, state = delta_predicted(p, j)
            assert direct == predicted, (p, j, direct, predicted, state)

            branch_first, generic_first, depth = first_visibility_interval(p, j)
            assert generic_first - branch_first == depth

            H = endpoint_indicator(p, j)
            d = vp_int(j, p)
            c = vp_one_plus_four_power(j, p)

            if p % 24 == 19:
                assert c == 0
                assert depth == H + d
            else:
                s, c_p = class13_parameters(p)
                cancellation = (j % s == 0) and ((j // s) % 2 == 1)
                if cancellation:
                    cancellation_checked += 1
                    assert H == 0
                    assert c == c_p + d
                    assert depth == -c_p
                else:
                    assert c == 0
                    assert depth == H + d

            if H and d:
                collision_checked += 1
                assert depth == H + d

            checked += 1

    # Regression witnesses for the three typed mechanisms and their collision.
    expected = {
        (13, 3): -1,    # cancellation delay
        (13, 6): 1,     # first endpoint
        (13, 13): 1,    # first denominator port
        (13, 39): -1,   # cancellation + p denominator: denominator neutralized
        (19, 9): 1,     # first endpoint
        (19, 19): 1,    # first denominator port
        (19, 171): 2,   # endpoint + denominator collision
        (1093, 91): -2, # Wieferich-height cancellation delay
    }
    for (p, j), want in expected.items():
        assert delta_direct(p, j) == want, (p, j, delta_direct(p, j), want)

    print("status=PASS")
    print(f"target_primes={len(targets)}")
    print(f"singleton_ports_checked={checked}")
    print(f"cancellation_ports_checked={cancellation_checked}")
    print(f"endpoint_denominator_collisions_checked={collision_checked}")
    print("witnesses=" + ",".join(f"{p}:{j}:{d}" for (p, j), d in expected.items()))


if __name__ == "__main__":
    main()
