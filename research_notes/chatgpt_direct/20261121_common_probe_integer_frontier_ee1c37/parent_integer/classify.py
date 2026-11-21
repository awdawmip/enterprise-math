"""Exact parent-tuple obstruction for the fixed cost-9858 spectrum.

All embedded candidate classes are generated afresh as subsets of complete
native mothers and priced with the original observation matrix.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import argparse
import importlib.util
import json
import time


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--artifact', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a=p.parse_args(); base=a.artifact.resolve(); start=time.perf_counter()
    bound=json.loads((Path(__file__).resolve().parent/'bindings.json').read_text())
    for rel, expected in bound['dependencies'].items():
        assert sha256((base/rel).read_bytes()).hexdigest()==expected, rel
    spec=importlib.util.spec_from_file_location('centers',base/'zero_defect_centers/replay.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    parent_path=base/'integer_cuts/mother12/native_sublevels/inputs/parent'
    data=m.run(parent_path)
    parents=sorted(int(x)+(int(y)<<64) for x,y in map(str.split,parent_path.read_text().splitlines()[:250]))
    assert max((u&v).bit_count() for u,v in combinations(parents,2))==3
    obs_path=base/'bias_extension/inputs/obs'; raw=obs_path.read_bytes()
    obs=[int.from_bytes(raw[j:j+32],'little') for j in range(0,125*125*32,32)]
    def price(ids):
        cost=0
        for x in ids:
            menus=0
            for y in ids:menus|=obs[125*x+y]
            cost+=menus.bit_count()
        return cost
    types=((11,936),(11,944),(12,1104));counts=(2,1,2)
    bank={};spectrum=Counter(); native_classes=0
    for mother in parents:
        pts=list(m.points(mother));assert price(pts)==1296
        for t in types:bank[mother,t]=[]
        for size in (11,12):
            for ids in combinations(pts,size):
                c=price(ids);spectrum[size,c]+=1;native_classes+=1
                if (size,c) in types:
                    bank[mother,(size,c)].append(sum(1<<x for x in ids))
    for key in bank:bank[key].sort()
    nodes=0;selected=[];surviving=[]
    def search(rem,used,cnt):
        nonlocal nodes
        nodes+=1
        if not rem:return all((used&f).bit_count()>=11 for f in m.FIBERS)
        union=used
        for father in rem:union|=father
        if union.bit_count()<57 or any((union&f).bit_count()<11 for f in m.FIBERS):return False
        options=[]
        for i,father in enumerate(rem):
            rows=[(j,c) for j,t in enumerate(types) if cnt[j]
                  for c in bank[father,t] if not (c&used)]
            if not rows:return False
            options.append((len(rows),i,rows))
        _,index,rows=min(options,key=lambda v:(v[0],v[1]))
        rest=rem[:index]+rem[index+1:]
        for j,c in rows:
            cnt[j]-=1;selected.append((types[j],c))
            if search(rest,used|c,cnt):return True
            selected.pop();cnt[j]+=1
        return False
    for row in data['survivors']:
        fathers=tuple(map(int,row['mothers']));selected.clear()
        if search(fathers,0,list(counts)):
            assert row['union_size']==65
            used=0
            for t,c in selected:
                assert not(c&used) and c.bit_count()==t[0] and price(list(m.points(c)))==t[1]
                used|=c
            surviving.append({'parents':list(map(str,fathers)),
                              'classes':[{'size':t[0],'cost':t[1],'mask':str(c)} for t,c in selected]})
    assert len(surviving)==4
    all_families=set()
    for row in surviving:
        for scale in (1,2):
            for shift in m.COORD:
                all_families.add(tuple(sorted(m.moved(int(v),shift=shift,scale=scale) for v in row['parents'])))
    assert len(all_families)==200
    frames=[]
    for idx in (1,2):
        point_path=base/f'integer_cuts/all_joint_exact/cover_{idx}.json'
        point=json.loads(point_path.read_text());cores=list(map(int,point['core_masks']))
        core_parents=[]
        for c in cores:
            matches=[v for v in parents if c&v==c];assert len(matches)==1
            core_parents.append(matches[0])
        compatible=sorted(v for v in all_families if all(p in v for p in core_parents))
        allowed=set(v for row in compatible for v in row)
        forbidden_weight=Fraction()
        for row in point['weights']:
            if row['cost'] not in (936,944):continue
            c=int(row['mask']);matches=[v for v in parents if c&v==c];assert len(matches)==1
            if matches[0] not in allowed:
                forbidden_weight+=Fraction(row['numerator'],row['denominator'])
        frames.append({'frame':idx,'core_masks':list(map(str,cores)),
                       'core_parents':list(map(str,core_parents)),
                       'compatible_parent_families':[[str(v) for v in row] for row in compatible],
                       'compatible_family_count':len(compatible),
                       'old_fractional_forbidden_parent_weight':str(forbidden_weight)})
    out={'status':'COMPLETE_NATIVE_PARENT_FAMILY_CLASSIFICATION',
         'cost_profile':[[9,557,2],[10,744,5],[11,936,2],[11,944,1],[12,1104,2]],
         'parent_sha256':sha256(parent_path.read_bytes()).hexdigest(),
         'obs_sha256':sha256(raw).hexdigest(),
         'all_native_embedded_subsets_priced':native_classes,
         'embedded_size_cost_counts':[[*k,v] for k,v in sorted(spectrum.items())],
         'normalized_parent_configurations':data['normalized_parent_configurations'],
         'parent_capacity_survivors':data['fiber_capacity_survivors'],
         'complete_embedded_search_nodes':nodes,
         'normalized_embedded_feasible_parent_families':surviving,
         'all_parent_family_count':len(all_families),
         'frames':frames,'elapsed_seconds':time.perf_counter()-start,
         'integer_partition_found':False,'review_status':'NOT_REVIEWED'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('normalized_embedded_feasible_parent_families','embedded_size_cost_counts')},indent=2))


if __name__=='__main__':main()
