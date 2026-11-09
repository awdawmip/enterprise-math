#!/usr/bin/env python3
"""Self-contained exact Fraction proof audit for R5 statistical observer fibers.
Inherited frozen seven-node likelihood-ratio experiment; no floating point.
"""
from fractions import Fraction as F

def Q(text): return tuple(map(F, text.split()))
R=Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
ZERO=(F(0),)*7

def masses(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u,(g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def slack(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def add(x,y,t=F(1)):
    return tuple(a+t*b for a,b in zip(x,y))

def combine(x,y,t):
    return tuple((1-t)*a+t*b for a,b in zip(x,y))

def derivative_matrix(fun):
    zero=fun(ZERO)
    cols=[tuple(a-b for a,b in zip(fun(tuple(F(i==k) for i in range(7))),zero)) for k in range(7)]
    return [list(row) for row in zip(*cols)]

def rank(A):
    a=[list(map(F,row)) for row in A]
    m=len(a);n=len(a[0]); r=0
    for c in range(n):
        p=next((j for j in range(r,m) if a[j][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        v=a[r][c];a[r]=[x/v for x in a[r]]
        for k in range(m):
            if k!=r and a[k][c]:
                v=a[k][c];a[k]=[x-v*y for x,y in zip(a[k],a[r])]
        r+=1
        if r==m:break
    return r

def determinant(A):
    a=[list(map(F,row)) for row in A]
    n=len(a); assert all(len(row)==n for row in a)
    v=F(1)
    for c in range(n):
        p=next((i for i in range(c,n) if a[i][c]),None)
        if p is None:return F(0)
        if p!=c:a[c],a[p]=a[p],a[c];v=-v
        t=a[c][c];v*=t
        for i in range(c+1,n):
            if a[i][c]:
                q=a[i][c]/t
                for j in range(c+1,n):a[i][j]-=q*a[c][j]
                a[i][c]=F(0)
    return v

M=derivative_matrix(masses);T=derivative_matrix(times)
K=Q('-49400/295513 -49400/295513 -49400/295513 -33345/591026 132145/295513 -33345/591026 1')
assert rank(M)==5 and rank(M+T)==6
assert all(sum(a*b for a,b in zip(row,K))==0 for row in M+T)
assert K[0]==K[2] and K[-1]==1
assert determinant([ [M[i][j] for j in (0,1,2,3,4)] for i in (0,1,2,3,4)])==F(67,4320)
assert determinant([ [ (M+T)[i][j] for j in (0,1,2,3,4,5)] for i in (0,1,2,3,4,7)])==F(295513,2916000)
# Restricted seedless F face: z=a/10 and v=z+9b/40.
V=[[F(int(i==0)), F(int(i==1))+F(int(i==4),10)+F(int(i==6),10),
    F(int(i==2))+F(9,40)*int(i==4),F(int(i==3)),F(int(i==5))] for i in range(7)]
MF=[[sum(M[i][k]*V[k][j] for k in range(7)) for j in range(5)] for i in range(7)]
assert determinant([[MF[i][j] for j in range(5)] for i in (0,1,2,4,5)])==F(3761,48000)

X0=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
X1=Q('1 1/10 1 27/800 1/100 27/400 1/100')
Y0=Q('871/1000 9/40 5/6 273/4000 21/100 143/1000 9/400')
Y1=Q('4673/6400 1311/6400 4673/6400 38759/512000 47301/256000 103999/512000 1311/64000')
DX=Q('-1802718000/1111424393 -1802718000/1111424393 -1802718000/1111424393 -608417325/1111424393 -496963350/1111424393 -608417325/1111424393 0')
DY=Q('-6000/3761 -6000/3761 -6000/3761 -2025/3761 -1950/3761 -2025/3761 -600/3761')
x=add(combine(X0,X1,F(1,4)),add(DX,K,F(-1)),F(1,240))
y=add(combine(Y0,Y1,F(1,4)),DY,F(1,240))
assert x[0]==x[2] and y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
assert all(t>=0 for t in slack(x)+slack(y))
assert times(x)==times(y)
SA=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),(3,3),(1,5),(2,5),(4,5),(5,5),(6,5))
A0=Q('33553/432000 38053/432000 3997/624000 3997/390000 1105679/28080000 15711211/52650000 14339/216000 388729/32400000 3298/16875 367/24000 7261/506250 113/6000 2612321/32400000 20761/270000')
AH=Q('54023/1080000 69773/1080000 6697/1248000 6697/780000 1175439949/17971200000 8008067351/33696000000 76032887/691200000 415111079/20736000000 101129/432000 367/48000 120750673/2592000000 113/12000 585724921/20736000000 155310673/1382400000')
D={(0,0):-F(1,2),(6,6):-F(1,2),(3,3):F(1)}
w=tuple((a+b)/2+F(1,240)*D.get(pair,F(0)) for a,b,pair in zip(A0,AH,SA))
E=dict(zip(SA,w));nu=masses(x);mu=masses(y)
assert min(w)>0
assert all(sum(E.get((i,j),F(0)) for j in range(7))==mu[i] for i in range(7))
assert all(sum(E.get((i,j),F(0)) for i in range(7))==nu[j] for j in range(7))
assert all(sum(R[i]*E.get((i,j),F(0)) for i in range(7))==R[j]*nu[j] for j in range(7))

base=slack(x); derivatives=tuple(a-b for a,b in zip(slack(add(x,K)),base))
lo=max((-v/d for v,d in zip(base,derivatives) if d>0))
hi=min((-v/d for v,d in zip(base,derivatives) if d<0))
assert (lo,hi)==(F(-11,2400),F(348915803,36160119456))
assert all(v>=0 for v in slack(add(x,K,lo))+slack(add(x,K,hi)))
assert add(x,K,lo)[6]==0
upper=add(x,K,hi)
assert upper[6]==upper[1]/10
# Whole interval: each physical slack is affine; the same E remains lawful.
assert all(z>=0 for z in slack(x))
assert all(z==0 for z in (tuple(a-b for a,b in zip(masses(add(x,K)),nu))))
assert times(add(x,K))==times(x)
print('PASS_MASS_RANK',rank(M),'MASS_TIME_RANK',rank(M+T),'UNIQUE_K',K)
print('PASS_SEEDLESS_F_FACE_5X5_MINOR',F(3761,48000))
print('PASS_R5_BASEPOINT_14_EDGE_TRANSPORT','min_edge',min(w))
print('PASS_EXACT_FULL_PHYSICAL_FIBER',lo,hi,'active_faces','z=0','z=a/10')
print('THEOREM_GLOBAL_1D_OBSERVER_FIBERS_AND_14_EDGE_SUPPORT_INVARIANCE')
