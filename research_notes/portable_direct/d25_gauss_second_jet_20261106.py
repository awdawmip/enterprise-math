"""Exact p-adic two-jet of the Gauss–Legendre factor for D25.
Pure standard-library, integral residues, no floating arithmetic."""
from math import comb

def primes(n):
    out=[]
    for p in range(5,n+1):
        if all(p%d for d in range(2,int(p**.5)+1)):
            out.append(p)
    return out

def residues(p):
    assert p%6==1
    m=(p-1)//6; M=p**3; M2=p*p
    fac=[1]*(p+1)
    for i in range(1,p+1):fac[i]=fac[i-1]*i%M
    H=[0]*(2*m+1); H2=[0]*(2*m+1)
    for i in range(1,2*m+1):
        H[i]=(H[i-1]+pow(i,-1,M2))%M2
        H2[i]=(H2[i-1]+pow(i,-2,p))%p
    P=0; C1=0; C2=0; K0=0; D1=0
    en=1
    for n in range(m+1):
        f=comb(m,n)*comb(2*m,n)*pow(2,-n,M)%M
        A=(H[m]-H[m-n])%M2; B=(H[2*m]-H[2*m-n])%M2
        A2=(H2[m]-H2[m-n])%p; B2=(H2[2*m]-H2[2*m-n])%p
        c1=f*(B-A)*pow(6,-1,M2)%M2
        c2=f*(A*A+4*A*B-5*B*B-A2+5*B2)*pow(72,-1,p)%p
        C1=(C1+c1)%M2; C2=(C2+c2)%p
        D1=(D1+(1+12*n)*c1)%M2
        P=(P+en)%M; K0=(K0+(1+12*n)*en)%M
        if n<m:
            en=en*(-m+n)*(2*m+1+2*n)*pow(4*(n+1)**2,-1,M)%M
    for n in range(m+1,2*m+1):
        numerator=fac[m]*fac[2*m]*fac[n-m-1]
        denominator=6*fac[2*m-n]*pow(2,n,M)*fac[n]*fac[n]
        b=(((-1)**(m+n))*numerator*pow(denominator,-1,M))%M
        D=((H[n-m-1]-H[m])*pow(6,-1,M2)-(H[2*m]-H[2*m-n])*pow(3,-1,M2))%M2
        C1=(C1+b)%M2; C2=(C2+b*D)%p
        D1=(D1+(1+12*n)*b)%M2
    for n in range(2*m+1,p):
        numerator=fac[m]*fac[2*m]*fac[n-m-1]*fac[n-2*m-1]
        denominator=18*pow(2,n,M)*fac[n]*fac[n]
        c=(((-1)**m)*numerator*pow(denominator,-1,M))%p
        C2=(C2+c)%p
    jet=(P+p*C1+p*p*C2)%M
    d=1; S=T=0; dsmall=[]
    for n in range(p):
        S=(S+d)%M;T=(T+n*d)%M;dsmall.append(d%p)
        if n<p-1:
            d=d*(6*n+1)*(3*n+1)*pow(36*(n+1)*(n+1),-1,M)%M
    K=(S+12*T)%M
    assert jet==S,(p,jet,S)
    assert (K0+p*D1)%M2==K%M2,(p,'K',K0,D1,K)
    prev=(1,0); curr=(0,1)
    inv2=pow(2,-1,M)
    O=None
    for n in range(1,2*m):
        nxt_a=((2*n+1)*curr[1]*inv2-n*prev[0])*pow(n+1,-1,M)%M
        nxt_b=((2*n+1)*curr[0]-n*prev[1])*pow(n+1,-1,M)%M
        prev,curr=curr,(nxt_a,nxt_b)
        if n==2*m-2: O=curr[1]
    Pleg=curr[0]
    if m==1: O=prev[1]
    if O is None: O=prev[1]
    assert curr[1]==0 and P==Pleg,(p,'legendre',P,Pleg,curr)
    K0_l=((2*p-1)*P-2*(p-1)*O)%M
    assert K0_l==K0,(p,'K0 Legendre',K0,K0_l,O)
    data=dict(p=p,m=m,P=P,C1=C1,C2=C2,S=S,K=K,K0=K0,D1=D1,quotient=(S//p if S%p==0 else None))
    if p%24 in (13,19):
        assert S%p==0 and P%p==0
        assert (P//p + C1 + p*C2)%M2 == S//p,(p,'quotient')
        e=pow(10,-1,p); E=R=J=0
        for i in range(1,m+1):
            if i>1:
                r=i-1
                e=e*36*r*r*pow((6*r+5)*(3*r+2),-1,p)%p
            E=(E+e)%p;R=(R+i*e)%p
            J=(J+dsmall[i]*((1+6*i)*E-6*R))%p
        ff=[1]*(3*p)
        for k in range(1,3*p):ff[k]=ff[k-1]*k%M
        W=0
        for n in range(p):
            an=ff[2*n]*ff[3*n]*pow(pow(216,n,M)*pow(ff[n],5,M),-1,M)%M
            W=(W+(6*n+1)*an)%M
        assert (S*K-2*p*p*J)%M==W,(p,'triangle')
        assert (jet*((K0+p*D1)%M2)-2*p*p*J)%M==W,(p,'jettriangle')
        data.update(J=J,W=W,second_digit_residue=(S//p*(K%M2)-(1+2*p*J))%M2)
    return data

if __name__=='__main__':
    tests=[p for p in primes(997) if p%6==1]
    out=[residues(p) for p in tests]
    print('primes',len(out),'target',sum(p['p']%24 in (13,19) for p in out))
    for x in out:
        if x['p'] in (7,13,19,31,67,373,997):print(x)
    assert all(x.get('second_digit_residue',0)==0 for x in out)
    print('ALL CHECKS PASSED')
