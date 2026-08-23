from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MontgomeryBridge:
    p: int
    t: int
    d: int
    alpha: int
    beta: int
    A_mont: int
    B_mont: int
    kappa: int


def inv_mod(a: int, p: int) -> int:
    a %= p
    if a == 0:
        raise ZeroDivisionError("noninvertible")
    return pow(a, p - 2, p)


def is_square(a: int, p: int) -> bool:
    a %= p
    return a == 0 or pow(a, (p - 1) // 2, p) == 1


def sqrt_bruteforce(a: int, p: int) -> int:
    a %= p
    for r in range(p):
        if r * r % p == a:
            return r
    raise ValueError("not a square")


def hessian_on_curve(x: int, y: int, d: int, p: int) -> bool:
    return (x**3 + y**3 + 1 - 3 * d * x * y) % p == 0


def hessian_affine_points(d: int, p: int) -> list[tuple[int, int]]:
    return [
        (x, y)
        for x in range(p)
        for y in range(p)
        if hessian_on_curve(x, y, d, p)
    ]


def hessian_double_affine(x: int, y: int, d: int, p: int) -> tuple[int, int] | None:
    den = (x**3 - y**3) % p
    if den == 0:
        return None
    z = inv_mod(den, p)
    x2 = y * (1 - x**3) * z % p
    y2 = x * (y**3 - 1) * z % p
    return x2, y2


def s_double(s: int, d: int, p: int) -> int | None:
    den = (2 * s**3 + 3 * d * s**2 - 1) % p
    if den == 0:
        return None
    num = -(s**4 + 4 * s + 3 * d)
    return num * inv_mod(den, p) % p


def hessian_to_weierstrass(x: int, y: int, d: int, p: int) -> tuple[int, int] | None:
    den = (d + x + y) % p
    if den == 0:
        return None
    delta = (d**3 - 1) % p
    q = 12 * delta * inv_mod(den, p) % p
    u = (q - 9 * d * d) % p
    v = 3 * q * (y - x) % p
    return u, v


def weierstrass_coeffs(d: int, p: int) -> tuple[int, int]:
    a = -27 * d * (d**3 + 8)
    b = 54 * (d**6 - 20 * d**3 - 8)
    return a % p, b % p


def weierstrass_on_curve(u: int, v: int, d: int, p: int) -> bool:
    a, b = weierstrass_coeffs(d, p)
    return (v * v - (u**3 + a * u + b)) % p == 0


def montgomery_bridge_from_t(t: int, p: int) -> MontgomeryBridge | None:
    """Construct the Hessian -> Montgomery bridge from a Hessian 2-torsion parameter.

    Requires odd prime p with p != 3.
    d = (2 t^3 + 1)/(3 t^2).
    The short-Weierstrass Montgomery criterion reduces to:
        (t^3 - 1)/t is a nonzero square in F_p.
    """
    t %= p
    if t == 0:
        return None
    d = (2 * t**3 + 1) * inv_mod(3 * t * t, p) % p
    if (d**3 - 1) % p == 0:
        return None

    q = (t**3 - 1) * inv_mod(t, p) % p
    if q == 0 or not is_square(q, p):
        return None
    r = sqrt_bruteforce(q, p)

    delta = (d**3 - 1) % p
    alpha = (12 * delta * inv_mod(d + 2 * t, p) - 9 * d * d) % p
    a, _ = weierstrass_coeffs(d, p)
    beta2 = (3 * alpha * alpha + a) % p

    # Exact simplification:
    # beta^2 = [4(t^3-1)/t^2]^2 * [(t^3-1)/t].
    beta = 4 * (t**3 - 1) * inv_mod(t * t, p) * r % p
    assert beta * beta % p == beta2
    if beta == 0:
        return None

    A_mont = 3 * alpha * inv_mod(beta, p) % p
    B_mont = beta
    # X_M = kappa * (2t-s)/(d+s)
    kappa = 12 * delta * inv_mod(beta * (d + 2 * t), p) % p

    return MontgomeryBridge(
        p=p,
        t=t,
        d=d,
        alpha=alpha,
        beta=beta,
        A_mont=A_mont,
        B_mont=B_mont,
        kappa=kappa,
    )


def weierstrass_to_montgomery(
    u: int, v: int, bridge: MontgomeryBridge
) -> tuple[int, int]:
    p = bridge.p
    X = (u - bridge.alpha) * inv_mod(bridge.beta, p) % p
    Y = v * inv_mod(bridge.beta * bridge.beta, p) % p
    return X, Y


def s_to_montgomery_x(s: int, bridge: MontgomeryBridge) -> int | None:
    p = bridge.p
    den = (bridge.d + s) % p
    if den == 0:
        return None
    return bridge.kappa * (2 * bridge.t - s) * inv_mod(den, p) % p


def montgomery_on_curve(X: int, Y: int, bridge: MontgomeryBridge) -> bool:
    p = bridge.p
    left = bridge.B_mont * Y * Y
    right = X**3 + bridge.A_mont * X**2 + X
    return (left - right) % p == 0


def verify_s_doubling_exhaustive(d: int, p: int) -> tuple[int, int, int]:
    checked = mismatches = singular_both = 0
    for x, y in hessian_affine_points(d, p):
        P2 = hessian_double_affine(x, y, d, p)
        sd = s_double((x + y) % p, d, p)
        if P2 is None or sd is None:
            if P2 is None and sd is None:
                singular_both += 1
            continue
        checked += 1
        if (P2[0] + P2[1]) % p != sd:
            mismatches += 1
    return checked, mismatches, singular_both


def verify_bridge_exhaustive(bridge: MontgomeryBridge) -> tuple[int, int, int]:
    p, d = bridge.p, bridge.d
    checked = mismatches = poles = 0
    for x, y in hessian_affine_points(d, p):
        W = hessian_to_weierstrass(x, y, d, p)
        if W is None:
            poles += 1
            continue
        u, v = W
        if not weierstrass_on_curve(u, v, d, p):
            mismatches += 1
            continue
        X, Y = weierstrass_to_montgomery(u, v, bridge)
        if not montgomery_on_curve(X, Y, bridge):
            mismatches += 1
            continue
        sX = s_to_montgomery_x((x + y) % p, bridge)
        if sX != X:
            mismatches += 1
            continue
        checked += 1
    return checked, mismatches, poles


def count_montgomery_points(bridge: MontgomeryBridge) -> int:
    p = bridge.p
    count = 1
    for X in range(p):
        rhs = (X**3 + bridge.A_mont * X**2 + X) % p
        val = rhs * inv_mod(bridge.B_mont, p) % p
        if val == 0:
            count += 1
        elif is_square(val, p):
            count += 2
    return count


def main() -> None:
    p = 239

    # Earlier non-Montgomery toy Hessian: d=5 has no affine rational 2-torsion.
    roots_d5 = [
        t
        for t in range(1, p)
        if (2 * t**3 - 3 * 5 * t**2 + 1) % p == 0
    ]
    assert roots_d5 == []

    # Convertible example: t=16 gives d=6.
    bridge = montgomery_bridge_from_t(16, p)
    assert bridge is not None
    assert bridge.d == 6
    assert bridge.A_mont == 140
    assert bridge.B_mont in (70, 169)
    assert (bridge.A_mont * bridge.A_mont - 4) % p != 0

    # The Hessian 2-torsion point maps to Montgomery X=0.
    assert hessian_on_curve(16, 16, bridge.d, p)
    assert s_to_montgomery_x(32, bridge) == 0

    # Full finite checks.
    s_checked, s_bad, s_singular = verify_s_doubling_exhaustive(5, p)
    assert s_bad == 0
    bridge_checked, bridge_bad, poles = verify_bridge_exhaustive(bridge)
    assert bridge_bad == 0

    h_count = len(hessian_affine_points(bridge.d, p)) + 1
    m_count = count_montgomery_points(bridge)
    assert h_count == m_count == 264

    print(
        {
            "p": p,
            "d5_2torsion_roots": roots_d5,
            "s_doubling_d5": {
                "checked": s_checked,
                "mismatches": s_bad,
                "singular_both": s_singular,
            },
            "bridge": bridge,
            "bridge_exhaustive": {
                "checked": bridge_checked,
                "mismatches": bridge_bad,
                "poles": poles,
            },
            "group_order_d6": h_count,
        }
    )


if __name__ == "__main__":
    main()
