#!/usr/bin/env python3
"""D25 author-side exact HB4 finite verifier; not a native H0/B0 experiment."""
from math import isqrt, factorial
import json

def primes(n):
    for p in range(5,n+1):
        if all(p%d for d in range(2,isqrt(p)+1)):
            yield p

def check(p, factorial_crosscheck=False):
    assert p>=7 and p%6==1
    m=(p-1)//6
    M=p**4
    a=[1]
    for k in range(p-1):
        a.append((a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M))%M)
    if factorial_crosscheck:
        fs=[1]*(3*p)
        for j in range(1,3*p): fs[j]=fs[j-1]*j%M
        for k in range(p):
            assert fs[2*k]*fs[3*k]*pow(216,-k,M)*pow(fs[k],-5,M)%M == a[k],('independent',p,k)
    harmonic=[0]*p
    for k in range(1,p): harmonic[k]=(harmonic[k-1]+pow(k,-1,p))%p
    q=(pow(216,p-1,p*p)-1)//p
    lower=sum((6*j+1)*a[j] for j in range(3*m+1))%M
    middle=0
    mid0=0
    for j in range(2*m+1,3*m+1):
        Aj=a[j]//p
        assert a[j]%p==0 and Aj%p!=0
        D=(2*harmonic[2*j-1]+3*harmonic[3*j-p-1]-5*harmonic[j-1]-q)%p
        c=(pow(36*j**3*Aj,-1,p*p)*(1+p*D))%(p*p)
        middle=(middle+(1+6*p-6*j)*c)%(p*p)
        mid0=(mid0+(1-6*j)*pow(36*j**3*Aj,-1,p))%p
        actual_high=a[p-j]//(p*p)
        assert a[p-j]%(p*p)==0 and actual_high%(p*p)==c,(p,j,'middle')
    high=sum((6*j-1)*pow(18*j**3*a[j],-1,p) for j in range(1,2*m+1))%p
    full=sum((6*k+1)*a[k] for k in range(p))%M
    reconstruct=(lower+p*p*middle+p**3*high)%M
    assert full==reconstruct,(p,'full',full,reconstruct)
    assert (full-lower)%p**2==0 and (full-lower)//(p*p)%p == mid0,(p,'p3-half-scope')
    return {'p':p, 'm':m, 'W_mod_p4':full, 'W_mod_p3':full%p**3,
            'lower_mod_p4':lower,'middle_two_digit_mod_p2':middle, 'high_first_digit_mod_p':high,
            'mid_p2_low_digit':middle%p,'middle_reconstructed_terms':m,'high_reconstructed_terms':2*m}

def main():
    qs=[p for p in primes(10000) if p%6==1]
    assert len(qs)==611
    results=[check(p,p in (7,13,19,31,73,157,373)) for p in qs]
    cert={
        'status':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_UNREVIEWED_NOT_ADMITTED',
        'science_pin':'c47e13e4aba0e006366f989d6334d443f6333ae3',
        'domain':'primes 7<=p<=10000, p mod6 == 1',
        'prime_count':len(qs), 'inert_count':sum(p%24 in (13,19) for p in qs),
        'mid_reconstructed_terms':sum(r['middle_reconstructed_terms'] for r in results),
        'high_reconstructed_terms':sum(r['high_reconstructed_terms'] for r in results),
        'independent_factorial_crosschecks':[7,13,19,31,73,157,373],
        'all_rows':results,
        'sample_rows':[r for r in results if r['p'] in (7,13,19,31,73,157,373)]
    }
    with open('d25_half_band_reflection_reconstruct_certificate_20261111.json','w') as f:
        json.dump(cert,f,indent=2,sort_keys=True)
    print('PASS',len(qs),'mid',cert['mid_reconstructed_terms'],'high',cert['high_reconstructed_terms'])
    for r in cert['sample_rows']: print(r)

if __name__=='__main__': main()
