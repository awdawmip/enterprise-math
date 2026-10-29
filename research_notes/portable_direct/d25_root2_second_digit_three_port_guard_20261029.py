#!/usr/bin/env python3
"""D25 author-side exact p^2 three-port coefficients, CM Hasse no-go.

Pure integer arithmetic, external mathematical evidence; not native H0/B0,
Source CLAIM, formal Result or independent mathematical review.
"""
from math import comb, factorial


def primes_below(bound):
    s = bytearray(b"\1") * bound
    s[0:2] = b"\0\0"
    for d in range(2, int(bound**0.5)+1):
        if s[d]:
            s[d*d:bound:d] = b"\0" * len(range(d*d, bound, d))
    return [p for p in range(5, bound) if s[p]]


def hits(p):
    r1 = next(r for r in range(p) if (8*r+1) % p == 0)
    r3 = next(r for r in range(p) if (8*r+3) % p == 0)
    a, b = sorted((r1, r3))
    lam1 = ((8*r1+1)//p) * pow(8, -1, p) % p
    lam3 = ((8*r3+3)//p) * pow(8, -1, p) % p
    return r1, r3, a, b, lam1, lam3


def direct_beta(p):
    mod = p*p
    x = 1
    out = [x]
    for n in range(1, p):
        x = x*(8*n-7)*(8*n-5)*pow(64*n*n, -1, mod) % mod
        out.append(x)
    return out


def three_ports(p):
    r1, r3, a, b, lam1, lam3 = hits(p)
    mod = p*p
    iv = [0]+[pow(i, -1, p) for i in range(1, p)]
    fact = [1]
    for n in range(1, p):
        fact.append(fact[-1]*n % p)
    ifact = [pow(i, -1, p) for i in fact]
    def binom_p(n, k):
        return fact[n]*ifact[k]*ifact[n-k] % p

    P = [0]*p
    L = [0]*p
    M = [0]*p
    h1 = h3 = 0
    for n in range(a+1):
        if n:
            h1 = (h1+iv[r1-n+1]) % p
            h3 = (h3+iv[r3-n+1]) % p
        P[n] = comb(r1,n)*comb(r3,n) % mod
        L[n] = -P[n]*(lam1*h1+lam3*h3) % p
    lowlam = lam1 if r1 == a else lam3
    for n in range(a+1,b+1):
        M[n] = ((-1)**(a+n)*lowlam*binom_p(b,n)*
                fact[a]*fact[n-a-1]*ifact[n]) % p
    original = direct_beta(p)
    for n in range(p):
        assert original[n] == (P[n]+p*(L[n]+M[n])) % mod, (p,n)
    z = pow(9,-1,mod)
    PP = LL = MM = KK = 0
    power = 1
    for n in range(p):
        PP = (PP+P[n]*power) % mod
        LL = (LL+L[n]*power) % p
        MM = (MM+M[n]*power) % p
        KK = (KK+original[n]*power) % mod
        power = power*z % mod
    assert KK == (PP+p*(LL+MM)) % mod
    return PP, LL, MM, KK


def direct_integer_product_sum(p):
    """Independent raw Pochhammer numerator product, no three-port formula."""
    mod = p*p
    numerator = 1
    total = 0
    for n in range(p):
        if n:
            numerator *= (8*n-7)*(8*n-5)
        denominator = pow(576,n,mod)*(factorial(n)**2 % mod) % mod
        total = (total+numerator % mod * pow(denominator,-1,mod)) % mod
    return total


def mul_quad(x,y,m):
    # t^2 = t-1/36 in (Z/m)[t]/(36t^2-36t+1)
    a,b=x; c,d=y
    return ((a*c-b*d*pow(36,-1,m))%m, (a*d+b*c+b*d)%m)


def hasse_pair(p):
    mod=p*p; k=(p-1)//2
    inv4=pow(4,-1,mod)
    x=(inv4,-inv4%mod)
    power=(1,0); result=(0,0)
    for j in range(k//2+1):
        c=comb(k,2*j)*comb(2*j,j)
        result=((result[0]+c*power[0])%mod,
                (result[1]+c*power[1])%mod)
        power=mul_quad(power,x,mod)
    return result


def main():
    primes=primes_below(1000)
    counts={13:0,17:0,19:0,23:0}
    for p in primes:
        P,L,M,K=three_ports(p)
        if p%24 in counts:
            counts[p%24]+=1
            assert K%p == 0
            if p%24 in (13,23):
                assert K==0, ('Root2 finite check',p)
            else:
                assert K!=0, ('negative control',p)
    print("PASS_D25_ROOT2_THREE_PORT_COEFFICIENTWISE_P2",len(primes),"primes p<1000")
    print("FINITE_CM_CLASS_COUNTS",counts)
    for p in (13,17,19,23,37,373):
        P,L,M,K=three_ports(p)
        assert direct_integer_product_sum(p)==K
        assert P%p==0 and K%p==0
        print("PORTS",p,"P/p",P//p,"L",L,"M",M,"K/p",K//p)
    for p in (13,23,373):
        h=hasse_pair(p)
        assert all(v%p==0 for v in h) and h!=(0,0)
        print("LIFTED_HASSE_CM_PAIR",p,"H/p",tuple(v//p for v in h))
    assert hasse_pair(13)==(26,52)
    assert hasse_pair(373)==(5222,10444)
    print("PASS_D25_NAIVE_HASSE_P2_TRANSFER_FALSIFIER",(13,373))


if __name__=="__main__":
    main()
