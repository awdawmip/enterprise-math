"""Predeclared finite actual-native witnesses; no ideal or RP1 reference run."""
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
sys.path.insert(0,str(BASE/'sep26-shor-general/optimization/collision_analysis'))
from check_gram_sampler import load_bank, ExactCarrierCodec, LazyStreamingProgram, observed_zero_shift
from adaptive_feedback import AdaptiveFeedbackGram, packed, strict_bytes
from certified_word_compiler import PositivePathObserver
from stage45.brc_loop_recheck import CALLS, verify_vendor
from gram_sampler import QueryBudgetExhausted


def vector_action(program, row, ids):
    den = 1
    for m in ids:
        word = program.bank[m]
        row = tuple(word.apply_numer(row))
        den *= word.den
    return row,den


def scalar(observer,label,terms):
    terms = tuple(terms)
    return observer.evaluate(label,terms) if terms else F(0)


def covariance(rows,den,dim,observer):
    return tuple(tuple(scalar(observer,'explicit_complete_covariance',
        ((F(row[j],den),F(row[k],den)) for row in rows.values() if row[j] and row[k]))
        for k in range(dim)) for j in range(dim))


def mass(rows,den,observer):
    return scalar(observer,'explicit_raw_mass',
        ((F(v,den),F(v,den)) for row in rows.values() for v in row if v))


