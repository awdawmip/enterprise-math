"""Bind actual completed samples to the new complete/partial hybrid driver."""
from pathlib import Path
import gzip, hashlib, json, random
from universal_factorization import factor_integer_universal, verify_factorization
from stage45.brc_loop_recheck import CALLS, verify_vendor
ROOT=Path(__file__).resolve().parent


class ZeroReadout:
    """Declared replay policy; no empirical uniform-randomness claim."""
    def randrange(self,*args):
        return args[0] if len(args)==2 else 0


def main():
    kernel=verify_vendor();examples=[];checks=[]
    for number, expected in [(15,[(3,1),(5,1)]),(21,[(3,1),(7,1)]),
            (35,[(5,1),(7,1)]),(225,[(3,2),(5,2)])]:
        result=factor_integer_universal(number,ZeroReadout(),failure_bits=2,
            max_attempts=1,base_provider=lambda N:[2])
        assert result['status']=='COMPLETE'
        assert [(p['prime'],p['exponent']) for p in result['prime_factors']]==expected
        split=[e for e in result['events'] if e['action']=='SAMPLED_SHOR_SPLIT']
        assert split
        for event in split:
            sampled=event['attempt_result']['attempts'][0]
            assert sampled['k']==0
            post=sampled['postprocessing']
            assert post['primary_postprocessing']['status']=='ZERO_PHASE_RETRY'
            assert post['factor_source']!='ORIGINAL_CF' and post['factors']
            assert event['universal_support_certificate']['all_completed_readouts_including_zero']
        examples.append(result);checks.append(verify_factorization(result))
        print(json.dumps({'N':number,'result':expected,'completed_zero_readout_retained':True}),flush=True)
    bad=factor_integer_universal(15,ZeroReadout(),failure_bits=2,
        max_attempts=1,base_provider=lambda N:[14])
    assert bad['status']=='PARTIAL' and bad['unresolved'][0]['cofactor']==15
    examples.append(bad);checks.append(verify_factorization(bad))
    # Default budget is actually selected, but the zero policy is still a
    # declared test policy. This does not validate an external randomness law.
    budgeted=factor_integer_universal(15,ZeroReadout(),failure_bits=2)
    assert budgeted['status']=='COMPLETE'
    assert budgeted['probability_contract']['budgets_meet_uniform_random_bound']
    examples.append(budgeted);checks.append(verify_factorization(budgeted))
    class Empty:
        def randrange(self,*args): raise EOFError
    incomplete=factor_integer_universal(21,Empty(),failure_bits=2,max_attempts=1,base_provider=lambda N:[2])
    assert incomplete['status']=='PARTIAL'
    event=next(e for e in incomplete['events'] if e['action']=='SAMPLED_SHOR_SPLIT')
    assert event['attempt_result']['status']=='INCOMPLETE_RANDOM_SOURCE'
    assert 'postprocessing' not in event['attempt_result']['attempts'][0]
    examples.append(incomplete);checks.append(verify_factorization(incomplete))
    out={'schema':'UNIVERSAL_HYBRID_FACTOR_INTEGRATION_CHECKS_V1',
        'activity':'RA-CAAAC604CB513AEA8BBC1DFC','status':'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED',
        'kernel':kernel,'examples':examples,'deterministic_result_verification':checks,
        'actual_BRC_calls':len(CALLS),'core_call_receipts':CALLS,
        'no_order_or_factor_input_to_simulation':True,
        'scope':'Actual complete zero-history samples then new postprocessing; fixed replay policies are not uniform sampling evidence'}
    raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
    (ROOT/'UNIVERSAL_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    brief={k:v for k,v in out.items() if k not in ('examples','core_call_receipts')}
    brief['examples']=[{k:r[k] for k in ('N','status','prime_factors','unresolved','probability_contract')} for r in examples]
    brief['full_payload_sha256']=hashlib.sha256(raw).hexdigest()
    (ROOT/'UNIVERSAL_SUMMARY.json').write_text(json.dumps(brief,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'complete':5,'partial':2,'actual_BRC_calls':len(CALLS)}),flush=True)


if __name__=='__main__':main()
