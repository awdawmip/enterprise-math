"""Degree-46 native FCC/HCP boundary certificate; standard library only."""
import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path

BASE_DIGEST = "82b672fa3179d66f5e0e4b337126485e45948da87e333035b9995a33c0533f9c"
BASE_FILE = Path(__file__).resolve().parents[1] / "seventysixth" / "completion_check.py"


def read_native(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != BASE_DIGEST:
        raise ValueError("Native core differs from the cited wave-76 source")
    spec = importlib.util.spec_from_file_location("r043_native_wave76", path)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    return core


def hidden_four(core, world):
    origin = core.ORIGIN
    shell = world(origin)
    second = sorted(core.ball(world, origin, 2) - {origin} - shell)
    overlap = {z: shell & world(z) for z in second}
    by_size = Counter()
    maximal = None
    for four in combinations(second, 4):
        if core.edge_count(world, four) != 1:
            continue
        covered = len(set.union(set(), *(overlap[z] for z in four)))
        by_size[covered] += 1
        if maximal is None or covered > maximal[0]:
            maximal = (covered, four)
    assert maximal[0] < len(shell)
    return dict(distance_two_vertices=len(second),
                four_centers_one_edge_count=sum(by_size.values()),
                coverage_histogram=dict(sorted(by_size.items())),
                maximal_coverage=maximal[0], maximal_example=maximal[1])


def hidden_five(core, world):
    shapes = set()
    for predecessor in core.connected_shapes(world, 4):
        old = set(predecessor)
        e = core.edge_count(world, old)
        for x in core.neighborhood(world, old) - old:
            if e + len(world(x) & old) == 7:
                shapes.add(core.canonical(world, old | {x}))

    graphs = []
    records = []
    for s in sorted(shapes):
        occupied = set(s)
        boundary = core.neighborhood(world, occupied) - occupied
        possible_centers = core.neighborhood(world, boundary)
        whole_shells = {z for z in possible_centers if world(z) <= boundary}
        assert not whole_shells
        boundary_graph = core.colored_graph(world, s, False)
        extension = core.colored_graph(world, s, True)
        assert core.cut(world, s) == 46 and core.connected(boundary_graph[1])
        assert len({world(z) - occupied for z in s}) == len(s)
        graphs.append((boundary_graph, extension))
        records.append(dict(centers=s, boundary_vertices=len(boundary), complete_shells=0))
    # Only 3 or 13 coordinate shapes, so check every pair, including self pairs.
    for i, j in combinations_with_replacement(range(len(graphs)), 2):
        b1, e1 = graphs[i]
        b2, e2 = graphs[j]
        nb = core.isomorphisms(b1, b2)
        ne = core.isomorphisms(e1, e2)
        assert nb == ne
        if i == j:
            records[i]["boundary_automorphisms"] = nb
            records[i]["completion_automorphisms"] = ne
        else:
            assert nb == 0
    return dict(shape_count=len(records),
                all_self_and_cross_pairs=len(records) * (len(records) + 1) // 2,
                boundary_automorphism_sum=sum(x["boundary_automorphisms"] for x in records),
                isomorphic_distinct_coordinate_shapes=0, shapes=records)


def reconstruct_embedded(world, lattice, colors):
    """Return (infinite-background membership, finite set of opposite values)."""
    if not colors:
        return False, set()
    coeffs, step = ((3, 2, 1), (1, 1, 0)) if lattice == 'fcc' else ((1, -1, 0), (1, -1, 0))
    def height(point):
        return sum(a*b for a,b in zip(coeffs, point))
    levels = [height(p) for p in colors]
    top = max(levels)
    edge_counts = [d for p, d in colors.items() if height(p) == top]
    background = any(d != 1 for d in edge_counts)
    if background and min(edge_counts) < 3:
        raise ValueError("inconsistent extreme-level counts")
    box = [range(min(p[i] for p in colors), max(p[i] for p in colors)+1)
           for i in range(3)]
    diff = set()
    for x in sorted(product(*box), key=height, reverse=True):
        if lattice == 'fcc' and sum(x) % 2:
            continue
        if x in colors:
            value = False
        else:
            y = tuple(a+b for a,b in zip(x,step))
            if y not in colors:
                value = background ^ (y in diff)
            else:
                value = colors[y] - sum(background ^ (z in diff) for z in world(y) if z != x)
                if value not in (0, 1):
                    raise ValueError("invalid embedded shell")
        if bool(value) != background:
            diff.add(x)
    incidences = Counter(y for x in diff for y in world(x))
    if background:
        rebuilt = {x: 12 - incidences[x] for x in diff if incidences[x] < 12}
    else:
        rebuilt = {y: n for y, n in incidences.items() if y not in diff}
    if rebuilt != colors:
        raise ValueError("reconstructed boundary does not match the supplied counts")
    return background, diff


def embedded_checks(core):
    result = {}
    for name in ('fcc','hcp'):
        world = getattr(core,name)
        origin = core.ORIGIN
        nbrs = sorted(world(origin))
        block = [origin, *nbrs[:3], *nbrs[-3:]]
        shapes = [{point for k,point in enumerate(block) if mask >> k & 1}
                  for mask in range(1,1<<len(block))]
        shapes.extend([set(core.ball(world,origin,r)) for r in (1,2,3)])
        largest = {}
        for dark in (False,True):
            for S in shapes:
                counts = Counter(z for v in S for z in world(v))
                if dark:
                    colors = {x:12-counts[x] for x in S if counts[x] < 12}
                else:
                    colors = {x:n for x,n in counts.items() if x not in S}
                assert reconstruct_embedded(world,name,colors) == (dark,S)
                if sum(colors.values()) > largest.get(str(dark),0):
                    largest[str(dark)] = sum(colors.values())
        assert reconstruct_embedded(world,name,{}) == (False,set())
        try:
            reconstruct_embedded(world, name, {origin: 2})
        except ValueError:
            pass
        else:
            raise AssertionError("inconsistent singleton was accepted")
        result[name] = {'nonempty_finite_tests':len(shapes),'cofinite_tests':len(shapes),
                        'largest_deficit_per_background':largest}
    return result


def check(core):
    result = {"base_core_sha256": BASE_DIGEST}
    for name in ("fcc", "hcp"):
        world = getattr(core, name)
        shell = world(core.ORIGIN)
        common_links = Counter()
        for v in shell:
            common = shell & world(v)
            common_links[len(common), core.edge_count(world, common)] += 1
        assert common_links == {(4, 2): 12}
        result[name] = dict(adjacent_common_neighbor_graph={"vertices": 4, "edges": 2, "directions_checked": 12},
                            original_shell_rigidity=core.shell_test(world),
                            hidden_four=hidden_four(core, world), hidden_five=hidden_five(core, world))
    result["embedded"] = embedded_checks(core)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--native", type=Path, default=BASE_FILE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(check(read_native(args.native)), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
