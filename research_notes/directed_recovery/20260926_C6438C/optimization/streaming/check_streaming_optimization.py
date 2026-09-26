"""Actual small-history equivalence and single-path work observations.

History enumeration is a bounded check, not part of the selected-path executor.
Performance comparisons isolate the terminal instrument with an explicit
non-factoring postprocessor; raw clocks are observations, not complexity proof.
"""
from __future__ import annotations
import gzip, hashlib, json, random, sys
from pathlib import Path
from fractions import Fraction as F
from time import perf_counter_ns

from lazy_streaming import (SelectedStreamingProgram, LazyStreamingProgram,
                            sample_selected, PACKAGE)
from general_streaming import GeneralStreamingProgram
from general_driver import sample_once
from terminal_instrument import load_frozen_bank
from sparse_modular import sparse_modular_columns, compile_modular_permutation
from stage80.fixed_phase import norm, leakage
from stage45.brc_loop_recheck import CALLS, verify_vendor
from stage79.phase_compiler import encode
from compiled_streaming import bank_from_compilation

ROOT = Path(__file__).resolve().parent


def sha(data): return hashlib.sha256(data).hexdigest()
def packed(value): return json.dumps(encode(value), sort_keys=True, separators=(',', ':')).encode()
def state_record(state, den):
    return {'den': den, 'state': [{'key': key, 'row': row} for key,row in sorted(state.items())]}
def instrument_only(N,a,t,k):
    return {'status':'INSTRUMENT_ONLY_TEST','N':N,'a':a,'t':t,'k':k,'factors':[]}


class ReferenceCounter(GeneralStreamingProgram):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.constructed_children = self.constructed_child_rows = 0
        self.phase_row_applications = {'total':0,'by_phase':{}}
        self.bank={m:CountPhaseRows(gate,m,self.phase_row_applications) for m,gate in self.bank.items()}
    def branches(self, state, den, history):
        result=super().branches(state,den,history)
        self.constructed_children += 2
        self.constructed_child_rows += sum(len(s) for s,d in result)
        return result


class CountPhaseRows:
    def __init__(self,gate,m,counter): self.gate,self.m,self.counter=gate,m,counter
    def __getattr__(self,name): return getattr(self.gate,name)
    def apply_numer(self,values,inverse=False):
        self.counter['total']+=1
        key=str(self.m)
        self.counter['by_phase'][key]=self.counter['by_phase'].get(key,0)+1
        return self.gate.apply_numer(values,inverse)


def reference(N,a,t,bank,dim):
    return ReferenceCounter(N,a,t,bank,dim,column_factory=sparse_modular_columns)


def lazy_certificate(program):
    unique_proofs={p['certificate_sha256']:p for p in program.lazy_permutation_verifications}
    return {'global_permutation_verifications':program.lazy_permutation_verifications,
            'distinct_global_verification_adder_digits':sum(p['replayed_adder_digits'] for p in unique_proofs.values()),
            'distinct_tables':program.lazy_factory.export_certificate(),
            'metrics':[table.report_metrics() for key,table in sorted(program.lazy_factory.tables.items())]}


def complete_histories(label,N,a,t,bank,dim):
    ref=reference(N,a,t,bank,dim)
    lazy=LazyStreamingProgram(N,a,t,bank,dim)
    selected=SelectedStreamingProgram(N,a,t,bank,dim)
    state,den=ref.initial(); prefixes=[((),state,den)]
    observations=[]; comparisons=0
    for depth in range(t):
        following=[]
        for history,state,den in prefixes:
            ref_children=ref.branches(state,den,history)
            lazy_children=lazy.branches(state,den,history)
            plan=selected.branch_plan(state,den,history)
            selected_children=[selected.materialize(plan,b) for b in (0,1)]
            assert ref_children==lazy_children==selected_children
            masses=tuple(norm(s,d) for s,d in ref_children)
            assert masses==plan.masses
            comparisons+=sum(len(s)*dim for s,d in ref_children)
            observations.append({'history':history,'before_mass':norm(state,den),
                'M':plan.M,'G':plan.G,'feedback_denominator':plan.h,
                'child_masses':masses,'support_rows':len(plan.rows),
                'support_collisions':sum(y in plan.rows for y in plan.targets.values()),
                'child_state_sha256':[sha(packed(state_record(s,d))) for s,d in ref_children]})
            following.extend((history+(b,),s,d) for b,(s,d) in enumerate(ref_children))
        prefixes=following
    assert len(prefixes)==1<<t
    assert sum(norm(s,d) for h,s,d in prefixes)==1
    return {'label':label,'N':N,'a':a,'t':t,'dim':dim,
            'all_history_edges':len(observations)*2,
            'nonzero_child_coordinates_compared':comparisons,
            'all_canonical_states_denominators_and_masses_equal':True,
            'terminal_leaf_slots':len(prefixes),'positive_leaves':sum(bool(s) for h,s,d in prefixes),
            'residual_mass':sum((leakage(s,d) for h,s,d in prefixes),F(0)),
            'observations':observations,
            'terminal_leaves':[{'history':h,**state_record(s,d)} for h,s,d in prefixes],
            'lazy_native_branch_metrics':lazy.report_metrics(),
            'selected_metrics':selected.report_metrics(),
            'lazy_certificates':lazy_certificate(selected),
            'whole_carrier_phase_bindings':selected.phase_bindings,
            'native_H4_binding':selected.h4_binding,
            'enumeration_scope':'finite validation only; not required by single-path execution'}


