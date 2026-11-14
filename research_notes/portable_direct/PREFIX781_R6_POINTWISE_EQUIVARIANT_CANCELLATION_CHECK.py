#!/usr/bin/env python3
"""PREFIX781: exact rational regression for two reflected adjacent cells.

Scope: observer-level algebra; NOT a new native BRC/X6/Gamma-kernel run.
"""
from fractions import Fraction as F
from itertools import product
import json


def ss(x):
    return str(x)


def cancellation_window(A1, A2, B1, B2, S1, S2, c):
    assert 0 < B1 < B2 and A2*B1-A1*B2 > 0
    assert min(S1,S2,c) >= 0
    i1=((A1-S1-c)/B1,(A1+S1+c)/B1)
    i2=((A2-S2-c)/B2,(A2+S2+c)/B2)
    i3=((A2-A1-S1-S2)/(B2-B1),(A2-A1+S1+S2)/(B2-B1))
    left=max(F(0),i1[0],i2[0],i3[0])
    right=min(i1[1],i2[1],i3[1])
    return {"intervals":(i1,i2,i3),"left":left,"right":right,
            "nonempty":left<=right and right>0}


def allocate(total,budgets,signs):
    """Construct signed private corner errors summing exactly to total."""
    S=sum(budgets, F(0))
    assert len(budgets)==3 and len(signs)==3
    if S == 0:
        assert total == 0
        return (F(0),)*3
    assert abs(total)<=S
    return tuple(s*total*w/S for s,w in zip(signs,budgets))


def witness(A1,A2,B1,B2,q,b1,b2,c):
    """Base seven corners; reflected partners copy them."""
    S1=sum(b1,F(0)); S2=sum(b2,F(0))
    x1=A1-q*B1; x2=A2-q*B2
    low=max(-c,-x1-S1,-x2-S2)
    high=min(c,-x1+S1,-x2+S2)
    if low>high:
        return None
    h=(low+high)/2
    r1=allocate(-x1-h,b1,(1,-1,-1))
    r2=allocate(-x2-h,b2,(1,-1,-1))
    assert all(abs(v)<=b for v,b in zip(r1,b1))
    assert all(abs(v)<=b for v,b in zip(r2,b2))
    assert abs(h)<=c
    L1=r1[0]-r1[1]-r1[2]+h
    L2=r2[0]-r2[1]-r2[2]+h
    assert x1+L1==x2+L2==0
    return {"R1_private":r1,"R2_private":r2,"shared":h}


def weighted_distance(A1,A2,B1,B2,q,S1,S2,c):
    x1=A1-q*B1; x2=A2-q*B2
    ratios=[]
    for a,b in ((abs(x1),S1+c),(abs(x2),S2+c),
                (abs(x1-x2),S1+S2)):
        if b==0 and a!=0:
            return None  # exact distance +infinity
        ratios.append(F(0) if b==0 else a/b)
    return max(ratios)


def check_case(A1,A2,B1,B2,b1,b2,c,q):
    S1=sum(b1,F(0)); S2=sum(b2,F(0))
    x1=A1-q*B1; x2=A2-q*B2
    criteria=(abs(x1)<=S1+c and abs(x2)<=S2+c
              and abs(x1-x2)<=S1+S2)
    bounds=cancellation_window(A1,A2,B1,B2,S1,S2,c)
    interval=(bounds["left"]<=q<=bounds["right"] and q>0)
    intersection=(max(-c,-x1-S1,-x2-S2)
                  <=min(c,-x1+S1,-x2+S2))
    assert criteria==interval==intersection
    w=witness(A1,A2,B1,B2,q,b1,b2,c)
    assert (w is not None)==criteria
    distance=weighted_distance(A1,A2,B1,B2,q,S1,S2,c)
    assert (distance is not None and distance<=1)==criteria
    if distance is not None and distance>0:
        assert witness(A1,A2,B1,B2,q,
                       tuple(distance*t for t in b1),
                       tuple(distance*t for t in b2),distance*c) is not None
        smaller=(distance-F(1,1000)
                 if distance>F(1,1000) else distance/2)
        assert witness(A1,A2,B1,B2,q,
                       tuple(smaller*t for t in b1),
                       tuple(smaller*t for t in b2),smaller*c) is None
    return criteria


