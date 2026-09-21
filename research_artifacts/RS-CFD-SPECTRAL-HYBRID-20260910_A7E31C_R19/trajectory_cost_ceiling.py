#!/usr/bin/env python3
from fractions import Fraction as F
import json


def w_upper(k:int,n:int,rho:F)->F:
    assert 0 <= k <= n and rho >= 1
    if k == 0:
        return F(0)
    if k == n:
        return F(1)
    return F(k) * rho / (F(k) * rho + (n-k))


def w_lower(k:int,n:int,rho:F)->F:
    assert 0 <= k <= n and rho >= 1
    if k == 0:
        return F(0)
    if k == n:
        return F(1)
    return F(k) / (F(k) + (n-k) * rho)


def speed_ceiling(k:int,n:int,rho:F,alpha_bar:F,f_bar:F,h_floor:F)->F:
    assert F(0) <= alpha_bar <= 1
    assert F(0) <= f_bar <= 1
    assert h_floor >= 0
    denom = F(1) - alpha_bar * f_bar * w_upper(k,n,rho) + h_floor
    assert denom > 0
    return F(1) / denom


def target_tau(q:F,alpha_bar:F,f_bar:F,h_floor:F)->F:
    assert q > 1 and alpha_bar > 0 and f_bar > 0 and h_floor >= 0
    return (F(1) - F(1)/q + h_floor) / (alpha_bar * f_bar)


def rho_min_for_target(k:int,n:int,q:F,alpha_bar:F,f_bar:F,h_floor:F):
    assert 0 < k < n
    tau = target_tau(q,alpha_bar,f_bar,h_floor)
    if tau >= 1:
        return None
    raw = tau * (n-k) / (F(k) * (F(1)-tau))
    return max(F(1), raw)

# R18 envelope identities and extremal attainability on a finite exact grid.
for n in range(2,8):
    for k in range(1,n):
        for rho_i in range(1,5):
            rho = F(rho_i)
            lo = w_lower(k,n,rho)
            hi = w_upper(k,n,rho)
            lower_constructed = F(k, k + (n-k)*rho_i)
            upper_constructed = F(k*rho_i, k*rho_i + n-k)
            assert lo == lower_constructed
            assert hi == upper_constructed
            assert lo <= F(k,n) <= hi

alpha = F(7,10)
fbar = F(4,5)
hfloor = F(1,50)
q = F(11,10)

# Frozen R10 route-count illustrations, rho=2.
assert w_upper(2,20,F(2)) == F(2,11)
assert w_upper(1,20,F(2)) == F(2,21)
assert speed_ceiling(2,20,F(2),alpha,fbar,hfloor) == F(110,101)
assert speed_ceiling(1,20,F(2),alpha,fbar,hfloor) == F(30,29)

# Exact target inversion.
tau = target_tau(q,alpha,fbar,hfloor)
assert tau == F(61,308)
rho2 = rho_min_for_target(2,20,q,alpha,fbar,hfloor)
rho1 = rho_min_for_target(1,20,q,alpha,fbar,hfloor)
assert rho2 == F(549,247)
assert rho1 == F(61,13)
assert speed_ceiling(2,20,rho2,alpha,fbar,hfloor) == q
assert speed_ceiling(1,20,rho1,alpha,fbar,hfloor) == q

# Monotonicity in rho for the frozen routes.
for k in (1,2):
    vals = [speed_ceiling(k,20,F(r),alpha,fbar,hfloor) for r in (1,2,3,5,10)]
    assert vals == sorted(vals)

# Fail-closed impossibility when the target requires all (or more than all)
# baseline work to be sparsely removable under finite rho and k<n.
assert target_tau(F(2), F(1,10), F(1,2), F(0)) > 1
assert rho_min_for_target(2,20,F(2),F(1,10),F(1,2),F(0)) is None

out = {
    "schema":"ENTERPRISE_MATH_CFD_TRAJECTORY_COST_CEILING_R19_V1",
    "assumptions":{
        "n_calls":20,
        "dense_cost_heterogeneity_rho_example":"2",
        "sparse_fractional_saving_upper_alpha":"7/10",
        "dense_nonlinear_baseline_fraction_upper_f":"4/5",
        "additive_hybrid_overhead_fraction_lower_h":"1/50",
        "target_speedup":"11/10"
    },
    "k2":{
        "w_sparse_upper":"2/11",
        "speedup_ceiling":"110/101",
        "rho_min_for_1.10x":"549/247"
    },
    "k1":{
        "w_sparse_upper":"2/21",
        "speedup_ceiling":"30/29",
        "rho_min_for_1.10x":"61/13"
    },
    "target_tau":"61/308",
    "status":"PASS_EXACT_FRACTION_ASSERTIONS"
}
print(json.dumps(out, indent=2, sort_keys=True))
