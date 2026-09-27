"""Three predeclared full-D61 native experiments and complete joint laws."""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import gzip,hashlib,json,random,sys
from time import perf_counter

HERE=Path(__file__).resolve().parent
OLD=HERE.parents[1]/'sep27-qft-research'
sys.path.insert(0,str(OLD/'gram_research'))
from check_single_walker import (load_bank,LazyStreamingProgram,SelectedStreamingProgram,
    RawRow,PointRowOracle,serializable,packed,CALLS,verify_vendor,ScriptedRandom)
from coherence_skip import (run_one_shot,total_transition_plan,CoherenceWalker,
    verify_validation,observed,PositivePathObserver,digest)


def norms(state,den,observer):
    return {key[1]:observed(observer,'actual_complete_row_norm',
        ((F(x,den),F(x,den)) for x in row if x))
        for key,row in state.items() if any(row)}


def exhaustive(program,explicit,partition,certificate):
    accepted=verify_validation(program,partition,certificate)
    skip=partition['depth'] if accepted else None
    obs=PositivePathObserver()
    state,den=explicit.initial()
    frontier={(): (state,den,{1:F(1)})}
    records=[]
    truths,approximates={},{}
    parent_zero=zero_pair=0
    layer_L=[]
    mu_layers=[]
    for depth in range(program.t):
        future={}
        layerterms=[]
        muterms=defaultdict(list)
        for history,(state,den,joint) in frontier.items():
            refnorm=norms(state,den,obs)
            for w,m in refnorm.items():muterms[w].append((m,))
            oracle=PointRowOracle(program,history,query_budget=10000)
            terms=defaultdict(list)
            plans=[]
            for latent,mass in sorted(joint.items()):
                if not mass:continue
                for auxiliary in (0,1):
                    plan=total_transition_plan(oracle,latent,auxiliary,fair=depth==skip)
                    parent_zero+=plan.get('parent_latent_row_zero',False)
                    zero_pair+=plan['zero_pair_fair_extension']
                    for bit in (0,1):
                        p=plan['bit_probability_given_proposed_label']
                        if bit:p=1-p
                        if p:terms[(bit,plan['candidate'])].append((mass,F(1,2),p))
                    plans.append(plan)
            if depth==partition['depth']:
                inverse=program.tables[depth].inverse()
                for w in sorted(refnorm):
                    source=state.get((0,inverse[w],0),(0,)*program.dim)
                    y=oracle.apply_feedback(depth,RawRow(tuple(source),den))
                    x=state[(0,w,0)]
                    ip=observed(obs,'signed_native_overlap',
                        ((F(a,den),F(b,y.den)) for a,b in zip(x,y.values) if a and b))
                    if ip:layerterms.append((abs(ip),))
            children=explicit.branches(state,den,history)
            for bit,(child,cd) in enumerate(children):
                h=history+(bit,)
                cj={w:observed(obs,'totalized_joint_kernel',x)
                    for (b,w),x in terms.items() if b==bit}
                if depth+1==program.t:
                    for w,m in norms(child,cd,obs).items():truths[(h,w)]=m
                    for w,m in cj.items():approximates[(h,w)]=m
                else:future[h]=(child,cd,cj)
            records.append({'history':history,'exact_state':[
                {'label':key[1],'row':row,'den':den} for key,row in sorted(state.items())],
                'approximate_incoming_joint':sorted(joint.items()),'plans':plans,
                'point_oracle_evidence':oracle.evidence()})
        frontier=future
        layer_L.append(observed(obs,'sum_all_history_absolute_coherence',layerterms))
        mu_layers.append({w:observed(obs,'sum_all_history_work_norm',x) for w,x in muterms.items()})
    diffs=[]
    for key in truths.keys()|approximates.keys():
        delta=observed(obs,'terminal_joint_signed_difference',
            ((truths.get(key,F(0)),),(-approximates.get(key,F(0)),)))
        if delta:diffs.append((abs(delta),F(1,2)))
    tv=observed(obs,'complete_terminal_joint_TV',diffs)
    assert observed(obs,'reference_total_mass',((x,) for x in truths.values()))==1
    assert observed(obs,'approximate_total_mass',((x,) for x in approximates.values()))==1
    depth=partition['depth']; A=frozenset(partition['set_A'])
    r=observed(obs,'actual_union_bad_probability',((m,) for w,m in mu_layers[depth].items()
        if w not in A or program.tables[depth][w] in A))
    L=layer_L[depth]
    local_budget=observed(obs,'half_layer_absolute_coherence',((L,F(1,2)),))
    tvsquare=observed(obs,'actual_joint_TV_squared',((tv,tv),))
    if accepted:
        assert tv<=local_budget
        if r<=F(1,2):
            rr=observed(obs,'actual_union_bound_squared',((r,1-r),))
            assert observed(obs,'layer_budget_squared',((local_budget,local_budget),))<=rr
        assert r<=F(certificate['threshold']), 'this fixed accepted fixture happened to false-accept'
        assert tvsquare<=F(certificate['layer_joint_TV_bound_squared'])
    else:assert tv==0
    return {'status':'ALL_NATIVE_JOINT_LAWS_VERIFIED','accepted':accepted,'skip_depth':skip,
        'parent_histories_checked':len(records),'actual_union_probability':r,
        'sum_reference_history_absolute_coherence':L,'reference_telescope_layer_budget':local_budget,
        'terminal_joint_TV':tv,'terminal_joint_TV_squared':tvsquare,
        'restoration_parent_zero_plans':parent_zero,'zero_pair_fair_extensions':zero_pair,
        'full_internal_dimension':program.dim,'mu_layers':mu_layers,
        'all_history_records':records,'terminal_true':[[h,w,m] for (h,w),m in sorted(truths.items())],
        'terminal_approximate':[[h,w,m] for (h,w),m in sorted(approximates.items())],
        'observer_operations':obs.operations}


