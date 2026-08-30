#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, factorial, prod

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def diag(v):
    return [[v[i] if i == j else F(0) for j in range(len(v))] for i in range(len(v))]

def tr(A):
    return [list(r) for r in zip(*A)]

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def sub(A, B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mv(A, x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def det(A):
    A=[r[:] for r in A]; n=len(A); z=F(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None: return F(0)
        if p!=c: A[c],A[p]=A[p],A[c]; z=-z
        q=A[c][c]; z*=q
        for j in range(c,n): A[c][j]/=q
        for r in range(c+1,n):
            q=A[r][c]
            if q:
                for j in range(c,n): A[r][j]-=q*A[c][j]
    return z

def inv(A):
    n=len(A); I=eye(n); A=[A[i][:]+I[i] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if A[r][c])
        A[c],A[p]=A[p],A[c]
        q=A[c][c]; A[c]=[x/q for x in A[c]]
        for r in range(n):
            if r!=c and A[r][c]:
                q=A[r][c]; A[r]=[A[r][j]-q*A[c][j] for j in range(2*n)]
    return [r[n:] for r in A]

def rank(A):
    A=[r[:] for r in A]; R=len(A); C=len(A[0]); r=0
    for c in range(C):
        p=next((i for i in range(r,R) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; q=A[r][c]; A[r]=[x/q for x in A[r]]
        for i in range(R):
            if i!=r and A[i][c]:
                q=A[i][c]; A[i]=[A[i][j]-q*A[r][j] for j in range(C)]
        r+=1
        if r==R: break
    return r

def h(m,q):
    return F(1,prod(1+q+l*m*m for l in range(m)))

def build(m,actual=True):
    n=m-1; w=[F((-1)**i*comb(n,i)) for i in range(m)]
    H=[[h(m,i+m*j) if actual else F(1,1+i+m*j) for j in range(m)] for i in range(m)]
    e=[sum(H[i][j]*w[j] for j in range(m)) for i in range(m)]
    d=[sum(w[i]*H[i][j] for i in range(m)) for j in range(m)]
    assert min(e+d)>0
    A=[[H[i][j]*w[j]/e[i] for j in range(m)] for i in range(m)]
    B=[[H[i][j]*w[i]/d[j] for i in range(m)] for j in range(m)]
    return H,w,e,d,A,B,mm(B,A)

def lag(nodes,j,x):
    return prod(x-y for k,y in enumerate(nodes) if k!=j)/prod(nodes[j]-y for k,y in enumerate(nodes) if k!=j)

def check_actual(m):
    H,w,e,d,A,B,K=build(m); n=m-1
    for i in range(m):
        for j in range(m):
            q=i+m*j
            lhs=sum(F((-1)**l*comb(n,l),q+1+l*m*m) for l in range(m))
            assert lhs==F(factorial(n)*(m*m)**n)*h(m,q)
    J=diag([F((-1)**i) for i in range(m)])
    W=diag(w); E=diag(e); D=diag(d); L=diag([F(comb(n,i)) for i in range(m)])
    P=mm(E,L); Q=mm(D,L); X=mm(A,J); Y=mm(B,J)
    assert mm(Q,Y)==mm(tr(X),P)
    assert K==mm(mm(mm(Y,J),X),J)
    assert mm(mm(D,W),K)==mm(mm(tr(A),E),mm(W,A))
    assert mv(K,[F(1)]*m)==[F(1)]*m
    assert rank(sub(eye(m),K))==m-1
    R=[[F((-1)**k*comb(j,k)) if k<=j else F(0) for k in range(m)] for j in range(m)]
    T=mm(mm(R,K),R); Qm=[r[1:] for r in T[1:]]
    qdet=det(sub(eye(m-1),Qm)); assert qdet
    return qdet,sum(w[j]*d[j] for j in range(m))

def check_cauchy(m):
    H,w,e,d,A,B,K=build(m,False); n=m-1
    xs=[F(1+i) for i in range(m)]; ys=[F(m*j) for j in range(m)]
    assert e==[F(factorial(n)*m**n,prod(int(x)+m*r for r in range(m))) for x in xs]
    assert d==[F(factorial(n),prod(int(y)+1+r for r in range(m))) for y in ys]
    assert all(A[i][j]==lag(ys,j,-xs[i]) for i in range(m) for j in range(m))
    nx=[-x for x in xs]
    assert all(B[j][i]==lag(nx,i,ys[j]) for i in range(m) for j in range(m))
    assert K==eye(m)

def principal_angle_m2():
    m=2; H,w,e,d,A,B,K=build(m)
    GV=[[h(m,i+j) for j in range(m)] for i in range(m)]
    GW=[[h(m,m*(i+j)) for j in range(m)] for i in range(m)]
    C=mm(mm(mm(inv(GW),tr(H)),inv(GV)),H)
    assert det(K)==F(529,1540)
    assert det(C)==F(18515,19968)
    assert det(K)!=det(C)

def main():
    q={}; s={}
    for m in range(2,7): q[m],s[m]=check_actual(m)
    for m in range(2,9): check_cauchy(m)
    principal_angle_m2()
    assert q[2]==F(1011,1540)
    assert s[2]==F(337,3360)
    print("PASS: exact AP m=2..6; Cauchy K=I m=2..8; m=2 principal-angle mismatch")

if __name__=="__main__":
    main()