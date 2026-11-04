#!/usr/bin/env python3
"""Exact p^2 Gauss-band injection and weighted-port certificate; author-side only."""
from math import isqrt, comb


def primes(limit):
    flags = bytearray(b'\x01') * (limit + 1)
    flags[0:2] = b'\x00\x00'
    for i in range(2, isqrt(limit)+1):
        if flags[i]:
            flags[i*i:limit+1:i] = b'\x00' * ((limit-i*i)//i+1)
    return [p for p in range(5, limit+1) if flags[p] and p % 8 == 5]


def test(p):
    q=(p-5)//8
    L=5*q+3; M=7*q+4
    m=p*p
    v=[1]*p; b=[1]*p
    inv576=pow(576,-1,m)
    for k in range(p-1):
        v[k+1]=v[k]*(8*k+1)*(8*k+3)*inv576*pow((k+1)**2,-1,m)%m
        b[k+1]=b[k]*(4*k+1)*(4*k+2)*(4*k+3)*inv576*pow((k+1)**3,-1,m)%m
    assert all(v[k]%p for k in range(L+1))
    assert all(v[k]%p==0 and (p==5 or v[k]%(p*p)!=0) for k in range(L+1,M+1))
    assert all(v[k]==0 for k in range(M+1,p))
    sigma=10*(v[L]%p)*pow(441,-1,p)%p
    r=[0]*(M-L)
    r[0]=sigma
    h=sigma
    for s in range(M-L-1):
        r[s+1]=r[s]*(8*s+8)*(8*s+10)*pow(576*(L+2+s)**2,-1,p)%p
        h=h*16*(s+1)*(4*s+5)*pow(9*(8*s+15)**2,-1,p)%p
        assert h==r[s+1], ("hypergeometric coefficient",p,s)
    assert all(v[L+1+s]//p==r[s] for s in range(M-L))
    U=sum(v[:L+1])%m
    DU=sum(k*v[k] for k in range(L+1))%m
    R=sum(r)%p
    DR=sum((L+1+s)*r[s] for s in range(len(r)))%p
    S=sum(v)%m
    D=sum(k*v[k] for k in range(p))%m
    assert S==(U+p*R)%m and D==(DU+p*DR)%m
    total=(S*(S+16*D))%m
    unit=(U*(U+16*DU))%m
    carry=(R*(2*U+16*DU)+16*U*DR)%p
    assert total==(unit+p*carry)%m
    V=sum((8*k+1)*b[k] for k in range(p))%m
    chi=1 if pow(p-3,(p-1)//2,p)==1 else -1
    assert V==(p*chi)%m,('known GZ quartic theorem finite check',p,V)
    assert unit%p==0,('source unit product mod p',p,unit)
    triangle=(total-V)%m
    assert triangle%p==0
    normalized=(unit//p+carry-chi)%p
    assert normalized==triangle//p
    if p<=157:
        brute=sum((8*(i+j)+1)*v[i]*v[j] for i in range(p) for j in range(p-i,p))%m
        assert triangle==brute,('Clausen strict triangle',p)
    if p in (5,13,29,37,53,61,101):
        for k in range(p):
            assert b[k]==comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,m)%m
    return {'p':p,'L':L,'M':M,'sigma':sigma,'U_mod_p':U%p,
            'U16DU_mod_p':(U+16*DU)%p,'unit_quotient':unit//p,
            'tail_carry':carry,'triangle_quotient':triangle//p,
            'chi':chi,'S_mod_p2':S,'S16D_mod_p2':(S+16*D)%m}


def main():
    xs=[test(p) for p in primes(2000)]
    assert len(xs)==79
    print('PASS primes=%d exact_band_coefficients=%d exact_Gauss_port_carry=%d independent_triangle_primes=%d' %
          (len(xs),sum(x['M']-x['L'] for x in xs),len(xs),sum(x['p']<=157 for x in xs)))
    for p in (5,13,29,37,53,373):
        x=next(x for x in xs if x['p']==p)
        print('p={p} L={L} M={M} injection={sigma} unit_product/p={unit_quotient} '
              'tail={tail_carry} T/p={triangle_quotient} S={S_mod_p2} S+16D={S16D_mod_p2}'.format(**x))


if __name__=='__main__':
    main()
