#!/usr/bin/env python3
"""D25 author-side finite p^2 clipped beta boundary certificate.

For primes p == 5 or 7 (mod 8) this implements a two-zone exact
congruence in binomial/harmonic data. Checks do not prove the separate
empirical character-value conjecture; no native Frobenius object is touched.
"""
from math import comb


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, int(n**0.5) + 1):
        if sieve[k]:
            sieve[k*k:n+1:k] = b'\x00' * ((n-k*k)//k + 1)
    return [k for k in range(5, n+1) if sieve[k]]


def exact_beta_tail(p):
    q=p*p
    beta=[1]
    for k in range(p-1):
        beta.append(beta[-1]*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,q)%q)
    suffix=[0]*(p+1); moment=[0]*(p+1)
    for j in range(p-1,-1,-1):
        suffix[j]=(suffix[j+1]+beta[j])%q
        moment[j]=(moment[j+1]+j*beta[j])%q
    tail=sum(beta[i]*((8*i+1)*suffix[p-i]+8*moment[p-i])
             for i in range(1,p))%q
    return tail,beta


def binomial_harmonic_ports(p):
    assert p>=5 and p%8 in (5,7)
    q=p*p
    n=(5*p-(1 if p%8==5 else 3))//8
    m=(7*p-(3 if p%8==5 else 1))//8
    assert p//2<n<m<p
    inv9=pow(9,-1,q)
    fac=[1]*(m+1)
    for t in range(1,m+1): fac[t]=fac[t-1]*t%p
    inv=[0]+[pow(i,-1,p) for i in range(1,m+1)]
    harmonic=[0]*(m+1)
    for k in range(1,m+1):
        harmonic[k]=(harmonic[k-1]+inv[k])%p
    inv8=pow(8,-1,p)
    lam=5*inv8%p
    mu=7*inv8%p
    C=[0]*(p+1); E=[0]*(p+1);D=[0]*(p+1)
    nine=1
    for k in range(m+1):
        if k<=n:
            C[k]=(comb(n,k)*comb(m,k)*nine)%q
            E[k]= (lam*(harmonic[n]-harmonic[n-k])
                   +mu*(harmonic[m]-harmonic[m-k]))%p
        else:
            # beta[k] / p, with a single first parameter zero at k=n+1
            # (-n+5p/8)_k/p = (5/8)(-1)^n n!(k-n-1)! (mod p)
            D[k]=(lam*(-1)**(n+k)*fac[n]*fac[k-n-1]*fac[m]
                  *pow(fac[m-k]*fac[k]*fac[k],-1,p)*nine)%p
        nine=nine*inv9%q
    SC=[0]*(p+1);JC=[0]*(p+1);SD=[0]*(p+1);JD=[0]*(p+1)
    for j in range(p-1,-1,-1):
        SC[j]=(SC[j+1]+C[j])%q;JC[j]=(JC[j+1]+j*C[j])%q
        SD[j]=(SD[j+1]+D[j])%p;JD[j]=(JD[j+1]+j*D[j])%p
    low_low=low_harm=low_mid=0
    for i in range(n+1):
        t=(8*i+1)*SC[p-i]+8*JC[p-i]
        low_low+=C[i]*t
        low_harm+=C[i]*E[i]*t
        low_mid+=C[i]*((8*i+1)*SD[p-i]+8*JD[p-i])
    low_low %=q
    low_harm=(-2*p*(low_harm%p))%q
    low_mid=(2*p*(low_mid%p))%q
    return dict(p=p, n=n, m=m, C=C, E=E, D=D, LL0=low_low, LL1=low_harm,
                LM=low_mid, total=(low_low+low_harm+low_mid)%q)


def main():
    rows=[]
    for p in primes_upto(1200):
        if p%8 not in (5,7): continue
        x=binomial_harmonic_ports(p)
        direct,beta=exact_beta_tail(p)
        assert x['total']==direct, (p, direct)
        q=p*p
        for k in range(p):
            expected=(x['C'][k]*(1-p*x['E'][k]) if k<=x['n']
                      else p*x['D'][k] if k<=x['m'] else 0)
            assert beta[k] == expected%q, (p,k,beta[k],expected%q)
        if p in (5,7,13,23,37,373):
            # Independent numerator-product / factorial denominator, not the recurrence.
            from math import prod, factorial
            for k in (0,1,p//2,p-1):
                numerator=prod((8*j+1)*(8*j+3) for j in range(k))
                denominator=(576**k)*(factorial(k)**2)
                assert beta[k]==numerator*pow(denominator,-1,q)%q
        # New character pattern: EXACT FINITE OBSERVATION ONLY, not theorem.
        chi=1 if p%3==1 else -1
        x['character_candidate']=(-p*chi)%(p*p)
        x['candidate_ok']=direct==x['character_candidate']
        rows.append({k:v for k,v in x.items() if k not in ('C','E','D')})
    print('PASS two-zone binomial/harmonic identity for',len(rows),'primes p<=1200, p%8=5/7')
    print('Empirical character-value conjecture:',sum(x['candidate_ok'] for x in rows),'/',len(rows))
    for row in rows:
        if row['p'] in (5,7,13,19,23,29,37,61,67,109,373):print(row)
    assert all(x['candidate_ok'] for x in rows)


if __name__=='__main__':main()
