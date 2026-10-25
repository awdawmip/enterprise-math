#!/usr/bin/env python3
"""Exact author checker for the external iid N14 Stage107 affine theorem.
No native P000/X6 mapping or independent mathematical acceptance implied.
"""
from fractions import Fraction as F

P = (F(1,8),F(1,24),F(5,6))
Q = (F(1,12),F(1,12),F(5,6))
A,B=(10,3,0),(12,0,1)
K,PREV=F(778896,767),F(107892,101)
L=72+F(8,9)*K
alpha0=F(646648605512624167,1862537719238885376)
V0=F(6009214469256084569,465634429809721344)
s0=F(4106591957559179,5222400000000000)

def states():
    for n in range(14,-1,-1):
        for a in range(n+1):
            for b in range(n-a+1):
                yield (n,a,b)

def children(z):
    n,a,b=z
    return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))

def likelihood(z):
    return F(2**(z[1]+z[2]),3**z[1])

def bell(k):
    ell=72+F(8,9)*k
    d,choices,gaps={},{},{}
    for z in states():
        costs={'P':k*likelihood(z),'Q':ell}
        if z[0]<14:
            costs['C']=1+sum((P[i]*d[v] for i,v in enumerate(children(z))),F())
        m=min(costs.values())
        d[z]=m
        choices[z]=tuple(act for act,val in costs.items() if val==m)
        gaps[z]={act:val-m for act,val in costs.items()}
    return d,choices,gaps

D,opts,gaps=bell(K)
assert len(D)==680
assert sum(len(row)-1 for row in gaps.values())==1240
assert sum(v>0 for row in gaps.values() for v in row.values())==1238
assert all(v>=0 for row in gaps.values() for v in row.values())
assert {z for z in opts if len(opts[z])>1}=={A,B}
assert opts[A]==('P','C') and opts[B]==('Q','C')
assert min(v for row in gaps.values() for v in row.values() if v>0)==F(12607,331344)
assert D[0,0,0]==F(14787165590378589778037,21008329862591545344)
policy={z:('C' if z==A else 'Q' if z==B else opts[z][0]) for z in opts}

def pinned(k):
    d={};ell=72+F(8,9)*k;minimum=F(0)
    for z in states():
        costs={'P':k*likelihood(z),'Q':ell}
        if z[0]<14:
            costs['C']=1+sum((P[i]*d[v] for i,v in enumerate(children(z))),F())
        d[z]=costs[policy[z]]
        minimum=min(minimum,*[v-d[z] for v in costs.values()])
    return minimum
assert pinned(K)==pinned(PREV)==0

# Prefix branch multiplicity and exact positive mass before either tie.
count={(0,0,0):1}
pm={(0,0,0):F(1)}
qm={(0,0,0):F(1)}
for n in range(14):
    for a in range(n+1):
        for b in range(n-a+1):
            z=(n,a,b)
            if z not in count or z in (A,B) or policy[z]!='C':
                continue
            for i,w in enumerate(children(z)):
                count[w]=count.get(w,0)+count[z]
                pm[w]=pm.get(w,F())+pm[z]*P[i]
                qm[w]=qm.get(w,F())+qm[z]*Q[i]
assert (count[A],pm[A],qm[A])==(120,F(390625,5971968),F(390625,20155392))
assert (count[B],pm[B],qm[B])==(12,F(48828125,725594112),F(48828125,362797056))

# Suffix tuple: P-error, Q-error, incremental times, terminal words.
strict={}
for z in states():
    action=policy[z]
    if action=='P':
        strict[z]=(F(0),F(1),F(0),F(0),1)
    elif action=='Q':
        strict[z]=(F(1),F(0),F(0),F(0),1)
    else:
        w=[strict[v] for v in children(z)]
        strict[z]=(sum((P[i]*w[i][0] for i in range(3)),F()),
                   sum((Q[i]*w[i][1] for i in range(3)),F()),
                   1+sum((P[i]*w[i][2] for i in range(3)),F()),
                   1+sum((Q[i]*w[i][3] for i in range(3)),F()),
                   sum(v[4] for v in w))

def suffix(z):
    w=[strict[v] for v in children(z)]
    return (sum((P[i]*w[i][0] for i in range(3)),F()),
            sum((Q[i]*w[i][1] for i in range(3)),F()),
            1+sum((P[i]*w[i][2] for i in range(3)),F()),
            1+sum((Q[i]*w[i][3] for i in range(3)),F()),
            sum(v[4] for v in w))

a,b=suffix(A),suffix(B)
assert a==(F(635,165888),F(10201,10368),F(7711,6912),F(1069,864),21)
assert b==(F(63,64),F(1,144),F(9,8),F(13,12),5)
assert A[0]<B[0] and A[1]>B[1]  # cones cannot meet

x=-pm[A]*a[0]
y=qm[A]*(1-a[1])
e=pm[B]*(1-b[0])
f=-qm[B]*b[1]
c=(y-x)/(e-f)
eta=x+e*c
u1=(1-s0)/c
assert (x,y,e,f)==(F(-248046875,990677827584),
                   F(65234375,208971104256),
                   F(48828125,46438023168),
                   F(-48828125,52242776064))
assert c==F(38521,136000) and eta==y+f*c==F(299609375,6315571150848)
assert 0<u1<1 and u1==F(1115808042440821,1479206400000000)
assert eta*u1==F(855824768552109707,23915605160933701189632)

def outcome(u,s):
    m={}
    for z in states():
        choices=({'P':u,'C':1-u} if z==A else
                 {'Q':s,'C':1-s} if z==B else {policy[z]:F(1)})
        row=[F() for _ in range(4)]
        for act,weight in choices.items():
            if weight==0:
                continue
            if act=='P':
                out=(F(0),F(1),F(0),F(0))
            elif act=='Q':
                out=(F(1),F(0),F(0),F(0))
            else:
                w=[m[v] for v in children(z)]
                out=(sum((P[i]*w[i][0] for i in range(3)),F()),
                     sum((Q[i]*w[i][1] for i in range(3)),F()),
                     1+sum((P[i]*w[i][2] for i in range(3)),F()),
                     1+sum((Q[i]*w[i][3] for i in range(3)),F()))
            for i in range(4):
                row[i]+=weight*out[i]
        m[z]=tuple(row)
    return m[0,0,0]

lo=outcome(F(0),s0)
hi=outcome(u1,F(1))
mid=outcome(u1/2,(s0+1)/2)
assert lo==(alpha0,alpha0,V0,F(5708989891929406961,465634429809721344))
alpha1=F(91588670614917102449,263775056922062880768)
V1=F(13541383133505475882195,1055100227688251523072)
assert hi==(alpha1,alpha1,V1,F(805267616960628807535,65943764230515720192))
assert alpha1==alpha0+eta*u1
assert V1==V0-(K+L)*eta*u1
assert mid==tuple((a+b)/2 for a,b in zip(lo,hi))
assert lo[2]>lo[3] and hi[2]>hi[3]
assert D[0,0,0]==V0+(K+L)*alpha0==V1+(K+L)*alpha1
print('PASS_STAGE107 EXACT AUTHOR CHECK',alpha1,V1,'delta',eta*u1,'u_end',u1)
