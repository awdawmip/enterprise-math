"""Declared N107 fixture: one actual BRC history, then separate order audit.

No order, factor, eigenvalue, ideal law, or reference QFT is supplied to the
simulation. Specifying k selects a possible-history replay, not random sampling.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter_ns

ROOT=Path(__file__).resolve().parent
for directory in ('phases','integration','sparse','completion'):
    sys.path.insert(0,str(ROOT.parent/directory))
from closed_phase_bank import load_certified_bank
from general_streaming import GeneralStreamingProgram
from sparse_modular import sparse_modular_columns,sparse_modular_power_trace
from typed_integer_prechecks import wilson_primality,verify_precheck
from stage80.fixed_phase import norm
from stage79.phase_compiler import encode
from stage45.brc_loop_recheck import CALLS,verify_vendor

def packed(value):
    return json.dumps(encode(value),sort_keys=True,separators=(',',':')).encode()

def write_compressed(path,value):
    raw=packed(value);temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_bytes(gzip.compress(raw,mtime=0));temporary.replace(path)
    return hashlib.sha256(raw).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--activity',required=True)
    args=ap.parse_args();start=perf_counter_ns();vendor=verify_vendor();initial_calls=len(CALLS)
    N,a,t,k=107,2,14,1
    bank,intervals,dim,phase_certificate=load_certified_bank(t,cutoff=33,
      expected_payload_sha256='feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c')
    program=GeneralStreamingProgram(N,a,t,bank,dim,column_factory=sparse_modular_columns)
    state,den=program.initial();history=();events=[]
    B=2*t+128*sum(t-m+1 for m in range(3,min(t,32)+1))
    for i in range(t):
        before=norm(state,den)
        children=program.branches(state,den,history)
        masses=[norm(s,d) for s,d in children]
        assert sum(masses)==before
        bit=(k>>i)&1
        assert masses[bit]>0
        state,den=children[bit];history+=(bit,)
        assert den>0 and den&(den-1)==0
        assert ((1<<B)%den)==0
        events.append({'round':i,'selected':bit,'parent_mass':before,
          'child_masses':masses,'selected_conditional_probability':masses[bit]/before,
          'selected_mass':masses[bit],'selected_endpoints':len(state),
          'amplitude_denominator_exponent':den.bit_length()-1})
        if (i+1)%4==0 or i+1==t:
            checkpoint={'schema':'BRC_SUPPORT_HISTORY_CHECKPOINT_V1',
              'activity':args.activity,'N':N,'a':a,'t':t,'declared_target_k':k,
              'history':history,'next_round':i+1,'den':den,
              'state':[[list(key),row] for key,row in sorted(state.items())],
              'events':events,'phase_certificate':phase_certificate,
              'scope':'raw unnormalized possible history, no order audit yet'}
            write_compressed(ROOT/'high_degree_checkpoint.json.gz',checkpoint)
            print('retained checkpoint',i+1,'endpoints',len(state),'denominator bits',den.bit_length(),flush=True)
    assert sum(bit<<i for i,bit in enumerate(history))==k
    assert all(x==0 and spectator==0 for x,w,spectator in state)
    terminal_mass=norm(state,den)
    assert terminal_mass>=F(1,1<<(2*B))
    terminal={'N':N,'a':a,'t':t,'k':k,'dim':dim,'den':den,
      'state':[[list(key),row] for key,row in sorted(state.items())]}
    terminal_sha=write_compressed(ROOT/'high_degree_terminal_state.json.gz',terminal)
    # ORDER AUDIT IS DELIBERATELY AFTER THE COMPLETE INSTRUMENT REPLAY.
    history_finished_ns=perf_counter_ns()-start
    powers={exponent:sparse_modular_power_trace(N,a,exponent) for exponent in (106,1,2,53)}
    assert powers[106]['value']==1
    assert all(powers[e]['value']!=1 for e in (1,2,53))
    prime_certificates={number:wilson_primality(number) for number in (53,107)}
    for number,certificate in prime_certificates.items():
        assert certificate['status']=='PRIME'
        verify_precheck(certificate)
    # 106=2*53; the proper divisors 1,2,53 exhaust its divisors by the
    # separately certified primality of 53. Thus the post-hoc order is 106.
    assert 106==2*53 and 53-1==52 and 52>32
    audit={'schema':'BRC_HIGH_DEGREE_POSTHOC_ORDER_AUDIT_V1','activity':args.activity,
      'N':N,'a':a,'verified_order':106,'odd_part':53,'odd_part_totient':52,
      'power_traces':powers,'primality_certificates':prime_certificates,
      'order_prime_factorization':[2,53],
      'proper_divisors_checked':[1,2,53],
      'scope':'post-run fixture theorem premise only, never supplied to instrument'}
    audit_sha=write_compressed(ROOT/'high_degree_order_audit.json.gz',audit)
    report={'schema':'BRC_HIGH_DEGREE_SUPPORT_FIXTURE_V1','activity':args.activity,
      'status':'AUTHOR_EXECUTED_SINGLE_DECLARED_HISTORY_NOT_FULL_SUPPORT_ENUMERATION',
      'N':N,'a':a,'t':t,'Q':1<<t,'Q_ge_N_squared':(1<<t)>=N*N,
      'declared_k':k,'history':history,'internal_dimension':dim,
      'common_rational_active_dimension_upper_bound':32,
      'terminal_mass':terminal_mass,'positive_terminal_mass':terminal_mass>0,
      'terminal_amplitude_denominator_exponent':den.bit_length()-1,
      'terminal_denominator_divides_two_to_B':True,'B':B,
      'probability_lower_bound_exponent':2*B,
      'proved_lower_bound_checked':terminal_mass>=F(1,1<<(2*B)),
      'retained_residual_mode_mass':F(sum(v*v for row in state.values() for v in row[2:]),den*den),
      'complete_state_sha256':terminal_sha,'posthoc_audit_sha256':audit_sha,
      'posthoc_verified_order':106,'posthoc_odd_part_totient':52,
      'order_supplied_to_simulator':False,'factor_supplied_to_simulator':False,
      'classical_reference_run':False,'full_control_expansion_run':False,
      'random_sample_claimed':False,'all_histories_empirically_checked':False,
      'phase_certificate':phase_certificate,'events':events,'metrics':program.report_metrics(),
      'vendor':vendor,'actual_BRC_core_calls':len(CALLS)-initial_calls,
      'call_receipts':CALLS[initial_calls:],
      'execution_sequence':['complete declared possible history','persist complete raw terminal state',
        'audit order using actual sparse BRC powers','certify 53 and 107 prime using actual typed BRC Wilson'],
      'history_finished_elapsed_ns':history_finished_ns,'elapsed_ns':perf_counter_ns()-start,
      'claim_scope':'actual one-history example satisfying the independently proved phi(d)>32 premise; prime input chosen to isolate support, not to exhibit a nontrivial factor'}
    report_sha=write_compressed(ROOT/'high_degree_support.json.gz',report)
    summary={key:value for key,value in report.items() if key not in
      ('terminal_mass','retained_residual_mode_mass','events','call_receipts','metrics')}
    summary['full_report_sha256']=report_sha
    summary['peak_endpoints']=program.metrics['peak_endpoints']
    summary['peak_scalar_slots']=program.metrics['peak_scalar_slots']
    summary['residual_mass_positive']=report['retained_residual_mode_mass']>0
    (ROOT/'HIGH_DEGREE_SUPPORT_SUMMARY.json').write_text(json.dumps(encode(summary),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(encode(summary),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
