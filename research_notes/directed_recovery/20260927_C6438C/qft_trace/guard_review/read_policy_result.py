"""Read-only examination of saved policy outputs, not scientific replay."""
from pathlib import Path
import gzip,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def sha(x):return hashlib.sha256(x).hexdigest()
gz=(ROOT/'policy_execution/SO_TRACE_POLICY_RESULTS.json.gz').read_bytes(); raw=gzip.decompress(gz);d=json.loads(raw)
s=json.loads((ROOT/'policy_execution/SO_TRACE_POLICY_SUMMARY.json').read_bytes())
c=json.loads((ROOT/'policy_execution/SO_TRACE_POLICY_COST_ACCOUNTING.json').read_bytes())
assert sha(raw)==s['raw_sha256']==c['raw_sha256'];assert sha(gz)==s['gzip_sha256']==c['gzip_sha256']
assert len(raw)==s['raw_bytes'] and len(gz)==s['gzip_bytes']
assert len(d['actual_core_calls'])==d['core_call_count']==1287
paths={'so_trace_feedback.py':ROOT/'policy_execution/so_trace_feedback.py','check_so_trace_policy.py':ROOT/'policy_execution/check_so_trace_policy.py','so_trace_certificates.py':ROOT/'trace_bank/so_trace_certificates.py','boundary_uniform.py':ROOT.parent/'sep27-qft-boundary/boundary_execution/boundary_uniform.py'}
for name,pin in d['source_hashes'].items():assert sha(paths[name].read_bytes())==pin
rows=[]
def strict(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'))
def checkguard(e):
    g=e['boundary_guard'];assert g['active_depth']==0 and g['owner_active'] is False
for fixture in d['fixtures']:
    old,new=(fixture[name] for name in ('old_boundary','so_boundary'))
    for e in (old,new):checkguard(e)
    for key in ('correlations','observer_operations'):
        assert strict(old['inherited'][key])==strict(new['inherited'][key])
    for key in ('history','query_requests','distinct_queries','actual_positive_path_observations','native_phase_vector_applications','cached_matrix_scalar_slots'):
        assert old['inherited']['report'][key]==new['inherited']['report'][key]
    assert old['certificate_bank_sha256']!=new['certificate_bank_sha256']
    assert len(fixture['steps'])==4
    rows.append({'N':fixture['N'],'a':fixture['a'],'observer_count_per_route':len(new['inherited']['observer_operations']),'full_correlations_equal':True,'full_observer_stream_equal':True})
for label in ('old_cold_bank','new_cold_bank'):
    setup=d[label]['setup'];start,stop=setup['call_interval']
    assert d['actual_core_calls'][start:stop]==setup['actual_core_calls']
    assert stop-start==setup['core_call_count']
negatives=d['cursor_negative_controls']+d['new_exact_bank_type_controls']
assert len(negatives)==9
for item in negatives:
    assert item['rejected']
    start,stop=item['call_interval'];assert stop-start==item['actual_core_calls']
    e=item['failed_replay_evidence']
    if e is not None:
        checkguard(e);assert len(e['inherited']['observer_operations'])==item['actual_core_calls']
for field in ('pending_snapshot','original','restored'):checkguard(d['pending_restore'][field])
assert d['pending_restore']['strict_new_cursor_equal'] and not d['pending_restore']['query_cache_or_rng_restored']
for field in ('failed_attempt','retried','fresh'):checkguard(d['budget_recovery'][field])
assert d['budget_recovery']['same_bit_committed_once']
before=d['budget_recovery']['failed_attempt']['inherited']['observer_operations'];after=d['budget_recovery']['retried']['inherited']['observer_operations']
assert strict(before)==strict(after[:len(before)])
assert sum(c['whole_checker']['core_call_decomposition'].values())==1287
receipt={'status':'PASS_COMPLETE_RECORD_REVIEW','reader_sha256':sha(Path(__file__).read_bytes()),'raw_sha256':sha(raw),'gzip_sha256':sha(gz),'fixtures':rows,'native_call_decomposition':c['whole_checker']['core_call_decomposition'],'negative_controls':len(negatives),'science_executed_by_reader':False,'scope':'saved complete-record links and source review, not an independent scientific implementation'}
with (ROOT/'guard_review/SO_TRACE_POLICY_RESULT_REVIEW.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt))
