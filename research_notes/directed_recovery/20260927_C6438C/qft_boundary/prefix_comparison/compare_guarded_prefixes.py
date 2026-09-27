"""Matched warm-prefix comparison; actual inherited native calculations only."""
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import gzip
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]
sys.path.insert(0,str(ROOT.parent/'boundary_execution'))
sys.path.insert(0,str(BASE/'sep27-qft-uniform/uniform_execution'))
sys.path.insert(0,str(BASE/'sep27-qft-adaptive/adaptive_execution'))
from boundary_uniform import BoundaryCheckedUniform
from uniform_feedback import UniformFeedbackGram,WordCertificateBank,packed
from check_adaptive_feedback import load_bank,ExactCarrierCodec,LazyStreamingProgram,CALLS,verify_vendor


def run_prefix(cls,program,certificates,history):
    columns_before=sum(t.report_metrics()['computed_columns']
                       for t in program.lazy_factory.tables.values())
    first,t0=len(CALLS),perf_counter()
    engine=cls(program,F(1,3),certificate_bank=certificates)
    plans=[]
    for bit in history:
        plans.append(engine.advance(bit))
    terminal_mass=engine.mass()
    calculation_seconds=perf_counter()-t0
    calculation_core_calls=len(CALLS)-first
    columns_after=sum(t.report_metrics()['computed_columns']
                      for t in program.lazy_factory.tables.values())
    counter_snapshot={'gram':dict(engine.stats),'policy':dict(engine.policy_stats)}
    if hasattr(engine,'_guard_diagnostics'):
        counter_snapshot['guard']=engine._guard_diagnostics()
    ledger=[{'history':s.history,'reference_ids':s.reference_ids,
             'selected_ids':s.selected_ids,'charge':s.charge,'bit':s.bit,
             'certificate_sha256':s.certificate_sha256} for s in engine.steps]
    evidence_start=perf_counter()
    evidence=engine.evidence()
    evidence_seconds=perf_counter()-evidence_start
    receipt={'implementation':cls.__name__,'history':history,
        'calculation_seconds':calculation_seconds,'evidence_capture_seconds':evidence_seconds,
        'total_seconds_through_evidence':perf_counter()-t0,
        'calculation_actual_core_calls':calculation_core_calls,
        'computed_modular_columns_before':columns_before,
        'computed_modular_columns_after':columns_after,
        'total_actual_core_calls':len(CALLS)-first,
        'core_call_interval':[first,len(CALLS)],'counters_before_evidence':counter_snapshot,
        'plans':plans,'terminal_mass':terminal_mass,'ledger':ledger,'evidence':evidence}
    return receipt


def main():
    guard=json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    paths=[Path(__file__),ROOT.parent/'boundary_execution/boundary_uniform.py',
           BASE/'sep27-qft-uniform/uniform_execution/uniform_feedback.py']
    source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    first,t0=len(CALLS),perf_counter()
    vendor=verify_vendor()
    native_bank,native_source=load_bank()
    programs=[LazyStreamingProgram(N,a,4,native_bank,61,codec=ExactCarrierCodec(61,tuple(range(6))))
              for N,a in ((21,2),(21,4),(65,3))]
    cold_start,cold_first=perf_counter(),len(CALLS)
    certificates=WordCertificateBank(programs[0])
    cold={'elapsed_seconds':perf_counter()-cold_start,'actual_core_calls':len(CALLS)-cold_first,
          'evidence':certificates.evidence()}
    history=(1,0,0,0)
    warmups=[]
    pairs=[]
    for program in programs:
        certificates.check(program)
        # Explicit paid preconditioning supplies both implementations the same
        # warm modular-column/primitive cache. Each measured Gram cache is fresh.
        warmups.append({'N':program.N,'a':program.a,
                        'run':run_prefix(UniformFeedbackGram,program,certificates,history)})
        for repetition,order in enumerate(((UniformFeedbackGram,BoundaryCheckedUniform),
                                           (BoundaryCheckedUniform,UniformFeedbackGram))):
            runs=[run_prefix(cls,program,certificates,history) for cls in order]
            old=next(x for x in runs if x['implementation']=='UniformFeedbackGram')
            new=next(x for x in runs if x['implementation']=='BoundaryCheckedUniform')
            assert old['plans']==new['plans'] and old['ledger']==new['ledger']
            assert old['terminal_mass']==new['terminal_mass']>0
            assert old['calculation_actual_core_calls']==new['calculation_actual_core_calls']
            for run in runs:
                assert run['computed_modular_columns_before']==run['computed_modular_columns_after']
            for key in ('correlations','observer_operations'):
                assert old['evidence']['inherited'][key]==new['evidence']['inherited'][key]
            for key in ('query_requests','query_cache_hits','base_queries','recurrence_queries',
                        'native_phase_vector_applications'):
                assert old['counters_before_evidence']['gram'][key]==new['counters_before_evidence']['gram'][key]
            summary={'N':program.N,'a':program.a,'repetition':repetition,
                'order':[x['implementation'] for x in runs],
                'old_seconds':old['calculation_seconds'],'new_seconds':new['calculation_seconds'],
                'old_total_seconds':old['total_seconds_through_evidence'],
                'new_total_seconds':new['total_seconds_through_evidence'],
                'core_calls_each':old['calculation_actual_core_calls'],
                'old_full_binding_checks':old['counters_before_evidence']['policy']['certificate_binding_checks'],
                'new_full_binding_checks':new['counters_before_evidence']['policy']['certificate_binding_checks'],
                'measured_new_modular_columns_each':0,
                'complete_saved_correlations_and_observer_streams_equal':True,
                'plans_ledger_terminal_mass_and_scientific_counters_equal':True}
            pairs.append({'summary':summary,'runs':runs})
            print(json.dumps(summary),flush=True)
    assert source_hashes=={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    record={'schema':'BRC_BOUNDARY_MATCHED_PREFIX_COMPARISON_V1','source_hashes':source_hashes,
        'vendor':vendor,'native_bank_source':native_source,'shared_cold_certificate':cold,
        'paid_warmups':warmups,'pairs':pairs,'actual_native_core_calls':CALLS[first:],
        'actual_native_core_call_count':len(CALLS)-first,'elapsed_seconds':perf_counter()-t0,
        'programs':[{'N':p.N,'a':p.a,'phase_bindings':p.phase_bindings,'codec_binding':p.codec_binding,
            'tables':[t.export_certificate() for t in p.lazy_factory.tables.values()],
            'permutation_verifications':p.lazy_permutation_verifications} for p in programs],
        'scope':'Three fixed positive prefixes, two alternating paired orders each, one process. Paid shared cold setup and warmups separate; each measured Gram cache fresh. Ordinary system load not controlled. Not full laws, independent random trials, asymptotic acceleration or cold startup speedup.'}
    raw=packed(record)
    target=ROOT/'MATCHED_PREFIX_RESULTS.json.gz'
    if target.exists():raise ValueError('refusing to replace recorded experiment')
    target.write_bytes(gzip.compress(raw,mtime=0))
    summary={'schema':record['schema'],'source_hashes':source_hashes,
        'pairs':[x['summary'] for x in pairs],
        'actual_native_core_call_count':record['actual_native_core_call_count'],
        'elapsed_seconds':record['elapsed_seconds'],'raw_bytes':len(raw),
        'raw_sha256':hashlib.sha256(raw).hexdigest(),'gzip_bytes':target.stat().st_size,
        'gzip_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
    (ROOT/'MATCHED_PREFIX_SUMMARY.json').write_bytes(packed(summary))
    print(packed(summary).decode(),flush=True)


if __name__=='__main__':main()
