"""Finalize byte/source evidence after complete scientific reruns; no dynamics."""
from pathlib import Path
import gzip, hashlib, json, sys
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent

def meta(name):
    raw = (ROOT/name).read_bytes()
    row = {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    if name.endswith('.json.gz'):
        payload=gzip.decompress(raw)
        row.update(uncompressed_bytes=len(payload),payload_sha256=hashlib.sha256(payload).hexdigest())
    return row

log=json.loads((ROOT/'EXECUTION_CHANGE_LOG.json').read_text(encoding='utf-8'))
log['after']={name:meta(name) for name in log['before']}
assert log['after']['certified_word_compiler.py']['sha256']=='e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d'
log['state']='REVALIDATED_AFTER_PATCH'
log['fresh_executions']={
    'compiler':{'actual_BRC_calls':738,'payload_sha256':log['after']['CERTIFIED_WORD_COMPILER_CHECKS.json.gz']['payload_sha256']},
    'streaming':{'actual_BRC_calls':6724,'payload_sha256':log['after']['COMPILED_STREAMING_RESULTS.json.gz']['payload_sha256'],'scientific_before_after_equality':'POST_CAP_FIX_REPLAY_CHECK.json'},
    'factorization':{'actual_BRC_calls':16991,'payload_sha256':log['after']['COMPILED_FACTORIZATION_RESULTS.json.gz']['payload_sha256']}}
log['io_only_check']={'file':'LARGE_CERTIFICATE_IO_SUMMARY.json','decimal_digits':5001,'actual_BRC_calls':0}
log['cli_cross_process']={
    'partial':meta('CLI_COMPILE_PARTIAL_N15.json.gz'),
    'resumed':meta('CLI_RESUMED_N15.json.gz'),
    'scope':'Compilation cursor restored in a new process; N15 becomes COMPLETE 3*5. RNG and an interrupted live factor tree are not restored.',
    'stochastic_budget_verified':False}
(ROOT/'EXECUTION_CHANGE_LOG.json').write_text(json.dumps(log,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'state':log['state'],'compiler_sha256':log['after']['certified_word_compiler.py']['sha256'],'fresh_executions':log['fresh_executions'],'cli_resumed':log['cli_cross_process']['resumed']}))
