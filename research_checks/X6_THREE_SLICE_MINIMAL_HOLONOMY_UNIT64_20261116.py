#!/usr/bin/env python3
"""Unit 64: exact X6 relative three-slice gluing / holonomy checker.

The selected three-axis charts are observations in Z^3/Z(1,1,1), not full native Cells.
No source mutation or unreviewed research promotion is implied by this checker.
"""
from itertools import combinations, product
from collections import Counter, defaultdict, deque
import json

AXES=tuple(range(6))
TRIPLES=tuple(combinations(AXES,3))
TREE=((0,1,2),(0,1,3),(2,4,5))        # overlap profile (0,1,2)
COMMON=((0,1,2),(0,1,3),(0,4,5))      # overlap profile (1,1,2), common vertex
CYCLE=((0,1,2),(0,3,4),(1,3,5))       # three distinct singleton overlaps


def chart(z,s):
    a=[z[i] for i in s]
    m=min(a)
    return tuple(x-m for x in a)


def solve(slices, charts):
    """Return a full Z6 potential (gauge fixed componentwise) or a typed obstruction."""
    edges=defaultdict(list)
    for triple, values in zip(slices,charts):
        for i,j in combinations(range(3),2):
            edges[(triple[i],triple[j])].append(values[i]-values[j])
    if any(len(set(observations))>1 for observations in edges.values()):
        return None, 'overlap_pair_conflict'
    graph=defaultdict(list)
    for (i,j),d in edges.items():
        graph[i].append((j,-d[0]))
        graph[j].append((i,d[0]))
    z={}
    components=0
    for start in AXES:
        if start in z:continue
        components+=1
        z[start]=0
        queue=deque([start])
        while queue:
            u=queue.popleft()
            for v,delta in graph[u]:
                expected=z[u]+delta
                if v in z:
                    if z[v]!=expected:
                        return None,'cycle_holonomy_nonzero'
                else:
                    z[v]=expected
                    queue.append(v)
    return tuple(z[i] for i in AXES), ('unique_mod_diagonal' if components==1 else 'nonunique_component_depth')


def obstruction_for_representative(slices, charts):
    intersections=sorted((tuple(set(a)&set(b)) for a,b in combinations(slices,2)),key=lambda x:len(x))
    if all(len(t)==1 for t in intersections):
        # Find the unique common vertex of each pair of successive labelled charts.
        ab=next(iter(set(slices[0])&set(slices[1])))
        bc=next(iter(set(slices[1])&set(slices[2])))
        ca=next(iter(set(slices[2])&set(slices[0])))
        def val(idx,vertex):return charts[idx][slices[idx].index(vertex)]
        return (val(0,ca)-val(0,ab))+(val(1,ab)-val(1,bc))+(val(2,bc)-val(2,ca))
    pair=[(i,j,set(a)&set(b)) for (i,a),(j,b) in combinations(list(enumerate(slices)),2) if len(set(a)&set(b))==2]
    assert len(pair)==1
    i,j,common=pair[0]; u,v=sorted(common)
    return (charts[i][slices[i].index(u)]-charts[i][slices[i].index(v)])-(charts[j][slices[j].index(u)]-charts[j][slices[j].index(v)])


def main():
    family_classes=Counter(); total=0; covered=0; connected=0
    for slices in combinations(TRIPLES,3):
        total+=1
        if len(set().union(*(set(s) for s in slices)))!=6: continue
        covered+=1
        intersections=sorted(len(set(a)&set(b)) for a,b in combinations(slices,2))
        triple=len(set(slices[0])&set(slices[1])&set(slices[2]))
        family_classes[f'{"-".join(map(str,intersections))};triple={triple}']+=1
        _,state=solve(slices,((0,0,0),)*3)
        if state=='unique_mod_diagonal':connected+=1
    assert total==1140 and covered==connected==480
    assert family_classes==Counter({'1-1-2;triple=1':180,'0-1-2;triple=0':180,'1-1-1;triple=0':120})

    local=[c for c in product(range(3),repeat=3) if min(c)==0]
    census={}
    for name,slices in [('pair_overlap_tree',TREE),('pair_overlap_common_vertex',COMMON),('three_singleton_cycle',CYCLE)]:
        outcomes=Counter(); checks=0
        for charts in product(local,repeat=3):
            z,state=solve(slices,charts)
            residue=obstruction_for_representative(slices,charts)
            assert (z is not None)==(residue==0)
            if z is not None:
                assert state=='unique_mod_diagonal'
                assert all(chart(z,sl)==c for sl,c in zip(slices,charts))
            outcomes[state]+=1
            checks+=1
        census[name]={'local_chart_families':checks, 'states':dict(outcomes)}

    # Check all 729 signed raw states in a 3x3x... cube reconstruct from each representative atlas.
    for slices in (TREE,COMMON,CYCLE):
        for z in product((-1,0,1),repeat=6):
            candidate,state=solve(slices,[chart(z,s) for s in slices])
            assert state=='unique_mod_diagonal'
            assert len({a-b for a,b in zip(candidate,z)})==1

    # Explicit signed holonomy obstruction on a triple cycle, with no repeated pair overlap.
    bad=((0,0,0),(0,0,0),(0,1,0))
    # For CYCLE, chart 3 corresponds to axes (1,3,5); its second entry at axis 3 introduces H != 0.
    H=obstruction_for_representative(CYCLE,bad)
    assert abs(H)==1 and solve(CYCLE,bad)[1]=='cycle_holonomy_nonzero'
    # Minimal L1 raw-chart repair: altering the axis-3 entry of chart 3 removes H at cost |H|.
    repaired=[list(c) for c in bad]
    # The chosen coefficient is +1 in H for chart3's shared index at axis 3 (bc).
    bc=next(iter(set(CYCLE[1])&set(CYCLE[2])))
    pos=CYCLE[2].index(bc)
    delta=-H
    repaired[2][pos]+=delta
    repaired=[chart(v,(0,1,2)) for v in repaired]   # just min-zero normalize each local 3-tuple
    assert solve(CYCLE,repaired)[1]=='unique_mod_diagonal'

    result={'schema':'X6_THREE_SLICE_HOLONOMY_UNIT64_EXACT_V1',
            'science_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
            'legacy_pin':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
            'three_slice_families':total,'full_axis_covering':covered,
            'full_axis_covering_connected':connected, 'topological_types':dict(family_classes),
            'minimal_chart_count':3,
            'local_minzero_0_to_2_count':len(local),
            'independent_chart_family_tests':len(local)**3 * 3,
            'signed_cell_lift_tests':3*(3**6),
            'representative_census':census,'cycle_nonzero_example_residue':H,
            'cycle_minimal_raw_chart_l1_repair_cost':abs(H),'status':'PASS'}
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True))

if __name__=='__main__': main()
