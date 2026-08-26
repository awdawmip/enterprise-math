#!/usr/bin/env python3
"""Exact rational certificate for the P017 sharp-odd W2 trivial collapse.

The source a6 root-edge weight on the W2 band vanishes linearly at
w=D^(c/a)=X^(1/2).  For a sharp interval of even integer length L<=Y=X^theta,
we use only S(A_p,z)<=L/p+1, enlarge the prime sum to all integers, and certify
W2/L < 1.7e-6 at the conservative Tier-A scale X0=K0^2.

No two-dimensional Selberg estimate or Fourier smoothing is used here.
"""

from fractions import Fraction as Q

K0 = 116_009_280_740_973_308
X0 = K0 * K0

def atanh_log_bounds(x: Q, terms: int) -> tuple[Q, Q]:
    z = (x - 1) / (x + 1)
    partial = sum(
        2 * z ** (2*j + 1) / Q(2*j + 1) for j in range(terms)
    )
    n = terms - 1
    tail = 2 * abs(z) ** (2*n + 3) / (
        Q(2*n + 3) * (1 - z*z)
    )
    return partial, partial + tail


def main() -> None:
    theta = Q(4999, 10000)
    a = Q(6)
    b = Q(22, 5)
    c = Q(27, 5)
    d = Q(5, 9)
    C = 2*c - b - 1
    assert C == c == Q(27, 5)
    assert d*c/a == Q(1, 2)
    assert Q(1, 2) - theta == Q(1, 10000)

    # Elementary rational bounds 2.3 < log 10 < 2.303.
    lo10, hi10 = atanh_log_bounds(Q(10), 11)
    assert lo10 > Q(23, 10)
    assert hi10 < Q(2303, 1000)

    assert 10**34 < X0 < 10**35

    # delta=log(w/Y)=(1/10000)log X0.
    delta_upper = Q(35) * Q(2303, 1000) / 10000
    assert delta_upper == Q(16121, 2_000_000)  # 0.0080605
    assert delta_upper < Q(81, 10000)

    # log X0 > 34 log 10 > 34*2.3, and
    # a/(C log D) = 2/log X exactly for a=6,C=27/5,d=5/9.
    prefactor_upper = Q(2) / (Q(34) * Q(23, 10))
    assert prefactor_upper == Q(10, 391)

    # Y=X^theta >10^16.  If L is the largest even integer <=Y, then
    # L>Y-2 and Y/L<1.000001.  We need only this coarse finite fact.
    assert Q(34) * theta > 16
    y_lower = 10**16
    assert Q(y_lower, y_lower - 2) < Q(1_000_001, 1_000_000)

    # Monotone sum bounds:
    # sum log(w/n)/n <= delta/Y + delta^2/2;
    # sum log(w/n) <= delta + Y(e^delta-1-delta),
    # and e^delta-1-delta <= delta^2/[2(1-delta)].
    B = (
        delta_upper**2 / 2
        + delta_upper / y_lower
        + delta_upper / (y_lower - 2)
        + Q(1_000_001, 1_000_000)
          * delta_upper**2 / (2*(1-delta_upper))
    )
    ratio_upper = prefactor_upper * B
    assert ratio_upper < Q(17, 10_000_000)

    # Compare with the source-decimal a6 main reserve on the final count scale.
    # main > (20/9)*(287/2500)*Y/log D = (574/2250)*Y/log D.
    # We do not need a tight finite lower bound here; merely certify the W2
    # trivial bound is orders of magnitude smaller than 0.005*Y.
    assert ratio_upper < Q(1, 500_000)  # 2e-6
    assert Q(1, 500_000) < Q(1, 200)   # 0.005

    print("P017 sharp-odd W2 trivial-collapse certificate: PASS")
    print("delta <", delta_upper, "~=", float(delta_upper))
    print("2/log(X0) <", prefactor_upper, "~=", float(prefactor_upper))
    print("W2/L <", ratio_upper, "~=", float(ratio_upper))
    print("certified clean bound: W2/L < 17/10^7")


if __name__ == "__main__":
    main()
