#!/usr/bin/env python3
"""Exact 4D early-error lift no-go: full-rank LR convex hull but strict FULL/LR support gap."""
from fractions import Fraction as F
from itertools import product
from math import lcm
A,B,t0,t1=F(49,100),F(1,100),F(1,16),F(1,8)
Q={(0,0):A,(1,0):F(1,2)-A,(0,1):B,(1,1):F(1,2)-B}
RU=(F(3,4),F(5,4)); RV=(F(1,2),F(1),F(3,2))
def k(t,u):
    return (F(1,2)+t,F(1,2)-2*t,t) if u==0 else (t,F(1,2)-2*t,F(1,2)+t)
rows=[(x,u,v, RV[v]*Q[x,u]*k((t0,t1)[x],u)[v],Q[x,u]*k((t0,t1)[x],u)[v]) for x,u,v in product(range(2),range(2),range(3))]
assert len(rows)==12 and all(p>0 and q>0 for x,u,v,p,q in rows)
assert sum(z[3] for z in rows)==sum(z[4] for z in rows)==1

def vec(bits,full):
    ep=eq=tp=tq=F(0)
    for x,u,v,p,q in rows:
        early=(bits>>x)&1
        middle=(bits>>(2+(2*x+u if full else u)))&1
        last=(bits>>(6+6*x+3*u+v if full else 4+v))&1
        tau=2 if not early else (3 if not middle else (4 if not last else 5))
        eps=F(3,4) if tau==2 else F(1,4)
        ep+=eps*p; eq+=eps*q; tp+=tau*p; tq+=tau*q
    return ep,eq,tp,tq

def det4(rows):
    matrix=[list(r) for r in rows]; total=F(1)
    for i in range(4):
        pivot=next((j for j in range(i,4) if matrix[j][i]),None)
        if pivot is None: return F(0)
        if pivot!=i:
            matrix[i],matrix[pivot]=matrix[pivot],matrix[i];total=-total
        d=matrix[i][i];total*=d
        for j in range(i+1,4):
            v=matrix[j][i]/d
            for z in range(i,4): matrix[j][z]-=v*matrix[i][z]
    return total

pts=[vec(b,False) for b in range(128)]
indices=(49,10,66,6)
base=pts[0]
D=det4([[pts[j][k]-base[k] for k in range(4)] for j in indices])
assert D==F(147,2000000)!=0
lam=F(1949,2298)
def H(z):return z[2]-lam*z[3]-2*z[1]
lr_direct=max(H(z) for z in pts)
L=[max(F(0),r-lam) for r in RV]
G={(x,u):RU[u]-lam+sum(k((t0,t1)[x],u)[v]*L[v] for v in range(3)) for x,u in product(range(2),repeat=2)}
g=[Q[x,0]*G[x,0] for x in (0,1)]
Dsource=[Q[x,0]*(RU[0]-lam)+Q[x,1]*(RU[1]-lam+G[x,1]) for x in (0,1)]
Qsource=[sum(Q[x,u] for u in (0,1)) for x in (0,1)]
assert Qsource==[F(1,2),F(1,2)] and g==[F(-49,229800),F(49,229800)]
assert all(Dsource[x]+Qsource[x]>0 and Dsource[x]+Qsource[x]+g[x]>0 for x in (0,1))
base_value=2*(1-lam)-F(3,2)
full=base_value+sum(max(F(0),Dsource[x]+Qsource[x]+max(F(0),g[x])) for x in (0,1))
lr=base_value+max(sum(max(F(0),Dsource[x]+Qsource[x]+h*g[x]) for x in (0,1)) for h in (0,1))
assert lr==lr_direct==F(871,2298)
assert full==F(87149,229800) and full-lr==F(49,229800)

# Independent complete enumeration of all 2^18 FULL deterministic policies.
den=lcm(*(z.denominator for row in rows for z in row[3:]))
a,b=lam.numerator,lam.denominator
introws=[(x,u,v,int(p*den),int(q*den)) for x,u,v,p,q in rows]
max_int=None; argmax=None
for bits in range(1<<18):
    value=0
    for x,u,v,p,q in introws:
        early=(bits>>x)&1;middle=(bits>>(2+2*x+u))&1;last=(bits>>(6+6*x+3*u+v))&1
        tau=2 if not early else (3 if not middle else (4 if not last else 5))
        value+=2*tau*(b*p-a*q)-(3 if tau==2 else 1)*b*q
    if max_int is None or value>max_int:
        max_int=value;argmax=bits
assert F(max_int,2*den*b)==full

# Explicit FULL witness: early CONTINUE; U=1 CONTINUE; X=1,U=0 CONTINUE.
# At time4 STOP for V=0, CONTINUE for V=1,2.
TP=TQ=F(0)
for x,u,v,p,q in rows:
    middle=(u==1 or x==1)
    tau=3 if not middle else (4 if v==0 else 5)
    TP+=tau*p;TQ+=tau*q
witness=(F(1,4),F(1,4),TP,TQ)
assert witness==(F(1,4),F(1,4),F(13539,3200),F(6323,1600))
assert H(witness)==full
assert (full-lr)/(F(1)+lam+F(2))==F(49,884300)
print('FULL_POLICIES',1<<18,'LR_POLICIES',128,'LR_UNIQUE_OBSERVATIONS',len(set(pts)))
print('RANK4_LR_VERTEX_INDICES',indices,'DETERMINANT',D)
print('DIRECTION H=TP-(1949/2298)TQ-2eQ')
print('EXACT_SUPPORT_FULL',full,'EXACT_SUPPORT_LR',lr,'EXACT_GAP',full-lr)
print('FULL_WITNESS',witness,'LINFINITY_DISTANCE_LOWER_BOUND',F(49,884300))
print('PASS_EXACT_R5_2D_HULL_EQUAL_RANK4_EARLY_ERROR_LIFT_NO_GO')
