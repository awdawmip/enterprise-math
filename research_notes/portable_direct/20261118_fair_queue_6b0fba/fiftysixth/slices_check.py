"""Frozen signed-X6 and positive-BRC replay with finite slice models. Standard library."""
import argparse
from collections import Counter
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import permutations, product
import json
from math import gcd
from pathlib import Path
import sys

SIGNED = 'experiments/x6_signed_native_spatial_v16_20260905'
SOURCES = {
    SIGNED+'/x6_signed.py':'e48b6f2133edc588fde98b1b0f02ce27fecda915b152b7901300898920d52b8e',
    SIGNED+'/signed_brc.py':'6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4',
    'src/enterprise_math/brc_weighted_recurrent.py':'7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'}
EXTERNAL = {
    '03-cyclic-encoding.tex':'960fc866515885ce534bc02335027354f6da341a2fc20d3f312476e690f0adee',
    '05-common-solution.tex':'08c188bd3ad1eda12a1c839d09085f68c08246ed18471b575de7152f1877ecc4',
    '06-stacking.tex':'6f17c3d3fa81b81ee8b7f556b67e94b5d0555400f118887025509e30870be574',
    '07-three-dimensions.tex':'392bafc7b05349b5e7d9cbdfd1fb14967abbc1933d3331e5c43b55c9504269e4'}
P000 = '4b3451eeb8c5a6834f9bee906e6f840aec3deba5cb7506ac3c6e13e664d87d8f'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def load(repo, name):
    path = repo/name
    assert digest(path) == SOURCES[name]
    spec = spec_from_file_location('frozen_56_'+path.stem,path)
    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def source_paths(x6, brc, power):
    start = x6.Spatial6((3,-5,7,11,-13,17))
    axes=(0,2,4)
    words=list(permutations(range(3)))
    ends=[]
    for word in words:
        pt=start
        for j in word:
            out=pt.step(axes[j],1)
            delta=pt.displacement_to(out)
            assert brc.shortest_event_count(delta)==1 and brc.primitive_straight(delta)
            assert brc.endpoint_multiplicity(1,delta)==1
            pt=out
        ends.append(pt)
    assert len(set(ends))==1 and start != ends[0]
    endpoint=ends[0]
    disp=start.displacement_to(endpoint)
    assert brc.endpoint_multiplicity(3,disp)==brc.shortest_path_multiplicity(disp)==len(words)
    assert start.observe(axes)==endpoint.observe(axes)
    before=x6.hidden_slice_coordinates(start,axes)
    after=x6.hidden_slice_coordinates(endpoint,axes)
    assert before[0]==after[0] and after[1]-before[1]==1 and after[2]==before[2]
    for pt,data in ((start,before),(endpoint,after)):
        assert x6.from_hidden_slice_coordinates(axes,*data)==pt
    edges=[(0,1),(1,2),(2,0)]
    counts=[]
    for mask in range(8):
        constraints=[edge for k,edge in enumerate(edges) if mask & (1<<k)]
        mat=[[0]*8 for _ in range(8)]
        for seen in range(8):
            for new in range(3):
                if seen & (1<<new):
                    continue
                if all(target!=new or seen & (1<<old) for old,target in constraints):
                    mat[seen][seen|(1<<new)]=1
        total=int(power(mat,3)[0][7])
        actual=sum(all(word.index(old)<word.index(target) for old,target in constraints) for word in words)
        assert total==actual
        counts.append(total)
    assert counts==[6,3,3,1,3,1,1,0]
    return dict(axes_one_based=[a+1 for a in axes],anchor=start.coords,endpoint=endpoint.coords,
                common_observed_triple=before[0],hidden_visible_offsets=[before[1],after[1]],
                coordinates_outside_slice=before[2],word_count=len(words),
                order_constraints=['1 before 2','2 before 3','3 before 1'],
                positive_BRC_by_three_bit_constraint_mask=counts)


