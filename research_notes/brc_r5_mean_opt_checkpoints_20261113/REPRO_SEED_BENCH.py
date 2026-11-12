#!/usr/bin/env python3
"""Reproduce CPython frozen R5 end-to-end seed-only benchmark on the stacked branch.
Top-level import reconstructs the pinned scientific seed OUTSIDE timed child processes.
Each child receives exactly 2520 bytes of seed (base64 transport), 15 integer port
coefficients, checkpoint center ranks, and carries out decode, setup, 8192 rational
queries and JSON serialization. No 28-coordinate fixture rebuild in the timed child.
Use: python3 research_notes/brc_r5_mean_opt_checkpoints_20261113/REPRO_SEED_BENCH.py
"""
from pathlib import Path
import sys, json, base64, subprocess, statistics, tempfile

HERE=Path(__file__).resolve().parent

def child(mode,filename):
    import time, random, tracemalloc, resource, hashlib
    from fractions import Fraction as F
    from bisect import bisect_right,bisect_left

    src=json.loads(Path(filename).read_text())
    seed=base64.b64decode(src['seed_base64'])
    assert len(seed)==2520 and mode in ('greedy','bounded','mean')
    t0=time.perf_counter();tracemalloc.start()
    def bits(a,b):return [(seed[i//8]>>(7-i%8))&1 for i in range(a,b)]
    N=2880
    bp=bits(0,2*N)
    rawlabels=bits(2*N,2*N+4*(N-1))
    labels=[(rawlabels[4*i]<<3)|(rawlabels[4*i+1]<<2)|
            (rawlabels[4*i+2]<<1)|rawlabels[4*i+3] for i in range(N-1)]
    terminal=bits(2*N+4*(N-1),2*N+4*(N-1)+N)
    assert len(bp)==5760 and sum(terminal)==1065
    PN=src['port_n_coeff']; PQ=src['port_36q_coeff']
    stack=[];parents=[];end=[];pairs=[];li=0
    for a in bp:
        if a:
            par=stack[-1][0] if stack else -1
            if stack:
                op=labels[li]-1;li+=1
                pn=stack[-1][1]+PN[op]
                pq=stack[-1][2]+PQ[op]
            else:pn=pq=0
            node=len(parents)
            parents.append(par);end.append(-1)
            stack.append((node,pn,pq))
            if terminal[node]:
                assert pn<0 and pq<0 and pq%36==0
                pairs.append((-pq//36,-pn))
        else:
            node=stack.pop()[0]
            end[node]=len(parents)
    assert len(parents)==N and not stack and li==N-1 and len(pairs)==1065
    pre=[0]
    for t in terminal:pre.append(pre[-1]+t)
    lohi=[(pre[i],pre[end[i]]) for i in range(N)]
    wall=sorted({(1-F(36*q,n))/23 for q,n in pairs})
    assert len(wall)==953
    wallid={w:i for i,w in enumerate(wall)}
    codes=[wallid[(1-F(36*q,n))/23] for q,n in pairs]
    freq=[0]*len(wall)
    for t in codes:freq[t]+=1
    E=[0]
    for t in freq:E.append(E[-1]+t)
    order=sorted(range(len(pairs)),key=lambda i:(codes[i],i))
    assert E[-1]==1065
    if mode=='greedy':
        centers=[];i=0
        while i<len(E):
            j=bisect_right(E,E[i]+2)-1
            centers.append(j)
            i=bisect_right(E,E[j]+2)
    else:
        centers=src['centers'][mode]
    assert len(centers)==213
    coord=[E[i] for i in centers]
    masks=[];mask=0;k=0
    for v in coord:
        while k<v:
            mask|=1<<order[k];k+=1
        masks.append(mask)
    setup=time.perf_counter()-t0
    peak=tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    rng=random.Random(20261113)
    req=[(rng.randrange(N),rng.randrange(len(E))) for _ in range(8192)]
    for i in range(64):req[i]=(0,req[i][1])
    rational=[wall[b-1] if b else wall[0]-1 for _,b in req]
    def count(v,r):
        b=bisect_right(wall,r);x=E[b]
        j=bisect_left(coord,x)
        if j==0:c=0
        elif j==len(coord):c=j-1
        else:c=j if coord[j]-x<x-coord[j-1] else j-1
        lo,hi=lohi[v]
        if lo==hi:return 0
        ans=((masks[c]>>lo)&((1<<(hi-lo))-1)).bit_count()
        y=coord[c]
        if y<x:
            for idx in range(y,x):ans+=(lo<=order[idx]<hi)
        elif y>x:
            for idx in range(x,y):ans-=(lo<=order[idx]<hi)
        return ans
    for v,b in req[::73]:
        r=wall[b-1] if b else wall[0]-1
        lo,hi=lohi[v]
        assert count(v,r)==sum(int(code<b) for code in codes[lo:hi])
    t0=time.perf_counter()
    values=[count(v,r) for (v,b),r in zip(req,rational)]
    qt=time.perf_counter()-t0
    t0=time.perf_counter()
    data=json.dumps(values,separators=(',',':'))
    ser=time.perf_counter()-t0
    print(json.dumps({'mode':mode,'setup_seconds':setup,'query_seconds':qt,
          'serialization_seconds':ser,'combined_seconds':setup+qt+ser,
          'peak_python_allocated_setup_bytes':peak,
          'maxrss_kb':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'query_count':len(values),'output_utf8_bytes':len(data.encode()),
          'checksum':sum(values),
          'output_sha256':hashlib.sha256(data.encode()).hexdigest()},
          separators=(',',':')))

def parent():
    import importlib, contextlib, io
    # Verifier and historical stacked source execute outside the timed subprocess.
    with contextlib.redirect_stdout(io.StringIO()):
        import VERIFY_R5_MEAN_OPT_FROM_PINNED as V
    pinned=V.P.prev.pinned
    raw=pinned.raw
    assert len(raw)==2520
    fixture={
        'science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'seed_base64':base64.b64encode(raw).decode(),
        'port_n_coeff':pinned.W,
        'port_36q_coeff':pinned.K,
        'centers':{
           'bounded':V.results['213']['same_radius_centers'],
           'mean':V.results['213']['unconstrained_centers']
        }}
    with tempfile.TemporaryDirectory() as d:
        path=Path(d)/'seed_fixture.json'
        path.write_text(json.dumps(fixture))
        results={}
        for mode in ('greedy','bounded','mean'):
            rows=[]
            for _ in range(9):
                done=subprocess.run([sys.executable,str(Path(__file__).resolve()),
                         'child',mode,str(path)],capture_output=True,text=True,check=True)
                rows.append(json.loads(done.stdout))
            assert len({r['output_sha256'] for r in rows})==1
            results[mode]={
               'median_setup_ms':1000*statistics.median(r['setup_seconds'] for r in rows),
               'median_query_ms':1000*statistics.median(r['query_seconds'] for r in rows),
               'median_json_ms':1000*statistics.median(r['serialization_seconds'] for r in rows),
               'median_combined_ms':1000*statistics.median(r['combined_seconds'] for r in rows),
               'median_peak_python_setup_bytes':statistics.median(r['peak_python_allocated_setup_bytes'] for r in rows),
               'median_maxrss_kb':statistics.median(r['maxrss_kb'] for r in rows),
               'checksum':rows[0]['checksum'],
               'sha256':rows[0]['output_sha256'],'runs':len(rows)}
        assert len({r['sha256'] for r in results.values()})==1
        print(json.dumps(results,ensure_ascii=False,indent=2))

if __name__=='__main__':
    if len(sys.argv)==1:parent()
    else:
        assert len(sys.argv)==4 and sys.argv[1]=='child'
        child(sys.argv[2],sys.argv[3])
