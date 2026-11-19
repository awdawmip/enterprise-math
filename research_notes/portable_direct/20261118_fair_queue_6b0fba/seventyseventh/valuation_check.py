"""Independent 18-representative RP15 direction audit. No frozen inputs are reproduced."""
from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import gc
import inspect
import sys
import time
import textwrap
import gzip
import hashlib
import json

WEIGHTS = tuple(2 if i == 2 else 6 if i == 14 else 1
                for i in range(21) if i not in (3, 15, 17))
PINS = {
    "rp15_fused/engine.py": "606aa6d3c404f10b131af4c8c4f3faa5cbabf52b0651b452ead8f42887266836",
    "rp15_fused/evidence/MICRO_REAL_FIELDS.json.gz": "38b3576349196874a18fc408dd06d411ea4aa003ce5606eb6457e094562b927f",
}


def valuation(n):
    return (n & -n).bit_length() - 1


@lru_cache(None)
def interval(bits, val, shift):
    if bits <= shift:
        return (F(0), F(0))
    if val >= shift:
        return (F(1), F(1))
    radix = 1 << shift
    small = 1 << val
    low = 1 << (bits-1)
    high = (1 << bits) - radix
    return F(low, low+radix-small), F(high, high+small)


def classify(rows):
    minimum = min(e for _,e in rows)
    spectrum = Counter()
    nonzero = 0
    for row,e in rows:
        assert len(row) == len(WEIGHTS)
        width = max(abs(i).bit_length() for i in row)
        for a,w in zip(row, WEIGHTS):
            if a:
                nonzero += 1
                bits = abs(a).bit_length()
                key = (width,bits,valuation(abs(a)))
                spectrum[key] += (w*a*a) << (2*(e-minimum))
    return spectrum, minimum, nonzero


def intervals(spectrum,cap):
    bands = Counter()
    for (width,bits,val),energy in spectrum.items():
        bands[interval(bits,val,max(0,width-cap))] += energy
    return bands


def relax(bands):
    # The derivative (divided by two) is continuous, monotone and piecewise linear.
    # On an active branch the term is energy*(1-s*rho)^2.
    events = {}
    slope = intercept = F(0)
    for (lo,hi),w in bands.items():
        if hi == 0:
            continue
        slope += w*hi*hi
        intercept -= w*hi
        for rho,sign in [(hi,-1),(lo,1)]:
            if rho:
                t = 1/rho
                ds,di = events.get(t,(0,0))
                events[t] = ds+sign*w*rho*rho, di-sign*w*rho
    if not events:
        return sum(bands.values()), F(0)
    optimum = None
    for t,(ds,di) in sorted(events.items()):
        if slope*t+intercept >= 0:
            optimum = -intercept/slope if slope else t
            break
        slope += ds
        intercept += di
    if optimum is None:
        assert slope
        optimum = -intercept/slope
    residual = sum(w*max(F(0),1-optimum*hi,optimum*lo-1)**2
                   for (lo,hi),w in bands.items())
    return residual,optimum


def exact_angle(rows,cap):
    minimum = min(e for _,e in rows)
    aa=cc=jj=0
    for row,e in rows:
        shift = max(0,max(abs(v).bit_length() for v in row)-cap)
        weight_shift = 2*(e-minimum)
        for value,weight in zip(row,WEIGHTS):
            n=abs(value)
            y=(n>>shift)<<shift
            aa+=weight*n*n<<weight_shift
            cc+=weight*y*y<<weight_shift
            jj+=weight*n*y<<weight_shift
    return F(aa*cc-jj*jj,aa*cc)


