#!/usr/bin/env python3
"""EC49FQT exact 30-node geometry and SHA256 evidence index checker.

Run: python EC49FQT_GEOMETRY_AND_INTEGRITY_20261116.py [extracted_archive_root]
For independently recomputed unrestricted Bellman optima, run
code/EC49FQT_INDEPENDENT_VERIFY.py from the full evidence archive.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
INDEX = HERE / "EC49FQT_EXACT_EVIDENCE_INDEX_20261116.json"
J = json.loads(INDEX.read_text())
assert J["source_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"

old = {
    F(1),F(13,12),F(7,6),F(5,4),F(4,3),F(17,12),
    F(3,2),F(13,8),F(7,4),F(15,8),F(2),F(17,8),
    F(9,4),F(19,8),F(5,2),F(31,12),F(8,3),
    F(11,4),F(17,6),F(23,8),F(3),F(47,16),
    F(39,16),F(35,16),F(37,16)
}
new = {F(n,16) for n in (25,27,29,31,33)}
G = sorted(old | new)
assert len(G) == 30
K = lambda x: 7557-169*x
gamma = lambda x: 310*(3-x)/K(x)
assert {str(x):str(gamma(x)) for x in sorted(new)} == J["new_gamma"]
assert all(x >= F(1) and x <= F(3) for x in G)
pairs = list(zip(G, G[1:]))
assert len(pairs) == 29
area = sum((b-a)*(gamma(a)-gamma(b)) for a,b in pairs)
frac = 1-area/2
assert area == F(43871554788230734445,7398811896183040660488)
assert frac == F(14753752237577850586531,14797623792366081320976)
assert str(frac) == J["certified_fraction"]
wide = [(a,b) for a,b in pairs if b-a == F(1,12)]
assert len(wide) == 10
assert max(wide) == (F(11,4), F(17,6))
assert all(b-a<=F(1,16) for a,b in pairs if (a,b) not in wide)
assert K(F(11,4)) == F(28369,4)
assert K(F(17,6)) == F(42469,6)
# Rigorous comparison of all shorter widths with the largest 1/12 width.
assert F(50,16*4*K(F(3))) < F(50,12*4*K(F(11,4)))
assert len(J["new_certificates"]) == 20

# Optional exact byte check of all new complete Bellman certificate files.
if len(sys.argv) > 1:
    root = Path(sys.argv[1])
    for path, record in J["new_certificates"].items():
        cert_path = root / "certificates" / path
        assert hashlib.sha256(cert_path.read_bytes()).hexdigest() == record["sha256"], path
        body = json.loads(cert_path.read_text())
        assert body["optimal_total_interpolated"] == record["optimum_integer"]
        assert body["optimal_first_interpolated"] == record["optimal_first"]
        assert body["frozen_scientific_commit"] == J["source_pin"]
    for path, digest in J["frozen_source_sha256"].items():
        assert hashlib.sha256((root/path).read_bytes()).hexdigest() == digest

print("EC49FQT_30_NODE_GEOMETRY_AND_INDEX_PASS")
print("exact_band_area =", area)
print("certified_fraction =", frac)
print("largest_regret_envelope_interval = [11/4,17/6]")
print("new_certificate_digest_checks =", 20 if len(sys.argv)>1 else "optional")
