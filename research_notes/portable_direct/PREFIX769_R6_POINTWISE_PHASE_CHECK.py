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

def main():
    B=10**8
    lo,hi=5029710,5029720
    signs=[]
    def check(x):
        a,d,j=values(x,B)
        assert a>0 and d>0
        sign=(j>0)-(j<0)
        signs.append([x,sign])
        return sign
    assert check(lo)<0 and check(hi)>0
    while hi-lo>1:
        mid=(lo+hi)//2
        if check(mid)<0:lo=mid
        else:hi=mid
    assert check(lo)<0 and check(hi)>0
    A,D,_=values(lo,B)
    scale=10**15
    upper=A*scale//D+1
    assert A*scale<upper*D and (upper-1)*D<=A*scale
    with localcontext() as ctx:
        ctx.prec=45
        display=str(Decimal(A)/Decimal(D))
    result={
        "schema":"PREFIX769_POINTWISE_DIAGONAL_PHASE_V1",
        "frozen_science_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "auxiliary_model":"189-layer killed-Pascal BRC stopping / independent Erlang Gamma maximum",
        "survivor_nonzero_positions":9529,
        "last_layer_empty":True,
        "stationary_bracket":[f"{lo}/{B}",f"{hi}/{B}"],
        "derivative_signs":signs,
        "D_positive_at_checked_points":True,
        "D_whole_interval_positive_source":"PREFIX767 theorem D(u)>27787 for 251/5000 <= u <= 252/5000",
        "pointwise_u":f"{lo}/{B}",
        "Q_display":display,
        "exact_upper_q_c":f"{upper}/{scale}",
        "upper_numerator":upper,
        "claim":"q_c<=Q(u)<upper by a pointwise negative mixed curvature neighborhood for q>Q(u)",
        "stationary_uniqueness":"not established",
        "full_global_minimum":"not established",
        "native_X6_transfer":"not asserted",
        "review":"UNREVIEWED",
        "execution":"ALL_CHECKS_PASS PREFIX769"
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print("ALL_CHECKS_PASS PREFIX769")
    return result
if __name__=="__main__":main()
