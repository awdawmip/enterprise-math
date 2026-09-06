#!/usr/bin/env python3
"""Rigorous Arb certificate attempt for the 32-dimensional N=8 four-branch
Dirichlet-sine subspace of the Riemann-Weil form on H_{log 3}.

The archimedean matrix is written as
    h0 I + sum_{n>=0} J_{2n+1/2},      J_c >= 0.
We sum the first K terms exactly in Arb.  The infinite tail is not discarded:
its algebraic part is expanded through c^{-P} and summed exactly with Hurwitz
zeta, while a rigorous elementwise ball encloses the convergent algebraic
remainder and all exponentially small endpoint terms.

Default parameters K=10000, P=10 were selected from an independent floating
pressure test.  There is no numerical quadrature and no frequency cutoff.

Boundary: finite 32-dimensional subspace only.  This is not positivity on all
of H_{log 3} and is not an RH proof.
"""
import argparse
from fractions import Fraction
import sys

from flint import arb, ctx

ORDER = {"S-": 0, "O-": 1, "O+": 2, "S+": 3}
PRIME_POWERS = {2: 2, 3: 3, 4: 2, 5: 5, 7: 7, 8: 2, 9: 3}


def make_basis(N=8):
    L2 = arb(2).log()
    L3 = arb(3).log()
    intervals = [
        (-L3, -L2, "S-", Fraction(1, 3), Fraction(1, 2)),
        (-L2, arb(0), "O-", Fraction(1, 2), Fraction(1, 1)),
        (arb(0), L2, "O+", Fraction(1, 1), Fraction(2, 1)),
        (L2, L3, "S+", Fraction(2, 1), Fraction(3, 1)),
    ]
    out = []
    for a, b, label, aq, bq in intervals:
        ell = b - a
        for k in range(1, N + 1):
            out.append(
                dict(
                    a=a, b=b, aq=aq, bq=bq, ell=ell, label=label, k=k,
                    A=arb.pi() * k / ell,
                    norm=(arb(2) / ell).sqrt(),
                )
            )
    return out


def zero_matrix(n):
    return [[arb(0) for _ in range(n)] for __ in range(n)]


def exp_moment(b, c):
    A, ell, a, norm, k = b["A"], b["ell"], b["a"], b["norm"], b["k"]
    sign = -1 if k % 2 else 1
    return norm * (c * a).exp() * A * (1 - sign * (c * ell).exp()) / (c * c + A * A)


def same_interval_laplace(bi, bj, c):
    ell = bi["ell"]
    A, B = bi["A"], bj["A"]
    ni, nj = bi["norm"], bj["norm"]
    k, l = bi["k"], bj["k"]
    Iss = ell / 2 if k == l else arb(0)
    if k == l:
        Isc = arb(0)
    else:
        s1 = 1 - ((-1) ** (k + l))
        s2 = 1 - ((-1) ** (k - l))
        Isc = (arb(s1) / (A + B) + arb(s2) / (A - B)) / 2
    sign_k = -1 if k % 2 else 1
    sign_l = -1 if l % 2 else 1
    # Stabilized form: no exp(+c ell) overflow.
    exp_part = -B * sign_l * A * ((-c * ell).exp() - sign_k) / (c * c + A * A)
    return ni * nj * (c * Iss + B * Isc + exp_part) / (c * c + B * B)


def ordered_distinct_laplace(bi, bj, c):
    """bi is strictly left of bj; factorized one-sided Laplace overlap.

    Expanded to exponent differences <= 0 to avoid overflow.
    """
    Ai, Aj = bi["A"], bj["A"]
    ni, nj = bi["norm"], bj["norm"]
    si = -1 if bi["k"] % 2 else 1
    sj = -1 if bj["k"] % 2 else 1
    num = (
        (c * (bi["a"] - bj["a"])).exp()
        - sj * (c * (bi["a"] - bj["b"])).exp()
        - si * (c * (bi["b"] - bj["a"])).exp()
        + si * sj * (c * (bi["b"] - bj["b"])).exp()
    )
    return ni * nj * Ai * Aj * num / ((c * c + Ai * Ai) * (c * c + Aj * Aj))


