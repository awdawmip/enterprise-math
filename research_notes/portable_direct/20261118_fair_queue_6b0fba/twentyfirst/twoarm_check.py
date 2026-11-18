"""Paired 2-adic normalization downstream of the original RP15 signed two-arm join."""
import argparse
from collections import Counter
from fractions import Fraction as F
import gc
import hashlib
import json
from pathlib import Path
import resource
import statistics
import subprocess
import sys
import time

CASES=((35,2,12),(85,2,14),(91,2,14))
SEEDS=tuple(tuple(20261119010000+100*i+j for j in range(3)) for i in range(len(CASES)))
ORDERS=(('original','paired'),('paired','original'),('paired','original'),('original','paired'))
PINS={'rp15_fused/engine.py':'606aa6d3c404f10b131af4c8c4f3faa5cbabf52b0651b452ead8f42887266836',
      'rp15_fused/run.py':'0e9b6cde04d2564ba5391f54fc3c85127eb424de0431bcc6bc6557c49c40f6e8',
      'rp15_fused/PLAN.json':'b0fce9471c53b01c28094e865cc1dadfc1578321c44cfb4622c4c1e8d1f252a7',
      'rp14_budget/engine.py':'3b3306918b3a6daeb21f9fb9850d7db6d857d42282b44119d8f5411663ea3fcc'}
def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':'),default=str).encode()).hexdigest()


def bind(root):
    sys.path.insert(0,str(root))
    for name,sha in PINS.items():
        assert hashlib.sha256((root/name).read_bytes()).hexdigest()==sha
    from rp15_fused import run,engine
    from rp11_closed.engine import Row,canonical,join
    return run,engine,Row,canonical,join


def new_method(api):
    run,engine,Row,canonical,join=api

    def primitive(x,led):
        if x is None:return None,-1
        if x.n[0]&1:return x,0
        for i,v in enumerate(x.n):
            if v&1:return x,i
        if not any(x.n):return None,-1
        # The frozen direct caller may pass a non-canonical dyadic Row. Preserve its numeric value.
        if led is not None:led['external_input_normalizations']+=1
        x=canonical(x.n,x.e)
        return x,next(i for i,v in enumerate(x.n) if v&1)

    def pair(x,y,led=None):
        x,j=primitive(x,led);y,_=primitive(y,led)
        if x is None or y is None:
            if x is None and y is None:return None,None
            z=x if x is not None else y
            p=Row(z.n,z.e-1)
            if led is not None:
                led['left' if x is not None else 'right']+=1
                led['new_join_Row_objects']+=1 if x is not None else 2
            return (p,p) if x is not None else (p,Row(tuple(-c for c in z.n),p.e))
        if x.e==y.e and x.n==y.n:
            if led is not None:led['equal']+=1
            return x,None
        a,b=x.n,y.n
        base=min(x.e,y.e)-1
        if x.e!=y.e:
            if x.e<y.e:b=tuple(v<<(y.e-x.e) for v in b)
            else:a=tuple(v<<(x.e-y.e) for v in a)
            outputs=(Row(tuple(v+w for v,w in zip(a,b)),base),
                     Row(tuple(v-w for v,w in zip(a,b)),base))
            if led is not None:
                led['different exponent']+=1;led['one_shifted_tuple']+=1;led['new_join_Row_objects']+=2
            return outputs
        plus=tuple(v+w for v,w in zip(a,b))
        if not any(plus):
            if led is not None:led['opposite']+=1
            return None,x
        minus=tuple(v-w for v,w in zip(a,b))
        if led is not None:led['new_join_Row_objects']+=2
        if any(v&1 for v in plus):
            if led is not None:led['different parity']+=1
            return Row(plus,base),Row(minus,base)
        p=tuple(v>>1 for v in plus);m=tuple(v>>1 for v in minus)
        plus_forced=bool(p[j]&1)
        known,other=(p,m) if plus_forced else (m,p)
        if led is not None:led['same parity, plus forced' if plus_forced else 'same parity, minus forced']+=1
        left=Row(known,x.e)
        if any(v&1 for v in other):right=Row(other,x.e)
        else:
            if led is not None:led['new_deep_output_normalizations']+=1
            right=canonical(other,x.e)
        return (left,right) if plus_forced else (right,left)

    class Paired(engine.FusedMassBudget):
        meter=None
        def prepare(self,h,field):
            self.program.literal_bank_handle.check_all()
            slots={w:[v,None] for w,v in field.items()}
            for w,x in field.items():
                dest=self.program.tables[len(h)][w]
                if dest not in slots:slots[dest]=[None,None]
                slots[dest][1]=self.word(h,x)
            arms=({},{});led=self.meter
            for w,(x,y) in slots.items():
                p,m=pair(x,y,led)
                if p is not None:arms[0][w]=p
                if m is not None:arms[1][w]=m
            if led is not None:
                led['new_join_label_visits']+=len(slots)
                led['join_slot_peak']=max(led['join_slot_peak'],len(slots))
                led['two_raw_fields_label_rows']+=len(arms[0])+len(arms[1])
            masses=tuple(engine.field_mass(self.replica,arm) for arm in arms)
            M=engine.field_mass(self.replica,field)
            if sum(masses)!=M:raise AssertionError('unchanged native instrument norm identity')
            self.stats['rounds']+=1;self.stats['rows']+=len(field)
            return arms,masses,M
    return pair,Paired


