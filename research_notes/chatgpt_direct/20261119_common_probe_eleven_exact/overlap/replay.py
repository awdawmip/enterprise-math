"""Classify constrained optimal fourteen-label completions from the original menus."""
import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
HERE = Path(__file__).resolve().parent

def certify(previous, workers):
    third=previous/'previous/previous/previous'
    second=third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
    sys.path.insert(0,str(third/'group'))
    from generate import maps, observation_file
    from cyclic11 import class_cost,observations
    linear,translations,_=maps()
    bad,menus=observations()
    group=sorted(bytes(t[q] for q in l) for l in linear for t in translations)
    assert len(set(group))==12000
    mask=lambda row:sum(1<<i for i in row)
    points=lambda m:[i for i in range(125) if m>>i&1]
    def moved(m,g):return mask(g[i] for i in points(m))
    coarse=json.loads((third/'asymmetric8721/groups.json').read_text())
    old=[mask(r) for r in coarse if len(r)==9]
    assert len(old)==9
    def put(path,vals):
        path.write_text(''.join(f'{m%2**64} {m>>64}\n' for m in vals))
    with TemporaryDirectory() as tmp:
        w=Path(tmp);observation_file(w/'menu')
        for name,src in [('seeds',second/'curve/class_minima.cpp'),('search',HERE/'search.cpp'),('three',HERE/'three.cpp'),('five',HERE/'five.cpp'),('anchors',HERE/'anchors.cpp')]:
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',src,'-o',w/name],check=True)
        subprocess.run([w/'seeds',w/'menu',w/'seedrows'],stdout=subprocess.DEVNULL,check=True)
        seed={8:set(),9:set()}
        for line in (w/'seedrows').read_text().splitlines():
            n,c,*r=map(int,line.split())
            if (n,c) in ((8,419),(9,557)):seed[n].add(tuple(r))
        bank={}
        for n,rows in seed.items():
            centered={tuple(sorted(l[i] for i in r)) for l in linear for r in rows}
            bank[n]={mask(t[i] for i in r) for t in translations for r in centered}
            put(w/f'full{n}',sorted(bank[n]))
        assert {s:len(v) for s,v in bank.items()}=={8:28000,9:24000}
        put(w/'keep9',old)
        rest=set(bank[8]);orbits=[]
        while rest:
            m=min(rest);r=points(m)
            images=[mask(g[i]for i in r)for g in group]
            stab=[i for i,q in enumerate(images)if q==m]
            orbits.append((m,len(set(images)),stab));rest-=set(images)
        assert sorted(o[1]for o in orbits)==[4000,12000,12000]
        def splits_cheaply(m):
            pts=points(m)
            for left in combinations(pts,4):
                right=[x for x in pts if x not in left]
                if left[0]==pts[0] and class_cost(left,menus)==72 and class_cost(right,menus)==72:
                    return True
            return False
        assert sorted(size for m,size,stab in orbits if splits_cheaply(m))==[4000]
        special=[o for o in orbits if o[1]==4000][0]
        b,_,stab=special
        g=next(i for i in stab if group[i]!=bytes(range(125)))
        assert all(group[g][group[g][group[g][i]]]==i for i in range(125))
        (w/'case').write_text(' '.join(map(str,[2,b%2**64,b>>64,3,g,*group[g]])))
        # Each row intersects every coordinate layer in one or two points.
        planes=[mask(x for x in range(125) if (x//5**d)%5==v) for d in range(3)for v in range(5)]
        assert all(1<=(m&p).bit_count()<=2 for bnk in bank.values()for m in bnk for p in planes)
        specialized={}
        for name,k in [('three',2),('five',1)]:
            p=subprocess.run([w/name,w/'full9',w/'case',str(k)],text=True,capture_output=True,check=True)
            assert not p.stdout
            counts=[list(map(int,line.split())) for line in p.stderr.splitlines()]
            if name=='three':
                assert len(counts)==1 and counts[0][-1]==1
                specialized['C3_two_orbits']=dict(available=counts[0][0],triples=counts[0][1],residuals=counts[0][2],nodes=counts[0][3])
            else:
                assert len(counts)==31
                specialized['any_translation_orbit']=dict(directions=len(counts),eligible_orbits=sum(r[1]for r in counts),
                    residuals=sum(r[2]for r in counts),nodes=counts[-1][-1])
        # Keep three old labels plus three distinct further labels from an affine image.
        witness=json.loads((previous/'overlap/witness14.json').read_text())
        assert len(witness)==14 and sum(class_cost(r,menus) for r in witness)==7660
        wm=[mask(r) for r in witness]
        oldset=set(old)
        affine_tables=set()
        for gmap in group:
            t=tuple(sorted(mask(gmap[x] for x in r)for r in witness))
            affine_tables.add(t)
        max_overlap=max(len(oldset.intersection(t)) for t in affine_tables)
        assert len(affine_tables)==12000 and max_overlap==2
        with (w/'bases').open('w') as out:
            for t in sorted(affine_tables):
                print(*(v for m in t for v in (m%2**64,m>>64)),file=out)
        def representatives(i):
            z=subprocess.run([w/'anchors',w,str(i),'3','0','3','999999999',w/'bases'],text=True,capture_output=True,check=True)
            tag,n,vis,und=z.stdout.split()
            assert tag=='DONE' and und=='0'
            return int(n),int(vis)
        with ThreadPoolExecutor(workers)as ex:
            counts=list(ex.map(representatives,range(3)))
        augmented={'known_fourteen_orbit':len(affine_tables),'known_maximum_common':max_overlap,
            'augmented_regions':sum(q[0] for q in counts),'nodes':sum(q[1] for q in counts),
            'other_shared_classes_at_most':2,'changed_classes_relative_to_known_orbit_at_least':10}
        specified=json.loads((HERE/'cases.json').read_text())
        def run(q):
            raw=subprocess.check_output([w/'search',w,'0','1','3','999999999999','0',str(q)],text=True)
            i,n,yes=map(int,raw.split());assert i==q and not yes
            return dict(subset=q,indices=[i for i in range(9) if q>>i&1],nodes=n)
        with ThreadPoolExecutor(workers) as pool:
            cases=list(pool.map(run,specified))
        assert len(set(specified))==len(specified) and all(q.bit_count()==3 for q in specified)
        return dict(total_three_subsets=84,augmented_triples=augmented,excluded_cases=cases,remaining_unclassified=84-len(cases),
                    total_nodes=sum(v['nodes']for v in cases),eight_orbit_sizes=sorted(o[1]for o in orbits),
                    special_eight=points(b),special_eight_exclusions=specialized)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True)
    p.add_argument('--jobs',type=int,default=2)
    p.add_argument('--history-only',action='store_true')
    a=p.parse_args()
    from history import history
    if a.history_only:
        distance=history(a.previous.resolve())
        assert distance==json.loads((HERE/'history_result.json').read_text())
        print(json.dumps(distance,indent=2,sort_keys=True))
    else:
        result=certify(a.previous.resolve(),a.jobs)
        assert result==json.loads((HERE/'result.json').read_text())
        print(json.dumps(result,indent=2,sort_keys=True))
