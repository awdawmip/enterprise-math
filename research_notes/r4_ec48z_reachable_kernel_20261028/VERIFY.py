#!/usr/bin/env python3
"""EC48Z: exact Fraction audit of reachable-kernel quotient LP (12 positive leaves)."""
from fractions import Fraction as F
from itertools import product
from random import Random
import json

Z = ("A", "B", "C")
W = (0, 1)
H = (0, 1)
qz = {0: (F(1,4), F(1,2), F(1,4)),
      1: (F(1,8), F(3,4), F(1,8))}
ratio = (F(1,2), F(1), F(3,2))
qw1 = {0: F(1,4), 1: F(3,4)}

# The first observed H is intentionally erased by the fixed one-register updater.
# P/Q share H, and P(Z|H)=ratio[Z] * Q(Z|H); P/Q share W|H,Z.
leaves = {}
for h, z, w in product(H, range(3), W):
    q = F(1,2)*qz[h][z]*(qw1[h] if w else 1-qw1[h])
    p = q*ratio[z]
    leaves[h,z,w] = (p,q)
assert all(p>0 and q>0 for p,q in leaves.values())
assert sum(p for p,q in leaves.values()) == 1
assert sum(q for p,q in leaves.values()) == 1
assert all(sum(qz[h][z]*ratio[z] for z in range(3)) == 1 for h in H)
assert qz[0] != qz[1] and qw1[0] != qw1[1]

QZ = tuple(sum(F(1,2)*qz[h][z] for h in H) for z in range(3))
PZ = tuple(QZ[z]*ratio[z] for z in range(3))
KW1 = tuple(sum(F(1,2)*qz[h][z]*qw1[h] for h in H)/QZ[z] for z in range(3))
assert QZ == (F(3,16), F(5,8), F(3,16))
assert PZ == (F(3,32), F(5,8), F(9,32))
assert KW1 == (F(5,12), F(11,20), F(5,12))
assert all(sum(leaves[h,z,w][0] for w in W)/sum(leaves[h,z,w][1] for w in W)==ratio[z]
           for h,z in product(H,range(3)))
assert all(leaves[h,z,w][0]/leaves[h,z,w][1]==ratio[z]
           for h,z,w in product(H,range(3),W))


def qpoly(pol):
    """A single common source-neutral behavioral policy: [a,r,c] at t1,t2; t3 accept."""
    init, middle, last = pol
    a1, r1, c1 = init
    assert a1+r1+c1==1 and min(init)>=0
    assert len(middle)==3 and len(last)==6
    for row in middle:
        assert sum(row)==1 and min(row)>=0
    assert all(0<=u<=1 for u in last)
    val=[]
    for masses in (PZ,QZ):
        acc = a1 + c1*sum(masses[z]*(middle[z][0]+middle[z][2]*
              ((1-KW1[z])*last[2*z]+KW1[z]*last[2*z+1])) for z in range(3))
        et = 1+c1+c1*sum(masses[z]*middle[z][2] for z in range(3))
        val.append((acc,et))
    return (val[0][0],val[1][0],val[0][1],val[1][1])


def fine(pol):
    init, middle, last=pol
    a1,r1,c1=init
    out=[]
    for source in (0,1):
        mass = lambda h,z,w: leaves[h,z,w][source]
        acc = a1 + c1*sum(mass(h,z,w)*(middle[z][0]+middle[z][2]*last[2*z+w])
                             for h,z,w in product(H,range(3),W))
        et = 1+c1+c1*sum(mass(h,z,w)*middle[z][2]
                            for h,z,w in product(H,range(3),W))
        out.append((acc,et))
    return (out[0][0],out[1][0],out[0][1],out[1][1])


def kernel_test(pol):
    c1=pol[0][2]
    for z in range(3):
        lhs_z=sum(F(1,2)*c1*qz[h][z] for h in H)
        assert lhs_z == c1*QZ[z]
        for w in W:
            lhs_w=sum(F(1,2)*c1*qz[h][z]*
                      (qw1[h] if w else 1-qw1[h]) for h in H)
            rhs_w=c1*QZ[z]*(KW1[z] if w else 1-KW1[z])
            assert lhs_w==rhs_w

ZERO=F(0)
ONE=F(1)
basis=((ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE))
case_count=0
unique=[]
for init_choice in range(3):
    for mid_choices in product(range(3),repeat=3):
        mid=tuple(basis[a] for a in mid_choices)
        for terminal_choices in product((ZERO,ONE),repeat=6):
            pol=(basis[init_choice],mid,terminal_choices)
            o=fine(pol)
            assert o==qpoly(pol)
            kernel_test(pol)
            unique.append(o)
            case_count+=1
assert case_count==3*3**3*2**6==5184

rng=Random(480048)
random_checked=0
for _ in range(1000):
    def triple():
        weights=[rng.randint(0,9) for _ in range(3)]
        if not sum(weights): weights[0]=1
        return tuple(F(v,sum(weights)) for v in weights)
    pol=(triple(), tuple(triple() for z in range(3)),
         tuple(F(rng.randint(0,12),12) for z,w in product(range(3),W)))
    assert fine(pol)==qpoly(pol)
    kernel_test(pol)
    random_checked+=1

pol=( (F(1,8),F(1,4),F(5,8)),
      ((F(1,4),F(1,4),F(1,2)),
       (F(1,8),F(3,8),F(1,2)),
       (F(1,2),F(1,4),F(1,4))),
      (F(1,3),F(2,3),F(1,4),F(3,4),F(2,5),F(4,5)) )
witness=fine(pol)
assert witness==qpoly(pol)
assert witness[2]!=witness[3] # two sources have different expected stopping times

report={
  "model":"EC48Z one-register 3-decision-stage strictly-positive rational dual-source model",
  "leaves":12,"source_mass":["1","1"],
  "fine_not_controlled_Markov_at_stages":[1,2],
  "QZ":[str(x) for x in QZ], "PZ":[str(x) for x in PZ],
  "Kbar_Q_W1_given_Z":[str(x) for x in KW1],
  "full_LR_given_Z":[str(x) for x in ratio],
  "deterministic_strategies_exhaustively_checked":case_count,
  "sampled_rational_behavioral_strategies_checked":random_checked,
  "total_four_vector_and_kernel_checks":case_count+random_checked,
  "distinct_deterministic_four_vectors":len(set(unique)),
  "explicit_rational_strategy_four_vector":[str(x) for x in witness],
  "all_assertions":"PASS",
  "coverage":"finite model strategy enumeration/sample; universal reachable-kernel LP theorem is analytic; no native X6 or signed amplitude computation"
}
print(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2))