class ExhaustingRandom:
    def __init__(self,limit,seed=20260927): self.left=limit;self.rng=random.Random(seed)
    def randrange(self,*args):
        if self.left==0: raise StopIteration
        self.left-=1
        return self.rng.randrange(*args)


def single_path(label,N,a,t,bank,dim):
    ref=reference(N,a,t,bank,dim)
    selected=SelectedStreamingProgram(N,a,t,bank,dim)
    start_calls=len(CALLS); start=perf_counter_ns()
    original=sample_once(ref,random.Random(20260927),postprocess=instrument_only)
    ref_clock=perf_counter_ns()-start; ref_calls=len(CALLS)-start_calls
    start_calls=len(CALLS); start=perf_counter_ns()
    optimized=sample_selected(selected,random.Random(20260927),postprocess=instrument_only)
    opt_clock=perf_counter_ns()-start; opt_calls=len(CALLS)-start_calls
    assert original==optimized
    assert selected.selected_metrics['materialized_children']==t
    full_columns=[]
    for b in sorted(set(ref.modular_powers)):
        _,certificate=compile_modular_permutation(N,b)
        full_columns.append({'N':N,'b':b,'full_carrier_columns':1<<(N-1).bit_length(),
            'typed_adder_digit_replays':sum(len(s['add_b']['cells'])+len(s['subtract_N']['cells'])
                                           for s in certificate['steps'])})
    interrupted=[]
    for budget in (0,1):
        p=reference(N,a,t,bank,dim);q=SelectedStreamingProgram(N,a,t,bank,dim)
        old=sample_once(p,ExhaustingRandom(budget),postprocess=instrument_only)
        new=sample_selected(q,ExhaustingRandom(budget),postprocess=instrument_only)
        assert old==new and old['status']=='INCOMPLETE_RANDOM_SOURCE'
        assert q.selected_metrics['materialized_children']==len(new['history'])
        interrupted.append({'random_call_budget':budget,'raw_outcome':new,
                            'optimized_metrics':q.report_metrics()})
    expected_default=sample_once(reference(N,a,t,bank,dim),random.Random(20260927))
    eager_calls=[]
    def eager_observer(frame,event,arg):
        if event=='call' and ((frame.f_code.co_name=='compile_modular_permutation' and
                              frame.f_globals.get('__name__')=='sparse_modular') or
                             (frame.f_code.co_name=='modular_columns' and
                              frame.f_globals.get('__name__')=='stage78.shor_benchmark')):
            eager_calls.append(frame.f_code.co_name)
    sys.setprofile(eager_observer)
    try:
        lazy_default=sample_selected(SelectedStreamingProgram(N,a,t,bank,dim),random.Random(20260927))
    finally:
        sys.setprofile(None)
    assert lazy_default==expected_default and not eager_calls
    return {'label':label,'N':N,'a':a,'t':t,'sample':optimized,
        'raw_events_and_outcome_exact_equal':True,
        'reference_constructed_children':ref.constructed_children,
        'reference_constructed_child_rows':ref.constructed_child_rows,
        'reference_phase_row_applications':ref.phase_row_applications,
        'reference_metrics':ref.report_metrics(),
        'optimized_metrics':selected.report_metrics(),
        'reference_distinct_complete_maps':full_columns,
        'optimized_lazy_certificates':lazy_certificate(selected),
        'clock_ns':{'reference_execution':ref_clock,'optimized_execution':opt_clock},
        'execution_native_kernel_call_deltas':{'reference':ref_calls,'optimized':opt_calls},
        'clock_scope':'one raw process observation after setup; caches may be warm; no wall-clock speedup or cold-cache claim',
        'postprocessing_scope':'explicit INSTRUMENT_ONLY_TEST; no factor result or CF work included',
        'random_source_scope':'same seeded software demonstration, not physical/uniformity certification',
        'default_lazy_postprocessing_exact_equal':True,
        'default_sample_result':lazy_default,
        'default_eager_modular_entrypoint_calls':eager_calls,
        'interrupted_raw_parent_regressions':interrupted}


