"""Check compiled phases in full factorization and preserve interrupted work."""
from pathlib import Path
from copy import deepcopy
import gzip,hashlib,json,random
from compiled_factorization import factor_integer_compiled,verify_factorization
from stage45.brc_loop_recheck import CALLS,verify_vendor
from stage79.phase_compiler import encode

ROOT=Path(__file__).resolve().parent

class ForbiddenRandom:
    def randrange(self,*args):
        raise AssertionError('Randomness consumed before compilation completed')

class Zero:
    def randrange(self,*args):
        return args[0] if len(args)==2 else 0


def main():
    kernel=verify_vendor()
    results=[]
    checks=[]
    # A perfect-power node reaches compilation as 15 with multiplicity two.
    # A zero budget must preserve 15^2=225 without requesting any random draw.
    partial=factor_integer_compiled(225,ForbiddenRandom(),compiler_pair_budget=0,
        failure_bits=2,max_attempts=12,base_provider=lambda N:[2]*12)
    assert partial['status']=='PARTIAL'
    assert [(r['cofactor'],r['multiplicity'],r['status']) for r in partial['unresolved']]==[(15,2,'COMPILATION_PARTIAL')]
    assert partial['multiplicative_ledger']['value']==225
    assert partial['probability_contract']['budgets_meet_uniform_random_bound'] is False
    results.append(partial);checks.append(verify_factorization(partial))
    print(json.dumps({'N':225,'status':'COMPILATION_PARTIAL','preserved':'15^2','random_draws':0}),flush=True)
    cursors=partial['native_word_compiler']['phase_cursors']
    resumed=factor_integer_compiled(225,random.Random(20260926+225),phase_cursors=cursors,
        compiler_pair_budget=32,failure_bits=2,max_attempts=12,
        base_provider=lambda N:[2]*12)
    assert resumed['status']=='COMPLETE'
    assert [(r['prime'],r['exponent']) for r in resumed['prime_factors']]==[(3,2),(5,2)]
    results.append(resumed);checks.append(verify_factorization(resumed))
    print(json.dumps({'N':225,'status':'COMPLETE','compiler_cursor_resumed':True}),flush=True)
    for N,expected in [(21,[(3,1),(7,1)])]:
        result=factor_integer_compiled(N,random.Random(20260926+N),compiler_pair_budget=32,
            failure_bits=2,max_attempts=12,base_provider=lambda value:[2]*12)
        assert result['status']=='COMPLETE'
        assert [(r['prime'],r['exponent']) for r in result['prime_factors']]==expected
        results.append(result);checks.append(verify_factorization(result))
        print(json.dumps({'N':N,'status':result['status'],'primes':expected}),flush=True)
    zero=factor_integer_compiled(21,Zero(),compiler_pair_budget=32,
        failure_bits=2,max_attempts=1,base_provider=lambda N:[2])
    assert zero['status']=='PARTIAL' and zero['unresolved'][0]['cofactor']==21
    event=next(e for e in zero['events'] if e['action']=='SAMPLED_SHOR_SPLIT')
    assert event['attempt_result']['attempts'][0]['postprocessing']['status']=='ZERO_PHASE_RETRY'
    results.append(zero);checks.append(verify_factorization(zero))
    print(json.dumps({'N':21,'status':'ZERO_PHASE_RETRY_PARTIAL'}),flush=True)
    for result in results:
        for e in result['events']:
            if e['action']=='SAMPLED_SHOR_SPLIT':
                n=(e['input']-1).bit_length()
                from fractions import Fraction as F
                assert F(e['per_attempt_success_lower_bound'])>=F(1,16*n)
                assert e['error_certificate']['all_residual_modes_retained']
    bad=deepcopy(partial);bad['status']='COMPLETE'
    try:verify_factorization(bad)
    except ValueError:pass
    else:raise AssertionError('Hidden compile interruption was accepted')
    out={'schema':'COMPILED_WORD_FULL_FACTORIZATION_CHECKS_V1',
      'activity':'RA-CAAAC604CB513AEA8BBC1DFC','kernel':kernel,
      'status':'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED',
      'results':results,'deterministic_verification':checks,
      'negative_controls':['hidden_compilation_partial_rejected'],
      'compiler_interruption_preserved_multiplicity':True,
      'compiler_resume_completed':True,'random_calls_before_partial_compilation':0,
      'actual_BRC_calls':len(CALLS),'native_call_receipts':CALLS,
      'scope':'Seeded/fixed-base actual original-CF samples and complete prime/product certificates; no empirical randomness, ideal-reference execution or polynomial-time claim'}
    raw=json.dumps(encode(out),sort_keys=True,separators=(',',':')).encode()
    (ROOT/'COMPILED_FACTORIZATION_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    summary={k:v for k,v in out.items() if k not in ('results','native_call_receipts')}
    summary['result_summaries']=[{k:r[k] for k in ('N','status','prime_factors','unresolved','probability_contract')} for r in results]
    summary['full_payload_sha256']=hashlib.sha256(raw).hexdigest()
    summary['uncompressed_bytes']=len(raw)
    (ROOT/'COMPILED_FACTORIZATION_SUMMARY.json').write_text(json.dumps(encode(summary),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'cases':len(results),'core_calls':len(CALLS),'payload_sha256':summary['full_payload_sha256']}),flush=True)

if __name__=='__main__':main()
