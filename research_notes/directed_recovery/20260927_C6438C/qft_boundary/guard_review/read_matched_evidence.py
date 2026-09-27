"""Read-only saved-evidence/hash/equality and host timing review; no science run."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT.parent/'prefix_comparison'
blob=(SOURCE/'MATCHED_PREFIX_RESULTS.json.gz').read_bytes()
raw=gzip.decompress(blob)
data=json.loads(raw)
summary=json.loads((SOURCE/'MATCHED_PREFIX_SUMMARY.json').read_bytes())
assert hashlib.sha256(blob).hexdigest()==summary['gzip_sha256']
assert hashlib.sha256(raw).hexdigest()==summary['raw_sha256']
assert (len(blob),len(raw))==(summary['gzip_bytes'],summary['raw_bytes'])
assert len(data['actual_native_core_calls'])==data['actual_native_core_call_count']==summary['actual_native_core_call_count']
paths={
    'compare_guarded_prefixes.py':SOURCE/'compare_guarded_prefixes.py',
    'boundary_uniform.py':ROOT.parent/'boundary_execution/boundary_uniform.py',
    'uniform_feedback.py':ROOT.parents[1]/'sep27-qft-uniform/uniform_execution/uniform_feedback.py'}
assert data['source_hashes']==summary['source_hashes']=={
    name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in paths.items()}
def strict(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def table_content(run):
    # Ordered entries preserve separate instances even when N/b coincide.
    return [{'permutation':x['permutation'],'permutation_sha256':x['permutation_sha256'],
             'queried_columns':x['queried_columns']}
            for x in run['evidence']['inherited']['typed_modular_certificates']]
warm={(x['N'],x['a']):x['run'] for x in data['paid_warmups']}
rows=[]
for pair in data['pairs']:
    info=pair['summary'];key=(info['N'],info['a'])
    old,new=(next(x for x in pair['runs'] if x['implementation']==name)
             for name in ('UniformFeedbackGram','BoundaryCheckedUniform'))
    for field in ('plans','ledger','terminal_mass'):
        assert strict(old[field])==strict(new[field])
    for field in ('correlations','observer_operations'):
        assert strict(old['evidence']['inherited'][field])==strict(new['evidence']['inherited'][field])
    for run in pair['runs']:
        assert run['computed_modular_columns_before']==run['computed_modular_columns_after']
        assert strict(table_content(run))==strict(table_content(warm[key]))
        assert run['total_actual_core_calls']==run['calculation_actual_core_calls']
        assert len(run['evidence']['inherited']['observer_operations'])==run['evidence']['inherited']['report']['actual_positive_path_observations']
        assert len(run['ledger'])==len(run['evidence']['certificates'])==4
    rows.append({**info,'calculation_old_over_new':old['calculation_seconds']/new['calculation_seconds'],
        'through_evidence_old_over_new':old['total_seconds_through_evidence']/new['total_seconds_through_evidence'],
        'strict_saved_semantics_equal':True,
        'all_forward_inverse_instance_column_contents_equal_to_paid_warmup':True,
        'table_instances_in_each_run':len(table_content(old))})
measured_calls=sum(x['total_actual_core_calls'] for p in data['pairs'] for x in p['runs'])
warm_calls=sum(x['run']['total_actual_core_calls'] for x in data['paid_warmups'])
cold_calls=data['shared_cold_certificate']['actual_core_calls']
assert cold_calls==data['shared_cold_certificate']['evidence']['setup']['core_call_count']
report={'scope':'Administrative checks on existing raw evidence; no BRC/model rerun',
    'source_hashes':data['source_hashes'],'raw_sha256':summary['raw_sha256'],
    'gzip_sha256':summary['gzip_sha256'],'raw_bytes':len(raw),'gzip_bytes':len(blob),
    'pairs':rows,'actual_core_calls_total':data['actual_native_core_call_count'],
    'measured_run_core_calls':measured_calls,'paid_warmup_core_calls':warm_calls,
    'cold_word_certificate_core_calls':cold_calls,
    'remaining_shared_native_admission_core_calls':data['actual_native_core_call_count']-measured_calls-warm_calls-cold_calls,
    'cold_word_certificate_seconds':data['shared_cold_certificate']['elapsed_seconds'],
    'paid_warmups':[{'N':x['N'],'a':x['a'],
        'calculation_seconds':x['run']['calculation_seconds'],
        'through_evidence_seconds':x['run']['total_seconds_through_evidence'],
        'actual_core_calls':x['run']['total_actual_core_calls']} for x in data['paid_warmups']],
    'calculation_ratio_range':[min(x['calculation_old_over_new'] for x in rows),max(x['calculation_old_over_new'] for x in rows)],
    'through_evidence_ratio_range':[min(x['through_evidence_old_over_new'] for x in rows),max(x['through_evidence_old_over_new'] for x in rows)],
    'summed_measured_calculation_old_over_new':sum(x['old_seconds'] for x in rows)/sum(x['new_seconds'] for x in rows),
    'summed_measured_through_evidence_old_over_new':sum(x['old_total_seconds'] for x in rows)/sum(x['new_total_seconds'] for x in rows),
    'claim_exclusions':['independent trials','controlled system load','cold startup speedup','full output law','asymptotic speedup']}
(ROOT/'MATCHED_PREFIX_METADATA_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
