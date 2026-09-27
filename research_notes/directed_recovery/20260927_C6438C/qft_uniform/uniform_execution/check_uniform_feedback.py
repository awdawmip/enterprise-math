"""Predeclared complete bounded laws for the reusable actual-word policy."""
from copy import deepcopy
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from time import perf_counter
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
sys.path.insert(0, str(BASE/'sep27-qft-adaptive/adaptive_execution'))
from check_adaptive_feedback import (load_bank, ExactCarrierCodec, LazyStreamingProgram,
    scalar, covariance, mass, child, PositivePathObserver, CALLS, verify_vendor, QueryBudgetExhausted)
from uniform_feedback import UniformFeedbackGram, WordCertificateBank, packed, strict_bytes


def actual_law(program, epsilon, certificates):
    law, receipts, checks = {}, [], []
    observer = PositivePathObserver()
    first_calls = len(CALLS)
    for history in product((0,1), repeat=program.t):
        gram = UniformFeedbackGram(program, epsilon, certificate_bank=certificates)
        rows, den = {1:(1,)+(0,)*(program.dim-1)}, 1
        reached = True
        for i, bit in enumerate(history):
            before = mass(rows, den, observer)
            if not before:
                reached = False
                break
            plan = gram.probabilities()
            decision = gram.pending
            assert plan['parent_mass'] == before
            cov = gram.gamma(i,1)
            assert tuple(tuple(F(v,cov.den) for v in row) for row in cov.rows) == covariance(rows,den,program.dim,observer)
            assert not decision['prefix_covariance_defect_observed']
            assert not decision['prefix_mass_observed_for_policy']
            next_rows,next_den = child(program,rows,den,i,decision['selected_ids'],bit,observer)
            assert mass(next_rows,next_den,observer) == plan['child_masses'][bit]
            checks.append({'history':history[:i], 'bit':bit, 'decision':decision['decision'],
                'mass':before, 'all_signed_covariance_entries_equal':True,
                'child_mass_equal':True, 'word_certificate_sha256':decision['word_certificate_sha256']})
            if not plan['child_masses'][bit]:
                reached = False
                break
            gram.advance(bit)
            rows,den = next_rows,next_den
        receipts.append(gram.evidence())
        if reached:
            for w,row in rows.items():
                value = mass({w:row},den,observer)
                if value:
                    law[(history,w)] = value
    total = scalar(observer,'terminal_law_total',((v,) for v in law.values()))
    assert total == 1
    return law, {'epsilon':str(epsilon), 'checks':checks, 'gram_executions':receipts,
        'explicit_observer_operations':observer.operations, 'terminal_mass':total,
        'actual_core_calls_delta':len(CALLS)-first_calls,
        'law':[{'history':h,'work':w,'mass':v} for (h,w),v in sorted(law.items())]}


def law_from_record(route):
    return {(tuple(x['history']),x['work']):F(x['mass']) for x in route['law']}


def tv_of(low, reference, observer, label):
    diffs = [scalar(observer,label+'_atom',((low.get(k,F(0)),),(-F(1),reference.get(k,F(0)))))
             for k in sorted(set(low)|set(reference))]
    return scalar(observer,label+'_tv',((abs(v),F(1,2)) for v in diffs if v))


