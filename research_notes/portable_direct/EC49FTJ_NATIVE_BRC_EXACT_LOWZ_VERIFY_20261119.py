#!/usr/bin/env python3
"""EC49FTJ: verify native 228-observer seven-phase original-index BRC certificate.

Extract the companion self-contained EC49FTJ evidence archive and run
  python EC49FTJ_NATIVE_BRC_EXACT_LOWZ_VERIFY_20261119.py --evidence-root DIR
  python EC49FTJ_NATIVE_BRC_EXACT_LOWZ_VERIFY_20261119.py --evidence-root DIR --full --start 0 --stop 8
  python EC49FTJ_NATIVE_BRC_EXACT_LOWZ_VERIFY_20261119.py --evidence-root DIR --full --start 8 --stop 16
  python EC49FTJ_NATIVE_BRC_EXACT_LOWZ_VERIFY_20261119.py --evidence-root DIR --independent
The complete frozen data, seven original-index trees and both native solvers live
in that archive. Without --full this checks exact geometry and archive witnesses,
not the unrestricted Bellman anchors; --full performs the original 228-query solve.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

def clip(poly, function):
    if not poly: return []
    result = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        f, g = function(p), function(q)
        if f <= 0: result.append(p)
        if (f < 0 < g) or (g < 0 < f):
            t = f / (f - g)
            result.append((p[0] + t * (q[0] - p[0]),
                           p[1] + t * (q[1] - p[1])))
    out = []
    for point in result:
        if not out or out[-1] != point: out.append(point)
    if len(out) > 1 and out[0] == out[-1]: out.pop()
    return out

def verify(root, full=False, independent=False, start=0, stop=16):
    sys.path.insert(0, str(root / "native_code"))
    from EC49FSA_THREE_OBSERVER_SOLVER import V, PIN
    cert = json.loads((root / "EC49FTJ_CERT.json").read_text())
    assert PIN == cert["scientific_source_pin"]
    assert len(V) == 228 and all(len(v) == 141 for v in V)
    assert len(cert["vectors"]) == 7
    assert len(cert["unrestricted_bellman_anchors"]) == 16
    for filename, sha in cert["source_sha256"].items():
        assert hashlib.sha256((root / "source" / filename).read_bytes()).hexdigest() == sha
    vectors = {key: tuple(v) for key, v in cert["vectors"].items()}
    a = F(3, 4)
    for name, usage in vectors.items():
        tree_file = root / "trees" / (name + ".json")
        assert hashlib.sha256(tree_file.read_bytes()).hexdigest() == cert["tree_sha256"][name]
        node = json.loads(tree_file.read_text())
        observed = Counter()
        for state in range(141):
            current, used = node, set()
            while "named_observer" in current:
                q = current["named_observer"]
                assert 0 <= q < 228 and q not in used
                used.add(q)
                observed[q] += 1
                current = current["children"][str(V[q][state])]
            assert current == {"leaf": state}
        assert usage == (sum(observed.values()), observed[32], observed[34], observed[140])
        print("FULL_NAMED_TREE_MATCH", name, flush=True)

    def cost(name, b, z):
        total, u32, u34, u140 = vectors[name]
        direct = name.startswith("D")
        return F(total) - a * (u32 if direct else u34) \
               - b * (u34 if direct else u32) - z * u140

    b_lo, b_hi, z_lo, z_hi = F(7, 16), F(57, 128), F(1, 4), F(3, 8)
    bounding = [(b_lo, z_lo), (b_hi, z_lo), (b_hi, z_hi), (b_lo, z_hi)]
    polygons, anchors = {}, set()
    for side in ("D", "S"):
        for name in vectors:
            if name[0] != side: continue
            polygon = bounding[:]
            for other in vectors:
                if other[0] != side or other == name: continue
                polygon = clip(polygon, lambda p: cost(name, *p) - cost(other, *p))
            assert polygon
            polygons[name] = polygon
            assert [[str(b), str(z)] for b, z in polygon] == \
                   cert["phase_polygons"][side][name]
            for b, z in polygon: anchors.add((side, b, z))

    recorded = {(row["o"], F(row["b"]), F(row["z"])): F(row["value"])
                for row in cert["unrestricted_bellman_anchors"]}
    assert len(recorded) == 16 and set(recorded) == anchors
    for (side, b, z), value in recorded.items():
        assert value == min(cost(name, b, z) for name in vectors if name[0] == side)
    print("EXACT_CONVEX_GEOMETRY_AND_RECORDED_ANCHORS", len(recorded), flush=True)

    for i, (side, b, z) in enumerate(sorted(recorded)):
        if full and start <= i < stop:
            cmd = [sys.executable, str(root / "native_code" / "EC49FSA_THREE_OBSERVER_SOLVER.py"),
                   "--a", str(a if side == "D" else b),
                   "--b", str(b if side == "D" else a),
                   "--z", str(z)]
            cp = subprocess.run(cmd, capture_output=True, text=True,
                                check=True, timeout=120)
            exact = json.loads(cp.stdout)
            assert F(exact["numerator"], exact["denominator"]) == recorded[side, b, z]
            print("UNRESTRICTED_ALL_228_BELLMAN", i, side, b, z, flush=True)

    if independent:
        from EC49FSA_FSB_INDEPENDENT_CHECK import certify
        for row in cert["independent_raw94"]:
            side, b, z = row["o"], F(row["b"]), F(row["z"])
            discounts = {32: a if side == "D" else b,
                         34: b if side == "D" else a, 140: z}
            got = F(certify(discounts)["value"])
            assert got == F(row["value"]) == recorded[side, b, z]
            print("INDEPENDENT_RAW94", side, b, z, flush=True)

    gaps = []
    for dn in polygons:
        if dn[0] != "D": continue
        for sn in polygons:
            if sn[0] != "S": continue
            polygon = bounding[:]
            for other in polygons:
                if other[0] == "D" and other != dn:
                    polygon = clip(polygon, lambda p: cost(dn, *p) - cost(other, *p))
                if other[0] == "S" and other != sn:
                    polygon = clip(polygon, lambda p: cost(sn, *p) - cost(other, *p))
            gaps.extend(cost(dn, b, z) - cost(sn, b, z) for b, z in polygon)
    assert min(gaps) == F("351/128")
    assert max(gaps) == F("87/16")
    print("EXACT_SHARP_GAP", min(gaps), max(gaps), flush=True)
    print("EC49FTJ_CERTIFICATE_CHECKED", flush=True)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--evidence-root", required=True, type=Path)
    p.add_argument("--full", action="store_true")
    p.add_argument("--independent", action="store_true")
    p.add_argument("--start", type=int, default=0)
    p.add_argument("--stop", type=int, default=16)
    args = p.parse_args()
    verify(args.evidence_root.resolve(), args.full, args.independent,
           args.start, args.stop)
