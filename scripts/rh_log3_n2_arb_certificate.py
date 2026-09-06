#!/usr/bin/env python3
"""Rigorous Arb certificate for the first 8-dimensional branch-sine subspace
of the Riemann-Weil form on H_{log 3}.

Basis: four labelled intervals
  S-=[-log3,-log2], O-=[-log2,0], O+=[0,log2], S+=[log2,log3],
with the first two Dirichlet sine modes on each interval.

Archimedean form:
  h_inf(t)=h0+sum_{n>=0} J_{2n+1/2},
where
  J_c = integral_0^infinity exp(-c r)
        (2I - R(r)-R(r)^T) dr >= 0.
The one-sided Laplace overlap is evaluated in elementary closed form; there is
no numerical quadrature and no frequency cutoff.

The script Arb-certifies positive definiteness of
  h0 I + sum_{n=0}^{K-1} J_{2n+1/2} + prime + pole.
Since every omitted J_c is positive semidefinite, a positive interval LDL^T
certificate for this lower matrix proves positive definiteness of the complete
Weil Gram matrix on this declared finite subspace.

All support-order decisions for prime translations are exact rational
comparisons in multiplicative coordinates; no floating-point control flow is
used in the certificate.

Boundary: finite-subspace certificate only.  This does NOT prove positivity on
all of H_{log 3} and is NOT an RH proof.

Requires python-flint >= 0.9.0.
"""
import argparse
from fractions import Fraction
import sys

from flint import arb, ctx

ORDER = {"S-": 0, "O-": 1, "O+": 2, "S+": 3}
PRIME_POWERS = {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2, 9: 3}


def make_basis():
    L2 = arb(2).log()
    L3 = arb(3).log()
    # aq,bq are the exact multiplicative endpoints: a=log(aq), b=log(bq).
    intervals = [
        (-L3, -L2, "S-", Fraction(1, 3), Fraction(1, 2)),
        (-L2, arb(0), "O-", Fraction(1, 2), Fraction(1, 1)),
        (arb(0), L2, "O+", Fraction(1, 1), Fraction(2, 1)),
        (L2, L3, "S+", Fraction(2, 1), Fraction(3, 1)),
    ]
    out = []
    for a, b, label, aq, bq in intervals:
        ell = b - a
        for k in (1, 2):
            out.append(
                dict(
                    a=a,
                    b=b,
                    aq=aq,
                    bq=bq,
                    ell=ell,
                    label=label,
                    k=k,
                    A=arb.pi() * k / ell,
                    norm=(arb(2) / ell).sqrt(),
                )
            )
    return out


def exp_moment(b, c):
    """Integral phi_b(x) exp(c x) dx over the support interval."""
    A, ell, a, norm, k = b["A"], b["ell"], b["a"], b["norm"], b["k"]
    sign = -1 if k % 2 else 1
    return norm * (c * a).exp() * A * (1 - sign * (c * ell).exp()) / (c * c + A * A)


def same_interval_laplace(bi, bj, c):
    """L_c(i,j) on one common support interval, in exact closed form."""
    ell = bi["ell"]
    A, B = bi["A"], bj["A"]
    ni, nj = bi["norm"], bj["norm"]
    k, l = bi["k"], bj["k"]

    Iss = ell / 2 if k == l else arb(0)
    if k == l:
        Isc = arb(0)
    else:
        # Exact parity form of integral sin(k*pi*u/ell) cos(l*pi*u/ell) du.
        s1 = 1 - ((-1) ** (k + l))
        s2 = 1 - ((-1) ** (k - l))
        Isc = (arb(s1) / (A + B) + arb(s2) / (A - B)) / 2

    sign_k = -1 if k % 2 else 1
    sign_l = -1 if l % 2 else 1
    Iexp = A * (1 - sign_k * (c * ell).exp()) / (c * c + A * A)

    return (
        ni
        * nj
        * (c * Iss + B * Isc - B * sign_l * (-c * ell).exp() * Iexp)
        / (c * c + B * B)
    )


def laplace_overlap_matrix(basis, c):
    """L_c(i,j)=int_0^infinity e^(-cr)<phi_i,T_r phi_j>dr."""
    m = len(basis)
    L = [[arb(0) for _ in range(m)] for __ in range(m)]
    for i, bi in enumerate(basis):
        for j, bj in enumerate(basis):
            if bi["label"] == bj["label"]:
                L[i][j] = same_interval_laplace(bi, bj, c)
            elif ORDER[bi["label"]] < ORDER[bj["label"]]:
                # Disjoint ordered supports: x <= y identically, hence factorization.
                L[i][j] = exp_moment(bi, c) * exp_moment(bj, -c)
            else:
                L[i][j] = arb(0)
    return L


