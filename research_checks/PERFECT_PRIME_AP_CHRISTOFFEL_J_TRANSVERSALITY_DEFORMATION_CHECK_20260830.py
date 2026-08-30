#!/usr/bin/env python3
from fractions import Fraction as F
from math import comb, factorial

def det(A):
    A=[row[:] for row in A]
    n=len(A); out=F(1)
    for c in range(n):
        p=next((r for r in range(c,n) if A[r][c]),None)
        if p is None:
            return F(0)
        if p!=c:
            A[c],A[p]=A[p],A[c]; out=-out
        q=A[c][c]; out*=q
        for j in range(c,n):
            A[c][j]/=q
        for r in range(c+1,n):
            q=A[r][c]
            if q:
                for j in range(c,n):
                    A[r][j]-=q*A[c][j]
    return out

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def tr(A):
    return [list(r) for r in zip(*A)]

def diag(v):
    return [[v[i] if i==j else F(0) for j in range(len(v))] for i in range(len(v))]

def add(A,B,sgn=1):
    return [[A[i][j]+sgn*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(A,c):
    return [[c*x for x in row] for row in A]

def invdiag(v):
    return diag([1/x for x in v])

def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

def crossing_direct(m):
    n=m-1; a=m*m
    w=[F((-1)**i*comb(n,i)) for i in range(m)]
    xs=[F(i+1) for i in range(m)]
    ys=[F(m*j) for j in range(m)]
    M=[[F(0) for _ in range(n)] for __ in range(n)]
    for r in range(1,m):
        for s in range(1,m):
            z=F(0)
            for i,x in enumerate(xs):
                for j,y in enumerate(ys):
                    dr=(-x)**r-y**r
                    ds=(-x)**s-y**s
                    z += w[i]*w[j]*dr*ds/(x+y+a)
            M[r-1][s-1]=-n*z
    return M

def crossing_reduced(m):
    n=m-1; a=m*m
    w=[F((-1)**j*comb(n,j)) for j in range(m)]
    ys=[F(m*j) for j in range(m)]
    sj=[F(factorial(n),1) / prodF([y+a+r for r in range(1,m+1)]) for y in ys]
    M=[[F(0) for _ in range(n)] for __ in range(n)]
    for r in range(1,m):
        for s in range(1,m):
            z=F(0)
            for j,y in enumerate(ys):
                dr=(y+a)**r-y**r
                ds=(y+a)**s-y**s
                z += w[j]*sj[j]*dr*ds
            M[r-1][s-1]=-n*z
    return M

def prodF(xs):
    z=F(1)
    for x in xs: z*=x
    return z

def H_and_dH_m3(t):
    m=3; n=2; a=9
    H=[]; Hd=[]
    for i in range(m):
        hr=[]; hdr=[]
        for j in range(m):
            base=i+m*j+1
            hr.append(F(1,base)-F(2)*t/F(base+a)+t*t/F(base+2*a))
            hdr.append(-F(2,base+a)+F(2)*t/F(base+2*a))
        H.append(hr); Hd.append(hdr)
    return H,Hd

def gamma_derivative_m3(t):
    m=3; n=2
    w=[F(1),F(-2),F(1)]
    lam=[F(1),F(2),F(1)]
    J=diag([F(1),F(-1),F(1)])
    La=diag(lam)
    H,Hd=H_and_dH_m3(t)
    e=mv(H,w); ed=mv(Hd,w)
    d=mv(tr(H),w); dd=mv(tr(Hd),w)
    E=diag(e); Ed=diag(ed); D=diag(d); Dd=diag(dd)
    X=mm(mm(invdiag(e),H),La)
    Xd=add(mm(mm(invdiag(e),Hd),La), mm(mm(invdiag(e),Ed),X), sgn=-1)
    P=mm(E,La); Pd=mm(Ed,La); Q=mm(D,La); Qd=mm(Dd,La)
    term=mm(Qd,J)
    term=add(term, mm(mm(mm(tr(Xd),P),J),X), sgn=-1)
    term=add(term, mm(mm(mm(tr(X),Pd),J),X), sgn=-1)
    term=add(term, mm(mm(mm(tr(X),P),J),Xd), sgn=-1)
    return term

# Polynomial helpers, low-to-high coefficients over Q.
def trim(p):
    p=list(map(F,p))
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def pder(p):
    p=trim(p)
    return trim([F(i)*p[i] for i in range(1,len(p))] or [F(0)])

def peval(p,x):
    z=F(0)
    for c in reversed(trim(p)):
        z=z*x+c
    return z

def pdivmod(a,b):
    a=trim(a); b=trim(b)
    if b==[F(0)]: raise ZeroDivisionError
    q=[F(0)]*max(1,len(a)-len(b)+1)
    r=a[:]
    while not (len(r)==1 and r[0]==0) and len(r)>=len(b):
        c=r[-1]/b[-1]; k=len(r)-len(b); q[k]=c
        for i in range(len(b)):
            r[i+k]-=c*b[i]
        r=trim(r)
    return trim(q),trim(r)

def pgcd(a,b):
    a=trim(a); b=trim(b)
    while b!=[F(0)]:
        _,r=pdivmod(a,b)
        a,b=b,r
    if a==[F(0)]: return a
    lead=a[-1]
    return trim([x/lead for x in a])

def sturm(p):
    p=trim(p); seq=[p,pder(p)]
    while seq[-1]!=[F(0)]:
        _,r=pdivmod(seq[-2],seq[-1])
        if r==[F(0)]: break
        seq.append(trim([-x for x in r]))
    return seq

def variations(seq,x):
    signs=[]
    for p in seq:
        v=peval(p,x)
        if v>0: signs.append(1)
        elif v<0: signs.append(-1)
    return sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))

