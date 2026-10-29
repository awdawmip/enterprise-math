#!/usr/bin/env python3
"""Independent exact F_p checks for reflected-tail critical polynomial and discriminant.
Author portable evidence, NOT native Enterprise Math execution.
"""
from math import comb, isqrt

def primes(n):
    s=bytearray(b'\x01')*(n+1);s[:2]=b'\x00\x00'
    for i in range(2,isqrt(n)+1):
        if s[i]:s[i*i:n+1:i]=b'\x00'*((n-i*i)//i+1)
    return [p for p in range(n+1) if s[p] and p%8==3]

def plus(a,b,p):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]=(z[i]+v)%p
    for i,v in enumerate(b):z[i]=(z[i]+v)%p
    return z

def multiply(a,b,p):
    z=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):z[i+j]=(z[i+j]+u*v)%p
    return z

def P_even(d,p):
    a,b=[1],[0,1]
    if not d:return [1]
    for n in range(1,d):
        c=plus([0]+[(2*n+1)*v for v in b],[-n*v for v in a],p)
        inv=pow(n+1,-1,p);a,b=b,[x*inv%p for x in c]
    assert all(b[i]==0 for i in range(1,d+1,2))
    return b

def hpolys(p):
    m=(p-3)//8;d=2*m;N=4*m+1
    E=P_even(d,p)[::2]
    G=[0]*(m+1)
    for j,ej in enumerate(E):
        for k in range(j+1):G[m-j+k]=(G[m-j+k]+ej*comb(j,k)*(-1)**(j-k))%p
    D=comb(3*m+1,m)%p
    assert G[0]==D and G[-1]==1
    A=[(16*i+5)*g%p for i,g in enumerate(G)]
    assert A[-1]==p-1
    GG=multiply(G,G,p)
    # M' = - z^(2m) * G^2, M(0)=0.
    M=[0]*(N+1)
    for i,c in enumerate(GG):M[2*m+i+1]=(-c*pow(2*m+i+1,-1,p))%p
    # R=(8*z^(2m+1)*G^2-3*M)/D^2
    invD2=pow(D*D,-1,p)
    R=[(-3*coef*invD2)%p for coef in M]
    for i,c in enumerate(GG):R[2*m+1+i]=(R[2*m+1+i]+8*c*invD2)%p
    # Derivative exactly z^d G A /D²
    RA=multiply(G,A,p)
    assert [(i*R[i])%p for i in range(1,N+1)]==[0]*(2*m)+[(c*invD2)%p for c in RA]
    return m,D,G,A,R

def val(a,x,p):
    s=0
    for c in reversed(a):s=(s*x+c)%p
    return s

def deriv(a,p):return [(i*a[i])%p for i in range(1,len(a))]

def trim(a):
    a=a[:]
    while len(a)>1 and not a[-1]:a.pop()
    return a

def resultant(a,b,p):
    a=trim(a);b=trim(b);m=len(a)-1;n=len(b)-1
    assert m and n
    mat=[]
    for i in range(n):
        row=[0]*(m+n);row[i:i+m+1]=list(reversed(a));mat.append(row)
    for i in range(m):
        row=[0]*(m+n);row[i:i+n+1]=list(reversed(b));mat.append(row)
    det=1
    for j in range(m+n):
        pivot=next((r for r in range(j,m+n) if mat[r][j]),None)
        if pivot is None:return 0
        if pivot!=j:mat[j],mat[pivot]=mat[pivot],mat[j];det=-det
        d=mat[j][j];det=det*d%p;id=pow(d,-1,p)
        for r in range(j+1,m+n):
            if mat[r][j]:
                t=mat[r][j]*id%p
                for k in range(j,m+n):mat[r][k]=(mat[r][k]-t*mat[j][k])%p
    return det%p

def check_discriminant(p,t):
    m,D,G,A,R=hpolys(p);N=len(R)-1
    Rt=R[:];Rt[0]=(Rt[0]-t)%p
    disc=resultant(Rt,deriv(R,p),p)*pow(R[-1],-1,p)%p
    pred=(-pow(2,-1,p)*pow(D,-2*(N-1),p)*pow(t,2*m,p)*resultant(Rt,G,p)*(-resultant(Rt,A,p)))%p
    # resultant(Rt,G)=K_G, resultant(Rt,A)=-K_A; formula disc=-1/(2D^...)* K_G*K_A
    assert disc==pred,(p,t,disc,pred)
    return disc

def check():
    ps=primes(2300)
    repeated=[]
    for p in ps:
        m,D,G,A,R=hpolys(p)
        # if A(a)=A'(a)=0, then a must be 5. Check via exhaustive p<=2300 for a small subset.
        if val(A,5,p)==0: repeated.append((p,m, val(deriv(A,p),5,p),val(deriv(deriv(A,p),p),5,p)))
    print('PASSES derivative factorization primes:',len(ps),'p<2300; roots A(5):',repeated[:30], 'total',len(repeated))
    trials=0
    for p in [11,19,43,59,67,83,107,131,139]:
        for t in range(min(p,7)):
            check_discriminant(p,t);trials+=1
    print('PASSES discriminant Sylvester test pairs:',trials)
    p=11;m,D,G,A,R=hpolys(p)
    rootsG=[x for x in range(p) if val(G,x,p)==0]
    rootsA=[x for x in range(p) if val(A,x,p)==0]
    print('p11: m D G A R',m,D,G,A,R)
    print('p11 critical values G / A:',[(x,val(R,x,p)) for x in rootsG],[(x,val(R,x,p)) for x in rootsA])
    assert len(rootsG)==1 and len(rootsA)==1 and val(R,rootsG[0],p)!=val(R,rootsA[0],p)
    assert all(val(R,x,p)!=0 for x in rootsG+rootsA)
    # Independent exact p=19 S_9 branch witness, including zero-fiber collision.
    p=19
    m,D,G,A,R=hpolys(p)
    assert (m,D,G,A)==(2,2,[2,14,1],[10,9,18])
    assert R==[0,0,0,0,0,1,5,17,4,10]
    def kres(t,B,sign=1):
        F=R[:];F[0]=(F[0]-t)%p
        return sign*resultant(F,B,p)%p
    kg=[kres(t,G) for t in (0,1,2)]
    ka=[kres(t,A,-1) for t in (0,1,2)]
    assert kg==[(t*t+8*t+5)%p for t in (0,1,2)]
    assert ka==[(t*t+9*t)%p for t in (0,1,2)]
    # In F_19 the zero fiber is 5[0]+2[-1]+[5]+[8].
    assert all(val(R,x,p)==0 for x in (0,18,5,8))
    assert val(deriv(R,p),18,p)==0 and val(deriv(deriv(R,p),p),18,p)!=0
    assert ka[0]==0 and (10*10+8*10+5)%p!=0
    print('p19: K_G=t^2+8t+5; K_A=t(t+9); zero inertia=(5)(2)(1^2),'
          ' isolated transposition at t=10, geometric/arithmetic S9')
    print('ALL PASS')

if __name__=='__main__':check()
