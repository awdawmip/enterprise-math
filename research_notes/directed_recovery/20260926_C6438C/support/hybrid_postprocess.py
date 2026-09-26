"""Explicit AFTER-readout low-odd-part returning-exponent enhancement.

The public inputs are N,a,t,k only. The unknown order is never an input and
this module does not prepare a state, choose a base or synthesize a readout.
"""
from __future__ import annotations
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'sparse'))
sys.path.insert(0,str(ROOT.parent/'completion'))
from sparse_modular import (sparse_classical_postprocess,sparse_modular_power_brc,
    sparse_modular_power_trace,compile_modular_permutation,verify_modular_certificate,
    integer,digest,gcd_brc)
from typed_integer_prechecks import add,compare,divide

ODD_PART_MAX=1023

def gcd_receipt(left,right):
    """Execute existing actual BRC gcd; retain a typed long-division replay."""
    native=gcd_brc(left,right)
    a,b=left,right;steps=[]
    while b:
        quotient,remainder,trace=divide(a,b)
        steps.append({'left':a,'right':b,'division':trace})
        a,b=b,remainder
    if a!=native:raise AssertionError('native gcd differs from typed Euclidean replay')
    return native,{'entrypoint':'stage78.shor_benchmark.gcd_brc',
      'left':left,'right':right,'value':native,'typed_divisions':steps}

def _proper_factors(N,values):
    factors=[];checks=[]
    for factor in sorted(set(values)):
        lower,lowtrace=compare(factor,1);upper,uptrace=compare(factor,N)
        check={'candidate_factor':factor,'greater_than_one':lowtrace,'less_than_N':uptrace}
        if lower>0 and upper<0:
            quotient,remainder,division=divide(N,factor)
            check.update(division=division,proper_factor=(remainder==0))
            if remainder:raise AssertionError('gcd output is not an exact divisor')
            factors.append(factor)
        else:check['proper_factor']=False
        checks.append(check)
    return factors,checks

def _candidate_contract(N):
    return {'N':N,'odd_part_max':ODD_PART_MAX,'u_min':1,
      'u_max':(N-1).bit_length(),'q_rule':'q = d << u, odd d in 1..1023, q < N',
      'ordering':'increasing u, then increasing odd d',
      'construction':'public finite integer labels and bit wiring; typed q<N comparison',
      'omitted_odd_exponents':'odd q cannot enter the unchanged half-exponent gcd route',
      'not_order_input':True,'minimal_order_claimed':False}

