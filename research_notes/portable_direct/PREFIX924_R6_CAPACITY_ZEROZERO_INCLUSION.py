#!/usr/bin/env python3
"""PREFIX-924 independent exact divisor/inclusion-exclusion enumeration.

Strict 19-bit odd a,b; zero/zero collisions iff lcm(a,b)<2**32.
Counts only O(sum_a divisors(a) * squarefree_divisors(a)) rather than Q**2.
"""
N=1<<32
L,U=262145,524287
C=33

def factor(n):
    ans=[]; p=3
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0: n//=p; e+=1
            ans.append((p,e))
        p+=2
    if n>1: ans.append((n,1))
    return ans

def divisors(n):
    ans=[1]
    for p,e in factor(n):
        old=ans;ans=[];v=1
        for _ in range(e+1):
            ans.extend(d*v for d in old)
            v*=p
    return ans

def mobius_divisors(n):
    ans=[(1,1)]
    for p,_ in factor(n):
        ans+= [(d*p,-mu) for d,mu in ans[:]]
    return ans

def ceildiv(x,y):return (x+y-1)//y

def bucket_floor(a):
    return max(L,C*ceildiv(N,a),ceildiv(N,a//C))

def coprime_odd_count(q,lo,hi):
    if lo>hi:return 0
    # q and all its divisors are odd: only odd t are legal.
    return sum(mu*((hi//d+1)//2-(((lo-1)//d+1)//2))
               for d,mu in mobius_divisors(q))

def count_row(a,min_b):
    if min_b>U:return 0
    ans=0
    for q in divisors(a):
        g=a//q
        lo=ceildiv(min_b,g)
        hi=min(U//g,(N-1)//a)
        ans+=coprime_odd_count(q,lo,hi)
    return ans

if __name__=="__main__":
    import json
    zero=extra=safe=diag=0
    for a in range(L,U+1,2):
        threshold=bucket_floor(a)
        zero+=count_row(a,L)
        extra+=count_row(a,threshold)
        start=threshold+(threshold%2==0)
        if start<=U:safe+=(U-start)//2+1
        diag+=(a>=threshold)
    total=((U-L)//2+1)**2
    out={"schema":"PREFIX924_R6_CAPACITY_ZEROZERO_UNION_V1",
         "strict_19bit_odd_count":131072,"total_ordered_pairs":total,
         "zerozero_all":zero,"zerozero_outside_capacity":extra,
         "capacity_safe":safe,"two_sided_capacity_violations":total-safe,
         "union_capacity_zerozero":total-safe+extra,
         "remaining_after_union":safe-extra,
         "safe_diagonal_zerozero":diag}
    assert (zero,extra,safe,diag)==(209050784,95349218,9814322940,73900)
    print(json.dumps(out,sort_keys=True,ensure_ascii=True))
