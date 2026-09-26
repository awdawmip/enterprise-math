"""Exercise the first identity-tail occurrence on a retained positive history."""
from pathlib import Path
import argparse,gzip,hashlib,json,sys
from fractions import Fraction as F
from time import perf_counter_ns
from closed_phase_bank import ROOT,PREVIOUS,truncated_tail_bank,truncated_error_certificate
sys.path.insert(0,str(ROOT.parent/'integration'));sys.path.insert(0,str(ROOT.parent/'sparse'))
from general_streaming import GeneralStreamingProgram
from sparse_modular import sparse_modular_columns
from stage80.fixed_phase import FixedRotor,QuarterTurn,norm
from stage79.phase_compiler import encode
from stage45.brc_loop_recheck import CALLS,verify_vendor

def replay(bank,dim):
    program=GeneralStreamingProgram(21,2,34,bank,dim,column_factory=sparse_modular_columns)
    state,den=program.initial();history=();trace=[]
    for i in range(34):
        children=program.branches(state,den,history)
        masses=[norm(s,d) for s,d in children]
        assert sum(masses)==norm(state,den)
        bit=int(i==0)
        assert masses[bit]>0
        state,den=children[bit];history+=(bit,)
        trace.append({'round':i,'selected':bit,'mass':masses[bit],
          'endpoints':len(state),'denominator_bits':den.bit_length()})
    assert history[0]==1 and len(history)==34
    assert all(h==0 for x,w,h in state)
    assert program.depth_metrics[33,'CP_34']['calls']==1
    state_raw=json.dumps(encode({'state':[[list(k),v] for k,v in sorted(state.items())],'den':den}),separators=(',',':')).encode()
    return {'history':history,'mass':norm(state,den),'trace':trace,
      'metrics':program.report_metrics(),'state_sha256':hashlib.sha256(state_raw).hexdigest(),
      'retained_mode_mass':F(sum(v*v for row in state.values() for v in row[2:]),den*den)},state_raw

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--activity',required=True)
    ap.add_argument('--cutoff',type=int,default=34);args=ap.parse_args()
    begin=perf_counter_ns();vendor=verify_vendor();start=len(CALLS)
    raw=gzip.decompress((ROOT/'bank_t34.json.gz').read_bytes());saved=json.loads(raw);dim=saved['internal_dimension']
    bank={2:QuarterTurn(dim)}
    for m in range(3,35):
        r=saved['phase_gates'][str(m)];bank[m]=FixedRotor(r['integer_unit_vector'],r['bits'],r)
    intv={int(m):{k:F(v) for k,v in r.items()} for m,r in saved['phase_intervals'].items()}
    old,oldstate=replay(bank,dim);print('closed bank history complete',flush=True)
    tail,newstate=replay(truncated_tail_bank(bank,34,args.cutoff),dim);print('identity tail history complete',flush=True)
    difference=abs(old['mass']-tail['mass'])
    assert old['state_sha256']!=tail['state_sha256']
    # Word34 versus I is bounded via their common ideal algebraic phase.
    local_bound=sum(((35-m)*(intv[m]['gate_error']+F(4,1<<32)+
      F(2*intv[args.cutoff]['upper'],1<<(m-args.cutoff))) for m in range(args.cutoff,35)),F(0))
    assert difference<=local_bound
    report={'schema':'BRC_SHOR_FIRST_IDENTITY_TAIL_HISTORY_V1','activity':args.activity,
      'status':'AUTHOR_EXECUTED_SINGLE_POSSIBLE_HISTORY_NOT_FULL_LAW_VERIFICATION',
      'N':21,'a':2,'t':34,'k':1,'dim':dim,'identity_tail_from_m':args.cutoff,
      'tail_occurrence_actual_history_control_one':True,
      'full_control_expansion_run':False,'precision_changed':False,
      'old_closed_bank':old,'new_identity_tail':tail,
      'probability_difference':difference,'common_reference_triangle_bound':local_bound,
      'ideal_TV_certificate':truncated_error_certificate(34,intv,args.cutoff),
      'bank_payload_sha256':hashlib.sha256(raw).hexdigest(),'vendor':vendor,
      'actual_BRC_core_calls':len(CALLS)-start,'call_receipts':CALLS[start:],
      'elapsed_ns':perf_counter_ns()-begin,
      'observation_scope':'same preselected possible k=1 prefix; not a sample or overall success frequency'}
    payload=json.dumps(encode(report),sort_keys=True,separators=(',',':')).encode()
    suffix='' if args.cutoff==34 else '_cutoff'+str(args.cutoff)
    (ROOT/f'tail_t34_history{suffix}.json.gz').write_bytes(gzip.compress(payload,mtime=0))
    (ROOT/'closed_t34_k1_state.json.gz').write_bytes(gzip.compress(oldstate,mtime=0))
    (ROOT/f'identity_t34_k1_state{suffix}.json.gz').write_bytes(gzip.compress(newstate,mtime=0))
    brief={k:v for k,v in report.items() if k not in ('old_closed_bank','new_identity_tail','probability_difference','call_receipts')}
    brief['report_sha256']=hashlib.sha256(payload).hexdigest()
    brief['different_retained_state']=True;brief['positive_mass_in_both']=True
    brief['old_peak_endpoints']=old['metrics']['peak_endpoints'];brief['new_peak_endpoints']=tail['metrics']['peak_endpoints']
    brief['old_final_denominator_bits']=old['trace'][-1]['denominator_bits']
    brief['new_final_denominator_bits']=tail['trace'][-1]['denominator_bits']
    (ROOT/f'tail_t34_summary{suffix}.json').write_text(json.dumps(encode(brief),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(encode(brief)),flush=True)

if __name__=='__main__':main()
