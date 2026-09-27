"""Actual joint-law, consecutive no-query, same-tape and resume checks."""
from __future__ import annotations
from collections import defaultdict
from dataclasses import asdict,is_dataclass
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json
import random
import sys

from power_sum_walker import PowerSumWalker
from power_sum_certificate import PREVIOUS
from single_walker import SingleWalker
from stage45.brc_loop_recheck import CALLS,verify_vendor
ROOT=Path(__file__).resolve().parent
for path in (PREVIOUS/'optimization/collision_analysis',PREVIOUS/'optimization/streaming'):
    sys.path.insert(0,str(path))
from check_gram_sampler import load_bank
from lazy_streaming import LazyStreamingProgram
from certified_word_compiler import PositivePathObserver


def clean(value):
    if is_dataclass(value): return clean(asdict(value))
    if isinstance(value,F): return {'numerator':value.numerator,'denominator':value.denominator}
    if isinstance(value,dict): return {str(k):clean(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [clean(v) for v in value]
    return value


def observe(observer,name,terms):
    terms=tuple(tuple(x) for x in terms if all(x))
    return observer.evaluate(name,terms) if terms else F(0)


def norms(observer,state):
    den=state['denominator']
    return {key[1]:observe(observer,'complete_actual_row_norm',
        ((F(x,den),F(x,den)) for x in row if x)) for key,row in state['rows'] if any(row)}


class RecordedRandom:
    def __init__(self,seed): self.rng,self.calls=random.Random(seed),[]
    def randrange(self,stop):
        value=self.rng.randrange(stop)
        self.calls.append({'stop':stop,'value':value})
        return value


class FiniteRandom:
    def __init__(self,values): self.values,self.calls=iter(values),[]
    def randrange(self,stop):
        value=0 if next(self.values)==0 else stop-1
        self.calls.append({'stop':stop,'value':value})
        return value


def event_key(events):
    keys=('history','latent_before','auxiliary_bit','candidate','selected_bit','selected_local_probability')
    return [tuple(e[k] for k in keys) for e in events]


def main():
    first=len(CALLS)
    kernel=verify_vendor()
    paths=(Path(__file__),ROOT/'power_sum_walker.py',ROOT/'power_sum_certificate.py')
    hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    raw=gzip.decompress((ROOT/'POWER_SUM_CERTIFICATE_RESULTS.json.gz').read_bytes())
    prior_hash=hashlib.sha256(raw).hexdigest()
    assert prior_hash=='1ab0f8a6c0b06d7495038e00be32fe434881c941e480a5049e8a1aa2664e400c'
    prior=json.loads(raw)
    bank,bank_source=load_bank()
    observer=PositivePathObserver()
    joint_checks,trajectories,restorations=[],[],[]
    for source in prior['actual_full_program_cases']:
        N,a,ell=source['N'],source['a'],source['ell']
        structure=source['certificate']['structure_witness']
        u,v=structure['u'],structure['v']
        program=LazyStreamingProgram(N,a,4,bank,61)
        terminal={}
        for prefix in source['complete_native_prefix_checks']:
            history=tuple(prefix['history']);depth=len(history)
            if depth==3:
                for bit,child in enumerate(prefix['children']): terminal[history+(bit,)]=child
            if not prefix['claimed_suffix']: continue
            parent=norms(observer,prefix['parent'])
            terms=defaultdict(list)
            for work,mass in parent.items():
                for auxiliary in (0,1):
                    candidate=work if auxiliary==0 else program.tables[depth][work]
                    for bit in (0,1): terms[(bit,candidate)].append((mass,F(1,2),F(1,2)))
            for bit,child in enumerate(prefix['children']):
                prediction={w:observe(observer,'two_fair_coins_joint_mass',value)
                    for (b,w),value in terms.items() if b==bit}
                expected=norms(observer,child)
                assert prediction==expected
                joint_checks.append({'N':N,'history':history+(bit,),
                    'all_child_work_label_masses_equal':True,'joint_masses':sorted(prediction.items())})
        for seed in (927101,927102,927103,927104):
            baseline=SingleWalker(program,query_budget=10000)
            optimized=PowerSumWalker(program,ell,u,v,query_budget=10000)
            left,right=RecordedRandom(seed),RecordedRandom(seed)
            b=baseline.run(left)
            before=None
            while len(optimized.history)<program.t:
                if len(optimized.history)==program.t-ell:
                    before=optimized.oracle.report()
                    optimized.oracle.query_budget=before['distinct_queries']
                optimized.step(right)
            after=optimized.oracle.report()
            assert optimized.shortcut_rounds==ell
            assert before['query_requests']==after['query_requests']
            assert before['distinct_queries']==after['distinct_queries']
            assert tuple(b['history'])==optimized.history and b['latent_work_label']==optimized.latent
            assert event_key(b['events'])==event_key(optimized.events) and left.calls==right.calls
            trajectories.append({'N':N,'ell':ell,'seed':seed,'same_report_and_latent_trajectory':True,
                'same_random_tape':True,'random_tape':right.calls,
                'before_suffix_oracle':before,'after_suffix_oracle':after,
                'optimized_events':optimized.events,'baseline':b,'optimization':optimized.report()})
            # Later recovery is explicitly charged and uses the original row
            # oracle with every reported bit still retained.
            optimized.oracle.query_budget=10000
            expected=terminal[optimized.history]
            for key,row in expected['rows']:
                actual=optimized.oracle.query(4,key[1])
                assert len(actual.values)==61
                assert all(x*expected['denominator']==y*actual.den for x,y in zip(actual.values,row))
            restorations.append({'N':N,'seed':seed,'history':optimized.history,
                'all_declared_terminal_rows_and_61_components_equal':True,
                'expected_complete_field':expected,'post_recovery_oracle':optimized.oracle.evidence()})

    # An unavailable witness follows the old row-query route exactly.
    fallback_program=LazyStreamingProgram(65,2,4,bank,61)
    ordinary=SingleWalker(fallback_program,query_budget=10000)
    fallback=PowerSumWalker(fallback_program,2,1,8,query_budget=10000)
    a_rng,b_rng=RecordedRandom(927200),RecordedRandom(927200)
    ar,br=ordinary.run(a_rng),fallback.run(b_rng)
    assert fallback.suffix_certificate['status']=='UNAVAILABLE' and fallback.shortcut_rounds==0
    assert event_key(ar['events'])==event_key(br['events']) and a_rng.calls==b_rng.calls

    # Pause after the proposal coin in the first of three certified rounds.
    program=LazyStreamingProgram(4097,3,4,bank,61)
    resumed=PowerSumWalker(program,3,8,1,query_budget=10000)
    resumed.step(RecordedRandom(927301))
    report=resumed.oracle.report();resumed.oracle.query_budget=report['distinct_queries']
    exhausted=FiniteRandom([1]);stopped=resumed.run(exhausted)
    assert stopped['status']=='INCOMPLETE_RANDOM_SOURCE' and len(resumed.history)==1
    assert resumed.pending_auxiliary_bit==1 and resumed.pending_plan['mode']=='CERTIFIED_POWER_SUM_SUFFIX'
    continuation=FiniteRandom([0,1,1,0,0]);done=resumed.run(continuation)
    assert done['status']=='COMPLETE_READOUT' and resumed.shortcut_rounds==3
    assert len(exhausted.calls)==1 and len(continuation.calls)==5
    assert resumed.oracle.report()['query_requests']==report['query_requests']
    before_bad=PowerSumWalker(program,3,8,1)
    before_bad.latent=3
    try: before_bad.step(RecordedRandom(1))
    except ValueError: bad_latent=True
    else: raise AssertionError('external latent injection accepted')
    changed=PowerSumWalker(program,3,8,1,query_budget=10000)
    changed.step(RecordedRandom(927301))
    changed.suffix_certificate['structure_witness']['ell']+=1
    changed.oracle.query_budget=changed.oracle.report()['distinct_queries']
    refusal=changed.run(FiniteRandom([0,0]))
    assert refusal['status']=='INCOMPLETE_POINT_QUERY_BUDGET' and changed.shortcut_rounds==0

    assert hashes=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    result={'status':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED','source_hashes':hashes,
        'kernel_verification':kernel,'prior_full_field_payload_sha256':prior_hash,
        'phase_bank_source':bank_source,'complete_joint_child_checks':joint_checks,
        'paired_trajectories':trajectories,'later_full_row_restorations':restorations,
        'unavailable_fallback':{'baseline':ar,'optimized':br,'same_random_tape':True},
        'live_resume':{'stopped':stopped,'completed':done,'saved_auxiliary_coin':True,
            'no_suffix_row_queries':True,'first_successful_random_calls':exhausted.calls,
            'remaining_successful_random_calls':continuation.calls},
        'external_latent_injection_rejected':bad_latent,'tampered_certificate_refusal':refusal,
        'joint_observer_operations':observer.operations,'native_core_calls':CALLS[first:],
        'ideal_reference_simulation':False,'factor_or_order_input':False,
        'large_power_sum_cases_not_instantiated_as_programs':True,
        'runtime_speedup_claimed':False}
    raw=json.dumps(clean(result),sort_keys=True,separators=(',',':')).encode()
    (ROOT/'POWER_SUM_WALKER_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    summary={'status':result['status'],'all_joint_children_checked':len(joint_checks),
        'same_tape_pairs':len(trajectories),'later_full_row_restorations':len(restorations),
        'certified_consecutive_lengths':[2,3],'all_suffix_point_queries_zero':True,
        'unavailable_fallback_equal':True,'live_rng_resume_preserved_auxiliary_coin':True,
        'tampered_certificate_refused_shortcut':True,'external_latent_rejected':True,
        'all_fixture_native_core_calls':len(CALLS)-first,'source_hashes':hashes,
        'payload_sha256':hashlib.sha256(raw).hexdigest()}
    (ROOT/'POWER_SUM_WALKER_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary))


if __name__=='__main__': main()
