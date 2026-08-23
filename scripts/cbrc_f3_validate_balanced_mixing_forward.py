#!/usr/bin/env python3
"""Deterministic validator for CBRC F3 balanced reversible mixing forward classification.

Uses only exact integer / finite-field / Fraction arithmetic.
No external mathematical source or package is required.
"""
from fractions import Fraction
import hashlib
import itertools
import json

MOD_T = 3
MOD_Q = 6
A = ((2, 3), (3, 4))
AINV = ((-4, 3), (3, -2))
P = ((0, 1), (1, 0))
L = ((1, 0), (0, -1))
RSGN = ((-1, 0), (0, 1))
B0 = ((0, 0), (0, 0))
I2_3 = ((1, 0), (0, 1))


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def mmul(x, y):
    return (
        (x[0][0] * y[0][0] + x[0][1] * y[1][0], x[0][0] * y[0][1] + x[0][1] * y[1][1]),
        (x[1][0] * y[0][0] + x[1][1] * y[1][0], x[1][0] * y[0][1] + x[1][1] * y[1][1]),
    )


def mvec(m, v):
    return (m[0][0] * v[0] + m[0][1] * v[1], m[1][0] * v[0] + m[1][1] * v[1])


def q_base(n):
    r = n % MOD_Q
    if r == 0:
        return Fraction(0)
    if r in (1, 5):
        return Fraction(1)
    return Fraction(1, 2)


def q(n, t, delta=Fraction(0)):
    t %= MOD_T
    bonus = delta if (n % MOD_T == 0 and t != 0) else Fraction(0)
    return q_base(n) + bonus


def R(n, t):
    return (n, (t + n) % 3)


def J(n, t):
    return (-n, (-t) % 3)


def S(n, t):
    return (n, (-t) % 3)


def apply_general(state, free=A, B=B0, D=I2_3):
    (n1, t1), (n2, t2) = state
    u, v = mvec(free, (n1, n2))
    r1, r2 = n1 % 3, n2 % 3
    ot1 = (B[0][0] * r1 + B[0][1] * r2 + D[0][0] * t1 + D[0][1] * t2) % 3
    ot2 = (B[1][0] * r1 + B[1][1] * r2 + D[1][0] * t1 + D[1][1] * t2) % 3
    return ((u, ot1), (v, ot2))


def apply_m(state):
    return apply_general(state, A, B0, I2_3)


def apply_m_inv(state):
    return apply_general(state, AINV, B0, I2_3)


def Q(state, delta=Fraction(0)):
    return q(*state[0], delta) + q(*state[1], delta)


def coeff_add(x, y):
    return (x[0] + y[0], (x[1] + y[1]) % 3)


def coeff_neg(x):
    return (-x[0], (-x[1]) % 3)


def all_gl2_f3():
    out = []
    for a, b, c, d in itertools.product(range(3), repeat=4):
        m = ((a, b), (c, d))
        if det2(m) % 3 != 0:
            out.append(m)
    return out


def all_b_f3():
    return [((a, b), (c, d)) for a, b, c, d in itertools.product(range(3), repeat=4)]


def finite_states():
    return [((n1, t1), (n2, t2))
            for n1 in range(6) for t1 in range(3)
            for n2 in range(6) for t2 in range(3)]


def preserves(delta, B=B0, D=I2_3):
    for st in finite_states():
        if Q(apply_general(st, A, B, D), delta) != Q(st, delta):
            return False
    return True


def check_accepted_relations():
    reps = [(n, t) for n in range(-3, 4) for t in range(3)]
    assert all(R(*R(*R(n, t))) == (n, t % 3) for n, t in reps)
    assert all(S(*S(n, t)) == (n, t % 3) for n, t in reps)
    for z in reps:
        lhs = S(*R(*S(*z)))
        rinv = R(*R(*z))
        assert lhs == rinv
        assert q(*R(*z), Fraction(1)) == q(*z, Fraction(1))
        assert q(*J(*z), Fraction(1)) == q(*z, Fraction(1))
        assert q(*S(*z), Fraction(1)) == q(*z, Fraction(1))
    e = (1, 0)
    tau = (0, 1)
    assert coeff_add(e, coeff_neg(e)) == (0, 0)
    assert coeff_add(e, J(*R(*e))) == coeff_neg(tau)
    return True


