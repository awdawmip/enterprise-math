#!/usr/bin/env python3
"""Independent exact audit of BRC N=4 BU full-causal 16-leaf reduction.
All arithmetic is rational or exact polynomial arithmetic.  Author-side model check,
not a native P000/X6 or formally admitted mathematical result.
"""
from collections import defaultdict
from fractions import Fraction as F
from random import Random
import sympy as S

q2 = {"AU": F(1,6), "AV": F(1,3), "BU": F(1,4), "BV": F(1,4)}
ratios = {
    "AU": (F(9,10),F(11,10)), "AV": (F(1,4),F(1,4)),
    "BU": (F(1,5),F(9,5)), "BV": (F(2),F(2)),
}
leaves = [(cat,j,k,q2[cat]/4,q2[cat]/4*ratios[cat][j])
          for cat in ("AU","AV","BU","BV") for j in range(2) for k in range(2)]
assert len(leaves)==16 and all(q>0 and p>0 for _,_,_,q,p in leaves)
assert sum(x[3] for x in leaves)==sum(x[4] for x in leaves)==1
assert {law: {root:sum((row[3] if law=="Q" else row[4]) for row in leaves if row[0][0]==root)
             for root in ("A","B")} for law in ("Q","P")} == {
                 "Q":{"A":F(1,2),"B":F(1,2)},
                 "P":{"A":F(1,4),"B":F(3,4)}}

# One computation through 16 leaves, no use of the claimed signed formulas.
def law_observation(policy, law):
    out=defaultdict(F)
    for cat,j,k,q,p in leaves:
        mass=q if law=="Q" else p
        root=cat[0]
        z=1 if cat=="BU" else 0
        t1=policy["t1"][root]
        t2=policy["t2"][cat]
        t3=policy["t3"][(cat,j)]
        for time,amount,pP in (
            (1, mass*(1-t1), policy["dec1"][root]),
            (2, mass*t1*(1-t2), policy["dec2"][cat]),
            (3, mass*t1*t2*(1-t3), policy["dec3"][(cat,j)]),
            (4, mass*t1*t2*t3, policy["dec4"][(cat,j,k)])
        ):
            zz=z if time>=3 else 0
            out[(time,"P",zz)]+=amount*pP
            out[(time,"Q",zz)]+=amount*(1-pP)
    assert sum(out.values())==1
    return out

def collapse_observation(observed):
    out=defaultdict(F)
    for (time,decision,z),mass in observed.items():
        if time<=2:
            key=(time,"Q",0)
        else:
            key=(3,"Q" if z==1 else "P",z)
        out[key]+=mass
    return out

def gk_policy(g):
    # Deterministic K-realizing S23 policy, matching G at t1/t2 continue rates.
    return dict(t1=g["t1"].copy(),t2=g["t2"].copy(),
                t3={(cat,j):F(0) for cat in q2 for j in range(2)},
                dec1={r:F(0) for r in ("A","B")},
                dec2={cat:F(0) for cat in q2},
                dec3={(cat,j):F(0) if cat=="BU" else F(1)
                      for cat in q2 for j in range(2)},
                dec4={(cat,j,k):F(1) for cat in q2 for j in range(2) for k in range(2)})

def target_policy(a,b):
    return dict(t1={"A":a,"B":b}, t2={"AU":F(1),"BU":F(0),"AV":F(0),"BV":F(0)},
                t3={(cat,j):F(0) for cat in q2 for j in range(2)},
                dec1={r:F(0) for r in ("A","B")},
                dec2={cat:F(0) for cat in q2},
                dec3={(cat,j):F(1) if cat=="AU" else F(0) for cat in q2 for j in range(2)},
                dec4={(cat,j,k):F(1) for cat in q2 for j in range(2) for k in range(2)})

def tv(x,y):
    return sum(abs(x.get(z,0)-y.get(z,0)) for z in set(x)|set(y))/2

# Independently reconstruct the four signed atom differences from second-level masses.
a,b,A,B,c,U,V=S.symbols('a b A B c U V', real=True)
secondP={cat: S.Rational(sum(row[4] for row in leaves if row[0]==cat).numerator,
                           sum(row[4] for row in leaves if row[0]==cat).denominator)
         for cat in q2}
secondQ={cat:S.Rational(m.numerator,m.denominator) for cat,m in q2.items()}
assert secondP=={"AU":S.Rational(1,6),"AV":S.Rational(1,12),
                 "BU":S.Rational(1,4),"BV":S.Rational(1,2)}

# Target and collapsed-competitor atoms, enumerating each category's marginal.
def four_atoms(law):
    w=secondQ if law=="Q" else secondP
    totalA=w["AU"]+w["AV"]
    totalB=w["BU"]+w["BV"]
    f=(1-a*totalA-b*totalB,
       a*w["AV"]+b*(w["BU"]+w["BV"]),
       a*w["AU"], S.Integer(0))
    g=(1-A*totalA-B*totalB,
       (A-A*c)*w["AU"]+(A-U)*w["AV"]+
       (B-B*c)*w["BU"]+(B-V)*w["BV"],
       A*c*w["AU"]+U*w["AV"]+V*w["BV"],
       B*c*w["BU"])
    assert S.expand(sum(f)-1)==S.expand(sum(g)-1)==0
    return tuple(S.expand(fv-gv) for fv,gv in zip(f,g))
