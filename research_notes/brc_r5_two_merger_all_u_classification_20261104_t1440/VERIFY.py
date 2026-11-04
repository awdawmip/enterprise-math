"""Exact all-u source-route two-merger separator; stdlib Fraction only."""
from fractions import Fraction as F
from itertools import product
Z=F(0); I=F(1); H=F(1,2)
S=('A','B'); T=('L','R'); J=tuple(product(S,T))
R=(H,I,F(3,2)); RR={'L':F(1,3),'R':F(5,3)}
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def obs(q,r,t,a):return (q*r if a=='Q' else Z,q if a=='P' else Z,t*q*r,t*q)
def dot(n,v):return sum((a*b for a,b in zip(n,v)),Z)
def run(u,root,side,merge,term):
    out=(Z,)*4
    for s in S:
        if root[s]!='C':out=add(out,obs(H,I,1,root[s]))
    for s,route in J:
        if root[s]!='C':continue
        q=F(1,4)
        out=add(out,obs(q*F(3,4),RR[route],3,side[s,route]))
        a=merge[s,route]
        if a!='C':out=add(out,obs(q/4,I,3,a))
        else:
            for r,p in zip(R,(u[s,route],I-2*u[s,route],u[s,route])):
                out=add(out,obs(q*p/4,r,4,term[s,route,r]))
    return out

def check(us):
    u=dict(zip(J,us));assert len(u)==4 and all(Z<x<H for x in us)
    a=min(us);b=max(us);t=(a+b)/2;lam=t/10
    assert Z<lam<F(1,20)
    n=(I,F(3,5),-lam,Z)
    root={s:'C' for s in S}
    side={j:('P' if j[1]=='L' else 'Q') for j in J}
    merge={j:('C' if u[j]>t else 'Q') for j in J}
    term={(s,route,r):('P' if r==H else 'Q') for s,route in J for r in R}
    w=run(u,root,side,merge,term)
    vals=[]
    for t1,l,r,m,ds in product(('P','Q','C'),('P','Q'),('P','Q'),('P','Q','C'),product(('P','Q'),repeat=3)):
        rt={s:t1 for s in S};sd={j:(l if j[1]=='L' else r) for j in J}
        mg={j:m for j in J}
        td={(s,route,rr):ds[i] for s,route in J for i,rr in enumerate(R)}
        vals.append(dot(n,run(u,rt,sd,mg,td)))
    assert len(vals)==288
    sidev=F(17,20)-F(9,4)*lam
    stop=I-3*lam
    cont=lambda x:I+x/10-4*lam
    hf=sidev+sum((max(stop,cont(x))/16 for x in us),Z)
    hl=sidev+max(stop,cont(sum(us,Z)/4))/4
    gap=(sum((max(Z,x-t) for x in us),Z)-max(Z,sum(us,Z)-4*t))/160
    assert max(vals)==hl and dot(n,w)==hf and hf-hl==gap
    assert (gap>0)==(a<b)
    dist=gap/sum((abs(x) for x in n),Z)
    return (tuple(us),n,w,hf,hl,gap,dist,len(vals))

cases={
 'same_side_high':(F(5,32),F(6,32),F(7,32),F(8,32)),
 'all_low':(F(1,32),F(2,32),F(3,32),F(4,32)),
 'mixed':(F(1,32),F(3,32),F(13,32),F(15,32)),
 'near_half':(F(13,32),F(14,32),F(15,32),F(31,64)),
 'equal':(F(1,4),)*4}
for name,us in cases.items():
    result=check(us)
    print(name,'u,n,W,HF,HL,gap,dist,LR_count=',result)
    if name=='same_side_high':
        assert result[5]==F(1,2560) and result[6]==F(1,4148)
    if name=='equal':assert result[5]==0
print('PASS_EXACT_R5_TWO_MERGER_ALL_U_FOUR_PARAMETER_CERTIFICATE')