def laplace_overlap(bi, bj, c):
    if bi["label"] == bj["label"]:
        return same_interval_laplace(bi, bj, c)
    if ORDER[bi["label"]] < ORDER[bj["label"]]:
        return ordered_distinct_laplace(bi, bj, c)
    return arb(0)


def arch_partial(basis, K):
    m = len(basis)
    h0 = -arb.const_euler() - arb.pi() / 2 - 3 * arb(2).log() - arb.pi().log()
    A = zero_matrix(m)
    for i in range(m):
        A[i][i] = h0
    for n in range(K):
        if n and n % 1000 == 0:
            print("  exact-series term %d/%d" % (n, K), flush=True)
        c = arb(2 * n) + arb('0.5')
        L = zero_matrix(m)
        for i, bi in enumerate(basis):
            for j, bj in enumerate(basis):
                L[i][j] = laplace_overlap(bi, bj, c)
        two_over_c = arb(2) / c
        for i in range(m):
            for j in range(m):
                v = -(L[i][j] + L[j][i])
                if i == j:
                    v += two_over_c
                A[i][j] += v
    return A


# ---------- asymptotic tail coefficients ----------

def add_inv_series(d, q, coef, a2, P):
    r = 0
    while q + 2 * r <= P:
        p = q + 2 * r
        d[p] = d.get(p, arb(0)) + coef * ((-a2) ** r)
        r += 1


def add_product_inv_series(d, q, coef, a2, b2, P):
    max_t = (P - q) // 2
    for t in range(max_t + 1):
        s = arb(0)
        for r in range(t + 1):
            s += ((-a2) ** r) * ((-b2) ** (t - r))
        p = q + 2 * t
        d[p] = d.get(p, arb(0)) + coef * s


def local_Isc(bi, bj):
    k, l = bi["k"], bj["k"]
    A, B = bi["A"], bj["A"]
    if k == l:
        return arb(0)
    s1 = 1 - ((-1) ** (k + l))
    s2 = 1 - ((-1) ** (k - l))
    return (arb(s1) / (A + B) + arb(s2) / (A - B)) / 2


def L_algebraic_coeffs(bi, bj, P):
    """Power coefficients of the non-exponential part of L_c in x=1/c."""
    d = {}
    if bi["label"] == bj["label"]:
        ell = bi["ell"]
        A, B = bi["A"], bj["A"]
        ni, nj = bi["norm"], bj["norm"]
        k, l = bi["k"], bj["k"]
        Iss = ell / 2 if k == l else arb(0)
        Isc = local_Isc(bi, bj)
        sk = -1 if k % 2 else 1
        sl = -1 if l % 2 else 1
        add_inv_series(d, 1, ni * nj * Iss, B * B, P)
        add_inv_series(d, 2, ni * nj * B * Isc, B * B, P)
        add_product_inv_series(d, 4, ni * nj * B * sl * sk * A, A * A, B * B, P)
    elif ORDER[bi["label"]] < ORDER[bj["label"]] and bi["bq"] == bj["aq"]:
        # The only non-exponentially-small distinct-interval term is the
        # touching endpoint b_i=a_j.
        si = -1 if bi["k"] % 2 else 1
        coef = bi["norm"] * bj["norm"] * bi["A"] * bj["A"] * (-si)
        add_product_inv_series(d, 4, coef, bi["A"] ** 2, bj["A"] ** 2, P)
    return d


def tail_power_sum(p, K):
    # c_n=2(n+1/4): sum_{n>=K} c_n^{-p}=2^{-p} zeta(p,K+1/4).
    return arb(p).zeta(arb(K) + arb('0.25')) / (arb(2) ** p)


