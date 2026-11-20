"""Reconstruct any archived exact-cover profile from its endpoint classes and orbit representatives."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent
PREVIOUS=HERE.parent/'anchors'
if not PREVIOUS.is_dir():
    PREVIOUS=HERE.parent/'proof'
sys.path.insert(0,str(PREVIOUS))
from replay import bank, maps, profiles, centre, POINTS, LOW_MASK
from extra_triples import pair_orbits
from twelve_point_geometry import describe, describe_large_classes

PROFILES = {
    8719: ('first.cpp',747,{557:8,564:1,744:1,747:1,1104:2}),
    8720: ('second.cpp',752,{557:9,747:1,752:1,1104:2}),
}

def verify(work,entry,jobs):
    results={}
    lin,translations,_=maps()
    acts=[bytes(t[i]for i in g)for g in lin for t in translations]
    rows=bank(work,lin,translations,8728)
    keys=list(rows)
    available={8719:[],8720:[]}
    for total,counts in profiles(keys,8720):
        if total in available:
            available[total].append({cost:n for (_,cost),n in zip(keys,counts) if n})
    assert len(available[8719])==2 and PROFILES[8719][2] in available[8719]
    assert {557:11,1296:2} in available[8719]
    assert available[8720]==[PROFILES[8720][2]]
    describe(rows[12,1104])
    describe_large_classes(rows)
    slice_masks=[[sum(1<<i for i in range(125) if i//stride%5==v) for v in range(5)] for stride in (1,5,25)]
    balanced=(2,2,2,2,2)
    short=(1,2,2,2,2)
    uneven=(1,2,2,2,3)
    expected={(9,557):[short]*3,(9,564):[short]*3,(10,744):[balanced]*3,
              (10,747):[uneven,balanced,balanced],(10,752):[uneven,balanced,balanced]}
    for key,signature in expected.items():
        for mask in rows[key]:
            assert sorted(tuple(sorted((mask & h).bit_count() for h in axis))
                          for axis in slice_masks)==signature
    pairs=[group for group,_ in pair_orbits(rows,acts,(12,1104),(12,1104))]
    def displacement(pair):
        a,b=pair
        first,second=centre(a),centre(b)
        lengths=[min(v,5-v) for p,q in zip(POINTS[first],POINTS[second]) if (v:=(p-q)%5)]
        return len(lengths),len(set(lengths)),bool(a>>second&1),bool(b>>first&1)
    assert [displacement(p) for p in pairs]==[
        (2,1,False,False),(1,1,False,False),(2,2,True,True),
        (3,2,False,False),(3,1,False,False),(0,0,False,False)]
    pairfile=work/'anchor_pairs'
    pairfile.write_text(''.join(' '.join(str(i)for m in p for i in(m&LOW_MASK,m>>64))+'\n'for p in pairs))
    idx_by_cost={c:(s,c) for s,c in rows}
    for total,reference in entry.items():
        source,price,profile=PROFILES[int(total)]
        assert sum(price*n for price,n in profile.items())==int(total)
        keys=[idx_by_cost[cost] for cost in profile if cost!=1104]
        with (work/'rows').open('w')as f:
            print(len(keys),file=f)
            for size,c in keys:
                arr=rows[size,c]
                print(size,c,len(arr),file=f)
                for m in arr:print(m&LOW_MASK,m>>64,file=f)
        exe=work/'solver'
        subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/source),'-o',str(exe)],check=True)
        def check(i):
            raw=subprocess.check_output([str(exe),str(work/'rows'),str(pairfile),str(price),str(i)],text=True,cwd=work)
            index,want,choices,visits,found=map(int,raw.split())
            assert index==i and want==price
            return {'orbit':i,'candidates':choices,'nodes':visits,'found':bool(found)}
        orbits=[r['orbit'] for r in reference]
        assert len(orbits)==len(set(orbits)) and all(i in range(6) for i in orbits)
        with ThreadPoolExecutor(max_workers=jobs)as pool:
            out=list(pool.map(check,orbits))
        assert out==reference,(total,out,reference)
        results[total]=out
    return results

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('reference',nargs='?',type=Path,default=HERE/'result.json')
    parser.add_argument('--jobs',type=int,default=2)
    args=parser.parse_args()
    with TemporaryDirectory()as work:
        print(json.dumps(verify(Path(work),json.loads(args.reference.read_text()),args.jobs),sort_keys=True,indent=2))
