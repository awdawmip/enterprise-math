#!/usr/bin/env python3
"""Exact n=11 certificate for the frozen Q22/Q25 return-profile 1-WL observable.

Discovery is deterministic but nonauthoritative. Completeness is the equality
between (i) independent exact connected degree-sector counts and (ii) the
disjoint orbit-stabilizer sum of one representative per distinct full packet.
A missing isomorphism class, including a second class in an existing packet
fiber, would leave a positive orbit deficit, so equality proves injectivity.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Q25_PATH = ROOT / "research_checks" / "P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_FIRST_COLLISION_FRONTIER_CHECK_20260901.py"
SPEC = importlib.util.spec_from_file_location("p000_q25_frozen_checker", Q25_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen Q25 checker")
Q25 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(Q25)

TASK = "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER"
PUB = "TP2-875D6C62E617BCC7CE63"
CLAIM = "chatgpt-pq27-20260902-0923-6f3a9c"
MASK = (1 << 64) - 1
BASE = 0x20260902
MIX = 0xD1B54A32D192ED03
TARGET = {2:5050080,4:11476080,6:27213300,8:69824160,10:194934600}
REPS = {2:23,4:197,6:536,8:482,10:114}
CLOSE = {2:179,4:1852,6:13207,8:10701,10:1707}
PACKET_SHA = {
    2:"08d08ab8ce8ce8237ecada9ea9ec76c7a6c87a4bf06ef455c61aafb28cdc8738",
    4:"0527cbbeb5474498b2252d9e417dba49fa020ef0a9f6d39d2a26631c2f11cd71",
    6:"fd60fdc131487e40f0a40e26ef9e63fd5d7a0c6d2b2e01763c2fa4189055852d",
    8:"e94a4220802e9b99b446a619dd203194b0fb7007b47980559649313d68e1315c",
    10:"e84ca3046ab07862854cdb783e8ee0ac6d54eed061f53a2c28f03d5adc1f3fa0",
}
TOTAL_REPS = 1352
TOTAL_CONNECTED = 308498220
COMBINED_SHA = "195df8a4567cec68de826035eee044c9915b3dafb207f260324a04e29a3535d2"

def check(ok, msg):
    if not ok:
        raise AssertionError(msg)

class SplitMix64:
    def __init__(self, seed):
        self.state = seed & MASK
    def next64(self):
        self.state = (self.state + 0x9E3779B97F4A7C15) & MASK
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK
        return (z ^ (z >> 31)) & MASK
    def shuffle(self, a):
        for i in range(len(a)-1, 0, -1):
            j = self.next64() % (i+1)
            a[i], a[j] = a[j], a[i]

def discovery_graph(r, rng):
    degrees = [3]*r + [2]*(11-r)
    for _ in range(100):
        stubs = [v for v,d in enumerate(degrees) for _ in range(d)]
        rng.shuffle(stubs)
        adj = [0]*11
        ok = True
        for i in range(0, len(stubs), 2):
            a,b = stubs[i],stubs[i+1]
            if a == b or ((adj[a] >> b) & 1):
                ok = False
                break
            adj[a] |= 1 << b
            adj[b] |= 1 << a
        if ok and Q25.connected(tuple(adj)):
            return tuple(adj)
    return None

def sector(r):
    rng = SplitMix64(BASE ^ ((r*MIX) & MASK))
    factor = math.factorial(r) * math.factorial(11-r)
    seen = {}
    orbit_sum = 0
    closure = None
    for sample in range(1, 20001):
        adj = discovery_graph(r, rng)
        if adj is None:
            continue
        check(Counter(x.bit_count() for x in adj) == Counter({3:r,2:11-r}), f"degree drift r={r}")
        profiles, colors, packet, stabilization = Q25.stable_packet(adj)
        enc = Q25.packet_encoding(packet)
        if enc in seen:
            continue
        aut = Q25.automorphism_count(adj, profiles, colors)
        check(factor % aut == 0, f"nonintegral orbit r={r}")
        seen[enc] = (aut, stabilization)
        orbit_sum += factor // aut
        check(orbit_sum <= TARGET[r], f"orbit sum exceeds exact sector r={r}")
        if orbit_sum == TARGET[r]:
            closure = sample
            break
    check(closure == CLOSE[r], f"closure sample drift r={r}: {closure}")
    check(len(seen) == REPS[r], f"representative count drift r={r}")
    encs = sorted(seen)
    digest = hashlib.sha256(("\n".join(encs)+"\n").encode()).hexdigest()
    check(digest == PACKET_SHA[r], f"packet digest drift r={r}")
    return {"encodings":encs,"orbit_sum":orbit_sum,"representatives":len(seen),"closure":closure}

def verify_artifact(path, combined):
    a = json.loads(path.read_text(encoding="utf-8"))
    check(a.get("schema") == "P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1", "artifact schema drift")
    check(a.get("task_id") == TASK and a.get("publication_id") == PUB and a.get("claim_id") == CLAIM, "artifact identity drift")
    check(a.get("sector_expected_normalized_connected") == {str(k):v for k,v in TARGET.items()}, "artifact sector totals drift")
    check(a.get("sector_representatives") == {str(k):v for k,v in REPS.items()}, "artifact representative counts drift")
    check(a.get("sector_samples_to_exact_orbit_closure") == {str(k):v for k,v in CLOSE.items()}, "artifact closure drift")
    check(a.get("sector_packet_image_sha256") == {str(k):v for k,v in PACKET_SHA.items()}, "artifact packet digests drift")
    check(a.get("total_representatives") == TOTAL_REPS and a.get("total_normalized_connected") == TOTAL_CONNECTED, "artifact totals drift")
    check(a.get("combined_packet_image_sha256") == combined and a.get("collision_count") == 0, "artifact terminal image drift")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--artifact", type=Path, default=ROOT/"research_artifacts"/"P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER"/"P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1.json")
    args = p.parse_args()
    Q25.verify_degree_count_regression()
    for r,want in TARGET.items():
        got = Q25.connected_sector(11-r, r)
        check(got == want, f"n=11 connected count drift r={r}: {got} != {want}")
    rows = {r:sector(r) for r in (2,4,6,8,10)}
    check(sum(v["representatives"] for v in rows.values()) == TOTAL_REPS, "total representative drift")
    check(sum(v["orbit_sum"] for v in rows.values()) == TOTAL_CONNECTED, "total connected drift")
    all_enc = [e for r in (2,4,6,8,10) for e in rows[r]["encodings"]]
    check(len(all_enc) == len(set(all_enc)), "cross-sector packet collision")
    combined = hashlib.sha256(("\n".join(sorted(all_enc))+"\n").encode()).hexdigest()
    check(combined == COMBINED_SHA, "combined packet digest drift")
    verify_artifact(args.artifact, combined)
    print(f"PASS Q27 n=11 exact orbit certificate: representatives={TOTAL_REPS} normalized_connected={TOTAL_CONNECTED} stable_packets={len(all_enc)} collision=0 lower_bound=n<=11")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
