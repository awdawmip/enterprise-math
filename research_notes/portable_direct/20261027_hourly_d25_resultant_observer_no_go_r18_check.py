#!/usr/bin/env python3
"""Author exact checks for the original finite-face geometric-source resultant.

Scope: D25 portable low/high *finite* ordered carrier, NOT CM/Frobenius,
not native Source execution, not independent Driver review. No floats.
"""
from fractions import Fraction
from math import isqrt


def target_primes(max_p=997):
    return [p for p in range(7, max_p+1) if p%6==1
            and all(p%q for q in range(2, isqrt(p)+1))]


def trim(v):
    v=list(v)
    while v and v[-1]==0: v.pop()
    return v


def mul(a,b,p):
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            result[i+j]=(result[i+j]+x*y)%p
    return trim(result)


def mod_poly(a,b,p):
    a=trim(a)
    b=trim(b)
    assert b
    inverse=pow(b[-1],-1,p)
    while len(a)>=len(b):
        coefficient=(a[-1]*inverse)%p
        offset=len(a)-len(b)
        for i,bi in enumerate(b):
            a[i+offset]=(a[i+offset]-coefficient*bi)%p
        a=trim(a)
    return a


def gcd_poly(a,b,p):
    a,b=trim(a),trim(b)
    while b:
        a,b=b,mod_poly(a,b,p)
    return [(x*pow(a[-1],-1,p))%p for x in a] if a else []


def resultant(a,b,p):
    """Exact Sylvester resultant via polynomial Euclidean identity over F_p."""
    a,b=trim(a),trim(b)
    if not b:return 0,0
    accumulator=1
    steps=0
    while len(b)>1:
        n,m=len(a)-1,len(b)-1
        r=mod_poly(a,b,p)
        steps+=1
        if not r:return 0,steps
        accumulator=(accumulator * (-1 if n*m%2 else 1)
                     * pow(b[-1],n-(len(r)-1),p))%p
        a,b=b,r
    return accumulator*pow(b[0],len(a)-1,p)%p,steps


def evaluate(a,z,p):
    total=0
    for coefficient in reversed(a):total=(total*z+coefficient)%p
    return total


def derivatives(a,p):
    return [i*a[i]%p for i in range(1,len(a))]


def genuine_coefficients(p):
    m=(p-1)//6
    factorial=[1]*p
    for r in range(1,p):factorial[r]=factorial[r-1]*r%p
    inv=lambda x:pow(x%p,-1,p)
    a=[0]*(m+1)
    a[0]=1
    for j in range(1,m+1):
        k=j-1
        a[j]=a[j-1]*(6*k+1)*(3*k+1)*inv(18*j*j)%p
    C=(-1 if m%2 else 1)*factorial[m]*factorial[2*m]*inv(18)%p
    b=[0]*(2*m+1)
    for ell in range(1,2*m+1):
        r=p-ell
        b[ell]=(C*factorial[r-m-1]*factorial[r-2*m-1]
                 *inv(factorial[r]**2))%p
    return m,a,b


def polynomials(p):
    m,a,b=genuine_coefficients(p)
    # U=z^m A0, V=z^{-1} B0; these are independent one-sided sources.
    U=[a[m-i] for i in range(m)]
    V=[b[i+1] for i in range(2*m)]
    # Direct ordered-pair construction P=z^(m-1) O.
    P=[0]*(3*m-1)
    for j in range(1,m+1):
        for ell in range(1,2*m+1):
            index=ell-j+m-1
            P[index]=(P[index]+(j+ell)*a[j]*b[ell])%p
    P=trim(P)
    # Totally different construction, twisted Wronskian.
    UV=mul(U,V,p)
    W1=mul(U,derivatives(V,p),p)
    W2=mul(derivatives(U,p),V,p)
    W=[0]*max(len(UV),len(W1)+1,len(W2)+1)
    for i,x in enumerate(UV):W[i]=(W[i]+(m+1)*x)%p
    for i,x in enumerate(W1):W[i+1]=(W[i+1]+x)%p
    for i,x in enumerate(W2):W[i+1]=(W[i+1]-x)%p
    assert P==trim(W),p
    assert len(P)==3*m-1 and P[0]!=0 and P[-1]!=0,p
    return P


