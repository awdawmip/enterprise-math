#!/usr/bin/env python3
"""R061 Stage 1R deterministic checker replay.

Reconstructs Stage 0 frozen regression hashes and Stage 1 native trace evidence
from definitions, exact integer/rational carrier arithmetic, and combinatorics.

No result artifact is read. Expected frozen/claimed digests are compared only
AFTER the corresponding data have been independently regenerated.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
import subprocess
from collections import defaultdict
from math import comb, gcd, isqrt
from pathlib import Path

TASK = "RS-R061-STAGE1R-NATIVE-LINE-TRACE-CHECKER-REPLAY"
TASKBOOK_SOURCE = "2fd179aa22db7fdc292817f24cb7f65008eb4b16"
STAGE0_HEAD = "e6657ce00382d52acda319f0108b787a03e9d5f2"
STAGE1_BRANCH = "research/r061-stage1-native-line-trace-realization"
OWNER_BRANCH = "research/r061-stage1r-native-line-checker-replay"

# These are comparison targets only. Generation code below never uses them.
FROZEN_STAGE0_TARGETS = {
    "coordinate_fiber_sha256": "0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338",
    "explicit_shuffle_sha256": "572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93",
    "compressed_pascal_sha256": "780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002",
    "explicit_shuffle_word_count": 8388607,
}
CLAIMED_STAGE1_TARGETS = {
    "native_replay_sha256": "359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702",
    "compressed_trace_sha256": "aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead",
    "pair_count": 190,
    "formal_linearization_count": 524287,
    "three_sector_native_path_count": 1572861,
}

SECTORS = ("S12", "S23", "S31")
# 3-scaled global carrier basis coordinates in (t1,t2).
BASIS3 = {
    "S12": ((3, 0), (0, 3)),          # (t1,t2)
    "S23": ((0, 3), (-3, -3)),        # (t2,t3)
    "S31": ((-3, -3), (3, 0)),        # (t3,t1)
}
# Plus-gauge unique origin-incident center in each open sector.
ANCHOR3 = {
    "S12": (1, 2),
    "S23": (-2, -1),
    "S31": (1, -1),
}
# All three incident centers in the same gauge.
INCIDENT3 = ((-2, -1), (1, -1), (1, 2))

AXIS_CHARTS = {
    "E1": (("S12", 0), ("S31", 1)),
    "E2": (("S12", 1), ("S23", 0)),
    "E3": (("S23", 1), ("S31", 0)),
}

MANDATORY_N = (0, 1, 2, 5, 25, 65, 169, 289, 625, 841, 4225)
SCALED_TRIPLES = ((6,8,10),(9,12,15),(10,24,26),(16,30,34),(40,42,58))
NONREPRESENTABLE = (3, 6, 7, 11, 12, 14, 15, 19, 21, 22, 23)

def json_dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")

def add(p, q):
    return (p[0] + q[0], p[1] + q[1])

def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])

def mul(k, p):
    return (k * p[0], k * p[1])

def q3(p):
    """Nine times squared carrier length for a 3-scaled (t1,t2) vector."""
    x, y = p
    return x*x + y*y - x*y

def is_open_sector_global3(sector: str, p) -> bool:
    x, y = p
    if sector == "S12":
        return x > 0 and y > 0
    if sector == "S23":
        return x < 0 and (y - x) > 0
    if sector == "S31":
        return y < 0 and (x - y) > 0
    raise KeyError(sector)

def vertex3(sector: str, a: int, b: int):
    u, v = BASIS3[sector]
    return add(mul(a, u), mul(b, v))

def center3(sector: str, a: int, b: int):
    return add(ANCHOR3[sector], vertex3(sector, a, b))

def typed_vaddr(sector, a, b):
    return {"kind": "VADDR", "sector": sector, "a": a, "b": b, "carrier3": list(vertex3(sector,a,b))}

def typed_caddr(sector, a, b):
    return {"kind": "CADDR", "sector": sector, "a": a, "b": b, "carrier3": list(center3(sector,a,b))}

def typed_cell(sector, a, b):
    return {"kind": "CIRCLE_CELL", "center": typed_caddr(sector,a,b)}

def typed_trace(sector, a, b):
    return {"kind": "TRACE", "sector": sector, "a": a, "b": b}

# ------------------------- Stage 0 regressions -------------------------

def coordinate_regression(limit: int = 100000):
    # Independent ordered-pair enumeration. Only representable N values receive
    # a list, avoiding a 100001-set object graph before the heavy word replay.
    maxc=isqrt(limit)
    fibers=defaultdict(list)
    for a in range(maxc+1):
        aa=a*a
        for b in range(maxc+1):
            n=aa+b*b
            if n<=limit:
                fibers[n].append((a,b))
    h=hashlib.sha256()
    for n in range(limit+1):
        sol=sorted(fibers.get(n,()))
        h.update((f"{n}:"+",".join(f"{a}.{b}" for a,b in sol)+"\n").encode())
    return {
        "N_range":[0,limit],
        "coordinate_fiber_sha256":h.hexdigest(),
    }

def euclid_solutions_for_hypotenuse(r: int):
    out = set()
    m = 2
    while m*m + 1 <= r:
        for n in range(1, m):
            hyp = m*m + n*n
            if hyp > r:
                continue
            if gcd(m,n) != 1 or (m-n) % 2 == 0 or r % hyp:
                continue
            k = r // hyp
            a = k*(m*m-n*n)
            b = 2*k*m*n
            out.add((a,b)); out.add((b,a))
        m += 1
    return out

def brute_square_nondeg(r: int):
    out=set()
    rr=r*r
    for a in range(1,r):
        b2=rr-a*a
        b=isqrt(b2)
        if b>0 and b*b==b2:
            out.add((a,b))
    return out

def euclid_regression(max_r: int = 4096):
    mismatches=[]
    for r in range(max_r+1):
        brute = brute_square_nondeg(r)
        eu = euclid_solutions_for_hypotenuse(r)
        if brute != eu:
            mismatches.append({"r":r,"brute":sorted(brute),"euclid":sorted(eu)})
            if len(mismatches) >= 10:
                break
    return {"square_hypotenuse_r_range":[0,max_r],
            "mismatch_count":len(mismatches),
            "mismatch_examples":mismatches}

def make_word(n: int, x_positions):
    pos=set(x_positions)
    return "".join("X" if i in pos else "Y" for i in range(n))

def explicit_shuffle_regression(max_total: int = 22):
    h=hashlib.sha256()
    total=0
    mismatch=[]
    for n in range(max_total+1):
        for a in range(n+1):
            b=n-a
            count=0
            previous_pos=None
            for pos in itertools.combinations(range(n),a):
                # itertools.combinations is lexicographically ordered; strict
                # increase certifies no repeated position set without retaining
                # an exponential-size seen table.
                if previous_pos is not None and not (previous_pos < pos):
                    if len(mismatch)<10:
                        mismatch.append({"n":n,"a":a,"kind":"combination_order_duplicate",
                                         "previous":previous_pos,"current":pos})
                previous_pos=pos
                w=make_word(n,pos)
                # The word/position bijection gives exact endpoint multiplicity.
                if len(pos)!=a or (n-len(pos))!=b:
                    if len(mismatch)<10:
                        mismatch.append({"n":n,"a":a,"kind":"endpoint_generation"})
                h.update(f"{a},{b}:".encode())
                h.update(w.encode()); h.update(b"\n")
                count += 1; total += 1
            if count != comb(n,a) and len(mismatch)<10:
                mismatch.append({"n":n,"a":a,"kind":"count","observed":count,"expected":comb(n,a)})
    return {"max_a_plus_b":max_total,
            "explicit_shuffle_word_count":total,
            "explicit_shuffle_sha256":h.hexdigest(),
            "mismatch_count":len(mismatch),
            "mismatch_examples":mismatch}

def pascal_regression(max_total: int = 512):
    h=hashlib.sha256()
    mismatch=[]
    previous=None
    for n in range(max_total+1):
        if n == 0:
            row=[1]
        else:
            row=[1]+[previous[k-1]+previous[k] for k in range(1,n)]+[1]
        for a,c in enumerate(row):
            target=comb(n,a)
            if c != target and len(mismatch)<10:
                mismatch.append({"n":n,"a":a,"dp":str(c),"comb":str(target)})
            h.update(f"{n},{a},{c}\n".encode())
        previous=row
    return {"max_a_plus_b":max_total,
            "compressed_pascal_sha256":h.hexdigest(),
            "mismatch_count":len(mismatch),
            "mismatch_examples":mismatch}

def run_stage0_regression():
    coord = coordinate_regression()
    eu = euclid_regression()
    sh = explicit_shuffle_regression()
    pa = pascal_regression()
    actual = {
        **coord,
        **eu,
        **sh,
        **pa,
    }
    comparisons = {
        "coordinate_hash_matches": actual["coordinate_fiber_sha256"] == FROZEN_STAGE0_TARGETS["coordinate_fiber_sha256"],
        "shuffle_hash_matches": actual["explicit_shuffle_sha256"] == FROZEN_STAGE0_TARGETS["explicit_shuffle_sha256"],
        "pascal_hash_matches": actual["compressed_pascal_sha256"] == FROZEN_STAGE0_TARGETS["compressed_pascal_sha256"],
        "shuffle_count_matches": actual["explicit_shuffle_word_count"] == FROZEN_STAGE0_TARGETS["explicit_shuffle_word_count"],
        "euclid_zero_mismatch": actual["mismatch_count"] == 0, # overwritten keys concern: fixed below
    }
    # Preserve distinct mismatch fields.
    actual["euclid_mismatch_count"] = eu["mismatch_count"]
    actual["shuffle_mismatch_count"] = sh["mismatch_count"]
    actual["pascal_mismatch_count"] = pa["mismatch_count"]
    comparisons["euclid_zero_mismatch"] = eu["mismatch_count"] == 0
    comparisons["shuffle_zero_mismatch"] = sh["mismatch_count"] == 0
    comparisons["pascal_zero_mismatch"] = pa["mismatch_count"] == 0
    return actual, comparisons

# --------------------- Exact origin incidence -------------------------

def origin_incidence_certificate():
    # The center lattice is anchor (1,2)/3 + Z*t1 + Z*t2.
    # q3=3 iff actual carrier radius squared is 1/3.
    # Exact bound: 4*q3=(2x-y)^2+3y^2 and symmetrically
    # 4*q3=(2y-x)^2+3x^2. Therefore q3<=12 implies
    # |x|,|y|<=4. Enumerating the congruence class inside [-4,4]^2
    # is exhaustive for the boundary q3=3 and for any possible shell
    # closer than the observed next shell q3=12.
    candidates=[]
    for x in range(-4,5):
        for y in range(-4,5):
            if (x-1)%3==0 and (y-2)%3==0:
                candidates.append((q3((x,y)),(x,y)))
    on_boundary=sorted(p for qv,p in candidates if qv==3)
    next_shell=min(qv for qv,_ in candidates if qv>3)

    pairwise=[]
    for i in range(len(on_boundary)):
        for j in range(i):
            pairwise.append({"i":i,"j":j,"q3":q3(sub(on_boundary[i],on_boundary[j]))})

    sector_members={s:[] for s in SECTORS}
    for p in on_boundary:
        hits=[s for s in SECTORS if is_open_sector_global3(s,p)]
        if len(hits)==1:
            sector_members[hits[0]].append(p)

    axis_hits=[p for p in on_boundary if not any(is_open_sector_global3(s,p) for s in SECTORS)]
    mirrors=[(-x,-y) for x,y in on_boundary]
    mirror_sector_counts={s:sum(is_open_sector_global3(s,p) for p in mirrors) for s in SECTORS}

    pass_flags={
        "exactly_three_incident_centers": len(on_boundary)==3,
