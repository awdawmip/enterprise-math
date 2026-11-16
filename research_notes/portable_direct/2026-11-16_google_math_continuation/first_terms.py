"""Certified first singleton for Erdős #1063 using exhaustive CRT classes.
Usage: python first_terms.py 60 61
Uses the adjacent file period.py (standard library only).
"""
from math import comb
from period import primes_up_to, local_table

def find_in_bound(k, limit, tables):
    """Return smallest success in [2k,limit], or None. Heuristics only
    control which filters become the CRT wheel. Every remaining filter is
    checked on every eligible lift before the current best candidate."""
    best = limit + 1
    for t in range(k):
        bit = 1 << t
        filters = []
        for masks in tables:
            allowed = [r for r,m in enumerate(masks) if m in (0,bit)]
            filters.append((len(masks),allowed,masks))
        filters.sort(key=lambda x:len(x[1])/x[0])
        residues = [0]
        modulus = 1
        while filters:
            q, allowed, masks = filters[0]
            if modulus*len(allowed) >= best:
                break
            filters.pop(0)
            inv = pow(modulus,-1,q)
            new = []
            for a in residues:
                for b in allowed:
                    candidate = a + modulus*(((b-a)*inv)%q)
                    if candidate < best:
                        new.append(candidate)
            residues = new
            modulus *= q
        tail = [(q,masks) for q,_,masks in filters]
        for a in residues:
            n = a if a>=2*k else a+((2*k-a+modulus-1)//modulus)*modulus
            while n<best:
                if all(masks[n%q] in (0,bit) for q,masks in tail):
                    B = comb(n,k)
                    assert [i for i in range(k) if B%(n-i)]==[t]
                    best=n
                    break
                n+=modulus
    return best if best<=limit else None

def first(k):
    tables = [local_table(k,p) for p in primes_up_to(k)]
    limit = 10**7
    while True:
        result=find_in_bound(k,limit,tables)
        if result is not None:
            B=comb(result,k)
            return result,[i for i in range(k) if B%(result-i)]
        print("no solution through",limit,"for k",k,flush=True)
        limit *= 100

if __name__=='__main__':
    import sys
    for k in map(int,sys.argv[1:]):
        print(k,first(k),flush=True)
