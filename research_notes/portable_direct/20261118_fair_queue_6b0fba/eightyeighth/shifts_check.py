"""Compare reachable shifted powers and all cyclotomic observations. Standard library."""
import argparse
from collections import Counter, defaultdict
from functools import cache
from math import comb, gcd, prod
from pathlib import Path
import json


@cache
def factor(n):
    primes = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            m = 1
            while n % p == 0:
                n //= p
                m *= p
            primes.append((p,m))
        p += 1
    if n > 1:
        primes.append((n,n))
    return tuple(primes)


def divisors(n):
    return [d for d in range(1,n+1) if not n % d]


@cache
def cyclotomic(n):
    # Build over Z using successive exact monic divisions, before reducing modulo N.
    a = [-1]+[0]*(n-1)+[1]
    for d in divisors(n)[:-1]:
        f = cyclotomic(d)
        degree = len(f)-1
        quotient = [0]*(len(a)-degree)
        for j in range(len(quotient)-1,-1,-1):
            c = a[j+degree]
            quotient[j] = c
            for k,h in enumerate(f):
                a[j+k] -= c*h
        assert not any(a)
        a = quotient
    return tuple(a)


@cache
def factors_for_width(r):
    return [(len(f)-1, tuple((j,c) for j,c in enumerate(f[:-1]) if c))
            for f in map(cyclotomic,divisors(r))]


def observed(v,r,m):
    result = []
    for d,coeff in factors_for_width(r):
        a = list(v)
        for h in range(len(a)-1,d-1,-1):
            c = a[h] % m
            if c:
                for j,b in coeff:
                    a[h-d+j] -= c*b
        result.append(tuple(x % m for x in a[:d]))
    return tuple(result)


def explicit_coefficients(N,t,m):
    # The length N+1 expansion via Python's exact integer binomial.
    return [comb(N,j)*pow(t,N-j,m) % m for j in range(N+1)]


def fold(v,r,m):
    a = [0]*r
    for j,x in enumerate(v):
        a[j % r] += x
    return tuple(x % m for x in a)


