"""Declared bounded full-D61 projected-row experiment, no ideal reference."""
from __future__ import annotations
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json
import random
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1]/'sep27-qft-research'
sys.path.insert(0,str(OLD/'gram_research'))
from check_single_walker import (load_bank, LazyStreamingProgram, SelectedStreamingProgram,
    serializable, packed, ScriptedRandom, CALLS, verify_vendor)
from projected_rows import (ProjectedRowOracle, ProjectedWalker, approximate_plan,
    train_envelope, validate_envelope, verify_validation, verify_envelope,
    observed, PositivePathObserver, digest, run_one_shot)


def state_norms(state,den,obs):
    return {key[1]:observed(obs,'actual_reference_row_norm',((F(x,den),F(x,den)) for x in row if x))
            for key,row in state.items() if any(row)}


def error_squared(oracle,state,den,obs):
    labels = set(oracle.rows)|{key[1] for key in state}
    terms=[]
    for label in sorted(labels):
        exact=state.get((0,label,0),(0,)*oracle.dim)
        approx=oracle.rows.get(label)
        for j,x in enumerate(exact):
            y=F(approx.values[j],approx.den) if approx else F(0)
            difference=observed(obs,'complete_signed_row_difference',((F(x,den),),(-y,)))
            if difference:
                terms.append((difference,difference))
    return observed(obs,'global_row_error_squared',terms)


def exhaustive_contract(program,explicit,envelope):
    obs=PositivePathObserver()
    initial,den=explicit.initial()
    frontier={(): (initial,den,{1:F(1)})}
    records=[]
    errors=[]
    missing=[]
    norms=[]
    terminal_true={}
    terminal_approx={}
    fallback_count=0
    residual=False
    query_count=0
    oracle_state_slots=[]
    for depth in range(program.t):
        following={}
        error_terms=[]
        missing_terms=[]
        mu_terms=defaultdict(list)
        for history,(state,den,joint) in frontier.items():
            oracle=ProjectedRowOracle(program,envelope,history)
            exactnorms=state_norms(state,den,obs)
            for label,mass in exactnorms.items():
                mu_terms[label].append((mass,))
                if label not in oracle.sets[depth]:
                    missing_terms.append((mass,))
            error=error_squared(oracle,state,den,obs)
            error_terms.append((error,))
            rows=[{'label':w,'values':row.values,'den':row.den} for w,row in sorted(oracle.rows.items())]
            residual |= any(any(row.values[j] for j in range(2,program.dim)) for row in oracle.rows.values())
            transitions=[]
            terms=defaultdict(list)
            for latent,mass in sorted(joint.items()):
                for auxiliary in (0,1):
                    plan=approximate_plan(oracle,latent,auxiliary)
                    fallback_count += int(plan['zero_pair_fair_fallback'])
                    for bit in (0,1):
                        p=plan['bit_probability_given_proposed_label']
                        if bit:p=1-p
                        if p:terms[(bit,plan['candidate'])].append((mass,F(1,2),p))
                    transitions.append(plan)
            children=explicit.branches(state,den,history)
            for bit,(child,cd) in enumerate(children):
                childjoint={label:observed(obs,'projected_sampler_joint_kernel',items)
                            for (b,label),items in terms.items() if b==bit}
                h=history+(bit,)
                if depth+1==program.t:
                    for label,mass in state_norms(child,cd,obs).items():
                        terminal_true[(h,label)]=mass
                    for label,mass in childjoint.items():
                        terminal_approx[(h,label)]=mass
                else:
                    following[h]=(child,cd,childjoint)
            query_count+=oracle.stats['row_lookup_queries']
            oracle_state_slots.append(len(oracle.rows)*program.dim)
            records.append({'history':history,'error_squared':error,'rows':rows,
                'exact_rows':[{'label':key[1],'values':row,'den':den} for key,row in sorted(state.items())],
                'oracle_report':oracle.report(),'local_plans':transitions,
                'actual_row_observers':oracle.observer.operations})
        errors.append(observed(obs,'sum_all_history_error',error_terms))
        missing.append(observed(obs,'sum_all_history_missing_mass',missing_terms))
        norms.append({label:observed(obs,'work_marginal_sum',terms) for label,terms in sorted(mu_terms.items())})
        assert errors[-1]<=sum(missing,F(0))
        frontier=following
    # Independent actual classical preparation marginal, no phase/reference QFT.
    marginal={1:F(1)}
    for depth in range(program.t):
        assert marginal==norms[depth]
        terms=defaultdict(list)
        for label,mass in marginal.items():
            terms[label].append((mass,F(1,2)))
            terms[program.tables[depth][label]].append((mass,F(1,2)))
        marginal={w:observed(obs,'classical_preparation_mass',x) for w,x in terms.items()}
    tv_terms=[]
    for key in terminal_true.keys()|terminal_approx.keys():
        difference=observed(obs,'terminal_joint_signed_difference',((terminal_true.get(key,F(0)),),(-terminal_approx.get(key,F(0)),)))
        if difference:tv_terms.append((abs(difference),F(1,2)))
    tv=observed(obs,'terminal_joint_TV',tv_terms)
    tv_squared=observed(obs,'terminal_joint_TV_squared',((tv,tv),))
    assert observed(obs,'approximate_joint_total',((x,) for x in terminal_approx.values()))==1
    assert observed(obs,'reference_joint_total',((x,) for x in terminal_true.values()))==1
    # Only depth 3 prunes in this predeclared fixture: strongest actual bound.
    assert not any(errors[:3]) and tv_squared<=errors[3]<=missing[3]
    assert residual
    return {'status':'EXHAUSTIVE_NATIVE_INSTRUMENT_CONTRACT_VERIFIED',
        'all_15_parent_histories_checked':len(records)==15,
        'all_internal_coordinates_retained':program.dim,
        'errors_squared_by_depth':errors,'true_missing_mass_by_depth':missing,
        'true_work_marginals':norms,'terminal_joint_TV':tv,'terminal_joint_TV_squared':tv_squared,
        'comparison_scope':'all actual same-word joint history/latent masses; no ideal reference',
        'positive_retained_residual':residual,'zero_pair_fair_fallback_plans':fallback_count,
        'checker_row_lookups':query_count,'peak_projected_row_scalar_slots':max(oracle_state_slots),
        'history_records':records,'observer_operations':obs.operations,
        'terminal_true':[[h,w,m] for (h,w),m in sorted(terminal_true.items())],
        'terminal_approximate':[[h,w,m] for (h,w),m in sorted(terminal_approx.items())]}


