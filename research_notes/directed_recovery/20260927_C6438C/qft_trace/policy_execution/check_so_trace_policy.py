"""Bounded fixed-prefix policy comparison; not a performance/full-law run."""
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
from uuid import uuid4
import gzip
import hashlib
import json
import sys
import traceback

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]
sys.path.insert(0,str(BASE/'sep26-shor-general/optimization/collision_analysis'))
from check_gram_sampler import load_bank,LazyStreamingProgram,ExactCarrierCodec,verify_vendor
from so_trace_feedback import (BoundaryCheckedSOTrace,SOTraceUniformFeedbackGram,
    SOTraceBank,FrozenBoundary,packed,strict_bytes,CursorReplayError)
from boundary_uniform import WordCertificateBank
from gram_sampler import QueryBudgetExhausted
from stage45.brc_loop_recheck import CALLS

CONTEXT={'stage':'not_started'}


def hashes():
    paths=(Path(__file__),ROOT/'so_trace_feedback.py',
           ROOT.parent/'trace_bank/so_trace_certificates.py',
           BASE/'sep27-qft-boundary/boundary_execution/boundary_uniform.py')
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def clean(obj):
    assert obj._guard_depth==0 and obj._guard_owner is None


def semantic_cursor(cursor):
    return {'epsilon':cursor['epsilon'],'program_sha256':cursor['program_sha256'],
        'history':cursor['history'],
        'steps':[{k:s[k] for k in ('history','reference_ids','selected_ids','charge','bit')}
                 for s in cursor['steps']]}


def pending_semantics(p):
    return {k:p[k] for k in ('history','reference_ids','candidate_ids','selected_ids',
        'remaining_before','charge','decision','uniform_s','rational_test_margin')}


