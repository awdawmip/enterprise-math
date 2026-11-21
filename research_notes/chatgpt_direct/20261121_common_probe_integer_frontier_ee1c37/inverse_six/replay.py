"""Rebuild the normalized parents and verify the inverse9-class exclusion."""
import argparse
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import struct
import subprocess
import time

HERE=Path(__file__).resolve().parent


def mask(points):return sum(1<<p for p in points)


def shift(m,d,scale=1):
    out=0
    for p in range(125):
        if m>>p&1:
            x=(scale*(p//25)+d//25)%5
            y=(scale*(p//5%5)+d//5%5)%5
            z=(scale*(p%5)+d%5)%5
            out|=1<<(25*x+5*y+z)
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bank',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();args.output=args.output.resolve();args.output.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();b=json.loads((HERE/'bindings.json').read_text())
    raw=args.bank.read_bytes();assert sha256(raw).hexdigest()==b['native_bank_sha256']
    for name,digest in b['files'].items():assert sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    records={lo|(hi<<64):(s&255,c) for lo,hi,c,s in struct.iter_unpack('<QQII',raw)}
    assert len(records)==len(raw)//24==426500
    mothers=sorted(m for m,t in records.items() if t==(13,1296));assert len(mothers)==250
    nine={m for m,t in records.items() if t==(9,557)};assert len(nine)==24000
    observed={int(a)|(int(c)<<64) for a,c in map(str.split,(HERE/'inputs/nine557.txt').read_text().splitlines())}
    assert observed==nine
    fibers=[mask(x for x in range(125) if (x//(25,5,1)[j])%5==v) for j in range(3) for v in range(5)]
    assert all(max((m&h).bit_count() for h in fibers)<=2 for m in nine)
    centers={}
    for mother in mothers:
        coord=[]
        for j in range(3):
            counts=[(mother&h).bit_count() for h in fibers[5*j:5*j+5]]
            assert sorted(counts)==[2,2,2,2,5]
            coord.append(counts.index(5))
        centers[mother]=25*coord[0]+5*coord[1]+coord[2]
    anchor=min(m for m in mothers if centers[m]==0)
    assert {shift(anchor,d,s) for s in (1,2) for d in range(125)}==set(mothers)
    supplied=set();supplied_count=0
    for line in (HERE/'inputs/embedded_rows.txt').read_text().splitlines():
        a,c,size,cost,lo,hi=map(int,line.split());mother=a|(c<<64);child=lo|(hi<<64)
        assert mother in centers and (child&mother)==child
        assert records[child]==(size,cost)
        if (size,cost) in ((11,944),(12,1116)):
            supplied_count+=1;supplied.add((mother,child,size,cost))
            assert child>>centers[mother]&1
    generated=set()
    for mother in mothers:
        points=[i for i in range(125) if mother>>i&1]
        for removed in (1,2):
            for deleted in combinations(points,removed):
                child=mother^mask(deleted);kind=records.get(child)
                if kind in ((11,944),(12,1116)):generated.add((mother,child,*kind))
    assert generated==supplied and supplied_count==len(supplied)
    mother_file=args.output/'mothers.txt'
    mother_file.write_text(''.join(f'{m%(1<<64)} {m>>64}\n' for m in mothers))
    parents_exe=args.output/'parent_centers'
    subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'parent_centers.cpp','-o',parents_exe],check=True)
    family_file=args.output/'six_families.txt'
    answer=subprocess.run([parents_exe,mother_file,family_file],text=True,capture_output=True,check=True)
    parent_result=json.loads(answer.stdout)
    assert parent_result==json.loads((HERE/'parent_centers_expected.json').read_text())
    assert family_file.read_bytes()==(HERE/'inputs/six_families.txt').read_bytes()
    exe=args.output/'inverse'
    subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'inverse.cpp','-o',exe],check=True)
    native_start=time.monotonic()
    answer=subprocess.run([exe,HERE/'inputs/embedded_rows.txt',family_file,HERE/'inputs/nine557.txt'],
                          text=True,capture_output=True,check=True)
    native_seconds=time.monotonic()-native_start
    result=json.loads(answer.stdout);assert result==json.loads((HERE/'expected.json').read_text())
    assert result['found']==result['proper_covers']==result['embedding_attempts']==result['proper_size_rejects']==0
    assert result['proper_union_rejects']==result['proper_cover_nodes']==result['proper_attempts']==143904
    assert result['embedded_feasible_families']==672 and result['union_histogram']==[[72,672]]
    report={'complete':True,'profile':result['profile'],'total_cost':9866,'solutions':0,
            'native_bank_classes_checked':len(records),'complete_nine_family':len(nine),
            'mother_child_records_checked':len(supplied),'parent_normalization_regenerated':True,
            'parent_geometry':parent_result,'inverse_search':result,
            'native_inverse_seconds':native_seconds,'total_seconds':time.monotonic()-start,
            'original_117_profile_search_rerun':False,'short_inverse_proof_rerun':True,
            'original_menu_pricing':'Inherited complete native bank, checked by its original binding; no new pricing run is claimed.',
            'review_status':'NOT_REVIEWED'}
    (args.output/'result.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('parent_geometry','inverse_search')},sort_keys=True))


if __name__=='__main__':main()