def collision_negative_control(bank,dim):
    p=SelectedStreamingProgram(15,2,4,bank,dim)
    native=reference(15,2,4,bank,dim)
    # At final depth with history 000, P is multiplication by2 and feedback I.
    u=tuple(int(j in (0,5)) for j in range(dim))
    cases=[]
    for labels in ((1,2),(1,4)):
        state={(0,w,0):u for w in labels};plan=p.branch_plan(state,2,(0,0,0))
        children=native.branches(state,2,(0,0,0))
        assert tuple(norm(s,d) for s,d in children)==plan.masses
        cases.append({'labels':labels,'row':u,'parent_mass':F(plan.M,4),
                      'G':plan.G,'child_masses':plan.masses})
    assert cases[0]['child_masses']==(F(3,4),F(1,4))
    assert cases[1]['child_masses']==(F(1,2),F(1,2))
    return {'same_complete_row_histogram':True,'different_label_collision_probabilities':True,
            'non_principal_mode_5_retained':True,'cases':cases,
            'conclusion':'row sharing is valid; discarding work-label collision structure is not'}


def main():
    kernel=verify_vendor(); start=len(CALLS)
    frozen,_,dim=load_frozen_bank(4)
    path=PACKAGE/'direct_word_integration'/'DIRECT_WORD_INTEGRATION_RESULTS.json.gz'
    raw=gzip.decompress(path.read_bytes())
    assert sha(raw)=='79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c'
    compiled=json.loads(raw)['phase_compilation']
    direct=bank_from_compilation(compiled,t=4,epsilon=1)['bank']
    history_results=[]; path_results=[]
    for label,N,bank in [('frozen_N15',15,frozen),('frozen_N21',21,frozen),('direct_N21',21,direct)]:
        history_results.append(complete_histories(label,N,2,4,bank,dim))
        path_results.append(single_path(label,N,2,4,bank,dim))
        print(json.dumps({'case':label,'all_edges':history_results[-1]['all_history_edges'],
                          'single_path_children':path_results[-1]['optimized_metrics']['selected_child']['materialized_children']}),flush=True)
    negative=collision_negative_control(direct,dim)
    source_files=[Path(__file__),ROOT/'lazy_streaming.py',ROOT.parent/'lazy_modular'/'lazy_modular.py',
                  ROOT.parent/'lazy_modular'/'lazy_postprocess.py',ROOT.parent/'lazy_modular'/'lazy_gcd.py']
    payload={'schema':'EXACT_SELECTED_CHILD_LAZY_STREAMING_CHECKS_V1',
        'status':'AUTHOR_ACTUAL_SHARED_CONTEXT_NOT_ADMITTED',
        'activity':'RA-CAAAC604CB513AEA8BBC1DFC','kernel':kernel,
        'source_files_sha256':{str(p.relative_to(PACKAGE)):sha(p.read_bytes()) for p in source_files},
        'history_results':history_results,'single_path_results':path_results,
        'label_collision_negative_control':negative,'actual_BRC_core_calls':len(CALLS)-start,
        'native_call_receipts':CALLS[start:],'ideal_reference_execution':False,
        'all_61_coordinates_retained':True,'whole_control_expansion_in_executor':False,
        'full_history_enumeration_used_only_by_tests':True}
    raw=packed(payload);out=ROOT/'STREAMING_OPTIMIZATION_RESULTS.json.gz'
    out.write_bytes(gzip.compress(raw,mtime=0))
    summary={k:v for k,v in payload.items() if k not in ('history_results','single_path_results','native_call_receipts')}
    summary['payload_sha256']=sha(raw);summary['gzip_sha256']=sha(out.read_bytes())
    summary['case_summaries']=[{k:r[k] for k in ('label','all_history_edges','terminal_leaf_slots','positive_leaves','residual_mass','nonzero_child_coordinates_compared')} for r in history_results]
    summary['single_path_summaries']=[{k:r[k] for k in ('label','reference_constructed_children','reference_constructed_child_rows','reference_phase_row_applications','optimized_metrics','clock_ns','execution_native_kernel_call_deltas','reference_distinct_complete_maps')} for r in path_results]
    (ROOT/'STREAMING_OPTIMIZATION_SUMMARY.json').write_text(json.dumps(encode(summary),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','actual_BRC_calls':len(CALLS)-start,'payload_sha256':sha(raw)}),flush=True)


if __name__=='__main__':main()
