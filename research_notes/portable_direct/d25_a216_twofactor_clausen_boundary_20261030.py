"""A216 two-factor Clausen cutoff certificate, Z/p^3Z, original index/weight.
Author-side exact check; not a native H0/B0 experiment or accepted Result.
"""
from math import comb


def primes(limit):
    for p in range(7, limit):
        if p % 6 == 1 and all(p % d for d in range(2, int(p**0.5)+1)):
            yield p


def certificate(p):
    assert p > 3 and p % 6 == 1
    m, M = (p-1)//6, p**3
    z, zp = pow(2,-1,M), [1]
    for _ in range(p+m):
        zp.append(zp[-1]*z%M)
    g, G, Gprime, coeff = 1, 0, 0, []
    for k in range(p):
        coeff.append(g)
        G = (G+g*zp[k]) % M
        if k: Gprime = (Gprime+k*g*zp[k-1])%M
        if k+1 < p:
            g = g*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,M)%M

    fact = [1]*p
    for k in range(1,p): fact[k]=fact[k-1]*k%p
    c = [0]*p
    for k in range(2*m+1,p):
        c[k] = ((-1)**m * fact[m]*fact[2*m]*fact[k-m-1]
                *fact[k-2*m-1]*pow(18*fact[k]**2,-1,p))%p
        assert coeff[k]%(p*p)==0 and coeff[k]//(p*p)%p==c[k]

    # Retain both labeled source indices in the n>=p cutoff port.
    tail = 0
    for i in range(1,m+1):
        Pi = comb(m,i)*comb(2*m,i)%p
        for k in range(p-i,p):
            tail += 2*(6*(i+k)+1)*Pi*c[k]*zp[i+k]
    tail%=p

    # Independently evaluate the frozen reflected R port from its own
    # rising-factorial recurrence (C_1=1/10), NOT the new factorial c[k].
    ca, sum_ca, sum_aca, reflected = pow(10,-1,p), 0, 0, 0
    for i in range(1,m+1):
        if i>1:
            a=i-1
            ca=ca*36*a*a*pow((6*a+5)*(3*a+2),-1,p)%p
        sum_ca=(sum_ca+ca)%p
        sum_aca=(sum_aca+i*ca)%p
        bi=coeff[i]*zp[i]%p
        reflected=(reflected+2*bi*((6*i+1)*sum_ca-6*sum_aca))%p
    assert reflected==tail,(p,reflected,tail)

    # Independent original factorial/binomial A216 expression.
    original = sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n)
                   *pow(216,-n,M) for n in range(p))%M
    rhs = (G*G + 6*G*Gprime - p*p*tail)%M
    assert original==rhs,(p,original,rhs)
    if p%24 in (13,19):
        assert G%p==0
        h=G//p
        assert (6*h*Gprime+p*(h*h-tail))%(p*p)==original//p%(p*p)
    return dict(p=p,m=m,A=original,G=G,Gprime_mod_p2=Gprime%(p*p),
                boundary_mod_p=tail,frozen_R_mod_p=reflected,
                CM_zero=G%p==0)


if __name__=='__main__':
    data=[certificate(p) for p in primes(500)]
    print('PASS_TWOFACTOR_EXACT_CLAUSEN_CUTOFF',len(data))
    print('TARGET_COUNT',sum(x['p']%24 in (13,19) for x in data))
    for p in (7,13,19,31,37,43,61,109,157,373):
        print('CERT',certificate(p))