def main():
    guard = json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    old_path = BASE/'sep27-qft-adaptive/adaptive_execution/ADAPTIVE_FEEDBACK_RESULTS.json.gz'
    old_bytes = old_path.read_bytes()
    old_sha = hashlib.sha256(old_bytes).hexdigest()
    assert old_sha == '36a6460fbda4d081d1416bbfa48fa0fd641f96d0df235d2d168a7ac06aa5a9c0'
    old = json.loads(gzip.decompress(old_bytes))
    sources = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (
        Path(__file__),ROOT/'uniform_feedback.py',ROOT.parent/'word_certificates/word_certificates.py',
        BASE/'sep27-qft-adaptive/adaptive_execution/check_adaptive_feedback.py')}
    first, started = len(CALLS), perf_counter()
    vendor = verify_vendor()
    bank, bank_source = load_bank()
    cases, full, programs = [], [], []
    certificate_bank = None
    certificate_setup = None
    for index,(N,a) in enumerate(((21,2),(21,4),(65,3),(15,2))):
        program = LazyStreamingProgram(N,a,4,bank,61,codec=ExactCarrierCodec(61,tuple(range(6))))
        programs.append(program)
        if certificate_bank is None:
            setup_start, setup_first = perf_counter(), len(CALLS)
            certificate_bank = WordCertificateBank(program)
            certificate_setup = {'elapsed_seconds':perf_counter()-setup_start,
                'actual_core_calls_delta':len(CALLS)-setup_first,
                'evidence':certificate_bank.evidence(), 'purpose':'ONE_SHARED_COLD_ADMISSION'}
        certificate_bank.check(program)
        low, le = actual_law(program,F(1,3),certificate_bank)
        reference, re = actual_law(program,F(0),certificate_bank)
        old_case = old['cases'][index]
        assert old_case['summary']['N'] == N and old_case['summary']['a'] == a
        assert reference == law_from_record(old_case['reference'])
        old_low = law_from_record(old_case['low'])
        observer = PositivePathObserver()
        tv = tv_of(low,reference,observer,'uniform_vs_reference')
        policy_tv = tv_of(low,old_low,observer,'uniform_vs_previous_adaptive')
        assert tv <= F(1,3)
        accepted = sum(g['policy_stats']['accepted_omissions'] for g in le['gram_executions'])
        case = {'N':N,'a':a,'t':4,'epsilon':F(1,3),'joint_history_work_tv':tv,
            'joint_tv_vs_frozen_state_specific_policy':policy_tv,
            'reference_law_equal_frozen_reference':True,
            'complete_laws_normalized':True,'joint_tv_within_budget':True,
            'accepted_omission_occurrences_in_replayed_leaf_runs':accepted,
            'prefix_checks':len(le['checks'])+len(re['checks']),
            'low_joint_atoms':len(low),'reference_joint_atoms':len(reference)}
        cases.append(case)
        full.append({'summary':case,'low':le,'reference':re,'tv_observer':observer.operations})
        print(packed(case).decode(),flush=True)
    program = programs[0]
    original = UniformFeedbackGram(program,F(1,3),certificate_bank=certificate_bank)
    original.advance(1);original.advance(0);original.advance(0)
    original.prepare_next()
    cursor = json.loads(strict_bytes(original.cursor()))
    resumed = UniformFeedbackGram.restore(program,cursor,certificate_bank=certificate_bank)
    assert strict_bytes(resumed.cursor()) == strict_bytes(original.cursor())
    assert resumed.probabilities() == original.probabilities()
    original.advance(0);resumed.advance(0)
    assert strict_bytes(resumed.cursor()) == strict_bytes(original.cursor()) and resumed.mass() == original.mass()
    # Cross-process-style cold restore really reconstructs and charges the bank.
    cold_start,cold_first = perf_counter(),len(CALLS)
    cold = UniformFeedbackGram.restore(program,cursor)
    cold_elapsed,cold_calls = perf_counter()-cold_start,len(CALLS)-cold_first
    assert strict_bytes(cold.cursor()) == strict_bytes(cursor)
    negative = []
    for label,change in (
        ('wrong_selected_word',lambda c:c['steps'][1]['selected_ids'].append(4)),
        ('wrong_charge',lambda c:c['steps'][0].update(charge='1/9')),
        ('wrong_certificate',lambda c:c['steps'][0].update(certificate_sha256='0'*64)),
        ('wrong_pending',lambda c:c.update(pending_certificate_sha256='0'*64)),
        ('wrong_program',lambda c:c.update(program_sha256='0'*64)),
        ('wrong_source',lambda c:c.update(source_sha256='0'*64)),
        ('wrong_bank',lambda c:c.update(certificate_bank_sha256='0'*64)),
        ('wrong_parent_source',lambda c:c.update(parent_source_sha256='0'*64)),
        ('bool_history',lambda c:c['history'].__setitem__(0,True)),
        ('extra_field',lambda c:c.update(uncommitted=True))):
        bad = deepcopy(cursor);change(bad)
        before = len(CALLS)
        try:
            UniformFeedbackGram.restore(program,bad,certificate_bank=certificate_bank)
        except ValueError as error:
            negative.append({'case':label,'rejected':True,'reason':str(error),
                'actual_core_calls_delta':len(CALLS)-before,
                'actual_failed_replay_evidence':getattr(error,'evidence',None)})
        else:raise AssertionError(label+' was accepted')
    stale = UniformFeedbackGram(program,0,certificate_bank=certificate_bank);stale.history=(1,)
    try:stale.mass()
    except ValueError as error:negative.append({'case':'uncommitted_history','rejected':True,'reason':str(error)})
    else:raise AssertionError('uncommitted history accepted')
    mutable = UniformFeedbackGram(program,0,certificate_bank=certificate_bank)
    saved = program.a
    program.a = 3
    try:
        try:mutable.mass()
        except ValueError as error:negative.append({'case':'changed_program','rejected':True,'reason':str(error)})
        else:raise AssertionError('changed program accepted')
    finally:program.a=saved
    interrupted = UniformFeedbackGram(program,F(1,3),query_budget=2,certificate_bank=certificate_bank)
    try:interrupted.advance(1)
    except QueryBudgetExhausted:
        assert interrupted.history == () and not interrupted.steps and interrupted.pending is not None
        interrupted_cursor = interrupted.cursor()
    else:raise AssertionError('declared resource interruption did not occur')
    interrupted.query_budget = 1000
    interrupted.advance(1)
    fresh = UniformFeedbackGram(program,F(1,3),certificate_bank=certificate_bank);fresh.advance(1)
    assert strict_bytes(interrupted.cursor()) == strict_bytes(fresh.cursor()) and interrupted.mass() == fresh.mass()
    record = {'schema':'BRC_UNIFORM_FEEDBACK_CHECK_V1','source_hashes':sources,
        'frozen_comparator_gzip_sha256':old_sha,'bank_source':bank_source,'vendor':vendor,
        'certificate_setup':certificate_setup,'certificate_bank_final':certificate_bank.evidence(),
        'cases':full,'programs':[{'phase_bindings':p.phase_bindings,'codec_binding':p.codec_binding,
            'native_two_H4':p.h4_binding,'permutation_verifications':p.lazy_permutation_verifications,
            'tables':[t.export_certificate() for t in p.lazy_factory.tables.values()]} for p in programs],
        'resume':{'input_cursor':cursor,'original':original.evidence(),'resumed':resumed.evidence(),
            'exact_pending_and_terminal_match':True,'RNG_restored':False,
            'cold_replay':cold.evidence(),'cold_elapsed_seconds':cold_elapsed,'cold_actual_core_calls':cold_calls},
        'negative_controls':negative,'actual_native_core_calls':CALLS[first:],
        'interruption_recovery':{'interrupted_cursor':interrupted_cursor,'retried':interrupted.evidence(),
            'fresh':fresh.evidence(),'same_bit_retry_commits_exactly_once':True},
        'elapsed_seconds':perf_counter()-started,
        'scope':'AUTHOR_EXECUTED_BOUNDED_REUSABLE_WORD_CERTIFICATE; NOT_POLYNOMIAL_DEQUANTIZATION'}
    raw = packed(record)
    output = ROOT/'UNIFORM_FEEDBACK_RESULTS.json.gz'
    if output.exists():raise ValueError('refusing to replace scientific raw output')
    output.write_bytes(gzip.compress(raw,mtime=0))
    summary = {'schema':record['schema'],'source_hashes':sources,'cases':cases,
        'negative_controls_rejected':len(negative),'serialized_cursor_replay_passed':True,
        'budget_interruption_rollback_and_retry_passed':True,'raw_bytes':len(raw),
        'raw_sha256':hashlib.sha256(raw).hexdigest(),'gzip_bytes':output.stat().st_size,
        'gzip_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
        'actual_native_core_calls':len(CALLS)-first,'elapsed_seconds':record['elapsed_seconds']}
    (ROOT/'UNIFORM_FEEDBACK_SUMMARY.json').write_bytes(packed(summary))
    print(packed(summary).decode(),flush=True)


if __name__ == '__main__':
    main()
