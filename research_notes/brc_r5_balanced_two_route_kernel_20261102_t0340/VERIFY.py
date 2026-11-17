"""R5 exact two-route provenance-compensation certificate (Fraction only).

All 64 LR deterministic policies and 4096 support-equivalent FULL policies are
checked at both ends of the declared tau interval. Affine flow interpolation
then establishes the complete real-parameter result; no floating point is used.
"""
from fractions import Fraction as F
from itertools import product

ZERO, ONE = F(0), F(1)
END = F(7, 32)
NORMAL = (14, -5, 5, 0)
FULL_WINNER = (1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1)
LR_WINNER = (1, 0, 0, 0, 1, 1)
# Terminal types Q3/P3/P4/Q4 and continuation types K/L. Each pair gives
# conditional P,Q probabilities from J for one source. No zero-probability
# natural branch is inserted: C only has Q3,K as its terminal/next-key routes.
N = {
    "Q3": (F(3, 10), F(1, 4)),
    "P3": (F(1, 10), F(1, 8)),
    "K": (F(1, 10), F(1, 8)),
    "P4": (F(1, 20), F(1, 16)),
    "Q4": (F(3, 20), F(3, 16)),
    "L": (F(3, 10), F(1, 4)),
}
C = {
    "Q3": (F(3, 5), F(1, 2)),
    "K": (F(2, 5), F(1, 2)),
}
# D = (5*N-C)/4. Missing C routes have coefficient 0 in this identity.
D = {key: tuple((5 * N[key][i] - C.get(key, (ZERO, ZERO))[i]) / 4
                for i in range(2)) for key in N}

def dot(normal, vec):
    return sum((F(a) * b for a, b in zip(normal, vec)), ZERO)

def lr_to_full(bits):
    p, rc, rd, q, k, ell = bits
    return (p, rc, rd, q, q, q, k, k, k, ell, ell, ell)

def observe(bits, tau):
    """12-bit reduced FULL policy: (p,rc,rd,qN,qC,qD,kN,kC,kD,lN,lC,lD).

    Source N combines A1/A2/B: at common keys these histories have the same
    P/Q ratio and future kernel, so a maximizing signed Bellman policy can
    choose the same deterministic action for all their copies. At K,L the
    future kernels are also source-blind. The reduced 4096 class therefore
    attains unrestricted FULL support in any fixed four-direction.
    """
    tau = F(tau)
    assert ZERO <= tau <= END
    delta = F(32, 7) * tau
    p, rc, rd, qn, qc, qd, kn, kc, kd, ln, lc, ld = map(F, bits)
    assert len(bits) == 12 and all(x in (ZERO, ONE) for x in bits)
    obs, total = [ZERO] * 4, [ZERO, ZERO]

    def key(mp, mq, ratio):
        assert mp >= ZERO and mq >= ZERO and mp == ratio * mq

    def terminal(mp, mq, answer, time):
        assert mp >= ZERO and mq >= ZERO
        total[0] += mp
        total[1] += mq
        if answer == "P":
            obs[0] += mp
        else:
            obs[1] += mq
        obs[2] += mp * time
        obs[3] += mq * time

    def at_L(mp, mq, ell):
        key(mp, mq, F(12, 5))
        terminal(mp * ell, mq * ell, "P", 4)
        terminal(mp * (1 - ell), mq * (1 - ell), "Q", 5)

    def at_K(mp, mq, k, ell):
        key(mp, mq, F(8, 5))
        terminal(mp * k, mq * k, "P", 3)
        mp *= 1 - k
        mq *= 1 - k
        terminal(mp / 4, mq / 2, "Q", 4)
        at_L(mp * F(3, 4), mq / 2, ell)

    def at_J(mp, mq, q, k, ell, kernel):
        key(mp, mq, F(2))
        terminal(mp * q, mq * q, "P", 2)
        mp *= 1 - q
        mq *= 1 - q
        for route, (a, b) in kernel.items():
            x, y = mp * a, mq * b
            if route == "K":
                at_K(x, y, k, ell)
            elif route == "L":
                at_L(x, y, ell)
            else:
                terminal(x, y, route[0], int(route[1]))

    # Initial A1+A2=(1/4,1/4) is at I=(1,1); B=(1/4,1/8) is at J.
    ap, aq = F(1, 4), F(1, 4)
    key(ap, aq, ONE)
    terminal(ap * p, aq * p, "P", 1)
    ap *= 1 - p
    aq *= 1 - p
    terminal(ap / 2, aq * F(3, 4), "Q", 2)
    at_J(ap / 2, aq / 4, qn, kn, ln, N)
    at_J(F(1, 4), F(1, 8), qn, kn, ln, N)

    # Distinct pre-J keys C=(1,3/4), D=(1,6/7), with J=(2,2).
    assert 0 <= F(2, 3) * tau < 1 and 0 <= tau / 4 < 1
    assert 0 <= F(7, 12) * delta < 1 and 0 <= delta / 4 < 1
    arrivals = (
        (F(1, 4), F(1, 3), F(3, 4), rc,
         F(2, 3) * tau, tau / 4, qc, kc, lc, C),
        (F(1, 4), F(7, 24), F(6, 7), rd,
         F(7, 12) * delta, delta / 4, qd, kd, ld, D),
    )
    for mp, mq, ratio, r, pgo, qgo, q, k, ell, kernel in arrivals:
        key(mp, mq, ratio)
        terminal(mp * r, mq * r, "Q", 1)
        mp *= 1 - r
        mq *= 1 - r
        terminal(mp * (1 - pgo), mq * (1 - qgo), "Q", 2)
        at_J(mp * pgo, mq * qgo, q, k, ell, kernel)
    assert total == [ONE, ONE], total
    return tuple(obs)


