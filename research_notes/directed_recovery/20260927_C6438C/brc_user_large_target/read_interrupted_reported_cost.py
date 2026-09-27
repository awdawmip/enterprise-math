"""Administrative extraction of saved reported costs; no native-cell audit."""
from pathlib import Path
from collections import Counter
import gzip
import hashlib
import json

ROOT=Path(__file__).resolve().parent
RUN=ROOT/'runs/full'
sha=lambda b:hashlib.sha256(b).hexdigest()
cost=Counter()
streams={}
catalog_calls=None
last_bit=None
members=0
offset=0
with (RUN/'EVIDENCE.jsonl.gz').open('rb') as handle:
    for line in (RUN/'MEMBER_INDEX.jsonl').open('rb'):
        row=json.loads(line)
        assert row['sequence']==members and row['offset']==offset
        packed=handle.read(row['compressed_bytes'])
        assert len(packed)==row['compressed_bytes'] and sha(packed)==row['compressed_sha256']
        raw=gzip.decompress(packed)
        assert sha(raw)==row['raw_sha256'] and len(raw)==row['raw_bytes']
        event=json.loads(raw)
        assert event['sequence']==members and event['kind']==row['kind']
        if event['kind']=='typed_operation':
            item=Counter(event['cost'])
            item['typed_operations']=1
            item['native_kernel_calls_delta']=event['native_kernel_calls_delta']
            cost.update(item)
            streams.setdefault(event['stream'],Counter()).update(item)
        elif event['kind']=='native_catalog_admission':
            catalog_calls=len(event['all_native_records'])
        elif event['kind']=='adjacent_bit_end':
            last_bit=event['bit_index']
        members+=1
        offset+=len(packed)
    tail=handle.read()
record={'status':'INTERRUPTED_ANCILLARY_REPORTED_COST_EXTRACTION_ONLY',
        'indexed_members':members,'indexed_bytes':offset,'unindexed_tail_bytes':len(tail),
        'last_completed_bit_index':last_bit,'reported_arithmetic_cost':dict(cost),
        'reported_stream_costs':{k:dict(v) for k,v in streams.items()},
        'observed_catalog_admission_calls':catalog_calls,
        'reader_sha256':sha(Path(__file__).read_bytes()),
        'evidence_sha256':sha((RUN/'EVIDENCE.jsonl.gz').read_bytes()),
        'index_sha256':sha((RUN/'MEMBER_INDEX.jsonl').read_bytes()),
        'scope':'Extracted completed indexed operation cost fields only. Hash/framing verified; digits and full algorithm history NOT audited. Interrupted or unreturned primitive work, labels, host control and serialization may be unaccounted. No scientific completion or resumability claimed.'}
with (RUN/'INTERRUPTED_REPORTED_COST.json').open('x',encoding='utf-8') as out:
    out.write(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
