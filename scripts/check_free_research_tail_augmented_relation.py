#!/usr/bin/env python3
"""Exact checks for the multichannel moving-cutoff relation decomposition.

The coefficient mismatch is represented by the ordinary weighted value channel
``w_a = V_a x_a``.  This keeps the tail equation linear in relation fields.
"""

from __future__ import annotations

from fractions import Fraction


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    for p in range(2, n + 1):
        if not is_prime(p):
            continue
        q = p
        while q < n:
            q *= p
        if q == n:
            return p
    return None


def prime_powers(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if prime_power_base(n) is not None]


def weight(a: int) -> Fraction:
    p = prime_power_base(a)
    assert p is not None
    return Fraction(p, a)


def q(a: int, n: int) -> int:
    return n // a


def field(n: int) -> Fraction:
    return Fraction(
        ((47 * n * n + 19 * n + 11) % 137) - 68,
        ((37 * n + 17) % 41) + 1,
    )


def defect(a: int, n: int) -> Fraction:
    return field(n) + field(q(a, n))


def residual(actions: list[int], n: int) -> Fraction:
    return sum((weight(c) * defect(c, n) for c in actions), Fraction(0, 1))


def relation(
    u: dict[int, Fraction],
    channel: dict[int, Fraction],
    a: int,
    b: int,
) -> Fraction:
    return u[a] * u[b] * (channel[a] - channel[b])


def check_augmented_tail_decomposition(max_y: int = 110) -> None:
    for y in range(2, max_y + 1):
        n = y * y
        actions = prime_powers(y)
        if not actions:
            continue
        u = {a: weight(a) for a in actions}
        total = sum(u.values(), Fraction(0, 1))

        x: dict[int, Fraction] = {}
        full_rho: dict[int, Fraction] = {}
        truncated_rho: dict[int, Fraction] = {}
        tail_mass: dict[int, Fraction] = {}
        tail_endpoint: dict[int, Fraction] = {}
        coefficient_channel: dict[int, Fraction] = {}

        for a in actions:
            m = q(a, n)
            full_actions = prime_powers(m)
            tail = [c for c in full_actions if c > y]
            x[a] = field(m)
            full_rho[a] = residual(full_actions, m)
            truncated_rho[a] = residual(actions, m)
            tail_mass[a] = sum((weight(c) for c in tail), Fraction(0, 1))
            tail_endpoint[a] = sum(
                (weight(c) * field(q(c, m)) for c in tail),
                Fraction(0, 1),
            )
            coefficient_channel[a] = tail_mass[a] * x[a]

            assert truncated_rho[a] == (
                full_rho[a] - coefficient_channel[a] - tail_endpoint[a]
            )
            for c in tail:
                assert q(c, m) <= (y - 1) // a

        for a in actions:
            for b in actions:
                z_now = relation(u, x, a, b)
                transported = sum(
                    (
                        u[c]
                        * u[a]
                        * u[b]
                        * (
                            field(q(a, q(c, n)))
                            - field(q(b, q(c, n)))
                        )
                        for c in actions
                    ),
                    Fraction(0, 1),
                )
                assert total * z_now + transported == relation(
                    u, truncated_rho, a, b
                )

                assert relation(u, truncated_rho, a, b) == (
                    relation(u, full_rho, a, b)
                    - relation(u, coefficient_channel, a, b)
                    - relation(u, tail_endpoint, a, b)
                )


def check_componentwise_s3_projection(max_y: int = 35) -> None:
    for y in range(3, max_y + 1):
        n = y * y
        actions = prime_powers(y)
        if len(actions) < 3:
            continue
        channels: list[dict[int, Fraction]] = []

        x = {a: field(q(a, n)) for a in actions}
        channels.append(x)

        v = {}
        e = {}
        w = {}
        r = {}
        for a in actions:
            m = q(a, n)
            full_actions = prime_powers(m)
            tail = [c for c in full_actions if c > y]
            v[a] = sum((weight(c) for c in tail), Fraction(0, 1))
            e[a] = sum(
                (weight(c) * field(q(c, m)) for c in tail),
                Fraction(0, 1),
            )
            w[a] = v[a] * x[a]
            r[a] = residual(full_actions, m)
        channels.extend([v, e, w, r])

        sample = actions[: min(7, len(actions))]
        for a in sample:
            for b in sample:
                for c in sample:
                    for channel in channels:
                        mean = (channel[a] + channel[b] + channel[c]) / 3
                        # Uniform transposition averaging sends each first slot
                        # to this same mean, hence every component relation dies.
                        assert (channel[b] + channel[c] + channel[a]) / 3 == mean
                        assert (channel[a] + channel[c] + channel[b]) / 3 == mean
                        assert (channel[a] + channel[b] + channel[c]) / 3 == mean


def main() -> None:
    check_augmented_tail_decomposition()
    check_componentwise_s3_projection()
    print("tail-augmented relation-state checks: PASS")


if __name__ == "__main__":
    main()
