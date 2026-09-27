"""Administrative metadata extraction only; no scientific modules imported.

Explicit call-graph ownership prevents nested historical certificates from
being charged as new executions. All summation here is resource metadata.
"""
from pathlib import Path
import gzip
import hashlib
import json

ROOT=Path(__file__).resolve().parent
AGG=ROOT.parent/'aggregation'


def load(path):
    raw=gzip.decompress(path.read_bytes())
    return json.loads(raw),hashlib.sha256(raw).hexdigest()


def inverse_cost(query):
    table=query.get('inverse_table')
    if table is None:
        return {'instances':0,'setup':0,'columns':0,'verification':0,'total':0}
    values={'instances':1,'setup':table['stats']['setup_adder_digit_replays'],
        'columns':table['stats']['column_adder_digit_replays'],
        'verification':query['inverse_permutation_replay']['replayed_adder_digits']}
    values['total']=values['setup']+values['columns']+values['verification']
    return values


def address_cost(record):
    return {'fresh_order_replay':record['metrics']['order_replay_adder_digit_replays'],
            'fresh_address_only':record['metrics']['address_only_adder_digit_replays']}


def query_cost(query):
    verification=query['address_verification']
    cost=address_cost(verification['replay'])
    cost.update(inherited_permutation_replay=verification['inherited_permutation_replay']['replayed_adder_digits'],
        index_or_count_arithmetic=query.get('index_arithmetic_stats',{}).get('adder_digit_replays',0),
        count_inverse=inverse_cost(query))
    cost['total']=sum(cost[k] for k in ('fresh_order_replay','fresh_address_only',
        'inherited_permutation_replay','index_or_count_arithmetic'))+cost['count_inverse']['total']
    return cost


def one_program(program):
    tables=program['program_table_instances']
    result={'instances':len(tables),
        'setup':sum(t['stats']['setup_adder_digit_replays'] for t in tables),
        'columns':sum(t['stats']['column_adder_digit_replays'] for t in tables),
        'verification':sum(v['replayed_adder_digits'] for v in program['program_permutation_verifications'])}
    result['total']=result['setup']+result['columns']+result['verification']
    return result


def phase_counts(paid,baseline=None):
    suffixes=[q['suffix_evidence'] for q in paid['aggregation_queries'] if 'suffix_evidence' in q]
    weighted=sum(op['name'].endswith(':weighted_suffix') for op in paid['observer_operations'])
    return {'ordinary_phase_vector_actions':paid['inherited_action_stats']['native_phase_vector_applications'],
        'counted_suffix_phase_vector_actions':sum(s['inherited_action_stats']['native_phase_vector_applications'] for s in suffixes),
        'ordinary_signed_observer_operations':len(paid['observer_operations'])-weighted,
        'counted_suffix_signed_observer_operations':weighted+sum(len(s['observer_operations']) for s in suffixes),
        'counted_parent_weighted_observer_operations':weighted,
        'baseline_phase_vector_actions':None if baseline is None else baseline['inherited_action_stats']['native_phase_vector_applications'],
        'baseline_signed_observer_operations':None if baseline is None else len(baseline['observer_operations'])}


