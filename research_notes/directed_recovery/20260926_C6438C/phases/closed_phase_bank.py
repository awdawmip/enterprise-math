"""Fixed target32/vector64 BRC phase-bank extension, with honest error budgets.

Reuses the frozen complete-word compiler. The only root-interface extension is
the already proved p=0 endpoint; no trig, new reference, or increased precision.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, os, sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from time import perf_counter_ns

ROOT=Path(__file__).resolve().parent
SOURCE=Path(os.environ.get('BRC_STAGE87_SOURCE','D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source')).resolve()
PREVIOUS=Path(os.environ.get('BRC_SHOR_ALTERNATIVE','D:/em/TEMP/sep26-shor-alternative')).resolve()
sys.path.insert(0,str(SOURCE));sys.path.insert(0,str(PREVIOUS/'adversarial'))
from stage45.brc_loop_recheck import CALLS,verify_vendor
from stage79.phase_compiler import encode,polynomial_probe
from stage80.fixed_phase import FixedRotor,QuarterTurn,unit_vector
from zero_endpoint_extension import closed_dyadic_parameters,closed_root_bracket

TARGET_BITS=32
VECTOR_BITS=64
STATIONARY_M=34
SOURCE_HEAD='0852cad130c1d877174d235687cf60c19f318c58'

def fixed_grid_intervals(max_m):
    if isinstance(max_m,bool) or not isinstance(max_m,int) or max_m<2:
        raise ValueError('max_m must be an integer >=2')
    intervals=closed_dyadic_parameters(min(max_m,STATIONARY_M),TARGET_BITS)
    if max_m>=STATIONARY_M:
        delta=F(1,1<<TARGET_BITS)
        assert intervals[STATIONARY_M]['lower']==0
        assert intervals[STATIONARY_M]['upper']==delta
        # Actual same-grid endpoint observers certify a fixed interval forever.
        assert closed_root_bracket(F(0),TARGET_BITS)==(F(0),F(0))
        assert closed_root_bracket(delta,TARGET_BITS)==(F(0),delta)
        assert polynomial_probe(delta,F(0))==-delta
        assert polynomial_probe(delta,delta)==delta+delta**3
        for m in range(STATIONARY_M+1,max_m+1):
            intervals[m]=dict(intervals[STATIONARY_M])
    return intervals

def error_certificate(t,intervals):
    """Whole extended-space operator and every common terminal TV bound.

    The arithmetic here is the proved telescoping observer of actual certified
    words and same-grid BRC endpoints, not a new scientific propagator.
    """
    if isinstance(t,bool) or not isinstance(t,int) or t<2:
        raise ValueError('integer t>=2 required')
    if any(m not in intervals for m in range(2,min(t,STATIONARY_M)+1)):
        raise ValueError('missing actual interval certificates')
    target=sum(((t-m+1)*intervals[m]['gate_error']
                for m in range(2,min(t,STATIONARY_M)+1)),F(0))
    if t>STATIONARY_M:
        if intervals[STATIONARY_M]['gate_error']!=F(1,1<<TARGET_BITS):
            raise ValueError('stationary interval not certified')
        target+=F((t-STATIONARY_M)*(t-STATIONARY_M+1),2<<TARGET_BITS)
    count=(t-1)*(t-2)//2
    dilation=F(4*count,1<<(VECTOR_BITS//2))
    return {'t':t,'target_bits':TARGET_BITS,'vector_bits':VECTOR_BITS,
      'phase_target':target,'fixed_word_dilation':dilation,
      'telescoping_sum':target+dilation,
      'operator_norm_bound':min(F(2),target+dilation),
      'terminal_TV_bound':min(F(1),target+dilation),
      'nonexact_phase_occurrences':count,
      'scope':'full retained internal space and common terminal instrument; no per-history relative-error claim'}

def compile_closed_bank(max_m,progress=None):
    """Return bank,intervals,dim,report; never assumes D=61 for new vectors."""
    intervals=fixed_grid_intervals(max_m)
    saved=json.loads((SOURCE/'stage80'/'RESULTS.json').read_text(encoding='utf-8'))
    assert saved['target_parameter_bits']==TARGET_BITS and saved['unit_vector_bits']==VECTOR_BITS
    raw={};reused=[];new=[]
    for m in range(3,min(max_m,STATIONARY_M)+1):
        if str(m) in saved['phase_gates']:
            cert=saved['phase_gates'][str(m)]
            old_interval={k:F(v) for k,v in saved['target_intervals'][str(m)].items()}
            assert old_interval==intervals[m]
            z=tuple(cert['integer_unit_vector']);reused.append(m)
        else:
            z,cert=unit_vector(intervals[m]['parameter'],VECTOR_BITS);new.append(m)
        raw[m]=(z,cert)
    dim=max([saved['internal_real_mode_count']]+[len(z) for z,c in raw.values()])
    bank={2:QuarterTurn(dim)};reports={};unique={}
    for m,(z,cert) in raw.items():
        padded=(*z,*([0]*(dim-len(z))))
        key=tuple(padded)
        if key not in unique:
            unique[key]=FixedRotor(padded,VECTOR_BITS,cert)
        rotor=unique[key];bank[m]=rotor
        if m in reused:
            old=saved['phase_gates'][str(m)]
            assert tuple(rotor.z[:len(old['integer_unit_vector'])])==tuple(old['integer_unit_vector'])
            assert not any(rotor.z[len(old['integer_unit_vector']):])
            # Padding leaves G unchanged; D0's extra signs cancel exactly.
            assert json.loads(json.dumps(rotor.word))==old['word_to_basis']
        reports[m]=rotor.report()
        if progress:progress(m,dim,rotor.full_columns_checked)
    for m in range(STATIONARY_M+1,max_m+1):
        bank[m]=bank[STATIONARY_M]
    certificate=error_certificate(max_m,intervals)
    phase_resources={name:sum((max_m-m+1)*getattr(bank[m],name)
      for m in range(3,max_m+1)) for name in ('h4_count','sign_count','swap_count')}
    report={'schema':'BRC_SHOR_CLOSED_FIXED_GRID_BANK_V1',
      'source_head':SOURCE_HEAD,'max_m':max_m,'target_bits':TARGET_BITS,
      'vector_bits':VECTOR_BITS,'internal_dimension':dim,
      'frozen_dimensions_padded_losslessly':True,'frozen_phase_reused':reused,
      'new_vector_phases':new,'stationary_phase_from':STATIONARY_M,
      'distinct_fixed_words_executed':len(unique),
      'actual_complete_columns_executed':sum(r.full_columns_checked for r in unique.values()),
      'every_certified_column_has_full_inverse_recovery':True,
      'phase_intervals':intervals,'phase_gates':reports,'error_certificate':certificate,
      'ordered_phase_word_resource_counts':phase_resources,
      'quarter_turn_occurrences':max_m-1,
      'streaming_two_H4_per_control_round':2*max_m,
      'streaming_macro_amplitude_denominator_exponent_bound':2*max_m+2*VECTOR_BITS*((max_m-1)*(max_m-2)//2),
      'raw_word_amplitude_denominator_exponent_bound':2*max_m+phase_resources['h4_count'],
      'resource_exclusions':['modular permutation compilation/application','integer bit operation costs','sampling rejection randomness','physical spatial layout'],
      'arithmetic':'ACTUAL_TYPED_BRC_ONLY','higher_precision':False,
      'ordinary_reference_execution':False,'all_residual_modes_retained':True}
    return bank,intervals,dim,report

def tolerance_frontier(intervals,tolerance=F(1,10**6)):
    if tolerance<=0:raise ValueError('positive tolerance required')
    last=2;next_t=4
    while error_certificate(next_t,intervals)['telescoping_sum']<=tolerance:
        last=next_t;next_t+=2
    return {'tolerance':tolerance,'max_even_t_certified_by_this_bound':last,
      'at_max':error_certificate(last,intervals),
      'next_even_t':error_certificate(next_t,intervals),
      'interpretation':'failure of this sufficient bound is not measured actual error and does not reject a run'}

class IdentityTail:
    """The empty exact native word on the ENTIRE retained carrier."""
    def __init__(self,dim):
        self.dim=dim;self.den=1
        self.h4_count=self.sign_count=self.swap_count=0
        self.inverse_phase_word=()
    def apply_numer(self,v,inverse=False):
        if len(v)!=self.dim:raise ValueError('complete carrier required')
        return list(v)

def truncated_tail_bank(bank,max_m,cutoff=34):
    if not isinstance(cutoff,int) or isinstance(cutoff,bool) or not 3<=cutoff<=34:
        raise ValueError('cutoff must have an actually certified fixed-grid endpoint 3..34')
    dim=bank[2].dim;out=dict(bank);identity=IdentityTail(dim)
    if any(m not in bank for m in range(2,min(max_m,cutoff-1)+1)):
        raise ValueError('missing retained actual phase prefix')
    for m in range(cutoff,max_m+1):out[m]=identity
    return out

def truncated_error_certificate(t,intervals,cutoff=34):
    """Explicit changed algorithm: omit entire small tail gates, never modes.

    For the ideal algebraic half-angle branch, 2*r_next<=r_previous. The
    ACTUAL grid certificate r34<=delta implies ideal tail gate error at most
    2*delta*2^(-(m-34)) for using the entire-space identity at phase m.
    """
    if isinstance(t,bool) or not isinstance(t,int) or t<2:raise ValueError('integer t>=2')
    if not isinstance(cutoff,int) or isinstance(cutoff,bool) or not 3<=cutoff<=34:
        raise ValueError('actual endpoint cutoff 3..34 required')
    top=min(t,cutoff-1);delta=F(1,1<<TARGET_BITS)
    prefix=sum(((t-m+1)*(intervals[m]['gate_error']+4*delta)
      for m in range(3,top+1)),F(0))
    if t<cutoff:tail=F(0)
    else:
        if cutoff not in intervals:raise ValueError('actual cutoff endpoint required')
        upper=intervals[cutoff]['upper']
        # Sum_{j=0}^{A-1} (A-j)/2^j = 2A-2+2^(1-A), A=t-cutoff+1.
        tail=4*upper*(t-cutoff)+F(4*upper,1<<(t-cutoff+1))
    total=prefix+tail
    return {'t':t,'target_bits':32,'vector_bits':64,'identity_tail_from_m':cutoff,
      'actual_word_prefix_error':prefix,'ideal_tail_error':tail,
      'telescoping_sum':total,'operator_norm_bound':min(F(2),total),
      'terminal_TV_bound':min(F(1),total),
      'all_residual_modes_retained':True,
      'scope':'changed terminal algorithm with full-D identity tail; not exact equality with the original closed bank'}

def optimize_tail_certificate(t,intervals):
    candidates=[truncated_error_certificate(t,intervals,k) for k in range(3,35)]
    chosen=min(candidates,key=lambda c:(c['telescoping_sum'],-c['identity_tail_from_m']))
    return {'chosen':chosen,'candidate_certificates':candidates,
      'selection_inputs':'t and same-grid certified phase upper endpoints only; no N,a,order,factor or outcomes',
      'execution_status':'proof-level selection; concrete program needs the matching cutoff bank'}

@lru_cache(maxsize=2)
def _reconstruct_certified_payload(payload):
    verify_vendor()
    saved=json.loads(payload)
    if saved['source_head']!=SOURCE_HEAD or saved['target_bits']!=32 or saved['vector_bits']!=64:
        raise ValueError('unexpected frozen compiler identity or precision')
    if saved['max_m']<34:raise ValueError('complete deep endpoint bank required')
    dim=saved['internal_dimension'];bank={2:QuarterTurn(dim)}
    for m in range(3,35):
        record=saved['phase_gates'][str(m)]
        if len(record['integer_unit_vector'])!=dim:raise ValueError('inconsistent carrier')
        rotor=FixedRotor(record['integer_unit_vector'],record['bits'],record)
        if json.loads(json.dumps(rotor.inverse_phase_word))!=record['fixed_inverse_phase_word']:
            raise ValueError('reconstructed complete native word differs')
        if rotor.full_columns_checked!=dim:raise ValueError('missing full-column verification')
        bank[m]=rotor
    intervals={int(m):{k:F(v) for k,v in record.items()}
      for m,record in saved['phase_intervals'].items()}
    if intervals[34]['lower']!=0 or intervals[34]['upper']!=F(1,1<<32):
        raise ValueError('stationary endpoint evidence differs')
    return bank,intervals,dim

def load_certified_bank(max_m,path=None,*,cutoff=None,expected_payload_sha256=None):
    """Read actual bank evidence, reexecute all words once, then use a copy.

    Endpoint probes are not repeated. Each distinct payload is cached only
    after full-column/inverse word execution. A matching cutoff is included in
    the returned certificate, so a caller cannot silently mix its error budget.
    """
    if not isinstance(max_m,int) or isinstance(max_m,bool) or max_m<2:
        raise ValueError('integer max_m>=2 required')
    payload=gzip.decompress(Path(path or ROOT/'bank_t34.json.gz').read_bytes())
    digest=hashlib.sha256(payload).hexdigest()
    if expected_payload_sha256 is not None and digest!=expected_payload_sha256:
        raise ValueError('bank artifact checksum differs')
    original,base_intervals,dim=_reconstruct_certified_payload(payload)
    bank={m:original[min(m,34)] for m in range(2,max_m+1)}
    intervals={m:dict(base_intervals[min(m,34)]) for m in range(2,max_m+1)}
    if cutoff is not None:
        bank=truncated_tail_bank(bank,max_m,cutoff)
        certificate=truncated_error_certificate(max_m,base_intervals,cutoff)
    else:certificate=error_certificate(max_m,base_intervals)
    return bank,intervals,dim,{'bank_payload_sha256':digest,'identity_tail_from_m':cutoff,
      'error_certificate':certificate,'complete_column_verification_on_cache_fill':32*dim,
      'whole_inverse_words_recovered':True,'endpoint_probes_repeated':False,
      'status':'ACTUAL_WORD_REPLAY_OR_SAME_PAYLOAD_VERIFIED_CACHE'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--max-m',type=int,default=34)
    ap.add_argument('--activity',required=True);ap.add_argument('--out',default=str(ROOT))
    args=ap.parse_args();out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    began=perf_counter_ns();vendor=verify_vendor();initial=len(CALLS)
    bank,intv,dim,report=compile_closed_bank(args.max_m,lambda m,d,c:print('phase',m,'D',d,'full columns',c,flush=True))
    report.update(activity=args.activity,status='AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED',vendor=vendor,
      actual_BRC_core_calls=len(CALLS)-initial,call_receipts=CALLS[initial:],elapsed_ns=perf_counter_ns()-began)
    if args.max_m>=34:
        report['accuracy_frontier']=tolerance_frontier(intv)
        report['error_examples']=[error_certificate(t,intv) for t in (12,34,40,64,100,1000)]
    raw=json.dumps(encode(report),ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    (out/f'bank_t{args.max_m}.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    brief={k:v for k,v in report.items() if k not in ('phase_gates','call_receipts','phase_intervals')}
    brief['full_payload_sha256']=hashlib.sha256(raw).hexdigest()
    brief['phase_extreme_certificates']={m:{k:report['phase_gates'][m][k] for k in
      ('dimension','all_columns_tested','H4_count','sign_count','swap_count','q','p0','p1','remainder')}
      for m in (33,34) if m in report['phase_gates']}
    (out/f'summary_t{args.max_m}.json').write_text(json.dumps(encode(brief),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(encode(brief),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
