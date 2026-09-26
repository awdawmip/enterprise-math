"""Declared integer fixtures and full provenance replay; no QFT reference."""
from pathlib import Path
import copy
import gzip
import hashlib
import json
from typed_integer_prechecks import (multiply, divide, power, compare,
    perfect_power, wilson_primality, verify_precheck)
from sparse_modular import CALLS, digest

fixtures = []
for left,right,expected in [(0,9,0),(1,19,19),(7,9,63),(13,17,221),(31,31,961)]:
    result,trace = multiply(left,right)
    assert result == expected
    fixtures.append({'operation':'multiply','input':[left,right],'expected':expected,'trace':trace})
for value,modulus,q,r in [(0,7,0,0),(5,9,0,5),(63,5,12,3),(221,13,17,0),(961,31,31,0)]:
    result_q,result_r,trace = divide(value,modulus)
    assert (result_q,result_r)==(q,r)
    fixtures.append({'operation':'divide','input':[value,modulus],'expected':[q,r],'trace':trace})
for base,e,expected in [(2,0,1),(3,4,81),(5,3,125),(2,16,65536)]:
    result,trace = power(base,e)
    assert result == expected
    fixtures.append({'operation':'power','input':[base,e],'expected':expected,'trace':trace})
for left,right,expected in [(0,0,0),(0,1,-1),(1,0,1),(17,17,0),(17,18,-1),(19,18,1)]:
    result,trace = compare(left,right)
    assert result == expected
    fixtures.append({'operation':'compare','input':[left,right],'expected':expected,'trace':trace})

certificates=[]
checks=[]
for N,expected in [(2,None),(3,None),(4,{'base':2,'exponent':2}),
    (64,{'base':2,'exponent':6}),(81,{'base':3,'exponent':4}),
    (225,{'base':15,'exponent':2}),(729,{'base':3,'exponent':6}),
    (65,None),(72,None)]:
    certificate=perfect_power(N)
    assert certificate['power']==expected
    verified=verify_precheck(certificate)
    checks.append(verified)
    certificates.append(certificate)

for N,expected in [(2,'PRIME'),(3,'PRIME'),(4,'COMPOSITE'),(5,'PRIME'),
    (9,'COMPOSITE'),(15,'COMPOSITE'),(17,'PRIME'),(21,'COMPOSITE'),
    (25,'COMPOSITE'),(31,'PRIME')]:
    certificate=wilson_primality(N)
    assert certificate['status']==expected
    verified=verify_precheck(certificate)
    checks.append(verified)
    certificates.append(certificate)

tampered=copy.deepcopy(certificates[-1])
tampered['steps'][0]['output_residue'] += 1
try:
    verify_precheck(tampered)
except ValueError:
    tamper_rejected=True
else:
    raise AssertionError('Changed Wilson product trace accepted')

tampered_power=copy.deepcopy(next(c for c in certificates if c['schema']=='BRC_PERFECT_POWER_V1' and c['N']==81))
tampered_power['power']['base']=9
try:
    verify_precheck(tampered_power)
except ValueError:
    power_tamper_rejected=True
else:
    raise AssertionError('Changed perfect-power answer accepted')

raw=json.dumps({'integer_fixtures':fixtures,'certificates':certificates},
    ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
compressed=gzip.compress(raw,mtime=0)
folder=Path(__file__).resolve().parent
(folder/'PRECHECK_CERTIFICATES.json.gz').write_bytes(compressed)
summary={'researcher':'EM-DIRECT-C6438C','activity':'RA-CAAAC604CB513AEA8BBC1DFC',
    'status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED',
    'integer_fixture_count':len(fixtures),'perfect_power_cases':9,'wilson_cases':10,
    'full_replay_checks':checks,'tampered_wilson_trace_rejected':tamper_rejected,
    'tampered_perfect_power_answer_rejected':power_tamper_rejected,
    'certificate_archive':{'filename':'PRECHECK_CERTIFICATES.json.gz',
      'gzip_sha256':hashlib.sha256(compressed).hexdigest(),
      'uncompressed_sha256':hashlib.sha256(raw).hexdigest(),
      'uncompressed_bytes':len(raw),'compressed_bytes':len(compressed)},
    'native_calls':CALLS,'no_ideal_reference_execution':True,
    'cost_note':'Wilson uses N-2 modular products; no efficiency or input-size polynomial claim'}
(folder/'PRECHECK_RESULTS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k not in ('full_replay_checks','native_calls')},ensure_ascii=False))
