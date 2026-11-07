#!/usr/bin/env python3
"""PREFIX-562 complete-output diagonal q5=q6 benchmark / checksum.
Requires adjacent PREFIX550, PREFIX561, PREFIX562_compact_certificate files.
Usage: python PREFIX562_benchmark_certificate.py 16
"""
from collections import Counter
import hashlib,json,sys,time
import PREFIX550_shared_gauge_compact_certificate as n
import PREFIX561_native_port_bijection_certificate as p
import PREFIX562_compact_certificate as c

Z=(0,)*7
def orbit_map(perm):
    orbs=sorted({tuple(sorted({i,perm[i]})) for i in range(len(perm))})
    return orbs,{i:k for k,orb in enumerate(orbs) for i in orb}
def orbit_rows(rows,perm):
    orbs,loc=orbit_map(perm);result=[]
    for orb in orbs:
        candidates=[]
        for i in orb:
            rr=Counter()
            for (j,w),a in rows[i].items():rr[(loc[j],w)]+=a
            candidates.append(rr)
        assert all(row==candidates[0] for row in candidates)
        result.append(candidates[0])
    return result,loc
def benchmark(depth):
    root=n.ZERO_ROOT;raw=c.rows_raw(root);physical=c.transform(raw,0)
    ids,g=n.classes(n.ROOTS[0]);assert g==[1,12,51]
    rows51=[]
    for k in range(51):
        i=next(i for i in range(96) if ids[i]==k)
        row=Counter((ids[j],c.proj(w)) for (j,w),a in raw[i].items() for _ in range(a))
        rows51.append(row)
    f=p.construct_lift()
    rows64,where64=orbit_rows(physical,f)
    pf=[]
    for k in range(51):
        targets={ids[f[i]] for i in range(96) if ids[i]==k}
        assert len(targets)==1;pf.append(targets.pop())
    rows34,where34=orbit_rows(rows51,pf)
    cases=[('96_native',physical,list(range(96))),
           ('64_orbit',rows64,[where64[i] for i in range(96)]),
           ('51_class',rows51,ids),
           ('34_orbit_class',rows34,[where34[ids[i]] for i in range(96)])]
    outputs=[]
    for name,rows,port_ix in cases:
        start=time.perf_counter();step_seconds=0
        v=[{Z:1} for _ in rows];sha=hashlib.sha256();slots=0
        for d in range(depth+1):
            for i in range(96):
                a=v[port_ix[i]];slots+=len(a)
                sha.update(f'{d}:{i}:{sorted(a.items())}\n'.encode())
            if d<depth:
                t=time.perf_counter();v=c.multiply(rows,v);step_seconds+=time.perf_counter()-t
        outputs.append({'method':name,'states':len(rows),'elapsed_seconds':round(time.perf_counter()-start,6),
                        'evolution_seconds':round(step_seconds,6),
                        'nonzero_positions':slots,'sha256':sha.hexdigest()})
    assert len({o['sha256'] for o in outputs})==1 and len({o['nonzero_positions'] for o in outputs})==1
    return {'status':'ALL_CHECKS_PASS','depth':[0,depth],'q5_equals_q6':True,'outputs':outputs}
if __name__=='__main__':print(json.dumps(benchmark(int(sys.argv[1]) if len(sys.argv)>1 else 16),indent=2))