def coefficient_matrices(basis, P):
    m = len(basis)
    Lc = {p: zero_matrix(m) for p in range(2, P + 1)}
    # p=1 is not stored: exact orthonormality gives L_1=I and hence
    # 2I/c-L/c-L^T/c=0 identically.
    for i, bi in enumerate(basis):
        for j, bj in enumerate(basis):
            d = L_algebraic_coeffs(bi, bj, P)
            for p, v in d.items():
                if p >= 2:
                    Lc[p][i][j] += v
    C = {p: zero_matrix(m) for p in range(2, P + 1)}
    for p in range(2, P + 1):
        for i in range(m):
            for j in range(m):
                C[p][i][j] = -(Lc[p][i][j] + Lc[p][j][i])
    return C


def ratio_log(q):
    """Arb enclosure of log(q) for an exact positive Fraction q."""
    return arb(q.numerator).log() - arb(q.denominator).log()


def single_inv_remainder(q, coef, a, P, K):
    R = (P - q) // 2
    first = R + 1
    p = q + 2 * first
    C0 = arb(2 * K) + arb('0.5')
    aa = a.abs_upper()
    rho = (aa / C0) ** 2
    denom = arb(1) - rho
    val = coef.abs_upper() * (aa ** (2 * first)) / denom * tail_power_sum(p, K)
    return val.upper()


def product_inv_remainder(q, coef, a, b, P, K):
    max_t = (P - q) // 2
    T = max_t + 1
    p = q + 2 * T
    C0 = arb(2 * K) + arb('0.5')
    # a+b is a simple certified upper bound for max(a,b).
    M = a.abs_upper() + b.abs_upper()
    rho = (M / C0) ** 2
    one_minus = arb(1) - rho
    factor = arb(T + 1) / one_minus + rho / (one_minus * one_minus)
    val = coef.abs_upper() * (M ** (2 * T)) * factor * tail_power_sum(p, K)
    return val.upper()


def L_algebraic_remainder(bi, bj, P, K):
    err = arb(0)
    if bi["label"] == bj["label"]:
        ell = bi["ell"]
        A, B = bi["A"], bj["A"]
        ni, nj = bi["norm"], bj["norm"]
        k, l = bi["k"], bj["k"]
        Iss = ell / 2 if k == l else arb(0)
        Isc = local_Isc(bi, bj)
        sk = -1 if k % 2 else 1
        sl = -1 if l % 2 else 1
        if not Iss.is_zero():
            err += single_inv_remainder(1, ni * nj * Iss, B, P, K)
        if not Isc.is_zero():
            err += single_inv_remainder(2, ni * nj * B * Isc, B, P, K)
        err += product_inv_remainder(4, ni * nj * B * sl * sk * A, A, B, P, K)
    elif ORDER[bi["label"]] < ORDER[bj["label"]] and bi["bq"] == bj["aq"]:
        si = -1 if bi["k"] % 2 else 1
        coef = bi["norm"] * bj["norm"] * bi["A"] * bj["A"] * (-si)
        err += product_inv_remainder(4, coef, bi["A"], bj["A"], P, K)
    return err.upper()


def exp_geometric_tail(coeff, d, K):
    """Bound sum_{n>=K} coeff*e^{-c_n d}/c_n^4, d>0."""
    C0 = arb(2 * K) + arb('0.5')
    denom = arb(1) - (-arb(2) * d).exp()
    val = coeff.abs_upper() * (C0 ** -4) * (-C0 * d).exp() / denom
    return val.upper()


def L_exponential_remainder(bi, bj, K):
    if bi["label"] == bj["label"]:
        coeff = bi["norm"] * bj["norm"] * bi["A"] * bj["A"]
        return exp_geometric_tail(coeff, bi["ell"], K)
    if ORDER[bi["label"]] >= ORDER[bj["label"]]:
        return arb(0)

    coeff = bi["norm"] * bj["norm"] * bi["A"] * bj["A"]
    # Four endpoint exponent gaps in the expanded factorized numerator.
    ratios = [
        bj["aq"] / bi["aq"],
        bj["bq"] / bi["aq"],
        bj["aq"] / bi["bq"],
        bj["bq"] / bi["bq"],
    ]
    err = arb(0)
    for q in ratios:
        if q == 1:
            continue  # touching endpoint: retained in algebraic series
        err += exp_geometric_tail(coeff, ratio_log(q), K)
    return err.upper()


