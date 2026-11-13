#!/usr/bin/env python3
"""Exact finite min-zero fibers on signed X6 G=25; observer scope only."""
from collections import Counter, defaultdict
from itertools import product, permutations
from math import factorial, prod

TYPES = ((5,), (4,3), (4,2,2,1), (3,2,2,2,2), (3,3,2,1,1,1))
EXPECTED_PAIRS = {
    (1, (4,2,2,1), (3,3,2,1,1,1)): 360,
    (1, (3,3,2,1,1,1), (4,2,2,1)): 360,
    (1, (3,3,2,1,1,1), (3,2,2,2,2)): 180,
    (1, (3,2,2,2,2), (3,3,2,1,1,1)): 180,
    (3, (4,2,2,1), (3,3,2,1,1,1)): 180,
    (3, (3,3,2,1,1,1), (4,2,2,1)): 180,
}

def orbit_type(z):
    return tuple(sorted((abs(t) for t in z if t), reverse=True))

def brc(z):
    return factorial(sum(map(abs, z))) // prod(factorial(abs(t)) for t in z)

def rho(z):
    lo = min(z)
    return tuple(t-lo for t in z)

def generate_orbits():
    # Independent representation: signed permutations of five complete square partitions.
    out = set()
    for ty in TYPES:
        for ordering in set(permutations(ty + (0,)*(6-len(ty)))):
            nonzero = tuple(i for i,v in enumerate(ordering) if v)
            for signs in product((-1,1), repeat=len(nonzero)):
                z = list(ordering)
                for i,s in zip(nonzero, signs):
                    z[i] *= s
                out.add(tuple(z))
    return out

def enumerate_native():
    # Independent original-input enumeration: no use of orbit classification.
    return {z for z in product(range(-5,6),repeat=6) if sum(v*v for v in z)==25}

def pair_fibers(shell):
    fibers = defaultdict(list)
    for z in shell: fibers[rho(z)].append(z)
    sizes = Counter(map(len, fibers.values()))
    table = Counter()
    paired_brc = 0
    for f in fibers.values():
        if len(f)==2:
            lo,hi = sorted(f)
            k = hi[0]-lo[0]
            assert all(hi[i]-lo[i] == k for i in range(6))
            assert sum(lo) == -3*k
            table[(k,orbit_type(lo),orbit_type(hi))] += 1
            paired_brc += brc(lo)+brc(hi)
            assert brc(lo)!=brc(hi)
        else:
            assert len(f)==1
    return fibers,sizes,table,paired_brc

def independent_sum_coefficient(shell):
    # Quadratic shift identity: if both G(z), G(z+kD)=25 then sum(z)=-3k.
    counts = Counter((orbit_type(z),sum(z)) for z in shell)
    assert sum(counts[(ty,-3)] for ty in TYPES)==1080
    assert sum(counts[(ty,-9)] for ty in TYPES)==360
    assert {ty:(counts[ty,-3],counts[ty,-9]) for ty in TYPES} == {
        (5,):(0,0), (4,3):(0,0), (4,2,2,1):(360,180),
        (3,2,2,2,2):(180,0), (3,3,2,1,1,1):(540,180)}
    return counts

def main():
    by_orbit = generate_orbits()
    direct = enumerate_native()
    assert by_orbit == direct and len(direct)==7812
    fibers,sizes,table,paired_brc = pair_fibers(direct)
    assert len(fibers)==6372 and sizes==Counter({1:4932,2:1440})
    assert table==Counter(EXPECTED_PAIRS),table
    independent_sum_coefficient(direct)
    assert sum(n for (k,a,b),n in table.items() if k==1)==1080
    assert sum(n for (k,a,b),n in table.items() if k==3)==360
    assert paired_brc==952106400
    assert sum(brc(z) for z in direct)==2538954612
    assert sum(brc(f[0]) for f in fibers.values() if len(f)==1)==1586848212
    assert len({(rho(z),brc(z)) for z in direct})==7812
    # Nontrivial finite collision witnesses: different native endpoints, same relative rho and G.
    assert rho((-4,-2,-2,-1,0,0)) == rho((-1,1,1,2,3,3))
    assert rho((-4,-2,0,0,1,2)) == rho((-3,-1,1,1,2,3))
    print('PASS_EXACT_X6_G25_RELATIVE_FIBER_BRC')
    print('native_endpoints=7812; observer_fibers=6372; singletons=4932; pairs=1440')
    print('depth_separations={1:1080,3:360}; BRC_same_within_pair=0')
    print('paired_endpoint_BRC_words=952106400; singleton_BRC_words=1586848212')
    print('pair_type_table=',dict(sorted(table.items(),key=lambda v:(v[0][0],str(v[0][1:])))))

if __name__ == '__main__':
    main()
