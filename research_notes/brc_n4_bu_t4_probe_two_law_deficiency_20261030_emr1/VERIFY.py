"""Exact 16-leaf BRC N=4 BU fourth-time probe obstruction.

External model only; no P000 native embedding, no original minmax re-proof.
Python 3, standard library Fraction only.
"""
from fractions import Fraction as F
from collections import defaultdict

ORIGINS = {
    "AU": (F(1, 6), (F(9, 10), F(11, 10))),
    "AV": (F(1, 3), (F(1, 4), F(1, 4))),
    "BU": (F(1, 4), (F(1, 5), F(9, 5))),
    "BV": (F(1, 4), (F(2), F(2))),
}


def leaves():
    for origin, (q_source, multipliers) in ORIGINS.items():
        for j, lr in enumerate(multipliers):
            for k in (0, 1):
                q = q_source / 4
                p = q * lr
                yield (origin, j, k, p, q)


def tv(dist1, dist2):
    return sum((abs(dist1[x] - dist2[x]) for x in dist1.keys() | dist2.keys()), F()) / 2


def exact_law_observations():
    # Legitimate S23: A=B=c=1, U=V=0. AU and BU reach T=3;
    # AV and BV stop at T=2. AU decides P, BU Q; all stage-3
    # decisions are current LR measurable because LR sets are disjoint.
    coarse = {"P": defaultdict(F), "Q": defaultdict(F)}
    fine = {"P": defaultdict(F), "Q": defaultdict(F)}
    for origin, j, k, p, q in leaves():
        key = ((3, "P", 0, 1) if origin == "AU" else
               (3, "Q", 1, 0) if origin == "BU" else
               (2, "Q", 0, 0))
        # Delayed external readout at time 4 of the actual fourth leaf;
        # 1 exactly on BU, second stage-3 child, second stage-4 child.
        h4 = int(origin == "BU" and j == 1 and k == 1)
        for label, mass in (("P", p), ("Q", q)):
            coarse[label][key] += mass
            fine[label][(key, h4)] += mass
    return coarse, fine


def decoder(coarse_law, theta):
    result = defaultdict(F)
    for key, mass in coarse_law.items():
        if key == (3, "Q", 1, 0):
            result[(key, 1)] += mass * theta
            result[(key, 0)] += mass * (1 - theta)
        else:
            result[(key, 0)] += mass
    return result


lv = list(leaves())
assert len(lv) == 16
assert all(p > 0 and q > 0 for _, _, _, p, q in lv)
assert sum((p for _, _, _, p, q in lv), F()) == 1
assert sum((q for _, _, _, p, q in lv), F()) == 1

coarse, fine = exact_law_observations()
for law in ("P", "Q"):
    assert sum(coarse[law].values(), F()) == 1
    assert sum(fine[law].values(), F()) == 1

BU = (3, "Q", 1, 0)
AU = (3, "P", 0, 1)
STOP = (2, "Q", 0, 0)
expected_coarse = {STOP: F(7, 12), AU: F(1, 6), BU: F(1, 4)}
assert dict(coarse["P"]) == expected_coarse
assert dict(coarse["Q"]) == expected_coarse
assert fine["P"][(BU, 1)] == F(9, 80)
assert fine["Q"][(BU, 1)] == F(1, 16)
assert fine["P"][(BU, 0)] == F(11, 80)
assert fine["Q"][(BU, 0)] == F(3, 16)
assert tv(coarse["P"], coarse["Q"]) == 0
assert tv(fine["P"], fine["Q"]) == F(1, 20)

# Any common decoder on the BU fiber must assign a single theta.
# Sharp lower bound by triangle inequality; midpoint attains.
theta = F(7, 20)
assert theta == (F(9, 20) + F(1, 4)) / 2
err_p = tv(fine["P"], decoder(coarse["P"], theta))
err_q = tv(fine["Q"], decoder(coarse["Q"], theta))
assert err_p == err_q == F(1, 40)
assert F(1, 40) == F(1, 4) * (F(9, 20) - F(1, 4)) / 2

# Connection to the exact old-observer minimizer (NOT a new minimax claim):
B, c = F(69, 500), F(1039, 1207)
m = B * c / 4
assert m == F(71691, 2414000)
sharp_conditional_radius = abs(F(9, 20) - F(1, 4)) / 2
assert sharp_conditional_radius == F(1, 10)
assert m * sharp_conditional_radius == F(71691, 24140000)

print("LEAVES=16 P_NORMALIZED=1 Q_NORMALIZED=1 STRICT_POSITIVE=True")
print("COARSE_P=COARSE_Q=", {str(k):str(v) for k,v in expected_coarse.items()})
print("Q_BU_R1=1/16 P_BU_R1=9/80")
print("TV_PQ_COARSE=0 TV_PQ_T4_REFINED=1/20")
print("BEST_COMMON_DECODER_THETA=7/20")
print("TV_P_DECODER=1/40 TV_Q_DECODER=1/40")
print("OLD_OPTIMUM_STRATEGY_BU_MASS=",m)
print("OLD_OPTIMUM_STRATEGY_T4_DECODER_LOWER_BOUND=",m/10)
print("PASS_EXACT_BRC_N4_BU_T4_PROBE_TWO_LAW_DEFICIENCY")
