"""Integer checks of projected periodic graph fibers. Run with Python 3.9+."""
from collections import Counter, deque
from itertools import combinations, product
from math import gcd, isqrt
from functools import reduce
import json


def add(a, b):
    return tuple(u + v for u, v in zip(a, b))


def negate(a):
    return tuple(-u for u in a)


def graph(n, arcs):
    out = [[] for _ in range(n)]
    for a, b, v in arcs:
        out[a].append((b, v))
        out[b].append((a, negate(v)))
    return out


def values(adj, zero, cutoff, project=None, allowed=None):
    start = (0, zero)
    distances, queue = {start: 0}, deque([start])
    while queue:
        typ, z = queue.popleft()
        depth = distances[(typ, z)]
        if depth == cutoff:
            continue
        for nxt, label in adj[typ]:
            dest = (nxt, add(z, label))
            if allowed is not None and project(*dest) not in allowed:
                continue
            if dest not in distances:
                distances[dest] = depth + 1
                queue.append(dest)
    return distances


def components_mod(m, generators):
    start = (0, 0, 0)
    seen, queue = {start}, deque([start])
    while queue:
        point = queue.popleft()
        for v in generators:
            nxt = tuple((x + y) % m for x, y in zip(point, v))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def det2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def direct_smith_factors(cols):
    d1 = reduce(gcd, (abs(x) for v in cols for x in v))
    minors = [abs(det2((a[i], a[j]), (b[i], b[j]))) for a, b in combinations(cols, 2)
              for i, j in combinations(range(3), 2)]
    d12 = reduce(gcd, minors)
    a, b, c = cols
    det = abs(sum((-1)**i * a[i] *
                  det2(b[:i]+b[i+1:], c[:i]+c[i+1:]) for i in range(3)))
    return [d1, d12 // d1, det // d12]


def rational_prime(n):
    return n > 1 and all(n % p for p in range(2, isqrt(n)+1))


def gaussian_prime(z):
    a,b = z
    if a and b:
        return rational_prime(a*a + b*b)
    ell = abs(a or b)
    return ell % 4 == 3 and rational_prime(ell)


def divides(g, z):
    a,b = g
    x,y = z
    norm = a*a+b*b
    return (a*x+b*y)%norm == 0 and (a*y-b*x)%norm == 0


def composite_witnesses():
    primes = [z for z in product(range(-10,11),repeat=2) if gaussian_prime(z)]
    winds = [z for z in product(range(-3,4),repeat=2) if any(z)]
    counts = Counter()
    for g in primes:
        a,b = g
        ell = a*a+b*b if a and b else abs(a or b)
        for v in winds:
            m = 1 if divides(g,v) else ell
            adj = [tuple(x+n*y for x,y in zip(g,v)) for n in (-m,m)]
            z = max(adj, key=lambda w:sum(u*u for u in w))
            assert sum(u*u for u in z)>a*a+b*b and divides(g,z) and not gaussian_prime(z)
            counts["length_one" if m==1 else "residue_characteristic"] += 1
    return dict(primes=len(primes), nonzero_winds=len(winds), checks=len(primes)*len(winds),
                certificate_classes=dict(counts))


def main():
    vec = [(1,1,0), (1,0,1), (-1,1,1)]
    labels = vec + [negate(v) for v in vec]
    assert direct_smith_factors(vec) == [1,1,3]
    n = 40
    lifts = values(graph(1, [(0,0,v) for v in vec]), (0,0,0), n)
    histogram = Counter(t for (_, z), t in lifts.items() if z[0] == 0)
    even_section = []
    for k in range(n+1):
        m = k//2
        count = sum(histogram[j] for j in range(k+1))
        assert count == 1 + 3*m*(m+1)
        even_section.append(count)
    for (_, z), steps in lifts.items():
        x,y,w=z
        coeff2 = y+w-x
        assert coeff2%3==0
        c=coeff2//3
        assert steps == abs(y-c)+abs(w-c)+abs(c)
    modulo = []
    for m in range(1,25):
        hs = components_mod(m, labels)
        fibers = Counter(a for a,b,c in hs)
        assert len(fibers) == m and set(fibers.values()) == {m*m//gcd(m,3)}
        internal = sum((a+b-c)%m==0 for a,b,c in product(range(m),repeat=3))
        assert internal == m*m
        modulo.append([m, len(hs), internal, fibers[0]])
    pairs = [(2,1), (1,2)]
    norms = [a*a+b*b for a,b in pairs]
    assert all(q==5 and all(q%p for p in range(2,isqrt(q)+1)) for q in norms)
    step2 = sum((u-v)**2 for u,v in zip(*pairs))
    assert step2==2
    corridor = graph(2, [(0,1,(0,)),(0,1,(1,))])
    out = {}
    for key, window in (("single",{pairs[0]}),("pair",set(pairs))):
        ds=values(corridor,(0,),100,lambda v,z:pairs[v],window)
        out[key] = dict(by_port=[sum(a==t for a,z in ds) for t in range(2)],
                        number=len(ds))
    assert out["single"]["number"]==1 and out["pair"]["by_port"]==[101,100]
    vertical=values(graph(1,[(0,0,(1,))]),(0,),100)
    assert len(vertical)==201
    print(json.dumps(dict(generators=vec, smith=[1,1,3], graph_ball_radius=n,
                          lifted_vertices=len(lifts), center_fiber_at_radius=even_section,
                          modular_columns=["m","ambient_image_size","intrinsic_kernel_size",
                                           "ambient_kernel_size"], modular_counts=modulo,
                          gaussian_winding_check=composite_witnesses(), gaussian_primes=pairs, norms=norms, gaussian_step_squared=step2,
                          corridor_100_steps=out, vertical_100_steps=len(vertical)),
                     indent=2, sort_keys=True))


if __name__=="__main__":
    main()
