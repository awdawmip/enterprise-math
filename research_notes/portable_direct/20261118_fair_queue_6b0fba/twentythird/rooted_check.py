"""Recompute node-deleted induced links and sealed C6 witnesses on both contact graphs."""
import json
from collections import Counter
from functools import cache
from itertools import combinations, product

ROOT = (0, 0, 0)
PLANAR = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))
FCC_MOVES = tuple(t for t in product((-1, 0, 1), repeat=3) if sum(map(abs, t)) == 2)


@cache
def neighbors(world, point):
    x, y, z = point
    if world == "FCC":
        moves = FCC_MOVES
    else:
        parity_sign = -1 if z % 2 == 0 else 1
        offsets = ((0, 0), (parity_sign, 0), (0, parity_sign))
        moves = [(a, b, 0) for a, b in PLANAR]
        moves += [(a, b, c) for a, b in offsets for c in (-1, 1)]
    return frozenset((x+a, y+b, z+c) for a, b, c in moves)


def induced(world, sites):
    return tuple(sum(1 << i for i, y in enumerate(sites) if y in neighbors(world, x))
                 for x in sites)


def adj(graph, i, j):
    return (graph[i] >> j) & 1


def vertex_signatures(graph):
    return tuple((row.bit_count(), tuple(sorted((row & graph[j]).bit_count()
                  for j in range(len(graph)) if adj(graph, i, j))))
                 for i, row in enumerate(graph))


def isomorphisms(a, b):
    sig_a, sig_b = vertex_signatures(a), vertex_signatures(b)
    if sorted(sig_a) != sorted(sig_b):
        return
    choices = [[j for j, v in enumerate(sig_b) if v == signature] for signature in sig_a]
    order = sorted(range(len(a)), key=lambda i: len(choices[i]))
    mapping = [-1] * len(a)

    def visit(depth, used):
        if depth == len(a):
            yield tuple(mapping)
            return
        i = order[depth]
        for j in choices[i]:
            if (1 << j) & used:
                continue
            if all(adj(a, i, k) == adj(b, j, mapping[k]) for k in order[:depth]):
                mapping[i] = j
                yield from visit(depth + 1, used | (1 << j))

    yield from visit(0, 0)


def ball(world, radius):
    reached = {ROOT}
    for _ in range(radius):
        reached |= set().union(*(neighbors(world, p) for p in reached))
    return reached


def connected(world, sites):
    reached = {next(iter(sites))}
    active = list(reached)
    while active:
        added = (neighbors(world, active.pop()) & sites) - reached
        reached.update(added)
        active.extend(added)
    return reached == sites


def sealed(world, ports):
    omega = {ROOT, *ports}
    occupied = ball(world, 4) - omega
    assert connected(world, occupied) and connected(world, omega)
    for site in omega:
        assert neighbors(world, site) <= occupied | omega
    ordered = (ROOT,) + tuple(ports)
    weights = [len(neighbors(world, v) & occupied) for v in ordered]
    assert all(w > 0 for w in weights)
    assert all(w == 12-d.bit_count() for w, d in zip(weights, induced(world, ordered)))
    assert neighbors(world, ROOT) <= occupied | set(ports)
    return {"occupied":len(occupied), "weights_root_then_ports":weights, "newly_exposed":0}


