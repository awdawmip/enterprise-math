#!/usr/bin/env python3
"""PREFIX-553: exact six-axis BRC terminal-match streams with grouped recomputation.
Frozen four-STAR X6 pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
The only scientific transition kernel is the published PREFIX-550 native BRC kernel.
Full polynomial outputs are serialized as deterministic, complete JSONL records.
"""
import argparse, hashlib, json, tempfile, os, tracemalloc
from collections import Counter, defaultdict
from statistics import median
from time import perf_counter
from pathlib import Path
import PREFIX550_shared_gauge_compact_certificate as x

ZERO6=(0,)*6

def root(i):
    c=x.P[i][2]
    return tuple((1 if c>0 else -1) if a==abs(c) else 0 for a in range(1,7))

def prepare():
    ids,g=x.classes(x.ROOTS[0]);assert g==[1,12,51]
    ph={ids[p]:x.V[p][0] for p in range(96)}
    sig={c:root(ph[c]) for c in range(51)}
    Q=x.quotient(ids,x.ZERO_ROOT)
    rows={}
    for c in range(51):
        rows[c]=Counter((j,w[6]) for (j,w),n in Q[c].items() for _ in range(n))
        assert sum(rows[c].values())==6
        assert all(sum(w[:6])==1 and w[abs(x.P[ph[c]][2])-1]==1 for (j,w) in Q[c])
    roots={r:tuple(p for p in range(96) if root(x.V[p][0])==r) for r in x.ROOTS}
    assert all(len(v)==8 for v in roots.values())
    return ids,ph,sig,rows,roots

def step(f,rows,ph):
    out=[{} for _ in range(51)]
    for c in range(51):
        axis=abs(x.P[ph[c]][2])-1
        for (j,gate),ntrans in rows[c].items():
            for mon,n in f[j].items():
                a=list(mon)
                if axis<5:a[axis]+=1
                a[5]+=gate
                t=tuple(a)
                out[c][t]=out[c].get(t,0)+ntrans*n
    return out

def recover(total,same,depth,axis):
    out=defaultdict(int)
    for mon,n in total.items():
        matching=same.get(mon,0)
        assert 0<=matching<=n
        q=list(mon[:5]);q6=depth-sum(q)
        if matching:out[tuple(q)+(q6,mon[5])]+=matching
        other=n-matching
        if other:
            q2=q.copy();s=q6
            if axis==5:s-=1
            else:q2[axis]-=1
            assert min(q2+[s])>=0 and sum(q2)+s==depth-1
            out[tuple(q2)+(s,mon[5])]+=other
    assert sum(out.values())==6**depth
    return dict(out)

def emit(fp,port,depth,hist):
    # Full exact seven-variable polynomial; integer coefficients, deterministic serialization.
    rec=[port,depth,[[*m,n] for m,n in sorted(hist.items())]]
    fp.write(json.dumps(rec,separators=(',',':'))+'\n')

def cached_stream(depth,path,prep):
    ids,ph,sig,rows,roots=prep
    totals=[[{ZERO6:1} for _ in range(51)]]
    for _ in range(depth):totals.append(step(totals[-1],rows,ph))
    with open(path,'w',encoding='utf-8') as fp:
        for r in x.ROOTS:
            f=[{ZERO6:1} if sig[c]==r else {} for c in range(51)]
            for d in range(depth+1):
                for p in roots[r]:
                    axis=abs(x.P[x.V[p][0]][2])-1
                    emit(fp,p,d,recover(totals[d][ids[p]],f[ids[p]],d,axis))
                if d<depth:f=step(f,rows,ph)
    return 96*(depth+1)

