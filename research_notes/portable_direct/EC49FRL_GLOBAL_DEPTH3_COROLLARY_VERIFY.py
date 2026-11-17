#!/usr/bin/env python3
"""EC49FRL: exact full-named native replay of the five inherited global BRC trees.

Run with the frozen EC49FRL evidence archive extracted. The program uses
unmodified original physical response IDs and the prior Bellman endpoint
JSON files. It checks depth, complete identification, exact query masses,
and canonical SHA256 of each tree object; no interpolation or floating point.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
from EC49FQI_NATIVE_DATA import V, weights, PIN

BASE = Path(__file__).resolve().parent.parent
assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
spec = {
    "A": ("x1-1_l0-1.json", "32", (6, 290, 6, 751)),
    "B": ("x1-1_l155-1847.json", "140", (5, 293, 5, 704)),
    "C": ("x1-1_l1-1.json", "16", (5, 295, 5, 685)),
    "D": ("x100000-1_l0-1.json", "140", (4, 296, 4, 707)),
    "E": ("x100000-1_l1-1.json", "16", (4, 298, 4, 688)),
}
expected_hashes = {
    "A": "50d4e26131e68373a57446a10f75c86bc7b95fbac509b858b90b863f2b8763aa",
    "B": "d9a3d95391459c49624f0b083d137d2ff55f13d31a24a2e00f99cf649018b12f",
    "C": "7b188990d5ae88f4d10e5015c28311330f764ac33e23b53693434340dda61100",
    "D": "764ab444a59ab338cd78ab56d105282da5724a2fdfad6e4b628ad0234a58ca6a",
    "E": "9a8b28cdf8d177ce9f2959c251db2274ef0690d34a7c8da338779bc53e3ef52f",
}
actual = {}
for label, (filename, query, expected_masses) in spec.items():
    endpoint = json.loads((BASE / "prior_endpoint_trees" / filename).read_text())
    tree = endpoint["all_optimal_first_trees"][query]
    assert tree["q"] == int(query)
    u_root = u_terminal = m_root = m_terminal = max_depth = 0
    depth_hist = Counter()
    for i in range(141):
        node = tree
        depth = 0
        while "leaf" not in node:
            z = node["q"]
            depth += 1
            assert depth <= 3
            if z < 144:
                u_terminal += 1
                m_terminal += weights[i]
            else:
                u_root += 1
                m_root += weights[i]
            node = node["children"][str(V[z][i])]
        assert node["leaf"] == i
        max_depth = max(max_depth, depth)
        depth_hist[depth] += 1
    masses = (u_root, u_terminal, m_root, m_terminal)
    assert masses == expected_masses
    assert max_depth == 3 and sum(depth_hist.values()) == 141
    canonical = json.dumps(tree, ensure_ascii=False, sort_keys=True,
                           separators=(",", ":")).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()
    assert digest == expected_hashes[label]
    actual[label] = {"source": filename, "original_root_query": int(query),
                     "cost_vector": list(masses), "max_depth": max_depth,
                     "depth_counts": dict(depth_hist), "tree_sha256": digest}
    print("PASS", label, actual[label])

expected = json.loads(
    (BASE / "EC49FRL_GLOBAL_FIVE_TREE_DEPTH3_CERTIFICATE.json").read_text())
assert actual == expected
print("PASS all five complete original native trees: 141 named states each, max depth 3")
print("The global envelope across x>=1 and lambda in [0,1] is the inherited EC49FRJ theorem.")