def check_branch_relation():
    pap = mmul(mmul(P, A), P)
    rhs = mmul(mmul(L, AINV), RSGN)
    assert pap == ((4, 3), (3, 2))
    assert pap == rhs
    return pap


def check_scalar_family():
    for delta in (Fraction(0), Fraction(1), Fraction(5, 2)):
        assert q(0, 0, delta) == 0
        assert q(1, 0, delta) == 1
        assert preserves(delta)
        for st in finite_states():
            out = apply_m(st)
            assert Q(out, delta) == Q(st, delta)
            assert apply_m_inv(out) == st
            assert Q(apply_m_inv(st), delta) == Q(st, delta)
        split = apply_m((((1, 0)), ((0, 0))))
        assert split == (((2, 0)), ((3, 0)))
        assert q(*split[0], delta) == Fraction(1, 2)
        assert q(*split[1], delta) == Fraction(1, 2)
    assert q(0, 1, Fraction(0)) == 0
    assert q(0, 1, Fraction(1)) == 1
    assert q(6, 0, Fraction(1)) == 0
    return True


def check_composition_depth4():
    for delta in (Fraction(0), Fraction(1)):
        for st in finite_states():
            cur = st
            for depth in range(1, 5):
                cur = apply_m(cur)
                assert Q(cur, delta) == Q(st, delta)
            back = cur
            for _ in range(4):
                back = apply_m_inv(back)
            assert back == st
    return True


def torsion_survivor_counts():
    gl = all_gl2_f3()
    bs = all_b_f3()
    counts = {}
    for delta in (Fraction(0), Fraction(1)):
        c = 0
        b0c = 0
        for B in bs:
            for D in gl:
                if preserves(delta, B, D):
                    c += 1
                    if B == B0:
                        b0c += 1
        counts[str(delta)] = {"all_B_D": c, "with_B_zero": b0c}
    assert len(gl) == 48
    assert len(bs) == 81
    assert counts["0"]["all_B_D"] == 3888
    assert counts["1"]["all_B_D"] == 36
    return counts


def check_free_periodic_classification():
    def wt(n, t):
        r = n % 6
        if r == 0:
            return Fraction(0)
        if r in (1, 5):
            return Fraction(1)
        if r in (2, 4):
            return t
        return Fraction(1) - t
    for t in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)):
        for x, y in itertools.product(range(6), repeat=2):
            u, v = mvec(A, (x, y))
            assert wt(u, t) + wt(v, t) == wt(x, t) + wt(y, t)
    assert wt(2, Fraction(1, 2)) == wt(3, Fraction(1, 2)) == Fraction(1, 2)
    assert wt(2, Fraction(1, 4)) != wt(3, Fraction(1, 4))
    return True


def check_recoalescence_discriminator():
    e = (1, 0)
    je = J(*e)
    jre = J(*R(*e))
    st0 = (e, je)
    st1 = (e, jre)
    for delta in (Fraction(0), Fraction(1)):
        out0 = apply_m(st0)
        out1 = apply_m(st1)
        assert [q(*z, delta) for z in out0] == [Fraction(1), Fraction(1)]
        assert [q(*z, delta) for z in out1] == [Fraction(1), Fraction(1)]
        assert Q(out0, delta) == Q(out1, delta) == 2
        agg0 = coeff_add(*out0)
        agg1 = coeff_add(*out1)
        assert agg0 != agg1
        assert coeff_add(agg1, coeff_neg(agg0)) == (0, 2)
    return {
        "input_unmarked": [coeff_add(*st0), coeff_add(*st1)],
        "output_unmarked": [coeff_add(*apply_m(st0)), coeff_add(*apply_m(st1))],
    }


