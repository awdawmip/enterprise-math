"""R5 author-side exact upstream J source-mixture phase certificate.

All rational arithmetic is fractions.Fraction.  No external optimizer is used.
The one-parameter real theorem follows from complete deterministic strategy
coverage and exact affine/quadratic Bernstein interpolation.
"""
from fractions import Fraction as F
from itertools import product

ZERO, ONE = F(0), F(1)
ETA, Z = F(1, 2), F(3, 4)
M = (-211, 10, -113, 0)
N0 = (200, -1280, -760, 1936)
N1 = (-680, -1216, -200, 656)
FULL_N_WITNESS = (0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1)
LR_N_WITNESS = (0, 0, 0, 0, 1)
FULL_M_CONST = (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0)
LR_M_CONST = (0, 1, 1, 0, 0)
FULL_M_AFF = (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
LR_M_AFF = (0, 0, 1, 0, 0)
COUNTS = {"flow_evaluations": 0, "Bernstein_FULL": 0, "Bernstein_LR": 0}


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), ZERO)


def observer(bits, lam):
    """Source-tagged two-law positive flow; λ selects B's J-kernel mixture.

    FULL bits order p1,p2,q1,q2,qB,r,k1,k2,kB,l1,l2,lB.
    Decision nodes I=(1,1), J=(2,2), K=(3,8/5), L=(4,12/5).
    """
    lam = F(lam)
    assert ZERO <= lam <= ONE
    p1, p2, q1, q2, qb, r, k1, k2, kb, l1, l2, lb = bits
    y, masses = [ZERO] * 4, [ZERO, ZERO]
    COUNTS["flow_evaluations"] += 1

    def terminal(ap, aq, ans, t):
        assert ap >= ZERO and aq >= ZERO
        masses[0] += ap
        masses[1] += aq
        if ans == "P":
            y[0] += ap
        else:
            y[1] += aq
        y[2] += t * ap
        y[3] += t * aq

    def A_kernel_after_J(ap, aq, k, l):
        # Identical conditioned-on-J mechanism for both P and Q laws,
        # with law-specific probabilities on its nature edges.
        terminal(ap * F(3, 5), aq / 2, "Q", 3)
        ap *= F(2, 5)
        aq /= 2
        terminal(ap / 2, aq / 2, "P", 3)
        ap /= 2
        aq /= 2
        terminal(ap * k, aq * k, "P", 3)
        ap *= 1 - k
        aq *= 1 - k
        terminal(ap / 4, aq / 2, "Q", 4)
        ap *= F(3, 4)
        aq /= 2
        terminal(ap * l, aq * l, "P", 4)
        terminal(ap * (1 - l), aq * (1 - l), "Q", 5)

    for p, q, k, l in ((p1, q1, k1, l1), (p2, q2, k2, l2)):
        ap = aq = F(1, 8)
        terminal(ap * p, aq * p, "P", 1)
        ap *= 1 - p
        aq *= 1 - p
        terminal(ap / 2, aq * F(3, 4), "Q", 2)
        ap /= 2
        aq /= 4
        terminal(ap * q, aq * q, "P", 2)
        ap *= 1 - q
        aq *= 1 - q
        A_kernel_after_J(ap, aq, k, l)

    # B at J has P/Q masses (1/4,1/8), hence likelihood ratio 2.
    ap, aq = F(1, 4), F(1, 8)
    terminal(ap * qb, aq * qb, "P", 2)
    ap *= 1 - qb
    aq *= 1 - qb

    # A law-independent source-B nature coin λ at J is the new upstream
    # coupling. On its A-kernel route B uses K bit kb and L bit lb.
    A_kernel_after_J(ap * lam, aq * lam, kb, lb)
    ap *= 1 - lam
    aq *= 1 - lam
    terminal(ap * (1 - F(6, 5) * ETA) * (1 - Z),
             aq * (1 - ETA) * (1 - Z), "P", 4)
    terminal(ap * (1 - F(6, 5) * ETA) * Z,
             aq * (1 - ETA) * Z, "Q", 4)
    ap *= F(6, 5) * ETA
    aq *= ETA
    terminal(ap * lb, aq * lb, "P", 4)
    terminal(ap * (1 - lb), aq * (1 - lb), "Q", 5)

    terminal(F(1, 2) * r, F(5, 8) * r, "Q", 1)
    terminal(F(1, 2) * (1 - r), F(5, 8) * (1 - r), "P", 3)
    assert masses == [ONE, ONE]
    return tuple(y)


def lr(bits, lam):
    p, q, r, k, l = bits
    return observer((p, p, q, q, q, r, k, k, k, l, l, l), lam)


def normal(lam):
    return tuple(a + lam * b for a, b in zip(N0, N1))


