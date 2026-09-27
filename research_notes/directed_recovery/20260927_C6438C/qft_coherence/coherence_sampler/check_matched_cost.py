"""Same viable tape row-cost comparison, not a distributional timing benchmark."""
from pathlib import Path
from fractions import Fraction as F
import gzip,hashlib,json,sys
from time import perf_counter

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from check_coherence_skip import (load_bank,LazyStreamingProgram,serializable,packed,
    CALLS,collect_tables)
from coherence_skip import CoherenceWalker,SingleWalker


class AllZeroTape:
    def randrange(self,n):return 0


def main():
    started=perf_counter();first=len(CALLS)
    source=HERE/'COHERENCE_SKIP_RESULTS.json.gz'
    payload=gzip.decompress(source.read_bytes());record=json.loads(payload)
    bank,binding=load_bank();cases=[];programs=[]
    for index,old in enumerate(record['cases'][:2]):
        N,a=old['spec']['N'],old['spec']['a']
        partition=old['outer_runner']['partition'];certificate=old['outer_runner']['certificate']
        measured=[];walkers=[]
        for name in ('exact','coherence'):
            start=len(CALLS);program=LazyStreamingProgram(N,a,4,bank,61)
            programs.append((f'{index}:{name}',program));post_setup=len(CALLS)
            if name=='exact':walker=SingleWalker(program,query_budget=10000)
            else:walker=CoherenceWalker(program,partition,certificate,query_budget=10000)
            pre_sample=len(CALLS)
            result=walker.run(AllZeroTape());post_sample=len(CALLS)
            assert result['status']=='COMPLETE_READOUT'
            assert result['history']==(0,0,0,0) and result['latent_work_label']==1
            measured.append({'route':name,'setup_native_calls':post_setup-start,
                'certificate_replay_native_calls':pre_sample-post_setup,
                'sampling_native_calls':post_sample-pre_sample,
                'sample':result,'oracle_evidence':walker.oracle.evidence()})
            walkers.append(walker)
        # Actual point-budget stop/resume uses same retained auxiliary draw.
        stopped=CoherenceWalker(programs[-1][1],partition,certificate,query_budget=1)
        partial=stopped.run(AllZeroTape())
        assert partial['status']=='INCOMPLETE_POINT_QUERY_BUDGET'
        assert stopped.pending_auxiliary_bit==0
        before_cache=dict(stopped.oracle.cache)
        stopped.oracle.query_budget=10000
        complete=stopped.run(AllZeroTape())
        assert complete['status']=='COMPLETE_READOUT' and complete['history']==(0,0,0,0)
        assert all(stopped.oracle.cache[k]==v for k,v in before_cache.items())
        exact_keys=set(walkers[0].oracle.cache);skip_keys=set(walkers[1].oracle.cache)
        cases.append({'N':N,'a':a,'same_viable_auxiliary_and_readout_tape':'all zeros',
            'measurements':measured,'distinct_exact_queries':len(exact_keys),
            'distinct_skip_queries':len(skip_keys),'same_final_query_key_set':exact_keys==skip_keys,
            'query_keys_avoided':sorted(exact_keys-skip_keys),
            'query_keys_added':sorted(skip_keys-exact_keys),
            'budget_resume':{'partial':partial,'complete':complete,
                'old_cached_rows_preserved':True,'oracle_evidence':stopped.oracle.evidence()}})
        print('matched',N,'exact',len(exact_keys),'skip',len(skip_keys),flush=True)
    result={'schema':'ACTUAL_SAME_TAPE_ROW_COST_V1','status':'AUTHOR_BOUNDED_NO_ASYMPTOTIC_CLAIM',
        'source_payload_sha256':hashlib.sha256(payload).hexdigest(),
        'source_hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
            (Path(__file__),HERE/'coherence_skip.py')},
        'bank_binding':binding,'cases':cases,'actual_table_instances':collect_tables(programs),
        'native_core_calls_count':len(CALLS)-first,'native_core_calls':CALLS[first:],
        'elapsed_seconds':perf_counter()-started,
        'tape_is_a_selected_positive_probability_path_not_fresh_uniform_sampling':True,
        'training_and_validation_generation_are_in_prior_complete_record_not_free':True}
    raw=packed(serializable(result));gz=gzip.compress(raw,mtime=0)
    (HERE/'MATCHED_COST_RESULTS.json.gz').write_bytes(gz)
    summary={'status':result['status'],'payload_sha256':hashlib.sha256(raw).hexdigest(),
        'gzip_sha256':hashlib.sha256(gz).hexdigest(),'native_core_calls_count':result['native_core_calls_count'],
        'cases':[{k:c[k] for k in ['N','a','distinct_exact_queries','distinct_skip_queries',
            'same_final_query_key_set','query_keys_avoided','query_keys_added']} for c in cases]}
    (HERE/'MATCHED_COST_SUMMARY.json').write_bytes(packed(summary))
    print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__':main()
