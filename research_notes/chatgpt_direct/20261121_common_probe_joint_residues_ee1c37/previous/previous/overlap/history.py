"""Integer dual certificates and a matching witness for 13-to-14 migration."""
import argparse
import json
import os
import subprocess
import sys
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent

def history(previous):
    third=previous/'previous/previous/previous'
    second=third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
    sys.path.insert(0,str(third/'group'))
    from generate import maps,observation_file
    from cyclic11 import class_cost,observations
    linear,translations,_=maps()
    affine=[bytes(t[x] for x in m) for m in linear for t in translations]
    assert len(set(affine))==len(affine)==12000
    coarse=json.loads((third/'asymmetric8721/groups.json').read_text())
    fine=json.loads((previous/'overlap/witness14.json').read_text())
    bad,menus=observations()
    def labels(rows):
        ids={x:i for i,row in enumerate(rows)for x in row}
        return ' '.join(str(ids[x])for x in range(125))
    for table,count,cost in [(coarse,13,8721),(fine,14,7660)]:
        assert len(table)==count and sorted(sum(table,[]))==list(range(125))
        assert all(not bad[x][y]>>z&1 for r in table for x,y,z in combinations(r,3))
        assert sum(class_cost(row,menus)for row in table)==cost
    mask=lambda row:sum(1<<x for x in row)
    with TemporaryDirectory()as tmp:
        w=Path(tmp)
        for name,src in [('seeds',second/'curve/class_minima.cpp'),('dual',HERE/'dual.cpp'),('distance',previous/'orbit_distance/distance.cpp')]:
            subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',src,'-o',w/name],check=True)
        observation_file(w/'obs')
        subprocess.run([w/'seeds',w/'obs',w/'seedrows'],stdout=subprocess.DEVNULL,check=True)
        def put(name,rows):
            (w/name).write_text(''.join(f'{m%2**64} {m>>64}\n' for m in rows))
        seed={8:set(),9:set()}
        for line in (w/'seedrows').read_text().splitlines():
            n,c,*r=map(int,line.split())
            if (n,c) in ((8,419),(9,557)):seed[n].add(tuple(r))
        for n,rows in seed.items():
            centered={tuple(sorted(l[i]for i in r))for l in linear for r in rows}
            bank={mask(t[i]for i in r) for t in translations for r in centered}
            assert len(bank)=={8:28000,9:24000}[n]
            put('full'+str(n),bank)
        old=list(map(mask,coarse));put('old',old)
        default=json.loads((HERE/'weights.json').read_text())['points']
        extra=json.loads((HERE/'branchweights.json').read_text())
        nines=[i for i,r in enumerate(coarse)if len(r)==9]
        by_size={};assert len(nines)==9
        jobs=[]
        for k in range(4):
            for fixed in combinations(nines,k):
                occ=sum(old[i]for i in fixed)
                free=[x for x in range(126)if not occ>>x&1]
                key='-'.join(map(str,fixed))
                weights=extra[key][1] if key in extra else [default[x]for x in free]
                assert len(weights)==len(free)and all(isinstance(q,int)for q in weights)
                jobs.append(' '.join(map(str,[sum(1<<i for i in fixed),*weights])))
        threshold=json.loads((HERE/'threshold.json').read_text())
        raw=subprocess.check_output([w/'dual',w,str(threshold),'9000000000'],input='\n'.join(jobs),text=True)
        scored=[tuple(map(int,line.split()))for line in raw.splitlines()]
        assert [i for i,_,_,_ in scored]==[int(line.split()[0]) for line in jobs]
        assert len(set(i for i,_,_,_ in scored))==len(scored)==130
        for k in range(4):
            vals=[v for i,v,flag,nodes in scored if i.bit_count()==k]
            by_size[str(k)]={'cases':len(vals),'max_numerator':max(vals)}
        assert all(flag==0 for i,v,flag,nodes in scored)
        bound=126-threshold
        (w/'maps').write_bytes(b''.join(affine))
        raw=subprocess.check_output([w/'distance',w/'maps'],input=f'13 14\n{labels(coarse)}\n{labels(fine)}\n',text=True)
        stats=[tuple(map(int,line.split()))for line in raw.splitlines()]
        best=max(h for _,_,h in stats)
        assert len(stats)==12000
        return dict(denominator=1000,by_number_of_exact_matches=by_size,minimum_changed_lower=bound,
                    excluded_retained_threshold=threshold,residual_search_nodes=sum(nodes for i,v,flag,nodes in scored),
                    known_fourteen_affine_positions=len(stats),maximum_retained_in_known_orbit=best,
                    known_orbit_by_intact={str(k):dict(positions=sum(s==k for i,s,h in stats),
                        maximum_retained=max(h for i,s,h in stats if s==k)) for k in sorted({s for i,s,h in stats})},
                    minimum_changed_in_known_orbit=125-best,first_attaining_map=next(i for i,s,h in stats if h==best))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',required=True,type=Path)
    print(json.dumps(history(p.parse_args().previous.resolve()),sort_keys=True,indent=2))
