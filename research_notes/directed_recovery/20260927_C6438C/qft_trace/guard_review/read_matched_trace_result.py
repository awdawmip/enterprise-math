"""Complete saved-pair integrity review; no scientific imports."""
from pathlib import Path
import gzip,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def sha(x):return hashlib.sha256(x).hexdigest()
gz=(ROOT/'prefix_comparison/SO_TRACE_MATCHED_PREFIX_RESULTS.json.gz').read_bytes();raw=gzip.decompress(gz);d=json.loads(raw)
s=json.loads((ROOT/'prefix_comparison/SO_TRACE_MATCHED_PREFIX_SUMMARY.json').read_bytes())
assert sha(raw)==s['raw_sha256'] and sha(gz)==s['gzip_sha256']
assert len(raw)==s['raw_bytes'] and len(gz)==s['gzip_bytes']
for path,pin in d['source_hashes'].items():assert sha(Path(path).read_bytes())==pin
assert sha((ROOT/'STARTUP_GUARD.json').read_bytes())==d['startup_guard']['sha256']
assert len(d['actual_native_core_calls'])==d['actual_native_core_call_count']==1700
assert len(d['pairs'])==6 and len(d['paid_warmups'])==3
def strict(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
rows=[];measured=0;warm=0
for pair in d['pairs']:
    routes={run['implementation']:run for run in pair['runs']}
    old=routes['BoundaryCheckedUniform'];new=routes['BoundaryCheckedSOTrace']
    for key in ('plans','terminal_mass','numeric_ledger','calculation_actual_core_calls'):
        assert strict(old[key])==strict(new[key])
    for key in ('gram','policy'):
        assert strict(old['counters_before_evidence'][key])==strict(new['counters_before_evidence'][key])
    for key in ('correlations','observer_operations'):
        assert strict(old['evidence']['inherited'][key])==strict(new['evidence']['inherited'][key])
    for run in pair['runs']:
        measured+=run['total_actual_core_calls']
        before,after=run['table_instances_before'],run['table_instances_after'];assert len(before)==len(after)
        for b,a in zip(before,after):
            assert (b['role'],b['parent_factory_index'])==(a['role'],a['parent_factory_index'])
            for key in ('computed_columns','column_adder_digit_replays'):assert b['stats'][key]==a['stats'][key]
        first,last=run['core_call_interval'];assert last-first==run['total_actual_core_calls']
        assert len(run['evidence']['inherited']['observer_operations'])==run['total_actual_core_calls']
    rows.append({k:pair['summary'][k] for k in ('N','a','repetition','old_seconds','new_seconds','core_calls_each')})
for x in d['paid_warmups']:warm+=x['run']['total_actual_core_calls']
cold=0
for x in d['separate_cold_banks']:
    start,stop=x['call_interval'];assert d['actual_native_core_calls'][start:stop]==x['evidence']['setup']['actual_core_calls']
    assert stop-start==x['actual_core_calls'];cold+=x['actual_core_calls']
assert measured==972 and warm==243 and cold==241
start,stop=d['native_admission_call_interval'];assert stop-start==244
assert measured+warm+cold+stop-start==1700
receipt={'status':'PASS_COMPLETE_SAVED_PAIR_REVIEW','reader_sha256':sha(Path(__file__).read_bytes()),'raw_sha256':sha(raw),'gzip_sha256':sha(gz),'pairs':rows,'native_decomposition':{'admission':244,'cold_banks':241,'warmups':243,'measured':972},'science_executed_by_reader':False,'new_measured_columns':0,'scope':'bounded recorded comparisons; uncontrolled timing and possible initial concurrent serialization remain explicit'}
with (ROOT/'guard_review/SO_TRACE_MATCHED_RESULT_REVIEW.json').open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt))
