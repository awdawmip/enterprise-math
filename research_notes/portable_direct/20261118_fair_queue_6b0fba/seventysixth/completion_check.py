"""Finite native incidence certificates for R043C7. Python standard library."""
import argparse
import json
from collections import Counter, defaultdict, deque
from functools import cache
from itertools import combinations, permutations, product
from pathlib import Path

ORIGIN = (0, 0, 0)
DIRECTIONS = tuple(v for v in product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 2)
PLANE = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))
DOWN = ((0, 0), (-1, 0), (0, -1))


@cache
def fcc(p):
    x, y, z = p
    return frozenset((x+i, y+j, z+k) for i, j, k in DIRECTIONS)


@cache
def hcp(p):
    x, y, k = p
    offsets = [(-i, -j) for i, j in DOWN] if k % 2 else DOWN
    same = {(x+i, y+j, k) for i, j in PLANE}
    return frozenset(same | {(x+i, y+j, k+d) for i, j in offsets for d in (-1, 1)})


def neighborhood(world, points):
    return set().union(*(world(u) for u in points))


@cache
def ball(world, center, radius):
    result = {center}
    for _ in range(radius):
        result |= neighborhood(world, result)
    return frozenset(result)


def edge_count(world, points):
    return sum(v in world(u) for u, v in combinations(points, 2))


def cut(world, points):
    return 12*len(points) - 2*edge_count(world, points)


@cache
def stabilizers(world):
    if world is fcc:
        return [lambda t, o=o, s=s: tuple(t[o[i]]*s[i] for i in range(3))
                for o in permutations(range(3)) for s in product((1,-1), repeat=3)]
    maps = []
    for (u, v), (i, j), (k, l) in permutations(DOWN):
        for sign in (-1, 1):
            def transform(t, u=u, v=v, a=u-i, b=v-j, c=u-k, d=v-l, sign=sign):
                x, y, z = t
                return a*x+c*y+u*(z%2), b*x+d*y+v*(z%2), sign*z
            maps.append(transform)
    return maps


def canonical(world, points):
    def at(center):
        i, j, k = center
        sign = -1 if world is hcp and k % 2 else 1
        return [(sign*(x-i), sign*(y-j), z-k) for x, y, z in points]
    return min(tuple(sorted(f(x) for x in local))
               for c in points for local in [at(c)] for f in stabilizers(world))


@cache
def connected_shapes(world, size):
    if size == 1:
        return {(ORIGIN,)}
    out = set()
    for shape in connected_shapes(world, size-1):
        old = set(shape)
        for v in neighborhood(world, old)-old:
            out.add(canonical(world, old|{v}))
    return out


def near_two_pieces(world):
    """Four centers with two contact components, at native distance two or three."""
    reps = set()
    for size in (2, 3):
        for shape in connected_shapes(world, size):
            old = set(shape)
            exclude = old | neighborhood(world, old)
            nearby = set().union(*(ball(world, v, 3) for v in old)) - exclude
            for x in nearby:
                if size == 3:
                    reps.add(canonical(world, old|{x}))
                else:
                    for y in world(x)-exclude:
                        reps.add(canonical(world, old|{x,y}))
    return reps


def colored_graph(world, centers, with_centers):
    U = set(centers)
    T = neighborhood(world, U)-U
    vertices = sorted(U|T if with_centers else T)
    colors = tuple(-1 if v in U else len(world(v)&U) for v in vertices)
    adjacency = tuple(tuple(i for i, y in enumerate(vertices) if y in world(x)) for x in vertices)
    return colors, adjacency


def connected(adjacency):
    seen = {0}
    todo = [0]
    while todo:
        for j in adjacency[todo.pop()]:
            if j not in seen:
                seen.add(j)
                todo.append(j)
    return len(seen) == len(adjacency)


def bucket(graph):
    colors, adj = graph
    return tuple(sorted((colors[i], len(nn), tuple(sorted((colors[j],len(adj[j])) for j in nn)))
                        for i, nn in enumerate(adj)))