def small_checks():
    signatures=Counter()
    for n in range(1,1024):
        for shift in range(12):
            key=(n.bit_length(),valuation(n),shift)
            r=F((n>>shift)<<shift,n)
            signatures[key,r]+=1
    endpoints={}
    for key,r in signatures:
        lo,hi=endpoints.get(key,(r,r))
        endpoints[key]=min(lo,r),max(hi,r)
    assert all(interval(*key)==got for key,got in endpoints.items())
    checked = 0
    for a,b,c in product(range(1,16), repeat=3):
        rows=[([a,-b,c]+[0]*15,0)]
        spec,_,_=classify(rows)
        for cap in (1,2,3):
            bands=intervals(spec,cap)
            cost,s=relax(bands)
            # Existence of vectors attaining the relaxed minimum, by optimal clamping.
            ratios=[min(hi,max(lo,F(1)/s)) for lo,hi in bands]
            weights=list(bands.values())
            aa=sum(weights)
            cc=sum(w*r*r for w,r in zip(weights,ratios))
            jj=sum(w*r for w,r in zip(weights,ratios))
            assert cost == aa-jj*jj/cc
            assert bands.get((F(0),F(0)),0) <= cost <= aa*exact_angle(rows,cap)
            checked += 1
    first=[([17,31]+[0]*16,0)]
    second=[([25,25]+[0]*16,0)]
    assert classify(first)[0]==classify(second)[0]=={(5,5,0):1250}
    unequal=exact_angle(first,4)
    assert exact_angle(second,4)==0<F(1,10000)<unequal==F(49,361250)
    return {"endpoint_classes":len(endpoints),"signed_fields_and_caps":checked,
            "same_spectrum_angles":[str(unequal),"0"]}


def frozen(root):
    for name,sha in PINS.items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==sha
    records=json.loads(gzip.decompress((root/list(PINS)[1]).read_bytes()))
    assert len(records)==98
    counts=Counter()
    peaks=Counter()
    for packet in records:
        cert=packet["certificate"]
        attempts=cert.get("candidates",[])
        counts["fields"]+=1
        if not attempts:
            counts["terminal_fields"]+=1
            continue
        rows=list(packet["raw"].values())
        spectrum,minimum,nz=classify(rows)
        A=sum(spectrum.values())
        assert F(A)*F(2)**(2*minimum)==F(cert["A"])
        largest=max(width for width,_,_ in spectrum)
        if largest>attempts[0]["cap"]:
            counts["fields_requiring_histogram"]+=1
            profiles=[]
            for row,e in rows:
                numbers=list(map(abs,row))
                width=max(numbers).bit_length()
                counts["drop_updates_with_positive_gap"]+=sum(v!=0 and v.bit_length()<width for v in numbers)
                profiles.append((None,None,numbers,width,2*(e-minimum)))
            gaps=drop_hist(profiles,WEIGHTS)
            counts["nonempty_positive_gap_bins"]+=len(gaps)
            peaks["positive_gap_bins"]=max(peaks["positive_gap_bins"],len(gaps))
            counts["preprocessed_rows"]+=len(rows)
            counts["preprocessed_18_coordinates"]+=18*len(rows)
            counts["preprocessed_nonzero_coordinates"]+=nz
            peaks["field_spectrum_bins"]=max(peaks["field_spectrum_bins"],len(spectrum))
        for at in attempts:
            cap=at["cap"]
            real=F(at["gamma2"])
            bound2=F(cert["allowance"])**2
            assert real==exact_angle(rows,cap) and at["passed"]==(real<=bound2)
            counts["attempts"]+=1
            counts["truly_failing"]+=int(not at["passed"])
            if cap>=largest:
                counts["unchanged_shortcuts"]+=1
                continue
            counts["raw_baseline_row_visits"]+=len(rows)
            bands=intervals(spectrum,cap)
            counts["spectrum_bins_charged"]+=len(spectrum)
            peaks["cap_interval_groups"]=max(peaks["cap_interval_groups"],len(bands))
            dropped=bands.get((F(0),F(0)),0)
            cost,s=relax(bands)
            assert dropped<=cost<=real*A
            counts["cost_strictly_above_dropped"]+=int(cost>dropped)
            counts["matches_true_gamma"]+=int(cost==real*A)
            if dropped>A*bound2:
                counts["drop_only_rejects"]+=1
                counts["drop_only_saved_rows"]+=len(rows)
            if cost>A*bound2:
                counts["full_band_rejects"]+=1
                counts["full_band_saved_rows"]+=len(rows)
                assert not at["passed"]
            else:
                counts["full_band_surviving_rows"]+=len(rows)
    return {"file_sha256":PINS,"grouped_data":dict(sorted(counts.items())),
            "peaks":dict(peaks)}


def drop_hist(raw_rows,weights):
    # Only positive gaps can drop at legal K. Exact source values already have abs/width/offset.
    buckets = Counter()
    for _, _, numbers, width, offset in raw_rows:
        for n,w in zip(numbers,weights):
            if n:
                gap=width-n.bit_length()
                if gap:
                    buckets[gap] += (w*n*n)<<offset
    return buckets