def field_rows(field):
    return [(w,x.e,x.n) for w,x in field.items()]


def solve(api,klass,cb,rep,case,seed,trace=False):
    run=api[0];rng=run.Tape(seed)
    post=run.DemandDriver(run.DemandFactory(16)).classical_postprocess
    records=[];full=[];led=Counter()
    if trace:
        class Observed(klass):
            def prepare(self,h,field):
                result=super().prepare(h,field);arms,masses,M=result
                full.append(('prepare',h,field_rows(field),[field_rows(arm) for arm in arms],masses,M))
                return result
            def finish_budget(self,h,raw,remaining,A=None):
                out=super().finish_budget(h,raw,remaining,A)
                full.append(('finish',h,remaining,A,field_rows(raw),field_rows(out[0]),out[1],out[2]))
                return out
    else:Observed=klass
    for trial in range(64):
        e=Observed(run.make_program(case,cb),cb,rep)
        if trace:e.meter=led
        record=e.sample(rng,post,1);records.append(record)
        if trace:
            for k in ('rows','gates','rounds'):led[k]+=record['stats'][k]
            for k in ('peak_raw_bits','peak_stored_bits','peak_support'):
                led[k]=max(led[k],record['stats'][k])
        if record['status']!='SURVIVED' or record['result']['postprocessing']['factors']:break
    result=(records,rng.requests,rng.getstate())
    return result,full,led


def group(api,cb,rep,cls,case,seeds):
    gc.collect();start=time.perf_counter_ns()
    rows=[solve(api,cls,cb,rep,case,s) for s in seeds]
    elapsed=time.perf_counter_ns()-start
    return elapsed,[digest(row[0]) for row in rows]


def interface(api,pair):
    run,_,Row,canonical,join=api;led=Counter()
    z=Row((0,)*18,7)
    def row(a,b,e):return Row((a,b)+(0,)*16,e)
    rs=[z]+[row(a,b,e) for a,b in ((1,0),(-1,0),(1,2),(1,6),(-3,2),(3,0),(2,4),(0,3),(0,-3),(0,8))
                                      for e in (-25,0,31)]
    # Include near cancellation, arbitrary high valuation and mixed-parity halves.
    rs.extend([row(1+(1<<160),2,0),row(1,2,0),row(3,6,0),row(-1,-2,0)])
    for x in rs:
        for y in rs:
            got=pair(x,y,led)
            for b,actual in enumerate(got):
                want=join(x,y,1 if b==0 else -1,True)
                assert (None if want.zero() else want)==actual
    assert all(led[k] for k in ('equal','opposite','different exponent','different parity',
                          'same parity, plus forced','same parity, minus forced','new_deep_output_normalizations',
                          'external_input_normalizations'))
    return {'row_count':len(rs),'paired_tests':len(rs)**2,'diagnostics':dict(led)}


