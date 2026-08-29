#!/usr/bin/env python3
import hashlib, json, math, pathlib, sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts" / "BRC_FACTOR_BLIND_BRIDGE_ENDPOINT_RECOVERY"
CORPUS = ART / "public_corpus.json"
SUMMARY = ART / "result_summary.json"

FIXED = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
POOL = [p for p in range(101,5000,2) if all(p % q for q in range(3, int(p**0.5)+1, 2))]
B_STAGES = [16,32,64,128,256,512,1024]

def adaptive_candidates(N, k=16):
    out, j = [], 0
    while len(out) < k:
        h = hashlib.sha256(f"BRC-SUPPORT-V1|{N}|{j}".encode()).digest()
        r = POOL[int.from_bytes(h[:8], "big") % len(POOL)]
        if r not in out:
            out.append(r)
        j += 1
    return out

def candidates(N):
    return FIXED + adaptive_candidates(N, 16)

def brc_matrix(r):
    # A_r=[[r,2],[(r^2-1)/2,r]]
    return (r,2,(r*r-1)//2,r)

def brc_response(N, r):
    # Accepted F3R2 witness q_{r,2}(N)=1/2*(1_{r∤N}+1_{2∤N})
    return 0.5 * ((0 if N % r == 0 else 1) + (0 if N % 2 == 0 else 1))

def endpoint(N, r):
    return math.gcd(N, 2*r)

def lcm_upto(B):
    m = 1
    for k in range(2, B+1):
        m = math.lcm(m, k)
    return m

M_STAGES = {B:lcm_upto(B) for B in B_STAGES}

def order_collision_control(N):
    for B in B_STAGES:
        x = pow(2, M_STAGES[B], N)
        d = math.gcd(x-1, N)
        if 1 < d < N:
            return True
    return False

def canonical_corpus_bytes(obj):
    return json.dumps(obj, indent=2, sort_keys=False).encode()

def main():
    corpus = json.loads(CORPUS.read_text())
    summary = json.loads(SUMMARY.read_text())

    digest = hashlib.sha256(canonical_corpus_bytes(corpus)).hexdigest()
    assert digest == summary["public_corpus_sha256"], (digest, summary["public_corpus_sha256"])

    # Exact BRC operator predicate check.
    for r in FIXED + POOL[:50]:
        a,b,c,d = brc_matrix(r)
        assert a*d-b*c == 1
        assert math.gcd(abs(a),abs(d)) == r > 1
        assert math.gcd(abs(b),abs(c)) == 2 > 1

    support_success = 0
    mismatch = 0
    failure_signatures = set()
    order_success = 0
    groups = defaultdict(lambda: {"n":0, "support_success":0, "order_control_success":0})

    for rec in corpus["records"]:
        N = int(rec["N"])
        assert N > 1 and N % 2 == 1
        rs = candidates(N)
        assert len(rs) == 40 and len(set(rs)) == 40
        responses = []
        any_hit = False
        for r in rs:
            R = brc_response(N, r)
            d = endpoint(N, r)
            response_hit = R < 1.0
            gcd_hit = 1 < d < N
            if response_hit != gcd_hit:
                mismatch += 1
            if gcd_hit:
                any_hit = True
                assert N % d == 0
            responses.append(R)
        if any_hit:
            support_success += 1
        else:
            failure_signatures.add(tuple(responses))

        order_hit = order_collision_control(N)
        order_success += int(order_hit)

        k=f"{rec['bit_band']}:{rec['class']}"
        groups[k]["n"] += 1
        groups[k]["support_success"] += int(any_hit)
        groups[k]["order_control_success"] += int(order_hit)

    assert mismatch == summary["support_response_gcd_equivalence_mismatches"] == 0
    assert support_success == summary["support_endpoint_successes"]
    assert len(failure_signatures) == summary["failure_response_unique_signatures"] == 1
    assert order_success == summary["order_collision_control_successes"]
    assert dict(groups) == summary["groups"]

    out = {
        "status":"PASS",
        "records":len(corpus["records"]),
        "support_equivalence_mismatches":mismatch,
        "support_endpoint_successes":support_success,
        "failure_response_unique_signatures":len(failure_signatures),
        "order_collision_control_successes":order_success,
    }
    print(json.dumps(out, sort_keys=True))

if __name__ == "__main__":
    main()