def main():
    out=ROOT/'SO_TRACE_POLICY_RESULTS.json.gz'
    if out.exists():raise ValueError('refusing to overwrite execution evidence')
    CONTEXT['stage']='startup_guard'
    guard=json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    source=hashes();first,start=len(CALLS),perf_counter()
    CONTEXT['stage']='actual_bank_and_program_admission'
    vendor=verify_vendor();native_bank,native_binding=load_bank()
    programs=[LazyStreamingProgram(21,a,4,native_bank,61,
        codec=ExactCarrierCodec(61,tuple(range(6)))) for a in (2,4)]
    initial_admission_end=len(CALLS)
    CONTEXT['stage']='old_and_new_cold_certificate_banks'
    old_bank=WordCertificateBank(programs[0]);new_bank=SOTraceBank(programs[0])
    fixtures=[]
    for program in programs:
        CONTEXT['stage']='matched_fixed_prefix:a'+str(program.a)
        old=FrozenBoundary(program,F(1,3),certificate_bank=old_bank)
        new=BoundaryCheckedSOTrace(program,F(1,3),certificate_bank=new_bank)
        steps=[]
        for bit in (1,0,0,0):
            depth=len(new.history)
            old_plan,new_plan=old.probabilities(),new.probabilities()
            assert old_plan==new_plan and new_plan['child_masses'][bit]>0
            assert pending_semantics(old.pending)==pending_semantics(new.pending)
            assert old.gamma(depth,1)==new.gamma(depth,1)
            assert old.advance(bit)==new.advance(bit)
            assert old.mass()==new.mass()
            assert semantic_cursor(old.cursor())==semantic_cursor(new.cursor())
            clean(old);clean(new)
            steps.append({'depth':depth,'bit':bit,'conditional_masses':deepcopy(new_plan),
                'full_signed_covariance_equal':True,'selected_ids_charge_bit_equal':True,
                'raw_mass_equal':True,'pending_numeric_semantics_equal':True})
        old_evidence=deepcopy(old.evidence());new_evidence=deepcopy(new.evidence())
        assert old_evidence['inherited']['correlations']==new_evidence['inherited']['correlations']
        assert old_evidence['inherited']['observer_operations']==new_evidence['inherited']['observer_operations']
        assert strict_bytes(old.cursor())!=strict_bytes(new.cursor())
        fixtures.append({'N':program.N,'a':program.a,'t':program.t,'history':[1,0,0,0],
            'steps':steps,'old_boundary':old_evidence,'so_boundary':new_evidence,
            'all_retained_covariances_equal':True,'entire_policy_gram_observer_stream_equal':True,
            'certificate_hash_and_cursor_bytes_intentionally_versioned':True})
    p=programs[0]
    CONTEXT['stage']='strict_pending_restore'
    target=BoundaryCheckedSOTrace(p,F(1,3),certificate_bank=new_bank)
    for bit in (1,0,0):target.advance(bit)
    target.prepare_next()
    cursor=json.loads(strict_bytes(target.cursor()))
    pending_snapshot=deepcopy(target.evidence())
    restored=BoundaryCheckedSOTrace.restore(p,cursor,certificate_bank=new_bank)
    assert strict_bytes(restored.cursor())==strict_bytes(cursor)
    assert target.advance(0)==restored.advance(0)
    assert strict_bytes(target.cursor())==strict_bytes(restored.cursor())
    clean(target);clean(restored)
    resume={'input_cursor':cursor,'pending_snapshot':pending_snapshot,
        'original':deepcopy(target.evidence()),'restored':deepcopy(restored.evidence()),
        'strict_new_cursor_equal':True,'query_cache_or_rng_restored':False}
    negatives=[]
    def reject(label,call,*,zero=False):
        CONTEXT['stage']='negative:'+label
        first_call=len(CALLS)
        try:call()
        except ValueError as error:
            delta=len(CALLS)-first_call
            if zero:assert delta==0
            evidence=deepcopy(getattr(error,'evidence',None))
            if evidence is not None:assert evidence['boundary_guard']['active_depth']==0
            negatives.append({'case':label,'rejected':True,'reason':str(error),
                'actual_core_calls':delta,'call_interval':[first_call,len(CALLS)],
                'failed_replay_evidence':evidence})
        else:raise AssertionError(label+' accepted')
    for label,mutate in (
        ('wrong_own_source',lambda c:c.update(source_sha256='0'*64)),
        ('wrong_trace_source',lambda c:c.update(trace_bank_source_sha256='0'*64)),
        ('wrong_guard_contract',lambda c:c.update(guard_contract='NONE')),
        ('wrong_selected_word',lambda c:c['steps'][1]['selected_ids'].append(4)),
        ('wrong_charge',lambda c:c['steps'][0].update(charge='1/9')),
        ('bool_history',lambda c:c['history'].__setitem__(0,True))):
        bad=deepcopy(cursor);mutate(bad)
        reject(label,lambda:BoundaryCheckedSOTrace.restore(p,bad,certificate_bank=new_bank))
    reject('old_boundary_cursor',lambda:BoundaryCheckedSOTrace.restore(
        p,fixtures[0]['old_boundary']['cursor'],certificate_bank=new_bank))
    assert len(negatives)==7
    type_negatives_start=len(negatives)
    reject('old_bank_at_constructor',lambda:BoundaryCheckedSOTrace(p,F(1,3),certificate_bank=old_bank),zero=True)
    def substitute_old_bank():
        original=target.word_certificates;target.word_certificates=old_bank
        try:target.cursor()
        finally:target.word_certificates=original
    reject('old_bank_at_outer_entry',substitute_old_bank,zero=True)
    clean(target)
    CONTEXT['stage']='query_budget_rollback_and_same_bit_retry'
    interrupted=BoundaryCheckedSOTrace(p,F(1,3),query_budget=2,certificate_bank=new_bank)
    try:interrupted.advance(1)
    except QueryBudgetExhausted:
        clean(interrupted)
        assert interrupted.history==() and not interrupted.steps and interrupted.pending is not None
        failed_attempt=deepcopy(interrupted.evidence())
    else:raise AssertionError('expected bounded query interruption')
    interrupted.query_budget=1000;interrupted.advance(1)
    fresh=BoundaryCheckedSOTrace(p,F(1,3),certificate_bank=new_bank);fresh.advance(1)
    assert strict_bytes(interrupted.cursor())==strict_bytes(fresh.cursor())
    assert interrupted.mass()==fresh.mass()
    clean(interrupted);clean(fresh)
    retry={'failed_attempt':failed_attempt,'retried':deepcopy(interrupted.evidence()),
        'fresh':deepcopy(fresh.evidence()),'same_bit_committed_once':True}
    CONTEXT['stage']='serialize_success'
    assert source==hashes()
    payload={'schema':'BRC_SO_TRACE_POLICY_BOUNDED_PREFIX_EXECUTION_V1','status':'PASSED',
        'source_hashes':source,'vendor':vendor,'native_bank_binding':native_binding,
        'initial_program_admission_call_interval':[first,initial_admission_end],
        'old_cold_bank':old_bank.evidence(),'new_cold_bank':new_bank.evidence(),
        'fixtures':fixtures,'pending_restore':resume,
        'cursor_negative_controls':negatives[:type_negatives_start],
        'new_exact_bank_type_controls':negatives[type_negatives_start:],
        'budget_recovery':retry,
        'program_final_tables':[{'N':p.N,'a':p.a,'phase_bindings':p.phase_bindings,
            'codec_binding':p.codec_binding,'H4_binding':p.h4_binding,
            'permutation_verifications':p.lazy_permutation_verifications,
            'factory_tables':[t.export_certificate() for t in p.lazy_factory.tables.values()]}
            for p in programs],
        'actual_core_calls':CALLS[first:],'core_call_count':len(CALLS)-first,
        'elapsed_seconds':perf_counter()-start,
        'scope':'BOUNDED_FIXED_POSITIVE_PREFIXES; NO_FULL_LAW_OR_MATCHED_TIMING_CLAIM'}
    raw=packed(payload);out.write_bytes(gzip.compress(raw,mtime=0))
    summary={'status':'PASSED','source_hashes':source,'fixtures':2,'positive_steps':8,
        'cursor_negative_controls':7,'new_exact_bank_type_controls':2,
        'strict_pending_restore':True,'budget_rollback_same_bit_retry':True,
        'full_saved_covariances_and_observer_streams_equal':True,
        'core_call_count':payload['core_call_count'],'elapsed_seconds':payload['elapsed_seconds'],
        'raw_sha256':hashlib.sha256(raw).hexdigest(),'raw_bytes':len(raw),
        'gzip_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'gzip_bytes':out.stat().st_size,
        'scope':payload['scope']}
    (ROOT/'SO_TRACE_POLICY_SUMMARY.json').write_bytes(packed(summary))
    print(packed(summary).decode(),flush=True);CONTEXT['stage']='complete'


if __name__=='__main__':
    first=len(CALLS);initial_sources=hashes()
    try:main()
    except BaseException as error:
        failure={'schema':'BRC_SO_TRACE_POLICY_FAILED_EXECUTION_V1','status':'FAILED',
            'source_hashes_at_start':initial_sources,'source_hashes_at_failure':hashes(),
            'known_context':dict(CONTEXT),'exception_type':type(error).__name__,
            'exception_message':str(error),'traceback':traceback.format_exc(),
            'attached_exception_evidence':getattr(error,'evidence',None),
            'call_interval':[first,len(CALLS)],'actual_core_calls':CALLS[first:]}
        path=ROOT/('FAILED_EXECUTION_'+uuid4().hex+'.json.gz')
        with path.open('xb') as handle:handle.write(gzip.compress(packed(failure),mtime=0))
        print('FAILED execution evidence saved: '+str(path),file=sys.stderr,flush=True)
        raise
