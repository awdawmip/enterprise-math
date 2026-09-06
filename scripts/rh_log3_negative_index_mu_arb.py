#!/usr/bin/env python3
"""Rigorous constant-floor negative-index certificate for the Riemann-Weil
form on H_{log 3}.

Let a(t) be the exact active non-pole scalar multiplier

  Re psi(1/4+i t/2)-log pi
  -2 sum_{m in {2,3,4,5,7,8}} Lambda(m)/sqrt(m) cos(t log m).

For mu=1 define b(t)=(1-a(t))_+ and
  W=P_L F^{-1} b F P_L, L=log 3.
Then Q_nonpole >= I-W, so
  n_-(Q_nonpole) <= #{lambda_j(W)>1} < Tr(W).
The trace is
  Tr(W)=log(3)/pi * integral_R b(t) dt.

This script rigorously upper-encloses that integral with Arb.  On [0,10000]
all cells that are not certified to satisfy a>1 are recursively refined to
width 2e-4; the final-cell Arb lower bound for a gives a rigorous upper
rectangle for (1-a)_+.  For t>=10000 an independent Binet lower bound proves
a(t)>1, so the frequency tail contributes exactly zero.

If Tr(W)<80 then n_-(Q_nonpole)<=79.  The pole operator is
  |u><v|+|v><u| = 1/2 |u+v><u+v| - 1/2 |u-v><u-v|,
with u=e^{x/2}, v=e^{-x/2}; hence it has exactly one negative channel on
H_{log3}.  Subadditivity of negative inertia then gives n_-(Q_full)<=80.

Boundary: this is a finite negative-index upper bound, not positivity and not
an RH proof.
"""
from collections import deque

from flint import arb, acb, ctx

DEN = 5000                    # final width = 2e-4
TMAX = 10000
TMAX_TICKS = TMAX * DEN
INITIAL_TICKS = 1250          # initial width = 0.25
MU = arb(1)
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
    return sum((2 * arb(p).log() / arb(m).sqrt() for m, p in ACTIVE), arb(0))


def high_frequency_lower(t):
    """Elementary lower bound for the active non-pole symbol.

    For t>0, a Binet bound gives
      h_inf(t) >= 1/2 log(1+4t^2)-log(4pi)
                  -2/(1+4t^2)-1/(3t).
    Subtracting the absolute active prime-comb constant gives a lower bound for
    a(t).  The displayed lower bound is strictly increasing in t.
    """
    t = arb(t)
    return (
        (arb(1) + 4 * t * t).log() / 2
        - (4 * arb.pi()).log()
        - 2 / (arb(1) + 4 * t * t)
        - 1 / (3 * t)
        - active_comb_constant()
    )


def positive_part_upper(ball):
    """Rigorous upper endpoint of max(ball,0), returned as an Arb enclosure."""
    if ball < 0:
        return arb(0)
    return ball.mid() + ball.rad()


def main():
    ctx.prec = 192
    tail_lb = high_frequency_lower(TMAX)
    print("RH LOG3 CONSTANT-FLOOR NEGATIVE-INDEX ARB CERTIFICATE")
    print("mu=1 active prime powers={2,3,4,5,7,8}; m=9 boundary-null")
    print("final unresolved/contributing-cell width=2e-4")
    print("A_log3=%s" % active_comb_constant().str(30, radius=False))
    print("high-frequency lower bound at 10000=%s" % tail_lb)
    if not (tail_lb > MU):
        raise SystemExit("high-frequency a(t)>1 bound failed")

    q = deque()
    for lo in range(0, TMAX_TICKS, INITIAL_TICKS):
        q.append((lo, min(lo + INITIAL_TICKS, TMAX_TICKS)))

    half_integral_upper = arb(0)
    evals = 0
    zero_cells = 0
    contributing_cells = 0

    while q:
        lo, hi = q.popleft()
        v = symbol_ball(lo, hi)
        evals += 1
        width = hi - lo

        # If the whole cell has a(t)>1 then b=(1-a)_+ vanishes there.
        if v > MU:
            zero_cells += 1
            continue

        if width <= 1:
            deficit = MU - v
            height_upper = positive_part_upper(deficit)
            if height_upper > 0:
                half_integral_upper += arb(width) / DEN * height_upper
                contributing_cells += 1
            continue

        mid = (lo + hi) // 2
        if mid == lo:
            deficit = MU - v
            height_upper = positive_part_upper(deficit)
            half_integral_upper += arb(width) / DEN * height_upper
            contributing_cells += 1
        else:
            q.append((lo, mid))
            q.append((mid, hi))

    trace_upper = 2 * arb(3).log() / arb.pi() * half_integral_upper

    print("evaluations=%d" % evals)
    print("certified-zero cells=%d" % zero_cells)
    print("final contributing cells=%d" % contributing_cells)
    print("half integral upper=%s" % half_integral_upper)
    print("Tr W upper=%s" % trace_upper)

    if not (trace_upper < arb(80)):
        raise SystemExit("target Tr(W)<80 not certified")

    print("CERTIFIED: Tr(W)<80 for W=P_L F^-1(1-a)_+ F P_L.")
    print("THEOREM: n_-(Q_nonpole)<=79 by Q_nonpole>=I-W and the trace eigenvalue count.")
    print("POLE: |u><v|+|v><u| has exactly one negative channel.")
    print("RESULT: n_-(Q_full on H_log3)<=80.")
    print("BOUNDARY: finite negative-index upper bound only; not full positivity and not RH.")


if __name__ == "__main__":
    main()
