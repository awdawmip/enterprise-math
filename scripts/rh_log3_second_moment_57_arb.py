#!/usr/bin/env python3
"""Rigorous second-moment negative-index certificate for the full H_log3 Weil form.

Target:
    n_-(Q_full on H_log3) <= 57.

Let a(t) be the exact active non-pole scalar multiplier, with boundary-null
m=9 removed, and fix mu=2.08. Put b=(mu-a)_+ and

    W = P_L F^{-1} b F P_L,   L=log 3.

Then Q_nonpole >= mu I-W, hence

    n_-(Q_nonpole) <= #{lambda_j(W)>mu} <= Tr(W^2)/mu^2.

We rigorously majorize b by g=H+e*1_C. H is the nonnegative piecewise-linear
interpolant of upward-quantized node values b(nh), h=1/50. The interpolation
error e=0.0024 is checked directly against the certified global curvature
bound M2 through e > M2*h^2/8. C is the union of cells not certified to stay
below the threshold.

Since W_b <= W_g and positive compact eigenvalues are monotone,
Tr(W_b^2)<=Tr(W_g^2). With W_g=W_H+e K_C and 0<=K_C<=I,

    Tr(W_g^2) <= Tr(W_H^2) + 2e Tr(W_H) + e^2 Tr(K_C).

The B-spline Fourier factor has modulus <=1, so Tr(W_H^2) is bounded by a
uniform-grid Toeplitz quadratic form. Node values are rounded upward to
multiples of 1e-5 and converted to integers. A single exact FLINT modular
polynomial product yields every autocorrelation coefficient. Cauchy gives
C_k<=C_0; after verifying C_0<2^61-1, the modular coefficients are the exact
integer autocorrelations.

The first 100000 lags (distance <2000) use exact Arb sinc weights. All farther
lags use sin^2<=1 and the 1/v^2 envelope. Frequencies beyond 30000 are absent:
an independent Binet lower bound proves a(t)>mu+e there.

If the final Arb upper bound is <57*mu^2, then n_-(Q_nonpole)<=56. The exact
pole operator has one negative channel, hence n_-(Q_full)<=57.

Boundary: finite Morse-index upper bound only; not positivity and not RH.
"""
import gc

from flint import arb, acb, nmod_poly, ctx

H_DEN = 50
TMAX = 30000
N = TMAX * H_DEN
SCALE = 100000
MU_TEXT = "2.08"
E_NUM = 3
E_DEN = 1250
K_NEAR = 100000
MOD = 2305843009213693951
ACTIVE = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2))


def active_data():
    out = []
    for m, p in ACTIVE:
        lm = arb(m).log()
        w = arb(p).log() / arb(m).sqrt()
        out.append((lm, w))
    return out


def symbol_point(i, data):
    t = arb(i) / H_DEN
    z = acb(arb(1) / 4, t / 2)
    s = z.digamma().real - arb.pi().log()
    for lm, w in data:
        s -= 2 * w * (t * lm).cos()
    return s


def active_comb_constant(data):
    return sum((2 * w for _, w in data), arb(0))


def high_frequency_lower(t, data):
    t = arb(t)
    return (
        (arb(1) + 4 * t * t).log() / 2
        - (4 * arb.pi()).log()
        - 2 / (arb(1) + 4 * t * t)
        - 1 / (3 * t)
        - active_comb_constant(data)
    )


def curvature_bound(data):
    prime = sum((2 * w * lm * lm for lm, w in data), arb(0))
    arch = arb(3).zeta(arb(1) / 4) / 2
    return prime + arch


