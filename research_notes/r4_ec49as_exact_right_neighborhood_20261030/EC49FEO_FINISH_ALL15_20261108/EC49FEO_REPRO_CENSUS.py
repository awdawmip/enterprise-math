"""Exact three-family signed-X6 BRC 22-word census, using unchanged EC49FEN frozen dependencies.
Pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Example: python EC49FEO_REPRO_CENSUS.py 3,5,6,8,9 4 EC49FEO_35689.json
Dependencies extracted from the prior EC49FEN_complete_evidence.tar.xz archive.
"""
import json,sys,math
from concurrent.futures import ProcessPoolExecutor
from itertools import product
from collections import Counter
from functools import reduce
from time import monotonic
from EC49FEJ_SIEVE import high_keys
from EC49FEM_FEASIBILITY_6 import mask
import EC49FEK_ALT_TEST as A

J=lambda k:(k[1]+2*k[2],k[0]-2*k[2],k[2])
FAMILIES=((3,5,6,8,9),(3,5,7,8,9),(3,6,7,8,9))

def init(hs):
    A.HIGHS=tuple(hs)
    A.GROUPS={h:((16,32) if h in A.HIGHS else (1,2,4,8)) for h in range(2,10)}
    A.groups.cache_clear()

def batch(items):
    rows=[]
    for i,K in items:
        missing=[]
        for h in range(2,10):
            if h in A.HIGHS:continue
            v=reduce(lambda a,k:a|mask(h,k),K,0)
            if v&15!=15:missing.append(h)
        if missing:rows.append(dict(index=i,keys=K,status='infeasible',missing_low_horizons=missing))
        else:
            lb,counts,stop_depth=A.lower(K,cap=94)
            rows.append(dict(index=i,keys=K,
                status=('excluded93' if lb>=94 else 'unresolved'),
                lower_bound=lb,counts=counts,stop_depth=stop_depth))
    return rows

def main():
    hs=tuple(map(int,sys.argv[1].split(',')))
    assert hs in FAMILIES
    workers=int(sys.argv[2]) if len(sys.argv)>2 else 4
    output=sys.argv[3] if len(sys.argv)>3 else 'EC49FEO_'+''.join(map(str,hs))+'.json'
    opts=[high_keys(h) for h in hs if h!=3]
    inventories=[((3,1,1),)+ks for ks in product(*opts)]
    assert len(inventories)==math.prod(map(len,opts))
    s=set(inventories)
    reps=[]
    for i,K in enumerate(inventories):
        other=tuple(map(J,K))
        assert other!=K and other in s and tuple(map(J,other))==K
        if K<other:reps.append((i,K))
    assert 2*len(reps)==len(inventories)
    chunks=[reps[i:i+200] for i in range(0,len(reps),200)]
    start=monotonic()
    rows=[]
    with ProcessPoolExecutor(max_workers=workers,initializer=init,initargs=(hs,)) as ex:
        for part in ex.map(batch,chunks):rows.extend(part)
    assert len(rows)==len(reps)
    ct=Counter(r['status'] for r in rows)
    result=dict(schema='EC49FEO_SYMMETRY_REDUCED_22_PATH_EXACT_V1',
        scientific_pin='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        high_horizons=hs,all_inventories=len(inventories),representatives=len(reps),
        counts_on_representatives=dict(ct),
        counts_on_all_inventories={k:2*v for k,v in ct.items()},
        elapsed_sec=round(monotonic()-start,3),rows=rows)
    with open(output,'w') as f:json.dump(result,f,separators=(',',':'))
    print('COMPLETE',output,result['counts_on_all_inventories'])
if __name__=='__main__':main()
