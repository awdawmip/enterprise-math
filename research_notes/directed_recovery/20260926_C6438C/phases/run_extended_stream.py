"""One standard-width N=35 streaming history using the actual extended bank."""
from pathlib import Path
import argparse,gzip,hashlib,json,random,sys
from fractions import Fraction as F
from time import perf_counter_ns
from closed_phase_bank import ROOT,SOURCE,PREVIOUS,error_certificate,truncated_error_certificate,truncated_tail_bank
sys.path.insert(0,str(ROOT.parent/'integration'));sys.path.insert(0,str(ROOT.parent/'sparse'))
sys.path.insert(0,str(PREVIOUS/'driver'))
from general_streaming import GeneralStreamingProgram
from sparse_modular import sparse_modular_columns,sparse_classical_postprocess
from general_driver import sample_once
from stage80.fixed_phase import FixedRotor,QuarterTurn,norm
from stage79.phase_compiler import encode
from stage45.brc_loop_recheck import CALLS,verify_vendor

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--activity',required=True);args=ap.parse_args()
    begin=perf_counter_ns();vendor=verify_vendor();start_calls=len(CALLS)
    raw=gzip.decompress((ROOT/'bank_t34.json.gz').read_bytes());saved=json.loads(raw)
    dim=saved['internal_dimension'];bank={2:QuarterTurn(dim)}
    for m in range(3,35):
        record=saved['phase_gates'][str(m)]
        rotor=FixedRotor(record['integer_unit_vector'],record['bits'],record)
        assert json.loads(json.dumps(rotor.inverse_phase_word))==record['fixed_inverse_phase_word']
        bank[m]=rotor
    intv={int(m):{k:F(v) for k,v in r.items()} for m,r in saved['phase_intervals'].items()}
    program=GeneralStreamingProgram(35,2,12,bank,dim,column_factory=sparse_modular_columns)
    result=sample_once(program,random.Random(20260926))
    assert len(result['history'])==12
    assert len(result['events'])==12
    assert all(e['endpoints']<=64 for e in result['events'])
    assert 35*35<=1<<12
    report={'schema':'BRC_SHOR_EXTENDED_BANK_STANDARD_WIDTH_STREAM_V1',
      'activity':args.activity,'status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED',
      'bank_payload_sha256':hashlib.sha256(raw).hexdigest(),'bank_max_m':34,
      'actual_used_phase_max_m':12,'internal_dimension':dim,
      'used_phase_complete_columns_reexecuted':sum(b.full_columns_checked for m,b in bank.items() if 3<=m<=12),
      'all_bank_complete_columns_reexecuted':sum(b.full_columns_checked for m,b in bank.items() if m>=3),
      'phase_error_certificate':error_certificate(12,intv),
      'N':35,'a':2,'t':12,'Q':4096,'Q_ge_N_squared':True,
      'full_control_expansion_run':False,'reference_QFT_run':False,
      'input_has_order_or_factors':False,'higher_precision':False,
      'modular_column_compiler':'explicit injection sparse_modular_columns; all W labels retained',
      'retained_residual_modes':dim-2,'shared_spectator_boundary_reset_used':False,
      'random_source':'seeded software PRNG demonstration, not a physical or ideal randomness certificate',
      'result':result,'metrics':program.report_metrics(),'vendor':vendor,
      'actual_BRC_core_calls':len(CALLS)-start_calls,'call_receipts':CALLS[start_calls:],
      'elapsed_ns':perf_counter_ns()-begin}
    (ROOT/'stream_t12.json').write_text(json.dumps(encode(report),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(encode({k:report[k] for k in ('N','a','t','internal_dimension','actual_BRC_core_calls','elapsed_ns')})),flush=True)
    print('k',result['k'],'post',result['postprocessing'],'peak',report['metrics']['peak_endpoints'],flush=True)
    replay=GeneralStreamingProgram(35,2,12,bank,dim,column_factory=sparse_modular_columns)
    state,den=replay.initial();history=();events=[]
    for i in range(12):
        before=norm(state,den);children=replay.branches(state,den,history)
        masses=[norm(s,d) for s,d in children]
        assert sum(masses)==before
        bit=(341>>i)&1
        assert masses[bit]>0
        state,den=children[bit];history+=(bit,)
        events.append({'round':i,'bit':bit,'conditional_probability':masses[bit]/before,
          'unconditional_history_mass':masses[bit]})
    post=sparse_classical_postprocess(35,2,12,341)
    assert post['factors']==[5,7]
    forced={'schema':'BRC_SHOR_POSSIBLE_HISTORY_REPLAY_V1','activity':args.activity,
      'N':35,'a':2,'t':12,'k':341,'history':history,'events':events,
      'history_probability':norm(state,den),'postprocessing':post,
      'semantics':'specified positive-mass history, not an unbiased sample or observed success frequency',
      'bank_payload_sha256':hashlib.sha256(raw).hexdigest(),'metrics':replay.report_metrics()}
    (ROOT/'stream_k341.json').write_text(json.dumps(encode(forced),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('possible k341',post,'peak',replay.metrics['peak_endpoints'],flush=True)
    identity_bank=truncated_tail_bank(bank,40)
    identity=identity_bank[34]
    checks=0
    for j in range(dim):
        vector=[int(i==j) for i in range(dim)]
        assert identity.apply_numer(vector)==vector
        assert identity.apply_numer(vector,True)==vector
        checks+=1
    nonzero_tail=tuple(range(-30,31));assert len(nonzero_tail)==dim
    assert identity.apply_numer(nonzero_tail)==list(nonzero_tail)
    # At the first extended width compare finite-sum and closed tail formulas.
    delta=F(1,1<<32)
    for t in range(34,81):
        explicit=sum((F(2*delta*(t-m+1),1<<(m-34)) for m in range(34,t+1)),F(0))
        assert explicit==truncated_error_certificate(t,intv)['ideal_tail_error']
    tail_report={'schema':'BRC_SHOR_FIXED_GRID_IDENTITY_TAIL_V1','activity':args.activity,
      'status':'AUTHOR_PROVED_AND_LOCAL_GATE_CHECKED_NOT_FULL_TAIL_CIRCUIT_EXECUTED',
      'identity_complete_basis_columns_checked':checks,'nonzero_residual_input_preserved':True,
      'finite_sum_identity_checks':47,'identity_empty_word':True,
      'frozen_bank_replaced':False,'higher_precision':False,
      'error_examples':[truncated_error_certificate(t,intv) for t in (12,34,40,64,100,1000,2000)]}
    (ROOT/'identity_tail.json').write_text(json.dumps(encode(tail_report),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