def transversal_checks():
    cases=[]
    for J in range(1,7):
        for D in range(1,7):
            if D**J>10000:
                continue
            M=J*D
            histogram=Counter()
            for high in product(range(D),repeat=J):
                points={v+J*h for v,h in enumerate(high)}
                # Every stabilizing displacement is a difference from the chosen source label.
                first=next(iter(points))
                size=sum(all((x+y-first)%M in points for x in points) for y in points)
                histogram[size]+=1
            max_coprime=max(t for t in range(1,J+1) if J%t==0 and gcd(t,D)==1)
            assert max(histogram)==max_coprime
            cases.append(dict(index=J,kernel_size=D,graphs=D**J,stabilizer_hist=dict(sorted(histogram.items()))))
    return dict(cases=len(cases),graphs=sum(x['graphs'] for x in cases),details=cases)


def slabs(power):
    # Quotient of Z^3 by <2e1,e2> with tile {0,e1,e3}. Two transverse residues.
    tile=[(0,0),(1,0),(0,1)]
    adj=[[0]*4 for _ in range(4)]
    for lower,upper in product(range(4),repeat=2):
        layer=[lower,upper]
        for x in range(2):
            if sum((layer[1-h]>>((x-y)%2))&1 for y,h in tile)!=1:
                break
        else:
            adj[lower][upper]=1
    assert adj==[[0,1,1,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
    masses=[int(sum(sum(row) for row in power(adj,h))) for h in range(5)]
    assert masses==[4,3,2,0,0]
    return dict(raw_tile=[[0,0,0],[1,0,0],[0,0,1]],candidate_periods=[[2,0,0],[0,1,0]],
                state_order=['00','01','10','11'],adjacency=adj,positive_BRC_walk_counts=masses)


def rod(x6,power,P):
    # The source-bit decoration is explicitly supplied for this finite test.
    def phase(x,y):
        return int((x,y)==(0,0))
    def mark(x,y,z):
        return int((z-phase(x,y))%P==0)
    rotate=[[int(j==(i+1)%P) for j in range(P)] for i in range(P)]
    assert power(rotate,P)[0][0]==1
    assert all(power(rotate,i)[0][0]==0 for i in range(1,P))
    # Lift to a raw chart with nonzero anchor and named inactive-axis residues.
    axes=(0,2,4); anchor=x6.Spatial6((3,-5,7,11,-13,17))
    def lift(pt):
        v=list(anchor.coords)
        for i,w in zip(axes,pt):
            v[i]+=w
        return x6.Spatial6(tuple(v))
    cells=list(product(range(-2,3),range(-2,3),range(-P,P+1)))
    for x,y,z in cells:
        assert sum(mark(x,y,z-j) for j in range(P))==1
        here=lift((x,y,z))
        for j in range(3):
            for sign in (-1,1):
                p=[x,y,z]; p[j]+=sign
                assert here.step(axes[j],sign)==lift(p)
    assert lift((0,0,1)).observe(axes)==lift((1,1,2)).observe(axes)
    assert mark(0,0,1)!=mark(1,1,2)
    shifts=0
    for a,b,c in product(range(-3,4),range(-3,4),range(-P,P+1)):
        lhs=all(mark(x,y,z)==mark(x+a,y+b,z+c) for x,y,z in cells)
        assert lhs==(a==b==0 and c%P==0)
        shifts+=1
    return dict(period=P,exact_one_test_cells=len(cells),tested_shifts=shifts,
                cyclic_states=P,integer_counters=2,
                indistinguishable_visible_pair=[[0,0,1],[1,1,2]],different_center_marks=[1,0])


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,default=Path('.'))
    p.add_argument('--external-sections',type=Path)
    p.add_argument('--p000',type=Path)
    args=p.parse_args()
    if args.p000:
        assert digest(args.p000)==P000
    if args.external_sections:
        assert all(digest(args.external_sections/name)==expected for name,expected in EXTERNAL.items())
    x6=load(args.repo,SIGNED+'/x6_signed.py')
    brc=load(args.repo,SIGNED+'/signed_brc.py')
    positive=load(args.repo,'src/enterprise_math/brc_weighted_recurrent.py')
    power=positive.recurrent_mass_power
    result=dict(native_source_commit='e7b9fb5084f93a9b2dbc16225629b667fb7bf46c',sources=SOURCES,
                P000_sha256=P000,external_sections_sha256=EXTERNAL,
                ordered_occurrences=source_paths(x6,brc,power),transversals=transversal_checks(),
                finite_slab=slabs(power),rod_example=rod(x6,power,5))
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