def check_kernel_and_balance():
    for k in (N, C, D):
        assert all(a > 0 and b > 0 for a, b in k.values())
        assert sum((a for a, _ in k.values()), ZERO) == ONE
        assert sum((b for _, b in k.values()), ZERO) == ONE
        for route, (a, b) in k.items():
            assert a == (F(6, 5) if route in ("Q3", "L")
                         else F(4, 5)) * b
    for route in N:
        for law in (0, 1):
            assert C.get(route, (ZERO, ZERO))[law] + 4 * D[route][law] == 5 * N[route][law]
    assert F(1, 4) * F(2, 3) == 2 * F(1, 3) / 4
    assert F(1, 4) * F(7, 12) == 2 * F(7, 24) / 4
    assert F(1, 3) / 4 == F(1, 4) * (F(7, 24) / 4) * F(32, 7)
    assert F(1, 4) * 3 + F(1, 4) == ONE  # P sources: A, B, C, D
    assert F(1, 4) + F(1, 8) + F(1, 3) + F(7, 24) == ONE


def verify():
    check_kernel_and_balance()
    lr_bits = tuple(product((0, 1), repeat=6))
    full_bits = tuple(product((0, 1), repeat=12))
    endpoints = (ZERO, END)
    examined = 0
    for tau in endpoints:
        lr = [(b, dot(NORMAL, observe(lr_to_full(b), tau))) for b in lr_bits]
        full = [(b, dot(NORMAL, observe(b, tau))) for b in full_bits]
        examined += len(lr) + len(full)
        best_lr = dot(NORMAL, observe(lr_to_full(LR_WINNER), tau))
        best_full = dot(NORMAL, observe(FULL_WINNER, tau))
        assert best_lr == max(v for _, v in lr)
        assert best_full == max(v for _, v in full)
        assert best_full - best_lr == F(31, 40) * tau
    assert examined == 8320

    v0 = observe(lr_to_full(LR_WINNER), ZERO)
    v1 = observe(lr_to_full(LR_WINNER), END)
    w0 = observe(FULL_WINNER, ZERO)
    w1 = observe(FULL_WINNER, END)
    assert v0 == w0 == (F(31,80), F(87,128), F(17,8), F(31,16))
    assert tuple((b-a)/END for a,b in zip(v0,v1)) == (
        F(11,24),-F(15,64),F(5,4),F(5,8))
    assert tuple((b-a)/END for a,b in zip(w0,w1)) == (
        F(67,120),-F(53,192),F(13,12),F(13,24))
    assert dot(NORMAL, v0) == F(8097,640)
    assert (dot(NORMAL,v1)-dot(NORMAL,v0))/END == F(2657,192)
    assert (dot(NORMAL,w1)-dot(NORMAL,w0))/END == F(14029,960)

    for tau in (F(1,100), F(1,32), F(7,64)):
        lrs = [dot(NORMAL, observe(lr_to_full(b), tau)) for b in lr_bits]
        full_w = observe(FULL_WINNER, tau)
        assert max(lrs)==F(8097,640)+F(2657,192)*tau
        assert dot(NORMAL,full_w)-max(lrs)==F(31,40)*tau
    example=observe(FULL_WINNER,F(7,64))
    assert example==(F(689,1536),F(7981,12288),F(1723,768),F(3067,1536))
    assert dot(NORMAL,example)==F(175103,12288)
    assert max(dot(NORMAL,observe(lr_to_full(b),F(7,64))) for b in lr_bits)==F(870307,61440)

    print('P_Q_SOURCE_TOTALS=1,1; THREE_SHARED_KEYS_J_K_L_AND_I_RATIO_CHECKS=PASS')
    print('DISTINCT_PRE_J_KEYS=C(1,3/4),D(1,6/7); J=(2,2)')
    print('KERNEL_COMPENSATION=C+4D=5N_FOR_EVERY_P_Q_BRANCH=PASS')
    print('ALL_NATURAL_PROBABILITIES_STRICTLY_POSITIVE_FOR_0<tau<=7/32=PASS')
    print('NORMAL=(14,-5,5,0); L1_NORM=24')
    print('FULL_REDUCED_DETERMINISTIC_VERTICES=4096; LR_DETERMINISTIC_VERTICES=64')
    print('EXACT_ENDPOINT_POLICY_OBSERVATIONS=',examined)
    print('SUPPORT_LR=(8097/640)+(2657/192)*tau')
    print('SUPPORT_FULL=(8097/640)+(14029/960)*tau')
    print('FULL_MINUS_LR=(31/40)*tau_FOR_ALL_REAL_0<=tau<=7/32')
    print('FULL_WITNESS_AT_tau=7/64=',','.join(map(str,example)))
    print('LR_MAX_AT_tau=7/64=870307/61440')
    print('GAP_AT_tau=7/64=217/2560; DIST_INFINITY_AT_LEAST=217/61440')
    print('NONENDPOINT_EXACT_REGRESSION_OBSERVATIONS=',3*65)
    print('BOUNDARY_tau=0_ACTUAL_IMAGE_EQUALITY=ANALYTIC_FLOW_AGGREGATION')
    print('STATUS=AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_ADMITTED')
    print('PASS_EXACT_R5_BALANCED_TWO_ROUTE_PROVENANCE_SEPARATION')

if __name__ == '__main__':
    verify()
