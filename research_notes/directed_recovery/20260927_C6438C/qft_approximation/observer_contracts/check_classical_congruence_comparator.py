"""Charge a classical factoring comparator for the same structured inputs.

Factors below are outputs, never construction inputs. This is a comparison
of arithmetic usefulness, not a simulation of the target QFT output law.
"""
from pathlib import Path
import gzip
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'characters'))
from power_sum_certificate import certify_power_sum_structure, verify_power_sum_structure
from lazy_modular import Arithmetic, require, digest
from stage45.brc_loop_recheck import CALLS


def scan(certificate,budget):
    require(type(budget) is int and budget>=0,'nonnegative declared budget required')
    verified=verify_power_sum_structure(certificate)
    require(verified['status']=='CERTIFIED_TWO_PART_LOWER_BOUND','verified input witness required')
    N,ell=certificate['N'],certificate['ell']
    m=1<<ell
    arithmetic=Arithmetic()
    candidate,initial_add=arithmetic.add(m,1)
    steps=[]
    status='PARTIAL_BUDGET'
    factors=None
    for _ in range(budget):
        square,square_op=arithmetic.multiply(candidate,candidate)
        relation,_,compare_op=arithmetic.compare(square,N)
        if relation>0:
            status='COMPLETE_NO_NONTRIVIAL_FACTOR'
            steps.append({'candidate':candidate,'square_operation':square_op,'compare_operation':compare_op,'beyond_sqrt':True})
            break
        quotient,remainder,division=arithmetic.divide(N,candidate)
        steps.append({'candidate':candidate,'square_operation':square_op,'compare_operation':compare_op,
                      'quotient':quotient,'remainder':remainder,'division_operation':division})
        if not remainder:
            product,check=arithmetic.multiply(candidate,quotient)
            require(product==N and 1<candidate<N and 1<quotient<N,'invalid output factor pair')
            steps[-1]['factor_product_operation']=check
            status='FACTOR_FOUND'
            factors=(candidate,quotient)
            break
        candidate,addition=arithmetic.add(candidate,m)
        steps[-1]['next_candidate_addition']=addition
    return {'N':N,'ell':ell,'modulus_stride':m,'budget':budget,'status':status,'factors':factors,
            'verified_witness':verified,'initial_candidate_addition':initial_add,'steps':steps,
            'candidate_divisions':sum('division_operation' in x for x in steps),
            'arithmetic_operations':arithmetic.operations,'cost':{k:v for k,v in arithmetic.stats.items() if k!='native_kernel_calls_delta'},
            'factor_order_or_primality_input':False,'QFT_law_simulation_claimed':False}


def main():
    files=[Path(__file__),ROOT.parent/'characters/power_sum_certificate.py']
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    first=len(CALLS)
    cases=[]
    for N,a,ell,u,v in ((65,3,2,8,1),(4097,3,3,8,1),(4294967297,3,6,2,1)):
        certificate=certify_power_sum_structure(N,a,ell,u,v)
        result=scan(certificate,32)
        require(result['status']=='FACTOR_FOUND','declared bounded comparison did not finish')
        cases.append({'structure_certificate':certificate,'comparator':result})
    partial=scan(cases[2]['structure_certificate'],1)
    require(partial['status']=='PARTIAL_BUDGET' and partial['factors'] is None,'budget must not assert a result')
    require(before=={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'source changed')
    payload={'activity':'RA-CAAAC604CB513AEA8BBC1DFC','status':'AUTHOR_BOUNDED_CLASSICAL_COMPARATOR_NOT_ADMITTED',
             'cases':cases,'partial_budget_check':partial,'source_sha256':before,'actual_core_calls':CALLS[first:],
             'scope':'typed witness-driven trial division; not a new factoring complexity claim or QFT sampler'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    artifact=ROOT/'CLASSICAL_COMPARATOR_RESULTS.json.gz'
    artifact.write_bytes(gzip.compress(raw,mtime=0))
    summary={'status':payload['status'],'cases':[{k:x['comparator'][k] for k in ('N','ell','status','factors','candidate_divisions','cost')} for x in cases],
             'actual_core_calls':len(CALLS)-first,'payload_sha256':hashlib.sha256(raw).hexdigest(),
             'gzip_sha256':hashlib.sha256(artifact.read_bytes()).hexdigest()}
    (ROOT/'CLASSICAL_COMPARATOR_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