def collect_tables(named_programs):
    seen=set();entries=[]
    for name,program in named_programs:
        pending=[(f'{name}:factory:{key}',table) for key,table in sorted(program.lazy_factory.tables.items())]
        for label,table in pending:
            if id(table) in seen:continue
            seen.add(id(table));entries.append({'instance':label,'certificate':table.export_certificate()})
            if table._inverse is not None:pending.append((label+':inverse',table._inverse))
    return entries


def main():
    start=perf_counter();callstart=len(CALLS)
    sources=[Path(__file__),HERE/'coherence_skip.py']
    source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    vendor=verify_vendor();bank,bankbinding=load_bank()
    # Frozen before seeing validation outcomes; no until-accepted retries.
    specs=[{'N':35,'a':2,'cap':8,'threshold':F(1,16),'seed':50201},
           {'N':129,'a':4,'cap':8,'threshold':F(3,8),'seed':50301},
           {'N':129,'a':4,'cap':1,'threshold':F(1,16),'seed':50401}]
    records=[];programs=[]
    for index,spec in enumerate(specs):
        program=LazyStreamingProgram(spec['N'],spec['a'],4,bank,61)
        programs.append((f'case{index}:algorithm',program))
        before=deepcopy(program.report_metrics());calls0=len(CALLS)
        outer=run_one_shot(program,2,training_samples=32,cap=spec['cap'],holdout_samples=96,
            threshold=spec['threshold'],confidence=F(1,32),
            training_rng=random.Random(spec['seed']),holdout_rng=random.Random(spec['seed']+1),
            walker_rng=random.Random(spec['seed']+2),query_budget=10000)
        walker=outer.pop('live_walker')
        assert outer['sample']['status']=='COMPLETE_READOUT'
        alg_evidence=walker.oracle.evidence()
        alg_metrics=deepcopy(program.report_metrics());calls1=len(CALLS)
        explicit=SelectedStreamingProgram(spec['N'],spec['a'],4,bank,61)
        programs.append((f'case{index}:explicit',explicit))
        law=exhaustive(program,explicit,outer['partition'],outer['certificate'])
        print('case',index,outer['outer_branch'],'misses',outer['certificate']['misses'],
              'r',law['actual_union_probability'],'TV',law['terminal_joint_TV'],flush=True)
        if index==0:assert outer['outer_branch']=='APPROXIMATE_CERTIFIED' and law['terminal_joint_TV']==0
        if index==1:assert outer['outer_branch']=='APPROXIMATE_CERTIFIED' and law['terminal_joint_TV']>0
        if index==2:assert outer['outer_branch']=='AUTOMATIC_EXACT_FALLBACK'
        assert len(law['all_history_records'])==15
        # Resume after the auxiliary proposal was drawn. No redraw on resume.
        resumed=CoherenceWalker(program,outer['partition'],outer['certificate'],query_budget=10000)
        partial=resumed.run(ScriptedRandom([0]))
        assert partial['status']=='INCOMPLETE_RANDOM_SOURCE' and resumed.pending_auxiliary_bit==0
        complete=resumed.run(random.Random(spec['seed']+3))
        assert complete['status']=='COMPLETE_READOUT' and complete['events'][0]['auxiliary_bit']==0
        negative=[]
        bad=deepcopy(outer['certificate']);bad['misses']+=1
        bad['certificate_sha256']=digest({k:v for k,v in bad.items() if k!='certificate_sha256'})
        try:verify_validation(program,outer['partition'],bad)
        except ValueError:negative.append('rehashed_false_miss_count_rejected')
        else:raise AssertionError('bad count accepted')
        bound=CoherenceWalker(program,outer['partition'],outer['certificate'])
        bound.latent=0
        try:bound.step(random.Random(1))
        except ValueError:negative.append('externally_replaced_latent_rejected')
        else:raise AssertionError('external latent accepted')
        records.append({'spec':spec,'outer_runner':outer,'algorithm_oracle':alg_evidence,
            'algorithm_program_metrics_before':before,'algorithm_program_metrics_after':alg_metrics,
            'algorithm_native_core_calls':calls1-calls0,'complete_joint_law':law,
            'pause_resume':{'partial':partial,'complete':complete,'oracle':resumed.oracle.evidence()},
            'negative_controls':negative})
    # Explicit zero-pair extension on a known impossible measured prefix.
    flat=LazyStreamingProgram(3,1,4,bank,61);programs.append(('zero_pair_extension',flat))
    zerooracle=PointRowOracle(flat,(1,),query_budget=1000)
    zeroplan=total_transition_plan(zerooracle,1,0)
    assert zeroplan['zero_pair_fair_extension'] and zeroplan['bit_probability_given_proposed_label']==F(1,2)
    assert any(r['complete_joint_law']['restoration_parent_zero_plans'] for r in records)
    evidence={'schema':'ACTUAL_NATIVE_COHERENCE_SKIP_EXPERIMENT_V1',
        'status':'AUTHOR_ACTUAL_BOUNDED_NOT_ADMITTED','source_sha256':source_hashes,
        'vendor_binding':vendor,'bank_binding':bankbinding,'cases':records,
        'zero_pair_extension_negative_reference':{'plan':zeroplan,'oracle':zerooracle.evidence()},
        'actual_table_instances':collect_tables(programs),
        'native_core_calls_this_run':len(CALLS)-callstart,
        'native_core_calls':CALLS[callstart:],'elapsed_wall_seconds':perf_counter()-start,
        'same_input_native_instrument_only_no_ideal_reference':True}
    assert source_hashes=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    payload=packed(serializable(evidence))
    target=HERE/'COHERENCE_SKIP_RESULTS.json.gz'
    target.write_bytes(gzip.compress(payload,mtime=0))
    summary={'status':evidence['status'],'native_core_calls':evidence['native_core_calls_this_run'],
        'elapsed_wall_seconds':evidence['elapsed_wall_seconds'],
        'payload_sha256':hashlib.sha256(payload).hexdigest(),
        'gzip_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
        'cases':[{k:r['complete_joint_law'][k] for k in ['accepted','actual_union_probability',
            'terminal_joint_TV','restoration_parent_zero_plans','zero_pair_fair_extensions']}
            for r in records]}
    (HERE/'COHERENCE_SKIP_SUMMARY.json').write_bytes(packed(serializable(summary)))
    print(json.dumps(json.loads(packed(serializable(summary))),indent=2),flush=True)


if __name__=='__main__':main()
