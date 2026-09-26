"""Typed gcd versus frozen actual gcd, including nonunits, zeros and signs."""
from pathlib import Path
from copy import deepcopy
import gzip,hashlib,json
from lazy_gcd import typed_gcd_trace,verify_typed_gcd
from stage78.shor_benchmark import gcd_brc
from stage45.brc_loop_recheck import CALLS

ROOT=Path(__file__).resolve().parent
cases=[]
for left,right in [(0,0),(0,15),(15,0),(1,1),(12,18),(21,35),(48,18),
                   (55,25),(8,21),(-12,18),(12,-18),(-12,-18),(144,96),(999,333)]:
    old=gcd_brc(left,right)
    certificate=typed_gcd_trace(left,right)
    assert certificate['value']==old
    verified=verify_typed_gcd(certificate)
    cases.append({'inputs':[left,right],'old_actual_value':old,
                  'typed_certificate':certificate,'replay':verified})
bad=deepcopy(cases[4]['typed_certificate'])
bad['steps'][0]['remainder']+=1
try:verify_typed_gcd(bad)
except ValueError:rejected=True
else:raise AssertionError('changed gcd remainder accepted')
out={'status':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED','cases':cases,
     'all_old_actual_values_equal':True,'changed_remainder_rejected':rejected,
     'typed_digit_replays_initial_runs':sum(c['typed_certificate']['cost']['adder_digit_replays'] for c in cases),
     'native_core_call_count':len(CALLS),'native_core_calls':CALLS,
     'reference_scope':'frozen gcd_brc isolated regression only; new gcd uses no ordinary remainder or dense Euclid graph'}
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
(ROOT/'LAZY_GCD_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
summary={k:v for k,v in out.items() if k not in ('cases','native_core_calls')}
summary['compared_cases']=len(cases)
summary['payload_sha256']=hashlib.sha256(raw).hexdigest()
(ROOT/'LAZY_GCD_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))
