"""Exact distribution of the survivor count for odd distinct semiprimes."""
from bisect import bisect_right
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt, prod
import json
N_MAX = 10_000_000
MODULI = (64,3,5,7)
M = prod(MODULI)
def local_counts(q):
    residues = {x*x % q for x in range(q)}
    values = [x*x % q for x in range(q)]
    return [sum((r - n) % q in residues for r in values) for n in range(q)]
def histogram(counter):
    total = sum(counter.values())
    ordered = sorted(counter)
    def quantile(rank):
        count = 0
        for item in ordered:
            count += counter[item]
            if count >= rank: return item
    return dict(total=total, bins={j:counter[j] for j in ordered},
                median_pair=[quantile((total+1)//2),quantile((total+2)//2)],
                expected_surviving_fraction=str(Fraction(sum(k*v for k,v in counter.items()), total*M)))
def main():
    prime = bytearray([1])*(N_MAX//3+1)
    prime[0:2]=b'\x00\x00'
    for p in range(2,isqrt(len(prime)-1)+1):
        if prime[p]:
            prime[p*p::p]=bytes((len(prime)-1-p*p)//p+1)
    primes=[x for x in range(3,len(prime),2) if prime[x]]
    tables = [local_counts(q) for q in MODULI]
    byN=[prod(table[n%q] for q,table in zip(MODULI,tables)) for n in range(M)]
    data=Counter()
    units=Counter()
    others=Counter()
    for i,p in enumerate(primes):
        if p*p>N_MAX: break
        for q in primes[i+1:bisect_right(primes,N_MAX//p)]:
            k=byN[p*q%M]
            data[k]+=1
            (others if p in (3,5,7) or q in (3,5,7) else units)[k]+=1
    result={name:histogram(c) for name,c in (('full',data),('coprime',units),('small_factor',others),('limiting_unit_residues',Counter(v for n,v in enumerate(byN) if gcd(n,M)==1)))}
    # For one fixed small prime r and the other prime tending to infinity,
    # the second factor becomes uniform over the units modulo M.
    unit_residues = [n for n in range(M) if gcd(n,M)==1]
    fixed = {}
    for r in (3,5,7):
        counter = Counter(byN[r*n % M] for n in unit_residues)
        cdf_128 = Fraction(sum(count for n,count in counter.items() if n<=128),len(unit_residues))
        fixed[r] = dict(law=histogram(counter), cdf_at_128=str(cdf_128))
    result['fixed_small_factor_limiting_laws'] = fixed
    assert [fixed[r]['cdf_at_128'] for r in (3,5,7)] == ['0','1/8','1/8']
    assert all(fixed[r]['law']['expected_surviving_fraction']=='3/64' for r in fixed)
    assert result['limiting_unit_residues']['expected_surviving_fraction']=='3/128'
    assert result['full']['total']==1555366
    return result
if __name__=='__main__': print(json.dumps(main(),indent=2))
