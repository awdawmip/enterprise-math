#!/usr/bin/env python3
"""Check exact Bellman endpoints + affine witnesses for EC49FQD.
Run with the complete EC49FQD archive directory:
    python EC49FQD_PRICE_PHASE_CHECK_20261116.py /path/to/EC49FQD_COMPLETE_UNIFORM_PHASE
Independent source replays use EC49FQA_INDEPENDENT_REPLAY.py in that delivery.
"""
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

p = Path(sys.argv[1])
certs = p / "certificates"
pin = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
master = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
profile = "a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"
assert hashlib.sha256((p / "source/frozen_original_master.txt").read_bytes()).hexdigest() == master
assert hashlib.sha256((p / "source/EC49FPG_PROFILE.csv").read_bytes()).hexdigest() == profile
bounds = list(map(Fraction, ["0", "4/7", "10/17", "3/5", "2/3", "3/4",
    "7/9", "4/5", "153/184", "1", "3"]))
lines = [(362,0), (355,4), (338,14), (323,23), (311,31),
    (303,37), (267,65), (242,85), (58,238), (6,290), (4,296)]
assert len(bounds) == len(lines) == 11
anchors = {"4/7":"4_7", "10/17":"10_17", "3/5":"3_5", "2/3":"2_3",
    "3/4":"3_4", "7/9":"7_9", "4/5":"4_5",
    "153/184":"153_184", "1":"1_1", "3":"3_1"}
for x,name in anchors.items():
    c = json.loads((certs / ("EC49FQD_" + name + ".json")).read_text())
    assert c["frozen_scientific_commit"] == pin
    assert c["source_master_sha256"] == master
    assert c["native_root_costs_sha256"] == profile
    assert (c["profile_count"],c["config_count"],c["terminal_actions"],c["named_root_actions"]) == (141,310,144,84)
    r,t = c["prices"]["root"],c["prices"]["terminal"]
    assert Fraction(r,t) == Fraction(x)
    k = bounds.index(Fraction(x))
    optimal = c["optimal_total_uniform"]
    assert optimal == lines[k-1][0]*r + lines[k-1][1]*t
    assert optimal == lines[k][0]*r + lines[k][1]*t
    assert min(c["first_query_costs_uniform"]) == optimal
    print("BELLMAN_ENDPOINT_PASS", x, optimal)
witness = {
    "ROOT_ONLY": (362,0), "4_7": (355,4), "10_17": (338,14),
    "3_5": (323,23), "2_3": (311,31), "3_4": (303,37),
    "7_9": (267,65), "FQC_157_189": (242,85),
    "153_184": (58,238), "1_1": (6,290), "3_1": (4,296)}
for name,(r,t) in witness.items():
    c = json.loads((certs / ("EC49FQD_" + name + ".json")).read_text())
    assert c["frozen_scientific_commit"] == pin
    observations = c["replay"]["uniform"]
    assert (observations["weighted_root_observations"],observations["weighted_terminal_observations"]) == (r,t)
    assert r*c["prices"]["root"]+t*c["prices"]["terminal"] == c["optimal_total_uniform"]
    print("WITNESS_PASS", name, r, t)
for k in range(1,len(bounds)-1):
    x = bounds[k]
    assert lines[k-1][0]*x+lines[k-1][1] == lines[k][0]*x+lines[k][1]
print("EC49FQD_FULL_UNIFORM_POSITIVE_PRICE_PHASE_CERTIFICATE_PASS")
