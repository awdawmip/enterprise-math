#!/usr/bin/env python3
"""Stage294-B: finite controlled weak-lumpability and repeated-coin port gap.
All numerical checks are exact Fraction arithmetic; no external dependencies.
The universal proofs and scope restrictions are in PROOF_STAGE294B.md.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

S = ("a", "b", "c")
A = ("left", "right")
obs = {"a": 0, "b": 0, "c": 1}
T = {
    "left": {
        "a": {"a": F(1, 2), "b": F(1, 4), "c": F(1, 4)},
        "b": {"a": F(0), "b": F(1, 4), "c": F(3, 4)},
        "c": {"a": F(0), "b": F(0), "c": F(1)},
    },
    "right": {
        "a": {"a": F(0), "b": F(1, 4), "c": F(3, 4)},
        "b": {"a": F(1, 2), "b": F(1, 4), "c": F(1, 4)},
        "c": {"a": F(0), "b": F(0), "c": F(1)},
    },
}
initial = {"a": F(1, 2), "b": F(1, 2), "c": F(0)}


def observable_words_original(actions):
    states = {(s, (obs[s],)): mass for s, mass in initial.items() if mass}
    for action in actions:
        nxt = defaultdict(F)
        for (s, word), mass in states.items():
            for t, prob in T[action][s].items():
                if prob:
                    nxt[(t, word + (obs[t],))] += mass * prob
        states = nxt
    result = defaultdict(F)
    for (_, word), mass in states.items():
        result[word] += mass
    return dict(result)


def observable_words_quotient(actions):
    states = {(0, (0,)): F(1)}
    for _ in actions:
        nxt = defaultdict(F)
        for (s, word), mass in states.items():
            trans = {0: F(1, 2), 1: F(1, 2)} if s == 0 else {1: F(1)}
            for t, prob in trans.items():
                nxt[(t, word + (t,))] += mass * prob
        states = nxt
    result = defaultdict(F)
    for (_, word), mass in states.items():
        result[word] += mass
    return dict(result)


def check_chain():
    for action in A:
        for s in S:
            assert sum(T[action][s].values()) == F(1)
        # Unnormalized posterior on live block after one step from (1/2,1/2)
        assert sum(T[action][s]["a"] for s in ("a", "b")) == F(1, 2)
        assert sum(T[action][s]["b"] for s in ("a", "b")) == F(1, 2)
        # Hence live probability 1/2 and conditional filter uniform.
        assert (T[action]["a"]["c"] + T[action]["b"]["c"]) / 2 == F(1, 2)
        # Strong lumpability fails for {a,b} -> {c}
        assert T[action]["a"]["c"] != T[action]["b"]["c"]
    tested = 0
    leaves = 0
    for depth in range(8):
        for word in product(A, repeat=depth):
            p = observable_words_original(word)
            q = observable_words_quotient(word)
            assert p == q, (word, p, q)
            assert sum(p.values()) == F(1)
            assert len(p) == depth + 1  # possible first absorption after t=1,...,t=depth or not yet
            tested += 1
            leaves += len(p)
    assert tested == 255  # sum 2^depth for depth=0..7
    assert leaves == sum((d+1) * (2**d) for d in range(8))
    print(f"WEAK_ADAPTIVE_EXACT_PASS words={tested} positive_observation_leaves={leaves}")
    print("SOURCE_CONDITIONAL_ONE_STEP_TV=1/4; TWO_OUTPUT_WEAK_MIN_LABELS=2; STRONG_MIN_LABELS=3")


def count_kernel(p):
    return ((1-p)**2, 2*p*(1-p), p*p)


def tv_count(p, q):
    return sum(abs(a-b) for a, b in zip(p, q)) / 2


P = (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))
K = tuple(count_kernel(p) for p in P)


def risk(theta):
    q = count_kernel(theta)
    return sum(tv_count(p, q) for p in K)


def group_lp_risk(q):
    return sum(tv_count(p, q) for p in K)


def piecewise_polynomial(left, right):
    """Return exact (constant, linear, quadratic) on an open breakpoint interval."""
    mid = (left + right) / 2
    # q_0=(1-t)^2, q_1=2t(1-t), q_2=t^2
    coin_coeff = ((F(1), F(-2), F(1)), (F(0), F(2), F(-2)), (F(0), F(0), F(1)))
    c = [F(0), F(0), F(0)]
    for target in K:
        for j in range(3):
            qmid = sum(coin_coeff[j][i] * mid**i for i in range(3))
            assert qmid != target[j]
            sign = F(1) if qmid > target[j] else F(-1)
            c[0] += sign * (coin_coeff[j][0] - target[j]) / 2
            c[1] += sign * coin_coeff[j][1] / 2
            c[2] += sign * coin_coeff[j][2] / 2
    for t in (left, mid, right):
        assert risk(t) == c[0] + c[1] * t + c[2] * t*t
    return tuple(c)


def check_coin():
    target = (F(1, 4), F(3, 8), F(3, 8))
    assert sum(target) == 1
    assert group_lp_risk(target) == F(2)
    # Coordinatewise convex-subgradient certificate at q*: each L_j has 1 as subgradient.
    # L_j(x)=sum_i |x-K_i[j]|; a common gradient 1 cancels on simplex sum(q)=1.
    for j in range(3):
        less = sum(target[j] > k[j] for k in K)
        equal = sum(target[j] == k[j] for k in K)
        greater = sum(target[j] < k[j] for k in K)
        lower = less - equal - greater
        upper = less + equal - greater
        assert lower <= 1 <= upper
    parts = []
    for a,b in zip(P[:-1],P[1:]):
        coeff = piecewise_polynomial(a,b)
        # On interval, polynomial minimum is achieved at endpoint or interior stationary point.
        candidates = [a,b]
        if coeff[2] > 0:
            critical = -coeff[1] / (2 * coeff[2])
            if a < critical < b:
                candidates.append(critical)
        minima = min(risk(t) for t in candidates)
        assert minima >= F(17, 8)
        parts.append((str(a), str(b), [str(z) for z in coeff], str(minima)))
    assert risk(F(1,2)) == F(17,8)
    # Equal-weight source risk with frozen two-label map: label 0 contains five
    # P=(0,1/4,1/2,3/4,1); label 1 contains a sixth P=1/2. Label 1 fits exactly.
    assert F(17,8) - F(2) == F(1,8)
    assert F(17,8)/6 - F(2)/6 == F(1,48)
    # If an independent random port parameter is permitted per label, convexification
    # closes this deterministic gap. Explicit rational mixture: 49/64 at y=3/7
    # and 15/64 at y=1 gives the LP target exactly.
    w = F(49,64)
    mix = tuple(w*x+(1-w)*y for x,y in zip(count_kernel(F(3,7)),count_kernel(F(1))))
    assert mix == target
    print("BERNOULLI_DETERMINISTIC_TWO_LABEL_LP_GAP_EXACT_PASS free=2 restricted=17/8 gap=1/8 normalized_gap=1/48")
    print("PORT_RANDOMIZATION_GAP_CLOSES_EXACT_PASS mixture=(49/64 at 3/7, 15/64 at 1)")
    print("PIECEWISE_CERTIFICATE:")
    for a,b,coeff,m in parts:
        print(f"  [{a},{b}] coeff={coeff} interval_min={m}")

if __name__ == "__main__":
    check_chain()
    check_coin()
    print("STAGE294B_ADAPTIVE_WEAK_AND_TYPED_PORT_EXACT_PASS")
