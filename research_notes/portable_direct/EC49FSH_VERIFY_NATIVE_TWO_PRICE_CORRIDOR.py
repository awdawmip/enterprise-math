#!/usr/bin/env python3
"""EC49FSH: replay native BRC witnesses and re-evaluate 14 exact 2D Bellman vertices.

Usage:
 python EC49FSH_VERIFY_NATIVE_TWO_PRICE_CORRIDOR.py CERTIFICATE.json /path/to/EXTRACTED_EC49FSG_COMPLETE_NATIVE_BRC_SEVEN_PHASE_20261118

The second argument MUST contain the preserved original solver files,
EC49FRZ2_COMPLETE_BRC_TWO_PRICE_SQUARE/{code,source}, and EC49FSG_RUNS.
This script never substitutes reduced observer representatives for the original
228 physically named native observations.
"""
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

def area(poly):
    return abs(sum(x * y2 - x2 * y
                   for (x, y), (x2, y2) in zip(poly, poly[1:] + poly[:1]))) / 2

def cost(plane, alpha, z):
    return F(plane["U"]) - F(plane["Q"]) * alpha - F(plane["K"]) * z

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python EC49FSH_VERIFY_NATIVE_TWO_PRICE_CORRIDOR.py CERTIFICATE.json FSG_EVIDENCE_DIR")
    cert = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    source = Path(sys.argv[2]).resolve()
    sys.path.insert(0, str(source))
    from EC49FSA_THREE_OBSERVER_SOLVER import PIN, V, solve
    from EC49FSA_FSB_INDEPENDENT_CHECK import certify

    assert PIN == cert["frozen_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    assert len(V) == 228 and all(len(x) == 141 for x in V)
    assert len(cert["strategies"]) == len(cert["polygons"]) == 7
    assert len(cert["vertices"]) == 14
    planes = cert["strategies"]

    for p in planes:
        f = source / p["original_native_tree_file"]
        raw = f.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == p["original_tree_file_sha256"], f
        saved = json.loads(raw)
        tree = saved["tree"]
        counts = Counter()
        maxdepth = 0
        for i in range(141):
            node = tree
            visited = set()
            depth = 0
            while "named_observer" in node:
                q = node["named_observer"]
                assert q not in visited and 0 <= q < 228
                visited.add(q)
                counts[q] += 1
                depth += 1
                node = node["children"][str(V[q][i])]
            assert node == {"leaf": i}
            maxdepth = max(maxdepth, depth)
        assert sum(counts.values()) == p["U"]
        assert counts[32] == p["N32"] and counts[34] == p["N34"]
        assert counts[32] + counts[34] == p["Q"]
        assert counts[140] == p["K"]
        assert tree["named_observer"] == p["root"]
        assert maxdepth <= 3
        print("NATIVE_TREE_REPLAY", p["i"], "141/141", "depth", maxdepth, flush=True)

    for v in cert["vertices"]:
        a, z, target = F(v["alpha"]), F(v["z"]), F(v["F"])
        info, _ = solve({32: a, 34: a, 140: z})
        observed = F(info["numerator"], info["denominator"])
        alternate = certify({32: a, 34: a, 140: z})
        assert observed == F(alternate["value"]) == target
        assert target == min(cost(p, a, z) for p in planes)
        print("DUAL_EXACT_BELLMAN", v["alpha"], v["z"], v["F"],
              info["states"], alternate["states"], flush=True)

    total_area = F(0)
    for reg in cert["polygons"]:
        p = planes[reg["strategy"] - 1]
        poly = [(F(x), F(y)) for x, y in reg["vertices"]]
        a = area(poly)
        assert a == F(reg["area"]) and a > 0
        for alpha, z in poly:
            assert F(5, 16) <= alpha <= F(1, 3)
            assert 0 <= z <= 1
            assert cost(p, alpha, z) == min(cost(r, alpha, z) for r in planes)
        total_area += a
    assert total_area == F(1, 48)
    assert len({(F(v["alpha"]), F(v["z"])) for v in cert["vertices"]}) == 14
    assert all(F(v["alpha"]) in {F(5, 16), F(1, 3)} for v in cert["vertices"])
    print("EXACT_CORRIDOR_VERIFIED", "14/14 Bellman vertices",
          "7/7 full native trees", "7 convex regions", "area=1/48")

if __name__ == "__main__":
    main()
