#!/usr/bin/env python3
"""D25 A/B coefficientwise p^3 Clausen/Euler fold and projected cutoff checks."""
from math import comb

def primes(n):
    s=bytearray(b"\1")*(n+1);s[0:2]=b"\0\0"
    for i in range(2,int(n**.5)+1):
        if s[i]:s[i*i::i]=b"\0"*(((n-i*i)//i)+1)
    return [i for i in range(5,n+1) if s[i]]

def at(v,x,M,weighted=False):
    a=0;t=1
    for n,c in enumerate(v):
        a=(a+t*c*(n if weighted else 1))%M;t=t*x%M
    return a

def calc(p,kind,poly=False,raw=False):
    assert kind in "AB"
    M=p**3
    if kind=="A":
        assert p%6==1
        m=(p-1)//6;cut=2*m; x=pow(2,-1,M)
        param=(1,3);scale=18;uparam=(0,)
        den=18;weight=6;rat=216;euler=False
    else:
        assert p%8 in (3,5)
        k=(p-3)//8 if p%8==3 else (p-5)//8
        cut=3*k+1; x=pow(9,-1,M);euler=p%8==5
        param=(5,7) if euler else (1,3)
        scale=64;den=32;weight=8;rat=2304
    g=[1];u=[1]
    for n in range(p-1):
        v=n+1
        if kind=="A":
            g.append(g[-1]*(6*n+1)*(3*n+1)*pow(18*v*v,-1,M)%M)
            u.append(u[-1]*(2*n+1)*(3*n+1)*(3*n+2)*pow(18*v*v*v,-1,M)%M)
        else:
            g.append(g[-1]*(8*n+param[0])*(8*n+param[1])*pow(64*v*v,-1,M)%M)
            u.append(u[-1]*(4*n+1)*(2*n+1)*(4*n+3)*pow(32*v*v*v,-1,M)%M)
    for n in range(cut+1,p):assert g[n]%(p*p)==0
    Q=at(g[:cut+1],x,M);DQ=at(g[:cut+1],x,M,True)
    S=at(u,x,M);weightedS=(S+weight*at(u,x,M,True))%M
    x0=x%p
    pref=[0]*p;dpref=[0]*p;t=1
    for n in range(p):
        val=(g[n]//(p*p))*t%p if n>cut else 0
        pref[n]=(val+(pref[n-1] if n else 0))%p
        dpref[n]=(n*val+(dpref[n-1] if n else 0))%p
        t=t*x0%p
    P0=D0=P1=D1=0;t=1
    for i in range(cut+1):
        a=g[i]*t%p;h=p-1-i
        P0=(P0+a*pref[h])%p
        D0=(D0+a*(i*pref[h]+dpref[h]))%p
        if h>0:
            P1=(P1+a*pref[h-1])%p
            D1=(D1+a*(i*pref[h-1]+dpref[h-1]))%p
        t=t*x0%p
    P=(P0-x0*P1)%p if euler else P0
    DP=(D0-x0*(D1+P1))%p if euler else D0
    low=(1-x)*Q*Q%M if euler else Q*Q%M
    if kind=="A":weightedLow=(Q*Q+12*Q*DQ)%M
    elif euler:weightedLow=((1-9*x)*Q*Q+16*(1-x)*Q*DQ)%M
    else:weightedLow=(Q*Q+16*Q*DQ)%M
    assert S==(low+2*p*p*P)%M,(p,kind,"value")
    assert weightedS==(weightedLow+2*p*p*(P+weight*DP))%M,(p,kind,"weighted")
    if poly:
        q=g[:cut+1]
        for n in range(p):
            def cv(j):
                if j<0:return 0
                low=sum(q[i]*q[j-i] for i in range(max(0,j-cut),min(j,cut)+1))
                hi=2*sum((q[i]%p)*(g[j-i]//(p*p))
                    for i in range(min(j,cut)+1) if cut<j-i<p)
                return (low+p*p*hi)%M
            value=cv(n)-(cv(n-1) if euler else 0)
            assert u[n]==value%M,(p,kind,n)
    if raw:
        t=1;v=0;inv=pow(rat,-1,M)
        for n in range(p):
            coefficient=comb(2*n,n)**2*(comb(3*n,n) if kind=="A" else comb(4*n,2*n))
            v=(v+(weight*n+1)*coefficient*t)%M;t=t*inv%M
        assert weightedS==v,(p,kind,"raw")
    return dict(p=p,kind=kind,root=Q%p==0,weighted=weightedS,
                overflow=(2*(P+weight*DP))%p,gauss=weightedLow)

def main():
    tested={"A":[7,13,19,31,37,43,67,73,97,139,373],
            "B":[13,19,37,43,67,139,373]}
    for kind,ps in tested.items():
        for p in ps:calc(p,kind,poly=True,raw=p in [13,19,43,67,373])
    target=[p for p in primes(2500) if p%24 in (13,19)]
    rows={}
    for p in target:
        a=calc(p,"A");b=calc(p,"B")
        assert a["root"] and b["root"]
        assert a["weighted"]==p and b["weighted"]==p
        if p in (13,19,43,67,373):
            ea=a["overflow"];eb=b["overflow"]
            dif=(a["gauss"]-b["gauss"])%(p**3)
            assert dif%(p*p)==0
            digit=dif//(p*p)
            assert (digit+ea-eb)%p==0
            rows[p]=(ea,eb,(ea-eb)%p,digit)
    assert rows=={13:(9,0,9,4),19:(13,8,5,14),
                  43:(31,33,41,2),67:(30,46,51,16),
                  373:(1,220,154,219)}
    print("PASS: A-11/B-7 polynomial p^3; five raw-binomial cases; %d target primes; cross-source cancellation"%len(target))
    print(rows)

if __name__=="__main__":main()