def audit(data,raw_hash,kind):
    assert data['source_sha256']['paid_aggregator.py']=='ff7cf4c32d5cd86c68a2602c4991972004762343ecff4de72e735441b1a68768'
    main=kind=='main'
    groups=data['aggregation_evidence'] if main else [{'paid':data['aggregation_evidence'],'baseline':data['baseline_evidence']}]
    programs=data['programs'] if main else [data['program']]
    aliases=data['alias_evidence'] if main else [data['alias_evidence']]
    queries=[q for e in groups for q in e['paid']['aggregation_queries']]
    # The checker creates one initial address per target, then performs exactly
    # one ordinary and one counted query using that address. This explicit
    # positional map is checked rather than scanning embedded copies.
    assert len(queries)==2*len(data['address_certificates'])
    case_rows=[]
    for j,(case,address) in enumerate(zip(data['cases'],data['address_certificates'])):
        ordinary,counted=queries[2*j:2*j+2]
        assert ordinary['target']==counted['target']==address['inputs']['z']==case['target']
        assert ordinary['depth']==counted['depth']==case['depth']
        initial_order=address['order_certificate']['metrics']['total_adder_digit_replays']
        initial=address_cost(address)
        ordinary_cost,counted_cost=query_cost(ordinary),query_cost(counted)
        setup=initial_order+sum(initial.values())
        case_rows.append({'N':case['N'],'a':case['a'],'depth':case['depth'],
            'history':case.get('history'),'target':case['target'],'status':address['status'],
            'initial_order_discovery':initial_order,'initial_address_recovery':initial,
            'ordinary_gamma':ordinary_cost,'counted_gamma':counted_cost,
            'initial_plus_ordinary_gamma':setup+ordinary_cost['total'],
            'initial_plus_counted_gamma':setup+counted_cost['total'],
            'actual_checker_both_routes_total':setup+ordinary_cost['total']+counted_cost['total'],
            'phase_costs_from_case':{k:case[k] for k in ('ordinary_cost','leading_cost','baseline_cost') if k in case}})
    negative_rows=[]
    for control in data.get('negative_controls',[]):
        name=control['name']; failure=control.get('failed_replay_evidence') or {}
        fresh=failure.get('replay',failure)
        digits=fresh.get('metrics',{}).get('total_adder_digit_replays',0)
        missing_inherited=0
        # Production adapter verifies the address before the inherited table;
        # these rejected address calls no longer execute a discarded replay.
        negative_rows.append({'name':name,'retained_fresh_execution_adder_digits':digits,
            'source_derived_unretained_inherited_replay_adder_digits':missing_inherited,
            'total':digits+missing_inherited})
    program_rows=[one_program(p) for p in programs]
    totals={'program_initialization':sum(p['total'] for p in program_rows),
        'initial_order_discoveries':sum(c['initial_order_discovery'] for c in case_rows),
        'initial_address_order_replays':sum(c['initial_address_recovery']['fresh_order_replay'] for c in case_rows),
        'initial_address_only':sum(c['initial_address_recovery']['fresh_address_only'] for c in case_rows),
        'query_order_replays':sum(c[k]['fresh_order_replay'] for c in case_rows for k in ('ordinary_gamma','counted_gamma')),
        'query_address_only':sum(c[k]['fresh_address_only'] for c in case_rows for k in ('ordinary_gamma','counted_gamma')),
        'query_inherited_permutation_replays':sum(c[k]['inherited_permutation_replay'] for c in case_rows for k in ('ordinary_gamma','counted_gamma')),
        'ordinary_index_arithmetic':sum(c['ordinary_gamma']['index_or_count_arithmetic'] for c in case_rows),
        'counted_index_arithmetic':sum(c['counted_gamma']['index_or_count_arithmetic'] for c in case_rows),
        'counted_inverse_setup':sum(c['counted_gamma']['count_inverse']['setup'] for c in case_rows),
        'counted_inverse_columns':sum(c['counted_gamma']['count_inverse']['columns'] for c in case_rows),
        'counted_inverse_replays':sum(c['counted_gamma']['count_inverse']['verification'] for c in case_rows),
        'independent_alias_reference_discovery':sum(a['metrics']['total_adder_digit_replays'] for a in aliases),
        'negative_retained_replay_work':sum(n['retained_fresh_execution_adder_digits'] for n in negative_rows),
        'negative_source_derived_unretained_inherited_replays':sum(n['source_derived_unretained_inherited_replay_adder_digits'] for n in negative_rows)}
    totals['total_counted_adder_digit_replays']=sum(totals.values())
    assert len(data['native_core_call_receipts'])==data['actual_native_core_calls']
    return {'source_payload_sha256':raw_hash,'case_costs':case_rows,'program_instances':program_rows,
        'negative_control_costs':negative_rows,'totals':totals,
        'phase_and_observer_groups':[phase_counts(e['paid'],e.get('baseline')) for e in groups],
        'actual_native_core_call_receipts':data['actual_native_core_calls'],
        'cycle_or_certificate_nested_copies_counted_as_new_work':False,
        'digits_do_not_include_phase_native_observer_or_all_host_bit_work':True}


def main():
    data,h=load(AGG/'PAID_AGGREGATION_RESULTS.json.gz')
    boundary,bh=load(AGG/'K_ZERO_BOUNDARY_RESULTS.json.gz')
    order=json.loads((ROOT.parent/'period_discovery/ODD_PART_SUMMARY.json').read_bytes())
    n97=next(c for c in order['case_summary'] if c['N']==97)
    output={'schema':'PAID_PIPELINE_CALL_GRAPH_RESOURCE_AUDIT_V1','metadata_only_no_new_scientific_execution':True,
        'main':audit(data,h,'main'),'K_zero':audit(boundary,bh,'boundary'),
        'standalone_N97_b5_R96_order_comparison':n97,
        'ownership_rule':'Only explicit initial address list and successful query list, plus explicit failure replay roots are charged. Supplied old certificates nested under those roots are provenance, not new calls.',
        'negative_receipt_status':'Production ff7cf4 validates the address first. No inherited permutation replay is executed or charged on the three rejected address paths. Superseded source-derived charges remain only in OLD_RUN artifacts.'}
    path=ROOT/'END_TO_END_COST_ACCOUNTING.json'
    path.write_text(json.dumps(output,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'main':output['main']['totals'],'K_zero':output['K_zero']['totals'],
        'cases':[{k:c[k] for k in ('N','a','depth','history','target','initial_order_discovery','initial_address_recovery','ordinary_gamma','counted_gamma','initial_plus_ordinary_gamma','initial_plus_counted_gamma','actual_checker_both_routes_total')} for c in output['main']['case_costs']],
        'phase_groups':output['main']['phase_and_observer_groups'],
        'accounting_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))


if __name__=='__main__': main()
