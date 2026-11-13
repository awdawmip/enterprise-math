#!/usr/bin/env python3
"""Exact algebra checks for unreviewed AU/BU lineage observer refinement."""
import sympy as s

A,B,a,b,c,U,V=s.symbols("A B a b c U V", real=True)
H=B*c/4
qF=s.Matrix([1-(a+b)/2, a/3+b/2, a/6, 0, 0])
pF=s.Matrix([1-(a+3*b)/4, a/12+3*b/4, a/6, 0, 0])
qG=s.Matrix([
    1-(A+B)/2, (A+B)/2-A*c/6-B*c/4-U/3-V/4,
    A*c/6, U/3+V/4, H,
])
pG=s.Matrix([
    1-(A+3*B)/4, (A+3*B)/4-A*c/6-B*c/4-U/12-V/2,
    A*c/6, U/12+V/2, H,
])
delta_s=(A-a+B-b)/2
delta_t=(A-a+3*(B-b))/4
w=a/6-A*c/6
dq=s.Matrix([delta_s,H-delta_s-w+U/3+V/4,w,-U/3-V/4,-H])
dp=s.Matrix([delta_t,H-delta_t-w+U/12+V/2,w,-U/12-V/2,-H])
assert all(s.simplify(x)==0 for x in qF-qG-dq)
assert all(s.simplify(x)==0 for x in pF-pG-dp)
for v in (qF,pF,qG,pG):
    assert s.simplify(sum(v)-1)==0
q4=s.Matrix([dq[0],dq[1],dq[2]+dq[3],dq[4]])
p4=s.Matrix([dp[0],dp[1],dp[2]+dp[3],dp[4]])
assert s.simplify(q4[2]-(a/6-A*c/6-U/3-V/4))==0
assert s.simplify(p4[2]-(a/6-A*c/6-U/12-V/2))==0
values={a:s.Rational(1,2),A:s.Rational(1,2),b:0,B:0,c:0,U:s.Rational(1,4),V:0}
def tv(vector):
    return s.Rational(1,2)*sum(abs(x.subs(values)) for x in vector)
assert (tv(q4),tv(dq),tv(p4),tv(dp)) == (
    0,s.Rational(1,12),s.Rational(1,16),s.Rational(1,12)
)
print("PASS_SYMBOLIC_5_ATOM_AU_BU_REFINEMENT")
print("STRICT_REFINEMENT_WITNESS",{
    "Q_coarse":str(tv(q4)), "Q_refined":str(tv(dq)),
    "P_coarse":str(tv(p4)), "P_refined":str(tv(dp)),
})
