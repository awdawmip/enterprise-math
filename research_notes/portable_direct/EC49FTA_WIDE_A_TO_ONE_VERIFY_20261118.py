#!/usr/bin/env python3
"""Exact 23-anchor and rational polyhedral certificate, widened EC49FTA a<=1."""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util,csv
BASE=Path(__file__).resolve().parent
path=BASE/"EC49FTA_VERIFY_TWO_SWITCH_FAN_20261118.py"
spec=importlib.util.spec_from_file_location("old",path)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
old.A=(Q(133,246),Q(1))
old.FACE=[(-q,Q(1),Q(0),Q(0)) for q in old.A]+[(-q,Q(0),Q(1),Q(0)) for q in old.B]+[(-q,Q(0),Q(0),Q(1)) for q in old.Z]
fn=BASE/"EC49FTA_WIDE_A_TO_ONE_23_BELLMAN_ANCHORS_20261118.csv"
records={"D":[],"S":[]}
with fn.open(newline="") as stream:
    for row in csv.DictReader(stream):
        o=row["orientation"]
        assert o in records and row["primary_exact_match"]=="true"
        x=tuple(Q(row[k]) for k in ("a","b","z"))
        v=Q(row["unrestricted_optimum"])
        assert v==Q(row["expected_minimum"])==old.optimum(o,x),(o,x,v)
        records[o].append(x)
for o,switch,n in [("D",old.D_SWITCH,11),("S",old.S_SWITCH,12)]:
    expected=old.vertices([switch])
    assert len(records[o])==n and set(records[o])==set(expected)
joint=old.vertices([old.D_SWITCH,old.S_SWITCH])
assert len(joint)==15
lower=min((old.gap(x),x) for x in joint)
upper=max((old.gap(x),x) for x in joint)
assert lower==(Q(99683,15744),(Q(133,246),Q(57,128),Q(277277,503808)))
assert upper==(Q(13),(Q(1),Q(7,16),Q(9,16)))
print("EC49FTA_WIDE_PASS: 11 D and 12 S unrestricted exact original-observer anchors")
print("EC49FTA_WIDE_PASS: 15 exact two-switch arrangement vertices")
print("EC49FTA_WIDE_PASS: sharp global exchange gap",lower[0],upper[0])
