#!/usr/bin/env python3
"""Actual pinned BRC candidate propagation; Octave owns truth and fitting.

This is a representation experiment, not an inferred native physical kernel.
Coordinates are six signed integers; the other six history entries and rational
remainders are separately typed decorations. A 12-dimensional affine packet is
NOT called a 12-dimensional or six-position/velocity native space.
"""
import argparse, csv, hashlib, json, sys, time, uuid
from fractions import Fraction as Q
from pathlib import Path

if not __debug__: raise SystemExit("Scientific certificates require Python assertions; do not use -O")
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'pinned_source'
sys.path.insert(0,str(SOURCE))
from enterprise_math.brc_transport import Affine, EffectHistogram

def nearest(q): return (2*q.numerator+q.denominator)//(2*q.denominator)
def writecsv(path,rows):
    with path.open('w',newline='') as f: csv.writer(f).writerows(rows)
def loadcsv(path):
    with path.open() as f:return [[float(x) for x in row] for row in csv.reader(f)]

def execute(spec,case,ni,den,tr,out,maxsteps,timebudget,bitcap,dest):
    began=time.perf_counter(); v=case['variants'][ni]; D=spec['coefficient_denominator']
    nums=[[int(x) for x in row] for row in v['theta_numerators']]
    A=tuple(tuple(Q(n,D) for n in row) for row in nums)
    A+=tuple(tuple(Q(int(i==j)) for j in range(12)) for i in range(6))
    packet=EffectHistogram.from_terms(12,[(Q(1),Affine(A,(Q(0),)*12),1)])
    wh=packet.forget_effects()
    assert wh.total_mass==wh.dominant_mass==wh.count==wh.dominant_degeneracy==1
    truth=loadcsv(out/f"{case['name']}_truth_{tr:02d}.csv")
    N=min(spec['steps'],maxsteps)
    initial=[[nearest(Q(str(x))*den) for x in row[1:7]] for row in truth[:2]]
    state=tuple(Q(x) for x in initial[1]+initial[0]); drop=state
    independent_num=[int(x) for x in state]; independent_den=1
    rows=[[truth[k][0]]+[x/den for x in initial[k]] for k in (0,1)]
    coarse=[row[:] for row in rows]; dropped=[row[:] for row in rows]
    path_rows=[]; certificate_checks=0; maxbits=1; discarded_squared=Q(0)
    max_component_increment=0; max_microsteps=0; bit_rows=[]
    old_z=initial[1]
    retained_seconds=0.;discard_seconds=0.;integer_seconds=0.
    stem=f"{case['name']}_n{ni}_d{den}_{tr:02d}"
    def fail_cap(reason):
        writecsv(dest/f'{stem}_PARTIAL_brc.csv',rows)
        writecsv(dest/f'{stem}_PARTIAL_drop.csv',dropped)
        writecsv(dest/f'{stem}_PARTIAL_path_rle.csv',path_rows)
        raise RuntimeError(reason)
    for k in range(1,N):
        if time.perf_counter()-began>timebudget:fail_cap('PROSPECTIVE_RUNTIME_CAP')
        tick=time.perf_counter()
        result=packet.evaluate(state);assert len(result)==1;state=next(iter(result))
        retained_seconds+=time.perf_counter()-tick
        tick=time.perf_counter()
        # Independent common-denominator integer recurrence, no Affine calls.
        newnum=[sum(nums[i][j]*independent_num[j] for j in range(12)) for i in range(6)]
        newnum += [x*D for x in independent_num[:6]]
        independent_num=newnum;independent_den*=D
        for a,b in zip(state,independent_num):
            assert a.numerator*independent_den==b*a.denominator
            certificate_checks+=1
        integer_seconds+=time.perf_counter()-tick
        z=[nearest(x) for x in state[:6]];r=[x-y for x,y in zip(state[:6],z)]
        assert all(-Q(1,2)<=x<Q(1,2) for x in r)
        assert all(Q(a)+b==c for a,b,c in zip(z,r,state[:6]))
        certificate_checks+=12
        # Declared canonical composite path, ordered E1,...,E6.
        steps=[a-b for a,b in zip(z,old_z)]
        assert [a+b for a,b in zip(old_z,steps)]==z
        path_rows.append([k+1]+steps)
        max_component_increment=max(max_component_increment,max(map(abs,steps)))
        max_microsteps=max(max_microsteps,sum(map(abs,steps)))
        old_z=z
        tick=time.perf_counter()
        dropout=next(iter(packet.evaluate(drop)))
        dz=tuple(Q(nearest(x)) for x in dropout)
        discarded_squared+=sum((a-b)**2 for a,b in zip(dropout[:6],dz[:6]))
        drop=dz
        discard_seconds+=time.perf_counter()-tick
        mb=max(max(abs(x.numerator).bit_length(),x.denominator.bit_length()) for x in state)
        maxbits=max(maxbits,mb)
        if mb>bitcap:fail_cap('PROSPECTIVE_BIT_LENGTH_CAP')
        tm=truth[k+1][0]
        rows.append([tm]+[float(x)/den for x in state[:6]])
        coarse.append([tm]+[x/den for x in z])
        dropped.append([tm]+[float(x)/den for x in drop[:6]])
        if k in (1,9,39,99,199,N-1):bit_rows.append([k+1,mb,time.perf_counter()-began])
    stem=f"{case['name']}_n{ni}_d{den}_{tr:02d}"
    tick=time.perf_counter()
    writecsv(dest/f'{stem}_brc.csv',rows);writecsv(dest/f'{stem}_cell.csv',coarse)
    writecsv(dest/f'{stem}_drop.csv',dropped);writecsv(dest/f'{stem}_path_rle.csv',path_rows)
    writecsv(dest/f'{stem}_resource.csv',bit_rows)
    return dict(stem=stem,case=case['name'],noise_index=ni,delta_denominator=den,trajectory=tr,
      horizon_steps=N,role='parameter_ood' if tr==13 else 'unseen_initial_state',
      exact_integer_comparator_checks=certificate_checks,max_fraction_bits=maxbits,
      runtime_seconds=time.perf_counter()-began,retained_brc_seconds=retained_seconds,discard_brc_seconds=discard_seconds,integer_validation_seconds=integer_seconds,artifact_io_seconds=time.perf_counter()-tick,max_component_increment=max_component_increment,
      max_primitive_unit_steps_per_sample=max_microsteps,
      sum_squared_local_rounding_errors=float(discarded_squared)/(den*den),
      semantics='DETERMINISTIC_BRC_AFFINE_EFFECT_CANDIDATE_WITH_X6_CHART_AND_TYPED_MEMORY',
      physical_residual_attribution='NOT_ESTABLISHED',parameter_count=72)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'output')
    ap.add_argument('--smoke',action='store_true');ap.add_argument('--verify-only',action='store_true');ap.add_argument('--time-cap',type=float,default=1800)
    args=ap.parse_args();out=args.out
    if args.verify_only:
        r=json.loads((out/'brc_results.json').read_text())
        if r['script_sha256']!=hashlib.sha256(Path(__file__).read_bytes()).hexdigest():raise RuntimeError('RUNNER_SOURCE_CHANGED')
        for key in ('scientific_inputs_sha256','output_sha256'):
            for name,sha in r[key].items():
                if hashlib.sha256((out/name).read_bytes()).hexdigest()!=sha:raise RuntimeError('ARTIFACT_HASH_MISMATCH:'+name)
        print('INPUT_OUTPUT_MANIFEST_VERIFIED');return
    run_id='RUN-'+uuid.uuid4().hex
    dest=out/'smoke' if args.smoke else out
    dest.mkdir(exist_ok=True)
    status_path=dest/('brc_smoke.json' if args.smoke else 'brc_results.json')
    status_path.write_text(json.dumps({'status':'RUNNING_OR_FAILED','run_id':run_id})+'\n')
    spec=json.loads((out/'experiment.json').read_text());records=[];errors=[]
    manifest=json.loads((SOURCE/'SOURCE_MANIFEST.json').read_text())
    for name,record in manifest.items():
        assert hashlib.sha256((SOURCE/'enterprise_math'/name).read_bytes()).hexdigest()==record['sha256']
    dest=out/'smoke' if args.smoke else out
    dest.mkdir(exist_ok=True)
    scientific_inputs_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [out/'experiment.json',*sorted(out.glob('*_truth_*.csv'))]}

    if args.smoke: schedule=[(spec['cases'][0],0,256,9,40)]
    else:
        # Fixed prospective exact budget: 23 trajectories, <=9200 transitions.
        # 2 of the 4 external holdout states get exact rational certificates.
        schedule=[(c,0,d,tr,400) for c in spec['cases'] for d in (64,256,1024) for tr in (9,10)]
        schedule += [(spec['cases'][1],1,256,tr,400) for tr in (9,10)]
        schedule += [(c,0,256,13,400) for c in spec['cases']]
    start=time.perf_counter()
    for c,ni,d,tr,n in schedule:
        try:
            left=args.time_cap-(time.perf_counter()-start)
            if left<=0:raise RuntimeError('PROSPECTIVE_TOTAL_RUNTIME_CAP')
            result=execute(spec,c,ni,d,tr,out,n,min(180,left),12000,dest)
            records.append(result);print(json.dumps(result),flush=True)
        except Exception as exc:
            errors.append(dict(case=c['name'],noise_index=ni,delta_denominator=d,trajectory=tr,error=str(exc)))
            break
    status='PASS' if not errors else ('BOUNDED_PARTIAL' if all('PROSPECTIVE_' in e['error'] and 'CAP' in e['error'] for e in errors) else 'FAIL')
    report=dict(status=status,smoke=args.smoke,
      source_pin=spec['source_pin'],run_id=run_id,imported_module=str(Path(sys.modules['enterprise_math.brc_transport'].__file__).resolve()),schedule_count=len(schedule),completed=len(records),
      caps=dict(total_runtime_seconds=args.time_cap,per_trajectory_seconds=180,max_fraction_bits=12000),
      records=records,errors=errors,scientific_inputs_sha256=scientific_inputs_sha256,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),runtime_seconds=time.perf_counter()-start)
    report['output_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for rec in records for p in dest.glob(rec['stem']+'_*.csv')}
    report['input_artifacts']=[{'name':name,'sha256':sha} for name,sha in scientific_inputs_sha256.items()]
    report['output_artifacts']=[{'name':name,'sha256':sha} for name,sha in report['output_sha256'].items()]
    report['caps']['scope']='Cooperative soft walltime caps; retained-state fraction bit cap, not peak intermediates'
    target=dest/('brc_smoke.json' if args.smoke else 'brc_results.json')
    temporary=target.with_suffix('.json.tmp');temporary.write_text(json.dumps(report,indent=2)+'\n');temporary.replace(target)
    print(report['status'])
    if errors:sys.exit(2)
if __name__=='__main__':main()
