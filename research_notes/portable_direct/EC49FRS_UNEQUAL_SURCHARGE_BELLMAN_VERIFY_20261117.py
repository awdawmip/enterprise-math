#!/usr/bin/env python3
"""EC49FRS: exact unrestricted original-BRC all-228-query Bellman
for independently surcharged terminal q32 and q34.

Run after extracting the inherited original BRC EC49FRR full evidence archive:
  python code/EC49FRS_UNEQUAL_SURCHARGE_BELLMAN_VERIFY_20261117.py evidence/result.json

The script resides in the archive's code/ directory, next to
EC49FRQ_INDEPENDENT_ALL228.py and EC49FQI_NATIVE_DATA.py.
The frozen source files reside in source/. Arithmetic is exact integer.
"""
from pathlib import Path
import sys,json,hashlib,time
from functools import cache
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
sys.path.insert(0,str(HERE))
from EC49FRQ_INDEPENDENT_ALL228 import (
    OBS,PARTS,ALL,representatives,multiplicities,subset_keys
)
from EC49FQI_NATIVE_DATA import V,PIN,MASTER,CSV,keys,weights,reps
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((BASE/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((BASE/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(OBS)==len(V)==228 and representatives==reps and multiplicities==weights
assert all(OBS[q]==V[q] for q in range(144))
assert len(keys)==len(subset_keys)==84 and set(keys)==set(subset_keys)
assert all(OBS[144+j]==V[144+keys.index(k)] for j,k in enumerate(subset_keys))

def bellman(A,B):
    """Surcharge a=A/141, b=B/141, A and B nonnegative integers.

    Integer objective is 141 times aggregate path cost on all 141 states.
    Baseline physical observation cost=141; q32 costs 141+A, q34 141+B.
    """
    assert A>=0 and B>=0
    @cache
    def opt(mask):
        if mask.bit_count()==1:
            return 0,()
        best=10**30
        first=[]
        for q,partition in enumerate(PARTS):
            children=[mask & sub for sub in partition if mask & sub]
            if len(children)<2:
                continue
            c=(141+A if q==32 else (141+B if q==34 else 141))
            cost=c*mask.bit_count()+sum(opt(child)[0] for child in children)
            if cost<best:
                best=cost
                first=[q]
            elif cost==best:
                first.append(q)
        return best,tuple(first)
    start=time.monotonic()
    val,first=opt(ALL)
    prediction=141*(296+min(A,B,2))
    assert val==prediction,(A,B,val,prediction)
    original_first=[q if q<144 else
                    144+keys.index(subset_keys[q-144]) for q in first]
    return {
        'A':A,'B':B,'a':f'{A}/141','b':f'{B}/141',
        'integer_objective_141_times_sum_over_141_named_state_path_costs':val,
        'predicted_integer_objective':prediction,
        'all_optimal_first_original_physical_query_ids':original_first,
        'reachable_bellman_subsets':opt.cache_info().currsize,
        'elapsed_seconds':round(time.monotonic()-start,3)
    }

def main():
    tests=[(1,3),(2,5),(3,5),(1,1),(5,1),(5,2),(5,5)]
    expected_first=[
        [32],[32,140,142],[140,142],[32,34],
        [34],[34,140,142],[140,142]
    ]
    cases=[]
    for pair,expected in zip(tests,expected_first):
        result=bellman(*pair)
        assert result['all_optimal_first_original_physical_query_ids']==expected
        assert result['reachable_bellman_subsets']==13063
        cases.append(result)
        print('PASS',pair,result['integer_objective_141_times_sum_over_141_named_state_path_costs'],
              expected,flush=True)
    cert={
        'schema':'EC49FRS_EXACT_UNEQUAL_NAMED_BRC_SURCHARGE_V1',
        'frozen_scientific_pin':PIN,
        'master_sha256':MASTER,'profile_sha256':CSV,
        'original_named_states':141,'configurations':310,
        'original_physical_queries':228,
        'two_native_raw_reconstructions_align_for_all_228_named_query_responses':True,
        'integer_surcharge_denominator':141,
        'cases':cases,
        'analytic_theorem':'V(a,b)/t=min(296/141+a,296/141+b,298/141), a,b>=0',
        'status':'AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED'
    }
    output=Path(sys.argv[1]) if len(sys.argv)>1 else BASE/'evidence/EC49FRS_UNEQUAL_SURCHARGE_CERTIFICATE_20261117.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print('ALL SEVEN CASES PASS',output)
if __name__=='__main__':
    main()
