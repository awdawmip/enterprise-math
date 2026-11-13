#!/usr/bin/env python3
"""PREFIX-624 — original native X6-BRC action rank, exact certificates and linear repair.
Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
Native action enumerator is the same as PREFIX-623 at commit 0ccdeea6c7b5ab9d1ac833990ce6eb40d4db18a6.
Dependencies: Python 3 and SymPy; run python PREFIX624_native_action_rank_checker.py.
"""
from itertools import product
from pathlib import Path
import json
import sympy as S

STARS = ((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P = tuple((a,p,s*k) for a in range(4) for k in STARS[a]
          for s in (-1,1) for p in near(a,s*k))
IX = {p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c = P[i]
    b = next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]
                                  +[(b,c,k) for k in near(b,c)]))
N = tuple(neighbors(i) for i in range(48))
G = IX[(0,1,-3)]
AXIS = tuple(abs(c)-1 for a,p,c in P)
WEIGHTS = (1,1,1,1,0,0)
assert len(P)==48 and len(set(P))==48 and G==4 and sum(map(len,N))==144

def actions(z):
    for i in range(48):
        for j in N[i]:
            for u,v in product((0,1),repeat=2):
                wt = z if j==G and u==v==1 else WEIGHTS[AXIS[i]]
                yield (2*i+u,2*j+v,wt,(i,j,u,v))
def matrix(z):
    M = S.zeros(96,96)
    for dest,src,wt,label in actions(z):
        M[dest,src] += wt
    return M

A0,A1 = matrix(S.Integer(0)),matrix(S.Integer(1))
assert len(list(actions(1)))==576 and (A1-A0).rank()==1
assert sum((A1-A0)[i,j]!=0 for i in range(96) for j in range(96))==3
live = [j for j in range(48) if any(A1[:,2*j])]
silent = sorted(set(range(48))-set(live))
live_ports = [2*j+v for j in live for v in (0,1)]
assert len(live)==32 and len(silent)==16 and G in live
for z in (S.Integer(0),S.Integer(1),S.Integer(2),S.Rational(7,3)):
    assert {src for dst,src,wt,label in actions(z) if wt>0}==set(live_ports)
for j in live:
    assert A1[:,2*j]==A1[:,2*j+1]
    if j!=G: assert A0[:,2*j]==A0[:,2*j+1]
for j in silent:
    for u in (0,1): assert not any(A0[:,2*j+u]) and not any(A1[:,2*j+u])
assert all(A0[:,j]==A1[:,j] for j in range(96) if j!=9)

C32 = [2*j for j in live]
R32 = list(A1[:,C32].T.rref()[1])
assert len(R32)==32 and A1.extract(R32,C32).det(method="bareiss")==6561
C33 = C32+[9]
R33 = list(A0[:,C33].T.rref()[1])
assert len(R33)==33
D0 = A0.extract(R33,C33).det(method="bareiss")
D1 = A1.extract(R33,C33).det(method="bareiss")
D2 = matrix(S.Integer(2)).extract(R33,C33).det(method="bareiss")
assert (D0,D1,D2)==(-6561,0,6561)
# Only source column 9 changes with z; det(R33,C33)=6561*(z-1).
assert (A0.rank(),A1.rank(),matrix(S.Integer(2)).rank())==(33,32,33)

def recover(z,r):
    A = matrix(z)
    y = A*r
    if z==1:
        known = [2*j+1 for j in live]
        unknown,rows = C32,R32
    else:
        known = [2*j+1 for j in live if j!=G]
        unknown,rows = C33,R33
    assert set(known)|set(unknown)==set(live_ports)
    rhs = y.extract(rows,[0])-A.extract(rows,known)*r.extract(known,[0])
    vals = A.extract(rows,unknown).LUsolve(rhs)
    rec = S.zeros(96,1)
    for i in known: rec[i]=r[i]
    for k,i in enumerate(unknown):rec[i]=vals[k]
    assert all(rec[i]==r[i] for i in live_ports)
    assert A*rec==y
    assert all(wt*rec[src]==wt*r[src] for dest,src,wt,label in actions(z))
    return len(known)

n=0
for z in (S.Integer(0),S.Integer(1),S.Integer(2),S.Rational(7,3)):
    for sh in (0,3,11):
        r = S.Matrix([S.Rational((13*i+17+sh)%29+1,(i+sh)%7+1)
                      for i in range(96)])
        assert recover(z,r)==(32 if z==1 else 31)
        n+=1
result = {
 "schema":"PREFIX624_NATIVE_X6_POSITIVE_PATH_RANK_V1",
 "date":"2026-11-09","frozen_science":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
 "native_action_source_commit":"0ccdeea6c7b5ab9d1ac833990ce6eb40d4db18a6",
 "native_phases":48,"native_ports":96,"native_labelled_actions":576,
 "live_phase_indices":live,"silent_phase_indices":silent,
 "live_source_port_count":64,
 "rank_gate_0":33,"rank_gate_1":32,"rank_gate_2":33,
 "rank_all_nonnegative_gates_except_1":33,
 "rank_all_gate_1":32,"rank_labelled_flow_all_nonnegative_gates":64,
 "rank_gate_perturbation":1,
 "minor32_rows":R32,"minor32_columns":C32,"minor32_det_gate_1":"6561",
 "minor33_rows":R33,"minor33_columns":C33,
 "minor33_det_gate_0":str(D0),"minor33_det_gate_1":str(D1),
 "minor33_det_gate_2":str(D2),"minor33_det_symbolic":"6561*(z-1)",
 "minimal_additional_linear_scalar_reads_gate_1":32,
 "minimal_additional_linear_scalar_reads_other_gates":31,
 "exact_positive_rational_96_port_reconstruction_tests":n,
 "all_tagged_action_flows_exactly_recovered":True,
 "calculation":"exact SymPy rational/integer; no floating point",
 "review":"AUTHOR_SIDE_UNREVIEWED",
 "status":"ALL_ASSERTIONS_PASS"
}
Path(__file__).with_name("PREFIX624_native_action_rank_results.json").write_text(
    json.dumps(result,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({k:v for k,v in result.items() if not k.startswith("minor") and not k.endswith("_indices")}))