def accelerated_tail(basis, K, P):
    m = len(basis)
    C = coefficient_matrices(basis, P)
    T = zero_matrix(m)
    for p in range(2, P + 1):
        Sp = tail_power_sum(p, K)
        for i in range(m):
            for j in range(m):
                T[i][j] += C[p][i][j] * Sp

    max_radius = arb(0)
    for i, bi in enumerate(basis):
        for j, bj in enumerate(basis):
            err = (
                L_algebraic_remainder(bi, bj, P, K)
                + L_algebraic_remainder(bj, bi, P, K)
                + L_exponential_remainder(bi, bj, K)
                + L_exponential_remainder(bj, bi, K)
            ).upper()
            if err > max_radius:
                max_radius = err
            T[i][j] += arb(0, err)
    return T, max_radius


# ---------- exact finite prime/pole blocks ----------

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

    return bi["norm"] * bj["norm"] / 2 * (
        Icos(A - B, p - q, zero=(same_len and bi["k"] == bj["k"]))
        - Icos(A + B, p + q)
    )


def fixed_shift_overlap(basis, i, j, q):
    bi, bj = basis[i], basis[j]
    r = arb(q).log()
    l1q, l2q = bi["aq"], bj["aq"] / q
    u1q, u2q = bi["bq"], bj["bq"] / q
    if min(u1q, u2q) <= max(l1q, l2q):
        return arb(0)
    lower = bi["a"] if l1q >= l2q else bj["a"] - r
    upper = bi["b"] if u1q <= u2q else bj["b"] - r
    return overlap_formula(bi, bj, r, lower, upper)


def prime_matrix(basis):
    m = len(basis)
    M = zero_matrix(m)
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


def add_matrices(*mats):
    n = len(mats[0])
    return [[sum((M[i][j] for M in mats), arb(0)) for j in range(n)] for i in range(n)]


def interval_ldlt(M):
    n = len(M)
    d = [None] * n
    L = zero_matrix(n)
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
    ap.add_argument("--K", type=int, default=10000)
    ap.add_argument("--P", type=int, default=10)
    ap.add_argument("--prec", type=int, default=384, help="Arb precision in bits")
    args = ap.parse_args()
    if args.P < 6:
        raise SystemExit("P must be at least 6 for this certificate path")

    ctx.prec = args.prec
    basis = make_basis(8)
    print("RH LOG3 N=8 ACCELERATED ARB CERTIFICATE")
    print("dimension=32 K=%d P=%d arb_prec=%d bits" % (args.K, args.P, args.prec), flush=True)
    print("support selectors=exact rational comparisons", flush=True)
    print("building exact closed-form partial archimedean sum ...", flush=True)
    A0 = arch_partial(basis, args.K)
    print("building Hurwitz-zeta accelerated rigorous tail ...", flush=True)
    Atail, max_tail_radius = accelerated_tail(basis, args.K, args.P)
    print("max tail enclosure radius=%s" % max_tail_radius.str(20, radius=False), flush=True)
    print("building exact finite prime/pole blocks ...", flush=True)
    M = add_matrices(A0, Atail, prime_matrix(basis), pole_matrix(basis))
    print("running interval LDL^T ...", flush=True)
    ok, pivots, bad = interval_ldlt(M)

    for i, p in enumerate(pivots):
        print("pivot[%d] mid=%s rad=%s" % (
            i, p.mid().str(30, radius=False), p.rad().str(10, radius=False)))

    if not ok:
        print("UNDETERMINED: pivot %d is not strictly positive" % bad)
        sys.exit(2)

    print("CERTIFIED: all 32 Arb LDL^T pivots are strictly positive.")
    print("TAIL: n>=K is rigorously enclosed by Hurwitz-zeta algebraic acceleration plus explicit exponential/remainder balls.")
    print("RESULT: the complete Weil Gram matrix is positive definite on the declared 32-dimensional N=8 H_log3 branch-sine subspace.")
    print("BOUNDARY: finite-subspace certificate only; not full H_log3 positivity and not RH.")


if __name__ == "__main__":
    main()
