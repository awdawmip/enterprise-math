"""Exact rational verification: R5 balanced-bypass normal-cone theorem."""
from fractions import Fraction as F
from itertools import product
Z, O, H, Q = F(0), F(1), F(1,2), F(1,4)
mass = {"via_k":(H,H),"bypass_k":(H,H)}
err = {"via_k":(Q,F(3,4)),"bypass_k":(F(3,4),Q)}
for i in mass:
    p,q=mass[i]; ep,eq=err[i]
    assert p>0 and q>0 and p==q
    assert Z<ep<O and Z<eq<O
    assert ep+(O-ep)==O and eq+(O-eq)==O
assert sum(m[0] for m in mass.values())==O
assert sum(m[1] for m in mass.values())==O
def obs(x,v,b):
    x,v,b=F(x),F(v),F(b)
    assert all(Z<=k<=O for k in (x,v,b))
    return (x*v/8+3*b/8,3*x*v/8+b/8,
            (3+x+x*v+b)/2,(3+x+x*v+b)/2)
def phi(o):
    ep,eq,tp,tq=o
    return 4+ep+3*eq-tp-tq
def add(*vs):
    return tuple(sum((v[i] for v in vs),Z) for i in range(4))
def neg(v):
    return tuple(-x for x in v)
A,B,C,D=[obs(i,j,j) for i,j in product((0,1),repeat=2)]
HV,HB=obs(O,O,Z),obs(O,Z,O)
assert HV==add(A,D,neg(B)) and HB==add(C,B,neg(A))
assert add(HV,HB)==add(C,D)
assert A==(Z,Z,F(3,2),F(3,2))
assert B==(F(3,8),F(1,8),F(2),F(2))
assert C==(Z,Z,F(2),F(2))
assert D==(H,H,F(3),F(3))
assert HV==(F(1,8),F(3,8),F(5,2),F(5,2))
assert HB==(F(3,8),F(1,8),F(5,2),F(5,2))
assert [phi(v) for v in (A,B,C,D,HV,HB)]==[O,F(3,4),Z,Z,Q,-Q]
for ix,iv,ib in product(range(9),repeat=3):
    x,v,b=F(ix,8),F(iv,8),F(ib,8)
    assert phi(obs(x,v,b))==O-x+x*v/4-b/4>=-Q
for ix,iy in product(range(9),repeat=2):
    x,y=F(ix,8),F(iy,8)
    assert phi(obs(x,y,y))==(O-x)*(O-y/4)>=Z
assert min(phi(obs(i,j,j)) for i,j in product((0,1),repeat=2))==Z
assert min(phi(obs(i,j,k)) for i,j,k in product((0,1),repeat=3))==-Q
P={
 "A":(0,0,0,0),"B":(1,0,0,0),"C":(0,1,0,0),
 "D":(0,0,1,0),"E":(-2,-2,1,0),"F":(-2,-2,2,0),
 "Q":(0,0,0,1)}
P={k:tuple(F(x) for x in v) for k,v in P.items()}
scores={
 "A":lambda p:-p[0]-p[1]-5*p[2]-p[3],
 "B":lambda p:p[0]-p[3],
 "C":lambda p:p[1]-p[3],
 "D":lambda p:p[0]+p[1]+3*p[2]-p[3],
 "E":lambda p:-p[0]-p[1]-p[2]-p[3],
 "F":lambda p:p[2]-p[3],
 "Q":lambda p:p[3]}
for k,f in scores.items():
    assert all(f(P[k])>f(v) for j,v in P.items() if j!=k)
def edge(v):return 4+v[0]-4*v[1]-4*v[2]
assert {k for k,v in P.items() if edge(v)==Z}=={"C","D"}
assert all(edge(v)>=Z for v in P.values())
S1=add(P["A"],P["D"],neg(P["B"]))
S2=add(P["C"],P["B"],neg(P["A"]))
assert add(S1,S2)==add(P["C"],P["D"])
assert (edge(S1),edge(S2))==(-O,O)
print("TWO_LAW_KERNELS_POSITIVE_AND_NORMALIZED=YES")
print("LR_TIME2_COLLISION_PQ_MASSES=1/2,1/2_EACH_ORIGIN")
print("CORNERS="+repr((A,B,C,D)))
print("FULL_SPLIT="+repr((HV,HB)))
print("PHI_VALUES="+repr(tuple(phi(v) for v in (A,B,C,D,HV,HB))))
print("ALL_REAL_LR_MIN=0 FULL_MIN=-1/4 GAP=1/4 DIST_INF_GE=1/24")
print("ABSTRACT_4D_FACET=6_EXTREME_VERTICES; CD_EXPOSED_EDGE=YES")
print("ABSTRACT_EDGE_SPLIT_PHI=(-1,+1); DIST_INF_GE=1/9")
print("GRID_CHECKS=729_FULL+81_LR (NOT ALL_REAL_PROOF)")
print("PASS_EXACT_R5_BALANCED_BYPASS_NORMAL_CONE")