def original_rational_cells(p):
    """Return actual original ordered Z and four cutoff E as exact rationals."""
    m=(p-1)//6
    L,N=1-2*m,2*m-1
    theta=Fraction(-p,6)
    f=[Fraction(1)]
    for r in range(p-1):
        f.append(f[-1]*Fraction((6*r+1)*(3*r+1),18*(r+1)**2))
    beta={r:f[r]/p**2 for r in range(2*m+1,p)}
    Z,E={},{}
    for n in range(L,N+1):
        cells=[(j,j+n) for j in range(1,2*m+1) if 1<=j+n<=2*m]
        Z[n]=sum(((j+ell-p)*f[j]*beta[p-ell] for j,ell in cells),Fraction())
        if n>=0:
            E[n]=(2*(m+theta)**2*beta[p-n-1]
                  -(6*m*m-8*m*theta+2*theta**2)*f[2*m-n]*beta[4*m])
        else:
            E[n]=((20*m*m-14*m*theta+2*theta**2)*f[-n]*beta[p-1]
                  +(2*m*theta-2*theta**2)*f[2*m]*beta[p-(2*m+n+1)])
    for n in range(L,N+1):
        assert E[n]==(p-n)*Z[n]-(p-n-Fraction(1,2))*Z.get(n+1,Fraction())
    return L,N,Z,E


def original_fraction_ports(p,z):
    """Independent original-parameter rational f_r / p^2 and four real E sources."""
    L,N,Z,E=original_rational_cells(p)
    return tuple(sum((Fraction(z)**n * d[n] for n in range(L,N+1)),Fraction())
                 for d in (Z,E)) + (sum((n*Fraction(z)**n*Z[n]
                                        for n in range(L,N+1)),Fraction()),)


def mod_fraction(x,p,digits=2):
    q=p**digits
    return x.numerator*pow(x.denominator,-1,q)%q


def check():
    primes=target_primes()
    assert len(primes)==80
    exceptional=[]
    for p in primes:
        P=polynomials(p)
        D=derivatives(P,p)
        g=gcd_poly(P,D,p)
        if len(g)>1:exceptional.append((p,g))
        if p==733:
            res,steps=resultant(P,D,p)
            assert (res,steps)==(254,362),(res,steps)
            assert g==[1]
            assert evaluate(P,1,p)==204
            roots=[z for z in range(1,p) if evaluate(P,z,p)==0]
            assert roots==[2],roots
            m=(p-1)//6
            o=evaluate(P,2,p)*pow(2,1-m,p)%p
            j=evaluate(D,2,p)*pow(2,2-m,p)%p
            gg=(-(2-1)*pow(2,1-m,p)*evaluate(D,2,p))%p
            assert (o,j,gg)==(0,38,714),(o,j,gg)
        if p==19:
            # Genuine mod-p triple intersection; NOT a universal no-go.
            assert P==[8,9,16,15,3,8,12,6],P
            assert g==[17,12,1]
            assert P==mul(mul(mul([6,1],[6,1],p),[6,1],p),
                          [12,17,5,18,6],p)
            assert evaluate(P,13,p)==0
            assert evaluate(D,13,p)==0
            assert evaluate(derivatives(D,p),13,p)==0
            assert evaluate([i*derivatives(D,p)[i]%p
                             for i in range(1,len(derivatives(D,p)))],13,p)!=0
    assert exceptional==[(19,[17,12,1])],exceptional

    # Independent rational original sources, not just formal mod-p P.
    O,G,J=original_fraction_ports(19,13)
    assert tuple(mod_fraction(x,19,2) for x in (O,G,J))==(95,95,323)
    # Triple mod-19 O root => first two derivatives zero; no lift in 13+19 Z_19.
    for t in range(19):
        Ot,Gt,Jt=original_fraction_ports(19,13+19*t)
        assert tuple(mod_fraction(x,19,2) for x in (Ot,Gt))==(95,95)
    L,N,Z,E=original_rational_cells(19)
    # T_19(z)=z^5 O_19(z) is an integral polynomial; translate z=13+x.
    from math import comb
    taylor=[sum((Fraction(comb(n+5,k)) * 13**(n+5-k) * Z[n]
                 for n in range(L,N+1) if n+5>=k),Fraction())
            for k in range(11)]
    assert [mod_fraction(c,19,2) for c in taylor[:4]] == [247,304,342,122]
    print('PASS 80 primes: twisted-Wronskian/direct-pair coefficient agreement')
    print('squarefree exceptions in [7,997], p=1(mod6): p19 only')
    print('p733: degree 364, resultant(P,P\')=254 mod733; 362 Euclidean steps; P(1)=204; sole unit root z=2; G(2)=714')
    print('p19: triple z=13 root; all 19 lifts retain O=G=95 modulo 361; original four-face fractions audited')

if __name__=='__main__':check()
