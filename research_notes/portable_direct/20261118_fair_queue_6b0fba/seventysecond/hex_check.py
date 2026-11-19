"""Rebuild hex_checked.json with the standard library. No network or input files."""
from collections import Counter, defaultdict
from itertools import product
from math import comb, gcd, isqrt
from pathlib import Path
import json


def hex_points(s):
    # Intersection of the three pairs of original half planes, at fixed q.
    for q in range(-s, s + 1):
        lo = max(-s - 2*q, -((s + q)//2), q - s)
        hi = min(s - 2*q, (s - q)//2, q + s)
        for r in range(lo, hi + 1):
            yield q, r


def height(q, r):
    return max(abs(2*q+r), abs(q+2*r), abs(q-r))


def period_ring(m):
    x, y = m, -1
    ring = []
    for i in range(6):
        ring.append((x, y))
        x, y = -y, x+y
    assert (x,y) == ring[0] and len(set(ring)) == 6
    return ring


def pair_classes(m):
    # Recover original pairs on the outer shell and identify their true inner
    # representatives with the quotient labels. Do not use the progression law.
    K = m*m-m+1
    pairs = defaultdict(list)
    inner = set()
    for q,r in hex_points(m):
        h = height(q,r)
        addr = (q+m*r)%K
        if h == m:
            pairs[q%m,r%m].append(addr)
        elif h == m-1:
            inner.add(addr)
    assert all(len(l) == 2 for l in pairs.values())
    edges = {tuple(sorted(l)) for l in pairs.values()}
    assert len(edges) == m-1 and len(inner) == 2*(m-1)
    assert {x for e in edges for x in e} == inner
    return edges


def divisors(n):
    return sorted({j for d in range(1,isqrt(n)+1) if n%d == 0 for j in (d,n//d)})


def parameters_from_edge(edge, target_edges, modulus):
    # Images of both possible orders of the actual first edge.
    a,b = edge
    inv = pow(b-a,-1,modulus)
    for c0,d0 in target_edges:
        for c,d in ((c0,d0),(d0,c0)):
            u = ((d-c)*inv)%modulus
            yield u,(c-u*a)%modulus


def move(e, u, v, d):
    return tuple(sorted((u*x+v)%d for x in e))


def projection_certificate(m, edges):
    K = m*m-m+1
    a = (m-1)//3
    rows = []
    for d in divisors(K):
        graph = Counter(tuple(sorted(x%d for x in e)) for e in edges)
        if d == 1:
            assert graph == {(0,0):m-1}
            continue
        assert all(gcd(y-x,d)==1 for x,y in graph)
        expected_rot = {pow(m,i,d) for i in range(6)}
        assert len(expected_rot) == 6
        if len(graph)*len(graph) < 400000:
            candidates = set(parameters_from_edge(min(graph),graph,d))
            simple, counted = set(), set()
            for u,v in candidates:
                if all(move(e,u,v,d) in graph for e in graph):
                    simple.add((u,v))
                    if all(graph[move(e,u,v,d)]==n for e,n in graph.items()):
                        counted.add((u,v))
            assert counted == {(u,0) for u in expected_rot}
            expected = {(u,v) for u in expected_rot for v in (range(d) if a>=d else (0,))}
            assert simple == expected
            simple_count, counted_count = len(simple),len(counted)
        else:
            simple_count = counted_count = None
        assert len(graph) == 3*min(a,d)
        rows.append(dict(d=d,distinct_edges=len(graph),total_weights=sum(graph.values()),
                         simple_group_enumerated=simple_count,counted_group_enumerated=counted_count))
    return rows


def matching_certificate(m):
    K = m*m-m+1
    a = (m-1)//3
    s = 1-2*m
    edges = pair_classes(m)
    rotations = {pow(m,i,K) for i in range(6)}
    assert {w%K for x,y in edges for w in (x-y,y-x)} == rotations
    assert {(tuple(sorted((2*x%K,2*y%K)))) for x,y in edges}.isdisjoint(edges)
    checks = {}
    for t in range(1,a):
        for direction in range(3):
            for sign in (-1,1):
                shift = sign*s*pow(m,direction,K)*t%K
                assert shift not in checks and shift != 0
                checks[shift] = a-t
    checks[0] = len(edges)
    assert len(checks) == 1+6*(a-1)
    # Any nonzero overlap has some ordered original and target edge.
    # Count each such pair by its inferred affine parameters (not only
    # parameters occurring in the first edge). This detects partial overlap.
    if m<=256:
        actual = Counter((u,v) for e in edges for u,v in parameters_from_edge(e,edges,K))
        assert actual == {(u,v):n for u in rotations for v,n in checks.items()}
        hist = Counter(actual.values())
        checked = len(actual)
    else:
        hist = Counter()
        checked = None
    if m in (4,16):
        # All affine maps, also nonunits, including those of zero overlap.
        exhaustive = Counter()
        for u,v in product(range(K),repeat=2):
            cnt = sum(move(e,u,v,K) in edges for e in edges)
            assert cnt == (checks.get(v,0) if u in rotations else 0)
            exhaustive[cnt] += 1
    else:
        exhaustive = {}
    x,y = min(edges)
    return dict(m=m,K=K,a=a,original_edges=len(edges),
                minimum_bad_multiplier=dict(multiplier=2,edge=[x,y],image=list(move((x,y),2,0,K))),
                affine_maps_with_positive_overlap_enumerated=checked,
                positive_overlap_histogram=dict(sorted(hist.items())),
                all_affine_maps_histogram=dict(sorted(exhaustive.items())),
                divisors_checked=projection_certificate(m,edges))


def primes_through(n):
    sieve = bytearray([1])*(n+1)
    sieve[:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = bytes((n-p*p)//p+1)
    return [p for p in range(2,n+1) if sieve[p]]


def pair_slots(mask):
    return (mask&7 | (mask>>3)).bit_count()


def modular_certificate(m):
    K = m*m-m+1
    ring = period_ring(m)
    test_primes = sorted(set(primes_through(149)) | {p for p in divisors(K) if p>1
                                                     and all(p%q for q in range(2,isqrt(p)+1))})
    for p in test_primes:
        points = [(x%p,y%p) for x,y in ring]
        assert (0,0) not in points and len(set(points)) == (3 if p==2 else 6)
        if p==2:
            assert points[:3] == points[3:]
        if K%p==0:
            assert p%12==1 and all(
                ((-y)%p,(x+y)%p) == (pow(m,-1,p)*x%p,pow(m,-1,p)*y%p) for x,y in points)
        if p<=149:
            # Enumerate local admissible residues directly in the plane.
            occupied = {(x,y):sum(1<<j for j,xy in enumerate(points) if xy==(x,y))
                        for x in range(p) for y in range(p)}
            freq = Counter(mask for xy,mask in occupied.items() if xy!=(0,0))
            for mask in range(64):
                got = sum(n for forbidden,n in freq.items() if not (forbidden&mask))
                expect = 3-pair_slots(mask) if p==2 else p*p-1-mask.bit_count()
                assert got==expect
                # Allow a nonprimitive centre by including the zero residue.
                assert got+1 == (4-pair_slots(mask) if p==2 else p*p-mask.bit_count())
    return test_primes


def visible_certificate(m):
    ring = period_ring(m)
    patterns = Counter()
    all_centres = Counter()
    threshold_neighbours = Counter()
    count = 0
    for q,r in hex_points(m-1):
        count += 1
        mask = sum(1<<i for i,(x,y) in enumerate(ring) if gcd(q-x,r-y)==1)
        all_centres[mask] += 1
        if m<=64:
            heights = [height(q-x,r-y) for x,y in ring]
            assert min(heights)>=m and heights.count(m)==int(height(q,r)==m-1)
            threshold_neighbours[heights.count(m)] += 1
        if gcd(q,r) == 1:
            assert pair_slots(mask)<=2 and mask.bit_count()<=4
            patterns[mask] += 1
    assert count == m*m-m+1 and all_centres[63]>0
    for mask,n in patterns.items():
        assert patterns[((mask<<1)&63)|(mask>>5)]==n
    hist = [sum(v for mask,v in patterns.items() if mask.bit_count()==j) for j in range(5)]
    if m>=256:
        assert set(patterns) == {mask for mask in range(64) if pair_slots(mask)<=2}
    return dict(m=m,domain=count,primitive_centres=sum(hist),neighbour_count_histogram=hist,
                unrestricted_all_six=all_centres[63],
                unrestricted_histogram=[sum(n for k,n in all_centres.items() if k.bit_count()==j) for j in range(7)],
                original_threshold_neighbour_counts=dict(threshold_neighbours),
                realised_masks=len(patterns),exact_patterns_by_decimal_mask=dict(sorted(patterns.items())),
                local_primes_checked=modular_certificate(m))


def limit_certificate(bound=1_000_000):
    # Directed fixed-point product enclosure. The omitted prime tail is bounded
    # by sum_{n>bound} k/(n^2-1) <= k/bound. No floating-point arithmetic.
    scale = 10**18
    primes = primes_through(bound)[1:]
    pk = []
    for k in range(5):
        lo=hi=scale
        for p in primes:
            b = p*p-1
            lo = lo*(b-k)//b
            hi = (hi*(b-k)+b-1)//b
        lo = lo*(bound-k)//bound
        pk.append((lo,hi))
    masses = []
    for j in range(5):
        lo=hi=0
        for k in range(j,5):
            coef = (-1)**(k-j)*comb(k,j)*comb(4,k)
            v,w = pk[k] if coef>=0 else pk[k][::-1]
            lo+=coef*v
            hi+=coef*w
        assert 0 < lo <= hi < scale
        masses.append([lo,hi])
    return dict(prime_cutoff=bound,unit_denominator=scale,
                normalized_local_products_intervals=pk,conditional_masses_intervals=masses)


def run():
    scales = [4,16,64,256,1024]
    return dict(matching=[matching_certificate(m) for m in scales],
                visibility=[visible_certificate(m) for m in scales],limits=limit_certificate())


if __name__=='__main__':
    out = Path(__file__).with_name('hex_checked.json')
    out.write_text(json.dumps(run(),indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(out.name)
