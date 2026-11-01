#!/usr/bin/env python3
"""Exact p-adic/Legendre checks for D25's even/odd mod-8 beta ports.
No external packages. Finite checks validate implementations, not universal statements.
"""
from math import comb, isqrt


def primes_up_to(n):
    return [p for p in range(5, n + 1) if all(p % d for d in range(2, isqrt(p) + 1))]


def legendre_port(p):
    # P_n(x) = 2^-n sum_j (-1)^j C(2n-2j,n) C(n,j) x^(n-2j).
    n = (p - 1) // 4 if p % 4 == 1 else (p - 3) // 4
    t = (p + 1) // 2 if n % 2 else 0
    inv2n = pow(2, -n, p)
    coefficients = [0] * p
    for j in range(n // 2 + 1):
        coeff = ((-1) ** j * comb(2*n-2*j, n) * comb(n, j) * inv2n) % p
        m = t + (n // 2) - j
        for k in range(m + 1):
            coefficients[k] = (coefficients[k] + coeff * (-1) ** k * comb(m,k)) % p
    return n, t, coefficients


def beta_coefficients(p):
    m = p*p
    c = [1]
    for k in range(p-1):
        factor = ((8*k+1) * (8*k+3) * pow(576*(k+1)**2, -1, m)) % m
        c.append(c[-1]*factor % m)
    return c


def bsum(p):
    m=p*p
    c=1
    total=0
    for k in range(p):
        total=(total+(8*k+1)*c)%m
        if k<p-1:
            c=(c*(4*k+1)*(4*k+3)*(2*k+1)*pow(288*(k+1)**3,-1,m))%m
    return total


def beta_boundary(beta,p):
    m=p*p
    suffix=[0]*(p+1)
    moment=[0]*(p+1)
    for i in range(p-1,-1,-1):
        suffix[i]=(suffix[i+1]+beta[i])%m
        moment[i]=(moment[i+1]+i*beta[i])%m
    return sum(beta[i]*((8*i+1)*suffix[p-i]+8*moment[p-i]) for i in range(p))%m


def legendre_at_19():
    # P4(sqrt(1-z))=1-5z+35/8*z^2, so at z=1/9 this is 323/648.
    p=19
    legendre_over_p=17*pow(648,-1,p)%p
    return legendre_over_p


def main():
    ps=primes_up_to(499)
    even_count=odd_count=0
    examples=[]
    for p in ps:
        m=p*p
        n,t,s=legendre_port(p)
        beta=beta_coefficients(p)
        assert all(beta[k]*pow(9,k,p)%p==s[k] for k in range(p)), ('Legendre',p)
        assert max(i for i,x in enumerate(s) if x%p) <p
        G=sum(beta)%m
        H=sum((16*k+1)*v for k,v in enumerate(beta))%m
        B=bsum(p)
        T=beta_boundary(beta,p)
        assert (G*H-T-B)%m==0, ('Clausen',p)
        chi=1 if p%3==1 else -1 # (-3/p) for p >3
        assert B == (p*chi)%m, ('Guo-Zudilin mod p2',p)
        if n%2==0:
            even_count+=1
            assert t==0 and p%8 in (1,3)
            assert all(beta[i]%m==0 for i in range((p+1)//2,p))
            assert T==0, ('boundary',p,T)
            assert G*H%m == (p*chi)%m
            assert (G%p==0) != (H%p==0)
            assert ((G*H)//p)%p == chi%p # G*H is integer product of residues
        else:
            odd_count+=1
            assert t==(p+1)//2 and p%8 in (5,7)
        if p in (11,13,17,19,23,37,43,67,73,139,373):
            examples.append((p,n,t,G,H,B,T))
    assert legendre_at_19()==18
    p=19
    beta=beta_coefficients(p)
    assert (sum(beta)%361, sum((16*k+1)*v for k,v in enumerate(beta))%361)==(171,131)
    assert (171//19)%19==9
    assert (9-18)%19==10  # beta-specific lift defect at z=1/9
    print('PASS full polynomial Legendre port: all',len(ps),'primes 5<=p<=499')
    print('PASS even-degree universal-valuation consequence:',even_count,'primes, odd-degree:',odd_count)
    print('PASS B=GH-T mod p^2 and published B congruence finite check:',len(ps))
    print('p n twist G_mod_p2 H_mod_p2 B_mod_p2 tail_mod_p2')
    for row in examples:
        print(*row)
    print('p19 exact: S(1/9)=323/648, S/19 mod19=18; G/19=9, defect=10; H mod19=17')


if __name__=='__main__':
    main()
