"""Concrete postprocessor checks and fixed-grid theorem threshold certificates.

No ideal QFT, probability reference, new phase bank, order search, or factor
search is executed. The numerical theorem thresholds are observed through
positive path products of the frozen actual BRC kernel. Input k values are
declared postprocessor test fixtures, not sampled observations.
"""
import argparse
import json
import os
import sys
from fractions import Fraction as F
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--source', default=os.environ.get('BRC_STAGE87_SOURCE'))
p.add_argument('--output', default=str(Path(__file__).with_name('COMPLETION_CHECKS.json')))
args = p.parse_args()
if not args.source:
    p.error('--source or BRC_STAGE87_SOURCE is required')
sys.path.insert(0, str(Path(args.source).resolve()))
from stage45.brc_loop_recheck import core_power, verify_vendor, CALLS
from stage78.shor_benchmark import classical_postprocess

vendor = verify_vendor()


def path_product(*weights):
    graph = [[F(0) for _ in range(len(weights) + 1)]
             for _ in range(len(weights) + 1)]
    for i, weight in enumerate(weights):
        graph[i][i + 1] = F(weight)
    return core_power(tuple(map(tuple, graph)), len(weights))[0][-1]


def threshold(coefficient, strict):
    # L_(2n)=(2n-1)(n-1); n>=2. The product is increasing in n.
    rows = []
    def accepts(n):
        t = 2*n
        L = (t-1)*(t-2)//2
        observed = path_product(coefficient, n, L)
        accepted = observed < 2**32 if strict else observed <= 2**32
        rows.append({'n': n, 't': t, 'L_t': L,
                     'observed_brc_product': str(observed),
                     'rhs': str(2**32), 'accepted': accepted})
        return accepted
    lo, hi = 2, 2048
    assert accepts(lo) and not accepts(hi)
    while hi-lo > 1:
        mid=(lo+hi)//2
        if accepts(mid): lo=mid
        else: hi=mid
    assert accepts(lo) and not accepts(hi)
    return {'coefficient': coefficient, 'strict': strict,
            'max_n_under_this_bound': lo, 'first_n_not_certified': hi,
            'observations': rows}


fixtures = [
    (15,2,8,64, [3,5], 'coprime numerator recovers r=4'),
    (21,2,10,171,[3,7], 'coprime numerator near 1/6'),
    (21,2,10,853,[3,7], 'coprime numerator near 5/6'),
    (21,2,10,341,[], 'noncoprime numerator near 2/6 reduces denominator'),
    (21,2,10,512,[], 'noncoprime numerator 3/6 reduces denominator'),
    (9,2,8,43,[], 'odd prime power even returning exponent cannot split'),
    (25,2,10,51,[], 'odd prime square even returning exponent cannot split'),
    (15,14,4,8,[], 'bad base minus one'),
]
results = []
for N,a,t,k,expected,note in fixtures:
    result=classical_postprocess(N,a,t,k)
    assert result['factors']==expected, (N,a,t,k,result)
    results.append({'input':{'N':N,'a':a,'t':t,'k':k},
                    'declared_fixture': True, 'note':note,'result':result})

all_k_9 = [classical_postprocess(9,2,8,k) for k in range(2**8)]
assert all(not result['factors'] for result in all_k_9)
all_k_bad = [classical_postprocess(15,14,4,k) for k in range(2**4)]
assert all(not result['factors'] for result in all_k_bad)

out = {
    'status':'AUTHOR_EXECUTED / UNREVIEWED / NOT_ADMITTED',
    'researcher':'EM-DIRECT-C6438C',
    'activity':'RA-CAAAC604CB513AEA8BBC1DFC',
    'registration_source':'f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf',
    'frozen_source':'0852cad130c1d877174d235687cf60c19f318c58',
    'vendor_verification':vendor,
    'fixed_grid':{'target_bits':32,'vector_bits':64,
                  'assumed_general_phase_theorem':'E_t <= 8 L_t / 2^32',
                  'not_new_bank_execution':True},
    'retry_bound_threshold':threshold(128,False),
    'strictly_positive_bound_threshold':threshold(64,True),
    'postprocess_fixtures':results,
    'exhaustive_postprocess_only':[
        {'N':9,'a':2,'t':8,'readouts_checked':256,'all_factors_empty':True,
         'results':all_k_9},
        {'N':15,'a':14,'t':4,'readouts_checked':16,'all_factors_empty':True,
         'results':all_k_bad}],
    'native_calls':CALLS,
    'no_ideal_reference_execution':True,
    'no_order_or_factor_search':True,
}
Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({'output':str(Path(args.output).resolve()),
                  'retry_max_n':out['retry_bound_threshold']['max_n_under_this_bound'],
                  'positive_max_n':out['strictly_positive_bound_threshold']['max_n_under_this_bound'],
                  'postprocess_fixture_count':len(results),
                  'exhaustive_readout_count':272,'native_call_count':len(CALLS)},default=str))
