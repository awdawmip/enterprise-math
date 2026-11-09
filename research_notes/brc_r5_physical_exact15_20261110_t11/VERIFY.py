#!/usr/bin/env python3
"""R5 physical matched-time g=b pair: exact Fraction + finite 4845-support proof.

Only standard-library rational arithmetic and exact modular Gaussian elimination.
No LP/MILP/float/external proof dependency.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial

def q(s):
    return tuple(map(F, s.split()))

R = q("1/10 1/2 3/4 1 5/4 3/2 19/10")
X0 = q("999/1000 1/6 999/1000 1/20 29/240 11/160 1/120")
Y0 = q("1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200")
H = F("17774559/17507527960")
DY = q("0 1 0 -1/4 -1/4 0 1/10")
X = X0[:6] + (X0[6] + H/2,)
Y = tuple(v+F(1,100000)*d for v,d in zip(Y0,DY))

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u + F(47,180)*z + F(67,162)*(v-z) + w/100,
            F(13,40)*a+b/80-u, (g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2, F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def slack(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def col(edge):
    i,j=edge
    c=[F(0)]*21
    c[i]=F(1); c[7+j]=F(1); c[14+j]=R[i]
    return tuple(c)

def solve(a,b):
    n=len(b); m=[list(a[i])+[b[i]] for i in range(n)]; det=F(1)
    for k in range(n):
        p=next((i for i in range(k,n) if m[i][k]),None)
        assert p is not None
        if p!=k: m[k],m[p]=m[p],m[k]; det=-det
        d=m[k][k]; det*=d
        m[k]=[v/d for v in m[k]]
        for i in range(n):
            if i==k:continue
            d=m[i][k]
            if d:m[i]=[x-d*y for x,y in zip(m[i],m[k])]
    return tuple(row[-1] for row in m),det

D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
        if j not in (0,6) or i==j)
B=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),
   (0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)

# A^T y_e <= indicator_e, certified against all 30 allowed columns.
CERT={
 (0,0):{7:"1"},
 (0,1):{1:"-5/13",8:"15/13",15:"-20/13"},
 (0,2):{1:"-5/9",2:"-5/18",9:"10/9",16:"-10/9"},
 (2,2):{0:"-18/5",1:"-2",7:"18/5",8:"54/13",9:"4",15:"-72/13",16:"-4"},
 (3,3):{0:"-11/5",1:"1",2:"3",3:"5",4:"5",5:"5",6:"5",7:"11/5",8:"3",9:"3",12:"-5",13:"-5",15:"-8",16:"-8",17:"-4"},
 (4,3):{0:"-9/10",1:"3/2",2:"3",3:"4",4:"6",5:"6",6:"6",7:"9/10",8:"3/2",9:"3/2",12:"-6",13:"-6",15:"-6",16:"-6",17:"-4"},
 (4,5):{0:"2/5",1:"2",2:"3",3:"4",4:"5",5:"4",6:"4",7:"-2/5",12:"-4",13:"-4",15:"-4",16:"-4",17:"-4"},
 (5,5):{0:"2/5",1:"2",2:"3",3:"4",4:"5",5:"6",6:"5",7:"-2/5",12:"-5",13:"-5",15:"-4",16:"-4",17:"-4"},
 (6,5):{0:"2/13",1:"10/13",2:"15/13",3:"20/13",4:"25/13",5:"25/13",6:"38/13",7:"-2/13",12:"-25/13",13:"-38/13",15:"-20/13",16:"-20/13",17:"-20/13"},
 (6,6):{13:"1"},
}

# 2^127 - 1 is a known Mersenne prime. It exceeds the full
# 14! 38^14 Leibniz integer-minor bound, so rational and modular
# ranks are equal on every 14-column support of the scaled C matrix.
P=(1<<127)-1
assert P>factorial(14)*38**14

def modq(a):
    a=F(a)
    assert a.denominator%P
    return a.numerator*pow(a.denominator,-1,P)%P

def rank_mod(rows):
    a=[list(row) for row in rows]
    m,n=len(a),len(a[0])
    rank=0
    for j in range(n):
        k=next((i for i in range(rank,m) if a[i][j]),None)
        if k is None:continue
        a[rank],a[k]=a[k],a[rank]
        inv=pow(a[rank][j],-1,P)
        a[rank]=[v*inv%P for v in a[rank]]
        for i in range(rank+1,m):
            if a[i][j]:
                t=a[i][j]
                a[i]=[(u-t*v)%P for u,v in zip(a[i],a[rank])]
        rank+=1
        if rank==m:break
    return rank

def exhaustive(rhs,columns):
    forced=tuple(CERT)
    others=tuple(e for e in D if e not in CERT)
    assert len(forced)==10 and len(others)==20 and len(I)==15
    scale=lambda i,x:20*x if i>=14 else x
    C={e:[modq(scale(i,columns[e][i])) for i in I] for e in D}
    b=[modq(scale(i,rhs[i])) for i in I]
    pivots=[];basis=[]
    def insert(v):
        v=v.copy()
        for k,w in zip(pivots,basis):
            t=v[k]
            if t:v=[(x-t*y)%P for x,y in zip(v,w)]
        k=next((i for i,x in enumerate(v) if x),None)
        if k is None:return False
        z=pow(v[k],-1,P);v=[x*z%P for x in v]
        for idx,w in enumerate(basis):
            t=w[k]
            if t:basis[idx]=[(x-t*y)%P for x,y in zip(w,v)]
        pivots.append(k);basis.append(v)
        return True
    assert all(insert(C[e]) for e in forced)
    assert len(pivots)==10
    remaining=tuple(i for i in range(15) if i not in pivots)
    assert len(remaining)==5
    def quotient(v):
        v=v.copy()
        for k,w in zip(pivots,basis):
            t=v[k]
            if t:v=[(x-t*y)%P for x,y in zip(v,w)]
        return tuple(v[i] for i in remaining)
    V={e:quotient(C[e]) for e in others}
    target=quotient(b)
    counts={}
    for four in combinations(others,4):
        mat=[[V[e][i] for e in four] for i in range(5)]
        a=rank_mod(mat)
        b=rank_mod([row+[target[i]] for i,row in enumerate(mat)])
        assert b==a+1,(four,a,b)
        counts[(a,b)]=counts.get((a,b),0)+1
    assert sum(counts.values())==4845
    assert counts=={(4,5):3669,(3,4):1143,(2,3):33}
    print("PASS_ALL_4845_FORCED_SUPPORT_EXTENSIONS_MOD_2_127_MINUS_1",counts)
    print("PASS_MODULAR_RANK_LIFT_MINOR_BOUND",factorial(14)*38**14)

def main():
    assert X[0]==X[2] and Y[0]==1 and Y[6]==Y[1]/10
    assert all(z>=0 for z in slack(X)+slack(Y))
    assert tuple(i for i,z in enumerate(slack(X)) if not z)==(4,)
    assert tuple(i for i,z in enumerate(slack(Y)) if not z)==(2,10)
    assert times(X)==times(Y)==q("17609/6000 33857/12000")
    mu,nu=mass(Y),mass(X)
    assert mu[1]==F(23,4000000) and nu[4]==0
    assert sum(mu)==sum(nu)==1 and len(D)==30
    rhs=mu+nu+tuple(R[j]*nu[j] for j in range(7))
    C={e:col(e) for e in D}
    weights,det=solve([[C[e][i] for e in B] for i in I],
                      tuple(rhs[i] for i in I))
    assert det==F("-299/1600") and len(weights)==15 and min(weights)>0
    E=dict(zip(B,weights))
    assert all(sum(E.get(e,F(0))*C[e][i] for e in D)==rhs[i]
               for i in range(21))
    print("PASS_EXACT_LAWFUL_G_EQUALS_B_AND_SEEDLESS_F")
    print("PASS_MATCHED_STOPPING_TIMES",*times(X))
    print("PASS_15_STRICTLY_POSITIVE_EDGE_COUPLING minimum=",min(weights))
    print("PASS_ALL_21_BLACKWELL_EQUALITIES det15=",det)
    assert len(CERT)==10
    lower={}
    for edge,sparse in CERT.items():
        y=[F(sparse.get(i,"0")) for i in range(21)]
        assert all(sum(y[i]*C[f][i] for i in range(21))<=F(edge==f)
                   for f in D)
        beta=sum(y[i]*rhs[i] for i in range(21))
        assert beta>0
        lower[edge]=beta
    assert lower[(4,3)]==F(64190522124239,2296534032000000)
    assert lower[(4,3)]>2*mu[1]
    print("PASS_10_FULL_CARRIER_RATIONAL_DUAL_CERTIFICATES")
    print("FORCED_E43_LOWER",lower[(4,3)],"ROW_MU1",mu[1],
          "E43_LOWER_GT_2MU1",lower[(4,3)]>2*mu[1])
    exhaustive(rhs,C)
    print("PROVED_NO_NONNEGATIVE_COUPLING_ON_LE_14_EDGES")
    print("EXACT_MINIMUM_POSITIVE_SUPPORT",len(B))
    for e in B: print("POSITIVE_EDGE",e[0],e[1],E[e])

if __name__=="__main__":
    main()
