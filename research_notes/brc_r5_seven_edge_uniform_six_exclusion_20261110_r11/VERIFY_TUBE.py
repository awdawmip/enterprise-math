#!/usr/bin/env python3
"""Verify an exact uniform six-edge exclusion tube around R5's closed seven-edge sheet.
The prior exact seven-edge composite verifier is imported by runpy from this
stacked research branch; the added checks are Fraction/SymPy-exact.
"""
from pathlib import Path
import runpy
import sympy as S
from fractions import Fraction as F

prior=Path(__file__).resolve().parents[1]/"brc_r5_exact_seven_edge_polygon_20261110_t1640"/"VERIFY_7.py"
p=runpy.run_path(str(prior))  # validates the pinned earlier exact model and polygon
C,D,DUAL=p["C"],p["D"],p["DUAL"]
F6,M6=p["F6"],p["M6"]
T=p["T"]
assert C.shape==(15,30) and len(D)==30 and M6.rank()==6
assert tuple(F6)==((0,0),(3,3),(4,3),(4,5),(6,5),(6,6))
assert p["K7"].shape==(8,2) and len(p["verts"])==5
assert all(v>0 for v in p["dual_min"].values())
assert all(v>0 for v in p["masses_min"].values())

ell=S.zeros(15,1)
ell[3]=-S.Rational(5,23)
ell[10]=S.Rational(25,23)
ell[14]=-S.Rational(1,23)
c7=C[:,D.index((0,3))]
assert (ell.T*M6)==S.zeros(1,6)
assert (ell.T*c7)[0]==1
norm_ell=sum(abs(v) for v in ell)
assert norm_ell==S.Rational(31,23)

margins={}
y_norms={}
for e in F6:
    y=S.zeros(15,1)
    for token in DUAL[e].split():
        i,v=token.split(":")
        y[int(i)]=S.Rational(v)
    assert all((y.T*C[:,j])[0] <= int(D[j]==e) for j in range(30))
    y_norms[e]=sum(abs(v) for v in y)
    margins[e]=p["dual_min"][e]/y_norms[e]
assert y_norms=={
 (0,0):1,(3,3):S.Rational(212,5),(4,3):S.Rational(451,10),
 (4,5):S.Rational(119,5),(6,5):S.Rational(297,13),
 (6,6):S.Rational(142,25)}
beta7=p["masses_min"][(0,3)]
seven_margin=beta7/norm_ell
r_q=min([*margins.values(),seven_margin])
assert r_q==S.Rational(2502770274125,3676504873334904)
assert margins[(4,3)]==r_q
assert all(margins[e]>=r_q for e in F6) and seven_margin>=r_q
assert all(p["dual_min"][e]>r_q*y_norms[e]/2 for e in F6)
assert beta7>r_q*norm_ell/2
T_norm=max(sum(abs(T[i,j]) for j in range(8)) for i in range(15))
assert T_norm==S.Rational(405,2)
r_z=r_q/T_norm
assert r_z==S.Rational(500554054825,148898447370063612)
print("SIX_DUALS_CHECKED_FULL_30_COLUMN_MODEL", True)
print("SEVENTH_SEPARATOR_ELL",tuple(ell),"L1",norm_ell)
print("DUAL_NORMALIZED_MARGINS",margins)
print("SEVENTH_NORMALIZED_MARGIN",seven_margin)
print("UNIFORM_15D_OPEN_RADIUS",r_q)
print("UNIFORM_15D_CLOSED_RADIUS",r_q/2)
print("EXACT_T_INFINITY_OPERATOR_NORM",T_norm)
print("UNIFORM_8D_PHYSICAL_PARAMETER_OPEN_RADIUS",r_z)
print("PASS_R5_UNIFORM_SIX_EDGE_EXCLUSION_TUBE")
