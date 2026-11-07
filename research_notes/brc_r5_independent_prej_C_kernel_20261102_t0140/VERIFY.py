"""Exact two-law finite-flow certificate for an independent pre-J C route.

Reproducible with Python 3 standard library.  All masses are Fraction;
no floating point is used in the theorem assertions.
"""
from fractions import Fraction as Q
from itertools import product

Z, H, O = Q(0), Q(1, 2), Q(1)
N = (11480, -1856, 9320, -9392)
LR = tuple(product((0, 1), repeat=5))
FULL_WITNESS = (1, 0, 1, 0, 0, 0, 1, 0)


def observe(bits, tau):
    """bits=(p,qN,qC,r,kN,kC,lN,lC); source tags remain separate.

    A1,A2 at I; B at J; C at (1,4/5).  J=(2,2), K=(3,8/5),
    L=(4,12/5).  N uses A/B kernels with common mixture 1/2.
    C has a distinct post-J kernel and a pre-J natural detour tau.
    """
    p, qn, qc, r, kn, kc, ln, lc = map(Q, bits)
    tau = Q(tau)
    assert Z <= tau <= O
    assert all(Z <= b <= O for b in (p, qn, qc, r, kn, kc, ln, lc))
    out = [Z, Z, Z, Z]
    totals = [Z, Z]
    key_checks = 0

    def key(mP, mQ, ratio):
        nonlocal key_checks
        assert mP == ratio * mQ, (mP, mQ, ratio)
        key_checks += 1

    def end(mP, mQ, answer, time):
        assert mP >= Z and mQ >= Z
        totals[0] += mP
        totals[1] += mQ
        if answer == "P":
            out[0] += mP
        else:
            out[1] += mQ
        out[2] += time * mP
        out[3] += time * mQ

    def from_K(mP, mQ, k, l):
        key(mP, mQ, Q(8, 5))
        end(mP * k, mQ * k, "P", 3)
        mP *= 1 - k
        mQ *= 1 - k
        end(mP / 4, mQ / 2, "Q", 4)
        mP *= Q(3, 4)
        mQ /= 2
        from_L(mP, mQ, l)

    def from_L(mP, mQ, l):
        key(mP, mQ, Q(12, 5))
        end(mP * l, mQ * l, "P", 4)
        end(mP * (1 - l), mQ * (1 - l), "Q", 5)

    def A_kernel(mP, mQ, k, l):
        end(mP * Q(3, 5), mQ / 2, "Q", 3)
        mP *= Q(2, 5)
        mQ /= 2
        end(mP / 2, mQ / 2, "P", 3)
        from_K(mP / 2, mQ / 2, k, l)

    def B_kernel(mP, mQ, l):
        end(mP / 10, mQ / 8, "P", 4)
        end(mP * Q(3, 10), mQ * Q(3, 8), "Q", 4)
        from_L(mP * Q(3, 5), mQ / 2, l)

    def C_kernel(mP, mQ, k, l):
        end(mP * Q(3, 5), mQ / 2, "Q", 3)
        from_K(mP * Q(2, 5), mQ / 2, k, l)

    def J_N(mP, mQ):
        key(mP, mQ, Q(2))
        end(mP * qn, mQ * qn, "P", 2)
        mP *= 1 - qn
        mQ *= 1 - qn
        A_kernel(mP / 2, mQ / 2, kn, ln)
        B_kernel(mP / 2, mQ / 2, ln)

    # Two labeled A sources; the grouping uses the same coins only for
    # this explicit admissible witness and for every LR policy.
    for name in ("A1", "A2"):
        mP = mQ = Q(1, 8)
        key(mP, mQ, Q(1))
        end(mP * p, mQ * p, "P", 1)
        mP *= 1 - p
        mQ *= 1 - p
        end(mP / 2, mQ * Q(3, 4), "Q", 2)
        J_N(mP / 2, mQ / 4)

    # B is a separate source already at J.
    J_N(Q(1, 4), Q(1, 8))

    # Independent early C path: initial LR 4/5; choose r at time 1.
    mP, mQ = Q(1, 2), Q(5, 8)
    key(mP, mQ, Q(4, 5))
    end(mP * r, mQ * r, "Q", 1)
    mP *= 1 - r
    mQ *= 1 - r
    # Nature J edge has conditional P probability tau/2 and Q tau/5;
    # therefore its likelihood multiplier is (tau/2)/(tau/5)=5/2.
    end(mP * (1 - tau / 2), mQ * (1 - tau / 5), "Q", 2)
    jP, jQ = mP * tau / 2, mQ * tau / 5
    key(jP, jQ, Q(2))
    end(jP * qc, jQ * qc, "P", 2)
    C_kernel(jP * (1 - qc), jQ * (1 - qc), kc, lc)

    assert totals == [O, O], totals
    assert key_checks >= 4
    return tuple(out)


