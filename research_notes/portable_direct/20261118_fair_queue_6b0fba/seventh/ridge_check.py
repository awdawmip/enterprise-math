"""Exact projection test. Optional RP15 replay with externally supplied RP14_Run.
No source, raw field or per-seed output from the supplied archive is distributed.
"""
import argparse
from collections import Counter
from fractions import Fraction as F
import gc
import hashlib
import inspect
from itertools import product
import json
from math import isqrt
from pathlib import Path
import platform
import statistics
import sys
import textwrap
import time

PIN = '606aa6d3c404f10b131af4c8c4f3faa5cbabf52b0651b452ead8f42887266836'
CASES = [(143,2,16),(323,2,18),(391,2,18)]
NEW_SEEDS = [202611180701,202611180702,202611180703]


def deficit(a,c,j):
    return F(a) - (F(j*j,c) if c else 0)


def public_checks():
    count = 0
    for vals in product(range(-2,3),repeat=6):
        x,u,v,y,b,d = vals
        A,C,J = x*x+u*u+v*v,y*y+b*b+d*d,x*y+u*b+v*d
        if not A or not C:
            continue
        past = F(0)
        for a,c,j in [(x*x,y*y,x*y),(x*x+u*u,y*y+b*b,x*y+u*b),(A,C,J)]:
            cur = deficit(a,c,j)
            assert past <= cur <= deficit(A,C,J)
            past=cur
        count+=1
    # Opposing signs and a zero-pair prefix, attained and unattained suprema.
    for j0 in (-3, 3):
        source = [F(j0), F(4)]
        candidate = [F(1), F(4,j0)]
        assert sum(x*y for x,y in zip(source,candidate))**2 / sum(y*y for y in candidate) == 25
    assert deficit(1,0,0) == 1
    assert F(16,5)<4 and F(1600,401)<4
    x = (135,136)
    angles=[]
    for K in (4,6):
        shift=max(v.bit_length() for v in x)-K
        y=tuple((v >> shift)<<shift for v in x)
        A,C,J=sum(v*v for v in x),sum(v*v for v in y),sum(v*w for v,w in zip(x,y))
        angles.append(F(A*C-J*J,A*C))
    assert angles[0] < F(1,10000) < angles[1]
    # A rational square threshold with an actually attained tie at gamma=3/5.
    assert deficit(25,1,4)==9 and F(9,25)==F(3,5)**2
    return {'signed_vectors':count,'exact_threshold_tie':True}


def early_class(host, path):
    """Insert only prefix bookkeeping into the *verified external* selector."""
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PIN:
        raise RuntimeError("host engine hash mismatch")
    original, start = inspect.getsourcelines(host.FusedBudget.finish_budget)
    extra = {
        59:"""
        prefix_mass = []
        if len(rows)>1 and largest>self.caps[0]:
            summed = 0
            for _, source, _, _, shift in rows:
                summed += self.replica.quad(source.n) << shift
                prefix_mass.append(summed)
            assert summed == ai
            self.performance['extra_source_rows'] += len(rows)
        cut_n, cut_d = ai * bound2.numerator, bound2.denominator
""",
        68:"""
                partial_failure = None
""",
        82:"""
                    used = len(pending)
                    if used < len(rows):
                        a0 = prefix_mass[used-1]
                        loss_n = a0*cn - jn*jn
                        self.performance['prefix_comparisons'] += 1
                        if loss_n*cut_d > cut_n*cn:
                            partial_failure = dict(cap=K, passed=False,
                                 early_prefix=(used,len(rows),a0,cn,jn,ai))
                            self.performance['skipped_rows'] += len(rows)-used
                            self.performance['early_candidates'] += 1
                            break
                if partial_failure is not None:
                    attempts.append(partial_failure)
                    continue
"""}
    chunks=[]
    for line_no,line in enumerate(original,start):
        chunks.append(line)
        if line_no in extra:
            chunks.append(extra[line_no].lstrip('\n'))
    space = host.__dict__.copy()
    exec(compile(textwrap.dedent(''.join(chunks)), '<verified RP15 plus prefix test>', 'exec'),space)
    return type('PrefixBudget',(host.FusedBudget,),{'finish_budget':space['finish_budget']})


