"""PREFIX768 exact BRC-width Gamma diagonal derivative and local square certificate.
Standalone stdlib Python 3; science pin enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
from decimal import Decimal,localcontext
import json

N,W=189,1<<18

@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(W-x)**(n-k)>W**n

@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    m=k*W//n
    assert inside(n,k,m)
    if k==0:lo=hi=0
    else:
        a,b=0,m
        while b-a>1:
            t=(a+b)//2
            if inside(n,k,t):b=t
            else:a=t
        lo,hi=a,b
    a,b=m,W
    while b-a>1:
        t=(a+b)//2
        if inside(n,k,t):a=t
        else:b=t
    if 4*(a-hi)>W:return True
    if 4*(b-lo)<W:return False
    raise ArithmeticError((n,k))

rows=[{0:1}]
for n in range(1,N+1):
    c=defaultdict(int)
    for k,v in rows[-1].items():c[k]+=v;c[k+1]+=v
    rows.append({k:v for k,v in c.items() if wide(n,k)})
assert not rows[-1] and sum(map(len,rows[:N]))==9529

@lru_cache(None)
def scaled(x,B):
    P=[1];Q=[1]
    for _ in range(N):P.append(P[-1]*x);Q.append(Q[-1]*(B-x))
    U=[];U1=[];U2=[]
    for n,row in enumerate(rows[:N]):
        s=d=e=0
        for k,v in row.items():
            j=n-k
            s+=v*P[k]*Q[j]
            if k:d+=v*k*P[k-1]*Q[j]
            if j:d-=v*j*P[k]*Q[j-1]
            if k>=2:e+=v*k*(k-1)*P[k-2]*Q[j]
            if k and j:e-=2*v*k*j*P[k-1]*Q[j-1]
            if j>=2:e+=v*j*(j-1)*P[k]*Q[j-2]
        U.append(s*B**(188-n));U1.append(d*B**(189-n));U2.append(e*B**(190-n))
    return U,U1,U2

@lru_cache(None)
def kernels():
    return [tuple(comb(i+j,i) << (376-i-j) for j in range(i,N)) for i in range(N)]

def bilinear(v,w,wantL=False):
    C=L=0
    for i,row in enumerate(kernels()):
        vi,wi=v[i],w[i]
        for h,t in enumerate(row):
            j=i+h
            vterm=vi*w[j] if i==j else vi*w[j]+v[j]*wi
            term=t*vterm
            C+=term
            if wantL:L+=(i+j+1)*term
    return (C,L) if wantL else C

def values(x,B):
    H=B**188; T=1<<377; E=H*H*T
    U,U1,U2=scaled(x,B)
    A,Ldd=bilinear(U1,U1,True)
    m=2*sum(U)*H*T-bilinear(U,U)
    v=sum(U1)*H*T-bilinear(U1,U)
    D=Ldd*E+2*v*v-2*m*A
    A1,L1=bilinear(U2,U1,True); A1*=2; L1*=2
    v1=sum(U2)*H*T-bilinear(U2,U)-A
    D1=L1*E+4*v*v1-4*v*A-2*m*A1
    return A*E,D,A1*D-A*D1

def transverse():
    B=10**8;u=5029714
    H=B**188;T=1<<377;E=H*H*T
    s,d,e=scaled(u,B)
    P=[1];R=[1]
    for _ in range(N):P.append(P[-1]*u);R.append(R[-1]*(B-u))
    f=[]
    for n,row in enumerate(rows[:N]):
        z=0
        for k,v in row.items():
            j=n-k
            if k>=3:z+=v*k*(k-1)*(k-2)*P[k-3]*R[j]
            if k>=2 and j:z-=3*v*k*(k-1)*j*P[k-2]*R[j-1]
            if k and j>=2:z+=3*v*k*j*(j-1)*P[k-1]*R[j-2]
            if j>=3:z-=v*j*(j-1)*(j-2)*P[k]*R[j-3]
        f.append(z*B**(191-n))
    A0,B0=bilinear(d,d,True)
    m=2*sum(s)*H*T-bilinear(s,s)
    v=sum(d)*H*T-bilinear(d,s)
    D0=B0*E+2*v*v-2*m*A0
    m2=sum(e)*H*T-bilinear(e,s)+A0
    two_vp2=sum(f)*H*T-bilinear(f,s)+bilinear(e,d)
    A2=bilinear(f,d)-bilinear(e,e)
    B2=bilinear(f,d,True)[1]-bilinear(e,e,True)[1]
    D2=B2*E+2*v*two_vp2-2*m2*m2-2*m2*A0-2*m*A2
    F=A2*D0-A0*D2
    assert A0>0 and D0>0 and 21*D0**2<F*E<22*D0**2
    with localcontext() as ctx:
        ctx.prec=32
        display=str(Decimal(F*E)/Decimal(D0**2))
    result={
        "schema":"PREFIX770_TRANSVERSE_PHASE_COEFFICIENT_V1",
        "frozen_science_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "auxiliary_model":"external BRC killed-Pascal 189-layer independent Gamma maximum",
        "base_diagonal_u":"5029714/100000000",
        "transverse_path":"p=u+t,z=u-t",
        "even_symmetry":"Q(u+t,u-t)=Q(u-t,u+t)",
        "survivor_nonzero_positions":9529,
        "Q2_strict_exact":"21<Q2<22",
        "Q2_decimal_display":display,
        "Q2_formula":"Q2 = E*(A2*D0-A0*D2)/D0**2",
        "local_transverse_minimum":"strict at this rational u for sufficiently small t",
        "stationary_unique":"not proved",
        "global_qc_attained":"not proved",
        "review":"UNREVIEWED",
        "execution":"ALL_CHECKS_PASS PREFIX770 TRANSVERSE"
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print("ALL_CHECKS_PASS PREFIX770 TRANSVERSE")
    return result
if __name__=="__main__":transverse()
