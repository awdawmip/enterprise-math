#!/usr/bin/env python3
"""Exact rational verification of the R5 S-escape optimal face and observer fiber."""
from fractions import Fraction as F


def Q(s):
    return tuple(map(F, s.split()))


R = Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
X = Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y = Q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
K = Q('-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1')
P = {
    (0, 0): F('33553/432000'), (0, 1): F('3997/368000'),
    (4, 1): F('3997/690000'), (0, 2): F('13091471/3762128400'),
    (2, 2): F('8901809/21809440'), (4, 2): F('170189123/37621284000'),
    (0, 3): F('8294919533/677183112000'),
    (3, 3): F('4095218743/29442744000'),
    (4, 3): F('8294919533/188106420000'),
    (4, 5): F('172449787/1363090000'),
    (5, 5): F('219439/545236000'),
    (6, 5): F('172449787/2180944000'),
    (6, 6): F('38053/432000'),
}
SA = ((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),
      (3,3),(1,5),(2,5),(4,5),(5,5),(6,5))
SB = ((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),
      (0,5),(1,5),(3,5),(4,5),(5,5),(6,5))
ATLAS = set(SA) | set(SB)
DUAL = [F(0)] * 21
for k, val in {0:'-28/5',1:'-84/23',2:'-3',3:'-51/23',
               7:'28/5',8:'6',9:'6',10:'163/23',
               15:'-4',16:'-4',17:'-112/23'}.items():
    DUAL[k] = F(val)


def mass(f):
    g,a,b,u,v,w,z = f
    return (F(509,900)*u + F(47,180)*z + F(67,162)*(v-z) + w/100,
            F(13,40)*a + b/80-u,(g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)
            +F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)


def times(f):
    g,a,b,u,v,w,z = f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)


def slack(f):
    g,a,b,u,v,w,z = f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)


def eq_row(edge):
    i,j = edge
    v = [F(0)]*21
    v[i] = 1
    v[7+j] = 1
    v[14+j] = R[i]
    return v


def matrix_rank(rows):
    m=[list(map(F,r)) for r in rows]
    if not m:return 0
    ncol=len(m[0]);p=0
    for col in range(ncol):
        k=next((k for k in range(p,len(m)) if m[k][col]),None)
        if k is None:continue
        m[p],m[k]=m[k],m[p]
        s=m[p][col]
        m[p]=[v/s for v in m[p]]
        for i in range(p+1,len(m)):
            if m[i][col]:
                c=m[i][col]
                m[i]=[a-c*b for a,b in zip(m[i],m[p])]
        p+=1
        if p==len(m):break
    return p


ALLOWED = [(i,j) for j in (0,1,2,3,5,6) for i in range(7)
           if j not in (0,6) or i==j]
assert len(ALLOWED)==30 and len(P)==13 and len(ATLAS)==16
assert all(w>0 for w in P.values())
NU,MU=mass(X),mass(Y)
assert all(v>=0 for v in slack(X)+slack(Y))
assert X[0]==X[2] and Y[6]==Y[1]/10 and Y[4]-Y[6]==F(9,40)*Y[2]
assert times(X)==times(Y)==(F('17609/6000'),F('33857/12000'))
assert sum(NU)==sum(MU)==1
assert sum(R[i]*NU[i] for i in range(7))==sum(R[i]*MU[i] for i in range(7))==1


def check_coupling(E):
    assert all(E.get(edge,F(0))>=0 for edge in ALLOWED)
    for i in range(7):
        assert sum(E.get((i,j),F(0)) for j in range(7))==MU[i]
    for j in range(7):
        assert sum(E.get((i,j),F(0)) for i in range(7))==NU[j]
        assert sum(R[i]*E.get((i,j),F(0)) for i in range(7))==R[j]*NU[j]


def dual_slack(edge):
    i,j=edge
    return F(int(edge not in ATLAS)) - (DUAL[i]+DUAL[7+j]+R[i]*DUAL[14+j])

