"""Run the original CF path and preserve success, zero, bad-base and EOF outputs."""
from pathlib import Path
from copy import deepcopy
import gzip,hashlib,json,random
from cf_universal_factorization import factor_integer_cf_universal,verify_factorization
from stage45.brc_loop_recheck import CALLS,verify_vendor
ROOT=Path(__file__).resolve().parent

class Zero:
    def randrange(self,*args):return args[0] if len(args)==2 else 0
class Empty:
    def randrange(self,*args):raise EOFError

def main():
    kernel=verify_vendor();results=[];checks=[]
    for number,expected in [(15,[(3,1),(5,1)]),(21,[(3,1),(7,1)]),(35,[(5,1),(7,1)]),(55,[(5,1),(11,1)]),(225,[(3,2),(5,2)])]:
        result=factor_integer_cf_universal(number,random.Random(20260926+number),failure_bits=2,max_attempts=12,
            base_provider=lambda N: [2]*12)
        assert result['status']=='COMPLETE',(number,result['unresolved'])
        assert [(p['prime'],p['exponent']) for p in result['prime_factors']]==expected
        for event in result['events']:
            if event['action']!='SAMPLED_SHOR_SPLIT':continue
            assert event['original_cf_support_certificate']['postprocessing_extension'] is False
            for attempt in event['attempt_result']['attempts']:
                post=attempt.get('postprocessing',{})
                assert 'hybrid' not in post and 'primary_postprocessing' not in post
        results.append(result);checks.append(verify_factorization(result))
        print(json.dumps({'N':number,'status':result['status'],'prime_factors':expected}),flush=True)
    zero=factor_integer_cf_universal(21,Zero(),failure_bits=2,max_attempts=1,base_provider=lambda N:[2])
    assert zero['status']=='PARTIAL' and zero['unresolved'][0]['cofactor']==21
    event=next(e for e in zero['events'] if e['action']=='SAMPLED_SHOR_SPLIT')
    assert event['attempt_result']['attempts'][0]['postprocessing']['status']=='ZERO_PHASE_RETRY'
    results.append(zero);checks.append(verify_factorization(zero))
    bad=factor_integer_cf_universal(15,random.Random(4),failure_bits=2,max_attempts=1,base_provider=lambda N:[14])
    assert bad['status']=='PARTIAL' and bad['unresolved'][0]['cofactor']==15
    results.append(bad);checks.append(verify_factorization(bad))
    eof=factor_integer_cf_universal(21,Empty(),failure_bits=2,max_attempts=1,base_provider=lambda N:[2])
    event=next(e for e in eof['events'] if e['action']=='SAMPLED_SHOR_SPLIT')
    assert eof['status']=='PARTIAL' and event['attempt_result']['status']=='INCOMPLETE_RANDOM_SOURCE'
    assert 'postprocessing' not in event['attempt_result']['attempts'][0]
    results.append(eof);checks.append(verify_factorization(eof))
    negative=deepcopy(zero);negative['status']='COMPLETE'
    try:verify_factorization(negative)
    except ValueError:pass
    else:raise AssertionError('partial result hidden')
    out={'schema':'ORIGINAL_CF_UNIVERSAL_ACTUAL_CHECKS_V1','activity':'RA-CAAAC604CB513AEA8BBC1DFC',
      'status':'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED','kernel':kernel,
      'examples':results,'deterministic_verification':checks,'actual_BRC_calls':len(CALLS),'core_call_receipts':CALLS,
      'negative_controls':['hide_unresolved_rejected'],
      'scope':'Seeded or fixed policies; actual original CF path; no hybrid and no empirical randomness/large-input-performance claim'}
    raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
    (ROOT/'CF_UNIVERSAL_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    brief={k:v for k,v in out.items() if k not in ('examples','core_call_receipts')}
    brief['examples']=[{k:r[k] for k in ('N','status','prime_factors','unresolved','probability_contract')} for r in results]
    brief['full_payload_sha256']=hashlib.sha256(raw).hexdigest()
    (ROOT/'CF_UNIVERSAL_SUMMARY.json').write_text(json.dumps(brief,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'complete':5,'partial':3,'calls':len(CALLS),'negative_controls':1}),flush=True)

if __name__=='__main__':main()
