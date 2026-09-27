"""Bounded actual-prefix/transaction checks; no full-law or timing benchmark."""
from copy import deepcopy
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import gzip
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]
sys.path.insert(0,str(BASE/'sep26-shor-general/optimization/collision_analysis'))
from check_gram_sampler import load_bank,LazyStreamingProgram,ExactCarrierCodec,verify_vendor
from boundary_uniform import (BoundaryCheckedUniform,UniformFeedbackGram,WordCertificateBank,
                              packed,strict_bytes,CursorReplayError,UNIFORM_SHA,WORDS_SHA)
from gram_sampler import QueryBudgetExhausted
from stage45.brc_loop_recheck import CALLS


def source_hashes():
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (
        Path(__file__),ROOT/'boundary_uniform.py',
        BASE/'sep27-qft-uniform/uniform_execution/uniform_feedback.py',
        BASE/'sep27-qft-uniform/word_certificates/word_certificates.py')}


def semantic_cursor(cursor):
    # Version/source/policy differ deliberately. Keep the entire executed word
    # ledger, charges, pending certificate and immutable program/bank binding.
    return {k:cursor[k] for k in ('epsilon','history','steps',
        'pending_certificate_sha256','program_sha256','certificate_bank_sha256')}


def clean_boundary(obj):
    assert obj._guard_depth==0 and obj._guard_owner is None