def isomorphisms(left, right):
    """Exact color-preserving bijection count, with simultaneous equitable refinement."""
    C, A = left
    D, B = right
    if len(C) != len(D):
        return 0
    def count(c, d):
        while True:
            l = [(col,tuple(sorted(c[j] for j in ns))) for col, ns in zip(c,A)]
            r = [(col,tuple(sorted(d[j] for j in ns))) for col, ns in zip(d,B)]
            if Counter(l) != Counter(r):
                return 0
            codes = {v:i for i,v in enumerate(sorted(set(l)))}
            stable = len(set(c)) == len(codes)
            c, d = [codes[v] for v in l], [codes[v] for v in r]
            if stable:
                break
        sizes = Counter(c)
        if len(sizes) == len(c):
            return 1
        label = min((n,i) for i,n in sizes.items() if n>1)[1]
        c[c.index(label)] = len(sizes)
        ans = 0
        for j,y in enumerate(d):
            if y == label:
                new = list(d)
                new[j] = len(sizes)
                ans += count(c, new)
        return ans
    return count(list(C), list(D))


def shell_test(world):
    src = sorted(world(ORIGIN))
    edges = [{i for i,v in enumerate(src) if v in world(u)} for u in src]
    order = [0]
    while len(order) < len(src):
        unseen = set(range(len(src))) - set(order)
        order.append(max(unseen, key=lambda i:(len(edges[i]&set(order)),i)))
    placed = {0:ORIGIN}
    images = Counter()
    def visit(j):
        if j == len(order):
            images[frozenset(placed.values())] += 1
            return
        new = order[j]
        adj = [world(v) for i,v in placed.items() if i in edges[new]]
        possible = set.intersection(*(set(nb) for nb in adj)) - set(placed.values())
        for i,v in placed.items():
            if i not in edges[new]:
                possible -= world(v)
        for v in possible:
            placed[new] = v
            visit(j+1)
            del placed[new]
    visit(1)
    true = {world(x) for x in world(ORIGIN)}
    assert images and set(images) <= true
    around = ball(world,ORIGIN,2) - {ORIGIN} - world(ORIGIN)
    common = {x:world(x)&world(ORIGIN) for x in around}
    assert max(map(len,common.values())) == 4
    maximal = [s for s in common.values() if len(s)==4]
    coverage = max(len(a|b|c) for a,b,c in combinations(maximal,3))
    assert coverage < 12
    # If fewer than two pairs have a common neighbor the total is at most 4.
    triple_max = max(len(common[a])+len(common[b])+len(world(a)&world(b))
                     for a,b in combinations(around,2) if b not in world(a))
    assert triple_max < 12
    clique = max(len(S) for k in range(1,5) for S in combinations(src,k)
                 if edge_count(world,S)==k*(k-1)//2)
    assert clique==3
    return dict(anchored_embeddings=sum(images.values()),native_images=len(images),
                max_common=4,max_cover_from_three_maximal=coverage,
                independent_triple_pair_sum_max=triple_max,link_has_no_four_clique=True)


def metric_pairs(world, points):
    """Native distances and number of shortest paths, invariant under every graph automorphism."""
    out = []
    for i,start in enumerate(points):
        dist, count = {start:0}, Counter({start:1})
        todo = deque([start])
        unseen = set(points[i+1:])
        while unseen:
            u = todo.popleft()
            unseen.discard(u)
            for v in world(u):
                if v not in dist:
                    dist[v] = dist[u]+1
                    todo.append(v)
                if dist[v] == dist[u]+1:
                    count[v] += count[u]
        out.extend((dist[v],count[v]) for v in points[i+1:])
    return sorted(out)


def actual_example(world, U):
    centers = set(U)
    omega = centers | neighborhood(world, centers)
    occupied = set(ball(world,ORIGIN,9))-omega
    def check(points):
        found = {min(points)}
        while True:
            new = (neighborhood(world,found)&points)-found
            if not new:
                return found==points
            found |= new
    assert check(omega) and check(occupied)
    assert neighborhood(world,omega) <= occupied|omega
    boundary = {x for x in omega if world(x)&occupied}
    assert omega-boundary==centers
    return dict(centers=U,occupied=len(occupied),frontier=len(boundary),
                cut=cut(world,U),distance_and_number_of_geodesics=metric_pairs(world,U))


def rooted_witness(world, first, second):
    def boundary(U):
        inside=set(U)
        return sorted(neighborhood(world,inside)-inside)
    def rooted(graph,i):
        colors,adj=graph
        return tuple(100+c if j==i else c for j,c in enumerate(colors)),adj
    def successor(U,x):
        remaining=(set(U)|set(boundary(U)))-{x}
        frontier=sorted(v for v in remaining if len(world(v)&remaining)<12)
        weights=tuple(12-len(world(v)&remaining) for v in frontier)
        adj=tuple(tuple(j for j,y in enumerate(frontier) if y in world(v)) for v in frontier)
        return weights,adj
    left,right=colored_graph(world,first,False),colored_graph(world,second,False)
    T,V=boundary(first),boundary(second)
    old=rooted(left,0)
    j=next(i for i in range(len(V)) if isomorphisms(old,rooted(right,i)))
    a,b=T[0],V[j]
    x,y=successor(first,a),successor(second,b)
    number=isomorphisms(x,y)
    assert number>0
    return dict(left=a,right=b,rooted_current_isomorphisms=isomorphisms(old,rooted(right,j)),
                exposed_left=len(world(a)&set(first)),exposed_right=len(world(b)&set(second)),
                successor_vertices=len(x[0]),successor_weighted_isomorphisms=number)


def verify(world):
    shell = shell_test(world)
    # Far pieces have size at most three. Check that their individual boundaries are connected.
    for n in (1,2,3):
        for S in connected_shapes(world,n):
            assert connected(colored_graph(world,S,False)[1])
    shapes = near_two_pieces(world)
    for n in (4,5):
        shapes |= {S for S in connected_shapes(world,n) if cut(world,S)<=44}
    profile = Counter()
    buckets = defaultdict(list)
    cross, raw_pairs = Counter(), Counter()
    witness = None
    for S in sorted(shapes):
        d = cut(world,S)
        assert d in (36,38,40,42,44)
        T = colored_graph(world,S,False)
        full = colored_graph(world,S,True)
        assert connected(T[1])
        # Distinct hidden centers have distinct (at least 8-point) visible neighborhoods.
        assert len({world(v)-set(S) for v in S})==len(S)
        assert isomorphisms(T,T)==isomorphisms(full,full)
        profile[len(S),d]+=1
        group=buckets[d,bucket(T)]
        for V,E,F in group:
            raw_pairs[d]+=1
            nr=isomorphisms(E,T)
            extended=isomorphisms(F,full)
            assert nr==extended
            if nr:
                cross[d]+=1
                if witness is None and metric_pairs(world,V)!=metric_pairs(world,S):
                    witness=dict(first=actual_example(world,V),second=actual_example(world,S),
                                 color_isomorphisms=nr,extended=extended,
                                 marked=rooted_witness(world,V,S))
        group.append((S,T,full))
    assert witness
    return dict(shell=shell,templates={f'{n}/{d}':v for (n,d),v in sorted(profile.items())},
                total=len(shapes),cross_pairs_requiring_exact_test=dict(sorted(raw_pairs.items())),
                congruence_representatives_with_isomorphic_boundary_pairs=dict(sorted(cross.items())),
                rooted_current_example=witness)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    record={N.__name__:verify(N) for N in (fcc,hcp)}
    data=json.dumps(record,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(data)
    else:
        print(data,end='')


if __name__=='__main__':
    main()
