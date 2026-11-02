#!/usr/bin/env python3
"""Independent replay of D25 author-side terminating Clausen gauge.
Run: python d25_clausen_gauge_replay_20261102.py --limit 3000
Standard-library exact Z/p^3 modular arithmetic; no Source/native execution.
"""
import argparse
import json
from math import comb

def primes(N):
    S=bytearray([1])*(N+1)
    S[:2]=b"\x00\x00"
    for d in range(2,int(N**0.5)+1):
        if S[d]:
            S[d*d::d]=bytes((N-d*d)//d+1)
    return [i for i in range(7,N+1) if S[i] and i%6==1]

def verify(p):
    m=(p-1)//6
    n=2*m
    M=p**3
    inv=lambda a:pow(a%M,-1,M)
    inv2=inv(2)
    h=[0]*(n+1)
    h2=[0]*(n+1)
    ii=[0]*(n+1)
    for k in range(1,n+1):
        ii[k]=inv(k)
        h[k]=(h[k-1]+ii[k])%M
        h2[k]=(h2[k-1]+ii[k]*ii[k])%M
    a=[1]
    for k in range(m):
        a.append(a[-1]*2*(k-m)*(k-2*m)*inv((2*k+2-p)*(k+1))%M)
    q=[0]*(n+1)
    for i,ai in enumerate(a):
        for j,aj in enumerate(a):
            q[i+j]=(q[i+j]+ai*aj)%M
    P=Pd=P0=C=Ct=j0=0
    beta=[]
    z=1
    for k,ak in enumerate(a):
        P=(P+ak*z)%M
        Pd=(Pd+2*k*ak*z)%M
        b=comb(m,k)*comb(2*m,k)*z%M
        beta.append(b%p)
        P0=(P0+b)%M
        C=(C+b*h[k])%M
        Ct=(Ct+k*b*h[k])%M
        j0=(j0+k*b)%M
        z=z*inv2%M
    assert (P-P0-p*inv2*C)%(p*p)==0
    H1=H2=Q=0
    z=1
    for k,qk in enumerate(q):
        v=(6*k+1)*qk*z%M
        Q=(Q+v)%M
        H1=(H1+v*h[k])%M
        H2=(H2+v*(9*h[k]**2-5*h2[k]))%M
        z=z*inv2%M
    assert Q==P*(P+6*Pd)%M
    Xi=sum((1+6*(i+j))*bi*bj*(h[i+j]-h[i]-h[j])
           for i,bi in enumerate(beta) for j,bj in enumerate(beta))%p
    assert H1%p==(2*(P0*C+6*(P0*Ct+j0*C))+Xi)%p
    direct=1
    gauge=1
    z=1
    sums=[0,0,0]
    check=[0,0,0]
    for k in range(n+1):
        if k:
            gauge=gauge*(1-p*inv2*ii[k])*(1-p*ii[k])%M
        series=(1-3*p*inv2*h[k]+p*p*inv(8)*(9*h[k]**2-5*h2[k]))%M
        from_gauge=q[k]*z*gauge%M
        from_series=q[k]*z*series%M
        assert direct==from_gauge==from_series,(p,k)
        for ell in range(3):
            sums[ell]=(sums[ell]+pow(k,ell,M)*(6*k+1)*direct)%M
            check[ell]=(check[ell]+pow(k,ell,M)*(6*k+1)*from_series)%M
        if k<n:
            direct=direct*(-1)*(3*m-k)*(2*m-k)*(4*m-k)*inv(2*(k+1)**3)%M
        z=z*inv2%M
    assert sums==check
    A0=sums[0]
    assert A0==(Q-3*p*inv2*H1+p*p*inv(8)*H2)%M
    target=(p%24 in (13,19))
    if target:
        assert P%p==P0%p==A0%p==0
        cp=(P0//p)%p
        J=j0%p
        assert J!=0
        assert (P//p)%p==(cp+inv2*C)%p
        assert Pd%p==2*J%p
        digit=(A0//p)%p
        assert digit==(6*(P//p)*Pd-3*inv2*H1)%p
        assert digit==(12*J*(cp-C)-3*inv2*Xi)%p
        tcm=-cp*pow(2*J,-1,p)%p
    else:
        cp=tcm=digit=None
    if p in (7,13,19,37,43,373,1171):
        assert A0==sum((6*k+1)*(-1 if k%2 else 1)
                 *comb(3*m,k)*comb(2*m,k)*comb(4*m,k)*pow(2,-k,M)
                 for k in range(n+1))%M
    return dict(p=p,m=m,cm=target,A0=A0,c=cp,j=j0%p,t_CM=tcm,
                C=C%p,Xi=Xi,H1=H1%p,H2=H2%p,A0_over_p=digit)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--limit",type=int,default=3000)
    args=ap.parse_args()
    rows=[verify(p) for p in primes(args.limit)]
    out={"limit":args.limit,"primes":len(rows),
         "target_count":sum(x["cm"] for x in rows),
         "coefficient_positions":sum(2*x["m"]+1 for x in rows),
         "nonzero_target_Xi":sum(x["Xi"]!=0 for x in rows if x["cm"]),
         "nonzero_target_H2":sum(x["H2"]!=0 for x in rows if x["cm"]),
         "selected":{str(x["p"]):x for x in rows if x["p"] in (7,13,19,37,43,373,1171)},
         "mismatches":0}
    print(json.dumps(out,indent=2))
if __name__=="__main__":
    main()