def hybrid_classical_postprocess(N,a,t,k):
    """Run original CF first; after failure test all declared even candidates.

    The caller supplies a completed readout. Zero readout also enters fallback.
    A successful primary result keeps every original field, with added source
    and primary/fallback records. Failure also keeps the primary status; the
    hybrid record explicitly reports whether its full candidate list exhausted.
    """
    if not integer(N) or N<2 or not integer(a) or not 1<=a<N:
        raise ValueError('integer N>=2 and 1<=a<N required')
    if not integer(t) or t<2 or t%2 or not integer(k) or not 0<=k<(1<<t):
        raise ValueError('completed readout 0<=k<2^t and even t>=2 required')
    coprime,coprime_trace=gcd_receipt(a,N)
    if coprime!=1:raise ValueError('coprime base required; caller handles nonunit gcd precheck')
    primary=sparse_classical_postprocess(N,a,t,k)
    contract=_candidate_contract(N)
    hybrid={'schema':'BRC_LOW_ODD_PART_POSTPROCESS_V1','N':N,'a':a,'t':t,'k':k,
      'candidate_contract':contract,'coprimality':coprime_trace,
      'execution_position':'after completed actual readout and primary CF',
      'attempts':[],'excluded_frontiers':[],'coverage_complete':False,
      'minimal_order_claimed':False}
    result={**primary,'primary_postprocessing':primary,'hybrid':hybrid}
    if primary['factors']:
        factors,checks=_proper_factors(N,primary['factors'])
        if factors!=primary['factors']:raise AssertionError('primary returned nonproper factors')
        result['factor_source']='ORIGINAL_CF'
        hybrid.update(status='NOT_RUN_PRIMARY_SUCCEEDED',primary_factor_validation=checks)
        return result

    for u in range(1,contract['u_max']+1):
        for d in range(1,ODD_PART_MAX+1,2):
            q=d<<u  # exact fixed-label bit wiring; no unknown order computation
            relation,bound_trace=compare(q,N)
            if relation>=0:
                # q increases strictly with d at this fixed u, certifying the
                # unvisited remainder of the odd-d range lies outside q<N.
                hybrid['excluded_frontiers'].append({'u':u,'first_excluded_d':d,
                  'first_excluded_q':q,'bound_comparison':bound_trace,
                  'reason':'q>=N and all later d at this u are larger'})
                break
            returning=sparse_modular_power_brc(N,a,q)
            row={'u':u,'d':d,'q':q,'candidate_bound':bound_trace,
              'returning_power':sparse_modular_power_trace(N,a,q),
              'minimal_order_claimed':False}
            hybrid['attempts'].append(row)
            if returning!=1:
                row['status']='NOT_RETURNING_EXPONENT';continue
            half=q>>1;h=sparse_modular_power_brc(N,a,half)
            relation,minus_trace=compare(h,1)
            if relation<0:raise AssertionError('unit modular power cannot be below one')
            minus=minus_trace['low_difference'];plus,plus_trace=add(h,1)
            left,left_trace=gcd_receipt(minus,N);right,right_trace=gcd_receipt(plus,N)
            factors,checks=_proper_factors(N,[left,right])
            row.update(verified_returning_exponent=q,half_exponent=half,
              half_power=None)
            row['half_power']=sparse_modular_power_trace(N,a,half)
            row['half_minus_one']=minus_trace;row['half_plus_one']=plus_trace
            row['gcds']=[left_trace,right_trace];row['factor_validation']=checks
            if factors:
                row['status']='FACTORS'
                hybrid.update(status='FALLBACK_FACTOR_FOUND',stopped_after_success=True,
                  verified_returning_exponent=q)
                result.update(status='FACTORS',factors=factors,
                  verified_returning_exponent=q,minimal_order_claimed=False,
                  factor_source='LOW_ODD_PART_RETURNING_EXPONENT_FALLBACK')
                return result
            row['status']='TRIVIAL_GCD_RETRY'
    hybrid.update(status='CANDIDATES_EXHAUSTED_NO_FACTOR',coverage_complete=True,
      stopped_after_success=False)
    result['factor_source']=None
    return result

def verify_hybrid_postprocess(result):
    """Deterministically replay all actual typed arithmetic and source records."""
    record=result['hybrid']
    rebuilt=hybrid_classical_postprocess(record['N'],record['a'],record['t'],record['k'])
    if digest(rebuilt)!=digest(result):raise ValueError('hybrid postprocess record does not replay')
    return {'verified':True,'result_sha256':digest(result),
      'candidate_attempts':len(record['attempts']),'coverage_complete':record['coverage_complete'],
      'scope':'post-readout arithmetic only; does not certify how k was sampled'}

def modular_source_certificates(result):
    """Resolve every modular table referenced by the primary/fallback record."""
    record=result['hybrid'];N,a=record['N'],record['a'];powers=[]
    primary=result['primary_postprocessing']
    for q,reason in primary.get('rejected',[]):
        powers.append(sparse_modular_power_trace(N,a,q))
        if reason=='TRIVIAL_GCD_RETRY':powers.append(sparse_modular_power_trace(N,a,q>>1))
    if 'verified_returning_exponent' in primary:
        q=primary['verified_returning_exponent']
        powers.extend([sparse_modular_power_trace(N,a,q),sparse_modular_power_trace(N,a,q>>1)])
    for row in record['attempts']:
        powers.append(row['returning_power'])
        if 'half_power' in row:powers.append(row['half_power'])
    certificates={}
    for power_trace in powers:
        for step in power_trace['steps']:
            _,certificate=compile_modular_permutation(N,step['b'])
            key=digest(certificate)
            if key!=step['certificate_sha256']:raise AssertionError('modular source identity differs')
            verify_modular_certificate(certificate);certificates[key]=certificate
    return certificates
