"""Administrative byte/framing audit of the cancelled ancillary stream; no scientific replay."""
from pathlib import Path
import hashlib,json,zlib

ROOT=Path(__file__).resolve().parent.parent
RUN=ROOT/'runs/full'
def sha(b):return hashlib.sha256(b).hexdigest()
def digest_file(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
source=Path(__file__).read_bytes()
stream=RUN/'EVIDENCE.jsonl.gz';index=RUN/'MEMBER_INDEX.jsonl'
before=(stream.stat().st_size,index.stat().st_size)
index_bytes=index.read_bytes()
assert index_bytes.endswith(b'\n'),'Index has a partial final line; preserve and separately identify before reviewing'
rows=[json.loads(line) for line in index_bytes.splitlines()]
cursor=0;raw_total=0;prefix_hasher=hashlib.sha256()
with stream.open('rb') as f:
 for number,row in enumerate(rows):
  assert row['sequence']==number and row['offset']==cursor
  packed=f.read(row['compressed_bytes'])
  assert len(packed)==row['compressed_bytes'] and sha(packed)==row['compressed_sha256']
  decoder=zlib.decompressobj(wbits=31);raw=decoder.decompress(packed)+decoder.flush()
  assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
  assert len(raw)==row['raw_bytes'] and sha(raw)==row['raw_sha256'] and raw.endswith(b'\n')
  # Only gzip framing and byte commitments are checked. Do not parse arithmetic,
  # assess native digit transitions, recompute an answer or claim a final outcome.
  prefix_hasher.update(packed);cursor+=len(packed);raw_total+=len(raw)
 tail_hasher=hashlib.sha256();tail_bytes=0
 for b in iter(lambda:f.read(1048576),b''):
  tail_hasher.update(b);tail_bytes+=len(b)
assert before==(stream.stat().st_size,index.stat().st_size),'Cancelled evidence changed during read'
assert cursor+tail_bytes==before[0]
logs=json.loads((RUN/'ACTUAL_EXECUTION_TOOL_LOG.json').read_bytes())
last=logs[-1]
assert last['tool_name']=='write_stdin' and last['arguments']['chars']=='\u0003'
assert last['result']['chunk_id']=='c13a3f' and last['result']['exit_code']==1
assert not (RUN/'SUMMARY.json').exists() and not (RUN/'FAILED.json').exists()
receipt={
 'status':'PRESERVED_INTERRUPTED_ANCILLARY_BYTES_NOT_SCIENTIFIC_COMPLETION',
 'formal_target':'input_block.json only; this cancelled full-string attempt supplies no formal factoring conclusion',
 'reader_sha256':sha(source),
 'scope':'Administrative closed-gzip framing and exact byte commitments only; no scientific stream/chronology audit, arithmetic import, replay or tail interpretation',
 'stream':{'local_path':'runs/full/EVIDENCE.jsonl.gz','bytes':before[0],'sha256':digest_file(stream),'published_remotely':False},
 'index':{'local_path':'runs/full/MEMBER_INDEX.jsonl','bytes':before[1],'sha256':sha(index_bytes),'published_remotely':False,'complete_jsonl_lines':len(rows),'partial_line_bytes':0},
 'closed_indexed_prefix':{'compressed_range_half_open':[0,cursor],'compressed_bytes':cursor,
     'compressed_sha256':prefix_hasher.hexdigest(),'member_count':len(rows),'sequence_range_inclusive':[0,len(rows)-1],
     'decoded_bytes_total':raw_total,'every_member_compressed_and_raw_commitment_verified':True,
     'every_indexed_member_gzip_closed_with_no_extra_bytes':True,
     'last_index_entry':rows[-1]},
 'unindexed_tail':{'compressed_range_half_open':[cursor,before[0]],'bytes':tail_bytes,'sha256':tail_hasher.hexdigest(),
     'interpretation':'Preserved exactly; not parsed or counted as a scientific completed operation, resumed state or complete gzip member'},
 'actual_interruption':{'tool_chunk_id':'c13a3f','process_exit_code':1,'reason':'User selected p*q, replacing the prior two-target fallback'},
 'terminal_scientific_summary_emitted':False,'internal_failure_receipt_claimed':False,
 'scientific_completion_claimed':False,'automatic_resume_supported':False,
 'remote_scope':'Publish this receipt, original STARTED, actual tool log and user target confirmation; keep ancillary raw stream and index local',
 'guard_updated':False,'raw_stream_or_index_modified':False
}
assert before==(stream.stat().st_size,index.stat().st_size)
with (RUN/'INTERRUPTED_EVIDENCE_PRESERVATION.json').open('x',encoding='utf-8',newline='\n') as f:
 f.write(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))
