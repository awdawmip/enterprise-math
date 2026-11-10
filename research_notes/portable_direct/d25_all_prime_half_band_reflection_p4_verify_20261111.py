#!/usr/bin/env python3
"""D25 exact all-prime p4 half-band reconstruction, author-side only."""
from math import isqrt
import json

def primes(n):
    for p in range(5,n+1):
        if all(p%d for d in range(2,isqrt(p)+1)): yield p

def check(p, factorial_check=False):
    assert p>=5 and p%2
    b=p//3; c=(p-1)//2; M=p**4
    a=[1]
    for k in range(p-1):
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M)
    if factorial_check:
        fs=[1]*(3*p)
        for j in range(1,3*p):fs[j]=fs[j-1]*j%M
        for k in range(p):
            assert fs[2*k]*fs[3*k]*pow(216,-k,M)*pow(fs[k],-5,M)%M==a[k],(p,k)
    H=[0]*p
    for k in range(1,p):H[k]=(H[k-1]+pow(k,-1,p))%p
    Q=(pow(216,p-1,p*p)-1)//p
    L=sum((6*k+1)*a[k] for k in range(c+1))%M
    middle=0
    for j in range(b+1,c+1):
        A=a[j]//p
        assert a[j]%p==0 and A%p!=0
        D=(2*H[2*j-1]+3*H[3*j-p-1]-5*H[j-1]-Q)%p
        high=pow(36*j**3*A,-1,p*p)*(1+p*D)%(p*p)
        assert a[p-j]%(p*p)==0 and a[p-j]//(p*p)%(p*p)==high,(p,j,'middle')
        middle=(middle+(1+6*p-6*j)*high)%(p*p)
    tail=0
    for j in range(1,b+1):
        h=-pow(18*j**3*a[j],-1,p)%p
        assert a[p-j]%(p**3)==0 and a[p-j]//(p**3)%p==h,(p,j,'high')
        tail=(tail+(1-6*j)*h)%p
    W=sum((6*k+1)*a[k] for k in range(p))%M
    assert W==(L+p*p*middle+p**3*tail)%M,(p,W,L,middle,tail)
    return {'p':p,'b':b,'c':c,'L_mod_p4':L,'middle_two_digit_mod_p2':middle,
            'tail_first_digit_mod_p':tail,'W_mod_p4':W,'mid_terms':c-b,'tail_terms':b}

def main():
    rows=[check(p,p in (5,7,11,13,19,31,73,157,373)) for p in primes(10000)]
    assert len(rows)==1227
    mid=sum(r['mid_terms'] for r in rows)
    tail=sum(r['tail_terms'] for r in rows)
    assert mid==956066 and tail==1911516
    cert={'status':'AUTHOR_EXACT_VERIFIED_UNREVIEWED_NOT_ADMITTED',
          'science_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
          'domain':'all primes 5<=p<=10000','prime_count':len(rows),
          'mid_terms':mid,'tail_terms':tail,
          'crosscheck_primes':[5,7,11,13,19,31,73,157,373],'rows':rows}
    with open('d25_all_prime_half_band_reflection_p4_certificate_20261111.json','w') as f:
        json.dump(cert,f,indent=2,sort_keys=True)
    print('PASS',len(rows),'middle',mid,'high',tail)
    for r in rows:
        if r['p'] in (5,7,11,13,19,157,373): print(r)

if __name__=='__main__': main()