def link_data(world):
    sites = tuple(sorted(neighbors(world, ROOT)))
    link = induced(world, sites)
    group = list(isomorphisms(link, link))
    edges = sum(v.bit_count() for v in link) // 2
    claws = [(i, triple) for i in range(12)
             for triple in combinations([j for j in range(12) if adj(link, i, j)], 3)
             if all(not adj(link, a, b) for a, b in combinations(triple, 2))]
    claw_incidence = [sum(i == center or i in leaves for center, leaves in claws)
                      for i in range(12)]
    assert all(row.bit_count() == 4 for row in link)
    assert claw_incidence == ([0]*12 if world == "FCC" else [2]*12)
    # A nonfrontier site cannot touch an occupied site. For each possible
    # nonempty Z, remove its closed link-neighborhood to find all legal I.
    partitions = 0
    for mask in range(1, 1 << 12):
        zero = [i for i in range(12) if mask >> i & 1]
        touch = mask
        for i in zero:
            touch |= link[i]
        free = ((1 << 12)-1) ^ touch
        occupied = free
        while occupied > 0:
            old = ((1 << 12)-1) ^ (mask | occupied)
            az = sum((link[i] & old).bit_count() for i in zero)
            zz_twice = sum((link[i] & mask).bit_count() for i in zero)
            assert az == 4*len(zero)-zz_twice
            partitions += 1
            occupied = (occupied-1) & free
    triangles = sum(all(adj(link, a, b) for a, b in combinations(t, 2))
                    for t in combinations(range(12), 3))
    if world == "FCC":
        cube = list(product((-1, 1), repeat=3))
        cube_edges = [{v for v in cube if all(y == 0 or x == y for x, y in zip(v, p))}
                      for p in sites]
        assert len({frozenset(e) for e in cube_edges}) == 12
        assert all(len(e) == 2 for e in cube_edges)
        assert all(bool(cube_edges[i] & cube_edges[j]) == bool(adj(link, i, j))
                   for i, j in combinations(range(12), 2))
    cards = {}
    for k in (12, 11, 10, 9):
        orbits = Counter(min(tuple(sorted(g[i] for i in s)) for g in group)
                         for s in combinations(range(12), k))
        cards[k] = {s:(n, induced(world, tuple(sites[i] for i in s))) for s, n in orbits.items()}
    out = {"ports_lexicographic":sites, "link_automorphisms":len(group), "edges":edges,
           "triangles":triangles, "claws":len(claws), "all_claws_center_then_leaves":claws,
           "claw_incidence_per_port":claw_incidence, "local_partitions_checked":partitions,
           "subset_orbits":{k:len(orbits) for k, orbits in cards.items()}}
    deletion = []
    for s, (count, card) in sorted(cards[10].items()):
        assert all(not list(isomorphisms(card, other)) for t, (_, other) in cards[10].items() if s != t)
        restrictions = {tuple(s.index(g[i]) for i in s) for g in group if {g[i] for i in s} == set(s)}
        autos = set(isomorphisms(card, card))
        assert restrictions <= autos
        missing = tuple(i for i in range(12) if i not in s)
        row = {"missing_indices":missing, "orbit_size":count,
               "card_aut":len(autos), "link_stabilizer_image":len(restrictions)}
        if autos != restrictions:
            row["nonextending_index_permutation_on_sorted_survivors"] = min(autos-restrictions)
            row["sealed"] = sealed(world, tuple(sites[i] for i in s))
        deletion.append(row)
    out["two_deletion_orbits"] = deletion
    return sites, cards, out


def main():
    labs, orbit_cards, world_out = {}, {}, {}
    worlds = ("FCC", "HCP")
    for world in worlds:
        labs[world], orbit_cards[world], world_out[world] = link_data(world)
    comparisons = {}
    for k in (12, 11, 10, 9):
        fcc, hcp = (orbit_cards[w][k] for w in worlds)
        matched_f, matched_h, common = set(), set(), []
        pairs = 0
        for s, (nf, a) in sorted(fcc.items()):
            for t, (nh, b) in sorted(hcp.items()):
                mapping = next(isomorphisms(a, b), None)
                if mapping is None:
                    continue
                matched_f.add(s)
                matched_h.add(t)
                pairs += nf*nh
                if any(next(isomorphisms(a, old), None) is not None for old, _ in common):
                    continue
                f_sites = tuple(labs["FCC"][i] for i in s)
                h_sites = tuple(labs["HCP"][i] for i in t)
                f_sealed = sealed("FCC", f_sites)
                h_sealed = sealed("HCP", h_sites)
                weights_f = f_sealed["weights_root_then_ports"]
                weights_h = h_sealed["weights_root_then_ports"]
                assert weights_f == [weights_h[0]] + [weights_h[1+j] for j in mapping]
                common.append((a, {"FCC_indices":s, "HCP_indices":t,
                               "FCC_to_HCP_local_indices":mapping, "FCC_sealed":f_sealed,
                               "HCP_sealed":h_sealed}))
        comparisons[k] = {"compatible_subset_pairs":pairs,
                          "participating_subsets":[sum(fcc[s][0] for s in matched_f),
                                                   sum(hcp[t][0] for t in matched_h)],
                          "common_types":len(common), "sealed_examples":[v for _, v in common]}
    assert [comparisons[k]["compatible_subset_pairs"] for k in (12, 11, 10, 9)] == [0, 0, 0, 32]
    assert comparisons[9]["common_types"] == 2 and comparisons[9]["participating_subsets"] == [16, 4]
    for world, sizes in (("FCC", (4, 16, 8)), ("HCP", (10, 8, 4))):
        orbits = world_out[world]["two_deletion_orbits"]
        extra = [r for r in orbits if r["card_aut"] != r["link_stabilizer_image"]]
        assert len(orbits) == sizes[0] and len(extra) == 1
        assert (extra[0]["card_aut"], extra[0]["link_stabilizer_image"]) == sizes[1:]
    print(json.dumps({"worlds":world_out, "induced_link_comparison":comparisons},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
