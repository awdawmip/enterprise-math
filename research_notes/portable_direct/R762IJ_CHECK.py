#!/usr/bin/env python3
"""R762IJ: exact seven-orbit obstruction to 3 critical supports with all 20 supports present.

Uses only integer tuples, set partitions, graph cycle checks and S6 permutations.
The check is a complete finite certificate of a *necessary* connectivity
condition; it makes no assertion about the exact Euler path count.
"""
from functools import lru_cache
from itertools import combinations, permutations

axes = range(6)
ports = list(combinations(axes, 2))
port_id = {x: i for i, x in enumerate(ports)}
supports = list(combinations(axes, 3))
tri = [tuple(port_id[x] for x in combinations(s, 2)) for s in supports]
assert len(ports) == 15 and len(supports) == 20

# The seven S6-orbits of unordered triples of supports are explicitly rederived.
all_triples = set(combinations(range(20), 3))
idx = {s: i for i, s in enumerate(supports)}
perms = [tuple(idx[tuple(sorted(g[a] for a in s))] for s in supports)
         for g in permutations(axes)]
orbits = []
while all_triples:
    representative = min(all_triples)
    orbit = {tuple(sorted(g[s] for s in representative)) for g in perms}
    assert orbit <= all_triples
    all_triples.difference_update(orbit)
    orbits.append((representative, len(orbit)))
assert len(orbits) == 7 and sum(size for _, size in orbits) == 1140

def merge(part, a, b):
    a, b = part[a], part[b]
    if a == b:
        return part
    return tuple(min(a, b) if v == a or v == b else v for v in part)

def incidence_forest(part, critical):
    """Bipartite incidence graph: distinct color vertices + critical support nodes.

    Every critical support must touch THREE distinct colors; its two edges
    must lie in a forest once all six candidate critical bridges are removed.
    Any partial incidence cycle survives further color identifications.
    """
    colors = {}
    for s in critical:
        values = [part[v] for v in tri[s]]
        if len(set(values)) != 3:
            return False
        for v in values:
            if v not in colors:
                colors[v] = len(colors)
    offset = len(colors)
    parent = list(range(offset + len(critical)))
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for j, s in enumerate(critical):
        for v in tri[s]:
            a, b = find(offset + j), find(colors[part[v]])
            if a == b:
                return False
            parent[a] = b
    return True

def check_critical(critical, reversed_order=False):
    noncritical = tuple(i for i in range(20) if i not in critical)
    if reversed_order:
        noncritical = noncritical[::-1]

    @lru_cache(None)
    def search(part):
        # A 6-edge bridge forest connecting 7 components is necessary.
        if len(set(part)) < 7 or not incidence_forest(part, critical):
            return False
        # Every noncritical support must have one internal Port edge:
        # at least one equality among its three Port vertices.
        for s in noncritical:
            vs = tri[s]
            if len({part[v] for v in vs}) == 3:
                # A final partition satisfying this constraint must merge
                # at least one of the 3 pairs. Explore all possibilities.
                return any(search(merge(part, a, b))
                           for a, b in combinations(vs, 2))
        # This relaxed terminal test is NECESSARY, not an assertion that
        # the original Euler histogram exists. Finding no terminal state
        # suffices to rule out the desired critical triple.
        return True

    possible = search(tuple(range(15)))
    return possible, search.cache_info()

results = []
for rep, orbit_size in orbits:
    possible, info = check_critical(rep)
    possible_reversed, _ = check_critical(rep, reversed_order=True)
    assert possible == possible_reversed
    results.append((rep, orbit_size, info.misses, info.hits, possible))
    assert not possible, (rep, 'unexpected candidate')

assert sorted(size for _, size, _, _, _ in results) == [60, 60, 120, 180, 180, 180, 360]
print('PASS R762IJ: k=3, all 20 supports is impossible')
print('support triplets up to S6: 7 orbits; total triples:', sum(row[1] for row in results))
print('representative / orbit_size / memoized_states / cache_hits / feasible')
for rep, size, nstates, hits, poss in results:
    names = [''.join(map(str, supports[s])) for s in rep]
    print(','.join(names), '/', size, '/', nstates, '/', hits, '/', poss)
print('TOTAL memoized states:', sum(r[2] for r in results))
print('CONSEQUENCE: 62-event witness upper bound, conditional on R762IH pair reduction')
