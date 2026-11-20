"""Resolve two 8721 profiles by anchoring three distinguished message classes."""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
HERE=Path(__file__).resolve().parent
ANCHORS=next((d/'anchors' for d in (HERE.parent,HERE.parents[2]/'delivery',*HERE.parents) if (d/'anchors/extra_triples.py').is_file()),None)
if ANCHORS is None:
    ANCHORS=next(d/'round3/delivery/anchors' for d in HERE.parents if (d/'round3/delivery/anchors/extra_triples.py').is_file())
sys.path.insert(0,str(ANCHORS))
from extra_triples import pair_orbits
from replay import bank, maps, moved, LOW_MASK
from generate import profiles
CASES={936:((12,1104),(12,1104),(11,936)),744:((13,1296),(12,1104),(10,744))}

def verify(work,which):
    lin,tr,_=maps()
    group=[bytes(t[i]for i in g)for g in lin for t in tr]
    rows=bank(work,lin,tr,8728)
    types=list(rows)
    target_profiles={tuple(sorted((kind[1],n)for kind,n in zip(types,counts) if n))
                     for total,counts in profiles(types,8721) if total==8721}
    expected=[
        {557:8,569:1,744:2,1104:2},
        {557:9,744:2,1104:1,1116:1},
        {557:9,564:1,936:1,1104:2},
        {557:9,564:1,744:1,1104:1,1296:1},
    ]
    assert target_profiles=={tuple(sorted(row.items())) for row in expected}
    with (work/'nines').open('w')as f:
        print(2,file=f)
        for c in (557,564):
            masks=sorted(rows[9,c])
            print(9,c,len(masks),file=f)
            for m in masks:print(m&LOW_MASK,m>>64,file=f)
    exe=work/'typed_nines'
    subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/'typed_nines.cpp'),'-o',str(exe)],check=True)
    result={}
    for c in which:
        left,right,third=CASES[c]
        jobs=[]
        for (a,b),stab in pair_orbits(rows,group,left,right):
            choices={m for m in rows[third] if not m&(a|b)}
            while choices:
                z=min(choices)
                equiv={moved(z,g) for g in stab}
                assert equiv<=choices
                choices-=equiv
                jobs.append((a,b,z))
        jf=work/'jobs'
        with jf.open('w')as f:
            for xyz in jobs:print(*(w for m in xyz for w in (m&LOW_MASK,m>>64)),10,file=f)
        def check(first):
            end=min(first+120,len(jobs))
            out=subprocess.check_output([str(exe),str(work/'nines'),str(jf),str(first),str(end)],text=True,stderr=subprocess.DEVNULL)
            checked=[list(map(int,r.split()))for r in out.splitlines()]
            assert [i for i,_,_ in checked]==list(range(first,end)) and not any(found for _,_,found in checked)
            return sum(n for _,n,_ in checked)
        with ThreadPoolExecutor(max_workers=2)as pool:nodes=sum(pool.map(check,range(0,len(jobs),120)))
        result[str(c)]=dict(triples=len(jobs),found=False)
    return result

if __name__=='__main__':
    which=[int(i)for i in json.loads((HERE/'result.json').read_text())]
    with TemporaryDirectory()as tmp:print(json.dumps(verify(Path(tmp),which),sort_keys=True))