def table_instance_evidence(programs):
    seen={}
    entries=[]
    for owner,program in programs:
        pending=[(f'{owner}:factory:{key}',table) for key,table in sorted(program.lazy_factory.tables.items())]
        cursor=0
        while cursor<len(pending):
            name,table=pending[cursor]
            cursor+=1
            if id(table) in seen:
                continue
            seen[id(table)]=name
            entries.append({'instance_name':name,'N':table.N,'b':table.b,
                'certificate':table.export_certificate()})
            if table._inverse is not None:
                pending.append((name+':inverse',table._inverse))
    return entries


def main():
    began=perf_counter()
    sources=[Path(__file__),ROOT/'projected_rows.py',OLD/'gram_research/single_walker.py']
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    callstart=len(CALLS)
    vendor=verify_vendor()
    bank,bank_binding=load_bank()
    program=LazyStreamingProgram(35,2,4,bank,61)
    stages=[{'stage':'after_full61_native_admission','core_calls':len(CALLS)-callstart,
             'program_metrics':deepcopy(program.report_metrics())}]
    outer=run_one_shot(program,training_samples=128,holdout_samples=64,caps=[1,2,3,5],
        exact_initial_depth=2,thresholds=[0,0,0,F(1,4)],confidences=[0,0,0,F(1,16)],
        training_rng=random.Random(40201),holdout_rng=random.Random(40202),walker_rng=random.Random(40203))
    walker=outer.pop('live_walker')
    envelope,certificate=outer['training'],outer['holdout']
    stages.append({'stage':'after_positive_outer_runner','core_calls':len(CALLS)-callstart,'program_metrics':deepcopy(program.report_metrics())})
    print('positive holdout',certificate['status'],certificate['tests'],flush=True)
    # One declared unsuccessful-size comparison: no repeated search for a pass.
    failed_outer=run_one_shot(program,training_samples=128,holdout_samples=64,caps=[1,2,3,1],
        exact_initial_depth=2,thresholds=[0,0,0,F(1,4)],confidences=[0,0,0,F(1,16)],
        training_rng=random.Random(40301),holdout_rng=random.Random(40302),walker_rng=random.Random(40303))
    failed_outer.pop('live_walker')
    small,failed=failed_outer['training'],failed_outer['holdout']
    print('small holdout',failed['status'],failed['tests'],flush=True)
    failed_replay=failed_outer['certificate_replay']
    assert failed_outer['route']=='AUTOMATIC_EXACT_FALLBACK'
    assert failed_outer['sample']['status']=='COMPLETE_READOUT'
    stages.append({'stage':'after_small_envelope_and_replay','core_calls':len(CALLS)-callstart,'program_metrics':deepcopy(program.report_metrics())})
    negative=[]
    try:ProjectedWalker(program,small,failed)
    except ValueError:negative.append('uncertified_envelope_rejected')
    else:
        if failed['status']=='NOT_CERTIFIED':raise AssertionError('failed certificate admitted')
    tampered=deepcopy(certificate)
    tampered['tests'][0]['binomial_lower_tail_at_threshold']='0'
    tampered['certificate_sha256']=digest({k:v for k,v in tampered.items() if k!='certificate_sha256'})
    try:verify_validation(program,envelope,tampered)
    except ValueError:negative.append('rehashed_false_binomial_tail_rejected')
    else:raise AssertionError('false binomial probability admitted')
    misleading=deepcopy(certificate)
    misleading['conditional_on_acceptance_probability_bound_claimed']=True
    misleading['certificate_sha256']=digest({k:v for k,v in misleading.items() if k!='certificate_sha256'})
    try:verify_validation(program,envelope,misleading)
    except ValueError:negative.append('rehashed_conditional_confidence_claim_rejected')
    else:raise AssertionError('misleading conditional confidence metadata admitted')
    broken=deepcopy(envelope)
    broken['sets'][2]=[1]
    broken['envelope_sha256']=digest({k:v for k,v in broken.items() if k!='envelope_sha256'})
    try:verify_envelope(program,broken)
    except ValueError:negative.append('rehashed_false_exact_coverage_rejected')
    else:raise AssertionError('false exact coverage admitted')
    sampler=None
    if certificate['status']=='ACCEPTED_STATISTICAL_CERTIFICATE':
        sampler=outer['sample']
        assert sampler['status']=='COMPLETE_READOUT'
        sampler={'result':sampler,'oracle_evidence':walker.oracle.evidence(),
                 'certificate_replay':walker.certificate_replay}
        # Interruption after both random draws but during field construction:
        # selected bit, proposal, parent rows/history survive without redraw.
        paused=ProjectedWalker(program,envelope,certificate,query_budget=2)
        interrupted=paused.run(ScriptedRandom([0,0]))
        assert interrupted['status']=='INCOMPLETE_POINT_QUERY_BUDGET'
        assert interrupted['pending_selected_bit']==0 and interrupted['history']==()
        paused.oracle.query_budget=100000
        resumed=paused.run(random.Random(40203))
        assert resumed['status']=='COMPLETE_READOUT'
        sampler['interrupted']=interrupted
        sampler['resumed']=resumed
    explicit=SelectedStreamingProgram(35,2,4,bank,61)
    contract=exhaustive_contract(program,explicit,envelope)
    assert contract['zero_pair_fair_fallback_plans']>0
    # Predeclared distinct odd-order fixture: final arms overlap, so projection
    # can alter scores rather than being hidden by N35's disjoint final arms.
    odd_program=LazyStreamingProgram(33,4,4,bank,61)
    odd_outer=run_one_shot(odd_program,training_samples=128,holdout_samples=64,caps=[1,2,4,4],
        exact_initial_depth=2,thresholds=[0,0,0,F(1,4)],confidences=[0,0,0,F(1,16)],
        training_rng=random.Random(40401),holdout_rng=random.Random(40402),walker_rng=random.Random(40403))
    odd_outer.pop('live_walker')
    print('odd-order contrast',odd_outer['route'],odd_outer['holdout']['tests'],flush=True)
    odd_explicit=SelectedStreamingProgram(33,4,4,bank,61)
    odd_contract=exhaustive_contract(odd_program,odd_explicit,odd_outer['training'])
    assert odd_contract['terminal_joint_TV']>0
    stages.append({'stage':'after_exhaustive_checker','core_calls':len(CALLS)-callstart,'program_metrics':deepcopy(program.report_metrics())})
    assert before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result={'status':'AUTHOR_ACTUAL_BOUNDED_PROJECTED_ROW_PROTOTYPE_NOT_ADMITTED',
        'activity':'RA-CAAAC604CB513AEA8BBC1DFC','N':35,'a':2,'t':4,'dimension':61,
        'default_width_for_N_not_claimed':True,'source_sha256':before,'source_bank':bank_binding,
        'kernel':vendor,'frozen_training':envelope,'holdout':certificate,
        'small_envelope':small,'small_holdout':failed,'small_holdout_replay':failed_replay,
        'projected_sampler':sampler,'full_history_contract_check':contract,'negative_controls':negative,
        'outer_runner_positive':outer,'outer_runner_failed_test_exact_fallback':failed_outer,
        'odd_order_contrast':{'N':33,'a':4,'t':4,'outer_runner':odd_outer,'contract_check':odd_contract},
        'resource_stages':stages,'complete_modular_table_instances':table_instance_evidence([
            ('N35algorithm',program),('N35checker',explicit),('N33algorithm',odd_program),('N33checker',odd_explicit)]),
        'actual_BRC_core_calls':len(CALLS)-callstart,'actual_BRC_core_receipts':CALLS[callstart:],
        'software_fixture_seeds':{'training':40201,'holdout':40202,'walker':40203,'small_training':40301,'small_holdout':40302,'small_fallback':40303,
            'odd_training':40401,'odd_holdout':40402,'odd_walker':40403},
        'same_envelope_retries':0,'ideal_reference_run':False,'order_or_factors_provided':False,
        'certificate_claim':'one attempt; true error budget TV<=1/2 if threshold valid, unconditional outer false-accept addition<=1/16 with exact fallback on failed tests',
        'exact_fallback_invoked_in_this_fixture':True,'universal_efficiency_claimed':False,
        'seconds':perf_counter()-began}
    raw=packed(serializable(result))
    target=ROOT/'PROJECTED_ROWS_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw,mtime=0))
    brief={k:result[k] for k in ('status','activity','N','a','t','dimension','source_sha256','actual_BRC_core_calls','negative_controls','resource_stages','seconds')}
    brief.update({'accepted_status':certificate['status'],'holdout_tests':certificate['tests'],
        'small_status':failed['status'],'small_holdout_tests':failed['tests'],
        'envelope_sets':envelope['sets'],'training_samples_each_case':128,'holdout_samples_each_case':64,
        'true_missing_mass_by_depth':contract['true_missing_mass_by_depth'],
        'errors_squared_by_depth':contract['errors_squared_by_depth'],
        'terminal_joint_TV':contract['terminal_joint_TV'],
        'positive_retained_residual':contract['positive_retained_residual'],
        'zero_pair_fair_fallback_plans':contract['zero_pair_fair_fallback_plans'],
        'outer_routes':[outer['route'],failed_outer['route'],odd_outer['route']],
        'odd_order_contrast':{'N':33,'a':4,'holdout_tests':odd_outer['holdout']['tests'],
            'sets':odd_outer['training']['sets'],'terminal_joint_TV':odd_contract['terminal_joint_TV'],
            'missing_mass':odd_contract['true_missing_mass_by_depth'],
            'errors_squared':odd_contract['errors_squared_by_depth'],
            'sample_report':odd_outer['sample']['oracle_report'],
            'resource_stages':odd_outer['resource_stages']},
        'sampler':None if sampler is None else {'status':sampler['result']['status'],'history':sampler['result']['history'],
            'report':sampler['result']['oracle_report']},
        'payload_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    (ROOT/'PROJECTED_ROWS_SUMMARY.json').write_text(json.dumps(serializable(brief),ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'core_calls':result['actual_BRC_core_calls'],
        'missing':list(map(str,contract['true_missing_mass_by_depth'])),'TV':str(contract['terminal_joint_TV']),
        'fallback':contract['zero_pair_fair_fallback_plans'],'seconds':result['seconds']}),flush=True)


if __name__=='__main__':main()
