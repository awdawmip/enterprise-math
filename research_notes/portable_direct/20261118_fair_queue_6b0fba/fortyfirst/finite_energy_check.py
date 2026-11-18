#!/usr/bin/env python3
"""Exact finite-state tests for separable energy on cyclic modular rotations."""
from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, lcm
import json


def prime_powers(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p:
            p += 1
            continue
        q = 1
        while n % p == 0:
            n //= p
            q *= p
        out.append((p, q))
    if n > 1:
        out.append((n, n))
    return out


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def rotations(n):
    return [(a,b) for a in range(n) for b in range(n) if (a*a+b*b-1) % n == 0]


def common_blocks(n, family):
    forced = n
    for a,b in family:
        forced = gcd(forced, a*b)
    blocks = defaultdict(lambda: 1)
    for p,q in prime_powers(forced):
        signature = tuple(0 if b % p == 0 else 1 for a,b in family)
        blocks[signature] *= q
    return forced, blocks


def orbit_basis(n, family):
    forced, blocks = common_blocks(n,family)
    # Encode the independent nonconstant block indicator columns in base 3.
    # Since only pairs are added, no carry can conceal an equation.
    codes = [0]*n
    column = 1
    for sig,q in sorted(blocks.items()):
        actions = set()
        for swap,(a,b) in zip(sig,family):
            if swap:
                actions.update((b % q, -b % q))
            else:
                actions.add(a % q)
        unused = set(range(1,q))
        while unused:
            orbit = {min(unused)}
            for multiplier in actions:
                orbit |= {x*multiplier % q for x in orbit}
            assert orbit <= unused
            unused -= orbit
            for x in range(n):
                if x % q in orbit:
                    codes[x] += 3**(column-1)
            column += 1
    actual_period = next(k for k in divisors(n) if all(codes[x] == codes[(x+k)%n] for x in range(n)))
    assert actual_period == forced
    return column, codes, forced


def rank_mod(matrix,p=1009):
    rows = [[x % p for x in row] for row in matrix]
    row = 0
    for col in range(len(rows[0])):
        i = next((i for i in range(row,len(rows)) if rows[i][col]),None)
        if i is None:
            continue
        rows[row],rows[i] = rows[i],rows[row]
        inv = pow(rows[row][col],-1,p)
        pivot = [(v*inv) % p for v in rows[row]]
        for i in range(row+1,len(rows)):
            if rows[i][col]:
                factor = rows[i][col]
                rows[i] = [(v-factor*w)%p for v,w in zip(rows[i],pivot)]
        row += 1
        if row == len(rows):
            break
    return row


def gram(n,rotation,codes):
    a,b = rotation
    ans = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            u,v = (a*x-b*y)%n, (b*x+a*y)%n
            assert codes[x]+codes[y] == codes[u]+codes[v]
            sparse = Counter((u,v))
            sparse.subtract((x,y))
            for i,vi in sparse.items():
                for j,vj in sparse.items():
                    ans[i][j] += vi*vj
    return ans


def check_spectrum(n,m):
    # With normalized counting measures the operator on f is m/n.
    square = [[sum(x*y for x,y in zip(r,s)) for s in m] for r in m]
    for i,row in enumerate(square):
        for j,col in enumerate(m):
            cubic = sum(x*y for x,y in zip(row,col))
            assert cubic-12*n*square[i][j]+32*n*n*m[i][j] == 0
    tr = sum(m[i][i] for i in range(n))
    tr2 = sum(square[i][i] for i in range(n))
    n8 = Fraction(tr2-4*n*tr,32*n*n)
    n4 = Fraction(tr-8*n*n8,4*n)
    assert n8.denominator == n4.denominator == 1
    return [n-int(n4+n8),int(n4),int(n8)]


def predicted_spectrum(n,ab):
    a,b = ab
    counts = Counter({0:1})
    for d in divisors(n)[1:]:
        units = sum(gcd(k,d) == 1 for k in range(d))
        if a % d and b % d:
            counts[4] += units
            continue
        u,v = (a % d,a % d) if b % d == 0 else (b % d,-b % d)
        group = [1,u,v,u*v % d]
        for eu in (-1,1):
            for ev in (-1,1):
                signs = [1,eu,ev,eu*ev]
                if any(group[i] == group[j] and signs[i] != signs[j]
                       for i in range(4) for j in range(i)):
                    continue
                counts[4-2*eu-2*ev] += units // len(set(group))
    return [counts[e] for e in (0,4,8)]


def check_family(n,family,spectral=False):
    dim,codes,forced = orbit_basis(n,family)
    total = [[0]*n for _ in range(n)]
    for ab in family:
        m = gram(n,ab,codes)
        for r,s in zip(total,m):
            for j,v in enumerate(s):
                r[j] += v
    # Explicit real null vectors plus a modular rank lower bound give exact real rank.
    assert rank_mod(total) == n-dim
    spectrum = check_spectrum(n,total) if spectral else None
    if spectral:
        assert spectrum[0] == dim and spectrum == predicted_spectrum(n,family[0])
    return dim,forced,spectrum


def multiply(z,w,n):
    a,b = z
    c,d = w
    return ((a*c-b*d)%n,(a*d+b*c)%n)


def power(z,k,n):
    out = (1,0)
    while k:
        if k % 2:
            out = multiply(out,z,n)
        z = multiply(z,z,n)
        k //= 2
    return out


def rotation_census(n):
    pp = prime_powers(n)
    all_rot = rotations(n)
    dual = [z for z in all_rot if gcd(z[0]*z[1],n) == 1]
    admissible = [z for z in all_rot if (z[0]*z[1]) % n == 0]
    roots = 1
    group_size = 1
    possible_orders = 1
    for p,q in pp:
        if p == 2:
            roots *= 1 if q == 2 else 2 if q == 4 else 4
            group_size *= 2 if q == 2 else 2*q
        else:
            roots *= 2
            chi = 1 if p % 4 == 1 else -1
            local = q//p*(p-chi)
            group_size *= local
            possible_orders = lcm(possible_orders,local)
    assert len(all_rot) == group_size
    assert len(admissible) == 2**len(pp)*roots
    assert sum(a != 0 and b != 0 for a,b in admissible) == (2**len(pp)-2)*roots
    actual = Counter()
    counts = {}
    if n % 2:
        ds = divisors(possible_orders)
        for z in dual:
            d = next(d for d in ds if power(z,d,n) == (1,0))
            actual[d] += 1
        for d in ds:
            at_most = 1
            for p,q in pp:
                h = p-(1 if p % 4 == 1 else -1)
                at_most *= gcd(d,q//p*h)-gcd(d,4*(q//p))
            counts[d] = at_most-sum(c for e,c in counts.items() if d%e == 0)
        assert {d:c for d,c in counts.items() if c} == dict(actual)
    else:
        assert not dual
    return dict(N=n,rotations=len(all_rot),positive_energy_admitting=len(admissible),
                both_units=len(dual),orders=dict(sorted(actual.items())))


def main():
    sizes = [*range(2,21),24,25]
    state_rows = []
    for n in sizes:
        census = Counter()
        nr = 0
        for ab in rotations(n):
            dim,forced,spectrum = check_family(n,[ab],True)
            assert (forced == n) == (ab[0]*ab[1] % n == 0)
            census[tuple(spectrum)] += 1
            nr += 1
        state_rows.append(dict(N=n,rotations=nr,states=n*n*nr,
                               spectrum_multiplicities=[[*e,c] for e,c in sorted(census.items())]))
    shared = [(91,15),(85,21)]
    assert all((a*a+b*b)%105 == 1 for a,b in shared)
    cases = []
    for family in [[shared[0]],[shared[1]],shared]:
        dim,period,_ = check_family(105,family)
        cases.append(dict(rotations=family,dimension=dim,common_period=period))
    assert [r['dimension'] for r in cases] == [18,23,8]
    assert check_family(7,[(2,2)],True) == (1,1,[1,6,0])
    assert check_family(25,[(1,5)],True) == (5,5,[5,20,0])
    group_tests = [2,3,4,5,7,8,9,11,13,15,16,17,21,25,27,32,35,49,64,65,77,81,121,125,169,343]
    out = dict(all_state_tests=state_rows,total_rotations=sum(x['rotations'] for x in state_rows),
               total_input_pairs=sum(x['states'] for x in state_rows),
               multiplicity_columns=['lambda_0','lambda_4','lambda_8','number_of_rotations'],
               shared_rotations_mod_105=cases,
               rotation_order_tests=[rotation_census(n) for n in group_tests])
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