def root_count(p,a,b):
    s=sturm(p)
    return variations(s,a)-variations(s,b)

# Obstruction polynomial P_12, low-to-high.
P12=[
410283992369849598000000,
-1076281742427279287900000,
1082281784621932214320000,
-538717964929345743542000,
141707915785000444930050,
-21386627649978696405300,
2128778523707885528100,
-114789507726989038041,
2666960532445357740,
-38119126605257040,
266836318177520,
-1030450862560,
18677859200,
]
A2=[12206367030,-36819435,1413754]
B6=[55117062000,-72293202550,40314445885,-10512282495,976346833,-15974170,11760]

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=F(x)*F(y)
    return trim(out)

def quad(c0,c1,c2,t):
    return F(c0)+F(c1)*t+F(c2)*t*t

def obstruction_den(t):
    A=quad(420,-42,5,t)
    B=quad(271700,-7315,728,t)
    C=quad(391391,-23920,2618,t)
    return F(50)*A*A*B*B*C*C

def main():
    # Exact finite regression of the all-m proof identity.
    dets={}
    for m in range(2,8):
        M1=crossing_direct(m)
        M2=crossing_reduced(m)
        assert M1==M2
        z=det(M1)
        assert z!=0
        expected=(-1)**(((m-1)*m)//2)
        assert (1 if z>0 else -1)==expected
        dets[m]=z

    # Exact m=3 obstruction: det of the 2x2 principal cofactor of Gamma'_3,t.
    # Algebraic elimination gives det = -27*P12/(50*A^2*B^2*C^2).
    # Equality is certified at 13 distinct rationals; both sides have numerator degree <=12.
    for k in range(13):
        t=F(k,12)
        Gd=gamma_derivative_m3(t)
        lhs=det([row[:2] for row in Gd[:2]])
        rhs=-F(27)*peval(P12,t)/obstruction_den(t)
        assert lhs==rhs

    lo=F(4991,5000)       # 0.9982
    hi=F(9983,10000)      # 0.9983
    assert peval(P12,lo)>0 and peval(P12,hi)<0
    assert root_count(P12,F(0),F(1))==1
    assert root_count(P12,lo,hi)==1

    # The derivative singularity is not an m=3 quotient-determinant zero.
    Nq=pmul(A2,B6)
    assert pgcd(P12,Nq)==[F(1)]
    assert root_count(A2,F(0),F(1))==0
    assert root_count(B6,F(0),F(1))==0

    print("PASS: local crossing identity/nondegeneracy regression m=2..7; "
          "m=3 Gamma' has exactly one algebraic singularity in (0,1), "
          "bracket (4991/5000,9983/10000), coprime to quotient determinant numerator")
    for m,z in dets.items():
        print(f"m={m} crossing_det={z}")

if __name__=="__main__":
    main()