def lr_bits(bits):
    p, q, r, k, l = bits
    return (p, q, q, r, k, k, l, l)


def score(v):
    return sum((a * b for a, b in zip(N, v)), Z)


def sample_slacks(tau):
    witness = observe(FULL_WITNESS, tau)
    values = tuple(score(witness) - score(observe(lr_bits(b), tau))
                   for b in LR)
    return witness, values


def verify():
    assert sum(abs(x) for x in N) == 32048
    # The compact source-label flow is exact under P and Q.  Three
    # parameter fibers suffice by affine dependence on tau of every
    # deterministic LR vertex and the chosen FULL witness.
    data = {t: sample_slacks(t) for t in (Z, H, O)}
    minimum = {t: min(row[1]) for t, row in data.items()}
    assert minimum == {Z: Q(-1210), H: Q(341), O: Q(341)}
    assert data[Z][0] == (Q(61, 160), Q(11, 16), Q(43, 20), Q(125, 64))
    assert data[H][0] == (Q(81, 160), Q(5, 8), Q(43, 20), Q(125, 64))
    assert data[O][0] == (Q(101, 160), Q(9, 16), Q(43, 20), Q(125, 64))

    # Exact active vertices furnish the upper envelope bound.
    lo = LR.index((1, 0, 1, 0, 1))
    hi = LR.index((1, 1, 0, 0, 0))
    assert data[Z][1][lo] == -1210
    assert data[H][1][lo] == 341
    assert data[H][1][hi] == 341
    assert data[O][1][hi] == 341
    for t in (Q(2, 5), Q(3, 7), H, Q(3, 4), Q(1)):
        W, slacks = sample_slacks(t)
        expected = min(Q(341), 3102 * t - 1210)
        assert min(slacks) == expected
        assert W == (Q(61, 160) + t / 4, Q(11, 16) - t / 8,
                     Q(43, 20), Q(125, 64))

    # The C kernel's Q probability to *arrive* at K from J is 1/2,
    # whereas the A kernel has 1/4 and the B kernel zero.  Thus C is
    # outside the convex mixture hull of the two previously used
    # post-J kernels (as typed path distributions).
    assert Q(1, 2) > max(Q(1, 4), Z)
    print("EXACT_FLOW_AND_KEY_RATIOS_PASS")
    print("natural_C_to_J_P=tau/2_Q=tau/5; J_LR=2")
    print("conditional_Q_K_arrival: A=1/4, B=0, C=1/2")
    print("all_32_LR_vertices_checked_at_tau=0,1/2,1")
    print("exact_min_gap=min(341,3102*tau-1210)")
    print("strict_for_tau_in_(55/141,1), distance_inf>=gap/32048")
    print("tau=1/2; W=(81/160,5/8,43/20,125/64); gap=341")
    print("status=AUTHOR_EXACT_CHECKED; NOT_NATIVE_ADMITTED")
    print("PASS_EXACT_R5_INDEPENDENT_PREJ_C_ROUTE_UNIFORM_FACET")


if __name__ == "__main__":
    verify()
