"""Exact original-216 valuation-2 signed kernel verifier (author-side only)."""
import json
from math import comb
from pathlib import Path

def primes_to(N):
    sieve = bytearray([1]) * (N+1)
    sieve[0:2] = bytes([0,0])
    for q in range(2,int(N**0.5)+1):
        if sieve[q]:
            sieve[q*q:N+1:q] = bytes([0])*(((N-q*q)//q)+1)
    return [q for q in range(N+1) if sieve[q]]

def check(p):
    assert p>=7 and p%6==1
    r=(p-1)//6
    start=3*r+1
    modulus=p**3
    chi=1 if pow(6,(p-1)//2,p)==1 else -1
    C=(chi*pow(9,-1,p))%p
    # Original unshifted coefficient recurrence, independent of q_n.
    a=1
    actual=[]
    for k in range(4*r+1):
        if k>=start:
            assert a%(p*p)==0
            actual.append(a//(p*p))
        if k<4*r:
            num=(2*k+1)*(3*k+1)*(3*k+2)
            den=36*(k+1)**3
            a=a*num*pow(den,-1,modulus)%modulus
    # Independent fixed-parameter universal kernel recurrence.
    q=1
    predicted=[]
    for n in range(r):
        predicted.append(C*q%p)
        if n<r-1:
            num=(n+1)*(6*n+5)*(6*n+7)
            den=9*(2*n+3)**3
            q=q*num*pow(den,-1,p)%p
    assert actual==predicted, (p,actual[:4],predicted[:4])
    assert 6*(r-1)+7==p and (2*(r-1)+3)%p!=0
    high=sum((6*(start+n)+1)*actual[n] for n in range(r))%p
    predicted_sum=sum((6*n+4)*predicted[n] for n in range(r))%p
    assert high==predicted_sum
    return dict(p=p,r=r,chi=chi,high=high,kernel_sum=(high*9*chi)%p,seed=C,first=actual[0],last=actual[-1])

def main():
    items=[check(p) for p in primes_to(2000) if p%6==1]
    assert len(items)==148
    direct_cases=[7,13,19,31,37,43,61,73,103,373]
    for p in direct_cases:
        r=(p-1)//6
        by_k={}
        for k in range(3*r+1,4*r+1):
            top=comb(2*k,k)**2 * comb(3*k,k)
            a=top*pow(216,-k,p**3)%(p**3)
            assert a%(p*p)==0
            by_k[k]=a//(p*p)
        summary=next(x for x in items if x['p']==p)
        assert summary['high']==sum((6*k+1)*v for k,v in by_k.items())%p
    result={
      'schema':'D25_ORIGINAL216_VAL2_UNIVERSAL_KERNEL_FINITE_CHECK_V1',
      'asof_date':'2026-11-04',
      'range':'p prime = 6r+1, 7 <= p <= 2000',
      'count_primes':len(items),
      'normalized_coefficients_checked':sum(x['r'] for x in items),
      'direct_binomial_primes':direct_cases,
      'failures':0,
      'samples':[x for x in items if x['p'] in [7,13,19,31,37,73,373]],
      'science_status':'finite verification of an algebraically proved scoped lemma',
      'native_benchmark_status':'NOT_EXECUTED',
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    with Path(__file__).with_name('d25_original216_high_universal_kernel_results_20261104.json').open('w') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)

if __name__=='__main__':main()
