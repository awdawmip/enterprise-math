"""Read existing complete evidence and verify its internal recording links only."""
from pathlib import Path
from copy import deepcopy
import gzip,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def digest(raw):return hashlib.sha256(raw).hexdigest()
raw_gz=(ROOT/'signed_gap/SIGNED_GAP_RESULTS.json.gz').read_bytes()
raw=gzip.decompress(raw_gz); d=json.loads(raw)
s=json.loads((ROOT/'signed_gap/SIGNED_GAP_SUMMARY.json').read_bytes())
assert digest(raw_gz)==s['artifact_sha256'] and digest(raw)==s['payload_sha256']
assert len(raw)==s['raw_bytes'] and len(raw_gz)==s['gzip_bytes']
for name,pin in s['source_sha256'].items():assert digest((ROOT/'signed_gap'/name).read_bytes())==pin
assert digest((ROOT/'STARTUP_GUARD.json').read_bytes())==d['startup_guard']['sha256']
assert d['actual_core_call_count']==s['actual_core_call_count']==len(d['actual_core_calls'])==1
def semantic(c):
    c=deepcopy(c); c['actual_integer_evidence']['arithmetic_stats']['native_kernel_calls_delta']=0
    return json.dumps(c,sort_keys=True,separators=(',',':'))
case_rows=[]
for case in d['cases']:
    c=case['certificate']; a=c['actual_integer_evidence']; inp=case['inputs']
    assert len(c['requests'])==inp['R']
    assert case['values']==[r['value'] for r in c['requests']]
    assert semantic(c)==semantic(case['verification']['replay_certificate'])
    assert case['verification']['requests_replayed']==inp['R']
    previous=0
    for i,req in enumerate(c['requests']):
        assert req['inputs']==dict(inp,r=i,stride=1)
        assert req['signed_operations_start']==previous
        start,scale,outer,stop=(req[k] for k in ('signed_operations_start','scale_operations_stop','outer_operations_start','signed_operations_stop'))
        assert start<=scale<=outer<stop<=len(a['signed_operations'])
        assert a['signed_operations'][stop-1]['result']==req['value']
        assert len(req['weight_query_indices'])==3
        for qi,key,delta in zip(req['weight_query_indices'],('J_zero','J_plus','J_minus'),(0,1,-1)):
            q=a['window_weight_queries'][qi]
            assert q['value']==req['weights'][key] and q['value']>=0
            assert q['inputs']=={'H':req['H'],'P':2,'R':inp['R'],'V':req['U'],'d':delta,'r':i}
            assert scale<=q['signed_operations_start']<=q['signed_operations_stop']<=outer
        previous=stop
    assert previous==len(a['signed_operations'])
    brute=case['typed_enumeration']; buckets=[0 for _ in range(inp['R'])]
    for pair in brute['pair_observations']:
        residue=pair['residue']; assert buckets[residue]==pair['bucket_before']
        buckets[residue]=pair['bucket_after']
        assert brute['actual_integer_evidence']['signed_operations'][pair['signed_operations_stop']-1]['result']==pair['bucket_after']
    assert buckets==case['values']
    case_rows.append({'inputs':inp,'values':case['values'],'recorded_pairs':len(brute['pair_observations']),'strict_positive_trace_equality':True})
assert len(d['input_rejections'])==15 and all(x['rejected'] and x['typed_operations']==0 for x in d['input_rejections'])
assert len(d['tamper_rejections'])==9 and all(x['rejected'] for x in d['tamper_rejections'])
negative=[]
for item in d['tamper_rejections']:
    assert item['attempted_certificate_typed_key_encoding']
    for replay in item['actual_replay_certificates']:
        assert replay['schema']=='BRC_ONE_NEGATIVE_SIGNED_GAP_V1'
        assert replay['actual_integer_evidence']['signed_operations']
    negative.append({'name':item['name'],'full_replays':len(item['actual_replay_certificates'])})
receipt={'status':'PASS_RECORDED_LINKS','science_executed_by_reader':False,'reader_sha256':digest(Path(__file__).read_bytes()),'payload_sha256':digest(raw),'compressed_sha256':digest(raw_gz),'case_count':len(case_rows),'residue_count':sum(len(c['values']) for c in case_rows),'pair_count':sum(c['recorded_pairs'] for c in case_rows),'cases':case_rows,'negative_replays':negative,'native_calls':d['actual_core_calls']}
target=ROOT/'guard_review/SIGNED_GAP_RECORD_REVIEW.json'
with target.open('x',encoding='utf-8') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps(receipt))
