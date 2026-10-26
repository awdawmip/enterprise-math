#!/usr/bin/env python3
"""Finite signed original-E3 CM-to-binomial diagnostic; not native H0/B0.

For p % 24 in {13,17,19,23}, compare the p^3 unweighted 3F2
U=sum C(2n,n)^2*C(3n,n)/216^n with the norm of the *original*
E3 formal invariant differential coefficient H_{3,p-1}(t),
t=(2-T)/4, T^2=2. The tested identity is
 U == -Legendre(2,p) * Norm(H) (mod p^3).
This verifies a finite range, not a universal theorem.
"""
from hashlib import sha256
from math import comb


def primes_under(bound):
    sieve = bytearray(b'\x01') * bound
    sieve[:2] = b'\x00\x00'
    for q in range(2, int(bound**0.5) + 1):
        if sieve[q]:
            sieve[q*q:bound:q] = b'\x00' * len(range(q*q,bound,q))
    return (p for p in range(5, bound) if sieve[p])


def times(a, b, modulus):
    return ((a[0]*b[0]+2*a[1]*b[1])%modulus,
            (a[0]*b[1]+a[1]*b[0])%modulus)


def compute(p):
    assert p > 3 and p % 24 in (13,17,19,23)
    mod=p**3
    a=1
    U=W=0
    # A_{n+1}/A_n = (2n+1)(3n+1)(3n+2)/(36(n+1)^3).
    for n in range(p):
        U=(U+a)%mod
        W=(W+(6*n+1)*a)%mod
        if n<p-1:
            den=36*(n+1)**3
            a=a*(2*n+1)*(3*n+1)*(3*n+2)*pow(den,-1,mod)%mod
    inv108=pow(108,-1,mod)
    c=(2*inv108%mod,-inv108%mod)  # (2-T)/108
    H=(0,0)
    cpower=(1,0)
    f=1
    last=(p-1)//3
    # H=sum_{j<=last} C(2j,j)*C(p-1-j,2j)*c^j.
    for j in range(last+1):
        H=((H[0]+f*cpower[0])%mod,(H[1]+f*cpower[1])%mod)
        if j<last:
            num=(p-1-3*j)*(p-2-3*j)*(p-3-3*j)
            den=(p-1-j)*(j+1)**2
            f=f*num*pow(den,-1,mod)%mod
            cpower=times(cpower,c,mod)
    norm=(H[0]*H[0]-2*H[1]*H[1])%mod
    sign=1 if p%24 in (13,19) else -1
    assert H[0]%p == H[1]%p == 0
    assert U%p**2 == norm%p**2 == 0
    assert (U-sign*norm)%mod == 0
    if sign==1:
        assert W==p  # independently known finite regression, NOT proof
    return (p,U,norm,W,H[0],H[1],sign)


def independent_binomial_crosscheck(row):
    p,U,N,W,h0,h1,sign=row
    mod=p**3
    inv216=pow(216,-1,mod)
    u2=w2=0
    power=1
    for k in range(p):
        v=comb(2*k,k)**2*comb(3*k,k)*power%mod
        u2=(u2+v)%mod
        w2=(w2+(6*k+1)*v)%mod
        power=power*inv216%mod
    assert (u2,w2)==(U,W)
    inv108=pow(108,-1,mod)
    c=(2*inv108%mod,-inv108%mod)
    h=(0,0)
    z=(1,0)
    for j in range((p-1)//3+1):
        a=comb(2*j,j)*comb(p-1-j,2*j)
        h=((h[0]+a*z[0])%mod,(h[1]+a*z[1])%mod)
        z=times(z,c,mod)
    assert h==(h0,h1)
    assert (h[0]**2-2*h[1]**2)%mod==N


def main():
    rows=[compute(p) for p in primes_under(2500)
          if p%24 in (13,17,19,23)]
    for row in rows:
        if row[0] in (13,17,19,23,37,41,43,47,211,373):
            independent_binomial_crosscheck(row)
    payload=''.join(','.join(map(str,row))+'\n' for row in rows).encode('ascii')
    print('SIGNED_ORIGINAL_E3_UNWEIGHTED_FINITE_CERTIFICATE_PASS')
    print('count:',len(rows))
    print('by residue:',{r:sum(p%24==r for p,*_ in rows)
                          for r in (13,17,19,23)})
    print('row_ledger_sha256:',sha256(payload).hexdigest())
    print('row_layout: p,U_mod_p3,NormH_mod_p3,W_mod_p3,'
          'H0_mod_p3,H1_mod_p3,sign')
    for p,U,N,W,h0,h1,sign in rows:
        if p in (13,17,19,23,37,41,43,47,211,373):
            print('witness',p,'U/p2',U//p**2,'N/p2',N//p**2,
                  'sign',sign,'W_mod_p3',W)


if __name__=='__main__':
    main()