def bernstein_certificate(name, fn, all_bits, intercept, slope):
    # Against claimed maximum I + slope*λ of n(λ)·O(λ).
    # For each deterministic strategy the difference is quadratic:
    #   A λ²+B λ+C = b0(1−λ)²+2 b1 λ(1−λ)+b2 λ².
    # b0,b1,b2 ≥ 0 proves every-real λ∈[0,1] dominance.
    mins = [None, None, None]
    tight = [0, 0, 0]
    for bits in all_bits:
        u = fn(bits, ZERO)
        v = tuple(b - a for a, b in zip(u, fn(bits, ONE)))
        C = intercept - dot(N0, u)
        B = slope - dot(N1, u) - dot(N0, v)
        A = -dot(N1, v)
        coeffs = (C, C + B / 2, C + B + A)
        assert all(c >= 0 for c in coeffs), (name, bits, coeffs)
        mins = [c if m is None else min(m, c) for m, c in zip(mins, coeffs)]
        tight = [old + (c == 0) for old, c in zip(tight, coeffs)]
        COUNTS["Bernstein_" + name] += 1
    assert mins == [ZERO, ZERO, ZERO], (name, mins)
    print(name, "Bernstein certificates", COUNTS["Bernstein_" + name],
          "min_coefficient", tuple(mins), "tight_counts", tuple(tight))


def witness_line(fn, bits, intercept, slope):
    u, v = fn(bits, ZERO), fn(bits, ONE)
    d = tuple(b - a for a, b in zip(u, v))
    assert dot(N0, u) == intercept
    assert dot(N1, u) + dot(N0, d) == slope
    assert dot(N1, d) == ZERO


def m_phase_check(name, fn, all_bits, const_bits, aff_bits, const, aff0, affs, cutoff):
    assert aff0 + affs * cutoff == const
    def max_m(lam):
        return max(dot(M, fn(bits, lam)) for bits in all_bits)
    for lam in (ZERO, cutoff, ONE):
        expected = max(F(const), F(aff0) + affs * lam)
        got = max_m(lam)
        assert got == expected, (name, lam, got, expected)
        assert dot(M, fn(const_bits, lam)) == const
        assert dot(M, fn(aff_bits, lam)) == F(aff0) + affs * lam
        print(name, "M envelope at λ=", lam, "=", got)
    # Every fixed deterministic M value is AFFINE in λ. Between these
    # three points a convex, upper-envelope bound follows by linearity.


def main():
    FB = tuple(product((0, 1), repeat=12))
    LB = tuple(product((0, 1), repeat=5))
    assert len(FB) == 4096 and len(LB) == 32
    # Strict positivity of all stated nature edges for λ in (0,1).
    assert all(x > 0 for x in (ETA, 1 - ETA, F(6, 5) * ETA,
                               1 - F(6, 5) * ETA, Z, 1 - Z,
                               F(3, 5), F(2, 5), F(1, 2), F(1, 4), F(3, 4)))
    assert observer(FULL_M_CONST, ZERO) == (F(11, 40), F(55, 64), F(267, 160), F(187, 128))
    # Exact full-history and LR support bounds for adaptive signed direction.
    witness_line(observer, FULL_N_WITNESS, F(3146), F(370))
    witness_line(lr, LR_N_WITNESS, F(3117), F(399))
    bernstein_certificate("FULL", observer, FB, F(3146), F(370))
    bernstein_certificate("LR", lr, LB, F(3117), F(399))
    for lam in (ZERO, F(1, 8), F(1, 2), F(7, 8), F(99, 100), ONE):
        f = dot(normal(lam), observer(FULL_N_WITNESS, lam))
        l = dot(normal(lam), lr(LR_N_WITNESS, lam))
        assert f - l == 29 * (1 - lam)
        assert sum(abs(c) for c in normal(lam)) <= 6528
        print("adaptive λ=", lam, "FULL", f, "LR", l, "signed_gap", f - l)
    # Exact phase boundaries for the former parameter-independent M.
    m_phase_check("FULL", observer, FB, FULL_M_CONST, FULL_M_AFF,
                  F(-238), -F(42061, 160), F(4781, 160), F(3981, 4781))
    m_phase_check("LR", lr, LB, LR_M_CONST, LR_M_AFF,
                  -F(481, 2), -F(42061, 160), F(4781, 160), F(3581, 4781))
    assert F(3981, 4781) < ONE
    assert F(3581, 4781) < F(3981, 4781)
    # At λ=1 the B-kernel is identical to the A kernel. Exact
    # key-wise aggregation of P/Q action flows gives actual-image equality;
    # the statement itself is proved in RESEARCH.md, not by these samples.
    assert dot(normal(ONE), observer(FULL_N_WITNESS, ONE)) == dot(normal(ONE), lr(LR_N_WITNESS, ONE))
    print("computed_flow_evaluations", COUNTS["flow_evaluations"])
    print("ALL_REAL certificate: max_FULL n(λ)=3146+370λ, max_LR n(λ)=3117+399λ")
    print("ALL_REAL signed_gap=29(1−λ); positive for all 0<=λ<1")
    print("OLD M gap: 5/2 to λ=3581/4781, declines, then zero from λ=3981/4781")
    print("λ=1: source-independent J/K/L continuation; actual-image equality by flow aggregation")
    print("scope: exact rational finite auxiliary model; author-side; not native X6 admission")
    print("PASS_EXACT_R5_UPSTREAM_J_MIX_ADAPTIVE_SUPPORT_PHASE")


if __name__ == "__main__":
    main()