assert all(dual_slack(e)>=0 for e in ALLOWED)
TIGHT=tuple(e for e in ALLOWED if dual_slack(e)==0)
assert len(TIGHT)==16
assert set(TIGHT)-set(P)=={(1,3),(2,1),(5,2)}
assert matrix_rank([[eq_row(e)[k] for e in TIGHT] for k in range(21)])==15
def determinant(rows):
    a=[list(map(F,row)) for row in rows]
    n=len(a)
    sign=1
    d=F(1)
    for col in range(n):
        idx=next((i for i in range(col,n) if a[i][col]),None)
        if idx is None:return F(0)
        if idx!=col:
            a[col],a[idx]=a[idx],a[col]
            sign=-sign
        v=a[col][col]
        d*=v
        for j in range(col+1,n):
            k=a[j][col]/v
            for t in range(col+1,n):
                a[j][t]-=k*a[col][t]
            a[j][col]=0
    return sign*d

MINOR_ROWS=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
MINOR_COLS=(0,1,2,3,4,5,7,8,9,10,11,12,13,14,15)
minor=[[eq_row(TIGHT[j])[i] for j in MINOR_COLS] for i in MINOR_ROWS]
assert determinant(minor)==F('-299/1600')
assert matrix_rank([[eq_row(e)[k] for e in P] for k in range(21)])==13
H={(0,1):F(-10,13),(2,1):F(23,13),(4,1):F(-1),
   (0,2):F(10,13),(2,2):F(-23,13),(4,2):F(1)}
assert all(e in TIGHT for e in H)
assert all(sum(H.get(e,F(0))*eq_row(e)[k] for e in TIGHT)==0 for k in range(21))
TMIN=max((-P.get(e,F(0))/v for e,v in H.items() if v>0))
TMAX=min((-P.get(e,F(0))/v for e,v in H.items() if v<0))
assert TMIN==0 and TMAX==F('3997/690000')
COST=F('225713944957/3385915560000')
DUAL_VALUE=sum(DUAL[i]*MU[i]+DUAL[7+i]*NU[i]+DUAL[14+i]*R[i]*NU[i] for i in range(7))
assert DUAL_VALUE==COST
for t,expected_support in [(TMIN,13),(TMAX/2,14),(TMAX,13)]:
    E={e:P.get(e,F(0))+t*H.get(e,F(0)) for e in TIGHT}
    check_coupling(E)
    assert sum(w for e,w in E.items() if e not in ATLAS)==COST
    assert sum(w>0 for w in E.values())==expected_support
    assert all((w==0 or dual_slack(e)==0) for e,w in E.items())

Z=(F(0),)*7
D=tuple(a-b for a,b in zip(slack(K),slack(Z)))
assert D==Q('-49400/295513 0 49400/295513 -49400/295513 0 -33345/591026 0 -33345/591026 0 1 -300453/295513 -163368/295513 152253/295513')
SL=slack(X)
lo=max((-SL[i]/D[i],i) for i in range(13) if D[i]>0)
hi=min((-SL[i]/D[i],i) for i in range(13) if D[i]<0)
assert lo==(F('-295513/49400000'),2)
assert hi==(F('295513/36054360'),10)
assert tuple(a-b for a,b in zip(mass(K),mass(Z)))==(F(0),)*7
assert tuple(a-b for a,b in zip(times(K),times(Z)))==(F(0),)*2
for h in (lo[0],F(0),hi[0]):
    xh=tuple(a+h*b for a,b in zip(X,K))
    assert all(s>=0 for s in slack(xh))
    assert xh[0]==xh[2] and mass(xh)==NU and times(xh)==times(Y)
assert SL[2]>0 and SL[10]>0
assert slack(tuple(a+lo[0]*b for a,b in zip(X,K)))[2]==0
assert slack(tuple(a+hi[0]*b for a,b in zip(X,K)))[10]==0
print('PASS_R5_LAWFUL_PHYSICAL_SEEDLESS_MARGINALS_AND_STOPPING_TIMES')
print('PASS_DUAL_30_EDGE_INEQUALITIES_TIGHT_EDGES',len(TIGHT),'RANK',15,'NULLITY',1)
print('PASS_OPTIMAL_FACE_ALL_REAL_TRANSPORT_SEGMENT',TMIN,TMAX)
print('PASS_OPTIMAL_SUPPORT_ENDPOINTS_13_INTERIOR_14')
print('PASS_OPTIMAL_ESCAPE_COST',COST)
print('PASS_COMPLETE_PHYSICAL_OBSERVER_FIBER',lo,hi)
print('PASS_ALL_REAL_RECTANGLE_SOURCE_FIBER_TIMES_OPTIMAL_FACE')
