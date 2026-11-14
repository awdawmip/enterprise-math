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

def derivative_sign(x,B):
    H=B**188; T=1<<377; E=H*H*T
    U,U1,U2=scaled(x,B)
    A,Ldd=bilinear(U1,U1,True)
    m=2*sum(U)*H*T-bilinear(U,U)
    v=sum(U1)*H*T-bilinear(U1,U)
    D=Ldd*E+2*v*v-2*m*A
    A1,L1=bilinear(U2,U1,True);A1*=2;L1*=2
    v1=sum(U2)*H*T-bilinear(U2,U)-A
    D1=L1*E+4*v*v1-4*v*A-2*m*A1
    num=A1*D-A*D1
    return -1 if num<0 else 1 if num>0 else 0,D>0

def main():
    B=10**7
    lo,hi=502900,503000
    checks=[]
    def check(x):
        sign,pos=derivative_sign(x,B)
        assert pos and sign!=0
        checks.append([x,sign])
        scaled.cache_clear()
        return sign
    assert check(lo)<0 and check(hi)>0
    for _ in range(7):
        x=(lo+hi)//2
        if x in (lo,hi):break
        if check(x)<0:lo=x
        else:hi=x
    assert lo==502971 and hi==502972
    H=B**188;T=1<<377;E=H*H*T
    u=scaled(lo,B)[0];w=scaled(hi,B)[0]
    d=[w_i-u_i for u_i,w_i in zip(u,w)]
    Cdd,Ldd=bilinear(d,d,True)
    maa=2*sum(u)*H*T-bilinear(u,u)
    mab=(sum(u)+sum(w))*H*T-bilinear(u,w)
    mbb=2*sum(w)*H*T-bilinear(w,w)
    delta_mu=-Cdd
    delta_var=-Ldd*E-(mbb*mbb-2*mab*mab+maa*maa)
    assert delta_mu==mbb-2*mab+maa
    assert delta_mu<0 and delta_var<0
    qnum=-delta_mu*E;qden=-delta_var
    assert qnum*10**12<28518591163*qden
    with localcontext() as ctx:
        ctx.prec=25
        display=str(Decimal(qnum)/Decimal(qden))
    result={"schema":"PREFIX768_R6_CERTIFICATE_V1",
        "science_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "model":"external 189-layer killed-Pascal BRC-Gamma two-clock auxiliary",
        "survivor_nonzero_positions":9529,
        "bracket":[f"{lo}/{B}",f"{hi}/{B}"],
        "bracket_width":f"{hi-lo}/{B}",
        "derivative_sign_checks":checks,
        "D_positive_at_all_check_points":True,
        "D_positive_on_full_interval":"PREFIX767 certificate D>27787 on [251/5000,252/5000]",
        "rectangle":[f"{lo}/{B}",f"{hi}/{B}"],
        "delta_mu_sign":"negative","delta_variance_sign":"negative",
        "q_R_display":display,"q_R_upper_exact":"28518591163/1000000000000",
        "q_c_upper_proved":"q_c<28518591163/1000000000000",
        "stationary_root_uniqueness_proved":False,
        "native_X6_transfer":"not claimed","formal_review":"pending",
        "execution":"ALL_CHECKS_PASS PREFIX768"}
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print("ALL_CHECKS_PASS PREFIX768")
    return result
if __name__=="__main__":main()
