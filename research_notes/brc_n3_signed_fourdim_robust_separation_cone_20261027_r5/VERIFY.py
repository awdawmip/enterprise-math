#!/usr/bin/env python3
"""Exact rational N=3 BRC two-measure decision tree; author-level UNREVIEWED."""
from fractions import Fraction as F
z=F(0)
first={"A":F(1,2),"B":F(1,2)}
r2={"C":F(1),"L":F(1,4),"H":F(7,4)}
q2={"C":F(1,2),"L":F(1,4),"H":F(1,4)}
term={
"A":{"C":[(F(1,4),F(2,5)),(F(1),F(1,5)),(F(7,4),F(2,5))],
     "L":[(F(1,4),F(1))],"H":[(F(7,4),F(1))]},
"B":{"C":[(F(1,4),F(1,20)),(F(1),F(9,10)),(F(7,4),F(1,20))],
     "L":[(F(1,4),F(1))],"H":[(F(7,4),F(1))]}}
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),z)
def zero():return (z,z,z,z)
def obs(q,r,t,d):
    return (q*r if d=="Q" else z,q if d=="P" else z,q*r*t,q*t)
def stop(q,r,t,l):
    return obs(q,r,t,"Q" if l[0]*r<l[1] else "P")
def options(pre,child,l):
    q=first[pre]*q2[child]
    s=stop(q,r2[child],2,l)
    c=zero()
    for r,p in term[pre][child]:
        c=add(c,stop(q*p,r,3,l))
    return s,c
def full(l):
    out=zero();acts=[]
    for pre in ("A","B"):
        s1=stop(first[pre],F(1),1,l)
        cont=zero();selected={}
        for child in ("C","L","H"):
            s,c=options(pre,child,l)
            selected[child]="T3" if dot(c,l)<dot(s,l) else "STOP"
            cont=add(cont,c if selected[child]=="T3" else s)
        if dot(cont,l)<dot(s1,l):
            out=add(out,cont);acts.append((pre,"T2",selected))
        else:
            out=add(out,s1);acts.append((pre,"STOP",None))
    return out,acts
def lr(l):
    s1=stop(F(1),F(1),1,l)
    cont=zero();selected={}
    for child in ("C","L","H"):
        ss,cc=zero(),zero()
        for pre in ("A","B"):
            s,c=options(pre,child,l);ss=add(ss,s);cc=add(cc,c)
        selected[child]="T3" if dot(cc,l)<dot(ss,l) else "STOP"
        cont=add(cont,cc if selected[child]=="T3" else ss)
    if dot(cont,l)<dot(s1,l):return cont,("T2",selected)
    return s1,("STOP",None)
EF=(F(7,80),F(13,20),F(9,4),F(9,4))
EL=(F(29,320),F(51,80),F(5,2),F(5,2))
def check(l):
    a,b,u,v=l;D=4*b-a;c=u+v
    assert a>0 and a/4<b<a and u/4+v>0 and 7*u/4+v>0 and D/80<c<9*D/160
    f,fa=full(l);p,pa=lr(l)
    assert (f,p)==(EF,EL),(l,f,p)
    assert [x[1] for x in fa]==["T2","T2"]
    assert [x[2]["C"] for x in fa]==["T3","STOP"]
    assert all(x[2]["L"]==x[2]["H"]=="STOP" for x in fa)
    assert pa==("T2",{"C":"T3","L":"STOP","H":"STOP"})
    diff=dot(p,l)-dot(f,l)
    assert diff==c/4-D/320 and diff>0
    return dot(f,l),dot(p,l),diff
assert sum(first.values(),z)==1 and sum(q2.values(),z)==1
for pre in first:
    assert sum(q2[c]*r2[c] for c in q2)==1
    for child in q2:
        assert sum(p for r,p in term[pre][child])==1
        assert sum(p*r for r,p in term[pre][child])==r2[child]
        assert all(p>0 and r>0 for r,p in term[pre][child])
assert sum(first[p]*q2[c]*w for p in first for c in q2 for r,w in term[p][c])==1
assert sum(first[p]*q2[c]*w*r for p in first for c in q2 for r,w in term[p][c])==1
assert sum(len(term[p][c]) for p in first for c in q2)==10
print("TREE: positive 10 leaves, P=Q=1, martingales PASS")
print("O_FULL",EF)
print("O_LR",EL)
for name,l in {
 "star":(F(1),F(63,64),F(0),F(1,16)),
 "signed_u":(F(1),F(63,64),F(-1,128),F(9,128)),
 "signed_v":(F(1),F(63,64),F(1,10),F(-1,50))}.items():
    print(name,"costs_gap",check(l))
count=0
for b in [F(1,2),F(3,4),F(7,8),F(63,64)]:
    D=4*b-1
    for k in [F(1,6),F(1,3),F(2,3),F(5,6)]:
        c=(F(1,80)+k*(F(9,160)-F(1,80)))*D
        for j in [F(-1,10),F(0),F(1,10)]:
            check((F(1),b,j*c,(1-j)*c));count+=1
assert count==48
print("RATIONAL_INTERIOR_CHECKS",count,"PASS")
print("ALL EXACT CHECKS PASSED")