def cyclic_product(a,b,m):
    # Kronecker convolution uses wide slots: no inter-slot carry.
    r = len(a)
    w = max(1,((r*(m-1)**2).bit_length()+7)//8)
    def pack(v):
        return int.from_bytes(b''.join(x.to_bytes(w,'little') for x in v),'little')
    raw = (pack(a)*pack(b)).to_bytes((2*r-1)*w,'little')
    v = memoryview(raw)
    c = [int.from_bytes(v[j:j+w],'little') for j in range(0,len(v),w)]
    return tuple((c[i] + (c[i+r] if i+1<r else 0)) % m for i in range(r))


def repeated_power(N,t,r,m):
    a = [0]*r
    a[0] = t % m
    a[1 % r] = (a[1 % r]+1) % m
    v = (1 % m,)+(0,)*(r-1)
    while N:
        if N & 1:
            v = cyclic_product(v,a,m)
        N >>= 1
        if N:
            a = cyclic_product(a,a,m)
    return v


def groups(states,r,m):
    fibers = defaultdict(set)
    for v in states:
        fibers[observed(v,r,m)].add(v)
    return fibers


def local_check(N,r,p,m,states):
    fibers = groups(states,r,m)
    unit_fine = set(states[1:])
    assert all(len(vs & unit_fine)<=1 for vs in fibers.values())
    bad = [frozenset(vs) for vs in fibers.values() if len(vs)>1]
    defective = p==3 and m%9==0 and N%2==0 and r==9
    if defective:
        assert len(set(states))==3 and len(fibers)==2
        assert bad==[frozenset((states[0],states[1]))]
        difference = tuple((v-u)%m for u,v in zip(states[0],states[1]))
        c = N//m
        assert gcd(c,3)==1 and c%2==0
        scale = (m//3)*(c//2)
        phi = cyclotomic(9)
        expected = tuple((scale*(phi[j] if j<len(phi) else 0))%m for j in range(9))
        assert difference==expected and any(difference)
    else:
        assert not bad
    return len(set(states))


def full_check(N,r,states):
    fibers = groups(states,r,N)
    finite_states = set(states)
    sizes = Counter(map(len,fibers.values()))
    unit_fine = {v for t,v in enumerate(states) if gcd(t,N)==1}
    assert all(len(vs & unit_fine)<=1 for vs in fibers.values())
    local_card = {}
    for p,m in factor(N):
        # Column t uses only t mod p. The caller supplies all these representatives.
        local = [tuple(x % m for x in v) for v in states[:p]]
        assert all(tuple(x % m for x in v)==local[t%p] for t,v in enumerate(states))
        local_card[p] = local_check(N,r,p,m,local)
    assert len(finite_states) == prod(local_card.values())
    if r==9 and N%18==0:
        s = prod(n for p,n in local_card.items() if p!=3)
        assert len(finite_states)==3*s and sizes=={1:s,2:s}
    else:
        assert sizes=={1:len(finite_states)}
    return dict(modulus=N,width=r,seed_period=prod(p for p,_ in factor(N)),
                local_fine_counts=local_card,fine=len(finite_states),observed=len(fibers),
                unit_only_distinct_fine_and_observed=len(unit_fine),
                observable_fibers_by_distinct_fine_states=dict(sorted(sizes.items())),
                raw_seed_multiplicities_per_fine_state=dict(sorted(Counter(Counter(states).values()).items())))


def small_grid():
    upper = 60
    widths = list(range(1,22))+[24,27,30,36]
    case_count = raw_shifts = cross_checks = direct_remainders = exceptional = 0
    for N in range(1,upper+1):
        coefficients = [explicit_coefficients(N,t,N) for t in range(N)]
        rad = prod(p for p,_ in factor(N))
        for r in widths:
            states = [fold(v,r,N) for v in coefficients]
            row = full_check(N,r,states)
            case_count += 1
            raw_shifts += len(states)
            exceptional += int(len(row['observable_fibers_by_distinct_fine_states'])==2)
            for t in sorted({0,1,N-1,-1,-rad-1,N+rad+1}):
                direct = fold(explicit_coefficients(N,t,N),r,N)
                assert direct==repeated_power(N,t,r,N)==states[t % N]
                assert direct==states[t % rad]
                cross_checks += 1
            # Bypass the fine ring, reduce a polynomial directly modulo each Phi_d.
            if N <= 20 and r <= 15:
                for t,v in enumerate(coefficients):
                    raw = v if len(v)>=r else v+[0]*(r-len(v))
                    assert observed(raw,r,N)==observed(states[t],r,N)
                    direct_remainders += 1
    return dict(modulus_inclusive=[1,upper],widths=widths,all_nonnegative_shifts='0 through N-1',
                modulus_width_cases=case_count,all_raw_shift_width_cases=raw_shifts,
                periodically_extended_signed_shift_checks=cross_checks,
                observations_reduced_directly_from_degree_N=direct_remainders,
                exceptional_modulus_width_cases=exceptional)


def large_local():
    tests = [
        (3,[1,2,3,6,9,12,16],[1,2,4,5,8,10,14,16],
         [1,2,3,4,6,8,9,12,15,18,24,27,36,45,54,63,72,81,90,99,108,117,135,162,189,225,243]),
        (2,[1,2,5,10,18],[1,3,7,9,15],[1,2,3,4,6,8,9,12,16,18,24,27,32,36,40,64,80,96]),
        (5,[1,2,4,7,10],[1,2,3,6,9],[1,4,5,9,10,15,20,25,30,45,50,75,100,125,225]),
        (7,[1,2,4,7],[1,2,3,6],[1,3,7,9,14,21,28,35,42,49,63,98,147,343]),
        (11,[1,3,5],[1,2,9],[1,9,11,22,33,55,99,121,242]),
        (13,[1,2,4],[1,2,9],[1,9,13,26,39,91,117,169]),
        (17,[2,4],[1,6],[1,9,17,34,51,153,289])]
    rows = []
    for p,exponents,cofactors,widths in tests:
        bad = shifts = 0
        for e in exponents:
            m = p**e
            for c in cofactors:
                assert gcd(p,c)==1
                N = m*c
                for r in widths:
                    states = [repeated_power(N,t,r,m) for t in range(p)]
                    local_check(N,r,p,m,states)
                    shifts += p
                    bad += int(p==3 and e>=2 and c%2==0 and r==9)
        rows.append(dict(prime=p,exact_valuations=exponents,coprime_cofactors=cofactors,
                         widths=widths,parameter_cases=shifts//p,all_local_representatives=shifts,
                         nontrivial_coarse_fibers=bad))
    return rows


def main():
    args = argparse.ArgumentParser()
    args.add_argument('--out',type=Path)
    path = args.parse_args().out
    direct = small_grid()
    high = large_local()
    composites = []
    for N,r in [(18,9),(36,9),(90,9),(648,9),(78120,9),
                (2**7*3**11*5**3,9),(2**7*3**11*5**3,27),(2**8*3**13*7**2,45)]:
        rad = prod(p for p,_ in factor(N))
        states = [repeated_power(N,t,r,N) for t in range(rad)]
        row = full_check(N,r,states)
        for t in (-2*rad-1,-rad,rad+1):
            assert repeated_power(N,t,r,N)==states[t%rad]
        if N==78120:
            assert row['local_fine_counts'][5]==2
        composites.append(row)
    witness = []
    for e,c in [(2,2),(2,4),(5,2),(9,10),(16,14)]:
        m = 3**e
        a,b = [repeated_power(m*c,t,9,m) for t in (0,1)]
        witness.append(dict(e=e,c=c,N=m*c,local_modulus=m,
                            difference_F1_minus_F0=[(y-x)%m for x,y in zip(a,b)]))
    result = dict(counting_convention="Fibers throughout count distinct fine states. Raw seeds in full CRT samples use t modulo rad(N).",
                  restricted_unit_test="In every local and global case the observation is injective on the distinct states reached by invertible shifts.",
                  direct_integer_binomial_grid=direct,high_prime_power_checks=high,
                  full_CRT_samples=composites,exceptional_local_differences=witness)
    data = json.dumps(result,sort_keys=True,indent=2)+'\n'
    if path:
        path.write_text(data)
    else:
        print(data,end='')


if __name__=='__main__':
    main()
