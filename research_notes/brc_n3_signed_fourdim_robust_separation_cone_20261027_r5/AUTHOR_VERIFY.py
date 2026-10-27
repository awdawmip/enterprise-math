#!/usr/bin/env python3
"""Exact finite BRC two-measure decision tree certificate; author-level UNREVIEWED.

Model: two first-stage histories A,B, each Q=P=1/2. At stage two,
children C,L,H have Q transition (1/2,1/4,1/4) and LR (1,1/4,7/4).
At common C the Q terminal LR kernel differs by predecessor, while L/H
end in one child retaining LR. Signed objectives use O=(eP,eQ,EP tau,EQ tau).
"""
from fractions import Fraction as F
from itertools import product

z=F(0)
q_first={"A":F(1,2),"B":F(1,2)}
r2={"C":F(1),"L":F(1,4),"H":F(7,4)}
qc2={"C":F(1,2),"L":F(1,4),"H":F(1,4)}
terminal={
  "A":{"C":[(F(1,4),F(2,5)),(F(1),F(1,5)),(F(7,4),F(2,5))],"L":[(F(1,4),F(1))],"H":[(F(7,4),F(1))]},
  "B":{"C":[(F(1,4),F(1,20)),(F(1),F(9,10)),(F(7,4),F(1,20))],"L":[(F(1,4),F(1))],"H":[(F(7,4),F(1))]}
}


def dot(a,b): return sum((x*y for x,y in zip(a,b)), z)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(k,v): return tuple(k*x for x in v)
def zero(): return (z,z,z,z)
def basic(q,r,t,decision):
    return (q*r if decision=="Q" else z,
            q if decision=="P" else z,
            q*r*t,q*t)
def pred(lam,r):
    x,y=lam[0]*r,lam[1]
    return "Q" if x<y else "P"
def cost(v,lam):return dot(v,lam)

def stop(q,r,t,lam): return basic(q,r,t,pred(lam,r))
def stage3(pre,child,lam):
    q=q_first[pre]*qc2[child]
    total=zero()
    for (r,p) in terminal[pre][child]:
        total=add(total,stop(q*p,r,3,lam))
    return total

def option2(pre,child,lam):
    q=q_first[pre]*qc2[child]
    return stop(q,r2[child],2,lam),stage3(pre,child,lam)

def full_opt(lam):
    out=zero(); acts=[]
    for pre in ("A","B"):
        fst_stop=stop(q_first[pre],F(1),1,lam)
        cont=zero()
        chacts={}
        for child in ("C","L","H"):
            s,c=option2(pre,child,lam)
            chacts[child]="T3" if cost(c,lam)<cost(s,lam) else "STOP"
            cont=add(cont,c if chacts[child]=="T3" else s)
        if cost(cont,lam)<cost(fst_stop,lam):
            out=add(out,cont);acts.append((pre,"T2",chacts))
        else:
            out=add(out,fst_stop);acts.append((pre,"STOP",None))
    return out,acts

def lr_opt(lam):
    first_stop=stop(F(1),F(1),1,lam)
    cont=zero();chacts={}
    for child in ("C","L","H"):
        ss,cc=zero(),zero()
        for pre in ("A","B"):
            s,c=option2(pre,child,lam)
            ss=add(ss,s);cc=add(cc,c)
        chacts[child]="T3" if cost(cc,lam)<cost(ss,lam) else "STOP"
        cont=add(cont, cc if chacts[child]=="T3" else ss)
    if cost(cont,lam)<cost(first_stop,lam):return cont,("T2",chacts)
    return first_stop,("STOP",None)

def d_value(lam): return 4*lam[1]-lam[0]
def cone(lam):
    l1,l2,l3,l4=lam;D=d_value(lam);c=l3+l4
    return bool(l1>0 and l1/4<l2<l1 and
           l3/4+l4>0 and 7*l3/4+l4>0 and D/80<c<9*D/160)


def expected():
    return (F(7,80),F(13,20),F(9,4),F(9,4)),\
           (F(29,320),F(51,80),F(5,2),F(5,2))

def vector_check(lam):
    assert cone(lam)
    full,fa=full_opt(lam);lr,la=lr_opt(lam)
    ef,el=expected()
    assert full==ef and lr==el,(full,lr)
    assert [x[1] for x in fa]==["T2","T2"]
    assert [x[2]["C"] for x in fa]==["T3","STOP"]
    assert [x[2]["L"] for x in fa]==["STOP","STOP"]
    assert [x[2]["H"] for x in fa]==["STOP","STOP"]
    assert la==("T2",{"C":"T3","L":"STOP","H":"STOP"})
    gap=cost(lr,lam)-cost(full,lam)
    predicted=(lam[2]+lam[3])/4-d_value(lam)/320
    assert gap==predicted and gap>0,(gap,predicted)
    return cost(full,lam),cost(lr,lam),gap


def verify_tree():
    assert sum(q_first.values(),z)==1
    for pre in ("A","B"):
        assert sum(qc2.values(),z)==1
        assert sum((qc2[c]*r2[c] for c in qc2),z)==1
        for child in ("C","L","H"):
            ker=terminal[pre][child]
            assert sum((p for r,p in ker),z)==1
            assert all(p>0 and r>0 for r,p in ker)
            assert sum((p*r for r,p in ker),z)==r2[child]
    qleaf=sum((q_first[a]*qc2[c]*p for a in q_first for c in qc2 for r,p in terminal[a][c]),z)
    pleaf=sum((q_first[a]*qc2[c]*p*r for a in q_first for c in qc2 for r,p in terminal[a][c]),z)
    assert pleaf==qleaf==1
    assert sum(len(terminal[a][c]) for a in q_first for c in qc2)==10

if __name__=="__main__":
    verify_tree()
    ef,el=expected();print("TREE: 10 strictly positive leaves, Q=P=1, LR martingales: PASS")
    print("EXPECTED_FULL_O:",tuple(map(str,ef)))
    print("EXPECTED_LR_O:  ",tuple(map(str,el)))
    print("LR_MINUS_FULL_O:",tuple(str(b-a) for a,b in zip(ef,el)))
    testcases={
      "tie_free_star":(F(1),F(63,64),F(0),F(1,16)),
      "negative_EP_time_weight":(F(1),F(63,64),F(-1,128),F(9,128)),
      "negative_EQ_time_weight":(F(1),F(63,64),F(1,10),F(-1,50)),
    }
    for name,lam in testcases.items():
        a,b,c=vector_check(lam)
        print(name,"lambda",tuple(map(str,lam)),"full",a,"LR",b,"gap",c)
    # Rational interior samples: direct finite Bellman cross-check; not a universal proof.
    n=0
    for l2 in [F(1,2),F(3,4),F(7,8),F(63,64)]:
        D=4*l2-1
        for k in [F(1,6),F(1,3),F(2,3),F(5,6)]:
            c=D/F(80)+k*(F(9,160)-F(1,80))*D
            for p in [F(-1,10),F(0),F(1,10)]:
                # parameterize lambda3 relative to c; ensures c_L,c_H positive
                l3=p*c; l4=c-l3
                lam=(F(1),l2,l3,l4)
                vector_check(lam);n+=1
    print("RATIONAL_CHAMBER_POINTS:",n,"PASS")
    # Closure: lower collision boundary c=d_B yields zero gap for the candidate vectors.
    D=F(47,16);boundary=D/80
    lb=(F(1),F(63,64),F(0),boundary)
    assert (lb[2]+lb[3])/4-D/320==0
    print("LOWER_FACE_GAP=0: PASS")
    print("ALL EXACT CHECKS PASSED")
