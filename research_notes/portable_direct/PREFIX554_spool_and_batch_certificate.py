#!/usr/bin/env python3
"""PREFIX-554 exact BRC six-axis deep benchmark and external-memory U schedule.
Scientific kernel: PREFIX-550 at frozen f42f2906d77f24085c123f3ccfe9667d41caa96d.
Independent implementation reused from published PREFIX-553 (no new BRC semantic kernel).
"""
import argparse, hashlib, json, os, tempfile, tracemalloc
from pathlib import Path
from time import perf_counter
from collections import defaultdict
import PREFIX553_batched_depth_stream_certificate as p
import PREFIX550_shared_gauge_compact_certificate as x


def serialize(f, sink):
    """One full auxiliary-root U vector per JSONL record (all 51 classes)."""
    sink.write(json.dumps([[[*m, n] for m, n in sorted(row.items())] for row in f],
                          separators=(',', ':'))+'\n')


def deserialize(line):
    return [{tuple(item[:6]):item[6] for item in row} for row in json.loads(line)]


def disk_spooled_stream(depth, destination, prep, spool):
    """Compute all U(d) once; materialize complete U(d) to local disk, stream U for each r."""
    ids, ph, sig, rows, roots = prep
    f = [{p.ZERO6:1} for _ in range(51)]
    with open(spool, 'w', encoding='utf-8') as fp:
        for d in range(depth+1):
            serialize(f,fp)
            if d<depth:f=p.step(f,rows,ph)
    written=0
    with open(destination,'w',encoding='utf-8') as out:
        for r in x.ROOTS:
            e=[{p.ZERO6:1} if sig[c]==r else {} for c in range(51)]
            with open(spool,encoding='utf-8') as spool_reader:
                for d, line in enumerate(spool_reader):
                    total=deserialize(line)
                    for port in roots[r]:
                        axis=abs(x.P[x.V[port][0]][2])-1
                        p.emit(out,port,d,p.recover(total[ids[port]],e[ids[port]],d,axis))
                        written+=1
                    if d<depth:e=p.step(e,rows,ph)
    assert written==96*(depth+1)
    return written


def projected_spool_stream(depth, destination, prep, directory):
    """Project U(d) onto root-specific output classes at write time, then stream per root.
    One 51-state U step per depth; only 4 or 7 classes per root kept on disk.
    """
    ids, ph, sig, rows, roots=prep
    names=[str(Path(directory)/('u_r'+str(i)+'.jsonl')) for i in range(12)]
    classes_by_root=[sorted({ids[p0] for p0 in roots[r]}) for r in x.ROOTS]
    fps=[open(name,'w',encoding='utf-8') for name in names]
    try:
        u=[{p.ZERO6:1} for _ in range(51)]
        for d in range(depth+1):
            for fp,cs in zip(fps,classes_by_root):
                fp.write(json.dumps([[[*m,n] for m,n in sorted(u[c].items())] for c in cs],separators=(',',':'))+'\n')
            if d<depth:u=p.step(u,rows,ph)
    finally:
        for fp in fps:fp.close()
    count=0
    with open(destination,'w',encoding='utf-8') as output:
        for i,r in enumerate(x.ROOTS):
            es=[{p.ZERO6:1} if sig[c]==r else {} for c in range(51)]
            cs=classes_by_root[i]
            with open(names[i],encoding='utf-8') as reader:
                for d,line in enumerate(reader):
                    items=[{tuple(e[:6]):e[6] for e in item} for item in json.loads(line)]
                    totals=dict(zip(cs,items))
                    for port in roots[r]:
                        axis=abs(x.P[x.V[port][0]][2])-1
                        p.emit(output,port,d,p.recover(totals[ids[port]],es[ids[port]],d,axis))
                        count+=1
                    if d<depth:es=p.step(es,rows,ph)
    assert count==96*(depth+1)
    return count


def _measure(fn, file, canonicalize=True):
    tracemalloc.start()
    t=perf_counter(); records=fn(); elapsed=perf_counter()-t
    peak=tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    o=p.keyed_digest(file) if canonicalize else {}
    return {'elapsed_seconds':round(elapsed,6),'tracemalloc_peak_bytes':peak,
            'complete_output_records':records,'output':o}


def execute(depth,folder, modes):
    prep=p.prepare()
    Path(folder).mkdir(parents=True,exist_ok=True)
    runs={}; anchor=None
    for mode in modes:
        output=str(Path(folder)/(mode+'.jsonl'))
        spool=str(Path(folder)/'aux_U_spool.jsonl')
        if mode=='cached':
            fn=lambda:p.cached_stream(depth,output,prep)
        elif mode=='spooled':
            fn=lambda:disk_spooled_stream(depth,output,prep,spool)
        elif mode=='projected_spool':
            fn=lambda:projected_spool_stream(depth,output,prep,folder)
        elif mode.startswith('batch_'):
            b=int(mode.split('_')[1]);assert 1<=b<=12
            fn=lambda:p.batched_stream(depth,output,prep,b)
        else:raise ValueError(mode)
        res=_measure(fn,output)
        if mode=='spooled':
            res['spool_serialized_bytes']=os.path.getsize(spool)
        elif mode=='projected_spool':
            res['spool_serialized_bytes']=sum(os.path.getsize(str(Path(folder)/('u_r'+str(i)+'.jsonl'))) for i in range(12))
            res['per_root_projected_class_counts']=[len({prep[0][z] for z in prep[4][r]}) for r in x.ROOTS]
        assert res['complete_output_records']==96*(depth+1)
        if anchor is None:anchor=res['output']['sha256_normalized_output']
        assert res['output']['sha256_normalized_output']==anchor,(mode,'mismatch')
        runs[mode]=res
        print(mode,res['elapsed_seconds'],res['tracemalloc_peak_bytes'],
              res['output']['nonzero_coefficients'],flush=True)
    return {'status':'ALL_CHECKS_PASS','frozen_science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'depth_inclusive':depth,'modes':modes,'port_count':96,
            'outputs_per_mode':96*(depth+1),'normalized_complete_output_sha256':anchor,
            'runs':runs,'scope':'exact nonnegative integer seven-variable BRC/gate histograms; no native future action or Cell continuation compression'}

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--depth',type=int,default=12)
    ap.add_argument('--modes',default='cached,projected_spool,batch_1,batch_2,batch_3,batch_4,batch_5,batch_6,batch_8,batch_12')
    ap.add_argument('--output-dir',default='p554_out')
    ap.add_argument('--summary',default='PREFIX554_EXECUTION_SUMMARY.json')
    a=ap.parse_args();assert 0<=a.depth<=16
    result=execute(a.depth,a.output_dir,a.modes.split(','))
    Path(a.summary).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'depth':a.depth,'sha256':result['normalized_complete_output_sha256']},ensure_ascii=False))
