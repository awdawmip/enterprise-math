#!/usr/bin/env python3
"""R749SSK exact two-read collision witness; Python standard library only."""
from fractions import Fraction as F
import json

W=(1,1,2,3,6)
def counts(N):
    a=[0]*(N+1); a[0]=1
    for w in W:
        for n in range(w,N+1):
            a[n]+=a[n-w]
    C=[0]*(N+1); T=[0]*(N+1)
    for q in range(1,N+1):
        C[q]=C[q-1]+a[q-1]
        T[q]=T[q-1]+C[q-1]
    return C,T
C,T=counts(30)

def S(q): return 18*q**4+54*q**3-345*q**2+2070*q-16315
def X(q,e=F(0),d=F(0)): return (F(T[q])+e)/(F(C[q])+d)
def Y(q,e=F(0),d=F(0)): return q**3*X(q,e,d)-F(S(q),108)
def pair(q,e,d): return (Y(q,e,d),Y(q+6,e,d))

def inverse(p,y0,y1):
    x0=(y0+F(S(p),108))/p**3
    x1=(y1+F(S(p+6),108))/(p+6)**3
    assert x0!=x1
    d=(T[p+6]-T[p]-x1*C[p+6]+x0*C[p])/(x1-x0)
    e=x0*(C[p]+d)-T[p]
    return e,d

def fixed_d_numerators(q,p,d):
    a=F(q**3,C[q]+d); b=F((q+6)**3,C[q+6]+d)
    A=F(p**3,C[p]+d); B=F((p+6)**3,C[p+6]+d)
    k0=Y(p,0,d)-Y(q,0,d)
    k1=Y(p+6,0,d)-Y(q+6,0,d)
    det=b*A-a*B
    assert det!=0
    return (k1*A-k0*B)/det,(a*k1-b*k0)/det

def J(q,e,d):
    return F(q**3*(q+6)**3,1)*(X(q,e,d)-X(q+6,e,d))/((C[q]+d)*(C[q+6]+d))

assert [(C[q],T[q]) for q in (6,7,8,12,13,14)]==[(41,50),(65,91),(98,156),(380,881),(506,1261),(662,1767)]
y0,y1=pair(6,F(0),F(0))
assert (y0,y1)==(F(400643,4428),F(690461,10260))
e7,d7=inverse(7,y0,y1)
assert (e7,d7)==(F(445301541473,452834122344),-F(16718273227,37736176862))
assert all(-2<v<2 for v in (e7,d7))
assert pair(7,e7,d7)==(y0,y1)
assert J(6,F(0),F(0)) and J(7,e7,d7)
e6,e8=fixed_d_numerators(6,8,F(-1))
assert (e6,e8)==(-F(96083110,75133251),F(20416063,33392556))
assert all(-2<v<2 for v in (e6,e8))
bpair=pair(6,e6,F(-1))
assert bpair==pair(8,e8,F(-1))
assert bpair==(F(9031928401,100177668),F(7216422841,100177668))
gap_a=Y(18,F(0),F(0))-Y(19,e7,d7)
gap_b=Y(18,e6,F(-1))-Y(20,e8,F(-1))
assert gap_a==F(2499325179139188767,1219962360222318330)
assert gap_b==F(321813705516,162895381165)
assert gap_a>0 and gap_b>0

out={
 "schema":"R749SSK_EXACT_TWO_READ_COLLISION_V1",
 "status":"PASS",
 "method":"exact integer coin-change and fractions.Fraction",
 "anchors":{str(q):{"C":C[q],"T":T[q]} for q in (6,7,8,12,13,14)},
 "A":{"q":6,"p":7,"q_errors":["0","0"],"p_errors":[str(e7),str(d7)],
      "two_reads":[str(y0),str(y1)],"jacobians":[str(J(6,F(0),F(0))),str(J(7,e7,d7))],
      "third_gap":str(gap_a)},
 "B":{"q":6,"p":8,"same_known_d":"-1","numerator_errors":[str(e6),str(e8)],
      "two_reads":[str(x) for x in bpair],"third_gap":str(gap_b)},
 "scope":"two exact continuous-error cutoff collisions, local open overlap, and two exact third-read separations",
 "unresolved":["three-read global injectivity", "unknown-cutoff integer-error injectivity", "BRC type preservation"]
}
with open("R749SSK_UNKNOWN_CUTOFF_COLLISION_RESULTS.json","w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=2,sort_keys=True)
    f.write("\n")
print("PASS",out["A"],out["B"])
