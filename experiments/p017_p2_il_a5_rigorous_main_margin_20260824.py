"""Certified rational-log lower bound for the P017 / IL a=5 main margin.

No floating point is used for the sign certificate.  For rational q>0,
log(q) is enclosed using

    log q = 2 sum_{n>=0} u^(2n+1)/(2n+1),  u=(q-1)/(q+1),

with a positive geometric tail bound (and log q = -log(1/q) for q<1).

This certifies only the algebraic/main-integral lower-bound expression derived
in `docs/P017_P2_IL_A5_RIGOROUS_MAIN_MARGIN_20260824.md`; it does not replace
the analytic Iwaniec-Laborde remainder lemmas or make their threshold explicit.
"""

from fractions import Fraction as Q

Interval = tuple[Q, Q]


def add(x: Interval, y: Interval) -> Interval:
    return x[0] + y[0], x[1] + y[1]


def scale(c: Q, x: Interval) -> Interval:
    if c >= 0:
        return c * x[0], c * x[1]
    return c * x[1], c * x[0]


def linear(terms: list[tuple[Q, Interval]]) -> Interval:
    out: Interval = (Q(0), Q(0))
    for c, x in terms:
        out = add(out, scale(c, x))
    return out


def log_interval(q: Q, terms: int = 30) -> Interval:
    if q <= 0:
        raise ValueError("log argument must be positive")
    if q == 1:
        return Q(0), Q(0)
    if q < 1:
        lo, hi = log_interval(1 / q, terms)
        return -hi, -lo

    u = (q - 1) / (q + 1)
    u2 = u * u
    power = u
    partial = Q(0)
    for n in range(terms):
        partial += power / (2 * n + 1)
        power *= u2
    lo = 2 * partial
    # `power` is u^(2*terms+1), the first omitted power.
    remainder = 2 * power / ((2 * terms + 1) * (1 - u2))
    return lo, lo + remainder


def main() -> None:
    ln2 = log_interval(Q(2))
    ln3 = log_interval(Q(3))
    ln5 = log_interval(Q(5))

    j1 = linear([
        (Q(-1, 15), ln2),
        (Q(2, 5), ln3),
    ])

    j3 = linear([
        (Q(4, 15), (Q(1), Q(1))),
        (Q(92, 15), ln2),
        (Q(-8, 3), ln5),
    ])

    j4 = linear([
        (Q(13, 15), log_interval(Q(49, 36))),
        (Q(2, 15), log_interval(Q(11, 24))),
    ])

    # Eight-bin left Riemann upper sum U2 for the decreasing kernel g(s).
    u2: Interval = (Q(0), Q(0))
    for i in range(8):
        u2 = add(
            u2,
            scale(Q(1, 8 + i), log_interval(Q(24 - i, 8 + i))),
        )

    # f(5) >= C log(4)/5 makes the positive normalized term 28 log(2)/15.
    positive = scale(Q(28, 15), ln2)

    L = linear([
        (Q(1), positive),
        (Q(-4, 3), j1),
        (Q(-2, 3), u2),
        (Q(-1), j3),
        (Q(-1), j4),
    ])

    r2 = Q(12, 47) ** 2
    net = linear([
        (Q(2), L),
        (Q(-1), (r2, r2)),
    ])

    assert net[0] > Q(5896564935, 10**11)  # 0.05896564935
    assert net[0] > 0

    print("Certified positive main margin passed")
    print("lower =", float(net[0]))
    print("upper =", float(net[1]))
    print("exact lower numerator digits =", len(str(net[0].numerator)))
    print("exact lower denominator digits =", len(str(net[0].denominator)))


if __name__ == "__main__":
    main()
