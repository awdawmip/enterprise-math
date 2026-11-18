#!/usr/bin/env python3
"""Exact rational-interval witness certificate for N(h)=2,455,069
at the single endpoint H=2500. No floating-point arithmetic is used.
"""
from bisect import bisect_right
from fractions import Fraction
from hashlib import sha256
from time import perf_counter

def log_bounds(z, terms=45):
    term = z
    total = Fraction(0)
    for j in range(terms):
        total += 2 * term / (2*j + 1)
        term *= z*z
    remainder = 2 * term / ((2*terms + 1) * (1-z*z))
    return total, total + remainder

l2,u2 = log_bounds(Fraction(1,3))
l9,u9 = log_bounds(Fraction(1,9))
l15,u15 = log_bounds(Fraction(1,15))
ln7_lo,ln7_hi = 3*l2-u15, 3*u2-l15
ln107_lo,ln107_hi = l9+l15, u9+u15

Q = 10**26
lo = ln7_lo * Q // ln107_hi
hi = ln7_hi * Q // ln107_lo + 1
assert Fraction(lo,Q) < ln7_lo/ln107_hi
assert ln7_hi/ln107_lo < Fraction(hi,Q)
assert hi-lo == 1
print("PASS_RATIONAL_R_INTERVAL", lo, hi, Q)

H = 2500
p, q = 2074774, 380295
nstar = p + q
short_budget = 15000
assert 7**510 > 10**431
assert 10**p > 7**(p+q)
assert 7**(p+q+510) > 10**(p+431)
assert 7**(p+q-1) > 10**(p-1)

started = perf_counter()
thresholds = [(v,k) for v in range(H+1) for k in range(H-v+1)]
thresholds.sort(key=lambda vk: lo*vk[0] - Q*vk[1])
keys = [lo*v - Q*k for v,k in thresholds]
assert len(thresholds) == (H+1)*(H+2)//2 == 3128751

# Exact strict ordering of every adjacent threshold pair.
for j in range(len(thresholds)-1):
    v1,k1 = thresholds[j]
    v2,k2 = thresholds[j+1]
    dv,dk = v2-v1,k2-k1
    assert (lo if dv >= 0 else hi)*dv > Q*dk, (j,thresholds[j],thresholds[j+1])
print("PASS_ALL_ADJACENT_THRESHOLD_ORDER", len(thresholds)-1)

# The translated base-gap cells are certified adjacent and have
# explicit witnesses of length at most nstar.
index = {pair:j for j,pair in enumerate(thresholds)}
special = set()
special_hash = sha256()
shift_limit = H-510
for v0 in range(shift_limit+1):
    for k0 in range(shift_limit-v0+1):
        j = index[(v0,k0)] + 1
        assert thresholds[j] == (v0+79,k0+431), (v0,k0,thresholds[j])
        special.add(j)
        k,ell = p-k0,q-v0
        assert k >= 0 and ell >= 0 and k+ell <= nstar
        vl,kl = thresholds[j-1]
        vr,kr = thresholds[j]
        assert (k+kl)*Q > hi*(ell+vl)
        assert (k+kr)*Q < lo*(ell+vr)
        special_hash.update(f"{j},{k},{ell}\n".encode("ascii"))
expected_special = (shift_limit+1)*(shift_limit+2)//2
assert len(special) == expected_special == 1983036
print("PASS_TRANSLATED_GAP_CELLS", len(special))

# All remaining cells receive explicit prefix witnesses of length <=15000.
flags = bytearray(len(thresholds)+1)
covered = 0
target = len(flags)-len(special)
last_ell = None
short_hash = sha256()
max_short_length = 0
max_short_ell = 0
for ell in range(short_budget+1):
    last_ell = ell
    kstart = max(0, lo*ell//Q - H - 2)
    kend = min(short_budget-ell, hi*(ell+H)//Q + 2)
    if kstart > kend:
        continue
    for k in range(kstart,kend+1):
        j = bisect_right(keys, Q*k-lo*ell)
        if j in special or flags[j]:
            continue
        if j:
            vl,kl = thresholds[j-1]
            if (k+kl)*Q <= hi*(ell+vl):
                continue
        if j < len(thresholds):
            vr,kr = thresholds[j]
            if (k+kr)*Q >= lo*(ell+vr):
                continue
        flags[j] = 1
        covered += 1
        max_short_length = max(max_short_length,k+ell)
        max_short_ell = max(max_short_ell,ell)
        short_hash.update(f"{j},{k},{ell}\n".encode("ascii"))
    if covered == target:
        break

missing = {j for j,flag in enumerate(flags) if not flag}
assert missing == special, (len(missing),len(special),len(missing-special),len(special-missing))
assert covered == target == 1145716
assert last_ell == max_short_ell == 463
assert max_short_length <= short_budget
print("CERTIFIED_EXACT_N", H, "N=", nstar,
      "SPECIAL=", len(special), "OTHER_CELLS=", covered,
      "LAST_ELL=", last_ell, "MAX_SHORT_LENGTH=", max_short_length)
print("SPECIAL_WITNESS_SHA256", special_hash.hexdigest())
print("OTHER_WITNESS_SHA256", short_hash.hexdigest())
print("PASS_S23_AV_EXACT_N_H2500_ENDPOINT", round(perf_counter()-started,2), "sec")
