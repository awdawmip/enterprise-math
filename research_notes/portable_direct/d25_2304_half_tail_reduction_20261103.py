"""Independent exact finite-check of published S2304 half-cutoff and signed band coordinates."""
from math import comb, factorial, isqrt
import json

def primes(n):
    return [p for p in range(13,n+1) if p%24 in (13,19) and all(p%d for d in range(2,isqrt(p)+1))]

def check(p):
    modulus=p**3
    h=(p-1)//2
    l=(2*p)//3
    H=(3*p)//4
    a=[];b=[]
    for k in range(H+1):
        if k<=l:
            a.append((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,modulus)%modulus)
        b.append((8*k+1)*comb(4*k,2*k)*comb(2*k,k)**2*pow(2304,-k,modulus)%modulus)
    sum_b_half=sum(b[:h+1])%modulus
    sum_b_full=sum(b)%modulus
    assert sum_b_half==sum_b_full==p
    low_b=sum(b[h+1:l+1])%modulus
    high_b=sum(b[l+1:H+1])%modulus
    assert (low_b+high_b)%modulus==0
    assert low_b%p**2==0 and high_b%p**2==0
    c=[]
    u=[]
    for k in range(h+1,H+1):
        normalized=2*factorial(4*k-2*p)*pow(factorial(k),-4,p)*pow(2304,-k,p)%p
        assert ((8*k+1)*normalized-b[k]//p**2)%p==0
        c.append(normalized);u.append((8*k+1)*normalized%p)
    for k in range(h+1,H):
        j=k-(h+1)
        num=1
        for t in range(1,5):num*=4*k+t
        den=2304*(k+1)**4
        assert (c[j+1]*den-c[j]*num)%p==0
    if p%24==13:
        r=(5*p-1)//8
        assert h+1<=r<=l and (8*r+1)%p==0
        assert c[r-h-1]!=0 and u[r-h-1]==0
    a_mid=[]
    for k in range(h+1,l+1):
        v=(6*k+1)*factorial(2*k-p)*factorial(3*k-p)*pow(factorial(k),-5,p)*pow(216,-k,p)%p
        assert v==(a[k]//p**2)%p
        a_mid.append(v)
    assert sum(a)%modulus==p
    a_half=sum(a[:h+1])%modulus
    assert (a_half-p)%p**2==0
    assert (((a_half-p)//p**2+sum(a_mid))%p)==0
    return {"p":p,"S_mid_digit":low_b//p**2,"S_hi_digit":high_b//p**2,"S_total_2digits":sum(u)%p,"W_half_digit":((a_half-p)//p**2),"W_mid_digit":sum(a_mid)%p,"S_weight_root":r if p%24==13 else None}

if __name__=='__main__':
    out=[check(p) for p in primes(1200)]
    print('checked',len(out),'S upper signed cancellation',sum(o['S_total_2digits']!=0 for o in out),'W bridge errors 0')
    for r in out:
        if r['p'] in (13,19,181,373,1171):print(r)
    with open('/mnt/data/d25_2304_half_tail_reduction_20261103.check_summary.json','w') as f:
        json.dump({'schema':'D25_S2304_HALF_TAIL_CANCEL_W216_MID_V1','classification':'FINITE_EXACT_CHECK_UNREVIEWED_NOT_ADMITTED','primes_tested':len(out),'prime_bound':1200,'results':out},f,indent=2)