def bind_runtime(cls):
    body = textwrap.dedent(inspect.getsource(cls.finish_budget))
    needle = '    attempts=[];selected=None'
    assert body.count(needle)==1
    setup = '''
    certificates={}
    if largest>self.caps[0]:
        hist=drop_hist(rows,weights)
        running=0
        sorted_gaps=sorted(hist.items(), reverse=True)
        ix=0
        for cap in sorted(set(self.caps),reverse=True):
            while ix<len(sorted_gaps) and sorted_gaps[ix][0]>=cap:
                running+=sorted_gaps[ix][1]
                ix+=1
            if running*bound2.denominator>ai*bound2.numerator:
                certificates[cap]=running
    '''
    body=body.replace(needle,textwrap.indent(textwrap.dedent(setup).strip(),'    ')+'\n'+needle)
    needle='        if largest<=K:'
    assert body.count(needle)==1
    body=body.replace(needle,'''        if K in certificates:
            attempts.append(dict(cap=K,passed=False,missing_energy=(certificates[K],ai)))
            self.performance['saved_rows']+=len(rows)
            continue
'''+needle)
    namespace=dict(cls.finish_budget.__globals__,drop_hist=drop_hist)
    exec(body,namespace)
    return type('DropBudget',(cls,),{'finish_budget':namespace['finish_budget']})


def compare_records(ref,new,visits,allow=None):
    if isinstance(new,dict):
        if 'missing_energy' in new:
            assert set(new)=={'cap','passed','missing_energy'}
            assert ref['cap']==new['cap'] and not ref['passed'] and not new['passed']
            num,den=new['missing_energy']
            assert allow*allow < F(num,den) <= ref['gamma2']
            visits['confirmed_rejects']+=1
            visits['max_certificate_bits']=max(visits['max_certificate_bits'],num.bit_length(),den.bit_length())
            return
        assert ref.keys()==new.keys()
        allow=new.get('allowance',allow)
        for name,value in new.items():
            compare_records(ref[name],value,visits,allow)
    elif isinstance(new,(list,tuple)):
        assert len(ref)==len(new)
        for f,g in zip(ref,new):
            compare_records(f,g,visits,allow)
    else:
        assert ref==new