def arch_partial(basis, K):
    m = len(basis)
    h0 = -arb.const_euler() - arb.pi() / 2 - 3 * arb(2).log() - arb.pi().log()
    A = [[arb(0) for _ in range(m)] for __ in range(m)]
    for i in range(m):
        A[i][i] = h0

    for n in range(K):
        c = arb(2 * n) + arb('0.5')
        L = laplace_overlap_matrix(basis, c)
        two_over_c = arb(2) / c
        for i in range(m):
            for j in range(m):
                v = -(L[i][j] + L[j][i])
                if i == j:
                    v += two_over_c
                A[i][j] += v
    return A


def overlap_formula(bi, bj, r, lower, upper):
    A, B = bi["A"], bj["A"]
    p = -A * bi["a"]
    q = B * (r - bj["a"])
    same_len = (
        (bi["label"] in ("O-", "O+") and bj["label"] in ("O-", "O+"))
        or (bi["label"] in ("S-", "S+") and bj["label"] in ("S-", "S+"))
    )

    def Icos(c, phase, zero=False):
        if zero:
            return (upper - lower) * phase.cos()
        return ((c * upper + phase).sin() - (c * lower + phase).sin()) / c

    return (
        bi["norm"]
        * bj["norm"]
        / 2
        * (
            Icos(A - B, p - q, zero=(same_len and bi["k"] == bj["k"]))
            - Icos(A + B, p + q)
        )
    )


def fixed_shift_overlap(basis, i, j, q):
    """Support-exact overlap at r=log(q), with exact selector logic.

    Since every interval endpoint is the logarithm of a positive rational and
    the shift is log(q), max/min support choices are equivalent to comparing
    rational multiplicative endpoints.  This removes floating-point branch
    decisions from the rigorous certificate.
    """
    bi, bj = basis[i], basis[j]
    r = arb(q).log()

    l1q, l2q = bi["aq"], bj["aq"] / q
    u1q, u2q = bi["bq"], bj["bq"] / q

    lower_q = max(l1q, l2q)
    upper_q = min(u1q, u2q)
    if upper_q <= lower_q:
        return arb(0)

    lower = bi["a"] if l1q >= l2q else bj["a"] - r
    upper = bi["b"] if u1q <= u2q else bj["b"] - r
    return overlap_formula(bi, bj, r, lower, upper)


def prime_matrix(basis):
    m = len(basis)
    M = [[arb(0) for _ in range(m)] for __ in range(m)]
    for q, p in PRIME_POWERS.items():
        weight = arb(p).log() / arb(q).sqrt()
        for i in range(m):
            for j in range(m):
                M[i][j] += -weight * (
                    fixed_shift_overlap(basis, i, j, q)
                    + fixed_shift_overlap(basis, j, i, q)
                )
    return M


def pole_matrix(basis):
    cp = arb('0.5')
    lp = [exp_moment(b, cp) for b in basis]
    lm = [exp_moment(b, -cp) for b in basis]
    m = len(basis)
    return [[lp[i] * lm[j] + lm[i] * lp[j] for j in range(m)] for i in range(m)]


def add_three(A, B, C):
    n = len(A)
    return [[A[i][j] + B[i][j] + C[i][j] for j in range(n)] for i in range(n)]


def interval_ldlt(M):
    n = len(M)
    d = [None] * n
    L = [[arb(0) for _ in range(n)] for __ in range(n)]
    pivots = []
    for i in range(n):
        s = M[i][i]
        for k in range(i):
            s -= L[i][k] * L[i][k] * d[k]
        pivots.append(s)
        d[i] = s
        if not (s > 0):
            return False, pivots, i
        for j in range(i + 1, n):
            t = M[j][i]
            for k in range(i):
                t -= L[j][k] * L[i][k] * d[k]
            L[j][i] = t / d[i]
    return True, pivots, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, default=1000)
    ap.add_argument("--prec", type=int, default=256, help="Arb precision in bits")
    args = ap.parse_args()

    ctx.prec = args.prec
    basis = make_basis()
    print("RH LOG3 N=2 ARB CERTIFICATE")
    print("dimension=8 K=%d arb_prec=%d bits" % (args.K, args.prec), flush=True)
    print("support selectors=exact rational comparisons", flush=True)
    print("building closed-form archimedean lower sum ...", flush=True)
    Aarch = arch_partial(basis, args.K)
    print("building exact finite prime/pole blocks ...", flush=True)
    M = add_three(Aarch, prime_matrix(basis), pole_matrix(basis))
    ok, pivots, bad = interval_ldlt(M)

    for i, p in enumerate(pivots):
        print(
            "pivot[%d] mid=%s rad=%s"
            % (i, p.mid().str(40, radius=False), p.rad().str(12, radius=False))
        )

    if not ok:
        print("UNDETERMINED: pivot %d is not strictly positive" % bad)
        sys.exit(2)

    print("CERTIFIED: all 8 Arb LDL^T pivots are strictly positive.")
    print("THEOREM STEP: every omitted J_c is PSD, so the complete archimedean series only adds a PSD matrix.")
    print("RESULT: the complete Weil Gram matrix is positive definite on the declared 8-dimensional H_log3 branch-sine subspace.")
    print("BOUNDARY: finite-subspace certificate only; not full H_log3 positivity and not RH.")


if __name__ == "__main__":
    main()
