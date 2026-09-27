"""Offline cost audit, not a scientific execution or replay.

Reuses only frozen standard-library accounting helpers. No scientific module is
imported. Final raw/source hashes and the historical comparator are checked.
"""
from pathlib import Path
from collections import Counter
import gzip
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parent
RUN = ROOT.parent / 'uniform_execution'
BASE = ROOT.parents[1]
OLD = BASE / 'sep27-qft-adaptive/adaptive_execution'
HELPER_SHA = '925cc3ee46effb69490ccb11ccf92d51120df489d4ec0b8c3a29ded3695ef730'
OLD_RAW_SHA = '3e356df6befcbf201801657016f64072e2bccebbc0a877a51570f77748d7b78b'
OLD_COST_SHA = 'f82a4362365c95112b3780685ac4e02ca0a24e88b37f421219ab06883d6999f3'
EXPECTED_RAW = '4a4e57d960ff689f5244307070d94ff180b594fb0db3824119d741cad78a1460'
ADDITIVE = ('native_phase_vector_applications','query_requests','query_cache_hits',
            'base_queries','recurrence_queries','actual_positive_path_observations',
            'single_term_wiring_observations','zero_wiring_observations',
            'zero_matrix_native_actions_skipped')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),
                      ensure_ascii=False,allow_nan=False).encode('utf-8')


