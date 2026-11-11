#!/usr/bin/env python3
"""R5: exact three-atom race and 18 exceptional prefixes at phase 607.

All 15 labeled atoms, 28 masses and scientific fractions are inherited
unchanged from the frozen parent R5 scripts. Python standard library only.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import contextlib
import io
import runpy

parent = (Path(__file__).resolve().parents[1] /
          "brc_r5_order_universality_threshold_20261111" /
          "VERIFY_ORDER_THRESHOLD.py")
with contextlib.redirect_stdout(io.StringIO()):
    p = runpy.run_path(str(parent))

phase, thresholds = p["phase"], p["thresholds"]
steps = p["steps"]
labels = [(j,i) for j,i,a,v in steps]
V = p["V"]
X = p["X"]
M = p["M"]
eps_max = p["eps_max"]
T = p["T"]
base = p["base"]
states = p["states"]
assert T == 32768 and len(phase) == 1145 and len(labels) == 15

critical = F(155682221, 377131868400000000)
assert eps_max*phase[606] == critical
assert eps_max*phase[605] < critical < eps_max*phase[607]
coord1 = V.index((1,3))
coord0 = V.index((0,3))
assert X[coord1] == X[coord0] == 15*critical
assert [m[coord1] for m in M if m[coord1]] == [-12,-3,15]

rank = [len(phase)+1]*T
for index,q in enumerate(phase,1):
    for mask,coord in thresholds[q]:
        assert rank[mask] == len(phase)+1
        rank[mask] = index
new = thresholds[phase[606]]
assert len(new) == 4114
assert Counter(V[coord] for mask,coord in new) == {
    (1,3):4096, (0,3):18
}

pair = (1<<labels.index((1,1))) | (1<<labels.index((2,1)))
relief = 1<<labels.index((5,1))
def race(mask):
    return (mask & pair) == pair and not (mask & relief)
assert sum(race(mask) for mask in range(T)) == 4096
assert all(rank[mask] == 607 for mask in range(T) if race(mask))
extras = sorted(mask for mask,coord in new if V[coord] == (0,3))
assert extras == [
    3152,3976,7380,7470,10800,11283,11608,15028,15511,
    15836,19640,19652,23581,24382,27300,27783,28108,30977
]
assert all(not race(mask) for mask in extras)

# Verify that each newly failing subset has exactly one zero mass.
for mask,coord in new:
    qs = [k for k in range(28)
          if base[k]*phase[606].denominator +
             (states[mask][k]-base[k])*phase[606].numerator == 0]
    assert qs == [coord]

def count(mode):
    # mode=0: old cut <=606; 1: additionally exclude three-atom race;
    # mode=2: additionally exclude the 18 target-0 exceptions.
    w = [0]*T
    w[0] = 1
    for mask in range(1,T):
        if rank[mask] <= 606: continue
        if mode >= 1 and race(mask): continue
        if mode >= 2 and rank[mask] <= 607: continue
        z = mask
        while z:
            bit = z & -z
            w[mask] += w[mask^bit]
            z ^= bit
    return w[-1]

before,filtered,after = count(0),count(1),count(2)
assert (before,filtered,after) == (
    851207682192,471427082208,470447833008)
assert (before-filtered,filtered-after,before-after) == (
    379780599984,979249200,380759849184)

# Independent exact direct coordinate tests, without consulting rank[].
def direct(q):
    w=[0]*T
    w[0]=1
    for mask in range(1,T):
        if all(base[k]*q.denominator +
               (states[mask][k]-base[k])*q.numerator >= 0
               for k in range(28)):
            z=mask
            while z:
                bit=z&-z
                w[mask]+=w[mask^bit]
                z^=bit
    return w[-1]
assert direct((phase[605]+phase[606])/2) == before
assert direct((phase[606]+phase[607])/2) == after

print("PHASE_INDEX",607)
print("PHASE_EPSILON",critical)
print("NEW_INFEASIBLE_PREFIX_MASKS",len(new))
print("SOURCE3_TARGET1_RACE_MASKS",4096)
print("SOURCE3_TARGET0_EXTRA_MASKS",len(extras))
print("SOURCE3_TARGET0_EXTRA_MASK_IDS",",".join(map(str,extras)))
print("PRE_PHASE_LEGAL_ORDERS",before)
print("PAIR_RACE_ONLY_FILTERED_ORDERS",filtered)
print("AFTER_PHASE_LEGAL_ORDERS",after)
print("RACE_ATTRIBUTED_ORDER_DROP",before-filtered)
print("ADDITIONAL_TARGET0_ORDER_DROP",filtered-after)
print("TOTAL_ORDER_DROP",before-after)
print("DIRECT_EXACT_CHECK_BOTH_SIDES",True)
print("PASS_R5_PHASE607_RESOURCE_RACE_AND_18_EXCEPTIONS")
