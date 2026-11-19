"""Finite checks for the ternary recorder on the signed-X6 source interfaces."""
import argparse
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from io import StringIO
from itertools import combinations, permutations, product
import json
from pathlib import Path
import runpy
import sys

PIN = {
    'research_tasks/RS-EULER-RR-20261012-08.md': '6f680599df5d5bea2b06035d873f3358af23a254c9ae9d9fe0325a8ca80bd91c',
    'experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py': 'e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e',
    'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py': '6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4',
    'experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py': '6e843f505807d9d68d9847a9e55e575e7663b6321151a08b8c4fcc7cdf45e579',
    'experiments/x6_native_event_time_v1_20260906/check_event_time_markov.py': '1474c65dba67c6eecfd6aabb54181f686bd6ce20b370614c60b0123daa8b2d91',
    'src/enterprise_math/brc_weighted.py': '4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f',
}
ADAPTER = '868595349d4ed76eee8c8cd7376afa43e20e409d99e4c7c648b70fd966884621'
G = tuple(product((1, -1), range(3)))
XYZ = tuple(product(range(3), repeat=3))


def act(g, x):
    s, b = g
    return (s*x+b) % 3


def conjugate(g, h):
    s, b = g
    t, c = h
    return t, (s*c+(1-t)*b) % 3


def conjugacy_key(row):
    return min(tuple(conjugate(g, h) for h in row) for g in G)


def affine_test(xs, ys):
    if any(s != t for (s, _), (t, _) in zip(xs, ys)):
        return False
    positive = [(b,c) for (s,b), (_,c) in zip(xs,ys) if s == 1]
    negative = [(b,c) for (s,b), (_,c) in zip(xs,ys) if s == -1]
    for alpha in (1,-1):
        if all((c-alpha*b)%3 == 0 for b,c in positive):
            if len({(c-alpha*b)%3 for b,c in negative}) <= 1:
                return True
    return False


def relabel_checks():
    good, ready = [], []
    for g,h,k in product(G,repeat=3):
        if all(act(k, r+j-a) == (act(k,r)+act(g,j)-act(h,a))%3 for j,a,r in XYZ):
            good.append((g,h,k))
            if all(act(h,a) == act(k,a) for a in range(3)):
                ready.append((g,h,k))
    assert set(good) == {(g,g,k) for g in G for k in G if g[0] == k[0]}
    assert set(ready) == {(g,g,g) for g in G}
    tuples = tuple(product(G,repeat=3))
    keys = {u:conjugacy_key(u) for u in tuples}
    pairs = {u:tuple(conjugacy_key((u[i],u[j])) for i,j in combinations(range(3),2)) for u in tuples}
    false_pairs = hits = 0
    for u,v in product(tuples,repeat=2):
        match = keys[u] == keys[v]
        assert affine_test(u,v) == match
        hits += match
        false_pairs += pairs[u] == pairs[v] and not match
    one = ((1,1),(-1,0),(-1,1))
    two = ((1,1),(-1,0),(-1,2))
    assert pairs[one] == pairs[two] and keys[one] != keys[two]
    return dict(gate_stabilizer=len(good), ready_gate_stabilizer=len(ready),
                ordered_triple_pairs=len(tuples)**2, simultaneously_conjugate=hits,
                match_every_pair_but_not_triple=false_pairs, sharp_example=[one,two])


def shell_checks(triad, clock):
    unit, act_q, make_q = (triad[k] for k in ('unit','act','q_triad'))
    counts = Counter()
    for axes in combinations(range(6),3):
        q = make_q(axes)
        for extra in (False,True):
            orbits = set()
            for order in (permutations(axes) if extra else [axes]):
                for ss in product((-1,1),repeat=3):
                    start = tuple(unit(i,s) for i,s in zip(order,ss))
                    history = []
                    at = start
                    for phase in range(6):
                        end = tuple(act_q(q,x) for x in at)
                        options = [triad['midpoint_options'](a,b) for a,b in zip(at,end)]
                        assert set.intersection(*(set(op) for op in options)) == {triad['ZERO']}
                        assert clock['succ'][clock['succ']['Theta',phase]] == ('Theta',(phase+1)%6)
                        history.append(at)
                        at = end
                    assert at == start and len(set(history)) == 6
                    orbits.add(frozenset(history))
            assert len(orbits) == (8 if extra else 4)
            counts[(extra,len(orbits))] += 1
    actual_orbits = {frozenset((j,a,(r+i*(j-a))%3) for i in range(3)) for j,a,r in XYZ}
    ready = {(j,a,a) for j,a in product(range(3),repeat=2)}
    assert len(actual_orbits) == 15
    assert sum(bool(orbit & ready) for orbit in actual_orbits) == 9
    return dict(triads=20, named_shell_orbits_fixed_order=4,
                named_shell_orbits_all_orders=8, macro_period=6,
                ready_required_orbits=9, full_required_orbits=15)


