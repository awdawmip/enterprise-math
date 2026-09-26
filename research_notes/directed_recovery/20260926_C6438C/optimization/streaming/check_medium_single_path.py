"""One actual N143/a2/t16 path, no all-history/control-state expansion.

The inherited frozen rank-one phase quotient and the admitted complete-column
adapter have different matvec implementations. Their raw clocks are reported
without inferring a general speedup from phase-vector counts.
"""
from __future__ import annotations
import gzip,json,random,sys
from pathlib import Path
from time import perf_counter_ns
from check_streaming_optimization import (ReferenceCounter, instrument_only,
    lazy_certificate, packed, sha, state_record, compile_modular_permutation,
    sparse_modular_columns, sample_once, sample_selected, SelectedStreamingProgram,
    CALLS, verify_vendor, encode, PACKAGE)

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(PACKAGE/'phases'))
from closed_phase_bank import load_certified_bank


class ReferenceRecorder(ReferenceCounter):
    def branches(self,*args,**kwargs):
        result=super().branches(*args,**kwargs)
        self.last_children=result
        return result


class SelectedRecorder(SelectedStreamingProgram):
    def materialize(self,*args,**kwargs):
        result=super().materialize(*args,**kwargs)
        self.last_selected=result
        return result


def measured(action):
    calls=len(CALLS);start=perf_counter_ns()
    result=action()
    return result,{'elapsed_ns':perf_counter_ns()-start,'native_kernel_calls_delta':len(CALLS)-calls}


def main():
    kernel=verify_vendor();first_call=len(CALLS)
    N,a,t=143,2,16
    loaded,load_cost=measured(lambda:load_certified_bank(t,cutoff=33,
        expected_payload_sha256='feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c'))
    bank,_,dim,bank_binding=loaded
    print(json.dumps({'stage':'frozen_bank_loaded','dim':dim,'load':load_cost}),flush=True)
    ref,ref_setup=measured(lambda:ReferenceRecorder(N,a,t,bank,dim,column_factory=sparse_modular_columns))
    opt,opt_setup=measured(lambda:SelectedRecorder(N,a,t,bank,dim))
    print(json.dumps({'stage':'programs_constructed','reference':ref_setup,'optimized':opt_setup}),flush=True)
    expected,ref_run=measured(lambda:sample_once(ref,random.Random(20260928),postprocess=instrument_only))
    print(json.dumps({'stage':'reference_path_complete','k':expected['k'],'cost':ref_run}),flush=True)
    actual,opt_run=measured(lambda:sample_selected(opt,random.Random(20260928),postprocess=instrument_only))
    assert actual==expected
    ref_state,ref_den=ref.last_children[expected['history'][-1]]
    opt_state,opt_den=opt.last_selected
    assert ref_state==opt_state and ref_den==opt_den
    assert ref.constructed_children==2*t and opt.selected_metrics['materialized_children']==t
    complete_maps=[]
    for b in sorted(set(ref.modular_powers)):
        _,certificate=compile_modular_permutation(N,b)
        complete_maps.append({'N':N,'b':b,'full_carrier_columns':1<<(N-1).bit_length(),
            'typed_adder_digit_replays':sum(len(r['add_b']['cells'])+len(r['subtract_N']['cells'])
                                           for r in certificate['steps'])})
    lazy=lazy_certificate(opt)
    source_paths=[Path(__file__),ROOT/'lazy_streaming.py',ROOT/'check_streaming_optimization.py',
                  ROOT.parent/'lazy_modular'/'lazy_modular.py',PACKAGE/'phases'/'closed_phase_bank.py']
    record={'schema':'MEDIUM_SELECTED_CHILD_SINGLE_PATH_V1',
        'status':'AUTHOR_ACTUAL_SHARED_CONTEXT_NOT_ADMITTED','activity':'RA-CAAAC604CB513AEA8BBC1DFC',
        'kernel':kernel,'N':N,'a':a,'t':t,'dim':dim,'seed':20260928,
        'source_files_sha256':{str(p.relative_to(PACKAGE)):sha(p.read_bytes()) for p in source_paths},
        'bank_binding':bank_binding,'whole_carrier_phase_bindings':opt.phase_bindings,
        'native_H4_binding':opt.h4_binding,'sample':actual,
        'all_events_probabilities_and_outcome_equal':True,
        'canonical_terminal_state_and_denominator_equal':True,
        'terminal_state':state_record(opt_state,opt_den),
        'terminal_coordinate_comparisons':len(opt_state)*dim,
        'reference_constructed_children':ref.constructed_children,
        'reference_constructed_child_rows':ref.constructed_child_rows,
        'reference_phase_row_applications':ref.phase_row_applications,
        'reference_metrics':ref.report_metrics(),'optimized_metrics':opt.report_metrics(),
        'reference_distinct_complete_maps':complete_maps,'optimized_lazy_certificates':lazy,
        'raw_cost_observations':{'frozen_bank_load':load_cost,'reference_setup':ref_setup,
          'optimized_setup':opt_setup,'reference_single_path':ref_run,'optimized_single_path':opt_run},
        'raw_clock_limitations':'One process observation, shared catalog/word caches may be warm. Setup included separately. Old FixedRotor uses its certified rank-one quotient; the optimized admission uses general complete columns. No uniform wall-clock or bit-complexity improvement inferred.',
        'postprocessing_scope':'Explicit INSTRUMENT_ONLY_TEST. No factor output, no CF work, no claim of uniform success.',
        'executed_histories_per_program':1,'all_history_enumeration':False,
        'full_control_state_expansion':False,'ideal_reference_execution':False,
        'native_call_receipts':CALLS[first_call:],'actual_BRC_core_calls':len(CALLS)-first_call}
    raw=packed(record);target=ROOT/'MEDIUM_SINGLE_PATH_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw,mtime=0))
    summary={k:v for k,v in record.items() if k not in ('terminal_state','whole_carrier_phase_bindings','native_call_receipts','optimized_lazy_certificates')}
    summary['lazy_table_metrics']=lazy['metrics']
    summary['lazy_distinct_global_verification_adder_digits']=lazy['distinct_global_verification_adder_digits']
    summary['payload_sha256']=sha(raw);summary['gzip_sha256']=sha(target.read_bytes())
    (ROOT/'MEDIUM_SINGLE_PATH_SUMMARY.json').write_text(json.dumps(encode(summary),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','N':N,'t':t,'k':actual['k'],
        'reference_children':ref.constructed_children,'optimized_children':opt.selected_metrics['materialized_children'],
        'terminal_coordinate_comparisons':len(opt_state)*dim,
        'actual_BRC_core_calls':len(CALLS)-first_call,'payload_sha256':sha(raw)}),flush=True)


if __name__=='__main__':main()
