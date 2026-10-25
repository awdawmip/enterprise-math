#!/usr/bin/env python3
"""Exact independent test: D25 signed Toeplitz residues / infinity compensation."""
from fractions import Fraction as Q
from math import factorial as f, isqrt, comb


def rational(m):
    L,U=m+1,2*m
    v={j:Q((-1)**(m+j+1)*f(m)*f(j-m-1)*f(2*m),
           f(2*m-j)*f(j)**2*2**j) for j in range(L,U+1)}
    g={l:Q(2*f(m)*f(2*m)*f(l-1)**2*2**l,
           f(l+m)*f(l+2*m)) for l in range(1,U+1)}
    return v,g


def evaluate(v,g,m):
    L,U=m+1,2*m
    H={}
    for j,vj in v.items():
        for l,gl in g.items():
            n=l-j
            H[n]=H.get(n,Q(0))+vj*gl
    residue_zero=sum(((1-6*n)*c for n,c in H.items() if n<=0),Q(0))
    residue_one=sum(((6*n-1)*c for n,c in H.items()),Q(0))
    residue_infinity=-sum(((6*n-1)*c for n,c in H.items() if n>=1),Q(0))
    direct_lower=sum((vj*gl*(6*(j-l)+1)
                       for j,vj in v.items() for l,gl in g.items() if l<=j),Q(0))
    direct_upper=sum((vj*gl*(6*(l-j)-1)
                       for j,vj in v.items() for l,gl in g.items() if l>j),Q(0))
    F=sum(v.values(),Q(0));G=sum(g.values(),Q(0))
    Fp=-sum((j*vj for j,vj in v.items()),Q(0))
    Gp=sum((l*gl for l,gl in g.items()),Q(0))
    moment=F*G-6*(Fp*G+F*Gp)
    A=J=prefix=Q(0)
    for l in range(L,U+1):
        if l>L:
            A+=v[l-1];J+=(l-1)*v[l-1]
            prefix+=g[l]*((6*l-1)*A-6*J)
    assert residue_zero==direct_lower
    assert residue_infinity==-direct_upper
    assert residue_one==6*(Fp*G+F*Gp)-F*G
    assert residue_zero+residue_one+residue_infinity==0
    assert direct_lower==moment+direct_upper==moment+prefix
    if m==1:
        assert direct_upper==0
    else:
        bound=5*v[L]*g[L+1]
        assert direct_upper>=bound>0
        assert (direct_upper==bound)==(m==2)
    if m>=3:
        c=Q((-1)**(3*m),2**(3*m))
        oa=c*(2*m+3)*comb(3*m+1,3*m)
        ob=c*(2*m+4)*comb(3*m+2,3*m)
        assert 10*ob-44*oa==c*(3*m+1)*(30*m*m-8*m-92)!=0
    return direct_upper


def primes(bound):
    return [p for p in range(7,bound+1)
            if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]


def finite_field(p):
    m=(p-1)//6; L,U=m+1,2*m
    fact=[1]*p
    for k in range(1,p):fact[k]=fact[k-1]*k%p
    inv=lambda d:pow(d%p,-1,p)
    v={j:(-1)**(m+j+1)*fact[m]*fact[j-m-1]*fact[2*m]
            *inv(fact[2*m-j]*fact[j]*fact[j]*pow(2,j,p))%p
       for j in range(L,U+1)}
    g={l:2*fact[m]*fact[2*m]*fact[l-1]**2*pow(2,l,p)
            *inv(fact[l+m]*fact[l+2*m])%p
       for l in range(1,U+1)}
    lower=sum((6*(j-l)+1)*v[j]*g[l] for j in v for l in g if l<=j)%p
    upper=sum((6*(l-j)-1)*v[j]*g[l] for j in v for l in g if l>j)%p
    F=sum(v.values())%p;G=sum(g.values())%p
    dF=-sum(j*v[j] for j in v)%p
    dG=sum(l*g[l] for l in g)%p
    moment=(F*G-6*(dF*G+F*dG))%p
    A=J=prefix=0
    for l in range(L,U+1):
        if l>L:
            A=(A+v[l-1])%p
            J=(J+(l-1)*v[l-1])%p
            prefix=(prefix+g[l]*((6*l-1)*A-6*J))%p
    assert lower==(moment+upper)%p and upper==prefix,(p,lower,moment,upper)
    return upper


if __name__=='__main__':
    for m in range(1,31):evaluate(*rational(m),m)
    pp=primes(997)
    observed={p:finite_field(p) for p in pp}
    assert len(pp)==80 and [p for p,c in observed.items() if c==0]==[7,199]
    assert observed[13]==11 and observed[19]==18
    assert evaluate(*rational(2),2)==Q(1,630)
    print('PASS: 30 exact rational cases, 80 independently reconstructed finite fields; residues/positivity/prefix/fiber.')
    print('p=13,19,199:',*[observed[p] for p in (13,19,199)])
