"""Read-only stdlib accounting of the saved SO-bank run; no native imports."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[1]


def sha(data):return hashlib.sha256(data).hexdigest()


def summary(label,bank):
    setup=bank['setup'];words=bank['logical']['words']
    operations=[op for word in words.values() for op in word['observer_operations']]
    return {'label':label,'bank_binding_sha256':bank['binding_sha256'],
        'native_core_calls':setup['core_call_count'],
        'call_interval':setup['call_interval'],'elapsed_seconds':setup['elapsed_seconds'],
        'word_count':len(words),'observer_operations':len(operations),
        'trace_expression_references':sum(w.get('expression_reference_count',0) for w in words.values()),
        'observer_graph_states_sum':sum(op['states'] for op in operations),
        'observer_graph_states_max':max((op['states'] for op in operations),default=0),
        'observer_depth_max':max((op['depth'] for op in operations),default=0),
        'stored_trace_nodes':setup.get('stored_trace_nodes'),
        'stored_full_matrix_scalar_entries':setup.get('stored_full_matrix_scalar_entries'),
        'stored_complete_column_scalar_entries':setup['stored_complete_column_scalar_entries'],
        'logical_serialized_bytes':setup['logical_serialized_bytes'],
        'mandatory_first_replay_basis_actions':183*len(words),
        'mandatory_basis_count_is_lower_bound_not_all_codec_cache_replay_work':True,
        'word_setups':setup['word_setups']}


def main():
    compressed=(ROOT/'SO_TRACE_BANK_RESULTS.json.gz').read_bytes()
    raw=gzip.decompress(compressed);record=json.loads(raw)
    assert sha(raw)=='6ec1b936ddb16370aa4ba596e7ba095f3bd90fc823d5a7b0d054cb3503019975'
    for name,expected in record['source_hashes'].items():
        assert sha((ROOT/name).read_bytes())==expected
    assert record['status']=='PASSED' and len(record['actual_core_calls'])==record['core_call_count']
    banks=[summary(name,record[name]) for name in ('encoded_bank','complete_bank','restored_bank')]
    banks += [summary('special:'+case['case'],case['bank']) for case in record['special_words']]
    failed=[]
    for item in record['negative_controls']:
        ev=item['failed_fresh_replay_evidence']
        if ev is not None:
            assert ev['setup']['core_call_count']==item['actual_core_calls']
            entry=summary('failed_replay:'+item['case'],ev);failed.append(entry);banks.append(entry)
    intervals=[tuple(bank['call_interval']) for bank in banks]
    nonempty=sorted((a,b) for a,b in intervals if a!=b)
    assert all(b<=c for (a,b),(c,d) in zip(nonempty,nonempty[1:]))
    bankcalls=sum(bank['native_core_calls'] for bank in banks)
    observercalls=sum(bank['observer_operations'] for bank in banks)
    old_raw=gzip.decompress((BASE/'sep27-qft-uniform/word_certificates/WORD_CERTIFICATE_RESULTS.json.gz').read_bytes())
    assert sha(old_raw)==record['prior_rank_two_comparison_raw_sha256']
    old=json.loads(old_raw)
    prior=summary('historical_rank_two_encoded_bank',old['encoded_bank'])
    tables=[]
    for index,program in enumerate(record['program_admissions']):
        # Each program owns its table instances. Same N/a does not identify
        # an instance; no repeated snapshot of that instance is included here.
        for j,table in enumerate(program['factory_tables']):
            tables.append({'program_index':index,'N':program['N'],'a':program['a'],
                't':program['t'],'factory_table_index':j,'stats':table['stats'],
                'permutation_sha256':table['permutation_sha256']})
    result={'schema':'SO_TRACE_BANK_OFFLINE_COST_ACCOUNTING_V1',
        'extractor_sha256':sha(Path(__file__).read_bytes()),'source_hashes':record['source_hashes'],
        'raw_sha256':sha(raw),'gzip_sha256':sha(compressed),
        'whole_checker':{'native_core_calls':record['core_call_count'],
            'elapsed_seconds':record['elapsed_seconds'],
            'bank_construction_or_fresh_replay_calls':bankcalls,
            'actual_bank_observer_operations':observercalls,
            'other_admission_calls':record['core_call_count']-bankcalls,
            'bank_invocations_with_saved_evidence':len(banks),
            'negative_controls':len(record['negative_controls']),
            'negative_controls_with_complete_fresh_replay':len(failed),
            'negative_controls_rejected_with_zero_core_calls':sum(
                x['actual_core_calls']==0 for x in record['negative_controls']),
            'replayed_word_count':sum(x['word_count'] for x in banks)},
        'bank_invocations':banks,'historical_comparator':prior,
        'historical_comparator_is_not_a_matched_timing_trial':True,
        'warm_reuse':record['warm_reuse'],'distinct_program_table_snapshots':tables,
        'table_scope':'factory instances only; initial permutation-verification receipts remain in raw; '
                      'no attempt to infer all host integer work or duplicate cumulative reports',
        'basis_scope':'183 basis actions per word counts only the forced first forward/inverse/recovery replay. '
                      'Final codec validation may trigger additional actual replay cache misses; '
                      'zero new core calls does not mean zero native word work.',
        'not_measured':['whole-program Shor speedup','complete host bit complexity',
                        'policy execution or conditional sampling','total primitive-loop operations'],
        'unexpected_failed_execution_artifacts':[p.name for p in ROOT.glob('FAILED_EXECUTION_*.json.gz')]}
    assert bankcalls==observercalls
    (ROOT/'SO_TRACE_COST_ACCOUNTING.json').write_text(
        json.dumps(result,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps(result['whole_checker'],sort_keys=True))


if __name__=='__main__':main()