def batched_stream(depth,path,prep,batch=1):
    ids,ph,sig,rows,roots=prep
    with open(path,'w',encoding='utf-8') as fp:
        for start in range(0,12,batch):
            group=x.ROOTS[start:start+batch]
            total=[{ZERO6:1} for _ in range(51)]
            f_by_root={r:[{ZERO6:1} if sig[c]==r else {} for c in range(51)] for r in group}
            for d in range(depth+1):
                for r in group:
                    f=f_by_root[r]
                    for p in roots[r]:
                        axis=abs(x.P[x.V[p][0]][2])-1
                        emit(fp,p,d,recover(total[ids[p]],f[ids[p]],d,axis))
                if d<depth:
                    total=step(total,rows,ph)
                    for r in group:f_by_root[r]=step(f_by_root[r],rows,ph)
    return 96*(depth+1)

def native_stream(depth,path,prep):
    ids,ph,sig,rows,roots=prep
    with open(path,'w',encoding='utf-8') as fp:
        for r in x.ROOTS:
            Q=x.quotient(ids,r)
            f=[{x.ZERO_MON:1} for _ in range(51)]
            for d in range(depth+1):
                for p in roots[r]:emit(fp,p,d,f[ids[p]])
                if d<depth:f=x.evo(Q,f)
    return 96*(depth+1)

def read_records(path):
    with open(path,encoding='utf-8') as fp:
        for line in fp:
            port,d,terms=json.loads(line)
            assert all(n>0 and len(item)==8 for item in terms for n in [item[7]])
            yield (port,d),tuple(tuple(item) for item in terms)

def keyed_digest(path):
    # Root and batch schedules have different record order: normalize by (port,depth) for a source-bound checksum.
    recs={key:terms for key,terms in read_records(path)}
    assert len(recs)==sum(1 for _ in read_records(path))
    h=hashlib.sha256()
    coeff=0
    for key in sorted(recs):
        coeff+=len(recs[key])
        h.update(json.dumps([*key,recs[key]],separators=(',',':')).encode())
        h.update(b'\n')
    return {'sha256_normalized_output':h.hexdigest(),'records':len(recs),'nonzero_coefficients':coeff,'serialized_bytes':os.path.getsize(path)}

def run_one(mode,depth,prep,folder):
    path=str(Path(folder)/(mode+'.jsonl'))
    fn=(lambda:cached_stream(depth,path,prep)) if mode=='cached' else (lambda: native_stream(depth,path,prep)) if mode=='native' else (lambda:batched_stream(depth,path,prep,int(mode.split('_')[1])))
    tracemalloc.start();t=perf_counter()
    count=fn();s=perf_counter()-t
    peak=tracemalloc.get_traced_memory()[1];tracemalloc.stop()
    digest=keyed_digest(path)
    assert digest['records']==count
    return {'mode':mode,'elapsed_seconds':round(s,6),'peak_traced_bytes':peak,'output':digest,'path':path}

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--depth',type=int,default=10);pa.add_argument('--batches',default='1,3,6,12');pa.add_argument('--native',action='store_true');pa.add_argument('--output-dir',default='PREFIX553_output');args=pa.parse_args()
    assert args.depth>=0 and args.depth<=16
    prep=prepare();Path(args.output_dir).mkdir(parents=True,exist_ok=True)
    modes=['cached']+['batch_'+str(v) for v in map(int,args.batches.split(','))]
    if args.native:modes+=['native']
    tests=[]
    for mode in modes:
        rec=run_one(mode,args.depth,prep,args.output_dir)
        if tests:assert rec['output']['sha256_normalized_output']==tests[0]['output']['sha256_normalized_output'],(mode,'output mismatch')
        tests.append(rec)
        print(mode,rec['elapsed_seconds'],rec['peak_traced_bytes'],rec['output']['nonzero_coefficients'],flush=True)
    return {'status':'ALL_CHECKS_PASS','science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d','depth_inclusive':args.depth,'model':{'phases':48,'directed_edges':144,'ports':96,'classes':51,'signed_roots':12},'complete_joint_polynomial_records':96*(args.depth+1),'runs':tests}

if __name__=='__main__':
    args=main();Path('PREFIX553_EXECUTION_SUMMARY.json').write_text(json.dumps(args,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':args['status'],'depth':args['depth_inclusive'],'digest':args['runs'][0]['output']['sha256_normalized_output']},ensure_ascii=False))
