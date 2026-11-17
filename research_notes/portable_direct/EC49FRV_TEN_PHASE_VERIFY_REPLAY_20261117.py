#!/usr/bin/env python3
"""Verify exact original-BRC named-query discount anchors and ten tree witnesses.

This script runs inside the EC49FRV self-contained 2026-11-17 evidence archive.
It consumes previously computed *exact integer* 2-route case receipts, replays
all 141 named-state paths, and checks affine envelopes. It does not itself
run new Bellman dynamic programs; use EC49FRV_RUN_CASE.py for that.
"""
from pathlib import Path
from fractions import Fraction
import hashlib, json
from EC49FRV_DUAL_DISCOUNT_VERIFY import V, OBS, PIN, SOURCE_SHA

BASE = Path(__file__).resolve().parent
ANCHORS = ["0/1", "1/4", "1/3", "2/5", "1/2", "5/9", "3/5",
           "2/3", "3/4", "4/5", "1/1"]
EXPECTED = [296, 1032, 735, 1166, 430, 1840, 978, 545, 649, 751, 99]
TREE_CASES = ["1/5", "7/24", "11/30", "9/20", "5/9", "3/5",
              "2/3", "3/4", "4/5", "1/1"]
LINES = [(296,152), (297,156), (304,177), (306,182), (310,190),
         (315,199), (321,209), (337,233), (343,241), (355,256)]

def case_data(frac, route):
    n, d = map(int, frac.split("/"))
    name = f"ec49frv_case_{n}_{d}_route{route}.json"
    file = BASE / name
    if not file.exists():
        file = BASE / "case_data" / name
    return json.loads(file.read_text())

def replay(tree):
    counts = {}
    max_depth = 0
    for state in range(141):
        node = tree
        visited = set()
        depth = 0
        while "leaf" not in node:
            q = node["q"]
            assert 0 <= q < 228 and q not in visited
            visited.add(q)
            counts[q] = counts.get(q, 0) + 1
            depth += 1
            node = node["children"][str(V[q][state])]
        assert node["leaf"] == state
        max_depth = max(max_depth, depth)
    return (sum(counts.values()), counts.get(32,0) + counts.get(34,0),
            max_depth, counts)

def main():
    assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    assert len(V) == len(OBS) == 228 and len(V[0]) == 141
    A = []
    for c, expected in zip(ANCHORS, EXPECTED):
        first = case_data(c, 0)
        independent = case_data(c, 1)
        assert first["scaled_integer_cost"] == independent["scaled_integer_cost"] == expected
        assert first["subsets"] == independent["subsets"] == 13063
        n,d = map(int, c.split("/"))
        assert expected == min(d*u-n*z for u,z in LINES)
        A.append({"delta":c, "integer_bellman_total":expected,
                  "primary_optimal_first":first["best_first_observers"],
                  "independent_optimal_first":independent["best_first_observers"],
                  "subsets_per_route":13063})
    W = []
    for i,c in enumerate(TREE_CASES):
        first = case_data(c,0)
        w = first["tree_witness"]
        tree = w["complete_tree"]
        U,N,depth,counts = replay(tree)
        assert (U,N) == LINES[i]
        assert U == w["query_uses_total"] and N == w["discount_uses_total"]
        assert depth == w["max_depth"] <= 140
        n,d = map(int,c.split("/"))
        assert d*U-n*N == first["scaled_integer_cost"]
        W.append({"segment":i,"sample_delta":c,"total_observation_uses":U,
                  "joint_32_34_uses":N,"first_original_query":w["first_query"],
                  "max_depth":depth,"full_named_query_replay":
                  {"named_states":141,"complete":True,
                   "no_observer_repeated_on_path":True},"tree":tree})
    br = [Fraction(*map(int,c.split("/"))) for c in ANCHORS]
    assert br == sorted(br) and len(br) == 11
    for i in range(10):
        u,n = LINES[i]
        left = u-n*br[i]
        right = u-n*br[i+1]
        assert left == Fraction(A[i]["integer_bellman_total"],br[i].denominator)
        assert right == Fraction(A[i+1]["integer_bellman_total"],br[i+1].denominator)
        if i>0:
            previous = LINES[i-1]
            assert Fraction(u-previous[0],n-previous[1]) == br[i]
        mid = (br[i]+br[i+1])/2
        costs = [u0-mid*n0 for u0,n0 in LINES]
        assert costs.count(min(costs)) == 1
        assert costs.index(min(costs)) == i
    report = {"schema":"EC49FRV_EXACT_DUAL_DISCOUNT_10_CHAMBER_CERTIFICATE_V1",
              "frozen_scientific_pin":PIN,
              "model":{"class_id":16943,"original_configurations":310,
                       "complete_named_states":141,
                       "original_named_physical_observations":228,
                       "root_to_terminal_base_price_ratio":1,
                       "prior_weight_interpolation_lambda":0,
                       "only_discounted_original_named_terminal_observers":[32,34],
                       "discounted_prices":"(1-delta)t","domain":"0<=delta<=1"},
              "frozen_raw_source_sha256":SOURCE_SHA,
              "query_vector_equality":"independent 228 original named responses matched exactly",
              "bellman_anchor_checks":A, "exact_phase_breakpoints":ANCHORS,
              "exact_piecewise_coefficients":[
                    {"interval":[ANCHORS[i],ANCHORS[i+1]],"U":u,"N":n}
                    for i,(u,n) in enumerate(LINES)],
              "complete_original_named_tree_witnesses":W,
              "real_domain_proof":"Concavity of minimum of affine complete-tree costs; each witnessed line matches unrestricted integer Bellman at adjacent anchors. Chord lower bound and witness upper bound coincide throughout, with ten distinct strictly optimal slopes.",
              "unreviewed_status":"AUTHOR_PROVED / EXACT_FINITE_CHECKED / TWO_INDEPENDENT_RAW_RESPONSE_RECONSTRUCTIONS / NOT_REVIEWED"}
    out = BASE / "EC49FRV_COMPLETE_10_CHAMBER_NATIVE_CERTIFICATE_REBUILT.json"
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print("VERIFIED", len(A),"anchors",len(W),"full original trees",len(V),"observations")
    print("output:",out,"sha256",hashlib.sha256(out.read_bytes()).hexdigest())

if __name__ == "__main__":
    main()
