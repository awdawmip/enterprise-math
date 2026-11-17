#!/usr/bin/env python3
"""EC49FSD exact native BRC q32=q34=1/2, q140=1-z phase finder.
Run inside the extracted EC49FSA_FSB_FSC_COMPLETE_AND_PARTIAL_EVIDENCE directory.
Uses the inherited frozen native source and saved EC49FSC Bellman anchors.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from EC49FSA_THREE_OBSERVER_SOLVER import solve, V

BASE = Path(__file__).resolve().parent
OLD = BASE / "ec49fsc_runs_PARTIAL"
OUT = BASE / "ec49fsd_runs"
OUT.mkdir(exist_ok=True)
checked = {}
lines = {}

def check_tree(tree, info, z):
    counts = Counter()
    worst = 0
    for i in range(141):
        node, seen, depth = tree, set(), 0
        while "named_observer" in node:
            q = node["named_observer"]
            assert q not in seen
            seen.add(q)
            counts[q] += 1
            depth += 1
            node = node["children"][str(V[q][i])]
        assert node["leaf"] == i
        worst = max(worst, depth)
    U = sum(counts.values())
    assert U == info["U"]
    for q in [32, 34, 140, 142]:
        assert counts[q] == info["uses"][str(q)]
    A = F(2 * U - counts[32] - counts[34], 2)
    K = counts[140]
    assert A - z * K == F(info["numerator"], info["denominator"])
    return (A, K), {"U": U, "N32": counts[32], "N34": counts[34],
                    "N140": K, "worst_depth": worst,
                    "root": info["root"]}

def value(line, z):
    return line[0] - z * line[1]

for file in sorted(OLD.glob("anchor_*.json")):
    record = json.loads(file.read_text())
    name = file.stem.split("_")
    z = F(int(name[1]), int(name[2]))
    line, stats = check_tree(record["tree"], record["info"], z)
    checked[z] = (value(line, z), line, file.relative_to(BASE).as_posix(), stats)
    lines.setdefault(line, file.relative_to(BASE).as_posix())

def oracle(z):
    if z in checked:
        return checked[z]
    info, tree = solve({32: F(1, 2), 34: F(1, 2), 140: z})
    line, stats = check_tree(tree, info, z)
    file = OUT / f"anchor_{z.numerator}_{z.denominator}.json"
    file.write_text(json.dumps({"info": info, "tree": tree}, separators=(",", ":")) + "\n")
    r = (value(line, z), line, file.relative_to(BASE).as_posix(), stats)
    checked[z] = r
    lines.setdefault(line, file.relative_to(BASE).as_posix())
    print("ORACLE", str(z), str(r[0]), [str(line[0]), line[1]], flush=True)
    return r

def corners():
    candidate = {F(0), F(1)}
    ls = list(lines)
    for i, (A, K) in enumerate(ls):
        for B, L in ls[i+1:]:
            if K != L:
                z = (A-B)/(K-L)
                if 0 < z < 1:
                    candidate.add(z)
    pts = sorted(candidate)
    lower = lambda z: min(value(l, z) for l in ls)
    chosen = [pts[0]]
    for i in range(1, len(pts)-1):
        z = pts[i]
        left, right = (pts[i-1]+z)/2, (z+pts[i+1])/2
        slope_left = {l[1] for l in ls if value(l, left) == lower(left)}
        slope_right = {l[1] for l in ls if value(l, right) == lower(right)}
        if slope_left != slope_right:
            chosen.append(z)
    return chosen + [pts[-1]]

for round_number in range(25):
    current = corners()
    refined = False
    for z in current:
        upper = min(value(line, z) for line in lines)
        exact = oracle(z)[0]
        assert exact <= upper
        if exact < upper:
            refined = True
            print("REFINED", z, upper, exact, flush=True)
    if not refined:
        break
else:
    raise RuntimeError("Phase discovery failed to stabilize")

corn = corners()
phases = []
for lo, hi in zip(corn, corn[1:]):
    mid = (lo+hi)/2
    best = min(value(l, mid) for l in lines)
    line = next(l for l in lines if value(l, mid) == best)
    assert oracle(lo)[0] == value(line, lo)
    assert oracle(hi)[0] == value(line, hi)
    phases.append({"range": [str(lo), str(hi)],
                   "A": str(line[0]), "K": line[1],
                   "witness": lines[line]})
certificate = {
    "schema": "EC49FSD_EIGHT_PHASE_FULL_REAL_INTERVAL_V1",
    "scientific_pin": "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    "native_profiles": 141, "named_observers": 228,
    "model": "q32=q34=1/2; q140=1-z; others=1; z in [0,1]",
    "phases": phases,
    "endpoints": [{"z": str(z), "global_optimum": str(oracle(z)[0])}
                  for z in corn],
    "checked_points": len(checked),
    "method": "exact finite Bellman endpoint lower bounds + complete native-tree affine witnesses + concavity"
}
(OUT / "CERTIFICATE.json").write_text(json.dumps(certificate, indent=2) + "\n")
print("SUCCESS", len(phases), "phases", len(checked), "checked anchors", flush=True)
