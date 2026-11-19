"""Literal frozen R11 reference, all 144 inputs and 256 calls to tick per input.
Outputs private temporary run statistics for aggregation by delay_check.py.
Scientific state and per-step observer use the supplied original source.
"""
import argparse
import json
import resource
import sys
import time
from collections import Counter
from dataclasses import replace
from pathlib import Path


def fields(s):
    return (s.q,s.pending,s.wall,s.b)


def alter(s,v,j,r,h,locations):
    """Positive complete state predicted by the single-delay theorem."""
    if h>r:return s
    p=dict(s.pending)
    q=s.q
    if h<r:
        key=(v,j,j,r-h)
        assert p[key]>0
        p[key]-=1
        if not p[key]:del p[key]
    else:
        target=v^(4>>j)
        q=list(q); row=list(q[target]);row[j]-=1
        assert row[j]>=0
        q[target]=tuple(row);q=tuple(q)
    key=(v,j,j,r+1-h)
    p[key]=p.get(key,0)+1
    return replace(s,pending=p,q=q)


def main(source,do_local=False):
    start=time.perf_counter()
    cpu=time.process_time()
    sys.path.insert(0,str(source))
    import test_cycles as R
    import hashlib
    assert hashlib.sha256((source/'test_cycles.py').read_bytes()).hexdigest()=='49d1c6ed0be596b82fa8bfa963df934fc1702cf91feda1680fb7f8d8e961c6d7'
    meta=json.loads((R.R10.R9.PARENT/'COORDINATES.json').read_bytes())
    conf=R.config('uniform',0)
    a=R.P.Arithmetic(ledger=False)
    a.stage='phase'
    m=R.instantiate(a,meta,conf)
    s=R.prepare(m,conf,literal=True)
    states=[];flows=[]
    s,_,_=R.run_one(m,s,True)
    for _ in range(6):
        states.append(s);s,inc,_=R.run_one(m,s,True);flows.append(inc)
    assert fields(states[0])==fields(s)
    assert len(s.b)==5832 and m.locations==tuple(range(728,736))
    setup=time.perf_counter()-start
    a.stage='repair' if do_local else 'reference'
    totals=Counter();rows=[]; elapsed=Counter()
    if do_local:
        from delay_local import repair_one
    for idx,base in enumerate(states):
        for (v,j,role,r),qty in sorted(base.pending.items()):
            assert j==role and qty==1
            current=alter(base,v,j,r,0,m.locations)
            assert m.normalized(current)
            a.stage='repair' if do_local else 'reference'
            assert m.total(current)==48
            observed=Counter()
            found=None
            space=0
            for h in range(1,257):
                bg=states[(idx+h)%6]
                flow=flows[(idx+h-1)%6]
                before=time.perf_counter()
                if do_local:
                    current,inc,nodes=repair_one(R,m,current,states[(idx+h-1)%6],bg,flow)
                    totals['recomputed_material_nodes']+=nodes
                else:
                    current,inc,_=R.run_one(m,current,True)
                    totals['literal_ticks']+=1
                    m.trace.clear()  # observations consumed, never a state input
                elapsed['kernel_and_source_observer_seconds']+=time.perf_counter()-before
                before=time.perf_counter()
                expected=alter(bg,v,j,r,h,m.locations)
                # Compare all q, all positive pending, all wall components, all 5832 b.
                assert fields(current)==fields(expected)
                assert current.t==base.t+h
                equal=fields(current)==fields(bg)
                if equal and found is None:found=h
                assert equal==(h>r)
                key=f'handoff:{v}:{j}:{role}'
                want=dict(flow)
                delta=int(h==r+1)-int(h==r)
                if delta:
                    want[key]=want.get(key,0)+delta
                    if not want[key]:del want[key]
                assert inc==want
                if delta: observed[key]+=delta
                assert observed.get(key,0)==-int(h==r)
                space=max(space,len(current.pending))
                totals['exact_full_fields_and_all_labelled_increments']+=1
                elapsed['whole_field_and_increment_verification_seconds']+=time.perf_counter()-before
            assert found==r+1 and all(x==0 for x in observed.values())
            rows.append([idx,v,j,role,r,found,space])
        print(('repair' if do_local else 'reference')+' completed phase '+str(idx),file=sys.stderr,flush=True)
    return dict(rows=rows,operations=dict(totals),brc_counts=a.counts,brc_max_bits=a.max_bits,
                timed_phases=dict(elapsed),setup_seconds=setup,wall_seconds=time.perf_counter()-start,
                cpu_seconds=time.process_time()-cpu,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def deep_size(objects):
    seen=set()
    def visit(obj):
        key=id(obj)
        if key in seen:return 0
        seen.add(key);size=sys.getsizeof(obj)
        if isinstance(obj,dict):
            return size+sum(visit(k)+visit(v) for k,v in obj.items())
        if isinstance(obj,(tuple,list)):
            return size+sum(visit(v) for v in obj)
        return size
    return visit(objects)


def measured_acceptance(directory,archive):
    import os
    import subprocess
    import tempfile
    commands={'verify_archive':['verify.py','--manifest','INPUT_MANIFEST.json',
                  '--require-cases','144','--max-ticks','256','--strict','--source-zip',str(archive.resolve())],
              'mutations':['test_mutations.py']}
    results={}
    for key,cmd in commands.items():
        with tempfile.TemporaryFile() as out:
            start=time.perf_counter()
            child=subprocess.Popen([sys.executable,'-B',*cmd],cwd=directory,stdout=out)
            _,status,usage=os.wait4(child.pid,0)
            child.returncode=os.waitstatus_to_exitcode(status)
            if child.returncode:raise RuntimeError((key,child.returncode))
            elapsed=time.perf_counter()-start
            out.seek(0);raw=out.read()
        results[key]=dict(cpu_seconds=usage.ru_utime+usage.ru_stime,wall_seconds=elapsed,
                          peak_rss_kib=usage.ru_maxrss,stdout_bytes=len(raw),result=json.loads(raw))
    return results


def summary(source,raw_paths,acceptance,checks,archive):
    import hashlib
    import tempfile
    from delay_check import main as portable
    records=[json.loads(p.read_bytes()) for p in raw_paths]
    assert records[0]['rows']==records[1]['rows'] and len(records[0]['rows'])==144
    obs_hist=Counter(str(row[-1]) for row in records[0]['rows'])
    for record in records:
        del record['rows']
        record['cases']=144
    t=time.perf_counter()
    source_index=(source/'MANIFEST.json').read_bytes()
    assert hashlib.sha256(source_index).hexdigest()=='f1869eeb941666ce686714ed057b39bd22f4aac1cea04e4bc9380b65e4a591c1'
    for name,binding in json.loads(source_index).items():
        data=(source/name).read_bytes()
        assert len(data)==binding['bytes'] and hashlib.sha256(data).hexdigest()==binding['sha256']
    bind_time=time.perf_counter()-t
    sys.path.insert(0,str(source))
    import test_cycles as R
    meta=json.loads((R.R10.R9.PARENT/'COORDINATES.json').read_bytes())
    a=R.P.Arithmetic(ledger=False);model=R.instantiate(a,meta,R.config('uniform',0))
    t=time.perf_counter(); loc={g:v for v,g in enumerate(model.locations)}
    nb={(v,j):model.target(v,j) for v in range(8) for j in range(3)}
    idx_time=time.perf_counter()-t
    t=time.perf_counter()
    s=R.prepare(model,R.config('uniform',0));s,_,_=R.run_one(model,s,True)
    states=[];flows=[]
    for _ in range(6):
        states.append(fields(s));s,inc,_=R.run_one(model,s,True);flows.append(inc)
    cache_build=time.perf_counter()-t
    footprints={'phase_fields_and_flows_deep_python_bytes':deep_size((states,flows)),
                'material_and_adjacency_indices_deep_python_bytes':deep_size((loc,nb))}
    with tempfile.TemporaryDirectory() as scratch:
        f=Path(scratch)/'CASES.jsonl'
        t=time.perf_counter();portable(f);construct=time.perf_counter()-t
        data=f.read_bytes()
        assert data==(acceptance/'CASES.jsonl').read_bytes()
        with_g=hashlib.sha256(data).hexdigest()
        t=time.perf_counter();g=Path(scratch)/'output.jsonl';g.write_bytes(data);write=time.perf_counter()-t
    audits=json.loads(checks.read_bytes()) if checks else measured_acceptance(acceptance,archive)
    assert audits['verify_archive']['result']['transitions_checked']==36864
    # Source setup is already in each run's wall_seconds. Cache reconstruction
    # below is an auxiliary measurement; it is not charged twice to the pipeline.
    common=bind_time+construct+audits['verify_archive']['wall_seconds']+audits['mutations']['wall_seconds']
    return dict(schema='R11_original_full_256_vs_positive_patch_v1',reference=records[0],repair=records[1],
                preparation=dict(original_manifest_with_all_41_bound_members_verify_seconds=bind_time,
                    auxiliary_rebuild_six_phase_seconds=cache_build,auxiliary_build_indices_seconds=idx_time,
                    original_addresses=5832,**footprints),
                certification=audits,output=dict(case_rows=144,bytes=len(data),sha256=with_g,
                    portable_ledger_construction_including_serialization_and_write_seconds=construct,
                    fresh_buffered_write_only_seconds=write),
                observed_max_pending_histogram_by_case=obs_hist,
                contract_total_wall_seconds_including_full_comparisons_certificate_and_output={
                    'reference':records[0]['wall_seconds']+common,
                    'repair':records[1]['wall_seconds']+common},
                scope='Separate processes and machine-dependent durations. Shared verification and output costs included once per compared route. Source import and phase building included in each source run. Buffered output does not measure fsync.')


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',required=True,type=Path);ap.add_argument('--stats',required=True,type=Path)
    ap.add_argument('--local',action='store_true')
    ap.add_argument('--combine',nargs=2,type=Path,metavar=('REFERENCE','REPAIR'))
    ap.add_argument('--acceptance',type=Path)
    ap.add_argument('--acceptance-measurements',type=Path)
    ap.add_argument('--source-zip',type=Path)
    args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(1800,1800))
    resource.setrlimit(resource.RLIMIT_AS,(1<<30,1<<30))
    if args.combine:
        if not args.acceptance or not (args.acceptance_measurements or args.source_zip):
            ap.error('--combine needs --acceptance and either --source-zip or --acceptance-measurements')
        result=summary(args.source,args.combine,args.acceptance,args.acceptance_measurements,args.source_zip)
    else:
        result=main(args.source,args.local)
    args.stats.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