def spatial_checks(spatial):
    origin = spatial['ORIGIN']
    w = (lambda x: (x+1)%3-1)
    tests = 0
    for axes in combinations(range(6),3):
        i,j,k = axes
        for xyz in product(range(-2,4), repeat=3):
            raw = [0]*6
            for index,value in zip(axes,xyz):
                raw[index] = value
            start = spatial['Spatial6'](tuple(raw))
            for exact in (False,True):
                state = start
                distance = []
                for _ in range(3):
                    x,a,r = (state.coords[axis] for axis in axes)
                    residual = state.observe(axes)
                    assert (residual[0]-residual[1]-x+a)%3 == 0
                    d = (x-a)%3
                    step = ((r-a+d)%3-(r-a)%3) if exact else w(d)
                    for _ in range(abs(step)):
                        state = state.step(k,1 if step>0 else -1)
                    assert (state.coords[k]-(x+r-a))%3 == 0
                    assert (state.coords[k]-a-(residual[2]+residual[0]-2*residual[1]))%3 == 0
                    distance.append(abs(step))
                if exact:
                    assert state == start and (not d or sorted(distance) == [1,1,2])
                else:
                    assert state.coords[k]-start.coords[k] == 3*w(d)
                tests += 1
    squares = []
    for i,j in combinations(range(3),2):
        path=[origin]
        for dim,sgn in ((i,1),(j,1),(i,-1),(j,-1)):
            path.append(path[-1].step(dim,sgn))
        assert path[0] == path[-1]
        squares.append(path)
    vertices = {x for path in squares for x in path}
    edges = {frozenset((x,y)) for path in squares for x,y in zip(path,path[1:])}
    assert len(edges)-len(vertices)+1 == 3
    return dict(signed_coordinate_checks=tests, square_graph_vertices=len(vertices),
                unoriented_edges=len(edges), free_cycle_rank=3)


def rank(rows):
    pivots = {}
    for row in rows:
        x = list(map(F,row))
        for i in sorted(pivots):
            c = x[i]
            x = [a-c*b for a,b in zip(x,pivots[i])]
        i = next((i for i,v in enumerate(x) if v),None)
        if i is not None:
            pivots[i] = [v/x[i] for v in x]
    return len(pivots)


def distributions(adapter, brc):
    hist = {}
    results = []
    for c in range(3):
        for sheet in range(2):
            source = [(j,a,r) for j,a,r in XYZ if (j-a+r)%3 == c]
            assert len(source) == 9
            pair_tables = [Counter((x[i], x[j]) for x in source) for i,j in combinations(range(3),2)]
            assert all(set(table.values()) == {1} and len(table)==9 for table in pair_tables)
            bins = [brc.CWM_ZERO for _ in range(3)]
            for j,a,r in source:
                z = (j,0,0,1,0,a,r)
                branch = brc.cwm_edge(F(1,9))
                for atom in adapter['instructions'](z,'E',sheet):
                    z = adapter['primitive'](z,atom,sheet)
                    branch = brc.cwm_propagate(branch,brc.CWM_ONE)
                assert z == (j,0,0,1,0,a,c)
                bins[c] = brc.cwm_recoalesce(bins[c],branch)
            assert [x.total for x in bins] == [int(i==c) for i in range(3)]
            hist[str((c,sheet))] = [bins[c].count,str(bins[c].total),str(bins[c].dominant)]
    rows = [[(x[i],x[j]) == val for x in XYZ] for i,j in combinations(range(3),2)
            for val in product(range(3),repeat=2)]
    results.append(rank(rows))
    for a,b in [(-1,1),(1,1),(1,-1),(-1,-1)]:
        rows.extend([[(x+a*y+b*z)%3 == c for x,y,z in XYZ] for c in range(3)])
        results.append(rank(rows))
    assert results == [19,21,23,25,27]
    return dict(plane_output_branch_count_total_max=hist, successive_ranks=results)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path.cwd())
    p.add_argument('--adapter',type=Path,default=Path(__file__).resolve().parent.parent/'hundredninth'/'feedback_check.py')
    args=p.parse_args()
    for file, digest in PIN.items():
        assert sha256((args.repo/file).read_bytes()).hexdigest() == digest, file
    assert sha256(args.adapter.read_bytes()).hexdigest() == ADAPTER
    with redirect_stdout(StringIO()):
        spatial = runpy.run_path(str(args.repo/'experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py'))
        triad = runpy.run_path(str(args.repo/'experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py'))
        clock = runpy.run_path(str(args.repo/'experiments/x6_native_event_time_v1_20260906/check_event_time_markov.py'))
    public = runpy.run_path(str(args.adapter))
    sys.path.insert(0,str(args.repo/'src'))
    from enterprise_math import brc_weighted
    output=dict(registration='RS-EULER-RR-20261012-08',source_sha256=PIN,adapter_sha256=ADAPTER,
                coordinate=spatial_checks(spatial),inner=shell_checks(triad,clock),
                frames=relabel_checks(),incidence=distributions(public,brc_weighted))
    print(json.dumps(output,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
