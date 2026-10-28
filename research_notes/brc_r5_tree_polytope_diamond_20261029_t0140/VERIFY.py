#!/usr/bin/env python3
"""Exact rational regression witness for finite no-reconvergence decision-tree lemma.

This is a scientific auxiliary calculation in a finite two-measure experiment;
not a native X6 / Heartbeat physics simulator or a formal proof checker.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from random import Random

S = (F(1,2), F(1), F(3,2), F(5,2))
ORIGINS = ("A", "B")
A = {"A":F(1,4), "B":F(1,4)}
OUTSIDE_Q = F(1,2)
ROOT = {
    "A": (F(7,50),F(11,75),F(1,2),F(16,75)),
    "B": (F(17,200),F(23,150),F(3,5),F(97,600)),
}
KERNEL = {
    ("A", "left"): (F(1,2),F(1,6),F(1,4),F(1,12)),
    ("B", "left"): (F(5,12),F(1,3),F(1,6),F(1,12)),
    ("A", "right"): (F(17,100),F(23,75),F(1,5),F(97,300)),
    ("B", "right"): (F(31,120),F(5,18),F(1,15),F(143,360)),
}
NODE = {S[1]:"left",S[2]:"right"}


def kernel_check(k, r):
    assert len(k)==len(S)
    assert all(p>0 for p in k)
    assert sum(k)==1 and sum(p*s for p,s in zip(k,S))==r
    # P-kernel probability at signature s is (s/r)*q(s).
    assert sum(s*p/r for p,s in zip(k,S))==1


def terminal_Q(alpha):
    """Aggregate Q mass by (termination-time, observed terminal LR)."""
    d=defaultdict(F)
    d[(1,S[0])]+=OUTSIDE_Q
    for i in ORIGINS:
        a=A[i]
        d[(1,S[2])]+=a*(1-alpha["root"])
        for s,q in zip(S,ROOT[i]):
            flow=a*alpha["root"]*q
            if s not in NODE:
                d[(2,s)]+=flow
            else:
                name=NODE[s]
                d[(2,s)]+=flow*(1-alpha[name])
                for s3,q3 in zip(S,KERNEL[(i,name)]):
                    d[(3,s3)]+=flow*alpha[name]*q3
    d={key:v for key,v in d.items() if v}
    assert sum(d.values())==1
    assert sum(s*v for (_,s),v in d.items())==1
    return d


def declaration(theta,t,s):
    j=S.index(s)+1
    return F(t+j,12) if theta==1 else F(2*t+j,13)


def observables(W,m):
    assert set(m).issubset(W)
    assert all(F(0)<=val<=W[key] for key,val in m.items())
    x=sum(s*val for (_,s),val in m.items())
    y=sum(m.values())
    TP=sum(t*s*val for (t,s),val in W.items())
    TQ=sum(t*val for (t,s),val in W.items())
    return (1-x,y,TP,TQ)


def interp(x,y,omega):return omega*x+(1-omega)*y


def format_q(x):return str(x)


def deterministic_vertices():
    policies=[{"root":F(0),"left":F(0),"right":F(0)}]
    for a,b in product((F(0),F(1)), repeat=2):
        policies.append({"root":F(1),"left":a,"right":b})
    return [terminal_Q(p) for p in policies]


def policy_as_vertices(alpha):
    """Weights for stop-root and continue-root with each pair of binary child decisions."""
    a=alpha["root"]
    left,right=alpha["left"],alpha["right"]
    return (1-a, a*(1-left)*(1-right), a*(1-left)*right,
            a*left*(1-right), a*left*right)


def check_vertex_decomposition(alpha, V):
    W=terminal_Q(alpha)
    c=policy_as_vertices(alpha)
    assert len(c)==len(V)==5 and sum(c)==1 and all(x>=0 for x in c)
    keys=set(W).union(*(set(w) for w in V))
    assert all(W.get(key,F(0))==sum(c[k]*V[k].get(key,F(0)) for k in range(5)) for key in keys)


def main():
    for i in ORIGINS:
        kernel_check(ROOT[i],F(3,2))
        kernel_check(KERNEL[(i,"left")],F(1))
        kernel_check(KERNEL[(i,"right")],F(3,2))
    assert sum(A.values())+OUTSIDE_Q==1
    assert sum(A.values())*F(3,2)+OUTSIDE_Q*S[0]==1

    L1={"root":F(1,2), "left":F(1,4), "right":F(3,4)}
    L2={"root":F(3,4), "left":F(3,5), "right":F(1,5)}
    omega=F(2,5)
    # Common prefix-flow variables root, root*left, root*right.
    u1=(L1["root"],L1["root"]*L1["left"],L1["root"]*L1["right"])
    u2=(L2["root"],L2["root"]*L2["left"],L2["root"]*L2["right"])
    u=tuple(interp(x,y,omega) for x,y in zip(u1,u2))
    assert u==(F(13,20),F(8,25),F(6,25))
    Lmix={"root":u[0],"left":u[1]/u[0],"right":u[2]/u[0]}
    assert Lmix=={"root":F(13,20),"left":F(32,65),"right":F(24,65)}
    W1,W2,Wmix=[terminal_Q(p) for p in (L1,L2,Lmix)]
    keys=set(W1)|set(W2)|set(Wmix)
    assert all(Wmix.get(key,F(0))==interp(W1.get(key,F(0)),W2.get(key,F(0)),omega) for key in keys)
    m1={key:val*declaration(1,*key) for key,val in W1.items()}
    m2={key:val*declaration(2,*key) for key,val in W2.items()}
    mm={key:interp(m1.get(key,F(0)),m2.get(key,F(0)),omega) for key in keys}
    theta_mix={key:mm[key]/Wmix[key] for key in Wmix}
    assert all(F(0)<=p<=F(1) for p in theta_mix.values())
    O1,O2,Om=[observables(W,m) for W,m in ((W1,m1),(W2,m2),(Wmix,mm))]
    assert Om==tuple(interp(x,y,omega) for x,y in zip(O1,O2))
    assert len(theta_mix)==len(Wmix)

    # One additional continuation level produces a true observable diamond:
    # parent ratios 1 and 3/2 can both continue to time-3 ratio 3/2.
    # The two incoming SOURCE vectors differ in direction.
    v={i:A[i]*ROOT[i][1]*KERNEL[(i,"left")][2] for i in ORIGINS}
    w={i:A[i]*ROOT[i][2]*KERNEL[(i,"right")][2] for i in ORIGINS}
    det=v["A"]*w["B"]-v["B"]*w["A"]
    assert (v["A"],v["B"],w["A"],w["B"])==(F(11,1200),F(23,3600),F(1,40),F(1,100))
    assert det==F(-49,720000)
    # Midpoint of feasible source-resolved flow choices (v,v) and (w,0).
    # In the midpoint x=(v+w)/2 and y=v/2; at a merged LR state
    # any shared local continuation probability must enforce y=gamma*x.
    x={i:(v[i]+w[i])/2 for i in ORIGINS}
    y={i:v[i]/2 for i in ORIGINS}
    assert y["A"]*x["B"]-y["B"]*x["A"]==F(-49,2880000)

    V=deterministic_vertices()
    rng=Random(20261029)
    for _ in range(600):
        a={name:F(rng.randint(0,29),29) for name in ("root","left","right")}
        check_vertex_decomposition(a,V)
    check_vertex_decomposition(Lmix,V)

    print("MODEL: 2 hidden origins; root ratio 3/2; two nonterminal child ratios 1 and 3/2; no merge")
    print("P/Q kernel normalization and all branch positivity: PASS")
    print("INITIAL: Q origin masses A=B=1/4, outside=1/2 at LR=1/2; P totals 1")
    print("EXACT MIXED PREFIX-FLOW (root,left,right):",", ".join(map(format_q,u)))
    print("EXACT MIXED BEHAVIOR (root,left,right):",", ".join(str(Lmix[n]) for n in ("root","left","right")))
    print("O1 (eP,eQ,TP,TQ):",", ".join(map(str,O1)))
    print("O2 (eP,eQ,TP,TQ):",", ".join(map(str,O2)))
    print("O_mix:",", ".join(map(str,Om)))
    print("MIXED POLICY TERMINAL DECLARATION COINS:")
    for key in sorted(theta_mix):print("  time",key[0],"ratio",key[1],"theta_P",theta_mix[key])
    print("DIAMOND INCOMING SOURCE VECTORS: left=",v["A"],v["B"],"right=",w["A"],w["B"])
    print("DIAMOND TWO-PARENT DETERMINANT:",det)
    print("DIAMOND MIDPOINT SHARED-CONTINUATION OBSTRUCTION:",y["A"]*x["B"]-y["B"]*x["A"])
    print("VOLUME: 600 random exact-rational policies + one chosen mixture checked against 5 deterministic flow vertices")
    print("PASS_EXACT_R5_NO_RECONVERGENCE_POLYTOPE")

if __name__=="__main__": main()
