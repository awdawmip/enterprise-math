#!/usr/bin/env python3
"""Recompute EC49FSR's exact original-BRC16943 native Bellman vertices.

Use the frozen source data and primary/independent solvers from the EC49FSO
self-contained original-source archive, with its 'code/' directory on
PYTHONPATH. Scientific source commit is fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

Usage:
  PYTHONPATH=/path/to/frozen/code python EC49FSR_REPLAY_NATIVE_3D_VERTEX_CERT_20261118.py
  PYTHONPATH=/path/to/frozen/code python ...py --independent crossing
  PYTHONPATH=/path/to/frozen/code python ...py --independent swapped

Run independent cases separately to keep DP memory bounded.
"""
from fractions import Fraction as Q
from pathlib import Path
import json,sys

from EC49FSA_THREE_OBSERVER_SOLVER import PIN, solve

HERE=Path(__file__).resolve().parent
CERT=json.loads((HERE/"EC49FSR_NATIVE_3D_BELLMAN_VERTEX_CERT_20261118.json").read_text())
assert PIN==CERT["science_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"

def A(a,b,z):return 319-18*a-75*b-141*z
def B(a,b,z):return 313-141*a-43*b-24*z
def C(a,b,z):return 311-141*a-10*b-69*z

def discount(row):
    a,b,z=[Q(row[k]) for k in ("a","b","z")]
    return ({32:b,34:a,140:z} if row["kind"]=="swapped_base"
            else {32:a,34:b,140:z})

def test_primary():
    rows=CERT["primary_vertices"]
    assert len(rows)==12
    for row in rows:
        a,b,z=[Q(row[k]) for k in ("a","b","z")]
        expected=Q(row["exact"])
        ast=(32*b+117*z-6)/123
        assert Q(1,2)<ast<1
        if row["kind"]=="unsaturated_lower":
            assert a==Q(1,2)
            assert expected==A(a,b,z)
        elif row["kind"]=="crossing":
            assert a==ast
            assert expected==A(a,b,z)==B(a,b,z)
        else:
            assert row["kind"]=="swapped_base" and a==Q(1,2)
            assert expected==C(a,b,z)
        info,full_tree=solve(discount(row))
        value=Q(info["numerator"],info["denominator"])
        assert value==expected,(row,info)
        if row["kind"]=="crossing":
            assert info["uses"]["32"]==141
        if row["kind"]=="swapped_base":
            assert info["uses"]["34"]==141
        assert info["states"]==row["reached_subsets"],(row,info)
        print("EXACT_ALL228_PASS",row["kind"],row["a"],row["b"],row["z"],str(value),flush=True)
    print("EC49FSR_12_VERTEX_PASS",len(rows))

def test_independent(tag):
    from EC49FSA_FSB_INDEPENDENT_CHECK import certify
    row=(CERT["primary_vertices"][1] if tag=="crossing" else CERT["primary_vertices"][11])
    assert tag in ("crossing","swapped")
    d=discount(row)
    actual=certify(d)
    assert Q(actual["value"])==Q(row["exact"])
    expected_state_count=9845 if tag=="crossing" else 9535
    assert actual["states"]==expected_state_count
    print("INDEPENDENT_ORIGINAL94_PASS",tag,actual["value"],actual["states"])

if __name__=="__main__":
    if len(sys.argv)==1: test_primary()
    elif len(sys.argv)==3 and sys.argv[1]=="--independent":
        test_independent(sys.argv[2])
    else:raise SystemExit("Use no args, or --independent crossing|swapped")
