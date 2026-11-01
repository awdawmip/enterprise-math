#!/usr/bin/env python3
"""Exact source-typed valuation joint for original Euler--Clausen 216 series.
No native H0/B0 claims. Pure integer modular arithmetic (no floating point).
"""
from collections import defaultdict
from math import comb


def primes_upto(limit):
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = [False] * ((limit-p*p)//p + 1)
    return [p for p in range(7,limit+1) if sieve[p] and p%6==1]


def run(p, diagnostic=True):
    m = (p-1)//6
    mod = p**3
    j0 = 3*m+1
    inv2 = pow(2,-1,mod)
    e = [1] * p
    g = [1] * p
    h = [1] * p
    a = [1] * p
    for n in range(p-1):
        ii = pow(n+1,-1,mod)
        e[n+1] = e[n] * (2*n-1) * inv2 * ii % mod
        g[n+1] = g[n] * (6*n+1) * (3*n+1) * pow(18,-1,mod) * ii**2 % mod
        h[n+1] = h[n] * (6*n+5) * (3*n+2) * pow(18,-1,mod) * ii**2 % mod
        a[n+1] = a[n] * (2*n+1) * (3*n+1) * (3*n+2) * pow(36,-1,mod) * ii**3 % mod
    ge = [int(k>=m+1)+int(k>=2*m+1) for k in range(p)]
    he = [int(k>=4*m+1)+int(k>=5*m+1) for k in range(p)]
    def ep(j):
        return 'E_LOW' if j<j0 else ('E_EXC' if j==j0 else 'E_HIGH')
    def ev(port):
        return int(port=='E_HIGH')
    for j in range(p):
        assert (e[j]%p != 0) == (j <= j0)
    for k in range(p):
        assert (g[k] % p**(ge[k]+1) != 0)
        assert (h[k] % p**(he[k]+1) != 0)
        assert (g[k] % p**ge[k] == 0) and (h[k] % p**he[k] == 0)
    pair = defaultdict(lambda: [0]*p)
    for j in range(p):
        port = ep(j)
        for k in range(p-j):
            if ev(port)+ge[k] > 2: continue
            pair[(port,ge[k])][j+k] = (pair[(port,ge[k])][j+k]+e[j]*g[k]) % mod
    weight = [(6*n+1)*pow(inv2,n,mod)%mod for n in range(p)]
    sums = defaultdict(int)
    for (port,kgrade),arr in pair.items():
        for n,v in enumerate(arr):
            if not v:continue
            for l in range(p-n):
                grade = ev(port)+kgrade+he[l]
                if grade>2: continue
                key=(port,kgrade,he[l])
                sums[key] = (sums[key] + v*h[l]*weight[n+l])%mod
    original = sum((6*n+1)*a[n] for n in range(p)) % mod
    independent = sum((6*n+1)*comb(2*n,n)**2*comb(3*n,n) * pow(216,-n,mod) for n in range(p))%mod
    assert original==independent
    assert sum(sums.values())%mod==original
    for key, value in sums.items():
        grade = ev(key[0])+key[1]+key[2]
        assert value%p**grade == 0, (p,key,value,grade)
    grade2={str(key):v//(p*p)%p for key,v in sorted(sums.items()) if ev(key[0])+key[1]+key[2]==2}
    bygrade={s:sum(v for key,v in sums.items() if ev(key[0])+key[1]+key[2]==s)%mod for s in range(3)}
    if m >= 2: assert len(sums) == 11
    below2 = (bygrade[0]+bygrade[1]-p) % mod
    if p % 24 in (13,19):
        assert below2 % (p*p) == 0
        assert (below2//(p*p) + bygrade[2]//(p*p)) % p == 0
    result={'p':p,'m':m,'A':original,'grade0':bygrade[0], 'grade1_over_p':bygrade[1]//p,'grade2_over_p2':bygrade[2]//(p*p), 'below2_over_p2':below2//(p*p) if below2%(p*p)==0 else None, 'grade2_ports':grade2, 'source_count':len(sums)}
    if diagnostic:print(result)
    return result


if __name__=='__main__':
    allp = primes_upto(997)
    results=[run(p, p in (13,19,37,43,61,67,373)) for p in allp]
    assert all(r['A'] == r['p'] % r['p']**3 for r in results if r['p']%24 in (13,19))
    print('PASS_EXACT_EULER_CLAUSEN_THREE_FACTOR_ORIGINAL_WEIGHTED_MOD_P3:',len(results),'primes; target',sum(r['p']%24 in (13,19) for r in results))