def compare(old,new,counts,allow=None):
    """Independent audit using the complete output, outside timed production."""
    if isinstance(new,dict):
        if 'early_prefix' in new:
            assert set(new)=={'cap','passed','early_prefix'}
            assert old['cap']==new['cap'] and not old['passed'] and not new['passed']
            k,n,a,c,j,full = new['early_prefix']
            assert 0 < k < n and 0 < c and 0 < j and 0 < a <= full
            lower=deficit(a,c,j)/full
            assert allow**2 < lower <= old['gamma2']
            counts['prefix_audits']+=1
            counts['max_observed_aggregate_bits']=max(counts['max_observed_aggregate_bits'],max(v.bit_length() for v in (a,c,j,full)))
            return
        assert old.keys()==new.keys()
        allow=old.get('allowance',allow)
        for k in new:
            compare(old[k],new[k],counts,allow)
    elif isinstance(new,(tuple,list)):
        assert len(old)==len(new)
        for x,y in zip(old,new):
            compare(x,y,counts,allow)
    else:
        assert old==new


def replay(root, full):
    path=root/'rp15_fused'/'engine.py'
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PIN:
        raise ValueError("unexpected archive engine")
    sys.path.insert(0,str(root))
    from rp15_fused import run, engine, micro
    from rp11_closed.engine import canonical, toward, pow2
    Alt=early_class(engine,path)
    Baseline=engine.FusedBudget
    timer=time.perf_counter
    began=timer()
    cb,rep,_=run.build()
    setup=timer()-began
    audit=Counter()
    result=dict(machine=platform.machine(),python=platform.python_version(),
                cpu=next((l.split(':')[1].strip() for l in Path('/proc/cpuinfo').read_text().splitlines() if l.startswith('model name')),'unknown'),
                setup_seconds=setup)
    def build(case,cls,**kwargs):
        return cls(run.make_program(tuple(case),cb),cb,rep,**kwargs)
    def pair(case,**kw):
        return [build(case,cls,**kw) for cls in (Baseline,Alt)]
    # Re-generate the 98 fields to preserve live dictionary order. Archived
    # JSON object keys are sorted, so parsing its raw map would change order.
    raw_packets=[]
    post=run.DemandDriver(run.DemandFactory(16)).classical_postprocess
    for i,case in enumerate(CASES):
        for j in (0,1):
            E=micro.Capture(run.make_program(case,cb),cb,rep)
            seed=run.PLAN['seed_base']+i*10000+j
            E.sample(run.Tape(seed),post,1)
            raw_packets.extend((case,seed,*p) for p in E.packets)
    stored=run.load(root/'rp15_fused'/'evidence'/'MICRO_REAL_FIELDS.json.gz')
    assert len(stored)==len(raw_packets)==98
    for old,(case,seed,h,raw,left,A,expect) in zip(stored,raw_packets):
        assert old['case']==list(case) and old['seed']==seed and old['h']==list(h)
        assert old['remaining']==left and F(old['A'])==A
        assert old['raw']=={str(w):[list(row.n),row.e] for w,row in raw.items()}
        assert old['certificate']==run.encode(expect[2])
    micro_ns=[[],[]]
    perf=[]
    for repeat in range(5):
        for idx in ((0,1) if repeat%2==0 else (1,0)):
            eng={case:build(case,(Baseline,Alt)[idx]) for case in CASES}
            gc.collect()
            begin=time.perf_counter_ns()
            produced=[eng[c].finish_budget(h,raw,left,A) for c,_,h,raw,left,A,_ in raw_packets]
            micro_ns[idx].append(time.perf_counter_ns()-begin)
            for (_,_,_,_,_,_,exp),got in zip(raw_packets,produced):
                compare(exp,got,audit)
            if repeat==0 and idx==1:
                for packet,output in zip(raw_packets,produced):
                    rowlist=list(packet[3].values())
                    scale=pow2(2*min(v.e for v in rowlist))
                    for attempt in output[2].get('candidates',[]):
                        if 'early_prefix' not in attempt:
                            continue
                        k,n,a,c,j,total=attempt['early_prefix']
                        source=rowlist[:k]
                        quantized=[toward(v,attempt['cap']) for v in source]
                        assert sum(map(rep.norm,source))==a*scale
                        assert sum(map(rep.norm,quantized))==c*scale
                        assert sum(rep.inner(v,w) for v,w in zip(source,quantized))==j*scale
                        assert packet[5]==total*scale
                        audit['independent_prefix_reconstructions']+=1
            if repeat==0:
                perf.append(dict(sum((e.performance for e in eng.values()),Counter())))
    result['micro']={'fields':98,'candidate_tests':sum(len(p[-1][2].get('candidates',[])) for p in raw_packets),
                     'baseline_perf':perf[0],'early_perf':perf[1],'ns_by_method':micro_ns}
    # Separate auxiliary scan cost, without the host's core construction.
    prep_ns=[]; max_prefix_rows=max_prefix_bytes=0
    for _ in range(5):
        begin=time.perf_counter_ns()
        for case,_,h,raw,_,_,_ in raw_packets:
            if len(h)==case[2] or len(raw)<=1:
                continue
            base=min(v.e for v in raw.values())
            rows=[(v,2*(v.e-base)) for v in raw.values()]
            if max(max(abs(n).bit_length() for n in v.n) for v,_ in rows)<=4:
                continue
            prefix=[]; acc=0
            for v,shift in rows:
                acc+=rep.quad(v.n)<<shift
                prefix.append(acc)
            max_prefix_bytes=max(max_prefix_bytes,sys.getsizeof(prefix)+sum(map(sys.getsizeof,prefix)))
            max_prefix_rows=max(max_prefix_rows,len(prefix))
        prep_ns.append(time.perf_counter_ns()-begin)
    result['micro'].update(standalone_preparation_ns=prep_ns,max_prefix_rows=max_prefix_rows,
                           max_measured_python_prefix_bytes=max_prefix_bytes)
    # Re-use the frozen inherited 256-field suite. Its own original checks
    # expect exact failed angles, so supply those only in the independent audit.
    from rp15_fused import verify
    original_make=verify.make
    class Audited(Alt):
        def finish_budget(self,*args,**kwargs):
            selected,left,cert=super().finish_budget(*args,**kwargs)
            ref=self.reference.finish_budget(*args,**kwargs)
            compare(ref,(selected,left,cert),audit)
            return selected,left,ref[2]
    def make_audited(case,method,bank,representation,epsilon=F(1,100),policy='carry',**kwargs):
        if method!='fused':
            return original_make(case,method,bank,representation,epsilon,policy,**kwargs)
        obj=build(case,Audited,epsilon=epsilon,policy=policy,**kwargs)
        obj.reference=build(case,Baseline,epsilon=epsilon,policy=policy,**kwargs)
        return obj
    verify.make=make_audited
    try:
        safety=verify.safety(cb,rep)
    finally:
        verify.make=original_make
    result['inherited_safety']={'fields':safety['same_target_interface_fields'],
                                 'invalid_constructors':len(safety['named_safety_checks']),
                                 'nonmonotone_actual_graph_calls':safety['nonmonotone']['positive_core_calls']}
    # Predeclared input stress, including zero budget, fallback and terminals.
    for policy in ['carry','uniform']:
        engines=pair(CASES[0],epsilon=F(1,1000),policy=policy,caps=(4,6))
        for bits in (9,65,1025):
            for offset in (-513,0,513):
                raw={k:canonical(tuple(((-1)**(k+i))*((1<<bits)+17*i+3+k) for i in range(18)), offset*(k-1)) for k in range(1,4)}
                A=sum((rep.norm(row) for row in raw.values()),F())
                for h in [(0,), (0,)*16]:
                    for left in (0,1,engines[0].ticks):
                        data=[E.finish_budget(h,raw,left,A) for E in engines]
                        compare(*data,audit)
                        audit['stress_fields']+=1
                        audit['stress_fallbacks']+=bool(data[0][2].get('fallback'))
    # Two dyadic thresholds straddling the exact full gamma, one at one grid
    # unit below and one above its square-root floor, with a signed scale gap.
    rows={1:canonical((135,-136)+(0,)*16,300),2:canonical((135,-136)+(0,)*16,-300)}
    A=sum(rep.norm(v) for v in rows.values())
    ys={i:toward(v,4) for i,v in rows.items()}
    C=sum(rep.norm(v) for v in ys.values())
    J=sum(rep.inner(v,ys[k]) for k,v in rows.items())
    angle=1-J*J/(A*C)
    precision=1<<80
    rootnum=isqrt((angle.numerator*precision*precision)//angle.denominator)
    for n,passed in [(rootnum,False),(rootnum+1,True)]:
        eps=F(n,precision)
        assert (angle<=eps*eps)==passed
        engines=pair(CASES[0],epsilon=eps,policy='carry',caps=(4,))
        vals=[engine.finish_budget((0,)*15,rows,engine.ticks,A) for engine in engines]
        compare(*vals,audit)
        assert vals[1][2]['fallback'] != passed
        audit['near_threshold_fields']+=1
    # Until-factor costs exclude setup/comparisons. Alternate the order.
    solves=[]
    for i,case in enumerate(CASES):
        for source,seed in [('inherited',run.PLAN['seed_base']+i*10000),('new',NEW_SEEDS[i])]:
            pairdata={}; costs={}; counters={}
            order=(0,1) if (i+(source=='new'))%2==0 else (1,0)
            for j in order:
                run.FusedBudget=(Baseline,Alt)[j]
                gc.collect()
                begin=timer()
                try: pairdata[j],counters[j]=run.solve(case,'fused',cb,rep,seed)
                finally: run.FusedBudget=Baseline
                costs[j]=timer()-begin
            compare(pairdata[0],pairdata[1],audit)
            assert pairdata[0]['success']
            if source=='inherited':
                prior=run.load(root/'rp15_fused'/'evidence'/f'SOLVES_{case[0]}_r0_fused.json.gz')
                assert run.encode(pairdata[0])==prior[0]['result']
            solves.append(dict(N=case[0],source=source,outputs=len(pairdata[0]['outputs']),
                               reference_seconds=costs[0],prefix_seconds=costs[1],
                               visits=counters[0].get('candidate_row_visits',0),
                               skipped=counters[1].get('skipped_rows',0)))
    result['solves']=solves
    if full:
        laws=[]
        for N,a,t,policy,eps in run.PLAN['diagnostics']:
            es=pair((N,a,t),policy=policy,epsilon=F(eps))
            stat=Counter()
            leaf_probs=[F(0)]*(1<<t)
            frozen_records=iter(run.load(root/'rp15_fused'/'evidence'/f'REPLAY_BRANCHES_{N}.json.gz'))
            def walk(h,field,left,prob):
                if len(h)==t:
                    stat['reachable_leaves']+=1
                    leaf_probs[sum(b<<i for i,b in enumerate(h))]=prob
                    return
                r0,r1=[E.prepare(h,field) for E in es]
                assert r0==r1
                arms,mass,total=r0
                for bit in (0,1):
                    if not mass[bit]: continue
                    hist=h+(bit,)
                    outputs=[E.finish_budget(hist,arms[bit],left,mass[bit]) for E in es]
                    compare(*outputs,audit)
                    out,bal,cert=outputs[0]
                    frozen=next(frozen_records)
                    assert frozen['h']==list(hist) and F(frozen['probability'])==prob*mass[bit]/total
                    assert frozen['certificate']==run.encode(cert)
                    stat['reachable_branches']+=1
                    stat['returned_rows']+=len(out)
                    stat['candidate_tests']+=len(cert.get('candidates',()))
                    walk(hist,out,bal,prob*mass[bit]/total)
            walk((),{1:es[0].one},es[0].ticks,F(1))
            assert next(frozen_records,None) is None
            assert run.encode(leaf_probs)==run.load(root/'rp15_fused'/'evidence'/f'REPLAY_LAW_{N}.json.gz')
            stat['complete_law_entries']=len(leaf_probs)
            assert es[0].counts==es[1].counts and es[0].stats==es[1].stats
            laws.append(dict(N=N,**stat,baseline_visits=es[0].performance['candidate_row_visits'],
                             skipped=es[1].performance['skipped_rows']))
        result['laws']=laws
    result['audit']=dict(audit)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--rp15',type=Path,help='externally supplied directory RP14_Run')
    parser.add_argument('--full-laws',action='store_true')
    args=parser.parse_args()
    result={'projection_checks':public_checks()}
    if args.rp15:
        result['archive_replay']=replay(args.rp15.resolve(),args.full_laws)
    print(json.dumps(result,indent=2))
