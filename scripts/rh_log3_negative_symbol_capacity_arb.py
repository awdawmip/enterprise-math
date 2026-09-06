#!/usr/bin/env python3
"""Rigorous negative-symbol outer-measure / phase-space capacity certificate
for the non-pole Riemann-Weil multiplier on H_{log 3}.

The boundary prime power m=9 is absent: log 9=2 log 3 is exactly the support
diameter, so its autocorrelation contribution is zero on H_{log 3}.  The active
prime-power comb is therefore m in {2,3,4,5,7,8}.

On [0,4000] the script classifies dyadic/rational cells by direct Arb evaluation
of the complete scalar symbol.  Cells not resolved by the final 1e-3 mesh are
included in the outer negative set.  For t>=4000 a separate elementary Binet
lower bound proves strict positivity, so no frequency tail is left unchecked.

The output is a rigorous outer bound on |{t in R: symbol(t)<0}| and on the trace
of the corresponding time-frequency concentration operator on [-log3,log3].
It is a capacity certificate, not a positivity/RH certificate.
"""
from collections import deque
from flint import arb, acb, ctx

DEN = 1000                 # final cell width = 1e-3
TMAX_TICKS = 4_000 * DEN
INITIAL_TICKS = 250         # initial width = 0.25
ACTIVE = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2))


def tball(lo, hi):
    return arb(lo + hi) / (2 * DEN) + arb(0, arb(hi - lo) / (2 * DEN))


def symbol_ball(lo, hi):
    t = tball(lo, hi)
    z = acb(arb(1) / 4, t / 2)
    s = z.digamma().real - arb.pi().log()
    for m, p in ACTIVE:
        w = arb(p).log() / arb(m).sqrt()
        s -= 2 * w * (t * arb(m).log()).cos()
    return s


def active_comb_constant():
    A = arb(0)
    for m, p in ACTIVE:
        A += 2 * arb(p).log() / arb(m).sqrt()
    return A


def high_frequency_lower(t):
    """Elementary lower bound for the active non-pole symbol.

    Binet's digamma formula gives, for t>0,
      h_inf(t) >= 1/2 log(1+4t^2)-log(4pi)
                  -2/(1+4t^2)-1/(3t).
    The active prime comb is <= A_L in absolute value.
    The displayed bound is strictly increasing in t.
    """
    t = arb(t)
    return (
        (arb(1) + 4 * t * t).log() / 2
        - (4 * arb.pi()).log()
        - 2 / (arb(1) + 4 * t * t)
        - 1 / (3 * t)
        - active_comb_constant()
    )


def main():
    ctx.prec = 192
    lb4000 = high_frequency_lower(4000)
    print("RH LOG3 NEGATIVE-SYMBOL CAPACITY ARB CERTIFICATE")
    print("active prime powers={2,3,4,5,7,8}; m=9 boundary-null")
    print("A_log3=%s" % active_comb_constant().str(30, radius=False))
    print("high-frequency lower bound at 4000=%s" % lb4000)
    if not (lb4000 > 0):
        raise SystemExit("high-frequency positivity bound failed")

    q = deque()
    for lo in range(0, TMAX_TICKS, INITIAL_TICKS):
        q.append((lo, min(lo + INITIAL_TICKS, TMAX_TICKS)))

    neg_ticks = 0
    amb_ticks = 0
    pos_ticks = 0
    neg_cells = 0
    amb_cells = 0
    evals = 0

    while q:
        lo, hi = q.popleft()
        v = symbol_ball(lo, hi)
        evals += 1
        width = hi - lo
        if v < 0:
            neg_ticks += width
            neg_cells += 1
        elif v > 0:
            pos_ticks += width
        elif width <= 1:
            amb_ticks += width
            amb_cells += 1
        else:
            mid = (lo + hi) // 2
            if mid == lo:
                amb_ticks += width
                amb_cells += 1
            else:
                q.append((lo, mid))
                q.append((mid, hi))

    if neg_ticks + amb_ticks + pos_ticks != TMAX_TICKS:
        raise SystemExit("partition accounting failure")

    half_lower = arb(neg_ticks) / DEN
    half_outer = arb(neg_ticks + amb_ticks) / DEN
    two_sided_lower = 2 * half_lower
    two_sided_outer = 2 * half_outer
    L = arb(3).log()
    capacity_outer = L * two_sided_outer / arb.pi()

    print("evaluations=%d" % evals)
    print("definitely-negative cells=%d" % neg_cells)
    print("ambiguous 1e-3 cells=%d" % amb_cells)
    print("negative half-measure lower=%s" % half_lower)
    print("negative half-measure outer=%s" % half_outer)
    print("negative two-sided measure outer=%s" % two_sided_outer)
    print("phase-space trace capacity outer=%s" % capacity_outer)

    if not (capacity_outer < arb('31.2')):
        raise SystemExit("capacity target <31.2 not certified")

    print("CERTIFIED: the complete negative-symbol set is contained in a set of two-sided measure given by the outer bound above.")
    print("CERTIFIED: its H_log3 time-frequency concentration trace is <31.2.")
    print("BOUNDARY: trace capacity is not a negative-index bound and does not prove full H_log3 positivity or RH.")


if __name__ == "__main__":
    main()