def check_ablations():
    N = ((2, 3), (3, 2))
    assert det2(N) == -5
    for x, y in itertools.product(range(6), repeat=2):
        u, v = mvec(N, (x, y))
        assert q_base(u) + q_base(v) == q_base(x) + q_base(y)
    assert q_base(2) == q_base(3) == Fraction(1, 2)

    def wt_t(n, t):
        r = n % 6
        if r == 0:
            return Fraction(0)
        if r in (1, 5):
            return Fraction(1)
        if r in (2, 4):
            return t
        return 1 - t
    t = Fraction(1, 4)
    assert wt_t(2, t) == Fraction(1, 4) and wt_t(3, t) == Fraction(3, 4)
    for x, y in itertools.product(range(6), repeat=2):
        u, v = mvec(A, (x, y))
        assert wt_t(u, t) + wt_t(v, t) == wt_t(x, t) + wt_t(y, t)

    def q_bad(n, torsion=0):
        n = abs(n)
        if n == 0:
            return Fraction(0)
        if n == 1:
            return Fraction(1)
        if n in (2, 3):
            return Fraction(1, 2)
        if n == 4:
            return Fraction(7)
        return Fraction(1)
    assert q_bad(2) == q_bad(3) == Fraction(1, 2)
    in_q = q_bad(2) + q_bad(0)
    u, v = mvec(A, (2, 0))
    out_q = q_bad(u) + q_bad(v)
    assert in_q != out_q
    assert q(6, 0, Fraction(1)) == 0 and (6, 0) != (0, 0)

    return {
        "without_M3_noninvertible_det": det2(N),
        "without_M4_balance_parameter_example": "t=1/4 gives split 1/4 + 3/4",
        "without_M6_counterexample": {"input_Q": str(in_q), "output_Q": str(out_q)},
        "global_strict_positivity_forced": False,
    }


def check_polynomial_relation():
    A2 = mmul(A, A)
    rhs = ((6 * A[0][0] + 1, 6 * A[0][1]), (6 * A[1][0], 6 * A[1][1] + 1))
    assert A2 == rhs
    return {"relation": "M^2 - 6 M - I = 0 on C1^2", "free_A2": A2}


def main():
    assert det2(A) == -1
    assert mmul(A, AINV) == ((1, 0), (0, 1))
    check_accepted_relations()
    pap = check_branch_relation()
    check_free_periodic_classification()
    check_scalar_family()
    check_composition_depth4()
    counts = torsion_survivor_counts()
    discr = check_recoalescence_discriminator()
    abl = check_ablations()
    poly = check_polynomial_relation()

    payload = {
        "schema": "CBRC_F3_CHECK_V1",
        "carrier": "Z e + Z/3 tau",
        "automorphism_structure": {
            "free_block": "A in GL(2,Z)",
            "cross_block_count": 81,
            "torsion_block_GL2_F3_count": 48,
            "cross_times_torsion_per_A": 3888,
        },
        "selected_free_A": A,
        "selected_free_A_inverse": AINV,
        "det_A": det2(A),
        "branch_swap_conjugate": pap,
        "balanced_split": {"free_outputs": [2, 3], "scalar_outputs": ["1/2", "1/2"]},
        "scalar_family": "q_delta=f(n mod 6)+delta*1_{3|n and torsion!=0}, delta>=0",
        "torsion_survivor_counts": counts,
        "composition_depth_checked": 4,
        "recoalescence_discriminator": discr,
        "ablations": abl,
        "operator_polynomial": poly,
        "theorem_enumeration_mismatches": 0,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    out = {"deterministic_digest": digest, "payload": payload}
    print(json.dumps(out, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