def tree_controls(api,cls,alt,cb,rep):
    run=api[0];out=[]
    for case in ((15,2,4),(21,2,6)):
        es=[C(run.make_program(case,cb),cb,rep) for C in (cls,alt)]
        # Empty fields never get conditionally normalized.
        assert es[0].prepare((),{})==es[1].prepare((),{})==(({},{}),(F(0),F(0)),F(0))
        frontier=[((),{1:es[0].one},es[0].ticks)]
        dead=0;records=[];tested=0;nonzero_tail=False
        for depth in range(case[2]):
            following=[]
            for h,field,ticks in frontier:
                left,right=[e.prepare(h,field) for e in es]
                assert left==right
                arms,masses,M=left;tested+=1
                for bit in (0,1):
                    records.append((h,bit,masses[bit],field_rows(arms[bit])))
                    if not masses[bit]:
                        assert not arms[bit];dead+=1;continue
                    for x in arms[bit].values():
                        nonzero_tail |= any(x.n[2:])
                    nh=(*h,bit)
                    old,new=[e.finish_budget(nh,arms[bit],ticks,masses[bit]) for e in es]
                    assert old==new
                    following.append((nh,old[0],old[1]))
            frontier=following
        class Exhausted:
            def __init__(self):self.calls=[]
            def randrange(self,n):
                self.calls.append(n);raise EOFError
        results=[]
        for e in es:
            e=type(e)(run.make_program(case,cb),cb,rep)
            tape=Exhausted()
            result=e.sample(tape,run.DemandDriver(run.DemandFactory(16)).classical_postprocess,1)
            results.append((result,tape.calls))
        assert results[0]==results[1] and results[0][0]['status']=='INCOMPLETE_RANDOM_SOURCE'
        out.append({'N_a_t':case,'positive_parents':tested,'positive_terminal_leaves':len(frontier),
                    'zero_mass_children':dead,'nonzero_internal_coordinates_beyond_first_two':nonzero_tail,
                    'ordered_raw_branch_digest':digest(records),'incomplete_tape_calls':results[0][1],
                    'incomplete_tape_stop_history':results[0][0]['result']['history']})
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--rp15',type=Path,required=True)
    ap.add_argument('--cold',choices=['original','paired'])
    ap.add_argument('--controls-only',action='store_true')
    args=ap.parse_args();root=args.rp15.resolve()
    began=time.perf_counter_ns();api=bind(root);run,eng=api[:2]
    pair,Alt=new_method(api);classes={'original':eng.FusedMassBudget,'paired':Alt}
    cb,rep,setup=run.build();built=time.perf_counter_ns()
    if args.controls_only:
        print(json.dumps(tree_controls(api,classes['original'],Alt,cb,rep),sort_keys=True));return
    if args.cold:
        ns,hashes=group(api,cb,rep,classes[args.cold],CASES[0],SEEDS[0][:1])
        print(json.dumps({'setup_ns':built-began,'solve_ns':ns,'full_result_digest':hashes[0],
            'actual_BRC_setup_calls':setup['actual_core_calls'],'maxrss_kib_process':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}))
        return
    cold={}
    for method in ('original','paired'):
        start=time.perf_counter_ns()
        data=subprocess.check_output([sys.executable,__file__,'--rp15',str(root),'--cold',method],text=True)
        cold[method]=json.loads(data);cold[method]['fresh_interpreter_total_ns']=time.perf_counter_ns()-start
    assert cold['original']['full_result_digest']==cold['paired']['full_result_digest']
    controls=tree_controls(api,classes['original'],Alt,cb,rep)
    interface_result=interface(api,pair)
    allcases=[]
    for i,case in enumerate(CASES):
        reference=[];pairs=[];ledger=Counter()
        for seed in SEEDS[i]:
            # Intercept only the frozen original prepare's imported join, never the solver word or quantizer.
            source_join=eng.join;original_calls=Counter()
            def counted(x,y,sign,half):
                z=source_join(x,y,sign,half)
                original_calls['original_join_visits']+=1
                original_calls['original_join_Row_objects']+=1
                original_calls['original_deep_output_normalizations']+=int(not z.zero())
                if not x.zero() and not y.zero() and x.e!=y.e:original_calls['original_nontrivial_aligned_copies']+=1
                return z
            eng.join=counted
            try:baseline,t0,m0=solve(api,classes['original'],cb,rep,case,seed,True)
            finally:eng.join=source_join
            new,t1,m1=solve(api,Alt,cb,rep,case,seed,True)
            assert baseline==new and t0==t1
            assert 2*m1['new_join_label_visits']==original_calls['original_join_visits']
            assert original_calls['original_nontrivial_aligned_copies']==2*m1['one_shifted_tuple']
            for key in ('peak_raw_bits','peak_stored_bits','peak_support','rows','gates','rounds'):assert m1[key]==m0[key]
            for key,val in m1.items():
                if key.startswith('peak_') or key.endswith('_peak'):ledger[key]=max(ledger[key],val)
                else:ledger[key]+=val
            ledger.update(original_calls)
            records,requests,state=baseline
            fullhash=digest(new);reference.append(fullhash)
            last=records[-1]
            pairs.append({'seed':seed,'number_outputs':len(records),'last_status':last['status'],
             'factors':last['result'].get('postprocessing',{}).get('factors',[]),'reference_equals_new':True,
             'science_rng_and_stop_digest':fullhash,'raw_fields_ordered_rows_and_certificates_digest':digest(t1),
             'full_prepare_and_finish_records':len(t1),'random_requests':len(requests)})
        times={'original':[],'paired':[]}
        for order in ORDERS:
            for method in order:
                ns,check=group(api,cb,rep,classes[method],case,SEEDS[i])
                assert check==reference
                times[method].append(ns)
        allcases.append({'N_a_t':case,'seeds':pairs,'prepare_cost_until_stop':dict(ledger),
                  'population_batch_wall_ns':times,'batch_median_ns':{k:statistics.median(v) for k,v in times.items()}})
    print(json.dumps({'experiment':'twoarm_paired_2adic_prepare','pinned_sources':PINS,'predeclared_orders':ORDERS,
       'max_outputs':64,'setup_actual_BRC_calls':setup['actual_core_calls'],'fresh_interpreters':cold,
       'small_trees_and_exhausted_tape':controls,'synthetic_typed_interface':interface_result,'cases':allcases,
       'scope':'all fields materialized; separate full-field audit; clock/RSS from this execution only'},
       default=str,indent=1,sort_keys=True))


if __name__=='__main__':main()
