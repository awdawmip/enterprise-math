"""Exact modular certificate: D25 corrected Clausen third Hasse source port.

F_p[t]/t^4 and original independent 3F2 coefficients mod p^4.
This is an author computation, not a native CM experiment or formal review.
"""
from math import factorial, isqrt


def prime(p):
    return p >= 2 and all(p % q for q in range(2, isqrt(p) + 1))


def mul(a, b, p):
    return [sum(a[j] * b[k-j] for j in range(k+1)) % p for k in range(4)]


def inv_series(a, p):
    inv = pow(a[0], -1, p)
    b = [inv]
    for k in range(1, 4):
        b.append(-inv * sum(a[j]*b[k-j] for j in range(1,k+1)) % p)
    return b


def divide(a, b, p):
    return mul(a, inv_series(b, p), p)


def sc(a, k, p):
    return [(k*v) % p for v in a]


def ports(p):
    m = (p-1)//6
    beta = [[1,0,0,0]]
    gamma = [[1,0,0,0]]
    for n in range(p-1):
        # Corrected 2F1 with c(x)=1/2-3x, x=m+t.
        # At t=0, c(m)=1-p/2, congruent to 1 mod p.
        b_num = mul([n-m,-1,0,0], [n-2*m,-2,0,0], p)
        b_den = sc([n+1,-3,0,0], n+1,p)
        beta.append(divide(mul(beta[-1],b_num,p),b_den,p))

        # Clausen 3F2 with denominators c(x) and -6x.
        g_num = mul(mul([n-2*m,-2,0,0], [n-3*m,-3,0,0],p),
                    [n-4*m,-4,0,0],p)
        g_den = mul([n+1,-3,0,0],[n+1,-6,0,0],p)
        g_den = sc(g_den,n+1,p)
        gamma.append(divide(mul(gamma[-1],g_num,p),g_den,p))
    return beta,gamma


def original_q(p):
    # (1/3)_n (1/2)_n (2/3)_n / (n!)^3 modulo p^4.
    modulus=p**4
    qs=[1]
    for n in range(p-1):
        factor=((3*n+1)*(2*n+1)*(3*n+2) *
                pow(18*(n+1)**3,-1,modulus)) % modulus
        qs.append(qs[-1]*factor % modulus)
    return qs


def check(p):
    if not prime(p) or p%6 != 1:
        raise ValueError("expected prime p = 1 mod 6")
    m=(p-1)//6
    beta,gamma=ports(p)
    original=original_q(p)
    fac=[factorial(n)%p for n in range(p)]
    inv216=pow(216,-1,p)
    conv_checks=0
    band_checks=0
    band_signed_convolution=0
    band_signed_original=0
    samples=[]
    for n in range(p):
        # Exact signed Cauchy convolution at four Hasse orders.
        con=[sum(sum(beta[j][a]*beta[n-j][k-a]
                     for a in range(k+1)) for j in range(n+1))%p
             for k in range(4)]
        assert con==gamma[n], (p,n,"Clausen",con,gamma[n])
        conv_checks+=4
        if n<=4*m:
            continue
        assert gamma[n][:3]==[0,0,0], (p,n,gamma[n])
        facprod=1
        for q in (2,3,4):
            facprod=facprod*fac[q*m]*fac[n-q*m-1]%p
        g3=(-24*(-1)**m*facprod*pow(fac[n]**3,-1,p))%p
        assert gamma[n][3]==g3, (p,n,"rank jet",gamma[n][3],g3)
        q3=(-inv216*g3)%p
        assert original[n]%(p**3)==0, (p,n,"valuation",original[n])
        assert original[n]//(p**3)==q3, (p,n,"original",original[n]//p**3,q3)
        weight=(6*n+1)*pow(2,-n,p)%p
        d=weight*q3%p
        band_signed_convolution=(band_signed_convolution+weight*(-inv216)*gamma[n][3])%p
        band_signed_original=(band_signed_original+weight*(original[n]//p**3))%p
        band_checks+=1
        if p in (7,13,19) or n==p-1:
            samples.append((n,g3,q3,d))
    endpoint=gamma[p-1][3]
    assert endpoint==(-pow(m,-3,p))%p
    assert original[p-1]//p**3 == p-1
    assert ((6*(p-1)+1)*pow(2,-(p-1),p) *
            (original[p-1]//p**3))%p == 5%p
    assert band_signed_convolution==band_signed_original
    return dict(p=p,m=m,clausen_jet_equalities=conv_checks,
                upper_band_terms=band_checks,band_sum_mod_p=band_signed_original,
                endpoint_gamma=endpoint,sample_n_gamma_q3_d=samples)


if __name__=="__main__":
    ps=[7,13,19,31,37,43,61,73,97,103,109,127,157,199,373]
    rs=[check(p) for p in ps]
    print("PASS",len(rs),"primes; Clausen coefficient-jet identities",
          sum(x["clausen_jet_equalities"] for x in rs),
          "; upper-band source terms",sum(x["upper_band_terms"] for x in rs))
    for r in rs:
        print("p=",r["p"],"band sum=",r["band_sum_mod_p"],
              "endpoint gamma3=",r["endpoint_gamma"],
              "samples=",r["sample_n_gamma_q3_d"] if r["p"] in (7,13,19) else "")