def main():
    guard=json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    hashes=source_hashes()
    first,start=len(CALLS),perf_counter()
    vendor=verify_vendor(); bank,bank_source=load_bank()
    programs=[]; fixtures=[]; certificates=None
    for a in (2,4):
        program=LazyStreamingProgram(21,a,4,bank,61,
                    codec=ExactCarrierCodec(61,tuple(range(6))))
        programs.append(program)
        if certificates is None:
            certificates=WordCertificateBank(program)
        old=UniformFeedbackGram(program,F(1,3),certificate_bank=certificates)
        new=BoundaryCheckedUniform(program,F(1,3),certificate_bank=certificates)
        checks=[]
        for bit in (1,0,0,0):
            depth=len(new.history)
            old_plan,new_plan=old.probabilities(),new.probabilities()
            assert old_plan==new_plan and old_plan['child_masses'][bit]>0
            assert old.pending==new.pending
            assert old.gamma(depth,1)==new.gamma(depth,1)
            assert old.advance(bit)==new.advance(bit)
            assert old.mass()==new.mass()
            assert semantic_cursor(old.cursor())==semantic_cursor(new.cursor())
            clean_boundary(new)
            checks.append({'depth':depth,'selected_bit':bit,'probabilities_equal':True,
                'full_signed_covariance_equal':True,'pending_decision_equal':True,
                'selected_child_positive':True,'raw_mass_equal':True,'word_ledger_equal':True})
        assert old.evidence()['inherited']['correlations']==new.evidence()['inherited']['correlations']
        fixtures.append({'N':21,'a':a,'t':4,'selected_history':[1,0,0,0],
            'checks':checks,'old':old.evidence(),'boundary':new.evidence(),
            'old_cursor_byte_equal_to_new':strict_bytes(old.cursor())==strict_bytes(new.cursor())})
        assert fixtures[-1]['old_cursor_byte_equal_to_new'] is False

    p=programs[0]
    target=BoundaryCheckedUniform(p,F(1,3),certificate_bank=certificates)
    for bit in (1,0,0):target.advance(bit)
    target.prepare_next()
    # Host-edited malformed metadata/input fixtures. These edits are never used
    # for numerical propagation: all must reject before any native observer.
    methods={
        'gamma':lambda:target.gamma(3,1),'mass':target.mass,
        'probabilities':target.probabilities,'advance':lambda:target.advance(0),
        'prepare_next':target.prepare_next,'cursor':target.cursor,
        'evidence':target.evidence,'report':target.report}
    controls=[]
    for name,invoke in methods.items():
        for mutation in ('strict_metadata_type','word','column','codec','history'):
            gate=p.bank[3]
            if mutation=='strict_metadata_type':
                saved=p.phase_bindings['3']['all_columns_orthonormal']
                assert saved is True
                p.phase_bindings['3']['all_columns_orthonormal']=1
                def undo():p.phase_bindings['3']['all_columns_orthonormal']=saved
            elif mutation=='word':
                p.bank[3]=replace(gate,inverse_phase_word=gate.inverse_phase_word+(('neg',0),))
                def undo():p.bank[3]=gate
            elif mutation=='column':
                first_column=(gate.columns[0][0]+1,)+gate.columns[0][1:]
                p.bank[3]=replace(gate,columns=(first_column,)+gate.columns[1:])
                def undo():p.bank[3]=gate
            elif mutation=='codec':
                saved=p.codec;p.codec=ExactCarrierCodec(61,tuple(range(5)))
                def undo():p.codec=saved
            else:
                saved=target.history;target.history=(0,)
                def undo():target.history=saved
            calls_before=len(CALLS); obs_before=len(target.observer.operations)
            try:
                try:invoke()
                except ValueError as error:
                    reason=str(error)
                else:raise AssertionError(name+' accepted '+mutation)
            finally:undo()
            clean_boundary(target)
            assert len(CALLS)==calls_before and len(target.observer.operations)==obs_before
            controls.append({'public_entry':name,'mutation':mutation,'rejected':True,
                'reason':reason,'native_calls_before_rejection':0,
                'observer_calls_before_rejection':0,'guard_depth_restored':True})
    assert target.history==(1,0,0)
    target_state_after_rejections=deepcopy(target.evidence())

    cursor=json.loads(strict_bytes(target.cursor()))
    resumed=BoundaryCheckedUniform.restore(p,cursor,certificate_bank=certificates)
    assert strict_bytes(resumed.cursor())==strict_bytes(cursor)
    assert target.advance(0)==resumed.advance(0)
    assert strict_bytes(target.cursor())==strict_bytes(resumed.cursor())
    clean_boundary(resumed);clean_boundary(target)
    resume={'input_cursor':cursor,'original':target.evidence(),'restored':resumed.evidence(),
            'strict_new_cursor_replay_passed':True,'RNG_or_cache_restored':False}
    negatives=[]
    for name,change in (
        ('wrong_source',lambda c:c.update(source_sha256='0'*64)),
        ('wrong_uniform_source',lambda c:c.update(uniform_source_sha256='0'*64)),
        ('wrong_guard_contract',lambda c:c.update(guard_contract='UNGUARDED')),
        ('wrong_selected_word',lambda c:c['steps'][1]['selected_ids'].append(4)),
        ('wrong_charge',lambda c:c['steps'][0].update(charge='1/9')),
        ('bool_history',lambda c:c['history'].__setitem__(0,True))):
        bad=deepcopy(cursor);change(bad)
        before=len(CALLS)
        try:BoundaryCheckedUniform.restore(p,bad,certificate_bank=certificates)
        except ValueError as error:
            ev=getattr(error,'evidence',None)
            if ev is not None:assert ev['boundary_guard']['active_depth']==0
            negatives.append({'case':name,'rejected':True,'reason':str(error),
                'actual_core_calls_delta':len(CALLS)-before,'actual_failed_replay_evidence':ev})
        else:raise AssertionError(name+' accepted')
    old_cursor=fixtures[0]['old']['cursor']
    try:BoundaryCheckedUniform.restore(p,old_cursor,certificate_bank=certificates)
    except CursorReplayError as error:
        assert error.evidence['boundary_guard']['active_depth']==0
        negatives.append({'case':'old_stage_cursor','rejected':True,
            'reason':str(error),'actual_failed_replay_evidence':error.evidence})
    else:raise AssertionError('old-stage cursor was silently accepted')

    interrupted=BoundaryCheckedUniform(p,F(1,3),query_budget=2,certificate_bank=certificates)
    try:interrupted.advance(1)
    except QueryBudgetExhausted:
        clean_boundary(interrupted)
        assert interrupted.history==() and not interrupted.steps and interrupted.pending is not None
        # Evidence is itself a guarded public operation after unwinding.
        failed_attempt=deepcopy(interrupted.evidence())
        assert failed_attempt['boundary_guard']['active_depth']==0
    else:raise AssertionError('predeclared query budget did not interrupt')
    interrupted.query_budget=1000
    interrupted.advance(1)
    fresh=BoundaryCheckedUniform(p,F(1,3),certificate_bank=certificates);fresh.advance(1)
    assert strict_bytes(interrupted.cursor())==strict_bytes(fresh.cursor())
    assert interrupted.mass()==fresh.mass()
    clean_boundary(interrupted);clean_boundary(fresh)
    recovery={'failed_attempt':failed_attempt,'retried':interrupted.evidence(),
              'fresh':fresh.evidence(),'same_bit_commits_once':True}
    assert source_hashes()==hashes
    record={'schema':'BRC_BOUNDARY_UNIFORM_PREFIX_PRECHECK_V1','source_hashes':hashes,
        'vendor':vendor,'bank_source':bank_source,'cold_word_certificate':certificates.evidence(),
        'fixtures':fixtures,'public_mutation_rejections':controls,
        'after_rejections':target_state_after_rejections,'resume':resume,
        'serialized_negative_controls':negatives,'budget_recovery':recovery,
        'programs':[{'N':x.N,'a':x.a,'phase_bindings':x.phase_bindings,
            'codec_binding':x.codec_binding,'H4_binding':x.h4_binding,
            'permutation_verifications':x.lazy_permutation_verifications,
            'factory_tables':[t.export_certificate() for t in x.lazy_factory.tables.values()]}
            for x in programs],
        'actual_native_core_calls':CALLS[first:],'elapsed_seconds':perf_counter()-start,
        'scope':'AUTHOR_ACTUAL_BOUNDED_PREFIX_TRANSACTIONS; NO_FULL_LAW_OR_TIMING_BENCHMARK'}
    raw=packed(record);out=ROOT/'BOUNDARY_PRECHECK_RESULTS.json.gz'
    if out.exists():raise ValueError('refusing to replace precheck execution evidence')
    out.write_bytes(gzip.compress(raw,mtime=0))
    summary={'schema':record['schema'],'source_hashes':hashes,'fixtures':2,'positive_prefix_steps':8,
        'public_entry_mutation_rejections':len(controls),'serialized_negative_controls':len(negatives),
        'strict_new_cursor_restore':True,'rollback_depth_and_same_bit_retry':True,
        'native_core_calls':len(CALLS)-first,'elapsed_seconds':record['elapsed_seconds'],
        'raw_sha256':hashlib.sha256(raw).hexdigest(),'raw_bytes':len(raw),
        'gzip_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'gzip_bytes':out.stat().st_size,
        'scope':record['scope']}
    (ROOT/'BOUNDARY_PRECHECK_SUMMARY.json').write_bytes(packed(summary))
    print(packed(summary).decode(),flush=True)


if __name__=='__main__':main()
