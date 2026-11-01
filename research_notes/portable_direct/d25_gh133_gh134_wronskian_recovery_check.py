#!/usr/bin/env python3
"""GH133-GH134 exact recurrence / double-path coefficient verifier; standard library only."""
from math import comb
PRIMES=[3,5,7,11,13,17,19,23,29,31,37,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def padd(a,b,p,sign=1):
    return trim([((a[i] if i<len(a) else 0)+sign*(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])
def mulp(a,b,p):
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            r[i+j]=(r[i+j]+ai*bj)%p
    return trim(r)
def dif(a,p):return [((j+1)*a[j+1])%p for j in range(len(a)-1)] or [0]
def check_poly(p):
    N=(p-1)//2;P=[[1],[p-1]]
    for i in range(2,N+1):P.append(padd([(-x)%p for x in P[-1]],[0]+P[-2],p,-1))
    A=[0]*N+P[N];E=P[N-1]
    W=padd(mulp(dif(A,p),E,p),mulp(A,dif(E,p),p),p,-1)
    goal=trim([0]*(N-1)+[(-N*comb(N-1,j)*pow(-4,j,p))%p for j in range(N)])
    assert trim(W)==goal,("W",p)
    for y in (A,E):
        ode=padd(padd(mulp([0,4%p,-16%p],dif(dif(y,p),p),p),
                       mulp([6%p,-48%p],dif(y,p),p),p),[-15*v%p for v in y],p)
        assert ode==[0],("ODE",p)
def field(p):
    def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def sub(a,b):return ((a[0]-b[0])%p,(a[1]-b[1])%p)
    def mul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def power(a,n):
        z=(1,0)
        while n:
            if n&1:z=mul(z,a)
            a=mul(a,a);n>>=1
        return z
    return add,sub,mul,power
def direct_coefficient(t,k,p,B,prec=None):
    add,_,mul,power=field(p)
    if prec is None:
        f=[1]*(t+1)
        for j in range(1,t+1):f[j]=f[j-1]*j%p
        fi=[pow(z,-1,p) for z in f]
        bp=[(1,0)]
        for j in range(t):bp.append(mul(bp[-1],B))
    else:f,fi,bp=prec
    z=(0,0)
    for a in range(max(0,k-t),min(t,k//2)+1):
        b=k-2*a;c=t-k+a
        z=add(z,mul((f[t]*fi[a]*fi[b]*fi[c]%p,0),bp[c]))
    return z
def check_mark(p):
    assert p%8==3 and p>=11
    add,sub,mul,power=field(p);N=(p-1)//2;B=(pow(8,-1,p),pow(12,-1,p))
    assert mul(B,sub((1,0),mul((4,0),B)))==(pow(144,-1,p),0)
    P=[(1,0),(p-1,0)];d=[(0,0),(0,0)]
    for i in range(2,N+1):
        pn=sub(sub((0,0),P[-1]),mul(B,P[-2]))
        dn=sub(sub(sub((0,0),d[-1]),P[-2]),mul(B,d[-2]))
        P.append(pn);d.append(dn)
    A=mul(power(B,N),P[N]);E=P[N-1]
    Ap=add(mul((N,0),mul(power(B,N-1),P[N])),mul(power(B,N),d[N]))
    Ep=d[N-1];A2=sub((0,0),Ap);E2=sub((0,0),Ep)
    Dlt=sub(mul(A,E2),mul(A2,E))
    assert Dlt==(72%p,0),("det",p,Dlt)
    if p<=107 or p==3347:
        fact=[1]*p
        for i in range(1,p):fact[i]=fact[i-1]*i%p
        inv=[pow(t,-1,p) for t in fact]
        bp=[(1,0)]
        for i in range(p):bp.append(mul(bp[-1],B))
        prec=fact,inv,bp
        assert (A,E,A2,E2)==tuple(direct_coefficient(t,k,p,B,prec) for t,k in
            [(p-1,N),(p-1,3*N+1),(p-2,N),(p-2,3*N+1)])
    C=direct_coefficient(N-1,N,p,B);D=direct_coefficient(N-1,N-1,p,B)
    H=add(D,mul((2,0),mul(B,C)));Hp=mul((N,0),C)
    U=power(C,p);V=power(D,p)
    m1=sub((0,0),add(mul(A,U),mul(E,V)))
    m2=sub((0,0),add(mul(A2,U),mul(E2,V)))
    invdet=(pow(72,-1,p),0)
    Ur=mul(sub(mul(E,m2),mul(E2,m1)),invdet)
    Vr=mul(sub(mul(A2,m1),mul(A,m2)),invdet)
    assert (U,V)==(Ur,Vr)
    Cr=power(Ur,p);Dr=power(Vr,p)
    Hr=add(Dr,mul((2,0),mul(B,Cr)))
    hpr=mul((N,0),Cr)
    S1=mul((2,0),mul(hpr,power(Hr,p)))
    tau=mul(Hr,power(Hr,p))
    assert (Cr,Dr,Hr,hpr)==(C,D,H,Hp)
    if p==3347:
        assert (A,E,A2,E2)==((3052,295),(2167,0),(33,2542),(0,127))
        assert (m1,m2,U,V)==((3179,0),(0,2701),(0,2702),(568,998))
        assert (C,D,H,Hp,S1,tau)==((0,645),(568,2349),(783,0),(0,1351),(0,362),(588,0))
    return p,m1,m2,S1,tau
def main():
    for p in PRIMES:check_poly(p)
    marks=[p for p in PRIMES if p>=11 and p%8==3]
    for p in marks:check_mark(p)
    big=check_mark(3347)
    print("PASS_GH133_UNIVERSAL_WRONSKIAN_POLYNOMIAL primes",len(PRIMES),"max_p",max(PRIMES))
    print("PASS_GH134_ALL_TARGET_MARKS_DETERMINANT_72 small_primes",len(marks))
    print("P3347_EXACT",big)
    print("PASS_GH134_P3347_TWO_MOMENT_RECOVERY_AND_INDEPENDENT_MULTINOMIAL")
if __name__=="__main__":main()
