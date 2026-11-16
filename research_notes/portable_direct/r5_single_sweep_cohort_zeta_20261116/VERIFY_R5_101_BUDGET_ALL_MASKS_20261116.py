#!/usr/bin/env python3
"""Independent 256-mask x 101-budget comparison against the single-sweep certificate."""
import hashlib, json, subprocess, sys, time
from pathlib import Path
from R5_PATH_REQUIREMENT_DP_20261116 import frozen, masked_cost_count

HERE=Path(__file__).resolve().parent

def run():
    report=json.loads(subprocess.check_output([sys.executable,str(HERE/'R5_ALL_BUDGET_COHORT_SWEEP_20261116.py')],cwd=HERE))
    raw=json.dumps(report['per_budget'],sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
    sha=hashlib.sha256(raw).hexdigest()
    expected='9cc63ca013a1652219245c42c554cd2bb23b87ee19b54a8cf9b1477b6dd2bd49'
    assert sha==expected,(sha,expected)
    x,cuts=frozen();ks=tuple(range(214,315));signatures=set();begun=time.perf_counter();tests=0
    minbits=999;maxbits=0
    start=int(sys.argv[1]) if len(sys.argv)>1 else 0
    stop=int(sys.argv[2]) if len(sys.argv)>2 else 256
    assert 0<=start<stop<=256
    for mask in range(start,stop):
        direct=masked_cost_count(x,cuts,mask,ks)
        for k,(cost,count) in direct.items():
            point=report['per_budget'][str(k)]
            cohort_sum=sum(int(v) for req,v in point['exact_cohorts'].items() if int(req)&mask==int(req))
            assert (cost,count)==(point['cost'],cohort_sum),(mask,k)
            tests+=1
        signatures.add(tuple(direct[k][1] for k in (214,223,294)))
        total_bits=sum(direct[k][1].bit_length() for k in (214,291,294))
        minbits=min(minbits,total_bits);maxbits=max(maxbits,total_bits)
    assert tests==(stop-start)*101 and len(signatures)==stop-start
    if start==0 and stop==256: assert (minbits,maxbits)==(298,305)
    print(json.dumps({'status':'PASS_R5_101_BUDGET_256_MASK_DIRECT_EXACT',
                      'budget_range':[214,314], 'budgets':101,'mask_interval':[start,stop], 'masks':stop-start,
                      'verified_scalar_cost_count_pairs':tests,'mismatches':0,
                      'three_count_signatures':len(signatures),
                      'raw_bit_range_214_291_294':[minbits,maxbits],
                      'per_budget_canonical_sha256':sha,
                      'direct_comparison_elapsed_s':round(time.perf_counter()-begun,3)},indent=2,sort_keys=True))

if __name__=='__main__':run()