def child(program, rows, den, depth, ids, bit, observer):
    """Independent explicit signed native two-H4 boundary, with actual typed P."""
    buckets = {}
    sign = F(1 if bit==0 else -1)
    for w,row in rows.items():
        target = program.tables[depth][w]
        transformed,gd = vector_action(program,row,ids)
        for j in range(program.dim):
            if row[j]:
                buckets.setdefault((w,j),[]).append((F(row[j],den),F(1,2)))
            if transformed[j]:
                buckets.setdefault((target,j),[]).append((sign,F(transformed[j],den*gd),F(1,2)))
    observed = {k:scalar(observer,'explicit_selected_native_child',v) for k,v in buckets.items()}
    common = max((v.denominator for v in observed.values()),default=1)
    out = {}
    for (w,j),value in observed.items():
        if value:
            out.setdefault(w,[0]*program.dim)[j] = value.numerator*(common//value.denominator)
    return {w:tuple(row) for w,row in out.items()},common


def direct_defect(program,rows,den,reference,selected,observer):
    diffs = []
    for row in rows.values():
        tr,td = vector_action(program,row,reference)
        sr,sd = vector_action(program,row,selected)
        diffs.append(tuple(scalar(observer,'explicit_signed_gate_difference',
            ((F(tr[j],den*td),),(-F(1),F(sr[j],den*sd)))) for j in range(program.dim)))
    return tuple(tuple(scalar(observer,'explicit_full_defect_covariance',
        ((row[j],row[k]) for row in diffs if row[j] and row[k]))
        for k in range(program.dim)) for j in range(program.dim))


def actual_law(program,epsilon):
    law,receipts,checks = {},[],[]
    observer = PositivePathObserver()
    first_calls = len(CALLS)
    for history in product((0,1),repeat=program.t):
        gram = AdaptiveFeedbackGram(program,epsilon)
        rows,den = {1:(1,)+(0,)*(program.dim-1)},1
        reached = True
        for i,bit in enumerate(history):
            before = mass(rows,den,observer)
            if not before:
                reached = False
                break
            plan = gram.probabilities()
            decision = gram.pending
            assert plan['parent_mass'] == before
            cov = gram.gamma(i,1)
            assert tuple(tuple(F(v,cov.den) for v in row) for row in cov.rows)==covariance(rows,den,program.dim,observer)
            if decision['candidate_defect'] is not None:
                d = decision['candidate_defect']
                actual = tuple(tuple(F(v,d['den']) for v in row) for row in d['rows'])
                assert actual == direct_defect(program,rows,den,decision['reference_ids'],decision['candidate_ids'],observer)
            next_rows,next_den = child(program,rows,den,i,decision['selected_ids'],bit,observer)
            assert mass(next_rows,next_den,observer) == plan['child_masses'][bit]
            checks.append({'history':history[:i],'bit':bit,'decision':decision['decision'],
                'mass':before,'all_signed_covariance_entries_equal':True,
                'all_signed_candidate_defect_entries_equal':decision['candidate_defect'] is not None,
                'child_mass_equal':True})
            if not plan['child_masses'][bit]:
                reached=False
                break
            gram.advance(bit)
            rows,den=next_rows,next_den
        receipts.append(gram.evidence())
        if reached:
            for w,row in rows.items():
                value = mass({w:row},den,observer)
                if value:
                    law[(history,w)]=value
    total = scalar(observer,'terminal_law_total',((v,) for v in law.values()))
    assert total == 1
    return law,{'epsilon':str(epsilon),'checks':checks,'gram_executions':receipts,
        'explicit_observer_operations':observer.operations,'terminal_mass':total,
        'actual_core_calls_delta':len(CALLS)-first_calls,
        'law':[{'history':h,'work':w,'mass':v} for (h,w),v in sorted(law.items())]}


def main():
    guard=json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in (ROOT/'adaptive_feedback.py',Path(__file__))}
    first,started=len(CALLS),perf_counter()
    kernel=verify_vendor()
    bank,bank_source=load_bank()
    cases=[]
    full=[]
    programs=[]
    for N,a in ((21,2),(21,4),(65,3),(15,2)):
        program=LazyStreamingProgram(N,a,4,bank,61,
            codec=ExactCarrierCodec(61,tuple(range(6))))
        programs.append(program)
        low,le=actual_law(program,F(1,3))
        reference,re=actual_law(program,F(0))
        observer=PositivePathObserver()
        differences=[scalar(observer,'joint_atom_difference',((low.get(k,F(0)),),(-F(1),reference.get(k,F(0)))))
                     for k in sorted(set(low)|set(reference))]
        tv=scalar(observer,'joint_total_variation',((abs(v),F(1,2)) for v in differences if v))
        assert tv<=F(1,3)
        accepted=sum(g['policy_stats']['accepted_omissions'] for g in le['gram_executions'])
        case={'N':N,'a':a,'t':4,'epsilon':F(1,3),'joint_history_work_tv':tv,
            'complete_laws_normalized':True,'joint_tv_within_budget':True,
            'accepted_omission_occurrences_in_replayed_leaf_runs':accepted,
            'prefix_checks':len(le['checks'])+len(re['checks']),
            'low_joint_atoms':len(low),'reference_joint_atoms':len(reference)}
        cases.append(case)
        full.append({'summary':case,'low':le,'reference':re,'tv_observer':observer.operations})
        print(json.dumps({**case,'epsilon':str(case['epsilon']),'joint_history_work_tv':str(tv)}),flush=True)
    assert any(x['accepted_omission_occurrences_in_replayed_leaf_runs'] for x in cases)
    # Pending and committed decisions replay from a serialized public-prefix cursor.
    program=programs[0]
    original=AdaptiveFeedbackGram(program,F(1,3))
    original.advance(1);original.advance(0);original.advance(0)
    original.prepare_next()
    cursor=json.loads(strict_bytes(original.cursor()))
    resumed=AdaptiveFeedbackGram.restore(program,cursor)
    assert resumed.cursor()==original.cursor()
    assert resumed.probabilities()==original.probabilities()
    original.advance(0);resumed.advance(0)
    assert resumed.cursor()==original.cursor() and resumed.mass()==original.mass()
    negative=[]
    for label,change in (
        ('wrong_selected_word',lambda c:c['steps'][1]['selected_ids'].append(4)),
        ('wrong_charge',lambda c:c['steps'][0].update(charge='1/9')),
        ('wrong_certificate',lambda c:c['steps'][0].update(certificate_sha256='0'*64)),
        ('wrong_pending',lambda c:c.update(pending_certificate_sha256='0'*64)),
        ('wrong_program',lambda c:c.update(program_sha256='0'*64)),
        ('wrong_source',lambda c:c.update(source_sha256='0'*64)),
        ('bool_history',lambda c:c['history'].__setitem__(0,True)),
        ('extra_field',lambda c:c.update(uncommitted=True))):
        bad=deepcopy(cursor);change(bad)
        try:
            AdaptiveFeedbackGram.restore(program,bad)
        except ValueError as e:
            negative.append({'case':label,'rejected':True,'reason':str(e),
                'actual_failed_replay_evidence':getattr(e,'evidence',None)})
        else:raise AssertionError(label+' was accepted')
    stale=AdaptiveFeedbackGram(program,0);stale.history=(1,)
    try:stale.mass()
    except ValueError as e:negative.append({'case':'uncommitted_history','rejected':True,'reason':str(e)})
    else:raise AssertionError('uncommitted history accepted')
    mutable=AdaptiveFeedbackGram(program,0)
    saved=program.a
    program.a=3
    try:
        try:mutable.mass()
        except ValueError as e:negative.append({'case':'changed_program','rejected':True,'reason':str(e)})
        else:raise AssertionError('changed program accepted')
    finally:program.a=saved
    interrupted=AdaptiveFeedbackGram(program,F(1,3),query_budget=2)
    try:interrupted.advance(1)
    except QueryBudgetExhausted:
        assert interrupted.history == () and not interrupted.steps
        assert interrupted.pending is not None
        interrupted_cursor = interrupted.cursor()
    else:raise AssertionError('declared resource interruption did not occur')
    interrupted.query_budget=1000
    interrupted.advance(1)
    fresh=AdaptiveFeedbackGram(program,F(1,3));fresh.advance(1)
    assert interrupted.cursor()==fresh.cursor() and interrupted.mass()==fresh.mass()
    record={'schema':'BRC_ADAPTIVE_FEEDBACK_CHECK_V1','source_hashes':source_hashes,
        'bank_source':bank_source,'vendor':kernel,'cases':full,
        'programs':[{'phase_bindings':p.phase_bindings,'codec_binding':p.codec_binding,
            'native_two_H4':p.h4_binding,'permutation_verifications':p.lazy_permutation_verifications,
            'tables':[t.export_certificate() for t in p.lazy_factory.tables.values()]} for p in programs],
        'resume':{'input_cursor':cursor,'original':original.evidence(),'resumed':resumed.evidence(),
                  'exact_pending_and_terminal_match':True,'RNG_restored':False},
        'negative_controls':negative,'actual_native_core_calls':CALLS[first:],
        'interruption_recovery':{'interrupted_cursor':interrupted_cursor,
            'retried':interrupted.evidence(),'fresh':fresh.evidence(),
            'same_bit_retry_commits_exactly_once':True},
        'elapsed_seconds':perf_counter()-started,
        'scope':'AUTHOR_EXECUTED_BOUNDED_NATIVE_WORD_OMISSION; NOT_RP1_LOW_BIT_EXECUTION'}
    raw=packed(record)
    output=ROOT/'ADAPTIVE_FEEDBACK_RESULTS.json.gz'
    if output.exists():raise ValueError('refusing to replace scientific raw output')
    output.write_bytes(gzip.compress(raw,mtime=0))
    summary={'schema':record['schema'],'source_hashes':source_hashes,'cases':cases,
        'negative_controls_rejected':len(negative),'serialized_cursor_replay_passed':True,
        'budget_interruption_rollback_and_retry_passed':True,
        'raw_bytes':len(raw),'raw_sha256':hashlib.sha256(raw).hexdigest(),
        'gzip_bytes':output.stat().st_size,'gzip_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
        'actual_native_core_calls':len(CALLS)-first,'elapsed_seconds':record['elapsed_seconds']}
    (ROOT/'ADAPTIVE_FEEDBACK_SUMMARY.json').write_bytes(packed(summary))
    print(packed(summary).decode(),flush=True)


if __name__=='__main__':main()