def native(root,cost_path=None,full=False):
    for name in PINS:
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==PINS[name]
    sys.path.insert(0,str(root))
    from rp15_fused import run,engine,micro
    baseline=engine.FusedBudget
    cheaper=bind_runtime(baseline)
    start=time.perf_counter_ns()
    cb,rep,_=run.build()
    timings={'bank_setup_ns':time.perf_counter_ns()-start}
    assert tuple(rep.weights)==WEIGHTS
    cases=[tuple(case) for case in run.PLAN['benchmark_cases']]
    records=run.load(root/'rp15_fused/evidence/MICRO_REAL_FIELDS.json.gz')
    streams=[]
    post=run.DemandDriver(run.DemandFactory(16)).classical_postprocess
    for i,case in enumerate(cases):
        for j in range(2):
            instance=micro.Capture(run.make_program(case,cb),cb,rep)
            seed=run.PLAN['seed_base']+10000*i+j
            instance.sample(run.Tape(seed),post,1)
            streams.extend((case,seed,*p) for p in instance.packets)
    assert len(streams)==len(records)==98
    for (case,seed,h,rows,left,A,expected),rec in zip(streams,records):
        assert list(case)==rec['case'] and seed==rec['seed'] and list(h)==rec['h']
        assert left==rec['remaining'] and A==F(rec['A'])
        assert {str(w):[list(x.n),x.e] for w,x in rows.items()}==rec['raw']
        assert run.encode(expected[2])==rec['certificate']
    visits=Counter()
    timings['field_ns']={'baseline':[],'drop':[]}
    for trial in range(5):
        order=(baseline,cheaper) if trial%2==0 else (cheaper,baseline)
        for method in order:
            hosts={case:method(run.make_program(case,cb),cb,rep) for case in cases}
            gc.collect()
            start=time.perf_counter_ns()
            results=[hosts[case].finish_budget(h,r,left,A) for case,_,h,r,left,A,_ in streams]
            elapsed=time.perf_counter_ns()-start
            timings['field_ns']['baseline' if method==baseline else 'drop'].append(elapsed)
            for v,packet in zip(results,streams):
                compare_records(packet[-1],v,visits if method==cheaper and trial==0 else Counter())
    assert visits['confirmed_rejects']==259
    solves=[]
    attempts={}
    timings['factor_ns']=[]
    for i,case in enumerate(cases):
        for j,seed in enumerate([run.PLAN['seed_base']+10000*i,20261119110800+i]):
            order=(baseline,cheaper) if (i+j)%2==0 else (cheaper,baseline)
            results={}
            timers={}
            perf={}
            for method in order:
                try:
                    run.FusedBudget=method
                    gc.collect()
                    start=time.perf_counter_ns()
                    results[method],perf[method]=run.solve(case,'fused',cb,rep,seed)
                    timers['baseline' if method==baseline else 'drop']=time.perf_counter_ns()-start
                finally:
                    run.FusedBudget=baseline
            cmpcounts=Counter()
            compare_records(results[baseline],results[cheaper],cmpcounts)
            assert results[baseline]['success']
            if j==0:
                path=root/f'rp15_fused/evidence/SOLVES_{case[0]}_r0_fused.json.gz'
                assert run.encode(results[baseline])==run.load(path)[0]['result']
            solves.append(dict(N=case[0],seed=seed,outputs=len(results[baseline]['outputs']),
                               requests=len(results[baseline]['rng_requests']) if not isinstance(results[baseline]['rng_requests'],int) else results[baseline]['rng_requests'],
                               full_rows=perf[baseline].get('candidate_row_visits',0),
                               saved_rows=perf[cheaper].get('saved_rows',0),**cmpcounts))
            timings['factor_ns'].append(dict(N=case[0],seed=seed,**timers))
    if full:
        for N,a,t,policy,eps in run.PLAN['diagnostics']:
            case=(N,a,t)
            hosts=[model(run.make_program(case,cb),cb,rep,epsilon=F(eps),policy=policy) for model in (baseline,cheaper)]
            initial=hosts[0]
            leaves=[F()]*(1<<t)
            stats=Counter()
            data=iter(run.load(root/f'rp15_fused/evidence/REPLAY_BRANCHES_{N}.json.gz'))
            def walk(h,raw,left,prob):
                if len(h)==t:
                    leaves[sum(b<<i for i,b in enumerate(h))]=prob
                    stats['reachable_leaves']+=1
                    return
                arms,masses,total=hosts[0].prepare(h,raw)
                assert (arms,masses,total)==hosts[1].prepare(h,raw)
                for bit,mass in enumerate(masses):
                    if mass==0: continue
                    nh=h+(bit,)
                    out=[host.finish_budget(nh,arms[bit],left,mass) for host in hosts]
                    compare_records(*out,stats)
                    field,bal,cert=out[0]
                    node=next(data)
                    pr=prob*mass/total
                    assert node['h']==list(nh) and F(node['probability'])==pr and run.encode(cert)==node['certificate']
                    stats['routes']+=1
                    stats['rows_returned']+=len(field)
                    walk(nh,field,bal,pr)
            walk((),{1:initial.one},initial.ticks,F(1))
            assert next(data,None) is None
            assert run.encode(leaves)==run.load(root/f'rp15_fused/evidence/REPLAY_LAW_{N}.json.gz')
            assert hosts[0].counts==hosts[1].counts and hosts[0].stats==hosts[1].stats
            attempts[str(N)]=dict(stats,full_rows=hosts[0].performance['candidate_row_visits'],saved_rows=hosts[1].performance['saved_rows'])
    if cost_path:
        import platform
        timings['python']=platform.python_version()
        timings['cpu']=next((s.split(':',1)[1].strip() for s in Path('/proc/cpuinfo').read_text().splitlines() if s.startswith('model name')),'unknown')
        Path(cost_path).write_text(json.dumps(timings,sort_keys=True,indent=2)+'\n')
    return dict(prepared_fields=len(records),compared_trials=5,field_audit=dict(visits),solves=solves,full_laws=attempts)


if __name__=="__main__":
    p=ArgumentParser()
    p.add_argument("--source",type=Path)
    p.add_argument("--native",action="store_true")
    p.add_argument("--full-laws",action="store_true")
    p.add_argument("--cost",type=Path)
    args=p.parse_args()
    out={"portable":small_checks()}
    if args.source:
        out["source"]=frozen(args.source)
    if args.native:
        out["runtime"]=native(args.source,args.cost,args.full_laws)
    print(json.dumps(out,sort_keys=True,indent=2))