def run():
    A1,A2,B1,B2=map(F,[1,2,2,3])
    D=A2*B1-A1*B2
    b1=(F(1,10),F(1,10),F(1,20))
    b2=(F(1,10),F(1,20),F(1,20))
    c=F(1,10)
    win=cancellation_window(A1,A2,B1,B2,sum(b1,F(0)),sum(b2,F(0)),c)
    assert (win["left"],win["right"])==(F(17,30),F(27,40))
    w=witness(A1,A2,B1,B2,F(3,5),b1,b2,c)
    assert w is not None and witness(A1,A2,B1,B2,F(1,2),b1,b2,c) is None
    qstar=(A1+2*A2)/(B1+2*B2)
    epsstar=D/(2*(B1+2*B2))
    def radius(q):
        x1=A1-q*B1; x2=A2-q*B2
        return max(abs(x1)/4,abs(x2)/4,abs(x1-x2)/6)
    assert qstar==F(5,8) and epsstar==F(1,16)
    assert radius(qstar)==epsstar
    for k in range(1,51):
        step=F(k,100)
        assert radius(qstar-step)>=epsstar
        assert radius(qstar+step)>=epsstar
    cases=0; feasible=0
    for x,y,z in product(range(4),repeat=3):
        b1x=(F(x,20),F(y,30),F(z,40))
        b2x=(F(z,25),F(x,35),F(y,45))
        cx=F((x+2*y+z)%5,50)
        for q in (F(1,2),F(3,5),F(2,3),F(7,10),
                  F(5,8),F(17,30),F(27,40),F(1,4)):
            feasible+=check_case(A1,A2,B1,B2,b1x,b2x,cx,q)
            cases+=1
    assert cases==512 and feasible==35
    result={
      "schema":"PREFIX781_R6_EXACT_POINTWISE_EQUIVARIANT_CANCELLATION_V1",
      "evidence_status":"AUTHOR_ALGEBRAIC_PROOF_WITH_EXACT_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED",
      "frozen_scientific_input":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
      "scope":"external reflected scalar Gamma-witness algebra; no native X6 comparator attribution",
      "theorem":"At q>0 cancellation iff |xi|<=Si+c (i=1,2) and |x1-x2|<=S1+S2.",
      "pointwise_weighted_distance":"max(|x1|/(S1+c),|x2|/(S2+c),|x1-x2|/(S1+S2)) with zero-denominator conventions",
      "q_window":{"left":ss(win["left"]),"right":ss(win["right"])},
      "worked_example":{"q_cancel":"3/5","q_robust":"1/2",
         "R1_private":[ss(t) for t in b1],
         "R2_private":[ss(t) for t in b2],"common":ss(c),
         "witness":{k:([ss(t) for t in v] if isinstance(v,tuple) else ss(v))
                    for k,v in w.items()}},
      "uniform_recovery":{"qstar":ss(qstar),"epsstar":ss(epsstar),
            "qstar_formula":"(A1+2*A2)/(B1+2*B2)",
            "epsstar_formula":"D/[2*(B1+2*B2)]"},
      "rational_regression":{"cases":cases,"feasible":feasible,
            "infeasible":cases-feasible,
            "arithmetic":"Python fractions.Fraction exact",
            "status":"ALL_CHECKS_PASS PREFIX781 POINTWISE_EQUIVARIANT_CANCELLATION"},
      "open":"Verify native typed observation correspondence and actual per-corner budgets."
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    print("ALL_CHECKS_PASS PREFIX781 POINTWISE_EQUIVARIANT_CANCELLATION")


if __name__=="__main__":
    run()
