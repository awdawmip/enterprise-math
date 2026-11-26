"""Exact checks for the BRC integration assessment's small explanatory examples.

These are finite examples and do not certify any complete Cogentic headline
theorem, general BRC algorithm, or Foundation promotion.
"""
from fractions import Fraction as F
import json

plus = [(2, 1, 0), (1, 0, 2), (0, 2, 1)]
minus = [(2, 0, 1), (1, 2, 0), (0, 1, 2)]
push = lambda u: 2 * u[1] + 3 * u[2]
hp = sorted(map(push, plus)) + [9]
hm = sorted(map(push, minus)) + [9]
moment = lambda values, m: sum(F(x) ** m for x in values)
mp = [moment(hp, m) for m in range(4)]
mm = [moment(hm, m) for m in range(4)]
assert hp == [2, 6, 7, 9] and hm == [3, 4, 8, 9]
assert mp[:3] == mm[:3] == [4, 24, 170]
assert (mp[3], mm[3]) == (1296, 1332)
assert max(hp) == max(hm) == 9
assert hp.count(9) == hm.count(9) == 1
wp, wm = [[F(x, 100) for x in h] for h in (hp, hm)]
assert sum(wp) == sum(wm) == F(6, 25) < 1

prior = {"a": F(1, 2), "b": F(1, 3), "c": F(1, 6)}
target = {"a": 0, "b": 0, "c": 1}
observers = {
    "is_a": {"a": 1, "b": 0, "c": 0},
    "is_c": {"a": 0, "b": 0, "c": 1},
}
assert sum(prior.values()) == 1 and all(p > 0 for p in prior.values())
selection = {}
for name, obs in observers.items():
    separated = sum(prior[x] * prior[y] for x in prior for y in prior if obs[x] != obs[y])
    residual = max(abs(target[x] - target[y]) for x in prior for y in prior if obs[x] == obs[y])
    masses = [sum(prior[x] for x in prior if obs[x] == b) for b in (0, 1)]
    selection[name] = {"separation_probability": str(separated), "worst_target_residual": residual,
                       "signature_masses": list(map(str, masses)), "cost": 1}
assert selection["is_a"]["separation_probability"] == "1/2"
assert selection["is_c"]["separation_probability"] == "5/18"
assert selection["is_a"]["worst_target_residual"] == 1
assert selection["is_c"]["worst_target_residual"] == 0
# Balanced binary entropy is uniquely maximal; no floating comparison is needed.
assert selection["is_a"]["signature_masses"] == ["1/2", "1/2"]
assert selection["is_c"]["signature_masses"] == ["5/6", "1/6"]

report = {
    "scope": "finite exact explanatory examples only",
    "histogram_pair": {"plus": hp, "minus": hm, "moments_0_through_3_plus": list(map(str, mp)),
                       "moments_0_through_3_minus": list(map(str, mm)),
                       "CWM": [4, 24, 9], "Lead": [9, 1],
                       "scaled_one_state_total_mass": str(sum(wp)),
                       "scaled_third_moments": [str(moment(wp, 3)), str(moment(wm, 3))],
                       "stable_potential": 1},
    "full_support_observer_counterexample": {"prior": {k: str(v) for k, v in prior.items()},
                                            "target": target, "comparisons": selection},
}
print(json.dumps(report, indent=2, ensure_ascii=False))
