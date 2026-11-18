#!/usr/bin/env python3
"""Independent exact rational geometry/anchor checker for EC49FTA.
With the self-contained evidence archive present, run EC49FTA_VERIFY.py for
complete 228-physical-observer Bellman recalculation and four-tree replay.
This small checker verifies the 23 published rational anchor receipts,
all actual switch geometry, and the sharp exchange gap without third-party deps.
"""
import csv
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

A=(Q(133,246),Q(9,16))
B=(Q(7,16),Q(57,128))
Z=(Q(1,2),Q(9,16))
D1=(Q(319),-Q(18),-Q(75),-Q(141))
D3=(Q(316),-Q(141),-Q(43),-Q(30))
P=(Q(315),-Q(141),-Q(10),-Q(77))
C=(Q(323),-Q(89),-Q(12),-Q(141))
def f(plane,x):
    return plane[0]+sum(a*b for a,b in zip(plane[1:],x))
def diff(a,b):
    return tuple(x-y for x,y in zip(a,b))
def det3(m):
    return m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
def intersection(p):
    m=[q[1:] for q in p]
    d=det3(m)
    if not d:
        return None
    rhs=[-q[0] for q in p]
    return tuple(det3([[rhs[i] if j==k else m[i][j] for j in range(3)] for i in range(3)])/d for k in range(3))
FACE=[(-q,Q(1),Q(0),Q(0)) for q in A]+[(-q,Q(0),Q(1),Q(0)) for q in B]+[(-q,Q(0),Q(0),Q(1)) for q in Z]
D_SWITCH=diff(D1,D3)
S_SWITCH=diff(P,C)
def vertices(extra):
    result=set()
    for eq in combinations(FACE+list(extra),3):
        x=intersection(eq)
        if x is not None and all(low<=v<=hi for v,(low,hi) in zip(x,(A,B,Z))):
            result.add(x)
    return sorted(result)
def optimum(orientation,x):
    return min(f(p,x) for p in ((D1,D3) if orientation=="D" else (P,C)))
def gap(x):
    return optimum("D",x)-optimum("S",x)

def audit(path):
    assert D_SWITCH==(Q(3),Q(123),-Q(32),-Q(111))
    assert S_SWITCH==(-Q(8),-Q(52),Q(2),Q(64))
    dv=vertices([D_SWITCH]); sv=vertices([S_SWITCH])
    assert (len(dv),len(sv))==(11,12)
    expected={"D":set(dv),"S":set(sv)}
    rows={"D":[],"S":[]}
    with Path(path).open(newline="") as fh:
        for row in csv.DictReader(fh):
            orientation=row["orientation"]
            x=tuple(Q(row[q]) for q in ("a","b","z"))
            v=Q(row["unrestricted_optimum"])
            assert row["primary_exact_match"]=="true"
            assert v==Q(row["expected_minimum"])==optimum(orientation,x)
            rows[orientation].append(x)
    for key in ("D","S"):
        assert len(rows[key])==len(expected[key])
        assert set(rows[key])==expected[key]
    v=vertices([D_SWITCH,S_SWITCH])
    assert len(v)==15
    low=min((gap(p),p) for p in v)
    high=max((gap(p),p) for p in v)
    assert low==(Q(99683,15744),(Q(133,246),Q(57,128),Q(277277,503808)))
    assert high==(Q(4973,444),(Q(9,16),Q(7,16),Q(931,1776)))
    print("PASS geometry: 11 D, 12 S, 15 joint vertices")
    print("PASS 23 exact rational original-observer Bellman records")
    print("PASS sharp gap:",str(low[0]),"< D-S <",str(high[0]))

if __name__=="__main__":
    audit(Path(__file__).with_name("EC49FTA_EXACT_23_BELLMAN_ANCHORS_20261118.csv"))