def helpers():
    path = OLD / 'extract_cost_accounting.py'
    assert sha(path.read_bytes()) == HELPER_SHA
    spec = importlib.util.spec_from_file_location('frozen_offline_cost_helpers',path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def gram(e,source,helper):
    assert e['source_sha256'] == source
    inherited = e['inherited']; report = inherited['report']
    assert inherited['source_sha256'] == '468de944518fbc6afa81a17555676436376da63921a784c810ffe8fab3ca17e9'
    ops = inherited['observer_operations']; matrices = inherited['correlations']
    assert len(ops) == report['actual_positive_path_observations']
    assert len(matrices) == report['distinct_queries']
    assert len(matrices)*report['dimension']**2 == report['cached_matrix_scalar_slots']
    assert report['query_keys'] == [[x['depth'],x['residue']] for x in matrices]
    assert e['policy_stats']['prefix_covariance_defect_calls'] == 0
    assert e['policy_stats']['defect_matrix_entries_observed'] == 0
    assert e['policy_stats']['prefix_mass_observations_for_policy'] == 0
    forbidden = ('full_gate_action_defect','rational_local_trace_distance_test','policy_prefix_mass')
    assert not any(op['name'].split(':',1)[-1] in forbidden for op in ops)
    certs = e['certificates'] + ([e['pending']] if e['pending'] is not None else [])
    for c in certs:
        assert c['prefix_mass_observed_for_policy'] is False
        assert c['prefix_covariance_defect_observed'] is False
    accepted = [c for c in certs if c['decision']=='OMIT_OLDEST_UNIFORM_CERTIFIED']
    assert len(accepted) == e['policy_stats']['accepted_omissions']
    assert sum(len(c['reference_ids'])-len(c['selected_ids']) for c in certs) == len(accepted)
    return {**{k:report[k] for k in ADDITIVE},
        'retained_independent_cache_matrices':len(matrices),
        'retained_matrix_scalar_slots':report['cached_matrix_scalar_slots'],
        'peak_cached_matrix_scalar_slots':report['peak_cached_matrix_scalar_slots'],
        'max_numerator_bits':report['max_correlation_numerator_bits'],
        'max_denominator_bits':report['max_correlation_denominator_bits'],
        'policy_stats':e['policy_stats'],'observer':helper.observer_cost(ops),
        'committed_history':e['cursor']['history'],
        'interruption_events':e['interruption_events'],
        'admission_mode':e['certificate_admission_mode'],
        'bank_binding':e['certificate_bank_sha256']}


def route(record,source,helper):
    gs = record['gram_executions']; leaves = [gram(e,source,helper) for e in gs]
    unique,decisions = {},{}
    for e in gs:
        h = e['cursor']['history']
        for c in e['inherited']['correlations']:
            key = (tuple(h[:c['depth']]),c['depth'],c['residue'])
            value = sha(encoded(c))
            assert key not in unique or unique[key] == value
            unique[key] = value
        for c in e['certificates'] + ([e['pending']] if e['pending'] is not None else []):
            key = tuple(c['history'])
            value = (c['decision'],tuple(c['selected_ids']))
            assert key not in decisions or decisions[key] == value
            decisions[key] = value
    return {'leaf_replay_invocations':len(leaves),'prefix_checks':len(record['checks']),
        'sums_over_separate_leaf_objects':{**{k:sum(g[k] for g in leaves) for k in ADDITIVE},
            'retained_independent_cache_matrices':sum(g['retained_independent_cache_matrices'] for g in leaves),
            'retained_matrix_scalar_slots':sum(g['retained_matrix_scalar_slots'] for g in leaves),
            **{k:sum(g['policy_stats'][k] for g in leaves) for k in
                ('accepted_omissions','candidate_tests','uniform_certificate_lookups','certificate_binding_checks',
                 'prefix_covariance_defect_calls','prefix_mass_observations_for_policy')}},
        'audit_union_of_history_specific_matrices':len(unique),
        'audit_union_of_accepted_prefix_decisions':sum(v[0]=='OMIT_OLDEST_UNIFORM_CERTIFIED' for v in decisions.values()),
        'max_single_leaf_scalar_slots':max(g['peak_cached_matrix_scalar_slots'] for g in leaves),
        'explicit_checker_observer':helper.observer_cost(record['explicit_observer_operations']),
        'explicit_checker_phase_vector_actions':None,
        'whole_route_actual_core_calls_delta':record['actual_core_calls_delta'],
        'leaf_replays':leaves}


def cold(e,helper):
    logical,setup = e['logical'],e['setup']
    assert sha(encoded(logical)) == e['binding_sha256']
    assert setup['core_call_count'] == len(setup['actual_core_calls'])
    words = []
    for m,w in logical['words'].items():
        assert w['full_dimension'] == 61
        assert w['actual_unique_observer_expressions'] == len(w['observer_operations'])
        for name,matrix in w['full_matrices'].items():
            assert len(matrix)==61 and all(len(row)==61 for row in matrix)
            ix=w['entry_expression_indices'][name]
            assert len(ix)==61 and all(len(row)==61 for row in ix)
            for i in range(61):
                for j in range(61):
                    assert w['observer_operations'][ix[i][j]]['signed_observation']==matrix[i][j]
        assert w['observer_operations'][w['s_expression_index']]['signed_observation']==w['s']
        words.append({'phase_index':int(m),'accepted':w['accepted'],'s':w['s'],
            'expression_references':w['expression_reference_count'],
            'zero_expression_references':w['zero_expression_reference_count'],
            'observer':helper.observer_cost(w['observer_operations']),
            'failed_entry_count':len(w['failed_entries'])})
    return {'binding_sha256':e['binding_sha256'],'core_calls':setup['core_call_count'],
        'elapsed_seconds':setup['elapsed_seconds'],'word_setups':setup['word_setups'],
        'stored_full_matrix_scalar_entries':setup['stored_full_matrix_scalar_entries'],
        'stored_complete_column_scalar_entries':setup['stored_complete_column_scalar_entries'],
        'logical_serialized_bytes':setup['logical_serialized_bytes'],
        'unique_word_observers':sum(w['observer']['operations'] for w in words),
        'words':words,'native_program_admission_setup_included':setup['native_program_admission_setup_included']}


def main():
    helper=helpers()
    wordroot=ROOT.parent/'word_certificates'
    wordzip=(wordroot/'WORD_CERTIFICATE_RESULTS.json.gz').read_bytes()
    wordraw=gzip.decompress(wordzip); wordrecord=json.loads(wordraw)
    wordsummary=json.loads((wordroot/'WORD_CERTIFICATE_SUMMARY.json').read_bytes())
    assert sha(wordzip)==wordsummary['gzip_sha256'] and sha(wordraw)==wordsummary['payload_sha256']
    for name,expected in wordsummary['source_hashes'].items():
        assert sha((wordroot/name).read_bytes())==expected
    assert wordrecord['source_hashes']==wordsummary['source_hashes']
    assert len(wordrecord['actual_core_calls'])==wordsummary['core_call_count']
    assert len(wordrecord['negative_controls'])==wordsummary['negative_controls']
    assert all(n['rejected'] for n in wordrecord['negative_controls'])
    assert wordrecord['failed_reflection_witness']['logical']['words']['2']['accepted'] is False
    assert wordrecord['failed_reflection_witness']['logical']['words']['2']['failed_entries']==[[0,0,'8']]
    assert wordrecord['zero_identity_witness']['logical']['words']['2']['accepted'] is True
    assert wordrecord['zero_identity_witness']['logical']['words']['2']['s']=='0'
    zipped=(RUN/'UNIFORM_FEEDBACK_RESULTS.json.gz').read_bytes()
    raw=gzip.decompress(zipped); r=json.loads(raw)
    assert sha(raw)==EXPECTED_RAW
    summary=json.loads((RUN/'UNIFORM_FEEDBACK_SUMMARY.json').read_bytes())
    assert sha(zipped)==summary['gzip_sha256'] and sha(raw)==summary['raw_sha256']
    assert len(zipped)==summary['gzip_bytes'] and len(raw)==summary['raw_bytes']
    assert r['source_hashes']==summary['source_hashes']
    paths={'uniform_feedback.py':RUN/'uniform_feedback.py',
           'check_uniform_feedback.py':RUN/'check_uniform_feedback.py',
           'word_certificates.py':ROOT.parent/'word_certificates/word_certificates.py',
           'check_adaptive_feedback.py':OLD/'check_adaptive_feedback.py'}
    for name,expected in r['source_hashes'].items():
        assert sha(paths[name].read_bytes())==expected
    oldraw=gzip.decompress((OLD/'ADAPTIVE_FEEDBACK_RESULTS.json.gz').read_bytes())
    assert sha(oldraw)==OLD_RAW_SHA
    oldrecord=json.loads(oldraw)
    oldcost=(OLD/'COST_ACCOUNTING.json').read_bytes()
    assert sha(oldcost)==OLD_COST_SHA
    prior=json.loads(oldcost)
    source=r['source_hashes']['uniform_feedback.py']
    cases=[]
    for i,c in enumerate(r['cases']):
        assert (c['summary']['N'],c['summary']['a'])==(prior['cases'][i]['fixture']['N'],prior['cases'][i]['fixture']['a'])
        new={name:route(c[name],source,helper) for name in ('low','reference')}
        historical={name:prior['cases'][i][name]['sums_over_separate_leaf_objects'] for name in ('low','reference')}
        def selected_ledgers(route):
            return [[(s['history'],s['selected_ids'],s['bit']) for s in g['cursor']['steps']]
                    for g in route['gram_executions']]
        ledger_match={name:selected_ledgers(c[name])==selected_ledgers(oldrecord['cases'][i][name])
                      for name in ('low','reference')}
        cases.append({'fixture':c['summary'],**new,'frozen_previous_route_counters':historical,
                      'selected_word_ledgers_equal_frozen_adaptive':ledger_match,
                      'tv_observer':helper.observer_cost(c['tv_observer'])})
    resume={name:gram(r['resume'][name],source,helper) for name in ('original','resumed','cold_replay')}
    negatives=[]
    for n in r['negative_controls']:
        e=n.get('actual_failed_replay_evidence')
        g=None if e is None else gram(e,source,helper)
        if g is not None and 'actual_core_calls_delta' in n:
            assert n['actual_core_calls_delta']==g['actual_positive_path_observations']
        negatives.append({'case':n['case'],'rejected':n['rejected'],
                          'actual_core_calls_delta':n.get('actual_core_calls_delta'),
                          'failed_replay':g,'reason':n['reason']})
    recovery={name:gram(r['interruption_recovery'][name],source,helper) for name in ('retried','fresh')}
    initial_cold=cold(r['certificate_setup']['evidence'],helper)
    restored_cold=cold(r['resume']['cold_replay']['cold_certificate_evidence'],helper)
    assert initial_cold['binding_sha256']==restored_cold['binding_sha256']==r['certificate_bank_final']['binding_sha256']
    assert initial_cold['core_calls']==r['certificate_setup']['actual_core_calls_delta']
    assert restored_cold['core_calls']+resume['cold_replay']['actual_positive_path_observations']==r['resume']['cold_actual_core_calls']
    # The pinned helper recovers factory and inverse instances from all saved
    # snapshots. Include cold-replay evidence as an additional same-program
    # snapshot, not as a new table construction or a scientific replay.
    for_tables={**r,'negative_controls':r['negative_controls']+[
        {'actual_failed_replay_evidence':r['resume']['cold_replay']}]}
    tables=[helper.collect_program_tables(for_tables,i) for i in range(len(r['programs']))]
    grams=[g for c in cases for name in ('low','reference') for g in c[name]['leaf_replays']]
    grams+=list(resume.values())+[n['failed_replay'] for n in negatives if n['failed_replay']]+list(recovery.values())
    ngram=sum(g['actual_positive_path_observations'] for g in grams)
    nexplicit=sum(c[name]['explicit_checker_observer']['operations'] for c in cases for name in ('low','reference'))
    ntv=sum(c['tv_observer']['operations'] for c in cases)
    ncold=initial_cold['core_calls']+restored_cold['core_calls']
    core=r['actual_native_core_calls']; assert len(core)==summary['actual_native_core_calls']
    remainder=len(core)-ngram-nexplicit-ntv-ncold; assert remainder>=0
    out={'schema':'UNIFORM_FEEDBACK_READONLY_COST_AUDIT_V1',
        'method':'Metadata/receipt extraction only; no scientific source imported or executed.',
        'input':{'raw_sha256':sha(raw),'gzip_sha256':sha(zipped),'source_hashes':r['source_hashes']},
        'extractor_sha256':sha(Path(__file__).read_bytes()),'accounting_helper_sha256':HELPER_SHA,
        'comparator':{'raw_sha256':OLD_RAW_SHA,'cost_sha256':OLD_COST_SHA},
        'separate_word_certificate_checker':{
            'raw_sha256':sha(wordraw),'gzip_sha256':sha(wordzip),
            'source_hashes':wordsummary['source_hashes'],
            'core_calls':wordsummary['core_call_count'],
            'negative_controls_rejected':wordsummary['negative_controls'],
            'cross_program_reuse':wordrecord['cross_program_reuse'],
            'reflection_failed_residual':'8','identity_zero_witness_passed':True,
            'not_added_to_main_execution_total':True},
        'cases':cases,'cold_shared_bank':initial_cold,'cold_restore_bank':restored_cold,
        'shared_program_modular_costs':tables,'resume':resume,'negative_controls':negatives,
        'budget_interruption_and_retry':recovery,
        'whole_run':{'actual_native_core_calls':len(core),
            'cold_word_setup_core_calls':ncold,'gram_policy_observers':ngram,
            'explicit_checker_observers':nexplicit,'tv_comparison_observers':ntv,
            'other_core_calls_not_finely_attributed':remainder,
            'gram_phase_vector_actions_including_controls':sum(g['native_phase_vector_applications'] for g in grams),
            'recorded_uniform_object_binding_checks':sum(g['policy_stats']['certificate_binding_checks'] for g in grams),
            'documented_additional_direct_fixture_bank_checks':len(cases),
            'discarded_early_rejected_object_constructor_bank_checks':2,
            'shared_modular_adder_digit_replays':sum(t['totals_counting_each_actual_table_once']['setup_plus_columns_plus_verification_adder_digit_replays'] for t in tables),
            'checker_elapsed_seconds':r['elapsed_seconds'],
            'core_elapsed_ns_sum':sum(c['elapsed_ns'] for c in core)},
        'limitations':[
            'Complete-law repeated leaf runs, not independent random trials or single-output timings.',
            'Phase-vector actions are cached admitted word-adapter applications, distinct from core calls.',
            'Cold setup includes its word observers; do not add unique_word_observers again to core calls.',
            'certificate_bank_final repeats immutable setup provenance, not an additional construction.',
            'Warm checks perform exact structural comparisons/serialization; their host-bit/time cost is not fully measured.',
            'Explicit-checker vector action count was not instrumented and is unknown.',
            'Retained matrices summed across objects are not peak memory or an implemented shared cache.',
            'Modular tables are counted once per actual factory/inverse object; route snapshots are cumulative.',
            'No complete host-bit cost, typical-path complexity or general efficient Gram oracle is established.']}
    (ROOT/'COST_ACCOUNTING.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'whole_run':out['whole_run'],'cold_shared_bank_core':initial_cold['core_calls'],
                      'cold_restore_core':restored_cold['core_calls'],
                      'accounting_sha256':sha((ROOT/'COST_ACCOUNTING.json').read_bytes())},indent=2))


if __name__=='__main__':
    main()
