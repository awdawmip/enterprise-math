"""Exact contact, degree and induced-subgraph certificates for the D<36 theorem."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
import json

ORIGIN = (0, 0, 0)
FCC_DIRECTIONS = [v for v in product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 2]
PLANAR = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))
MODULUS = 1009


@lru_cache(maxsize=None)
def fcc(p):
    x, y, z = p
    return frozenset((x+i, y+j, z+k) for i, j, k in FCC_DIRECTIONS)


@lru_cache(maxsize=None)
def hcp(p):
    x, y, z = p
    offsets = ((0, 0), (-1, 0), (0, -1)) if z % 2 == 0 else ((0, 0), (1, 0), (0, 1))
    return frozenset([(x+i, y+j, z) for i, j in PLANAR] +
                     [(x+i, y+j, z+k) for i, j in offsets for k in (-1, 1)])


def expand(neighbors, seed, radius):
    reached = set(seed)
    for _ in range(radius):
        reached |= set().union(*(neighbors(p) for p in reached))
    return reached


def connected(neighbors, vertices):
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        fresh = (neighbors(stack.pop()) & vertices) - seen
        seen.update(fresh)
        stack.extend(fresh)
    return seen == vertices


def rank_mod(matrix):
    rows = [v.copy() for v in matrix]
    rank = 0
    for j in range(len(rows[0])):
        piv = next((i for i in range(rank, len(rows)) if rows[i][j] % MODULUS), None)
        if piv is None:
            continue
        rows[piv], rows[rank] = rows[rank], rows[piv]
        inv = pow(rows[rank][j], -1, MODULUS)
        rows[rank] = [a*inv % MODULUS for a in rows[rank]]
        for i in range(rank+1, len(rows)):
            multiple = rows[i][j] % MODULUS
            if multiple:
                rows[i] = [(a-multiple*b) % MODULUS for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def pair_check(neighbors, second):
    first_side = neighbors(ORIGIN) - {second}
    second_side = neighbors(second) - {ORIGIN}
    positive = first_side | second_side
    both = first_side & second_side
    exclusive = sorted(first_side ^ second_side)
    planted = [1 if y in first_side else -1 for y in exclusive]
    rows = []
    for y in sorted(positive):
        adjacent = neighbors(y)
        row = [int(z in adjacent) for z in exclusive]
        if y not in both:
            row[exclusive.index(y)] -= 8 - len(adjacent & positive) - len(adjacent & both)
        rows.append(row)
    rows.append([1]*len(exclusive))
    assert all(sum(a*b for a, b in zip(row, planted)) == 0 for row in rows)
    assert rank_mod(rows) == len(exclusive)-1
    return len(both)


def mask_of(indices):
    return sum(1 << i for i in indices)


def visible(neighbors, hidden):
    sites = sorted(set().union(*(neighbors(p) for p in hidden)) - hidden)
    deficits = [len(neighbors(y) & hidden) for y in sites]
    adjacency = [mask_of(i for i, z in enumerate(sites) if z in neighbors(y)) for y in sites]
    return sites, deficits, adjacency


def ten_sets(neighbors, hidden, overlap):
    sites, deficits, adjacency = visible(neighbors, hidden)
    levels = {d: [i for i, v in enumerate(deficits) if v == d] for d in (1, 2, 3)}
    n3 = len(levels[3])
    n2 = overlap-2*n3
    n1 = 10-n2-n3
    fixed = mask_of(levels[3])
    ones = [mask_of(xs) for xs in combinations(levels[1], n1)]
    found = set()
    for twos in combinations(levels[2], n2):
        base = fixed | mask_of(twos)
        for one in ones:
            candidate = base | one
            remaining = candidate
            while remaining:
                bit = remaining & -remaining
                i = bit.bit_length()-1
                if (adjacency[i] & candidate).bit_count() != 5-deficits[i]:
                    break
                remaining -= bit
            if remaining == 0:
                found.add(candidate)
    expected = {mask_of(i for i, y in enumerate(sites) if y in neighbors(u))
                for u in hidden if len(neighbors(u) & hidden) == 2}
    assert found == expected
    return len(found)


def root_link_order(neighbors):
    link = sorted(neighbors(ORIGIN))
    order = []
    while len(order) < len(link):
        remaining = [v for v in link if v not in order]
        order.append(max(remaining, key=lambda v: len(neighbors(v) & set(order))))
    return [[j for j, v in enumerate(order[:i]) if v in neighbors(u)] for i, u in enumerate(order)]


def induced_links(adjacency, template):
    """Visit every induced injective map. Only distinct unordered images survive."""
    possible = mask_of(i for i, a in enumerate(adjacency) if a.bit_count() >= 4)
    copies = set()

    def extend(sequence, mask):
        i = len(sequence)
        if i == len(template):
            copies.add(mask)
            return
        choices = possible & ~mask
        for j, pos in enumerate(sequence):
            choices &= adjacency[pos] if j in template[i] else ~adjacency[pos]
        while choices:
            bit = choices & -choices
            choices -= bit
            extend(sequence + (bit.bit_length()-1,), mask | bit)

    extend((), 0)
    return copies


def isolated_check(neighbors, edge, isolated, template):
    sites, _, adjacency = visible(neighbors, edge | {isolated})
    expected = mask_of(i for i, y in enumerate(sites) if y in neighbors(isolated))
    assert induced_links(adjacency, template) == {expected}


def sharp_witness(neighbors, hidden):
    omega = expand(neighbors, hidden, 1)
    occupied = expand(neighbors, {ORIGIN}, 6) - omega
    assert connected(neighbors, occupied) and connected(neighbors, omega)
    assert expand(neighbors, omega, 1) - omega <= occupied
    front = {y for y in omega if neighbors(y) & occupied}
    assert omega-front == hidden
    boundary = sum(12-len(neighbors(y) & occupied)-len(neighbors(y) & front) for y in front)
    assert boundary == 36
    return {"hidden": sorted(hidden), "occupied_size": len(occupied), "frontier_size": len(front),
            "defect": boundary}


def world(neighbors):
    link = sorted(neighbors(ORIGIN))
    assert len(link) == 12 and connected(neighbors, set(link))
    for y in link:
        assert ORIGIN in neighbors(y) and len(neighbors(y) & set(link)) == 4
    reached = {ORIGIN}
    pair_rows = {}
    for radius in (1, 2, 3):
        layer = expand(neighbors, reached, 1) - reached
        reached.update(layer)
        counts = Counter(pair_check(neighbors, y) for y in sorted(layer))
        pair_rows[radius] = dict(sorted(counts.items()))
    triple_counts = Counter()
    for a, b in combinations(link, 2):
        hidden = {a, b, ORIGIN}
        triangle = b in neighbors(a)
        count = ten_sets(neighbors, hidden, 6 if triangle else 8)
        assert count == (3 if triangle else 1)
        triple_counts['triangles' if triangle else 'paths'] += 1

    template = root_link_order(neighbors)
    near = 0
    for a in link:
        edge = {a, ORIGIN}
        placements = expand(neighbors, edge, 3) - expand(neighbors, edge, 1)
        for z in sorted(placements):
            isolated_check(neighbors, edge, z, template)
        near += len(placements)
        # Disjoint positive subgraphs at distances >=4: this test checks
        # that the adjacent-pair component contains no extra full link.
        isolated_check(neighbors, edge, (20, 0, 0), template)

    triangle = next({a, b, c} for a, b, c in combinations(link, 3)
                    if b in neighbors(a) and c in neighbors(a) & neighbors(b))
    independent = next({a, b, c} for a, b, c in combinations(link, 3)
                       if b not in neighbors(a) and c not in neighbors(a) | neighbors(b))
    return {"pair_count_by_native_distance_and_common_visible_neighbors": pair_rows,
            "pair_rational_nullity": 1, "triangle_and_path_template_counts": dict(triple_counts),
            "near_isolated_site_and_oriented_edge_templates": near,
            "far_disjoint_template_types_checked": len(link),
            "boundary_36_three_independent": sharp_witness(neighbors, independent),
            "boundary_36_tetrahedron": sharp_witness(neighbors, triangle | {ORIGIN})}


def main():
    assert all(MODULUS % d for d in range(2, 32))
    report = {"basis": "C6 exact native 12-contact FCC/HCP. D is the sum of current deficits.",
              "pair_rank_prime": MODULUS, "FCC": world(fcc), "HCP": world(hcp)}
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