def main():
    ctx.prec = 192
    mu = arb(MU_TEXT)
    h = arb(1) / H_DEN
    e = arb(E_NUM) / E_DEN
    data = active_data()

    print("RH LOG3 SECOND-MOMENT ARB CERTIFICATE")
    print("mu=%s h=1/%d scale=%d TMAX=%d" % (MU_TEXT, H_DEN, SCALE, TMAX))
    print("active prime powers={2,3,4,5,7,8}; m=9 boundary-null")

    m2 = curvature_bound(data)
    needed_e = m2 * h * h / 8
    print("global |a''| bound=%s" % m2)
    print("required interpolation error=%s; declared e=%s" % (needed_e, e))
    if not (m2 < arb(48)):
        raise SystemExit("curvature bound <48 failed")
    if not (e > needed_e):
        raise SystemExit("declared interpolation error is too small")

    tail_lb = high_frequency_lower(TMAX, data)
    print("Binet lower a(30000)>=%s" % tail_lb)
    if not (tail_lb > mu + e):
        raise SystemExit("frequency support closure a>mu+e failed")

    qpos = [0] * (N + 1)
    candidate_half = 0
    prev_f_up = None

    print("sampling %d positive-half Arb nodes ..." % (N + 1), flush=True)
    for i in range(N + 1):
        a = symbol_point(i, data)
        f_up = (mu - a).upper()
        q = int((f_up * SCALE).ceil()) if f_up > 0 else 0
        qpos[i] = q

        if prev_f_up is not None and max(prev_f_up, f_up) + e > 0:
            candidate_half += 1
        prev_f_up = f_up

        if i and i % 100000 == 0:
            print("  sampled %d/%d" % (i, N), flush=True)

    if qpos[-1] != 0:
        raise SystemExit("last quantized node is nonzero despite tail closure")

    qfull = qpos[:0:-1] + qpos
    M = len(qfull)
    if M != 2 * N + 1:
        raise SystemExit("full sequence length mismatch")

    sumq = qpos[0] + 2 * sum(qpos[1:])
    c0_exact = qpos[0] * qpos[0] + 2 * sum(q * q for q in qpos[1:])
    print("quantized nonzero nodes=%d" % sum(1 for q in qfull if q))
    print("candidate half-cells=%d" % candidate_half)
    print("C0 exact=%d; modulus=%d" % (c0_exact, MOD))
    if not (c0_exact < MOD):
        raise SystemExit("single-modulus exact-autocorrelation condition failed")

    print("building exact nmod autocorrelation polynomial, length=%d ..." % M, flush=True)
    P = nmod_poly(qfull, MOD)
    del qfull
    gc.collect()
    R = P * P.reverse()
    del P
    gc.collect()
    center = M - 1

    if int(R[center]) != c0_exact:
        raise SystemExit("autocorrelation center mismatch")

    L = arb(3).log()
    pi = arb.pi()
    scale2 = arb(SCALE) * SCALE

    near = arb(c0_exact) * (2 * L) ** 2
    print("accumulating %d exact Arb lag weights ..." % (K_NEAR - 1), flush=True)
    for k in range(1, K_NEAR):
        ck = int(R[center + k])
        v = arb(k) / H_DEN
        kval = (2 * (L * v).sin() / v) ** 2
        near += 2 * arb(ck) * kval
        if k % 10000 == 0:
            print("  lag %d/%d" % (k, K_NEAR - 1), flush=True)

    R0 = arb(K_NEAR) / H_DEN
    far = 4 * arb(sumq) * arb(sumq) / (R0 * R0)

    hh_upper = h * h / (4 * pi * pi * scale2) * (near + far)
    integral_H_upper = h * arb(sumq) / SCALE
    trace_H_upper = L / pi * integral_H_upper
    measure_C = 2 * h * candidate_half
    trace_C = L / pi * measure_C

    moment_upper = hh_upper + 2 * e * trace_H_upper + e * e * trace_C
    target = arb(57) * mu * mu

    print("HH upper=%s" % hh_upper)
    print("Tr H upper=%s" % trace_H_upper)
    print("Tr K_C=%s" % trace_C)
    print("Tr W_g^2 upper=%s" % moment_upper)
    print("57*mu^2=%s" % target)
    print("margin=%s" % (target - moment_upper))

    if not (moment_upper < target):
        raise SystemExit("second-moment target <57*mu^2 not certified")

    print("CERTIFIED: Tr(W_mu^2)/mu^2 <57 on the full H_log3 window.")
    print("THEOREM: n_-(Q_nonpole)<=56.")
    print("POLE: the exact pole operator has one negative channel.")
    print("RESULT: n_-(Q_full on H_log3)<=57.")
    print("BOUNDARY: finite Morse-index upper bound only; not positivity and not RH.")


if __name__ == "__main__":
    main()