s=(A-a+B-b)/2
p=(A-a+3*(B-b))/4
H=B*c/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
DQ_expected=(s,H-s-rQ,rQ,-H)
DP_expected=(p,H-p-rP,rP,-H)
assert all(S.cancel(x-y)==0 for x,y in zip(four_atoms("Q"),DQ_expected))
assert all(S.cancel(x-y)==0 for x,y in zip(four_atoms("P"),DP_expected))

# Check the deterministic K maps arbitrary S2 policies to actual S23 policies
# exactly under each law, and TV contracts for arbitrary rational policies.
rng=Random(20261029)

def rnd():
    return F(rng.randrange(0,12),11)

cases=[]
for idx in range(41):
    first={"A":rnd(),"B":rnd()}
    common=rnd()
    stage2={"AU":common,"BU":common,"AV":rnd(),"BV":rnd()}
    g=dict(t1=first,t2=stage2,
           t3={(cat,j):rnd() for cat in q2 for j in range(2)},
           dec1={r:rnd() for r in ("A","B")},
           dec2={cat:rnd() for cat in q2},
           dec3={(cat,j):rnd() for cat in q2 for j in range(2)},
           dec4={(cat,j,k):rnd() for cat in q2 for j in range(2) for k in range(2)})
    # Ensure a legal S2 policy has the same stop decision at equal-LR AU and BU.
    g["dec2"]["BU"]=g["dec2"]["AU"]
    f=target_policy(F(97,100),F(1,10))
    kg=gk_policy(g)
    for law in ("Q","P"):
        obsG=law_observation(g,law)
        obsK=law_observation(kg,law)
        post=collapse_observation(obsG)
        assert {k:v for k,v in obsK.items() if v}=={k:v for k,v in post.items() if v}, (idx,law,obsK,post)
        target=law_observation(f,law)
        assert {k:v for k,v in collapse_observation(target).items() if v}=={k:v for k,v in target.items() if v}
        assert tv(target,obsK)<=tv(target,obsG)
    # Check the complete four-atom signed vector for the same policy.
    av=F(97,100);bv=F(1,10)
    AA=first["A"];BB=first["B"]
    cc=common;UU=AA*stage2["AV"];VV=BB*stage2["BV"]
    subs={a:S.Rational(av),b:S.Rational(bv),A:S.Rational(AA),B:S.Rational(BB),
          c:S.Rational(cc),U:S.Rational(UU),V:S.Rational(VV)}
    for law, vec in (("Q",DQ_expected),("P",DP_expected)):
        observed=law_observation(f,law)
        observedK=law_observation(kg,law)
        keys=((1,"Q",0),(2,"Q",0),(3,"P",0),(3,"Q",1))
        measured=tuple(S.Rational(observed[z]-observedK[z]) for z in keys)
        symbolic=tuple(S.factor(x.subs(subs)) for x in vec)
        assert measured==symbolic, (idx,law,measured,symbolic)
    cases.append(g)

# Boundary rate guards demonstrate surjectivity (A=0 and/or B=0).
for AA,BB,cc,UU,VV in [(F(0),F(0),F(1),F(0),F(0)),
                         (F(0),F(1),F(1,2),F(0),F(1,2)),
                         (F(1),F(0),F(1,3),F(1,4),F(0)),
                         (F(1),F(1),F(1),F(1),F(1))]:
    cAV=F(0) if AA==0 else UU/AA
    cBV=F(0) if BB==0 else VV/BB
    assert 0<=cAV<=1 and 0<=cBV<=1

# Deliberately inefficient lawful S2 strategy: stop P at time 1,
# illustrating strict TV contraction by K rather than merely equality.
f=target_policy(F(97,100),F(1,10))
g=dict(t1={"A":F(97,100),"B":F(1,10)},
       t2={"AU":F(1,2),"BU":F(1,2),"AV":F(0),"BV":F(0)},
       t3={(cat,j):F(0) for cat in q2 for j in range(2)},
       dec1={"A":F(1),"B":F(1)},
       dec2={cat:F(0) for cat in q2},
       dec3={(cat,j):F(1) for cat in q2 for j in range(2)},
       dec4={(cat,j,k):F(1) for cat in q2 for j in range(2) for k in range(2)})
assert g["dec2"]["AU"]==g["dec2"]["BU"]
strict_data=[]
for law in ("Q","P"):
    tf=law_observation(f,law)
    eg=tv(tf,law_observation(g,law))
    ek=tv(tf,law_observation(gk_policy(g),law))
    assert ek<eg
    strict_data.append((law,eg,ek,eg-ek))
print('STRICT_DATA_PROCESSING_WITNESS',strict_data)
print('16_LEAVES',len(leaves),'Q_P_MASS',sum(row[3] for row in leaves),sum(row[4] for row in leaves))
print('EXACT_SYMBOLIC_VECTORS',four_atoms('Q'),four_atoms('P'))
print('POLICY_TEST_CASES',len(cases),'LAWS_PER_CASE',2,'BOUNDARY_RATE_CASES',4)
print('PASS_EXACT_BRC_N4_BU_CAUSAL_REDUCTION_16LEAF_AUDIT')
